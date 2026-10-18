"""Offline-first Semantic Scholar Graph/Recommendations metadata adapters."""
from __future__ import annotations

from collections.abc import Mapping, Sequence
import json
from typing import Any
from urllib.parse import quote, urlencode
from urllib.request import Request

from .base import Provider, ProviderFailure, coerce_request, decode_json_count, now_utc, redact_value
from .models import ProviderPaper, ProviderResult, SearchRequest


class SemanticScholarProvider(Provider):
    """One request per call, no implicit auth, retries, pagination or quota promise."""

    name = "semantic_scholar"
    search_url = "https://api.semanticscholar.org/graph/v1/paper/search"
    recommendations_url = "https://api.semanticscholar.org/recommendations/v1/papers/"
    graph_url = "https://api.semanticscholar.org/graph/v1/paper"
    default_fields = "paperId,title,abstract,authors,venue,journal,year,externalIds,citationCount,referenceCount"
    search_filters = {"offset", "minCitationCount", "year", "publicationTypes", "publicationDateOrYear", "venue", "fieldsOfStudy", "openAccessPdf"}

    @classmethod
    def _fields(cls, filters: Mapping[str, Any]) -> str:
        fields = filters.get("fields", cls.default_fields)
        if isinstance(fields, (list, tuple)):
            if any(not isinstance(value, str) or not value.strip() for value in fields):
                raise ValueError("fields must contain non-empty strings")
            fields = ",".join(fields)
        if not isinstance(fields, str) or not fields.strip():
            raise ValueError("fields must be a non-empty string or string array")
        return fields

    def search(self, request: SearchRequest | Mapping[str, Any]) -> ProviderResult:
        request = coerce_request(request)
        try:
            if set(request.filters) - self.search_filters - {"fields"}:
                raise ValueError("unsupported Semantic Scholar search filters")
            if request.limit > 100:
                raise ValueError("paper/search limit must be at most 100; pagination is not implemented")
            params = {"query": request.query, "limit": request.limit, "fields": self._fields(request.filters)}
            params.update({key: value for key, value in request.filters.items() if key in self.search_filters})
            # The official openAccessPdf parameter is a presence-only flag.
            if "openAccessPdf" in params:
                if params["openAccessPdf"] is False:
                    params.pop("openAccessPdf")
                else:
                    params["openAccessPdf"] = ""
            plan = {"endpoint": self.search_url, "method": "GET", "params": params, "channel": "keyword"}
        except (ValueError, TypeError) as error:
            return self._failed(request, {}, ProviderFailure("invalid_request", str(error)))
        return self._execute(request, plan)

    def recommend(self, seed_ids: Sequence[str] | str, *, limit: int = 20, mode: str = "planned",
                  filters: Mapping[str, Any] | None = None) -> ProviderResult:
        """Plan/execute POST recommendations; similarity is not a citation edge."""
        seeds = [seed_ids] if isinstance(seed_ids, str) else list(seed_ids)
        if not seeds or any(not isinstance(seed, str) or not seed.strip() for seed in seeds):
            raise ValueError("seed_ids must contain non-empty strings")
        seeds = list(dict.fromkeys(seed.strip() for seed in seeds))
        request = SearchRequest(json.dumps({"seed_ids": seeds, "channel": "semantic_recommendation"}, sort_keys=True), filters or {}, limit, mode)
        try:
            if set(request.filters) - {"fields"}:
                raise ValueError("recommend filters support fields only")
            if limit > 500:
                raise ValueError("recommendation limit must be at most 500")
            plan = {
                "endpoint": self.recommendations_url, "method": "POST",
                "params": {"limit": limit, "fields": self._fields(request.filters)},
                "body": {"positivePaperIds": seeds, "negativePaperIds": []},
                "channel": "semantic_recommendation", "discovery_channel": True,
                "candidate_reason": "semantic_recommendation", "seed_ids": seeds,
                "relationship_semantics": "similarity recommendation, not direct citation",
            }
        except (ValueError, TypeError) as error:
            return self._failed(request, {}, ProviderFailure("invalid_request", str(error)))
        return self._execute(request, plan)

    recommendations = recommend

    def citations(self, seed_id: str, *, direction: str = "citations", limit: int = 20,
                  mode: str = "planned", filters: Mapping[str, Any] | None = None) -> ProviderResult:
        """citations => citingPaper; references => citedPaper, never inferred edges."""
        if not isinstance(seed_id, str) or not seed_id.strip():
            raise ValueError("seed_id must be a non-empty string")
        if direction not in {"citations", "references"}:
            raise ValueError("direction must be citations or references")
        seed_id = seed_id.strip()
        channel = "citation" if direction == "citations" else "reference"
        request = SearchRequest(json.dumps({"seed_id": seed_id, "channel": channel}, sort_keys=True), filters or {}, limit, mode)
        try:
            if set(request.filters) - {"fields", "offset"}:
                raise ValueError("citation filters support fields/offset only")
            if limit > 1000:
                raise ValueError("citation/reference limit must be at most 1000")
            params = {"limit": limit, "fields": self._fields(request.filters)}
            if "offset" in request.filters:
                params["offset"] = request.filters["offset"]
            plan = {
                "endpoint": f"{self.graph_url}/{quote(seed_id, safe='')}/{direction}", "method": "GET",
                "params": params, "channel": channel, "discovery_channel": True,
                "candidate_reason": "citation_from_seed" if direction == "citations" else "reference_from_seed",
                "seed_ids": [seed_id], "relationship_semantics": "explicit provider citation/reference edge",
            }
        except (ValueError, TypeError) as error:
            return self._failed(request, {}, ProviderFailure("invalid_request", str(error)))
        return self._execute(request, plan)

    citation = citations

    def _execute(self, request: SearchRequest, plan: dict[str, Any]) -> ProviderResult:
        plan = redact_value(plan, self._secrets(request))
        deferred = self._preflight(request, plan)
        if deferred:
            return deferred
        before, executed_at = self._requests_made, now_utc()
        raw: dict[str, Any] = {"plan": plan}
        try:
            # Parameters belong in the URL for both GET and POST APIs.
            url = plan["endpoint"] + "?" + urlencode(plan["params"])
            body = json.dumps(plan["body"]).encode("utf-8") if "body" in plan else None
            headers = {"Accept": "application/json"}
            if body:
                headers["Content-Type"] = "application/json"
            if self.api_key:
                headers["x-api-key"] = self.api_key
            payload = self._send(Request(url, data=body, headers=headers, method=plan["method"]), secrets=self._secrets(request))
            result = self.parse_response(payload, request, channel=plan["channel"], seed_ids=plan.get("seed_ids"),
                                         candidate_reason=plan.get("candidate_reason"))
            result.request_count, result.executed_at = self._requests_made - before, executed_at
            result.raw_response = {"plan": plan, "response": result.raw_response}
            return result
        except (ValueError, TypeError, UnicodeError) as error:
            return self._failed(request, raw, error, request_count=self._requests_made - before, executed_at=executed_at)

    def parse_response(self, payload: Any, request: SearchRequest, *, channel: str = "keyword",
                       seed_ids: Sequence[str] | None = None, candidate_reason: str | None = None) -> ProviderResult:
        """Offline parse: no transport, request budget, execution timestamp or recall."""
        request = coerce_request(request)
        raw = None
        try:
            if isinstance(payload, bytes):
                payload = payload.decode("utf-8")
            if isinstance(payload, str):
                payload = json.loads(payload)
            raw = redact_value(payload, self._secrets(request))
            if not isinstance(raw, Mapping):
                raise ValueError("expected Semantic Scholar response object")
            if raw.get("error") or raw.get("message") and "data" not in raw and "recommendedPapers" not in raw:
                raise ProviderFailure("provider_error", "Semantic Scholar reported an error")
            if channel not in {"keyword", "semantic_recommendation", "citation", "reference"}:
                raise ValueError("unsupported discovery channel")
            if channel != "keyword" and (not seed_ids or any(not isinstance(seed, str) or not seed for seed in seed_ids)):
                raise ValueError("discovery results require explicit seed_ids")
            collection = "recommendedPapers" if channel == "semantic_recommendation" else "data"
            values = raw.get(collection)
            if not isinstance(values, list):
                raise ValueError(f"Semantic Scholar response requires {collection}[]")
            count = decode_json_count(raw["total"]) if "total" in raw else None
            warnings, papers = [], []
            for value in values[:request.limit]:
                if not isinstance(value, Mapping):
                    warnings.append("paper_record_invalid")
                    continue
                edge = value
                if channel in {"citation", "reference"}:
                    value = value.get("citingPaper" if channel == "citation" else "citedPaper")
                paper = self._paper(value, channel=channel, seed_ids=list(seed_ids or []), candidate_reason=candidate_reason)
                if paper is None:
                    warnings.append("paper_missing_id_or_title")
                else:
                    if channel in {"citation", "reference"}:
                        paper.raw = {"paper": dict(value), "edge": dict(edge)}
                    papers.append(paper)
            return ProviderResult(self.name, "partial" if warnings else "success", reported_count=count,
                                  fetched_count=len(papers), papers=papers, raw_response=raw,
                                  error_type="partial_records" if warnings else None,
                                  error_message="; ".join(warnings) if warnings else None,
                                  source_level="A", query_hash=request.query_hash)
        except (ValueError, TypeError, UnicodeError) as error:
            return self._failed(request, raw, error)

    @staticmethod
    def _paper(record: Any, *, channel: str, seed_ids: list[str], candidate_reason: str | None) -> ProviderPaper | None:
        if not isinstance(record, Mapping):
            return None
        paper_id, title = record.get("paperId"), record.get("title")
        if not isinstance(paper_id, str) or not paper_id.strip() or not isinstance(title, str) or not title.strip():
            return None
        external = record.get("externalIds") or {}
        if not isinstance(external, Mapping):
            return None
        authors = record.get("authors") or []
        if not isinstance(authors, list):
            return None
        field_sources = {"s2_paper_id": "Semantic Scholar API / paperId", "title": "Semantic Scholar API / title"}
        for field, source in (("doi", "externalIds.DOI"), ("pmid", "externalIds.PubMed"), ("abstract", "abstract"),
                              ("authors", "authors"), ("citation_count", "citationCount")):
            if field in {"doi", "pmid"}:
                present = external.get("DOI" if field == "doi" else "PubMed")
            else:
                present = source in record
            if present:
                field_sources[field] = "Semantic Scholar API / " + source
        journal_value = record.get("journal")
        journal = journal_value.get("name") if isinstance(journal_value, Mapping) else None
        if journal:
            field_sources["journal"] = "Semantic Scholar API / journal.name"
        else:
            journal = record.get("venue")
            if journal:
                field_sources["journal"] = "Semantic Scholar API / venue"
        def ids(key: str) -> list[str]:
            items = record.get(key) or []
            return [item["paperId"] for item in items if isinstance(item, Mapping) and isinstance(item.get("paperId"), str)] if isinstance(items, list) else []
        citation_source = "Semantic Scholar API / citations" if "citations" in record or channel == "citation" else None
        references_source = "Semantic Scholar API / references" if "references" in record or channel == "reference" else None
        reason = candidate_reason or ({"semantic_recommendation": "semantic_recommendation", "citation": "citation_from_seed", "reference": "reference_from_seed"}.get(channel))
        return ProviderPaper(
            "semantic_scholar", paper_id.strip(), title.strip(), s2_paper_id=paper_id.strip(),
            doi=external.get("DOI"), pmid=external.get("PubMed"),
            abstract=record.get("abstract") if isinstance(record.get("abstract"), str) else None,
            authors=[author["name"] for author in authors if isinstance(author, Mapping) and isinstance(author.get("name"), str)],
            journal=journal if isinstance(journal, str) else None,
            publication_year=record.get("year") if type(record.get("year")) is int else None,
            citation_count=record.get("citationCount") if type(record.get("citationCount")) is int else None,
            citation_ids=ids("citations"), reference_ids=ids("references"), citation_source=citation_source,
            references_source=references_source, source_url=f"https://www.semanticscholar.org/paper/{paper_id.strip()}",
            field_sources=field_sources, channel=channel, discovery_channel=channel != "keyword",
            candidate_reason=reason, seed_ids=seed_ids, raw=dict(record),
        )
