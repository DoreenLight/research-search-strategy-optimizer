from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from datetime import timezone, datetime
from email.utils import parsedate_to_datetime
import inspect
import json
import math
import os
from pathlib import Path
import re
import time
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, quote, quote_plus, unquote, unquote_plus, urlencode, urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

from .models import Paper
from .query_cache import CacheRequest, CacheWriteError, QueryCache


RequestFn = Callable[..., Any]
MAX_URL_BYTES = 4094
MAX_ABSTRACT_POSITION = 100_000
MAX_ABSTRACT_TOKENS = 100_000
MAX_ABSTRACT_BYTES = 1_000_000
RETRYABLE_STATUSES = frozenset({408, 429, 500, 502, 503, 504})


@dataclass
class OpenAlexSearchResult:
    status: str
    papers: list[Paper] = field(default_factory=list)
    total_count: int | None = None
    fetched_count: int = 0
    request_count: int = 0
    request_url: str | None = None
    error_type: str | None = None
    error_message: str | None = None
    raw_meta: dict[str, Any] = field(default_factory=dict)
    raw_response: dict[str, Any] | None = None
    attempts: list[dict[str, Any]] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    retrieved_at: str = ""
    cache_hit: bool = False
    metadata_bytes: int = 0
    cache_key: str | None = None


class _NoRedirectHandler(HTTPRedirectHandler):
    """Reject every redirect before urllib can forward an Authorization header."""

    def _reject(self, request, fp, code, msg, headers):
        raise HTTPError(request.full_url, code, msg, headers, fp)

    http_error_301 = _reject
    http_error_302 = _reject
    http_error_303 = _reject
    http_error_307 = _reject
    http_error_308 = _reject


_NO_REDIRECT_OPENER = build_opener(_NoRedirectHandler())


def _now(timestamp: float | None = None) -> str:
    if timestamp is None:
        return datetime.now(timezone.utc).isoformat()
    return datetime.fromtimestamp(timestamp, timezone.utc).isoformat()


def _contains_named_credential(value: Any, secrets: tuple[str, ...] = ()) -> bool:
    text = str(value)
    variants = {text}
    current = text
    for _ in range(3):
        current = unquote_plus(current)
        variants.add(current)
        current = unquote(current)
        variants.add(current)
    for secret in secrets:
        if secret:
            encoded = {secret, quote(secret, safe=""), quote_plus(secret)}
            if any(item in candidate for candidate in variants for item in encoded):
                return True
    return any(
        _is_sensitive_key(candidate.strip().split("=", 1)[0]) or
        re.search(r"(?i)\bbearer(?:\s|%20|\+)", candidate) or
        re.search(r"(?i)(?:api[_-]?key|access[_-]?token|authorization|client[_-]?secret)\s*(?:=|:)", candidate)
        for candidate in variants
    )


def _is_sensitive_key(key: str) -> bool:
    return re.sub(r"[^a-z0-9]", "", key.lower()) in {
        "apikey", "authorization", "accesstoken", "authtoken", "bearertoken",
        "clientsecret", "password", "privatekey", "refreshtoken", "secret", "token",
    }


def _redact_text(value: Any, secrets: tuple[str, ...] = ()) -> str:
    """Redact credentials, without truncating ordinary evidence or URL values."""
    text = str(value)
    for secret in secrets:
        if secret:
            for variant in {secret, quote(secret, safe=""), quote_plus(secret)}:
                # Percent-encoded octets are case-insensitive; other text is not.
                if "%" in variant:
                    pattern = "".join(
                        f"[{character.lower()}{character.upper()}]" if character.isalpha() else re.escape(character)
                        for character in variant
                    )
                    text = re.sub(pattern, "<redacted>", text)
                else:
                    text = text.replace(variant, "<redacted>")
    text = re.sub(
        r"(?i)(bearer(?:\s+|%20|\+))[^\s\"',;}&\]]+",
        r"\1<redacted>", text,
    )
    text = re.sub(
        r"(?i)([\"']?(?:api[_-]?key|access[_-]?token|authorization|client[_-]?secret|password|private[_-]?key|refresh[_-]?token|secret|token)[\"']?\s*(?:[=:]|%3d|%3a)\s*[\"']?)[^\s\"'&,;}\]]+",
        r"\1<redacted>", text,
    )
    return text


