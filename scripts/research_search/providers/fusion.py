"""Conservative cross-provider fusion with explicit provenance and conflicts."""
from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import replace
import re
from typing import Any

from ..models import Paper
from .models import FusionConflict, FusionResult, ProviderPaper, ProviderResult


def _norm(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip().casefold().rstrip("/")
    return text or None


def _identifier(value: Any, kind: str) -> str | None:
    text = _norm(value)
    if not text:
        return None
    if kind == "doi":
        text = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", text)
    elif kind == "pmid":
        text = re.sub(r"^(?:https?://pubmed\.ncbi\.nlm\.nih\.gov/|pmid:\s*)", "", text)
    elif kind == "openalex":
        match = re.search(r"(W\d+)$", text, re.IGNORECASE)
        text = match.group(1).upper() if match else text
    elif kind == "s2":
        text = text.rsplit("/", 1)[-1]
    return text or None


def title_fingerprint(title: str | None) -> str:
    return re.sub(r"[^\w]+", "", (title or "").casefold())


def _record_keys(paper: ProviderPaper) -> dict[str, str]:
    values = (
        ("openalex", paper.openalex_id), ("pmid", paper.pmid), ("doi", paper.doi),
        ("s2", paper.s2_paper_id or (paper.paper_id if paper.provider == "semantic_scholar" else None)),
    )
    return {kind: normalized for kind, value in values if (normalized := _identifier(value, kind))}


def _to_provider_paper(item: Any, provider: str | None = None) -> ProviderPaper:
    if isinstance(item, ProviderPaper):
        return item
    if isinstance(item, Paper):
        return ProviderPaper(
            provider=provider or "p0", paper_id=item.paper_id, title=item.title,
            abstract=item.abstract, authors=list(item.authors), journal=item.source_title,
            publication_year=item.publication_year, doi=item.doi, pmid=item.pmid,
            openalex_id=item.openalex_id, author_keywords=list(item.author_keywords),
            database_keywords=list(item.database_keywords), source_url=item.source_url,
            source_run_ids=list(item.source_run_ids),
        )
    if isinstance(item, Mapping):
        values = dict(item)
        values.setdefault("provider", provider or "unknown")
        values.setdefault("paper_id", values.get("s2_paper_id") or values.get("pmid") or values.get("doi") or values.get("title"))
        if not values.get("title"):
            raise ValueError("paper record requires title")
        allowed = set(ProviderPaper.__dataclass_fields__)
        return ProviderPaper(**{key: value for key, value in values.items() if key in allowed})
    raise TypeError("fusion input must contain ProviderResult, ProviderPaper, Paper, or mapping records")


def _empty_coverage(status: str = "provided") -> dict[str, Any]:
    return {"status": status, "request_count": 0, "reported_count": None, "fetched_count": 0,
            "raw_count": 0, "unique_count": 0, "fusion_count": 0, "retrieval_count": 0,
            "discovery_count": 0}


def _flatten(results: Iterable[Any]) -> tuple[list[ProviderPaper], dict[str, dict[str, Any]]]:
    papers: list[ProviderPaper] = []
    coverage: dict[str, dict[str, Any]] = {}
    for source in results:
        if isinstance(source, ProviderResult):
            provider = source.provider
            bucket = coverage.setdefault(provider, _empty_coverage(source.status))
            bucket.update(status=source.status, request_count=source.request_count,
                          reported_count=source.reported_count, fetched_count=source.fetched_count)
            for paper in source.papers:
                record = _to_provider_paper(paper, provider)
                papers.append(record)
                bucket["raw_count"] += 1
                bucket["discovery_count"] += int(record.discovery_channel)
                bucket["retrieval_count"] += int(not record.discovery_channel)
        elif isinstance(source, (ProviderPaper, Paper)) or isinstance(source, Mapping):
            record = _to_provider_paper(source)
            papers.append(record)
            bucket = coverage.setdefault(record.provider, _empty_coverage())
            bucket["raw_count"] += 1
            bucket["fetched_count"] += 1
            bucket["discovery_count"] += int(record.discovery_channel)
            bucket["retrieval_count"] += int(not record.discovery_channel)
        else:
            nested_papers, nested_coverage = _flatten(list(source))
            papers.extend(nested_papers)
            for provider, details in nested_coverage.items():
                bucket = coverage.setdefault(provider, _empty_coverage(details.get("status", "provided")))
                for key, value in details.items():
                    if key in {"raw_count", "fetched_count", "unique_count", "fusion_count", "retrieval_count", "discovery_count"}:
                        bucket[key] += value
                    elif bucket.get(key) in (None, 0):
                        bucket[key] = value
    return papers, coverage


def _richness(paper: ProviderPaper) -> int:
    return sum(bool(value) for value in (paper.abstract, paper.doi, paper.pmid, paper.openalex_id,
                                         paper.s2_paper_id, paper.authors, paper.journal,
                                         paper.mesh_terms, paper.author_keywords, paper.database_keywords))


def _pair_conflict(left: ProviderPaper, right: ProviderPaper) -> FusionConflict | None:
    left_keys, right_keys = _record_keys(left), _record_keys(right)
    shared_kinds = set(left_keys) & set(right_keys)
    shared_id = any(left_keys[key] == right_keys[key] for key in shared_kinds)
    same_title = bool(title_fingerprint(left.title)) and title_fingerprint(left.title) == title_fingerprint(right.title)
    ids = tuple(dict.fromkeys((left.paper_id, right.paper_id)))
    # Only compare records that have a relationship: a shared reliable ID or
    # an identical title fingerprint. Unrelated papers are not conflicts.
    if not shared_id and not same_title:
        return None
    if shared_kinds:
        mismatched = sorted(key for key in shared_kinds if left_keys[key] != right_keys[key])
        if mismatched:
            return FusionConflict("identifier_conflict", ids,
                                  "Reliable identifiers conflict; source records are kept separate.",
                                  {"fields": mismatched, "left": left_keys, "right": right_keys})
        if title_fingerprint(left.title) != title_fingerprint(right.title):
            return FusionConflict("title_identifier_conflict", ids,
                                  "A reliable identifier agrees but source titles differ; records are kept separate.",
                                  {"left": left_keys, "right": right_keys,
                                   "left_title": left.title, "right_title": right.title})
        return None
    if title_fingerprint(left.title) == title_fingerprint(right.title) and left_keys and right_keys:
        return FusionConflict("title_identifier_conflict", ids,
                              "Title fingerprint agrees but reliable identifiers differ; source records are kept separate.",
                              {"left": left_keys, "right": right_keys})
    return None


def _merge_group(group: list[ProviderPaper]) -> tuple[ProviderPaper, list[FusionConflict]]:
    winner = max(group, key=_richness)
    conflicts = [conflict for index, left in enumerate(group) for right in group[index + 1:]
                 if (conflict := _pair_conflict(left, right))]
    merged = replace(
        winner,
        abstract=winner.abstract or next((paper.abstract for paper in group if paper.abstract), None),
        doi=winner.doi or next((paper.doi for paper in group if paper.doi), None),
        pmid=winner.pmid or next((paper.pmid for paper in group if paper.pmid), None),
        openalex_id=winner.openalex_id or next((paper.openalex_id for paper in group if paper.openalex_id), None),
        s2_paper_id=winner.s2_paper_id or next((paper.s2_paper_id for paper in group if paper.s2_paper_id), None),
        authors=winner.authors or next((paper.authors for paper in group if paper.authors), []),
        mesh_terms=winner.mesh_terms or next((paper.mesh_terms for paper in group if paper.mesh_terms), []),
        author_keywords=winner.author_keywords or next((paper.author_keywords for paper in group if paper.author_keywords), []),
        database_keywords=winner.database_keywords or next((paper.database_keywords for paper in group if paper.database_keywords), []),
        source_run_ids=list(dict.fromkeys(run_id for paper in group for run_id in paper.source_run_ids)),
        candidate_reason=winner.candidate_reason or next((paper.candidate_reason for paper in group if paper.candidate_reason), None),
        seed_ids=list(dict.fromkeys(seed for paper in group for seed in paper.seed_ids)),
        channel=winner.channel or next((paper.channel for paper in group if paper.channel), None),
        discovery_channel=any(paper.discovery_channel for paper in group),
    )
    return merged, conflicts


def _matching_kind(paper: ProviderPaper, existing: ProviderPaper) -> str | None:
    left, right = _record_keys(paper), _record_keys(existing)
    shared = set(left) & set(right)
    if shared and all(left[key] == right[key] for key in shared):
        return next((key for key in ("openalex", "pmid", "doi", "s2") if key in shared), "identifier")
    if not left and not right and title_fingerprint(paper.title) == title_fingerprint(existing.title):
        return "title_fingerprint"
    return None


def _group_match(paper: ProviderPaper, group: list[ProviderPaper]) -> tuple[str | None, list[FusionConflict]]:
    """Return a safe match only when every existing source agrees with it."""
    matches: list[str] = []
    conflicts: list[FusionConflict] = []
    for existing in group:
        if (conflict := _pair_conflict(existing, paper)) is not None:
            conflicts.append(conflict)
        if (kind := _matching_kind(paper, existing)) is not None:
            matches.append(kind)
    if conflicts:
        unique: list[FusionConflict] = []
        seen: set[tuple[str, tuple[str, ...]]] = set()
        for conflict in conflicts:
            key = (conflict.kind, conflict.paper_ids)
            if key not in seen:
                unique.append(conflict)
                seen.add(key)
        return None, unique
    return (matches[0] if matches and len(set(matches)) == 1 else ("identifier" if matches else None)), []


def fuse_results(results: Iterable[Any]) -> FusionResult:
    """Fuse by reliable ID first, title fingerprint only when both sides lack IDs.

    Conflicting records are never merged; every input remains in source_records.
    ``retrieval_papers`` and ``discovery_papers`` are separate views, even when
    their canonical record is shared.
    """
    papers, coverage = _flatten(results)
    groups: list[list[ProviderPaper]] = []
    merge_events: list[dict[str, Any]] = []
    conflicts: list[FusionConflict] = []
    for paper in papers:
        candidate_indices: list[int] = []
        candidate_kinds: dict[int, str] = {}
        for index, group in enumerate(groups):
            kind, group_conflicts = _group_match(paper, group)
            conflicts.extend(group_conflicts)
            if kind:
                candidate_indices.append(index)
                candidate_kinds[index] = kind
        if len(candidate_indices) == 1:
            index = candidate_indices[0]
            groups[index].append(paper)
            merge_events.append({"paper_ids": [record.paper_id for record in groups[index]],
                                 "matched_by": [candidate_kinds[index]],
                                 "providers": [record.provider for record in groups[index]]})
        else:
            groups.append([paper])
    canonical, source_records, provider_ids, paper_provider_ids, paper_channels = [], {}, {}, {}, {}
    retrieval_papers, discovery_papers = [], []
    used_keys: dict[str, int] = {}
    for group in groups:
        merged, group_conflicts = _merge_group(group)
        canonical.append(merged)
        conflicts.extend(group_conflicts)
        keys = _record_keys(merged)
        canonical_key = next((f"{kind}:{keys[kind]}" for kind in ("doi", "pmid", "openalex", "s2") if kind in keys),
                             f"title:{title_fingerprint(merged.title)}")
        occurrence = used_keys.get(canonical_key, 0)
        used_keys[canonical_key] = occurrence + 1
        if occurrence:
            canonical_key = f"{canonical_key}#conflict-{occurrence + 1}"
        source_records[canonical_key] = [paper.to_dict() for paper in group]
        providers: dict[str, list[str]] = {}
        channels: set[str] = set()
        for paper in group:
            providers.setdefault(paper.provider, []).append(paper.paper_id)
            provider_ids.setdefault(paper.provider, []).append(paper.paper_id)
            if paper.channel:
                channels.add(paper.channel)
        paper_provider_ids[canonical_key] = {provider: list(dict.fromkeys(ids)) for provider, ids in providers.items()}
        paper_channels[canonical_key] = sorted(channels)
        if any(not paper.discovery_channel for paper in group):
            retrieval_papers.append(replace(merged, discovery_channel=False))
        if any(paper.discovery_channel for paper in group):
            discovery_papers.append(replace(merged, discovery_channel=True))
    for provider, ids in provider_ids.items():
        provider_ids[provider] = list(dict.fromkeys(ids))
    for provider, details in coverage.items():
        details["unique_count"] = len({paper.paper_id for paper in papers if paper.provider == provider})
        details["fusion_count"] = sum(1 for group in groups if any(paper.provider == provider for paper in group))
    return FusionResult(papers=canonical, source_records=source_records, provider_ids=provider_ids,
                        conflicts=conflicts, coverage_by_provider=coverage,
                        paper_provider_ids=paper_provider_ids, merge_events=merge_events,
                        retrieval_papers=retrieval_papers, discovery_papers=discovery_papers,
                        paper_channels=paper_channels)


fuse = fuse_results
fuse_provider_results = fuse_results
