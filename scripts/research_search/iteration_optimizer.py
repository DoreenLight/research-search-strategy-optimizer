"""P1 query-iteration planning; it proposes and compares, but never silently adopts terms."""
from __future__ import annotations

from collections.abc import Iterable
from typing import Any


def _dedupe(values: Iterable[str]) -> list[str]:
    return list(dict.fromkeys(values))


def compare_strategy_versions(
    baseline_ids: list[str],
    candidate_ids: list[str],
    *,
    human_labels: dict[str, str] | None = None,
    model_labels: dict[str, str] | None = None,
) -> dict[str, Any]:
    human = human_labels or {}
    model = model_labels or {}
    allowed = {"relevant", "irrelevant", "uncertain"}
    if any(label not in allowed for label in [*human.values(), *model.values()]):
        raise ValueError("labels must be relevant, irrelevant, or uncertain")
    baseline = set(baseline_ids)
    new_ids = [paper_id for paper_id in _dedupe(candidate_ids) if paper_id not in baseline]
    new_relevant = [paper_id for paper_id in new_ids if human.get(paper_id) == "relevant"]
    new_unjudged = [paper_id for paper_id in new_ids if paper_id not in human or human[paper_id] == "uncertain"]
    model_only = [paper_id for paper_id in new_ids if model.get(paper_id) == "relevant" and human.get(paper_id) != "relevant"]
    return {
        "baseline_unique_count": len(baseline),
        "candidate_unique_count": len(set(candidate_ids)),
        "new_ids": new_ids,
        "new_relevant_ids": new_relevant,
        "new_unjudged_ids": new_unjudged,
        "model_only_relevant_ids": model_only,
        "confirmed_new_relevant_count": len(new_relevant),
        "coverage_claim": "reference_set_only" if human else "unavailable",
    }


def propose_iteration(
    current_terms: set[str],
    discovered_terms: list[dict[str, Any]],
    *,
    budget_remaining: int,
) -> dict[str, Any]:
    if budget_remaining < 0:
        raise ValueError("budget_remaining must be non-negative")
    candidates: list[dict[str, Any]] = []
    skipped = 0
    for item in discovered_terms:
        term = str(item.get("term", "")).strip()
        if not term or term.casefold() in {value.casefold() for value in current_terms}:
            skipped += 1
            continue
        relationship = item.get("relationship", "unclassified")
        if relationship not in {"equivalent", "broader", "narrower", "related_task", "alternative_method", "application", "unclassified"}:
            raise ValueError(f"unsupported relationship: {relationship}")
        candidates.append({
            "term": term,
            "relationship": relationship,
            "source_paper_ids": list(dict.fromkeys(item.get("source_paper_ids", []))),
            "status": "candidate",
            "adopted": False,
            "action": "test_as_separate_query",
            "reason": "Observed outside the current term set; semantic relationship requires review.",
        })
    candidates.sort(key=lambda item: (item["relationship"] != "equivalent", item["term"].casefold()))
    return {
        "budget_remaining": budget_remaining,
        "candidates": candidates[:budget_remaining],
        "deferred_candidate_count": max(0, len(candidates) - budget_remaining),
        "skipped_existing_count": skipped,
        "adoption": "manual_or_agent_review_required",
    }


def should_stop(
    rounds: list[dict[str, Any]],
    *,
    budget_remaining: int,
    branches_remaining: int,
    max_drift_rate: float = 0.6,
) -> dict[str, Any]:
    if budget_remaining < 0 or branches_remaining < 0:
        raise ValueError("budget and branch counts must be non-negative")
    drift = rounds[-1].get("drift_rate") if rounds else None
    if drift is not None and not 0 <= drift <= 1:
        raise ValueError("drift_rate must be in [0,1] or null")
    if drift is not None and drift >= max_drift_rate:
        return {"stop": True, "reason": "semantic_drift_alarm", "coverage_claim": "not_proven_complete"}
    if budget_remaining == 0:
        return {"stop": True, "reason": "budget_exhausted", "coverage_claim": "not_proven_complete"}
    if rounds and rounds[-1].get("new_relevant_count") is None:
        return {"stop": False, "reason": "awaiting_human_judgments", "coverage_claim": "not_proven_complete"}
    if len(rounds) >= 2:
        tail = rounds[-2:]
        if all(item.get("new_relevant_count") == 0 and item.get("new_term_count") == 0 for item in tail) and branches_remaining == 0:
            return {"stop": True, "reason": "two_low_gain_rounds_and_no_unexplored_branches", "coverage_claim": "not_proven_complete"}
    return {"stop": False, "reason": "continue", "coverage_claim": "not_proven_complete"}


def analyze_omissions(
    keyword_paper_ids: list[str],
    discovery_papers: list[dict[str, Any]],
    *,
    human_labels: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Identify human-confirmed records absent from the keyword channel.

    Observation only: phrases are not automatically equivalent or query-ready.
    """
    from .keyword_extractor import extract_terms
    from .models import Paper

    existing = set(keyword_paper_ids)
    human = human_labels or {}
    missed: list[str] = []
    candidates: dict[str, dict[str, Any]] = {}
    for record in discovery_papers:
        paper_id = record.get("paper_id")
        if not isinstance(paper_id, str) or not paper_id:
            raise ValueError("discovery paper requires paper_id")
        if record.get("channel") not in {"semantic", "citation", "recommendation", "reference", "citations", "references"}:
            raise ValueError("omission evidence requires an independent discovery channel")
        if paper_id in existing or human.get(paper_id) != "relevant":
            continue
        missed.append(paper_id)
        paper = Paper(paper_id, record.get("title", ""), abstract=record.get("abstract"),
                      database_keywords=record.get("database_keywords", []))
        for occurrence in extract_terms(paper):
            if len(occurrence.term.split()) < 2:
                continue
            candidate = candidates.setdefault(occurrence.term, {
                "term": occurrence.term, "status": "candidate", "adopted": False,
                "relationship": "unclassified", "source_paper_ids": [],
                "action": "review_relationship_then_test_separate_query",
            })
            if paper_id not in candidate["source_paper_ids"]:
                candidate["source_paper_ids"].append(paper_id)
    return {"missed_relevant_ids": list(dict.fromkeys(missed)),
            "candidate_terms": [candidates[key] for key in sorted(candidates)][:50],
            "coverage_claim": "comparison_of_observed_channels_only"}
