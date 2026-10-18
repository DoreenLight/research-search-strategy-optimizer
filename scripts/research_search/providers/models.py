"""Provider-level records and execution contracts for optional discovery sources.

The existing P0 ``Paper`` model remains unchanged.  These records preserve
provider-specific fields (for example MeSH and Semantic Scholar identifiers)
without manufacturing P0 ``source_run_ids``.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
import hashlib
import json
from typing import Any, Mapping


_SENSITIVE_NAMES = {
    "apikey", "api_key", "api-key", "authorization", "bearertoken",
    "accesstoken", "access_token", "clientsecret", "client_secret", "secret",
    "token", "password",
}


def _is_sensitive_name(name: str) -> bool:
    compact = "".join(character for character in name.casefold() if character.isalnum())
    return compact in {"apikey", "authorization", "bearertoken", "accesstoken", "clientsecret", "secret", "token", "password"}


def _safe_json_value(value: Any) -> Any:
    """Return a deterministic, credential-free value for request hashing."""
    if isinstance(value, Mapping):
        return {
            str(key): "<redacted>" if isinstance(key, str) and _is_sensitive_name(key)
            else _safe_json_value(item)
            for key, item in sorted(value.items(), key=lambda pair: str(pair[0]))
        }
    if isinstance(value, (list, tuple)):
        return [_safe_json_value(item) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def query_hash_for(query: str, filters: Mapping[str, Any] | None = None) -> str:
    """Hash query semantics, independent of execution mode or filter order."""
    payload = {"query": query, "filters": _safe_json_value(filters or {})}
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


@dataclass(frozen=True)
class SearchRequest:
    """Provider-neutral request.

    ``planned`` is the safe default.  A caller must explicitly choose
    ``mode='live'`` and inject a transport/client before any network request
    can happen.
    """

    query: str
    filters: Mapping[str, Any] = field(default_factory=dict)
    limit: int = 20
    mode: str = "planned"

    def __post_init__(self) -> None:
        if not isinstance(self.query, str) or not self.query.strip():
            raise ValueError("query must be a non-empty string")
        if not isinstance(self.filters, Mapping):
            raise ValueError("filters must be a mapping")
        if type(self.limit) is not int or self.limit < 0:
            raise ValueError("limit must be a non-negative integer")
        if self.mode not in {"planned", "live", "replay"}:
            raise ValueError("mode must be planned, live, or replay")
        object.__setattr__(self, "filters", dict(self.filters))

    @property
    def query_hash(self) -> str:
        return query_hash_for(self.query, self.filters)

    def to_dict(self) -> dict[str, Any]:
        return {
            "query": self.query,
            "filters": _safe_json_value(self.filters),
            "limit": self.limit,
            "mode": self.mode,
            "query_hash": self.query_hash,
        }


@dataclass
class ProviderPaper:
    """A paper record with both common and source-specific metadata."""

    provider: str
    paper_id: str
    title: str
    abstract: str | None = None
    authors: list[str] = field(default_factory=list)
    journal: str | None = None
    publication_year: int | None = None
    doi: str | None = None
    pmid: str | None = None
    openalex_id: str | None = None
    s2_paper_id: str | None = None
    mesh_terms: list[str] = field(default_factory=list)
    author_keywords: list[str] = field(default_factory=list)
    database_keywords: list[str] = field(default_factory=list)
    source_url: str | None = None
    field_sources: dict[str, str] = field(default_factory=dict)
    citation_source: str | None = None
    references_source: str | None = None
    citation_ids: list[str] = field(default_factory=list)
    reference_ids: list[str] = field(default_factory=list)
    citation_count: int | None = None
    candidate_reason: str | None = None
    seed_ids: list[str] = field(default_factory=list)
    channel: str | None = None
    discovery_channel: bool = False
    source_run_ids: list[str] = field(default_factory=list)
    raw: dict[str, Any] | None = None

    @property
    def source_title(self) -> str | None:
        return self.journal

    @property
    def source_fields(self) -> dict[str, str]:
        """Compatibility alias used by callers that name provenance fields this way."""
        return self.field_sources

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def __getitem__(self, key: str) -> Any:
        return self.to_dict()[key]

    def get(self, key: str, default: Any = None) -> Any:
        return self.to_dict().get(key, default)


@dataclass
class ProviderResult:
    """The common execution result returned by every provider."""

    provider: str
    status: str
    request_count: int = 0
    reported_count: int | None = None
    fetched_count: int = 0
    papers: list[ProviderPaper] = field(default_factory=list)
    raw_response: Any = None
    error_type: str | None = None
    error_message: str | None = None
    source_level: str = "U"
    executed_at: str | None = None
    query_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def __getitem__(self, key: str) -> Any:
        return self.to_dict()[key]


@dataclass
class FusionConflict:
    kind: str
    paper_ids: tuple[str, ...]
    message: str
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def __getitem__(self, key: str) -> Any:
        return self.to_dict()[key]


@dataclass
class FusionResult:
    """Cross-source output with an auditable record of every input source."""

    papers: list[ProviderPaper] = field(default_factory=list)
    source_records: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    provider_ids: dict[str, list[str]] = field(default_factory=dict)
    conflicts: list[FusionConflict] = field(default_factory=list)
    coverage_by_provider: dict[str, dict[str, Any]] = field(default_factory=dict)
    paper_provider_ids: dict[str, dict[str, list[str]]] = field(default_factory=dict)
    merge_events: list[dict[str, Any]] = field(default_factory=list)
    retrieval_papers: list[ProviderPaper] = field(default_factory=list)
    discovery_papers: list[ProviderPaper] = field(default_factory=list)
    paper_channels: dict[str, list[str]] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def __getitem__(self, key: str) -> Any:
        return self.to_dict()[key]