def _clean_error(value: Any, secrets: tuple[str, ...] = ()) -> str:
    return _redact_text(value, secrets)[:500]


def _contains_known_secret(value: Any, secrets: tuple[str, ...]) -> bool:
    if not secrets:
        return False
    if isinstance(value, Mapping):
        return any(_contains_known_secret(key, secrets) or _contains_known_secret(item, secrets)
                   for key, item in value.items())
    if isinstance(value, (list, tuple)):
        return any(_contains_known_secret(item, secrets) for item in value)
    if not isinstance(value, str):
        return False
    candidates = {value}
    for _ in range(3):
        decoded = {unquote_plus(item) for item in candidates}
        if decoded <= candidates:
            break
        candidates.update(decoded)
    variants = {secret for secret in secrets if secret}
    variants.update(quote(secret, safe="") for secret in secrets if secret)
    variants.update(quote_plus(secret) for secret in secrets if secret)
    return any(candidate == variant or variant in candidate for candidate in candidates for variant in variants)


def _contains_sensitive_marker(value: Any) -> bool:
    if isinstance(value, Mapping):
        return any(
            isinstance(key, str) and _is_sensitive_key(key)
            or _contains_sensitive_marker(key)
            or _contains_sensitive_marker(item)
            for key, item in value.items()
        )
    if isinstance(value, (list, tuple)):
        return any(_contains_sensitive_marker(item) for item in value)
    if not isinstance(value, str):
        return False
    candidates = {value}
    for _ in range(3):
        decoded = {unquote_plus(item) for item in candidates}
        if decoded <= candidates:
            break
        candidates.update(decoded)
    pattern = re.compile(
        r"(?i)(?:bearer(?:\\s+|%20|\\+)|(?:api[_-]?key|access[_-]?token|authorization|client[_-]?secret|password|private[_-]?key|refresh[_-]?token|secret|token)(?:\\s*|%20)*(?:=|%3d|:))"
    )
    return any(pattern.search(candidate) is not None for candidate in candidates)


def _redact_data(value: Any, secrets: tuple[str, ...]) -> Any:
    if isinstance(value, dict):
        result: dict[Any, Any] = {}
        for key, item in value.items():
            safe_key = _redact_text(key, secrets) if isinstance(key, str) else key
            # Offset arrays may legitimately use words such as "authorization".
            if isinstance(key, str) and _is_sensitive_key(key) and isinstance(item, str):
                result[safe_key] = "<redacted>"
            else:
                result[safe_key] = _redact_data(item, secrets)
        return result
    if isinstance(value, list):
        return [_redact_data(item, secrets) for item in value]
    if isinstance(value, str):
        return _redact_text(value, secrets)
    return value


def _abstract_from_inverted_index(
    index: Any, *, max_position: int, max_tokens: int, max_bytes: int,
) -> tuple[str | None, str | None]:
    if index is None or index == {}:
        return None, None
    if not isinstance(index, dict):
        return None, "abstract_inverted_index_invalid"
    if len(index) > max_tokens:
        return None, "abstract_inverted_index_too_large"
    positions: dict[int, str] = {}
    output_bytes = 0
    for token, offsets in index.items():
        if not isinstance(token, str) or not token.strip() or not isinstance(offsets, list):
            return None, "abstract_inverted_index_invalid"
        if len(offsets) + len(positions) > max_tokens:
            return None, "abstract_inverted_index_too_large"
        if len(token) > max_bytes:
            return None, "abstract_inverted_index_size_limit"
        try:
            token_bytes = len(token.encode("utf-8"))
        except UnicodeError:
            return None, "abstract_inverted_index_invalid"
        for offset in offsets:
            if type(offset) is not int or offset < 0:
                return None, "abstract_inverted_index_invalid_offset"
            if offset > max_position:
                return None, "abstract_inverted_index_position_limit"
            if offset in positions:
                return None, "abstract_inverted_index_collision"
            output_bytes += token_bytes + (1 if positions else 0)
            if output_bytes > max_bytes:
                return None, "abstract_inverted_index_size_limit"
            positions[offset] = token
    if not positions:
        return None, None
    if len(positions) != max(positions) + 1:
        return None, "abstract_inverted_index_gap"
    return " ".join(positions[position] for position in range(len(positions))), None


