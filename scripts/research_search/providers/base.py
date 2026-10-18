"""Common protocol and stdlib helpers; there is deliberately no default transport."""
from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Callable, Mapping
from datetime import datetime, timezone
import inspect
import math
import re
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, quote_plus
from urllib.request import Request

from .models import ProviderResult, SearchRequest, _is_sensitive_name

Transport = Callable[..., Any]


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def redact_text(value: Any, secrets: tuple[str, ...] = ()) -> str:
    """Redact credentials without truncating normal metadata or raw evidence."""
    text = str(value)
    for secret in secrets:
        if not secret:
            continue
        text = text.replace(secret, "<redacted>")
        for encoded in (quote(secret, safe=""), quote_plus(secret)):
            if encoded != secret:
                pattern = "".join(f"[{char.lower()}{char.upper()}]" if char.isalpha() else re.escape(char) for char in encoded)
                text = re.sub(pattern, "<redacted>", text)
    text = re.sub(r"(?i)(bearer(?:\s+|%20|\+))[^\s\"',;}&\]]+", r"\1<redacted>", text)
    return re.sub(
        r"(?i)([\"']?(?:api[_-]?key|access[_-]?token|authorization|client[_-]?secret|password|token)[\"']?\s*(?:[=:]|%3d)\s*[\"']?)[^\s\"'&,;}\]]+",
        r"\1<redacted>", text,
    )


def redact_value(value: Any, secrets: tuple[str, ...] = ()) -> Any:
    if isinstance(value, Mapping):
        return {
            redact_text(key, secrets) if isinstance(key, str) else key:
            "<redacted>" if isinstance(key, str) and (_is_sensitive_name(key) or key.casefold() == "email")
            else redact_value(item, secrets)
            for key, item in value.items()
        }
    if isinstance(value, (list, tuple)):
        return [redact_value(item, secrets) for item in value]
    if isinstance(value, str):
        return redact_text(value, secrets)
    return value


def coerce_request(request: SearchRequest | Mapping[str, Any]) -> SearchRequest:
    if isinstance(request, SearchRequest):
        return request
    if isinstance(request, Mapping):
        return SearchRequest(**dict(request))
    raise TypeError("request must be a SearchRequest or mapping")


class ProviderFailure(ValueError):
    def __init__(self, error_type: str, message: str) -> None:
        super().__init__(message)
        self.error_type = error_type


def decode_json_count(value: Any) -> int:
    if type(value) is int and value >= 0:
        return value
    if isinstance(value, str) and re.fullmatch(r"\d+", value.strip()):
        return int(value)
    raise ValueError("reported count must be a non-negative integer")


