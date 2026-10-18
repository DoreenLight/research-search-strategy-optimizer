"""Local-only JSON Schema and cross-file integrity validation."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

from .models import ConceptGroup
from .query_builder import build_strategy_plans


def schema_root() -> Path:
    root = Path(__file__).resolve().parents[2] / "schemas"
    if not root.is_dir():
        raise ValueError("schemas directory missing; use the full project or standalone release package")
    return root


def validate_record(kind: str, record: Any) -> None:
    root = schema_root()
    schemas = {path.name: json.loads(path.read_text(encoding="utf-8")) for path in root.glob("*.schema.json")}
    name = f"{kind}.schema.json"
    if name not in schemas:
        raise ValueError(f"unknown schema {kind}")
    registry = Registry().with_resources((name, Resource.from_contents(content)) for name, content in schemas.items())
    validator = Draft202012Validator(schemas[name], registry=registry, format_checker=FormatChecker())
    errors = list(validator.iter_errors(record))
    if errors:
        first = errors[0]
        pointer = "/".join(map(str, first.absolute_path)) or "<root>"
        raise ValueError(f"{kind} {pointer}: {first.message}")


def validate_case(case: Any) -> None:
    validate_record("research-case", case)
    constraints = case["research_scope"]["constraints"]
    if "date_from" in constraints and "date_to" in constraints and constraints["date_from"] > constraints["date_to"]:
        raise ValueError("date_from is after date_to")
    groups = [ConceptGroup(item["group_id"], item["label"], item["terms"], item.get("role")) for item in case["concept_groups"]]
    build_strategy_plans(groups)
    scope_id = case["research_scope"]["scope_id"]
    if any(j["scope_id"] != scope_id for j in case.get("judgments", [])):
        raise ValueError("judgment scope_id mismatch")


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def validate_package(output: Path, *, check_hashes: bool = True) -> dict[str, int]:
    """Raise ValueError for malformed records, dangling IDs or edited content."""
    output = Path(output)
    scope = json.loads((output / "01-research-scope.json").read_text(encoding="utf-8"))
    keywords = json.loads((output / "02-keywords.json").read_text(encoding="utf-8"))
    plans = json.loads((output / "03-search-strategies.json").read_text(encoding="utf-8"))
    papers = _read_jsonl(output / "04-papers.jsonl")
    runs = _read_jsonl(output / "05-search-runs.jsonl")
    evidence = _read_jsonl(output / "07-evidence.jsonl")
    judgments = _read_jsonl(output / "10-judgments.jsonl")
    validate_record("research-scope", scope)
    for kind, items in [("keyword", keywords), ("search-plan", plans), ("paper", papers),
                        ("search-run", runs), ("evidence", evidence), ("judgment", judgments)]:
        for item in items:
            validate_record(kind, item)
    def index(items: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
        result = {item[key]: item for item in items}
        if len(result) != len(items):
            raise ValueError(f"duplicate {key}")
        return result
    plan_ids = index(plans, "plan_id")
    paper_ids = index(papers, "paper_id")
    run_ids = index(runs, "run_id")
    evidence_ids = index(evidence, "evidence_id")
    index(keywords, "term_id")
    index(judgments, "judgment_id")
    for plan in plans:
        if plan["group_ids"] != plan["logic"]["groups"] or plan["group_ids"] != [g["group_id"] for g in plan["groups"]]:
            raise ValueError("plan group logic mismatch")
    for run in runs:
        if run["plan_id"] not in plan_ids or not set(run["paper_ids"]).issubset(paper_ids):
            raise ValueError("run has dangling plan/paper ID")
        if run["deduplicated_count"] != len(set(run["paper_ids"])) or run["deduplicated_count"] > run["fetched_count"]:
            raise ValueError("run count mismatch")
        if run["mode"] != "live" and run["request_count"] != 0:
            raise ValueError("offline record claims network requests")
        if run.get("raw_path"):
            raw = output / run["raw_path"]
            if not raw.resolve().is_relative_to(output.resolve()) or not raw.is_file():
                raise ValueError("raw response path invalid")
    for paper in papers:
        if not set(paper["source_run_ids"]).issubset(run_ids):
            raise ValueError("paper has dangling run ID")
    for ev in evidence:
        if ev["paper_id"] not in paper_ids or not set(ev["run_ids"]).issubset(run_ids):
            raise ValueError("evidence has dangling paper/run ID")
        if ev["excerpt"]:
            value = paper_ids[ev["paper_id"]].get(ev["locator"])
            if isinstance(value, list):
                found = ev["excerpt"] in value
            else:
                found = isinstance(value, str) and ev["excerpt"] in value
            if not found:
                raise ValueError("evidence excerpt not found in source field")
    for keyword in keywords:
        if not set(keyword["evidence_ids"]).issubset(evidence_ids) or not set(keyword["paper_ids"]).issubset(paper_ids):
            raise ValueError("keyword has dangling evidence/paper ID")
        if keyword["evidence_status"] not in {"unverified_candidate"} and not keyword["evidence_ids"]:
            raise ValueError("observed keyword missing evidence")
    if check_hashes:
        manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
        files = manifest["files"]
        actual = {str(path.relative_to(output)) for path in output.rglob("*") if path.is_file() and path.name != "manifest.json"}
        if set(files) != actual:
            raise ValueError("manifest inventory mismatch")
        for name, digest in files.items():
            path = output / name
            if not path.resolve().is_relative_to(output.resolve()):
                raise ValueError("unsafe manifest path")
            if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                raise ValueError(f"manifest hash mismatch: {name}")
    return {"papers": len(papers), "keywords": len(keywords), "runs": len(runs), "evidence": len(evidence)}
