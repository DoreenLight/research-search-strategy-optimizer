"""Explicit P2 execution plans shared by the CLI and Research Search Package."""
from __future__ import annotations

import hashlib
import json
import time
from typing import Any, Mapping
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

from .base import ProviderFailure, redact_value
from .models import SearchRequest
from .pubmed import PubMedProvider
from .semantic_scholar import SemanticScholarProvider

_CHANNELS = {"keyword", "semantic_recommendation", "citation", "reference"}
_TYPES = {"pubmed": PubMedProvider, "semantic_scholar": SemanticScholarProvider}


class _RejectRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise HTTPError(req.full_url, code, "redirect refused", headers, fp)


class ProviderTransport:
    """Rate-limited public-API transport; no redirects or implicit credentials."""

    def __init__(self, interval: float = 0.35) -> None:
        self.interval = interval
        self.last_request: dict[str, float] = {}
        self.opener = build_opener(_RejectRedirects())

    def __call__(self, request: Request, *, timeout: float):
        host = urlsplit(request.full_url).hostname
        if host not in {"eutils.ncbi.nlm.nih.gov", "api.semanticscholar.org"}:
            raise ProviderFailure("invalid_endpoint", "provider endpoint is not allowed")
        delay = self.interval - (time.monotonic() - self.last_request.get(host, 0))
        if delay > 0:
            time.sleep(delay)
        self.last_request[host] = time.monotonic()
        request.add_header("User-Agent", "research-search-strategy-optimizer/0.1")
        return self.opener.open(request, timeout=timeout)


def _invoke(provider, item: dict[str, Any], mode: str):
    if item["channel"] == "keyword":
        return provider.search(SearchRequest(item["query"], item["filters"], item["limit"], mode))
    if item["channel"] == "semantic_recommendation":
        return provider.recommend(item["seed_ids"], limit=item["limit"], mode=mode, filters=item["filters"])
    return provider.citations(item["seed_ids"][0], direction="citations" if item["channel"] == "citation" else "references",
                              limit=item["limit"], mode=mode, filters=item["filters"])


def validate_provider_plan(plan: Any) -> list[dict[str, Any]]:
    if not isinstance(plan, list):
        raise ValueError("provider_plan must be an array")
    items = []
    for index, original in enumerate(plan):
        allowed = {"provider", "query", "filters", "limit", "channel", "seed_ids", "query_type"}
        if not isinstance(original, dict) or set(original) - allowed or original.get("provider") not in _TYPES:
            raise ValueError("invalid provider plan entry")
        provider_name = original["provider"]
        channel = original.get("channel", "keyword")
        if channel not in _CHANNELS or (provider_name == "pubmed" and channel != "keyword"):
            raise ValueError("unsupported provider/channel combination")
        item = {"provider": provider_name, "channel": channel, "query": original.get("query", ""),
                "filters": original.get("filters", {}), "limit": original.get("limit", 5),
                "seed_ids": original.get("seed_ids", [])}
        if not isinstance(item["filters"], dict) or any(name in item["filters"] for name in {"api_key", "email", "tool"}):
            raise ValueError("provider plan filters cannot contain credentials/contact parameters")
        if type(item["limit"]) is not int or not 1 <= item["limit"] <= 100:
            raise ValueError("provider plan limit must be 1..100")
        if channel != "keyword":
            seeds = item["seed_ids"]
            if not isinstance(seeds, list) or not seeds or any(not isinstance(seed, str) or not seed.strip() for seed in seeds):
                raise ValueError("discovery plans require explicit seed_ids")
            if channel != "semantic_recommendation" and len(seeds) != 1:
                raise ValueError("citation/reference plan requires exactly one seed")
        if redact_value(item) != item:
            raise ValueError("provider plan must not contain credentials")
        provider = _TYPES[provider_name](api_key="")
        preview = _invoke(provider, item, "planned")
        if preview.status != "planned":
            raise ValueError(f"invalid provider plan: {preview.error_message}")
        query_type = ("mesh_plus_free_text" if item["filters"].get("mesh_terms") else "free_text") if provider_name == "pubmed" else channel
        if original.get("query_type", query_type) != query_type:
            raise ValueError("query_type contradicts the actual provider request")
        item["query_type"] = query_type
        item["plan_id"] = "provider-" + hashlib.sha256(json.dumps(item, sort_keys=True, allow_nan=False).encode()).hexdigest()[:16]
        if any(previous["plan_id"] == item["plan_id"] for previous in items):
            raise ValueError("duplicate provider plan")
        item["plan_index"] = index
        items.append(item)
    return items


__all__ = ["ProviderTransport", "validate_provider_plan", "execute_provider_plan"]


def execute_provider_plan(plan: list[dict[str, Any]], *, live: bool = False,
                          transports: Mapping[str, Any] | None = None, max_requests: int = 0,
                          api_keys: Mapping[str, str] | None = None,
                          use_default_public_transport: bool = False) -> list[dict[str, Any]]:
    """Validate all requests first, then execute within one shared P2 budget."""
    if type(live) is not bool or type(max_requests) is not int or max_requests < 0:
        raise ValueError("invalid provider execution mode/budget")
    originals = [{key: value for key, value in item.items() if key not in {"plan_id", "plan_index"}} for item in plan]
    items = validate_provider_plan(originals)
    remaining = max_requests
    results = []
    for item in items:
        transport = (transports or {}).get(item["provider"]) if live else None
        if live and transport is None and use_default_public_transport:
            transport = ProviderTransport()
        provider = _TYPES[item["provider"]](transport=transport, max_requests=remaining, timeout=20,
                                            api_key=(api_keys or {}).get(item["provider"], ""))
        result = _invoke(provider, item, "live" if live else "planned")
        remaining -= result.request_count
        if remaining < 0:
            raise ValueError("provider exceeded request budget")
        results.append({**result.to_dict(), "plan_id": item["plan_id"], "query_type": item["query_type"],
                        "channel": item["channel"], "request": item,
                        "ingestion_mode": "live" if live else "planned",
                        "historical_request_count": 0, "new_network_request_count": result.request_count})
    return results