class Provider(ABC):
    """All implementations expose search(SearchRequest) -> ProviderResult.

    A live request requires both ``mode='live'`` and an explicitly injected
    callable transport (or client exposing ``open``/``request``).  Transports
    receive a urllib Request, may accept timeout=, and own rate/redirect policy.
    ``max_requests`` is shared across calls on this instance. No retries occur.
    """

    name = "provider"

    def __init__(self, *, transport: Transport | None = None, client: Any = None,
                 timeout: float = 20.0, max_requests: int | None = None,
                 api_key: str | None = None) -> None:
        if transport is not None and client is not None:
            raise ValueError("provide transport or client, not both")
        if type(timeout) not in (int, float) or not math.isfinite(timeout) or timeout <= 0:
            raise ValueError("timeout must be finite and positive")
        if max_requests is not None and (type(max_requests) is not int or max_requests < 0):
            raise ValueError("max_requests must be a non-negative integer or None")
        if api_key is not None and not isinstance(api_key, str):
            raise ValueError("api_key must be a string or None")
        self.transport = transport if transport is not None else client
        self.timeout, self.max_requests, self.api_key = float(timeout), max_requests, api_key
        self._requests_made = 0

    @abstractmethod
    def search(self, request: SearchRequest | Mapping[str, Any]) -> ProviderResult:
        """Plan or explicitly execute a search."""

    def _secrets(self, request: SearchRequest | None = None) -> tuple[str, ...]:
        values = [self.api_key] if self.api_key else []
        if request:
            values.extend(value for key, value in request.filters.items()
                          if (_is_sensitive_name(key) or key.casefold() == "email") and isinstance(value, str))
        return tuple(values)

    def _preflight(self, request: SearchRequest, plan: Any) -> ProviderResult | None:
        if request.mode == "planned":
            return ProviderResult(self.name, "planned", raw_response={"plan": plan}, query_hash=request.query_hash)
        reason = None
        if request.mode == "replay":
            reason = ("replay_payload_missing", "use parse_response(payload, request) for offline replay")
        elif self.transport is None:
            reason = ("transport_not_configured", "live mode requires an injected transport or client")
        elif request.limit == 0:
            reason = ("limit_zero", "zero result limit; no request executed")
        elif self.max_requests is not None and self._requests_made >= self.max_requests:
            reason = ("budget_exhausted", "request budget exhausted")
        if reason:
            return ProviderResult(self.name, "not_executed", raw_response={"plan": plan},
                                  error_type=reason[0], error_message=reason[1], query_hash=request.query_hash)
        return None

    def _send(self, request: Request, *, secrets: tuple[str, ...] = ()) -> Any:
        """One bounded transport attempt. Responses always close, including errors."""
        if self.max_requests is not None and self._requests_made >= self.max_requests:
            raise ProviderFailure("budget_exhausted", "request budget exhausted")
        target = self.transport
        if not callable(target):
            target = next((getattr(target, name) for name in ("open", "request") if callable(getattr(target, name, None))), None)
        if not callable(target):
            raise ProviderFailure("invalid_transport", "transport/client must be callable or expose open/request")
        response = None
        self._requests_made += 1
        try:
            try:
                try:
                    parameters = inspect.signature(target).parameters.values()
                    accepts_timeout = any(p.kind == inspect.Parameter.VAR_KEYWORD or p.name == "timeout" for p in parameters)
                except (TypeError, ValueError):
                    accepts_timeout = True
                response = target(request, timeout=self.timeout) if accepts_timeout else target(request)
            except HTTPError as error:
                response = error
            status = getattr(response, "status", None)
            if status is None:
                getcode = getattr(response, "getcode", None)
                status = getcode() if callable(getcode) else 200
            if type(status) is not int or not 100 <= status <= 599:
                raise ProviderFailure("invalid_response", "invalid HTTP status")
            if not 200 <= status < 300:
                raise ProviderFailure("http_error", f"HTTP {status}")
            if isinstance(response, (str, bytes, dict, list)):
                return response
            body = response.read()
            if not isinstance(body, (bytes, str)):
                raise ProviderFailure("invalid_response", "response body must be bytes or text")
            return body
        except ProviderFailure:
            raise
        except (URLError, TimeoutError, OSError) as error:
            reason = getattr(error, "reason", error)
            error_type = "timeout" if isinstance(reason, TimeoutError) or "timed out" in str(reason).lower() else "transport_error"
            raise ProviderFailure(error_type, redact_text(error, secrets)[:500]) from error
        except Exception as error:
            raise ProviderFailure("transport_error", redact_text(error, secrets)[:500]) from error
        finally:
            close = getattr(response, "close", None)
            if callable(close):
                try:
                    close()
                except Exception:
                    pass

    def _failed(self, request: SearchRequest, raw: Any, error: Exception, *, request_count: int = 0,
                executed_at: str | None = None, reported_count: int | None = None) -> ProviderResult:
        return ProviderResult(
            self.name, "partial" if reported_count is not None and request_count else "failed",
            request_count=request_count, reported_count=reported_count,
            raw_response=redact_value(raw, self._secrets(request)),
            error_type=getattr(error, "error_type", "invalid_response"),
            error_message=redact_text(error, self._secrets(request))[:500],
            executed_at=executed_at if request_count else None, query_hash=request.query_hash,
        )
