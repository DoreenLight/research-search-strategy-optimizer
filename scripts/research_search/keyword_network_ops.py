"""K2-K5 operations around the read-only keyword evidence network."""
from __future__ import annotations

from collections import defaultdict
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

from .validation import validate_case


def _json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    path.write_text("".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in records), encoding="utf-8")


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")


def _hash(value: Any, prefix: str = "") -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
    return prefix + hashlib.sha256(encoded).hexdigest()[:20]


def _safe_new_dir(output: Path) -> None:
    if output.exists():
        raise FileExistsError(f"output directory already exists: {output}")
    output.mkdir(parents=True, exist_ok=False)


def _load_network(network_dir: Path) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
    network_dir = Path(network_dir)
    if network_dir.is_symlink() or not network_dir.is_dir():
        raise ValueError("network directory must be a regular directory")
    manifest = _json(network_dir / "manifest.json")
    if manifest.get("status") != "completed":
        raise ValueError("network manifest is not completed")
    network = _json(network_dir / "network.json")
    nodes = _jsonl(network_dir / "nodes.jsonl")
    edges = _jsonl(network_dir / "edges.jsonl")
    return network, nodes, edges


def _paper_diversity(edge: dict[str, Any]) -> int:
    return len(set(edge.get("supporting_paper_ids", [])))


def _edge_priority(edge: dict[str, Any], node_by_id: dict[str, dict[str, Any]]) -> tuple[float, dict[str, Any]]:
    subject = node_by_id.get(edge.get("subject"), {})
    object_node = node_by_id.get(edge.get("object"), {})
    document_frequency = len(set(edge.get("supporting_paper_ids", [])))
    source_diversity = len(set(edge.get("source_levels", []))) or 1
    field_diversity = len(set(subject.get("source_fields", []) + object_node.get("source_fields", []))) or 1
    review_cost = max(1, len(edge.get("evidence_ids", [])))
    drift_risk = 1.0 if edge.get("predicate") in {"broader_than", "narrower_than", "related_task", "alternative_method", "application_of"} else 0.35
    score = (document_frequency * source_diversity * field_diversity) / (review_cost * (1 + drift_risk))
    return score, {
        "document_frequency": document_frequency, "source_diversity": source_diversity,
        "field_diversity": field_diversity, "review_cost": review_cost, "semantic_drift_risk": drift_risk,
    }


def score_keyword_frontier(network_dir: Path, output_dir: Path, *, limit: int = 30) -> dict[str, Any]:
    if type(limit) is not int or not 1 <= limit <= 500:
        raise ValueError("limit must be between 1 and 500")
    network, nodes, edges = _load_network(Path(network_dir))
    node_by_id = {node["node_id"]: node for node in nodes}
    candidates = []
    for edge in edges:
        if edge.get("status") != "candidate":
            continue
        score, components = _edge_priority(edge, node_by_id)
        candidates.append({**edge, "priority_score": score, "priority_components": components,
                          "review_status": "pending_review", "adopted": False})
    candidates.sort(key=lambda edge: (-edge["priority_score"], edge["edge_id"]))
    selected = candidates[:limit]
    payload = {
        "schema_version": "0.1", "network_schema_version": network.get("network_schema_version"),
        "scope_id": network["scope_id"], "selection_limit": limit,
        "selection_rule": "Rank candidate edges by paper/source/field diversity divided by review cost and semantic drift risk. Ranking never approves or adopts an edge.",
        "candidate_count": len(candidates), "selected_count": len(selected),
        "deferred_count": max(0, len(candidates) - len(selected)), "edges": selected,
    }
    _safe_new_dir(Path(output_dir))
    _write_json(Path(output_dir) / "candidate-frontier.json", payload)
    manifest = {"schema_version": "0.1", "status": "completed", "files": {
        "candidate-frontier.json": hashlib.sha256((Path(output_dir) / "candidate-frontier.json").read_bytes()).hexdigest()
    }}
    _write_json(Path(output_dir) / "manifest.json", manifest)
    return payload


