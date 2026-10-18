"""Re-evaluate an existing P1 session with explicit, auditable human judgments."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .optimization_session import run_optimization
from .validation import validate_package, validate_record


def _json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _verify_session(source: Path) -> dict[str, Any]:
    manifest_path = source / "manifest.json"
    manifest = _json(manifest_path)
    if not isinstance(manifest, dict) or not isinstance(manifest.get("files"), dict):
        raise ValueError("session manifest files are missing")
    actual = {
        str(path.relative_to(source))
        for path in source.rglob("*")
        if path.is_file() and path != source / "manifest.json"
    }
    listed = set(manifest["files"])
    required = {"history.json", "summary.json", "active-case.json"}
    if listed != actual or not required.issubset(listed):
        raise ValueError("session manifest inventory is incomplete")
    for name, digest in manifest["files"].items():
        path = source / name
        if path.is_symlink() or not path.resolve().is_relative_to(source.resolve()) or not path.is_file():
            raise ValueError("unsafe or missing session file")
        if not isinstance(digest, str) or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError(f"session hash mismatch: {name}")
    return manifest


def review_optimization_session(source: Path, judgment_files: list[Path], output_dir: Path) -> dict[str, Any]:
    """Write a new offline session; never mutate the source or invent labels."""
    source, output_dir = Path(source), Path(output_dir)
    if output_dir.exists():
        raise FileExistsError("output directory already exists")
    if source.is_symlink() or output_dir.resolve().is_relative_to(source.resolve()):
        raise ValueError("review output must be outside the immutable source session")
    _verify_session(source)
    history = _json(source / "history.json")
    if not isinstance(history, list) or not history:
        raise ValueError("source session has no rounds")
    config_path = source / "session-config.json"
    config = _json(config_path) if config_path.exists() else {"session_id": _json(source / "summary.json")["session_id"], "max_requests": 0}
    rounds = []
    scopes = set()
    all_ids = set()
    for entry in history:
        package = source / f"round-{entry['round_index']:02d}"
        validate_package(package)
        case = _json(package / "input-case.json")
        scopes.add(case["research_scope"]["scope_id"])
        all_ids.update(json.loads(line)["paper_id"] for line in (package / "04-papers.jsonl").read_text(encoding="utf-8").splitlines() if line.strip())
        bundle_path = package / "replay-bundle.json"
        if not bundle_path.is_file():
            raise ValueError("every reviewed round needs an existing replay bundle")
        rounds.append({"case": case, "snapshots": _json(bundle_path), "rationale": entry.get("rationale", ""),
                       "reviewed_by": entry.get("reviewed_by"), "change_relationship": entry.get("relationship", "baseline"),
                       "evidence_paper_ids": entry.get("evidence_paper_ids", entry.get("evidence_ids", [])),
                       "new_terms": entry.get("new_terms", []), "drift_rate": entry.get("drift_rate"),
                       "separate_branch": entry.get("decision") == "branch_only", "judgments": []})
    judgments = []
    seen_ids = set()
    for filename in judgment_files:
        for line in Path(filename).read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            item = json.loads(line)
            validate_record("judgment", item)
            if item["judge_type"] != "human" or not item.get("reviewer_id", "").strip() or not item.get("evidence_locator", "").strip():
                raise ValueError("review import needs human reviewer_id and evidence_locator")
            if item["scope_id"] not in scopes or item["paper_id"] not in all_ids:
                raise ValueError("judgment is outside the session paper/scope pool")
            if item["judgment_id"] in seen_ids:
                raise ValueError("duplicate judgment_id; supply each original record once")
            seen_ids.add(item["judgment_id"])
            judgments.append(item)
    if not judgments:
        raise ValueError("no human judgments supplied")
    # Keep every original reviewer record. A disagreement remains uncertain in
    # run_optimization; importing another reviewer never silently overwrites it.
    for round_config in rounds:
        round_config["judgments"] = list(judgments)
        round_config["case"]["judgments"] = list(judgments)
    config.update(session_id=f"{config['session_id']}-reviewed", rounds=rounds, max_requests=0, max_rounds=len(rounds))
    result = run_optimization(config, output_dir)
    (output_dir / "review-import.json").write_text(json.dumps({
        "schema_version": "0.1", "human_judgments": judgments,
        "source_session_manifest_sha256": hashlib.sha256((source / "manifest.json").read_bytes()).hexdigest(),
        "new_network_requests": 0,
    }, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    # The session manifest also inventories the provenance artifact.
    manifest_path = output_dir / "manifest.json"
    manifest = _json(manifest_path)
    manifest["files"]["review-import.json"] = hashlib.sha256((output_dir / "review-import.json").read_bytes()).hexdigest()
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result
