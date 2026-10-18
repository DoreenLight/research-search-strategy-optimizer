"""Explicitly apply approved keyword reviews to a new research case."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .validation import validate_case, validate_record


def _load(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def adopt_reviewed_keywords(
    case_path: Path,
    reviewed_keywords_path: Path,
    output_path: Path,
    *,
    group_id: str,
) -> dict[str, Any]:
    """Write a new case with explicitly approved terms appended to one group.

    This is intentionally separate from package generation: ranking or approval
    never mutates a case implicitly, and the source case is never overwritten.
    """
    case_path, reviewed_keywords_path, output_path = map(Path, (case_path, reviewed_keywords_path, output_path))
    if output_path.exists():
        raise FileExistsError(f"output exists; choose a new filename: {output_path}")
    case = _load(case_path)
    validate_case(case)
    reviewed = _load(reviewed_keywords_path)
    if not isinstance(reviewed, dict) or not isinstance(reviewed.get("terms"), list):
        raise ValueError("reviewed-keywords must contain terms[]")
    group = next((item for item in case["concept_groups"] if item["group_id"] == group_id), None)
    if group is None:
        raise ValueError(f"unknown concept group: {group_id}")
    adopted: list[str] = []
    existing = {term.casefold() for term in group["terms"]}
    for item in reviewed["terms"]:
        validate_record("keyword", item)
        if item.get("adopted") is not True or item.get("evidence_status") != "reviewed":
            continue
        if item.get("relationship") == "unclassified":
            raise ValueError("adopted term must be classified")
        term = item["term"]
        if term.casefold() not in existing:
            group["terms"].append(term)
            existing.add(term.casefold())
            adopted.append(term)
    if not adopted:
        raise ValueError("no explicitly approved reviewed keywords to adopt")
    validate_case(case)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(case, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"status": "written", "output": str(output_path), "group_id": group_id, "adopted_terms": adopted}