def export_edge_review_workbench(network_dir: Path, frontier_path: Path, output_dir: Path) -> dict[str, Any]:
    network, nodes, edges = _load_network(Path(network_dir))
    frontier = _json(Path(frontier_path))
    selected_ids = {item["edge_id"] for item in frontier.get("edges", [])}
    edge_by_id = {edge["edge_id"]: edge for edge in edges}
    node_by_id = {node["node_id"]: node for node in nodes}
    queue = []
    for edge_id in sorted(selected_ids):
        edge = edge_by_id.get(edge_id)
        if not edge:
            raise ValueError(f"frontier edge not found in network: {edge_id}")
        queue.append({
            "edge_id": edge_id, "scope_id": network["scope_id"], "predicate": edge["predicate"],
            "status": "pending_review", "subject": node_by_id[edge["subject"]].get("label"),
            "object": node_by_id[edge["object"]].get("label"),
            "evidence_ids": edge.get("evidence_ids", []),
            "supporting_paper_ids": edge.get("supporting_paper_ids", []),
            "source_count": edge.get("source_count", 0),
        })
    _safe_new_dir(Path(output_dir))
    output = Path(output_dir)
    html = """<!doctype html><meta charset="utf-8"><title>Keyword edge review</title>
<style>body{font-family:system-ui,sans-serif;background:#f7f5f0;color:#26352d;max-width:1100px;margin:32px auto;padding:0 20px}article{background:white;border:1px solid #dfe7df;border-radius:12px;padding:16px;margin:12px 0}button{padding:8px 12px;margin-right:8px}code{overflow-wrap:anywhere}</style>
<h1>Keyword edge review</h1><p>Offline candidate-edge review. Ranking, expected gain, provider identity, and query text are not shown.</p><p>Allowed review states: approved / rejected / pending_review.</p>
<div id="queue"></div><script>const data=__DATA__;const root=document.getElementById('queue');for(const e of data.edges){const a=document.createElement('article');a.innerHTML='<h2></h2><p></p><p>Evidence count: '+e.evidence_ids.length+'; supporting papers: '+e.supporting_paper_ids.length+'</p><button>approved</button><button>rejected</button><button>pending_review</button>';a.querySelector('h2').textContent=e.subject+' ↔ '+e.object;a.querySelector('p').textContent=e.predicate;root.appendChild(a)}</script>""".replace("__DATA__", json.dumps({"edges": queue}, ensure_ascii=False).replace("<", "\\u003c"))
    (output / "index.html").write_text(html, encoding="utf-8")
    (output / "edge-review-queue.jsonl").write_text("".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in queue), encoding="utf-8")
    (output / "review-events.jsonl").write_text("", encoding="utf-8")
    (output / "README.md").write_text("# Keyword edge review\n\nOffline candidate-edge review; no edge is automatically approved or adopted.\n", encoding="utf-8")
    files = {str(path.name): hashlib.sha256(path.read_bytes()).hexdigest() for path in output.iterdir() if path.name != "manifest.json"}
    _write_json(output / "manifest.json", {"schema_version": "0.1", "status": "completed", "edge_count": len(queue), "files": files})
    return {"status": "completed", "edge_count": len(queue), "output": str(output)}


