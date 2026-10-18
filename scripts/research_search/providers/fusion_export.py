"""Offline, auditable export for already obtained P2 provider results."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .base import redact_value
from .fusion import fuse_results
from .models import ProviderPaper, ProviderResult


def _read(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError(f"invalid provider result JSON: {path}") from error
    if not isinstance(value, dict):
        raise ValueError("provider result must be an object")
    return value


def _result(value: dict[str, Any]) -> ProviderResult:
    required = {"provider", "status", "request_count", "reported_count", "fetched_count", "papers"}
    if not required.issubset(value) or not isinstance(value["papers"], list):
        raise ValueError("provider result is missing required fields")
    papers: list[ProviderPaper] = []
    for item in value["papers"]:
        if not isinstance(item, dict) or not item.get("provider") or not item.get("paper_id") or not item.get("title"):
            raise ValueError("provider paper requires provider, paper_id, and title")
        allowed = set(ProviderPaper.__dataclass_fields__)
        papers.append(ProviderPaper(**{key: item[key] for key in item if key in allowed}))
    result = ProviderResult(
        provider=value["provider"], status=value["status"], request_count=value["request_count"],
        reported_count=value.get("reported_count"), fetched_count=value["fetched_count"], papers=papers,
        raw_response=value.get("raw_response"), error_type=value.get("error_type"),
        error_message=value.get("error_message"), source_level=value.get("source_level", "U"),
        executed_at=value.get("executed_at"), query_hash=value.get("query_hash", ""),
    )
    if type(result.request_count) is not int or result.request_count < 0:
        raise ValueError("request_count must be non-negative")
    if type(result.fetched_count) is not int or result.fetched_count < 0:
        raise ValueError("fetched_count must be non-negative")
    if result.status not in {"planned", "not_executed", "success", "partial", "failed"}:
        raise ValueError("unsupported provider result status")
    return result


def _jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    path.write_text("".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records), encoding="utf-8")


def _write_manifest(output: Path, metadata: dict[str, Any]) -> None:
    files = {
        str(path.relative_to(output)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(output.rglob("*"))
        if path.is_file() and path.name != "manifest.json"
    }
    (output / "manifest.json").write_text(json.dumps({**metadata, "files": files}, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def export_provider_fusion(inputs: list[Path], output_dir: Path) -> dict[str, Any]:
    """Fuse local ProviderResult JSON files without network or source mutation."""
    if not isinstance(inputs, list) or not inputs:
        raise ValueError("inputs must be a non-empty list")
    output = Path(output_dir)
    if output.exists():
        raise FileExistsError(f"output directory already exists: {output}")
    paths = [Path(item) for item in inputs]
    if any(path.is_symlink() or not path.is_file() for path in paths):
        raise ValueError("provider input must be a regular file")
    values = [_read(path) for path in paths]
    results = [_result(value) for value in values]
    fused = fuse_results(results)
    historical_requests = sum(result.request_count for result in results)
    source_coverage: dict[str, dict[str, Any]] = {}
    for value, result in zip(values, results):
        details = source_coverage.setdefault(result.provider, {
            "request_count": 0, "reported_counts": [], "fetched_count": 0,
            "query_types": [], "input_result_count": 0,
        })
        details["request_count"] += result.request_count
        details["fetched_count"] += result.fetched_count
        details["input_result_count"] += 1
        if result.reported_count is not None:
            details["reported_counts"].append(result.reported_count)
        query_type = value.get("query_type")
        if query_type is None:
            query_type = next((paper.channel for paper in result.papers if paper.channel), "unknown")
        if query_type not in details["query_types"]:
            details["query_types"].append(query_type)
    for provider, details in source_coverage.items():
        details["reported_count"] = details["reported_counts"][0] if len(details["reported_counts"]) == 1 else None
        details["unique_provider_paper_count"] = len({paper.paper_id for result in results if result.provider == provider for paper in result.papers})
        details["deduplicated_count"] = fused.coverage_by_provider.get(provider, {}).get("fusion_count", 0)
        details.pop("reported_counts")
    payload = {
        "schema_version": "0.1", "mode": "offline_fusion", "new_network_request_count": 0,
        "historical_request_count": historical_requests, "source_coverage": source_coverage,
        "input_file_count": len(paths), "fusion": fused.to_dict(),
    }
    canonical_records = [paper.to_dict() for paper in fused.papers]
    source_records = [{"canonical_id": key, "records": redact_value(records)} for key, records in fused.source_records.items()]
    conflicts = [conflict.to_dict() for conflict in fused.conflicts]
    output.mkdir(parents=True, exist_ok=False)
    (output / "fusion.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _jsonl(output / "papers.jsonl", canonical_records)
    _jsonl(output / "source-records.jsonl", source_records)
    _jsonl(output / "conflicts.jsonl", conflicts)
    _write_manifest(output, {"schema_version": "0.1", "status": "completed", "mode": "offline_fusion", "summary": {
        "provider_count": len(fused.coverage_by_provider), "canonical_paper_count": len(canonical_records),
        "conflict_count": len(conflicts), "historical_request_count": historical_requests,
        "new_network_request_count": 0,
    }})
    return payload
