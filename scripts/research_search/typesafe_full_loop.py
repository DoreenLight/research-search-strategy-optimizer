"""Jev decisions across the full research-search loop, never human truth."""
from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Any, Callable, Mapping, Sequence

from .typesafe_reranker import RerankConfig, normalize_typesafe_answer


@dataclass(frozen=True)
class FullLoopConfig:
    api_key: str | None = None
    model: str = "jev-latest"
    route: str = "jev@typesafe"
    max_terms: int = 50
    max_papers: int = 100
    min_confidence: float = 0.0

    def __post_init__(self) -> None:
        if self.route != "jev@typesafe":
            raise ValueError("route must be jev@typesafe")
        if type(self.max_terms) is not int or self.max_terms <= 0 or type(self.max_papers) is not int or self.max_papers <= 0:
            raise ValueError("limits must be positive integers")
        if not 0 <= self.min_confidence <= 1:
            raise ValueError("min_confidence must be between 0 and 1")


def _judge(config: FullLoopConfig, judger: Callable[..., Mapping[str, Any]] | None, state: dict[str, Any]) -> Mapping[str, Any]:
    if judger is not None:
        return judger(state, model=config.model, route=config.route)
    if not config.api_key:
        raise RuntimeError("TYPESAFE_API_KEY_not_configured")
    from .typesafe_reranker import _sdk_judger
    return _sdk_judger(RerankConfig(api_key=config.api_key, model=config.model, route=config.route))(state, model=config.model)


def _unexecuted(config: FullLoopConfig, count: int, reason: str) -> dict[str, Any]:
    return {"status": "not_executed", "route": config.route, "model": config.model,
            "request_count": 0, "candidate_count": count, "skipped_count": 0,
            "judgments": [], "human_relevance_claim": False, "reason": reason}