def _canonical_work_id(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    match = re.fullmatch(r"(?:https?://openalex\.org/)?(W[0-9]+)/?", value.strip(), re.IGNORECASE)
    return f"https://openalex.org/{match.group(1).upper()}" if match else None


def _work_shape_valid(work: dict[str, Any]) -> bool:
    for field_name in ("authorships", "keywords"):
        value = work.get(field_name)
        if value is not None and (not isinstance(value, list) or any(not isinstance(item, dict) for item in value)):
            return False
    for field_name in ("ids", "primary_location"):
        if work.get(field_name) is not None and not isinstance(work[field_name], dict):
            return False
    for authorship in work.get("authorships") or []:
        if authorship.get("author") is not None and not isinstance(authorship["author"], dict):
            return False
    location = work.get("primary_location") or {}
    return location.get("source") is None or isinstance(location["source"], dict)


def _paper_from_work(
    work: dict[str, Any], retrieved_at: str, *,
    max_abstract_position: int, max_abstract_tokens: int, max_abstract_bytes: int,
) -> tuple[Paper | None, list[str]]:
    warnings = []
    openalex_id = _canonical_work_id(work.get("id"))
    title = work.get("title")
    if openalex_id is None:
        warnings.append("work_missing_id" if not work.get("id") else "work_invalid_id")
    if not isinstance(title, str) or not title.strip():
        warnings.append("work_missing_title")
    if warnings:
        return None, warnings
    ids = work.get("ids") or {}
    doi = work.get("doi") or ids.get("doi")
    pmid = ids.get("pmid")
    if isinstance(pmid, str) and pmid:
        pmid = urlsplit(pmid).path.rstrip("/").rsplit("/", 1)[-1] or None
    else:
        pmid = None
    abstract, warning = _abstract_from_inverted_index(
        work.get("abstract_inverted_index"), max_position=max_abstract_position,
        max_tokens=max_abstract_tokens, max_bytes=max_abstract_bytes,
    )
    if warning:
        warnings.append(warning)
    authors = []
    for authorship in work.get("authorships") or []:
        name = (authorship.get("author") or {}).get("display_name")
        if isinstance(name, str) and name.strip():
            authors.append(name.strip())
    keywords = []
    for keyword in work.get("keywords") or []:
        name = keyword.get("display_name")
        if isinstance(name, str) and name.strip():
            keywords.append(name.strip())
    source = (work.get("primary_location") or {}).get("source") or {}
    source_title = source.get("display_name")
    year = work.get("publication_year")
    return Paper(
        paper_id=openalex_id, title=title.strip(), abstract=abstract, openalex_id=openalex_id,
        doi=doi if isinstance(doi, str) and doi else None, pmid=pmid,
        publication_year=year if type(year) is int else None, authors=authors,
        source_title=source_title.strip() if isinstance(source_title, str) and source_title.strip() else None,
        author_keywords=[], database_keywords=keywords, source_url=openalex_id, retrieved_at=retrieved_at,
    ), warnings


def _close_response(response: Any) -> None:
    close = getattr(response, "close", None)
    if callable(close):
        try:
            close()
        except Exception:
            pass  # Best effort cleanup must not mask the original result.


def _header_value(headers: Any, name: str) -> str | None:
    if headers is not None:
        try:
            for key, value in headers.items():
                if str(key).lower() == name.lower():
                    return str(value)
        except AttributeError:
            pass
    return None


def _timeout_error(error: BaseException) -> bool:
    reason = error.reason if isinstance(error, URLError) else error
    return isinstance(reason, TimeoutError) or "timed out" in str(reason).lower()


@dataclass
class _Response:
    status: int | None = None
    payload: Any = None
    error_type: str | None = None
    error_message: str | None = None
    retryable: bool = False
    headers: Any = None
    metadata_bytes: int = 0


class OpenAlexClient:
    """Standard-library Works GET client; max_requests is shared across this instance.

    request_fn is the legacy alias of transport. Injected transports receive a
    Request and may accept timeout=; they must not follow redirects themselves.
    clock is monotonic; wall_clock supplies Unix seconds for HTTP dates and logs.
    A synchronous custom transport must honor timeout= to be interruptible.
    """

    base_url = "https://api.openalex.org/works"

    def __init__(
        self, *, request_fn: RequestFn | None = None, transport: RequestFn | None = None,
        api_key: str | None = None, timeout: float = 20.0, total_timeout: float | None = None,
        max_retries: int = 2, max_requests: int | None = None, max_wait: float = 60.0,
        backoff_factor: float = 0.5, min_request_interval: float = 1.0,
        clock: Callable[[], float] | None = None, sleep: Callable[[float], None] | None = None,
        wall_clock: Callable[[], float] | None = None, cache_dir: Path | str | None = None,
        api_version: str = "works-v1",
        max_abstract_position: int = MAX_ABSTRACT_POSITION,
        max_abstract_tokens: int = MAX_ABSTRACT_TOKENS, max_abstract_bytes: int = MAX_ABSTRACT_BYTES,
    ) -> None:
        if request_fn is not None and transport is not None:
            raise ValueError("provide request_fn or transport, not both")
        for name, value, allow_zero in (
            ("timeout", timeout, False), ("max_wait", max_wait, True),
            ("backoff_factor", backoff_factor, True), ("min_request_interval", min_request_interval, True),
            ("total_timeout", total_timeout, False),
        ):
            if name == "total_timeout" and value is None:
                continue
            if type(value) not in (int, float) or not math.isfinite(value) or value < 0 or (value == 0 and not allow_zero):
                raise ValueError(f"{name} must be finite and {'non-negative' if allow_zero else 'positive'}")
        for name, value in (
            ("max_retries", max_retries), ("max_requests", max_requests),
            ("max_abstract_position", max_abstract_position), ("max_abstract_tokens", max_abstract_tokens),
            ("max_abstract_bytes", max_abstract_bytes),
        ):
            if name == "max_requests" and value is None:
                continue
            if type(value) is not int or value < 0:
                raise ValueError(f"{name} must be a non-negative integer")
        if api_key is not None and not isinstance(api_key, str):
            raise ValueError("api_key must be a string or None")
        if not isinstance(api_version, str) or not api_version:
            raise ValueError("api_version must be a non-empty string")
        self.request_fn = request_fn or transport or self._default_transport
        self.api_key = os.getenv("OPENALEX_API_KEY") if api_key is None else api_key
        self.timeout, self.total_timeout = float(timeout), total_timeout
        self.max_retries, self.max_requests = max_retries, max_requests
        self.max_wait, self.backoff_factor = float(max_wait), float(backoff_factor)
        self.min_request_interval = float(min_request_interval)
        self.clock, self.sleep = clock or time.monotonic, sleep or time.sleep
        self.wall_clock = wall_clock or time.time
        self.max_abstract_position = max_abstract_position
        self.max_abstract_tokens, self.max_abstract_bytes = max_abstract_tokens, max_abstract_bytes
        self.api_version = api_version
        self.cache = QueryCache(cache_dir, provider="openalex", api_version=api_version) if cache_dir is not None else None
        self._requests_made = 0
        self._last_request_at: float | None = None

    @staticmethod
    def _default_transport(request: Request, *, timeout: float) -> Any:
        return _NO_REDIRECT_OPENER.open(request, timeout=timeout)

    def _secrets(self) -> tuple[str, ...]:
        return (self.api_key,) if self.api_key else ()

    def _timestamp(self) -> str:
        return _now(self.wall_clock())

    def _safe_url(self, url: str) -> str:
        parts = urlsplit(url)
        params = [
            (_redact_text(key, self._secrets()), "<redacted>" if _is_sensitive_key(key) else _redact_text(value, self._secrets()))
            for key, value in parse_qsl(parts.query, keep_blank_values=True)
        ]
        return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(params), parts.fragment))

    def _call_transport(self, request: Request, timeout: float) -> Any:
        try:
            signature = inspect.signature(self.request_fn)
        except (TypeError, ValueError):
            return self.request_fn(request, timeout=timeout)
        parameters = signature.parameters.values()
        if any(parameter.kind == inspect.Parameter.VAR_KEYWORD or (
            parameter.name == "timeout" and parameter.kind != inspect.Parameter.POSITIONAL_ONLY
        ) for parameter in parameters):
            return self.request_fn(request, timeout=timeout)
        return self.request_fn(request)

    def _receive(self, request: Request, timeout: float) -> _Response:
        response = None
        status = None
        try:
            try:
                response = self._call_transport(request, timeout)
            except HTTPError as error:
                response = error
            status = getattr(response, "status", None)
            if status is None:
                getcode = getattr(response, "getcode", None)
                status = getcode() if callable(getcode) else 200
            if type(status) is not int or not 100 <= status <= 599:
                return _Response(error_type="invalid_response", error_message="invalid HTTP status")
            headers = getattr(response, "headers", None)
            body_error = None
            payload = None
            metadata_bytes = 0
            try:
                body = response.read()
                if not isinstance(body, (bytes, bytearray)):
                    raise TypeError("response body must be bytes")
                metadata_bytes = len(body)
                payload = json.loads(bytes(body).decode("utf-8"), parse_constant=lambda _: (_ for _ in ()).throw(ValueError("non-finite JSON number")))
            except (TypeError, ValueError, UnicodeError, RecursionError, OSError) as error:
                body_error = error
            if not 200 <= status < 300:
                message: Any = f"HTTP {status}"
                if isinstance(payload, dict):
                    message = payload.get("message") or payload.get("error") or payload.get("detail") or message
                return _Response(
                    status=status, payload=payload, error_type="http_error",
                    error_message=_clean_error(message, self._secrets()),
                    retryable=status in RETRYABLE_STATUSES, headers=headers,
                    metadata_bytes=metadata_bytes,
                )
            if body_error is not None:
                error_type = "timeout" if _timeout_error(body_error) else (
                    "transport_error" if isinstance(body_error, OSError) else "invalid_response"
                )
                return _Response(status=status, error_type=error_type, error_message=_clean_error(body_error, self._secrets()),
                                 retryable=error_type != "invalid_response", headers=headers,
                                 metadata_bytes=metadata_bytes)
            return _Response(status=status, payload=payload, headers=headers, metadata_bytes=metadata_bytes)
        except (URLError, TimeoutError, OSError) as error:
            return _Response(status=status, error_type="timeout" if _timeout_error(error) else "transport_error",
                             error_message=_clean_error(error, self._secrets()), retryable=True)
        except (TypeError, ValueError, UnicodeError, AttributeError, RecursionError) as error:
            return _Response(status=status, error_type="invalid_response", error_message=_clean_error(error, self._secrets()))
        finally:
            _close_response(response)

    def _remaining(self, started_at: float) -> float | None:
        return None if self.total_timeout is None else self.total_timeout - max(0.0, self.clock() - started_at)

    def _wait(self, delay: float, started_at: float) -> bool:
        remaining = self._remaining(started_at)
        if remaining is not None and (remaining <= 0 or delay >= remaining):
            return False
        if delay > 0:
            self.sleep(delay)
        remaining = self._remaining(started_at)
        return remaining is None or remaining > 0

    def _retry_delay(self, retry_number: int, headers: Any) -> float:
        value = _header_value(headers, "Retry-After")
        if value is not None:
            try:
                seconds = float(value.strip())
                if not math.isnan(seconds):
                    return min(self.max_wait, max(0.0, seconds))
            except (ValueError, OverflowError):
                try:
                    date = parsedate_to_datetime(value)
                    if date.tzinfo is None:
                        date = date.replace(tzinfo=timezone.utc)
                    return min(self.max_wait, max(0.0, date.timestamp() - self.wall_clock()))
                except (TypeError, ValueError, OverflowError, OSError):
                    pass
        return min(self.max_wait, self.backoff_factor * 2 ** min(retry_number - 1, 60))

    def parse_response(self, payload: dict[str, Any], retrieved_at: str) -> OpenAlexSearchResult:
        """Parse an offline replay without I/O, requests, sleeps, or budget usage.

        raw_response is a recursively redacted copy, not the caller's dictionary.
        The same method is used by search_works after a successful HTTP response.
        """
        result = OpenAlexSearchResult(status="failed", retrieved_at=retrieved_at)
        try:
            raw = _redact_data(payload, self._secrets())
            result.raw_response = raw if isinstance(raw, dict) else None
            meta = raw.get("meta") if isinstance(raw, dict) else None
            works = raw.get("results") if isinstance(raw, dict) else None
            result.raw_meta = meta if isinstance(meta, dict) else {}
            if (not isinstance(meta, dict) or not isinstance(works, list)
                    or any(not isinstance(work, dict) or not _work_shape_valid(work) for work in works)):
                result.error_type = "invalid_response"
                result.error_message = "OpenAlex response must contain meta object and valid results[]"
                result.warnings = ["invalid_response_shape"]
                return result
            count = meta.get("count")
            if count is not None and (type(count) is not int or count < 0):
                result.error_type = "invalid_response"
                result.error_message = "OpenAlex meta.count must be a non-negative integer when present"
                result.warnings = ["invalid_meta_count"]
                return result
            skipped = False
            for index, work in enumerate(works):
                paper, warnings = _paper_from_work(
                    work, retrieved_at, max_abstract_position=self.max_abstract_position,
                    max_abstract_tokens=self.max_abstract_tokens, max_abstract_bytes=self.max_abstract_bytes,
                )
                result.warnings.extend(f"result_{index}_{warning}" for warning in warnings)
                if paper is None:
                    skipped = True
                else:
                    result.papers.append(paper)
            result.status = "partial" if skipped else "success"
            result.total_count, result.fetched_count = count, len(result.papers)
            return result
        except (TypeError, ValueError, UnicodeError, AttributeError, RecursionError) as error:
            result.papers = []
            result.error_type = "invalid_response"
            result.error_message = _clean_error(error, self._secrets())
            return result

    def search_works(
        self, search: str, *, per_page: int = 25, cursor: str | None = None,
        filters: Mapping[str, Any] | None = None,
    ) -> OpenAlexSearchResult:
        if not isinstance(search, str) or not search.strip():
            raise ValueError("search must be a non-empty string")
        if type(per_page) is not int or not 1 <= per_page <= 100:
            raise ValueError("per_page must be between 1 and 100")
        if cursor is not None and not isinstance(cursor, str):
            raise ValueError("cursor must be a string or None")
        if filters is not None and not isinstance(filters, Mapping):
            raise ValueError("filters must be a mapping or None")
        params: dict[str, Any] = {"search": search, "per-page": per_page}
        if cursor is not None:
            params["cursor"] = cursor
        if filters:
            clauses = []
            for key, value in filters.items():
                if not isinstance(key, str) or not key:
                    raise ValueError("filter names must be non-empty strings")
                if value is not None:
                    clauses.append(f"{key}:{str(value).lower() if isinstance(value, bool) else value}")
            if clauses:
                params["filter"] = ",".join(clauses)
        started_at = self.clock()
        result = OpenAlexSearchResult(status="failed", retrieved_at=self._timestamp())
        cache_request = CacheRequest(
            provider="openalex", query=search, filters=dict(filters or {}), per_page=per_page,
            cursor=cursor, api_version=self.api_version,
        )
        cache_key: str | None = None
        cache_warning: str | None = None
        secrets = self._secrets()
        sensitive_request = _contains_named_credential(search, secrets) or _contains_named_credential(cursor or "", secrets) or _contains_named_credential(self.api_version, secrets)
        if filters:
            sensitive_request = sensitive_request or any(_contains_named_credential(key, secrets) or _contains_named_credential(value, secrets) for key, value in filters.items())
        if sensitive_request:
            cache_warning = "cache_bypassed_sensitive_request"
        if self.cache is not None and not sensitive_request:
            try:
                cache_key = self.cache.key(cache_request)
                cached = self.cache.load(cache_request)
            except (TypeError, ValueError, OverflowError, RecursionError):
                cache_warning = "cache_bypassed_invalid_parameters"
                cached = None
            if cached is not None:
                replayed = self.parse_response(cached["response"], cached["retrieved_at"])
                replayed.request_url = _redact_text(cached.get("request_metadata", {}).get("request_url"), self._secrets())
                if replayed.status not in {"success", "partial"}:
                    cached = None
                else:
                    replayed.cache_hit = True
                    replayed.cache_key = cache_key
                    replayed.warnings = [*replayed.warnings, "cache_hit"]
                    return replayed
        result.cache_key = cache_key
        if cache_warning:
            result.warnings.append(cache_warning)
        url = f"{self.base_url}?{urlencode(params)}"
        result.request_url = self._safe_url(url)
        if sensitive_request:
            result.request_url = "<redacted-url>"
        if len(url.encode("utf-8")) > MAX_URL_BYTES:
            result.error_type, result.error_message = "url_too_long", "request URL exceeds 4094 bytes; query was not sent or rewritten"
            return result
        headers = {"Accept": "application/json", "User-Agent": "research-search-strategy-optimizer/0.1"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        request = Request(url, headers=headers, method="GET")
        retry_delay = 0.0
        for attempt_number in range(self.max_retries + 1):
            if self.max_requests is not None and self._requests_made >= self.max_requests:
                result.error_type, result.error_message = "budget_exhausted", "max_requests budget exhausted"
                return result
            rate_delay = 0.0 if self._last_request_at is None else max(0.0, self.min_request_interval - (self.clock() - self._last_request_at))
            if not self._wait(max(rate_delay, retry_delay), started_at):
                result.error_type, result.error_message = "timeout", "total timeout exceeded or insufficient time for the next attempt"
                return result
            remaining = self._remaining(started_at)
            timeout = self.timeout if remaining is None else min(self.timeout, remaining)
            timestamp = self._timestamp()
            self._requests_made += 1
            self._last_request_at = self.clock()
            response = self._receive(request, timeout)
            result.metadata_bytes += response.metadata_bytes
            attempt = {"request_url": result.request_url, "timestamp": timestamp,
                       "status": response.status, "error_type": response.error_type}
            result.attempts.append(attempt)
            result.request_count += 1
            if isinstance(response.payload, dict):
                try:
                    result.raw_response = _redact_data(response.payload, self._secrets())
                except (TypeError, ValueError, RecursionError):
                    result.raw_response = None
            remaining = self._remaining(started_at)
            if remaining is not None and remaining <= 0:
                attempt["error_type"] = "timeout"
                result.error_type, result.error_message = "timeout", "total timeout exceeded"
                return result
            if response.error_type is None:
                parsed = self.parse_response(response.payload, result.retrieved_at)
                parsed.request_url, parsed.request_count, parsed.attempts = result.request_url, result.request_count, result.attempts
                parsed.metadata_bytes = result.metadata_bytes
                parsed.cache_key = result.cache_key
                parsed.warnings = [*result.warnings, *parsed.warnings]
                attempt["error_type"] = parsed.error_type
                remaining = self._remaining(started_at)
                if self.cache is not None and parsed.status in {"success", "partial"} and parsed.raw_response is not None and cache_warning is None and (remaining is None or remaining > 0):
                    try:
                        self.cache.store(
                            cache_request,
                            request_url=parsed.request_url,
                            retrieved_at=parsed.retrieved_at,
                            response=parsed.raw_response,
                        )
                    except (CacheWriteError, TypeError, ValueError, OSError, OverflowError, RecursionError) as error:
                        warning = "cache_write_failed"
                        if isinstance(error, CacheWriteError) and error.scratch_path is not None:
                            warning = f"cache_write_failed:{error.scratch_path}"
                        parsed.warnings.append(warning)
                if remaining is not None and remaining <= 0:
                    parsed.status, parsed.papers, parsed.fetched_count = "failed", [], 0
                    parsed.error_type, parsed.error_message = "timeout", "total timeout exceeded"
                    attempt["error_type"] = "timeout"
                return parsed
            result.error_type, result.error_message = response.error_type, response.error_message
            if not response.retryable or attempt_number >= self.max_retries:
                return result
            if self.max_requests is not None and self._requests_made >= self.max_requests:
                result.error_type, result.error_message = "budget_exhausted", "max_requests budget exhausted before retry"
                return result
            retry_delay = self._retry_delay(attempt_number + 1, response.headers)
        return result


def parse_response(payload: dict[str, Any], retrieved_at: str) -> OpenAlexSearchResult:
    """Public anonymous offline replay; use a client method to redact a known API key."""
    return OpenAlexClient(api_key="").parse_response(payload, retrieved_at)
