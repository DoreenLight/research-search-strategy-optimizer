"""Strict offline intake and aggregation for P4 dual-review evidence."""
from __future__ import annotations

from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
from typing import Any


_LABELS = {"relevant", "irrelevant", "pending", "uncertain"}
_DECISIVE = {"relevant", "irrelevant"}


def _clone(value: Any) -> Any:
    try:
        return json.loads(json.dumps(value, ensure_ascii=False, allow_nan=False))
    except (TypeError, ValueError) as error:
        raise ValueError("input must contain ordinary JSON values") from error


def _nonempty(value: Any, field: str) -> str:
    if type(value) is not str or not value.strip() or any(ord(char) < 32 for char in value):
        raise ValueError(f"{field} must be a non-empty single-line string")
    return value.strip()


def _safe_review_text(value: Any, field: str) -> str:
    text = _nonempty(value, field)
    if re.search(r"(?i)(?:api[_-]?key|access[_-]?token|authorization|bearer|client[_-]?secret|password|token)\s*(?:=|:|\s+)", text):
        raise ValueError(f"{field} contains a credential-shaped value")
    if re.search(r"(?i)(?:file://|(?:^|[ =])/(?:Users|private|home|tmp)/|[A-Za-z]:[\\/])", text):
        raise ValueError(f"{field} contains a local path")
    return text


def _iso_datetime(value: Any, field: str) -> str:
    text = _nonempty(value, field)
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError(f"{field} must be an ISO date-time") from error
    if parsed.tzinfo is None:
        raise ValueError(f"{field} must include a timezone")
    return text


def _ids(value: Any, field: str) -> list[str]:
    if type(value) is not list or not value:
        raise ValueError(f"{field} must be a non-empty string array")
    result = [_nonempty(item, f"{field} item") for item in value]
    if len(set(result)) != len(result):
        raise ValueError(f"{field} contains duplicate IDs")
    return result


def _load_reviewer(path: Path, pool: set[str]) -> tuple[str, dict[str, dict[str, Any]]]:
    if path.is_symlink() or not path.is_file():
        raise ValueError("reviewer input must be a regular file")
    reviewer_id: str | None = None
    rows: dict[str, dict[str, Any]] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"invalid reviewer JSONL line {line_number}") from error
        if not isinstance(value, dict):
            raise ValueError("reviewer row must be an object")
        required = {"reviewer_id", "paper_id", "label", "rationale", "evidence_locator", "judged_at"}
        if set(value) != required:
            raise ValueError(f"reviewer row fields must be exactly {sorted(required)}")
        current_reviewer = _nonempty(value["reviewer_id"], "reviewer_id")
        if reviewer_id is None:
            reviewer_id = current_reviewer
        elif current_reviewer != reviewer_id:
            raise ValueError("one reviewer file must contain exactly one reviewer_id")
        paper_id = _nonempty(value["paper_id"], "paper_id")
        if paper_id not in pool:
            raise ValueError(f"reviewer paper_id is outside the frozen review pool: {paper_id}")
        if paper_id in rows:
            raise ValueError(f"duplicate paper_id for reviewer: {paper_id}")
        label = value["label"]
        if label not in _LABELS:
            raise ValueError("review label must be relevant, irrelevant, pending, or uncertain")
        rows[paper_id] = {
            "reviewer_id": current_reviewer,
            "paper_id": paper_id,
            "label": label,
            "rationale": _safe_review_text(value["rationale"], "rationale"),
            "evidence_locator": _safe_review_text(value["evidence_locator"], "evidence_locator"),
            "judged_at": _iso_datetime(value["judged_at"], "judged_at"),
        }
    if reviewer_id is None:
        raise ValueError("reviewer file is empty")
    return reviewer_id, rows


def _review_pool(case: dict[str, Any]) -> list[str]:
    explicit = case.get("review_pool_ids")
    if explicit is not None:
        return _ids(explicit, "review_pool_ids")
    pool: dict[str, None] = {}
    for run in case.get("runs", []):
        if not isinstance(run, dict) or not isinstance(run.get("paper_ids"), list):
            raise ValueError("test case runs must contain paper_ids arrays")
        for paper_id in run["paper_ids"]:
            pool[_nonempty(paper_id, "paper_id")] = None
    if not pool:
        raise ValueError("test case has no review pool")
    return list(pool)


def _consensus(left: dict[str, Any] | None, right: dict[str, Any] | None) -> tuple[str, bool, str]:
    if left is None or right is None:
        return "pending", True, "missing_reviewer"
    left_label = "pending" if left["label"] == "uncertain" else left["label"]
    right_label = "pending" if right["label"] == "uncertain" else right["label"]
    if left_label in _DECISIVE and left_label == right_label:
        return left_label, False, "not_needed"
    if left_label == right_label == "pending":
        return "pending", True, "pending_review"
    return "pending", True, "pending_adjudication"


