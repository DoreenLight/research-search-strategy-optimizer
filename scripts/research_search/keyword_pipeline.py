"""Rank field observations without mistaking frequency for semantic approval."""
from __future__ import annotations

from typing import Any

from .keyword_normalizer import normalize_term

DEFAULT_CANDIDATE_LIMIT = 50


def keyword_layers(
    keywords: list[dict[str, Any]], evidence: list[dict[str, Any]], *,
    limit: int = DEFAULT_CANDIDATE_LIMIT, reviews: list[dict[str, Any]] = (),
) -> dict[str, Any]:
    if type(limit) is not int or not 1 <= limit <= 500:
        raise ValueError("candidate_limit must be between 1 and 500")
    by_evidence = {item["evidence_id"]: item for item in evidence}
    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in keywords:
        grouped.setdefault(item["term"], []).append(item)
    observations = []
    merged = []
    for term, records in sorted(grouped.items()):
        evidence_ids = sorted({eid for item in records for eid in item["evidence_ids"]})
        sources = [by_evidence[eid] for eid in evidence_ids]
        for source in sources:
            observations.append({
                "term": term, "source_field": source["locator"], "paper_id": source["paper_id"],
                "excerpt": source["excerpt"], "evidence_id": source["evidence_id"],
                "evidence_status": "database_assigned" if source["locator"] == "database_keywords" else "observed_in_paper",
                "source_url": source["source_url"], "run_ids": source["run_ids"],
                "retrieved_at": source["retrieved_at"], "evidence_level": source["evidence_level"],
            })
        preferred = min(records, key=lambda item: (
            item["source_type"] == "llm_candidate", item["source_type"] != "openalex_keyword", item["term_id"],
        ))
        merged.append({**preferred, "evidence_ids": evidence_ids,
                       "paper_ids": sorted({source["paper_id"] for source in sources}),
                       "document_frequency": len({source["paper_id"] for source in sources})})
    reviews_by_term: dict[str, dict[str, Any]] = {}
    for review in reviews:
        term = normalize_term(review["term"])
        if term not in grouped:
            raise ValueError(f"reviewed keyword is not in the observed/input term inventory: {term}")
        if term in reviews_by_term:
            raise ValueError(f"duplicate keyword review: {term}")
        if review["adopted"] and (review["review_status"] != "approved" or review["relationship"] == "unclassified"):
            raise ValueError("adopted keyword requires an approved, classified review")
        reviews_by_term[term] = review
    reviewed = []
    ranked = []
    for item in merged:
        term = item["term"]
        sources = [by_evidence[eid] for eid in item["evidence_ids"]]
        fields = sorted({source["locator"] for source in sources})
        review = reviews_by_term.get(term)
        if review:
            if review["adopted"] and not sources:
                raise ValueError("adopted keyword requires locatable external field evidence")
            item.update(relationship=review["relationship"], adopted=review["adopted"])
            if sources and review["review_status"] == "approved":
                item["evidence_status"] = "reviewed"
            reviewed.append({**item, **review, "term": term})
        # All observations remain available, but singleton abstract fragments and
        # numeric-only artifacts are not a useful human review shortlist.
        eligible = any(character.isalpha() for character in term) and (
            review is not None or "database_keywords" in fields or "author_keywords" in fields
            or ("title" in fields and len(term.split()) >= 2) or item["document_frequency"] >= 2
            or item["source_type"] == "llm_candidate"
        )
        if eligible:
            ranked.append((item, fields, review))
    ranked.sort(key=lambda entry: (
        entry[2] is None,
        -entry[0]["document_frequency"],
        not bool({"database_keywords", "author_keywords"} & set(entry[1])),
        "title" not in entry[1], -len(entry[1]),
        entry[0]["source_type"] == "llm_candidate", entry[0]["term"],
    ))
    candidates = []
    compatibility = []
    for rank, (item, fields, review) in enumerate(ranked[:limit], 1):
        compatibility.append(dict(item))
        candidates.append({**item, "candidate_rank": rank, "source_fields": fields,
                           "source_field_count": len(fields),
                           "observed_in_multiple_papers": item["document_frequency"] > 1,
                           "review_status": review["review_status"] if review else "pending"})
    return {
        "observations": observations, "keywords": compatibility, "reviewed": reviewed,
        "candidates": {"schema_version": "0.1", "selection_limit": limit,
                       "raw_observation_count": len(observations), "observed_term_count": len(grouped),
                       "eligible_term_count": len(ranked), "candidate_count": len(candidates),
                       "deferred_candidate_count": max(0, len(ranked) - limit),
                       "selection_rule": "Reviewed first, document frequency, author/database labels, title, field diversity, lexical tie-break. Numeric-only and singleton abstract-only fragments excluded. Frequency is not semantic approval; independent provenance is not inferred.",
                       "terms": candidates},
    }
