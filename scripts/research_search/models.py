"""Versioned data contracts. Semantic decisions remain explicit Agent/user inputs."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

SCHEMA_VERSION = "0.1"


@dataclass(frozen=True)
class TermOccurrence:
    term: str
    source_field: str
    evidence_status: str = "observed_in_paper"
    original_term: str = ""
    paper_id: str = ""


@dataclass
class Paper:
    paper_id: str
    title: str
    abstract: str | None = None
    openalex_id: str | None = None
    doi: str | None = None
    pmid: str | None = None
    publication_year: int | None = None
    authors: list[str] = field(default_factory=list)
    source_title: str | None = None
    author_keywords: list[str] = field(default_factory=list)
    database_keywords: list[str] = field(default_factory=list)
    source_url: str | None = None
    retrieved_at: str | None = None
    source_run_ids: list[str] = field(default_factory=list)
    schema_version: str = SCHEMA_VERSION

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ConceptGroup:
    group_id: str
    label: str
    terms: list[str]
    role: str | None = None


@dataclass(frozen=True)
class SearchPlan:
    strategy: str
    database: str
    group_ids: list[str]
    query: str
    plan_id: str = ""
    logic: dict[str, Any] = field(default_factory=dict)
    groups: list[dict[str, Any]] = field(default_factory=list)
    status: str = "planned"
    reason: str | None = None
    version: int = 1
    syntax_status: str = "local_checked"
    schema_version: str = SCHEMA_VERSION

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ResearchScope:
    description: str
    research_object: list[str] = field(default_factory=list)
    input_modality: list[str] = field(default_factory=list)
    research_task: list[str] = field(default_factory=list)
    method: list[str] = field(default_factory=list)
    application: list[str] = field(default_factory=list)
    constraints: dict[str, Any] = field(default_factory=dict)
    unspecified: list[str] = field(default_factory=list)
    scope_id: str = "scope-1"
    mode: str = "exploratory"
    schema_version: str = SCHEMA_VERSION

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class SearchRun:
    run_id: str
    plan_id: str
    status: str
    returned_count: int | None = None
    fetched_count: int = 0
    deduplicated_count: int = 0
    request_count: int = 0
    started_at: str | None = None
    finished_at: str | None = None
    request_url: str | None = None
    error_type: str | None = None
    error_message: str | None = None
    paper_ids: list[str] = field(default_factory=list)
    raw_path: str | None = None
    attempts: list[dict[str, Any]] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    mode: str = "live"
    estimated_cost_usd: float | None = None
    schema_version: str = SCHEMA_VERSION

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Evidence:
    evidence_id: str
    source_type: str
    source_url: str | None
    evidence_level: str
    retrieved_at: str | None
    locator: str | None = None
    supports: str | None = None
    paper_id: str | None = None
    excerpt: str | None = None
    run_ids: list[str] = field(default_factory=list)
    schema_version: str = SCHEMA_VERSION

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class KeywordCandidate:
    term_id: str
    term: str
    canonical_term: str
    category: str
    relationship: str
    source_type: str
    evidence_status: str
    evidence_ids: list[str] = field(default_factory=list)
    retrieval_status: str = "untested"
    paper_ids: list[str] = field(default_factory=list)
    document_frequency: int = 0
    adopted: bool = False
    schema_version: str = SCHEMA_VERSION

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class Judgment:
    judgment_id: str
    paper_id: str
    scope_id: str
    label: str
    judge_type: str
    rationale: str
    judged_at: str
    schema_version: str = SCHEMA_VERSION

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