def _write_payloads(output: Path, payloads: dict[str, str]) -> None:
    output.mkdir(parents=True, exist_ok=False)
    for name, content in payloads.items():
        with (output / name).open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(content)


def prepare_p4_review(
    base_manifest: dict[str, Any],
    reference_ids: list[str],
    reference_set_source: str,
    reviewer_files: list[Path],
    output_dir: Path,
    *,
    test_case_id: str,
) -> dict[str, Any]:
    """Aggregate two independent reviewer files into a frozen P4 test manifest.

    This function does not invent papers, labels, adjudication, or metrics. It
    retains raw reviewer decisions and only writes decisive consensus labels to
    the benchmark manifest; pending/conflicts remain outside human_judgments.
    """
    if not isinstance(base_manifest, dict):
        raise ValueError("base_manifest must be an object")
    if not isinstance(test_case_id, str) or not test_case_id.strip():
        raise ValueError("test_case_id is required")
    reference = _ids(reference_ids, "reference_ids")
    source = _nonempty(reference_set_source, "reference_set_source")
    if "\n" in source or "\r" in source:
        raise ValueError("reference_set_source must be single-line")
    if type(reviewer_files) is not list or len(reviewer_files) != 2:
        raise ValueError("exactly two reviewer files are required")
    output = Path(output_dir)
    if output.exists():
        raise FileExistsError(f"output directory already exists: {output}")
    manifest = _clone(base_manifest)
    cases = manifest.get("cases")
    if type(cases) is not list:
        raise ValueError("base_manifest.cases must be an array")
    targets = [case for case in cases if isinstance(case, dict) and case.get("case_id") == test_case_id]
    if len(targets) != 1:
        raise ValueError("test_case_id must identify exactly one case")
    target = targets[0]
    if target.get("split") != "test":
        raise ValueError("P4 independent review target must use split=test")
    pool = _review_pool(target)
    reviewer_data = [_load_reviewer(Path(path), set(pool)) for path in reviewer_files]
    if reviewer_data[0][0] == reviewer_data[1][0]:
        raise ValueError("reviewer_id must be different for independent review")
    reviewer_ids = [item[0] for item in reviewer_data]
    reviewed_rows: list[dict[str, Any]] = []
    conflicts: list[dict[str, Any]] = []
    consensus_labels: dict[str, str] = {}
    coverage_count = 0
    actual_review_count = 0
    pending_count = 0
    for paper_id in pool:
        left = reviewer_data[0][1].get(paper_id)
        right = reviewer_data[1][1].get(paper_id)
        actual_review_count += int(left is not None) + int(right is not None)
        coverage_count += int(left is not None and right is not None)
        consensus, conflict, status = _consensus(left, right)
        if consensus == "pending":
            pending_count += 1
        elif consensus in _DECISIVE:
            consensus_labels[paper_id] = consensus
        if conflict:
            conflict_reason = "conflict" if status == "pending_adjudication" else status
            conflicts.append({"paper_id": paper_id, "reason": conflict_reason, "reviewer_ids": reviewer_ids})
        ordered_judgments = [left, right]
        if left is None and right is not None:
            ordered_judgments = [right, left]
        reviewed_rows.append({
            "paper_id": paper_id,
            "judgments": ordered_judgments,
            "consensus_label": consensus,
            "conflict": conflict,
            "adjudication_status": status,
        })
    target["reference_set"] = reference
    target["reference_set_independent"] = True
    target["reference_set_source"] = source
    target["human_judgments"] = consensus_labels
    reviewed_jsonl = "".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in reviewed_rows)
    conflicts_jsonl = "".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in conflicts)
    benchmark_json = json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    payloads = {
        "reviewed.jsonl": reviewed_jsonl,
        "conflicts.jsonl": conflicts_jsonl,
        "benchmark-manifest.json": benchmark_json,
    }
    hashes = {
        "schema_version": "0.1", "status": "completed", "algorithm": "sha256",
        "files": {name: hashlib.sha256(content.encode("utf-8")).hexdigest() for name, content in payloads.items()},
    }
    result = {
        "benchmark_manifest": manifest,
        "summary": {
            "test_case_id": test_case_id, "reference_set": reference,
            "reference_set_source": source, "reviewer_ids": reviewer_ids,
            "review_pool_count": len(pool), "actual_review_count": actual_review_count,
            "coverage_count": coverage_count, "pending_count": pending_count,
            "conflict_count": len(conflicts), "new_network_request_count": 0,
        },
    }
    _write_payloads(output, {**payloads, "manifest.sha256.json": json.dumps(hashes, ensure_ascii=False, indent=2, sort_keys=True) + "\n"})
    return result
