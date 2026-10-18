"""Small, local, content-addressed cache for redacted provider responses.

The cache is deliberately opt-in and conservative: malformed, unsafe, or
partially-written entries are treated as misses and are never removed by this
module.  A failed atomic write leaves its scratch path available for
inspection instead of silently deleting user-owned data.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import hashlib
import json
import math
import os
from pathlib import Path
import stat
import tempfile
from typing import Any, Mapping
from urllib.parse import parse_qsl, urlsplit, urlunsplit, urlencode


CACHE_SCHEMA_VERSION = "0.2"
MAX_CACHE_FILE_BYTES = 16 * 1024 * 1024
_REQUIRED_RECORD_KEYS = frozenset({
    "schema_version", "request", "request_sha256", "request_metadata",
    "retrieved_at", "response_sha256", "response",
})
_OMIT = object()
_SENSITIVE_QUERY_NAMES = frozenset({
    "apikey", "authorization", "accesstoken", "authtoken", "bearertoken",
    "clientsecret", "password", "privatekey", "refreshtoken", "secret",
    "token",
})


def _reject_nonfinite(value: str) -> Any:
    raise ValueError(f"non-finite JSON value: {value}")


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _safe_value(value: Any) -> Any:
    """Return a JSON-safe copy, rejecting non-finite numbers and odd shapes."""
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key in value:
            if not isinstance(key, str):
                raise ValueError("cache objects must use string keys")
            result[key] = _safe_value(value[key])
        return {key: result[key] for key in sorted(result)}
    if isinstance(value, (list, tuple)):
        return [_safe_value(item) for item in value]
    if value is None or isinstance(value, str) or type(value) is bool or type(value) is int:
        return value
    if type(value) is float:
        if not math.isfinite(value):
            raise ValueError("cache values must contain finite numbers")
        return value
    raise ValueError("cache values must contain JSON-compatible values")


def _canonical_json(value: Any) -> str:
    return json.dumps(
        _safe_value(value), ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False,
    )


def _normalize_filter_value(value: Any) -> str | object:
    """Normalize the value as OpenAlex's emitted filter scalar semantics."""
    if value is None:
        return _OMIT
    if type(value) is bool:
        return "true" if value else "false"
    if isinstance(value, str):
        return value
    if type(value) is int:
        return str(value)
    if type(value) is float and math.isfinite(value):
        return str(value)
    raise ValueError("cache filters must contain scalar, finite values")


def _normalize_filters(filters: Mapping[str, Any]) -> dict[str, str]:
    if not isinstance(filters, Mapping):
        raise ValueError("cache filters must be a mapping")
    normalized: dict[str, str] = {}
    for key in sorted(filters):
        if not isinstance(key, str) or not key:
            raise ValueError("cache filter names must be non-empty strings")
        value = _normalize_filter_value(filters[key])
        if value is not _OMIT:
            normalized[key] = value
    return normalized


def _cache_key_name(value: str) -> str:
    return value.casefold().replace("_", "").replace("-", "")


def _redact_metadata_url(value: str | None) -> str | None:
    """Remove URL userinfo and values of credential-like query parameters."""
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError("request_url must be a string or None")
    try:
        parts = urlsplit(value)
        hostname = parts.hostname
        if hostname is None:
            netloc = ""
        else:
            host = f"[{hostname}]" if ":" in hostname and not hostname.startswith("[") else hostname
            try:
                port = parts.port
            except ValueError:
                port = None
            netloc = host if port is None else f"{host}:{port}"
        query: list[tuple[str, str]] = []
        for key, item in parse_qsl(parts.query, keep_blank_values=True):
            safe_key = str(key)
            safe_value = "<redacted>" if _cache_key_name(safe_key) in _SENSITIVE_QUERY_NAMES else item
            query.append((safe_key, safe_value))
        return urlunsplit((parts.scheme, netloc, parts.path, urlencode(query), parts.fragment))
    except (TypeError, ValueError, UnicodeError):
        return "<redacted-url>"


@dataclass(frozen=True)
class CacheRequest:
    provider: str
    query: str
    filters: dict[str, Any]
    per_page: int
    cursor: str | None
    api_version: str

    def payload(self) -> dict[str, Any]:
        return _safe_value({
            "provider": self.provider,
            "query": self.query,
            "filters": _normalize_filters(self.filters),
            "per_page": self.per_page,
            "cursor": self.cursor,
            "api_version": self.api_version,
        })


