"""Transparent set metrics: incomplete judgments never become negative labels."""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any


@dataclass(frozen=True)
class RetrievalMetrics:
    returned_count: int
    fetched_count: int
    deduplicated_count: int
    relevant_found: int | None
    recall_at_k: float | None
    precision_at_k: float | None
    k: int
    effective_k: int
    reference_hits_at_k: int | None
    judged_count: int
    unjudged_count: int
    judged_precision: float | None
    precision_at_available: float | None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def evaluate_retrieval(returned_ids: list[str], known_relevant_ids: set[str] | None,
                       fetched_count: int, deduplicated_count: int, k: int,
                       *, relevance_labels: dict[str, str] | None = None) -> RetrievalMetrics:
    if type(k) is not int or k <= 0:
        raise ValueError("k must be a positive integer")
    if any(type(n) is not int or n < 0 for n in (fetched_count, deduplicated_count)):
        raise ValueError("counts must be non-negative integers")
    if deduplicated_count > fetched_count:
        raise ValueError("deduplicated count cannot exceed fetched count")
    if not isinstance(returned_ids, list) or any(not isinstance(x, str) or not x for x in returned_ids):
        raise ValueError("returned IDs must be a string array")
    ranked_ids = list(dict.fromkeys(returned_ids))
    labels = relevance_labels or {}
    if any(v not in {"relevant", "irrelevant", "uncertain"} for v in labels.values()):
        raise ValueError("invalid relevance label")
    top = ranked_ids[:k]
    judged = [pid for pid in top if labels.get(pid) in {"relevant", "irrelevant"}]
    positive_count = sum(labels.get(pid) == "relevant" for pid in judged)
    hits = len(set(top) & known_relevant_ids) if known_relevant_ids is not None else None
    recall = hits / len(known_relevant_ids) if known_relevant_ids else None
    complete = bool(top) and len(judged) == len(top)
    available = positive_count / len(top) if complete else None
    return RetrievalMetrics(
        returned_count=len(returned_ids), fetched_count=fetched_count,
        deduplicated_count=deduplicated_count,
        relevant_found=positive_count if labels else hits,
        recall_at_k=recall,
        precision_at_k=available if len(top) == k else None,
        k=k, effective_k=len(top), reference_hits_at_k=hits,
        judged_count=len(judged), unjudged_count=len(top) - len(judged),
        judged_precision=positive_count / len(judged) if judged else None,
        precision_at_available=available,
    )


def compare_retrieval(baseline_ids: list[str], candidate_ids: list[str],
                      relevance_labels: dict[str, str] | None = None) -> dict[str, Any]:
    labels = relevance_labels or {}
    baseline = set(baseline_ids)
    new = [pid for pid in dict.fromkeys(candidate_ids) if pid not in baseline]
    return {"new_ids": new,
            "new_relevant_ids": [pid for pid in new if labels.get(pid) == "relevant"],
            "unjudged_new_count": sum(labels.get(pid) not in {"relevant", "irrelevant"} for pid in new),
            "attribution": "strategy_version_not_individual_terms"}
