"""Optional Jev/TypeSafe Top-K reranking after deterministic retrieval.

This module never expands the candidate set, never turns a model score into a
human relevance label, and safely degrades to the provider order without a key.
"""
from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Any, Callable, Mapping, Sequence


@dataclass(frozen=True)
class RerankConfig:
    api_key: str | None = None
    # Public workflow alias is "jev@typesafe"; official SDK model is jev-latest.
    model: str = "jev-latest"
    route: str = "jev@typesafe"
    top_k: int = 20
    min_confidence: float = 0.0

    def __post_init__(self) -> None:
        if self.top_k <= 0:
            raise ValueError("top_k must be positive")
        if self.route != "jev@typesafe":
            raise ValueError("route must be jev@typesafe")
        if not 0 <= self.min_confidence <= 1:
            raise ValueError("min_confidence must be between 0 and 1")


def _score_from_answer(answer: Mapping[str, Any]) -> tuple[float, float | None]:
    if "noul" in answer:
        score = answer["noul"]
        if type(score) not in (int, float) or not 0 <= score <= 1:
            raise ValueError("noul must be between 0 and 1")
        confidence = answer.get("confidence")
        return float(score), float(confidence) if isinstance(confidence, (int, float)) else None
    if "score" in answer:
        probabilities = answer.get("probabilities")
        if not isinstance(probabilities, Mapping) or not probabilities:
            raise ValueError("score answer requires probabilities")
        values = {int(key): float(value) for key, value in probabilities.items()}
        total = sum(values.values())
        if total <= 0 or any(value < 0 for value in values.values()):
            raise ValueError("invalid score probabilities")
        normalized = {key: value / total for key, value in values.items()}
        # Convert ordered Score levels to a normalized 0..1 ranking score.
        top = max(normalized)
        score = sum(level * probability for level, probability in normalized.items()) / top if top else 0.0
        confidence = answer.get("confidence")
        return float(score), float(confidence) if isinstance(confidence, (int, float)) else None
    raise ValueError("answer must contain noul or score")


def normalize_typesafe_answer(response: Mapping[str, Any]) -> dict[str, Any]:
    answers = response.get("answers") if isinstance(response, Mapping) else None
    if not isinstance(answers, Mapping):
        raise ValueError("TypeSafe response missing answers")
    answer = answers.get("relevance")
    if not isinstance(answer, Mapping):
        # Permit one-question responses with a different ID while keeping type safety.
        answer = next(iter(answers.values()), None)
    if not isinstance(answer, Mapping):
        raise ValueError("TypeSafe response missing relevance answer")
    score, confidence = _score_from_answer(answer)
    return {"score": score, "confidence": confidence, "type": answer.get("type"), "raw": dict(response)}


def _sdk_judger(config: RerankConfig) -> Callable[..., Mapping[str, Any]]:
    from typesafe_sdk import Noul, NoulCriteria, TypeSafeClient

    client = TypeSafeClient(api_key=config.api_key, timeout=60.0)
    question = Noul(
        instructions="How directly does this candidate paper answer the research query?",
        criteria=NoulCriteria(
            true="The paper directly studies the requested research object, input modality, and task; method terms may be absent.",
            false="The paper is only adjacent, shares a broad topic, or misses the core research object/input/task.",
        ),
    )

    def judge(state: Mapping[str, Any], **_: Any) -> Mapping[str, Any]:
        with client:
            response = client.system_one(
                model=config.model,
                state=state,
                questions={"relevance": question},
            )
        return response.model_dump() if hasattr(response, "model_dump") else response

    return judge


def rerank_papers(
    query: str,
    papers: Sequence[Mapping[str, Any]],
    *,
    config: RerankConfig | None = None,
    judger: Callable[..., Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Rerank an existing shortlist with Jev; never expand it or label truth."""
    config = config or RerankConfig(api_key=os.getenv("TYPESAFE_API_KEY"))
    records = [dict(paper) for paper in papers]
    top = records[:config.top_k]
    if not top:
        return {"status": "not_executed", "model": config.model, "ordered_paper_ids": [],
                "scores": [], "request_count": 0, "human_relevance_claim": False,
                "reason": "empty_candidate_shortlist"}
    if judger is None and not config.api_key:
        return {"status": "not_executed", "route": config.route, "model": config.model,
                "ordered_paper_ids": [paper.get("paper_id") for paper in records], "scores": [],
                "request_count": 0, "human_relevance_claim": False,
                "reason": "TYPESAFE_API_KEY_not_configured"}
    judge = judger or _sdk_judger(config)
    scored: list[dict[str, Any]] = []
    for index, paper in enumerate(top):
        try:
            raw = judge({"query": query, "paper": paper}, model=config.model)
            normalized = normalize_typesafe_answer(raw)
            if normalized["confidence"] is not None and normalized["confidence"] < config.min_confidence:
                normalized["error_type"] = "low_confidence"
            scored.append({"paper_id": paper.get("paper_id"), "original_rank": index + 1,
                           "score": normalized["score"], "noul": normalized["score"],
                           "confidence": normalized["confidence"], "model": raw.get("model", config.model),
                           "usage": raw.get("usage"), "error_type": normalized.get("error_type")})
        except Exception as error:
            scored.append({"paper_id": paper.get("paper_id"), "original_rank": index + 1,
                           "score": None, "noul": None, "confidence": None, "model": config.model,
                           "usage": None, "error_type": "invalid_answer", "error_message": str(error)[:300]})
    valid = [item for item in scored if item["score"] is not None and item.get("error_type") != "low_confidence"]
    if len(valid) != len(scored):
        return {"status": "partial", "route": config.route, "model": config.model,
                "ordered_paper_ids": [paper.get("paper_id") for paper in records], "scores": scored,
                "request_count": len(scored), "human_relevance_claim": False,
                "reason": "one_or_more_jev_scores_unusable"}
    ordered_top = [item["paper_id"] for item in sorted(scored, key=lambda item: (-item["score"], item["original_rank"]))]
    tail = [paper.get("paper_id") for paper in records[config.top_k:]]
    rank_by_id = {paper_id: index + 1 for index, paper_id in enumerate(ordered_top)}
    ranked_scores = sorted(scored, key=lambda item: rank_by_id.get(item["paper_id"], item["original_rank"]))
    for item in ranked_scores:
        item["reranked_rank"] = rank_by_id[item["paper_id"]]
    return {"status": "success", "route": config.route, "model": config.model,
            "ordered_paper_ids": ordered_top + tail, "scores": ranked_scores,
            "request_count": len(scored), "human_relevance_claim": False,
            "candidate_set_changed": False, "reason": "Jev reranked existing shortlist only"}