class CacheWriteError(RuntimeError):
    """A cache write failed; the scratch path is retained when one exists."""

    def __init__(self, message: str, *, path: Path | None = None,
                 scratch_path: Path | None = None) -> None:
        super().__init__(message)
        self.path = path
        self.scratch_path = scratch_path


class QueryCache:
    """A filesystem cache that stores only redacted JSON responses.

    Cache files are keyed by the semantic request payload, not URL ordering.
    Invalid entries are ignored rather than deleted, preserving user-owned data
    for later inspection.
    """

    def __init__(self, directory: Path | str, *, provider: str, api_version: str) -> None:
        self.directory = Path(directory)
        if not provider or not api_version:
            raise ValueError("provider and api_version must be non-empty")
        self.provider = provider
        self.api_version = api_version

    @staticmethod
    def _absolute(path: Path) -> Path:
        # abspath normalizes ``..`` without resolving symlinks.
        return Path(os.path.abspath(os.fspath(path)))

    @classmethod
    def _has_symlink_component(cls, path: Path) -> bool:
        absolute = cls._absolute(path)
        current = Path(absolute.anchor)
        for part in absolute.parts:
            if part == absolute.anchor:
                continue
            current /= part
            try:
                mode = os.lstat(current).st_mode
            except FileNotFoundError:
                return False
            except OSError:
                return True
            if stat.S_ISLNK(mode):
                return True
        return False

    @classmethod
    def _is_regular_file(cls, path: Path) -> bool:
        try:
            mode = os.lstat(path).st_mode
        except OSError:
            return False
        return stat.S_ISREG(mode) and not stat.S_ISLNK(mode)

    def _ensure_directory(self) -> Path:
        directory = self._absolute(self.directory)
        if self._has_symlink_component(directory):
            raise CacheWriteError(f"cache directory contains a symlink: {directory}", path=directory)

        current = Path(directory.anchor)
        parts = directory.parts
        for part in parts:
            if part == directory.anchor:
                continue
            current /= part
            try:
                mode = os.lstat(current).st_mode
            except FileNotFoundError:
                try:
                    os.mkdir(current, 0o700)
                except FileExistsError:
                    mode = os.lstat(current).st_mode
                except OSError as error:
                    raise CacheWriteError(
                        f"cache directory could not be created: {current}", path=directory,
                    ) from error
                else:
                    mode = os.lstat(current).st_mode
            except OSError as error:
                raise CacheWriteError(
                    f"cache directory could not be inspected: {current}", path=directory,
                ) from error
            if stat.S_ISLNK(mode) or not stat.S_ISDIR(mode):
                raise CacheWriteError(
                    f"cache directory is not a real directory: {current}", path=directory,
                )

        try:
            os.chmod(directory, 0o700)
        except OSError as error:
            raise CacheWriteError(f"cache directory permissions could not be set: {directory}", path=directory) from error
        return directory

    def key(self, request: CacheRequest) -> str:
        return hashlib.sha256(_canonical_json(request.payload()).encode("utf-8")).hexdigest()

    def _path(self, request: CacheRequest) -> Path:
        return self._absolute(self.directory) / f"{self.key(request)}.json"

    def _validate_record(self, record: Any, request: CacheRequest, expected_key: str) -> dict[str, Any] | None:
        if not isinstance(record, dict) or set(record) != _REQUIRED_RECORD_KEYS:
            return None
        if record.get("schema_version") != CACHE_SCHEMA_VERSION:
            return None
        try:
            request_payload = request.payload()
        except (TypeError, ValueError, OverflowError, RecursionError):
            return None
        if record.get("request") != request_payload:
            return None
        if record.get("request_sha256") != expected_key:
            return None
        if not isinstance(record.get("request_sha256"), str) or len(record["request_sha256"]) != 64:
            return None
        if any(character not in "0123456789abcdef" for character in record["request_sha256"]):
            return None

        metadata = record.get("request_metadata")
        if not isinstance(metadata, dict) or set(metadata) != {"request_url"}:
            return None
        if metadata["request_url"] is not None and not isinstance(metadata["request_url"], str):
            return None

        retrieved_at = record.get("retrieved_at")
        if not isinstance(retrieved_at, str) or not retrieved_at:
            return None
        try:
            datetime.fromisoformat(retrieved_at.replace("Z", "+00:00"))
        except (TypeError, ValueError, OverflowError):
            return None

        response = record.get("response")
        if not isinstance(response, dict):
            return None
        response_sha256 = record.get("response_sha256")
        if not isinstance(response_sha256, str) or len(response_sha256) != 64:
            return None
        if any(character not in "0123456789abcdef" for character in response_sha256):
            return None
        try:
            digest = hashlib.sha256(_canonical_json(response).encode("utf-8")).hexdigest()
        except (TypeError, ValueError, OverflowError, RecursionError, UnicodeError):
            return None
        if response_sha256 != digest:
            return None
        # Keep metadata in the record shape but ensure direct callers cannot put
        # URL userinfo or obvious credential query values on disk.
        record["request_metadata"] = {"request_url": _redact_metadata_url(metadata["request_url"])}
        return record

    def load(self, request: CacheRequest) -> dict[str, Any] | None:
        try:
            path = self._path(request)
            expected_key = self.key(request)
            directory = self._absolute(self.directory)
            if self._has_symlink_component(directory) or self._has_symlink_component(path):
                return None
            try:
                directory_mode = os.lstat(directory).st_mode
            except OSError:
                return None
            if stat.S_ISLNK(directory_mode) or not stat.S_ISDIR(directory_mode):
                return None
            try:
                size = os.lstat(path).st_size
            except OSError:
                return None
            if not self._is_regular_file(path) or size < 0 or size > MAX_CACHE_FILE_BYTES:
                return None

            nofollow = getattr(os, "O_NOFOLLOW", 0)
            fd: int | None = None
            try:
                fd = os.open(os.fspath(path), os.O_RDONLY | nofollow)
                with os.fdopen(fd, "r", encoding="utf-8") as handle:
                    fd = None
                    record = json.load(
                        handle, parse_constant=_reject_nonfinite,
                        object_pairs_hook=_reject_duplicate_keys,
                    )
            finally:
                if fd is not None:
                    try:
                        os.close(fd)
                    except OSError:
                        pass
            return self._validate_record(record, request, expected_key)
        except (FileNotFoundError, OSError, UnicodeError, json.JSONDecodeError,
                TypeError, ValueError, OverflowError, RecursionError):
            return None

    def store(
        self,
        request: CacheRequest,
        *,
        request_url: str | None,
        retrieved_at: str,
        response: dict[str, Any],
    ) -> Path:
        if not isinstance(response, dict):
            raise ValueError("cache response must be an object")
        if not isinstance(retrieved_at, str) or not retrieved_at:
            raise ValueError("cache retrieved_at must be a non-empty string")
        # Serialize before touching the filesystem so an unsafe response cannot
        # leave a scratch file behind.
        request_payload = request.payload()
        key = hashlib.sha256(_canonical_json(request_payload).encode("utf-8")).hexdigest()
        safe_response = _safe_value(response)
        safe_url = _redact_metadata_url(request_url)
        record = {
            "schema_version": CACHE_SCHEMA_VERSION,
            "request": request_payload,
            "request_sha256": key,
            "request_metadata": {"request_url": safe_url},
            "retrieved_at": retrieved_at,
            "response_sha256": hashlib.sha256(_canonical_json(safe_response).encode("utf-8")).hexdigest(),
            "response": safe_response,
        }
        payload = json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n"

        directory = self._ensure_directory()
        destination = directory / f"{key}.json"
        try:
            destination_mode = os.lstat(destination).st_mode
        except FileNotFoundError:
            destination_mode = None
        except OSError as error:
            raise CacheWriteError(f"cache destination could not be inspected: {destination}", path=destination) from error
        if destination_mode is not None and stat.S_ISLNK(destination_mode):
            raise CacheWriteError(f"cache destination is a symlink: {destination}", path=destination)

        fd: int | None = None
        scratch: Path | None = None
        try:
            fd_number, scratch_name = tempfile.mkstemp(
                prefix=f".{key}.", suffix=".tmp", dir=os.fspath(directory),
            )
            fd, scratch = fd_number, Path(scratch_name)
            os.fchmod(fd, 0o600)
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                fd = None
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
            try:
                destination_mode = os.lstat(destination).st_mode
            except FileNotFoundError:
                destination_mode = None
            if destination_mode is not None and stat.S_ISLNK(destination_mode):
                raise CacheWriteError(
                    f"cache destination became a symlink: {destination}",
                    path=destination, scratch_path=scratch,
                )
            os.replace(os.fspath(scratch), os.fspath(destination))
        except CacheWriteError:
            raise
        except Exception as error:
            raise CacheWriteError(
                f"cache atomic write failed; scratch retained at {scratch}",
                path=destination, scratch_path=scratch,
            ) from error
        finally:
            if fd is not None:
                try:
                    os.close(fd)
                except OSError:
                    pass
        return destination


__all__ = ["CACHE_SCHEMA_VERSION", "CacheRequest", "CacheWriteError", "QueryCache"]