def adopt_edge(case_path: Path, network_dir: Path, review_events_path: Path, edge_id: str, output_path: Path) -> dict[str, Any]:
    if Path(output_path).exists():
        raise FileExistsError(f"output exists: {output_path}")
    case = json.loads(Path(case_path).read_text(encoding="utf-8"))
    validate_case(case)
    _network, nodes, edges = _load_network(Path(network_dir))
    edge = next((item for item in edges if item.get("edge_id") == edge_id), None)
    if not edge:
        raise ValueError("edge_id not found")
    events = _jsonl(Path(review_events_path))
    approved = [event for event in events if event.get("edge_id") == edge_id and event.get("label") == "approved" and event.get("review_status") == "approved"]
    reviewer_ids = {event.get("reviewer_id") for event in approved if event.get("reviewer_id")}
    if len(reviewer_ids) < 2:
        raise ValueError("edge requires two independent approved reviewer events")
    if any(event.get("synthetic_review") is not True for event in approved):
        raise ValueError("edge review provenance must be explicit")
    group_ids = {group["group_id"] for group in case["concept_groups"]}
    review = approved[-1]
    group_id = review.get("group_id")
    term = review.get("adopted_term")
    if group_id not in group_ids or not isinstance(term, str) or not term.strip():
        raise ValueError("approved edge must identify one concept group and adopted_term")
    group = next(group for group in case["concept_groups"] if group["group_id"] == group_id)
    if term.casefold() not in {item.casefold() for item in group["terms"]}:
        group["terms"].append(term)
    validate_case(case)
    metadata_path = Path(str(output_path) + ".adoption.json")
    adoption = {
        "edge_id": edge_id, "review_event_ids": [event.get("review_event_id") for event in approved],
        "group_id": group_id, "adopted_term": term, "synthetic_review": True,
        "rollback_target": case.get("case_id"), "status": "candidate",
    }
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(json.dumps(case, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    metadata_path.write_text(json.dumps(adoption, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"status": "written", "output": str(output_path), "adoption_metadata": str(metadata_path), "edge_id": edge_id, "group_id": group_id, "adopted_term": term}


def aggregate_edge_reviews(frontier_path: Path, reviewer_files: list[Path], output_dir: Path, *, adjudication_path: Path | None = None) -> dict[str, Any]:
    if type(reviewer_files) is not list or len(reviewer_files) != 2:
        raise ValueError("exactly two reviewer files are required")
    frontier = _json(Path(frontier_path))
    edge_ids = {item["edge_id"] for item in frontier.get("edges", [])}
    if not edge_ids:
        raise ValueError("frontier contains no edges")
    reviewers = []
    reviewer_ids = set()
    for file in reviewer_files:
        rows = _jsonl(Path(file))
        if not rows:
            raise ValueError("reviewer file is empty")
        current = {row.get("reviewer_id") for row in rows}
        if len(current) != 1 or None in current:
            raise ValueError("one reviewer file must contain one reviewer_id")
        reviewer_id = next(iter(current))
        if reviewer_id in reviewer_ids:
            raise ValueError("two distinct reviewer ids are required")
        reviewer_ids.add(reviewer_id)
        by_edge = {}
        for row in rows:
            if row.get("edge_id") not in edge_ids:
                raise ValueError("review row references an unknown edge")
            if row["edge_id"] in by_edge:
                raise ValueError("duplicate edge review")
            if row.get("label") not in {"approved", "rejected", "pending_review"}:
                raise ValueError("invalid edge review label")
            by_edge[row["edge_id"]] = row
        reviewers.append(by_edge)
    adjudications = {}
    if adjudication_path is not None:
        for row in _jsonl(Path(adjudication_path)):
            if row.get("edge_id") not in edge_ids or row.get("label") not in {"approved", "rejected", "pending_review"}:
                raise ValueError("invalid adjudication edge/label")
            adjudications[row["edge_id"]] = row
    records, conflicts = [], []
    approved_count = conflict_count = missing_count = adjudicated_count = 0
    for edge in frontier["edges"]:
        edge_id = edge["edge_id"]
        judgments = [reviewers[0].get(edge_id), reviewers[1].get(edge_id)]
        labels = [item["label"] for item in judgments if item is not None]
        if len(labels) == 2 and labels[0] == labels[1] and labels[0] == "approved":
            consensus, status, conflict = "approved", "not_needed", False
            approved_count += 1
        elif edge_id in adjudications:
            consensus, status, conflict = adjudications[edge_id]["label"], "adjudicated", True
            adjudicated_count += 1
        elif len(labels) < 2:
            consensus, status, conflict = "pending_review", "missing_reviewer", True
            missing_count += 1
        elif labels[0] != labels[1]:
            consensus, status, conflict = "pending_review", "pending_adjudication", True
            conflict_count += 1
        else:
            consensus, status, conflict = "pending_review", "pending_review", True
        if conflict and status != "adjudicated" and status != "missing_reviewer":
            conflict_count += 0
        if conflict:
            conflicts.append({"edge_id": edge_id, "reason": status, "synthetic_review": True})
        records.append({"edge_id": edge_id, "judgments": judgments, "consensus_label": consensus,
                        "conflict": conflict, "adjudication_status": status, "synthetic_review": True})
    _safe_new_dir(Path(output_dir))
    output = Path(output_dir)
    _write_jsonl(output / "edge-consensus.jsonl", records)
    _write_jsonl(output / "edge-conflicts.jsonl", conflicts)
    summary = {"edge_count": len(records), "approved_count": approved_count, "conflict_count": conflict_count,
               "missing_count": missing_count, "adjudicated_count": adjudicated_count, "synthetic_review": True}
    _write_json(output / "summary.json", summary)
    files = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in output.iterdir()}
    _write_json(output / "manifest.json", {"schema_version": "0.1", "status": "completed", "synthetic_review": True, "summary": summary, "files": files})
    return {"status": "completed", "summary": summary, "output": str(output)}


def build_network_experiment_config(base_config: dict[str, Any], candidate_case: dict[str, Any], *, edge_id: str,
                                    review_event_ids: list[str], output_path: Path) -> dict[str, Any]:
    if Path(output_path).exists():
        raise FileExistsError(f"output exists: {output_path}")
    if not isinstance(base_config, dict) or not isinstance(candidate_case, dict):
        raise ValueError("base_config and candidate_case must be objects")
    validate_case(base_config["rounds"][0]["case"])
    validate_case(candidate_case)
    parent = base_config["rounds"][0]["case"]
    before_groups = {item["group_id"]: item for item in parent["concept_groups"]}
    after_groups = {item["group_id"]: item for item in candidate_case["concept_groups"]}
    changed = [group_id for group_id in sorted(set(before_groups) | set(after_groups))
               if before_groups.get(group_id, {}).get("terms") != after_groups.get(group_id, {}).get("terms")]
    if len(changed) != 1 or set(before_groups) != set(after_groups):
        raise ValueError("network experiment must change exactly one existing concept group")
    config = copy.deepcopy(base_config)
    config["rounds"] = list(config["rounds"]) + [{
        "case": candidate_case, "rationale": f"Keyword network edge {edge_id} explicit adoption; synthetic review input.",
        "tested_in": {"edge_id": edge_id, "review_event_ids": list(review_event_ids), "synthetic_review": True,
                      "query_version": "candidate", "request_count": None, "paper_ids": None,
                      "confirmed_new_relevant_ids": None, "cost_usd": None, "screening_minutes": None},
        "reviewed_by": "keyword-network-review", "change_relationship": "unclassified",
        "keyword_network_edge_ids": [edge_id], "review_event_ids": list(review_event_ids),
        "new_terms": sorted(set(candidate_case["concept_groups"][0]["terms"]) - set(parent["concept_groups"][0]["terms"])),
        "separate_branch": False, "judgments": [],
    }]
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(json.dumps(config, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"status": "written", "output": str(output_path), "edge_id": edge_id, "changed_group": changed[0]}