def judge_term_candidates(
    research_scope: Mapping[str, Any], candidates: Sequence[Mapping[str, Any]], *,
    config: FullLoopConfig | None = None, judger: Callable[..., Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    config = config or FullLoopConfig(api_key=os.getenv("TYPESAFE_API_KEY"))
    selected = list(candidates)[:config.max_terms]
    if judger is None and not config.api_key:
        result = _unexecuted(config, len(selected), "TYPESAFE_API_KEY_not_configured")
        result["skipped_count"] = max(0, len(candidates) - len(selected))
        return result
    judgments: list[dict[str, Any]] = []
    for candidate in selected:
        try:
            raw = _judge(config, judger, {"research_scope": dict(research_scope), "candidate_term": dict(candidate)})
            answers = raw.get("answers", {})
            fit = normalize_typesafe_answer({"answers": {"relevance": answers.get("direct_fit", {})}, "model": raw.get("model"), "usage": raw.get("usage")})
            drift = normalize_typesafe_answer({"answers": {"relevance": answers.get("scope_drift", {})}})
            relationship_answer = answers.get("relationship", {})
            relationship = relationship_answer.get("choice", "unclassified") if isinstance(relationship_answer, Mapping) else "unclassified"
            confidence = fit.get("confidence")
            low = confidence is not None and confidence < config.min_confidence
            judgments.append({
                "term": candidate.get("term"), "relationship": relationship, "direct_fit": fit["score"],
                "scope_drift": drift["score"], "confidence": confidence, "model": raw.get("model", config.model),
                "usage": raw.get("usage"), "evidence_ids": candidate.get("evidence_ids", []),
                "adopted": False, "action": "human_review" if relationship == "equivalent" and not low else "test_as_separate_query_or_review",
                "error_type": "low_confidence" if low else None,
            })
        except Exception as error:
            judgments.append({"term": candidate.get("term"), "relationship": "unclassified", "direct_fit": None,
                              "scope_drift": None, "confidence": None, "model": config.model,
                              "usage": None, "evidence_ids": candidate.get("evidence_ids", []),
                              "adopted": False, "action": "human_review", "error_type": "jev_error",
                              "error_message": str(error)[:300]})
    return {"status": "partial" if any(j["error_type"] for j in judgments) else "success", "route": config.route,
            "model": config.model, "request_count": len(judgments), "candidate_count": len(selected),
            "skipped_count": max(0, len(candidates) - len(selected)), "judgments": judgments,
            "human_relevance_claim": False}


def judge_paper_candidates(
    research_scope: Mapping[str, Any], papers: Sequence[Mapping[str, Any]], *,
    config: FullLoopConfig | None = None, judger: Callable[..., Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    config = config or FullLoopConfig(api_key=os.getenv("TYPESAFE_API_KEY"))
    selected = list(papers)[:config.max_papers]
    if judger is None and not config.api_key:
        result = _unexecuted(config, len(selected), "TYPESAFE_API_KEY_not_configured")
        result["skipped_count"] = max(0, len(papers) - len(selected))
        return result
    judgments: list[dict[str, Any]] = []
    for paper in selected:
        try:
            raw = _judge(config, judger, {"research_scope": dict(research_scope), "paper": dict(paper)})
            answers = raw.get("answers", {})
            direct = normalize_typesafe_answer({"answers": {"relevance": answers.get("direct_relevance", {})}})
            fit = normalize_typesafe_answer({"answers": {"relevance": answers.get("scope_fit", {})}})
            confidence = direct.get("confidence")
            action = "human_review"
            if paper.get("channel") in {"semantic", "citation", "reference", "recommendation"}:
                action = "human_review" if direct["score"] < 0.8 or (confidence is not None and confidence < 0.8) else "independent_channel_candidate"
            judgments.append({"paper_id": paper.get("paper_id"), "channel": paper.get("channel", "keyword"),
                              "seed_ids": paper.get("seed_ids", []), "direct_relevance": direct["score"],
                              "scope_fit": fit["score"], "confidence": confidence, "model": raw.get("model", config.model),
                              "usage": raw.get("usage"), "action": action, "human_label": None,
                              "human_relevance_claim": False, "error_type": None})
        except Exception as error:
            judgments.append({"paper_id": paper.get("paper_id"), "channel": paper.get("channel", "keyword"),
                              "seed_ids": paper.get("seed_ids", []), "direct_relevance": None, "scope_fit": None,
                              "confidence": None, "model": config.model, "usage": None,
                              "action": "human_review", "human_label": None, "human_relevance_claim": False,
                              "error_type": "jev_error", "error_message": str(error)[:300]})
    return {"status": "partial" if any(j["error_type"] for j in judgments) else "success", "route": config.route,
            "model": config.model, "request_count": len(judgments), "candidate_count": len(selected),
            "skipped_count": max(0, len(papers) - len(selected)), "judgments": judgments,
            "human_relevance_claim": False}


def prioritize_review_queue(papers: Sequence[Mapping[str, Any]], judgments: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    by_id = {item.get("paper_id"): item for item in judgments}
    queue = []
    for paper in papers:
        item = by_id.get(paper.get("paper_id"))
        if not item:
            continue
        score, confidence = item.get("direct_relevance"), item.get("confidence")
        independent = paper.get("channel") in {"semantic", "citation", "reference", "recommendation"}
        if independent and confidence is not None and confidence < 0.8:
            reason = "independent_discovery_low_confidence"
        elif independent and isinstance(score, (int, float)) and score < 0.8:
            reason = "independent_discovery_low_model_score"
        else:
            reason = "model_human_review"
        queue.append({"paper_id": paper.get("paper_id"), "title": paper.get("title"),
                      "priority_reason": reason, "jev_score": score, "confidence": confidence,
                      "channel": paper.get("channel", "keyword"), "human_label": None})
    return sorted(queue, key=lambda item: (item["priority_reason"] == "model_human_review", -(item["confidence"] if item["confidence"] is not None else 0)))


def recommend_version_action(
    active_ids: Sequence[str], candidate_ids: Sequence[str], model_judgments: Sequence[Mapping[str, Any]],
    *, human_labels: Mapping[str, str],
) -> dict[str, Any]:
    active = set(active_ids)
    candidate = set(candidate_ids)
    lost = sorted(active - candidate)
    new = sorted(candidate - active)
    conflicts = [item for item in model_judgments if item.get("paper_id") in new and item.get("confidence", 0) is not None and item.get("confidence", 0) < 0.8]
    unknown = [paper_id for paper_id in new if human_labels.get(paper_id) not in {"relevant", "irrelevant"}]
    if lost or unknown or conflicts:
        action = "pending_review" if unknown or conflicts else "rollback_candidate"
    elif any(human_labels.get(paper_id) == "relevant" for paper_id in new):
        action = "retain_candidate"
    else:
        action = "rollback_candidate"
    return {"recommended_action": action, "active_version_change": False,
            "lost_active_ids": lost, "new_candidate_ids": new, "unknown_new_ids": unknown,
            "low_confidence_ids": [item.get("paper_id") for item in conflicts],
            "human_gate": "satisfied_for_review_not_automatic_truth" if human_labels else "required",
            "human_relevance_claim": False}
