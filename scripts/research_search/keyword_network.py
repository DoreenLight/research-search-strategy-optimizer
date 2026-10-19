"""Deterministic, read-only keyword evidence network construction."""
from __future__ import annotations

from collections import defaultdict
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

from .validation import validate_package


SCHEMA_VERSION = "0.1"
_DEFAULT_MAX_COOCCURRENCE_EDGES = 50_000
_DEFAULT_MAX_COOCCURRENCE_DEGREE = 25
_DEFAULT_MIN_COOCCURRENCE_DOCUMENT_FREQUENCY = 2
_OUTPUT_FILES = (
    "network.json", "nodes.jsonl", "edges.jsonl", "observations.jsonl",
    "candidate-frontier.json", "review-events.jsonl", "adoption-events.jsonl",
    "network-experiments.jsonl", "source-index.jsonl", "README.md",
)


def _canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _hash(prefix: str, value: Any) -> str:
    return prefix + hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()[:20]


def _jsonl(path: Path, records: Iterable[dict[str, Any]]) -> None:
    path.write_text("".join(json.dumps(item, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n" for item in records), encoding="utf-8")


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot read package JSON: {path.name}") from error


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as error:
        raise ValueError(f"cannot read package JSONL: {path.name}") from error
    records = []
    for line in lines:
        if line.strip():
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"package JSONL record must be object: {path.name}")
            records.append(value)
    return records


def _package_snapshot(package: Path) -> dict[str, Any]:
    package = Path(package)
    if package.is_symlink() or not package.is_dir():
        raise ValueError("keyword network input must be a package directory")
    if any(path.is_symlink() for path in package.rglob("*")):
        raise ValueError("keyword network package must not contain symlinks")
    try:
        validate_package(package)
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        raise ValueError(f"invalid research search package: {package}") from error
    manifest = _read_json(package / "manifest.json")
    scope = _read_json(package / "01-research-scope.json")
    papers = _read_jsonl(package / "04-papers.jsonl")
    runs = _read_jsonl(package / "05-search-runs.jsonl")
    evidence = _read_jsonl(package / "07-evidence.jsonl")
    keywords = _read_json(package / "02-keywords.json")
    observations_path = package / "raw-observations.jsonl"
    observations = _read_jsonl(observations_path) if observations_path.is_file() else []
    if not isinstance(keywords, list) or not isinstance(scope, dict):
        raise ValueError("package keyword/scope files have invalid shape")
    if not observations:
        evidence_by_id = {item["evidence_id"]: item for item in evidence}
        for keyword in keywords:
            for evidence_id in keyword.get("evidence_ids", []):
                item = evidence_by_id.get(evidence_id)
                if item is None:
                    continue
                observations.append({
                    "term": keyword.get("term", ""),
                    "source_field": item.get("locator"),
                    "paper_id": item.get("paper_id"),
                    "excerpt": item.get("excerpt"),
                    "evidence_id": evidence_id,
                    "evidence_status": keyword.get("evidence_status", "observed_in_paper"),
                })
    provider_results_path = package / "11-provider-results.jsonl"
    provider_fusion_path = package / "12-provider-fusion.json"
    provider_results = _read_jsonl(provider_results_path) if provider_results_path.is_file() else []
    provider_fusion = _read_json(provider_fusion_path) if provider_fusion_path.is_file() else None
    return {"path": package.resolve(), "manifest": manifest, "scope": scope, "papers": papers,
            "runs": runs, "evidence": evidence, "keywords": keywords, "observations": observations,
            "provider_results": provider_results, "provider_fusion": provider_fusion}


def _source_record_id(paper_id: str, provider: str | None) -> str:
    return f"{provider or 'unknown'}:{paper_id}"


def _build_observations(snapshot: dict[str, Any], scope_id: str) -> list[dict[str, Any]]:
    evidence_by_id = {item["evidence_id"]: item for item in snapshot["evidence"]}
    keyword_by_term = {item.get("term"): item for item in snapshot["keywords"] if isinstance(item, dict)}
    observations: list[dict[str, Any]] = []
    for item in snapshot["observations"]:
        evidence_ids = [item.get("evidence_id")] if item.get("evidence_id") else []
        if not evidence_ids:
            keyword = keyword_by_term.get(item.get("term"))
            evidence_ids = list(keyword.get("evidence_ids", [])) if keyword else []
        for evidence_id in evidence_ids:
            evidence = evidence_by_id.get(evidence_id)
            if not evidence:
                continue
            payload = {
                "scope_id": scope_id, "term": item.get("term", ""),
                "normalized_term": item.get("term", "").casefold().strip(),
                "source_field": item.get("source_field") or evidence.get("locator"),
                "paper_id": item.get("paper_id") or evidence.get("paper_id"),
                "source_record_id": _source_record_id(item.get("paper_id") or evidence.get("paper_id"), evidence.get("source_type", "openalex")),
                "excerpt": item.get("excerpt") or evidence.get("excerpt"),
                "evidence_id": evidence_id,
                "evidence_ids": [evidence_id],
                "evidence_level": evidence.get("evidence_level", "U"),
                "source_level": evidence.get("evidence_level", "U"),
                "evidence_status": item.get("evidence_status") or evidence.get("supports", "observed_in_paper"),
                "run_ids": list(evidence.get("run_ids", [])),
                "source_url": evidence.get("source_url"),
                "retrieved_at": evidence.get("retrieved_at"),
                "status": "observed",
            }
            stable_identity = {
                "scope_id": scope_id, "term": payload["normalized_term"],
                "source_field": payload["source_field"], "paper_id": payload["paper_id"],
                "excerpt": payload["excerpt"],
            }
            payload["observation_id"] = _hash("obs-", stable_identity)
            observations.append(payload)
    for provider_result in snapshot.get("provider_results", []):
        provider = provider_result.get("provider", "unknown")
        query_type = provider_result.get("query_type", "unknown")
        channel = provider_result.get("channel", query_type)
        for paper in provider_result.get("papers", []):
            paper_id = paper.get("paper_id")
            if not paper_id:
                continue
            for field, values in (("author_keywords", paper.get("author_keywords", [])),
                                  ("mesh_terms", paper.get("mesh_terms", [])),
                                  ("database_keywords", paper.get("database_keywords", []))):
                for term in values or []:
                    if not isinstance(term, str) or not term.strip():
                        continue
                    normalized = term.casefold().strip()
                    provider_observation = {
                        "scope_id": scope_id, "term": term, "normalized_term": normalized,
                        "source_field": f"{provider}:{field}", "paper_id": paper_id,
                        "source_record_id": _source_record_id(paper_id, provider),
                        "excerpt": term, "evidence_id": f"provider:{provider}:{paper_id}:{field}:{normalized}",
                        "evidence_ids": [f"provider:{provider}:{paper_id}:{field}:{normalized}"],
                        "evidence_level": "A" if provider in {"pubmed", "semantic_scholar"} else "U",
                        "source_level": "A" if provider in {"pubmed", "semantic_scholar"} else "U",
                        "evidence_status": "database_assigned" if field in {"mesh_terms", "database_keywords"} else "observed_in_paper",
                        "run_ids": [], "source_url": paper.get("source_url"),
                        "retrieved_at": provider_result.get("executed_at"), "provider": provider,
                        "query_type": query_type, "channel": channel, "status": "observed",
                    }
                    provider_observation["observation_id"] = _hash("obs-", {
                        "scope_id": scope_id, "provider": provider, "query_type": query_type,
                        "paper_id": paper_id, "source_field": field, "normalized_term": normalized,
                    })
                    observations.append(provider_observation)
    unique = {item["observation_id"]: item for item in observations}
    return [unique[key] for key in sorted(unique)]


def _build_nodes(observations: list[dict[str, Any]], keywords: list[dict[str, Any]], scope_id: str) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for observation in observations:
        grouped[observation["normalized_term"]].append(observation)
    keyword_map = {item.get("term", "").casefold().strip(): item for item in keywords if isinstance(item, dict)}
    nodes = []
    for normalized, items in sorted(grouped.items()):
        papers = sorted({item["paper_id"] for item in items if item.get("paper_id")})
        fields = sorted({item["source_field"] for item in items if item.get("source_field")})
        evidence_statuses = {keyword_map.get(normalized, {}).get("evidence_status", "observed_in_paper")}
        node = {
            "node_id": _hash("lex-", {"scope_id": scope_id, "label": normalized, "node_type": "lexical_form"}),
            "node_type": "lexical_form", "label": items[0]["term"], "normalized_label": normalized,
            "scope_ids": [scope_id], "observation_ids": sorted({item["observation_id"] for item in items}),
            "paper_ids": papers, "document_frequency": len(papers), "source_field_count": len(fields),
            "provider_count": len({item.get("source_url") for item in items if item.get("source_url")}),
            "evidence_status": "database_assigned" if "database_assigned" in evidence_statuses else "observed",
            "review_status": "pending", "adopted_cases": [], "created_from": "package-artifact",
            "schema_version": SCHEMA_VERSION,
        }
        nodes.append(node)
    return nodes


def _build_edges(observations: list[dict[str, Any]], nodes: list[dict[str, Any]], scope_id: str, *,
                 max_cooccurrence_edges: int = _DEFAULT_MAX_COOCCURRENCE_EDGES,
                 max_cooccurrence_degree: int = _DEFAULT_MAX_COOCCURRENCE_DEGREE,
                 min_cooccurrence_document_frequency: int = _DEFAULT_MIN_COOCCURRENCE_DOCUMENT_FREQUENCY) -> list[dict[str, Any]]:
    edges = []
    node_by_term = {node["normalized_label"]: node for node in nodes}
    for item in observations:
        node = node_by_term.get(item["normalized_term"])
        if not node or not item.get("paper_id"):
            continue
        predicate = "database_assigned" if item.get("source_field") == "database_keywords" else "observed_in"
        object_id = _source_record_id(item["paper_id"], "openalex") if predicate == "database_assigned" else item["paper_id"]
        evidence = {
            "scope_id": scope_id, "subject": node["node_id"], "predicate": predicate,
            "object": object_id, "evidence_ids": [item["evidence_id"]],
            "supporting_paper_ids": [item["paper_id"]], "run_ids": item["run_ids"],
            "status": "observed", "source_count": 1,
        }
        evidence["edge_id"] = _hash("edge-", {"scope_id": scope_id, "subject": evidence["subject"], "predicate": predicate, "object": object_id})
        edges.append(evidence)
    # Cooccurrence is a candidate relation only, generated inside a paper.
    paper_terms: dict[str, set[str]] = defaultdict(set)
    for item in observations:
        if item.get("paper_id") and item["normalized_term"] in node_by_term:
            paper_terms[item["paper_id"]].add(item["normalized_term"])
    pairs: dict[tuple[str, str], set[str]] = defaultdict(set)
    for paper_id, terms in paper_terms.items():
        ordered = sorted(terms)
        for index, left in enumerate(ordered):
            for right in ordered[index + 1:]:
                pairs[(left, right)].add(paper_id)
    ranked_pairs = sorted(
        ((left, right, papers) for (left, right), papers in pairs.items()
         if len(papers) >= min_cooccurrence_document_frequency),
        key=lambda item: (-len(item[2]), item[0], item[1]),
    )
    degree: dict[str, int] = defaultdict(int)
    selected_pairs = []
    for left, right, papers in ranked_pairs:
        if len(selected_pairs) >= max_cooccurrence_edges:
            break
        if degree[left] >= max_cooccurrence_degree or degree[right] >= max_cooccurrence_degree:
            continue
        selected_pairs.append((left, right, papers))
        degree[left] += 1
        degree[right] += 1
    observations_by_paper_term: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for item in observations:
        if item.get("paper_id") and item.get("normalized_term"):
            observations_by_paper_term[(item["paper_id"], item["normalized_term"])].append(item)
    for left, right, papers in selected_pairs:
        endpoint_observations = [
            item for paper_id in papers
            for term in (left, right)
            for item in observations_by_paper_term[(paper_id, term)]
        ]
        payload = {
            "scope_id": scope_id, "subject": node_by_term[left]["node_id"],
            "predicate": "cooccurs_with", "object": node_by_term[right]["node_id"],
            "status": "candidate", "confidence": None,
            "evidence_ids": sorted({item["evidence_id"] for item in endpoint_observations}),
            "observation_ids": sorted({item["observation_id"] for item in endpoint_observations}),
            "supporting_paper_ids": sorted(papers), "source_count": len(papers),
        }
        payload["edge_id"] = _hash("edge-", {"scope_id": scope_id, "subject": payload["subject"], "predicate": payload["predicate"], "object": payload["object"]})
        edges.append(payload)
    unique = {item["edge_id"]: item for item in edges}
    return [unique[key] for key in sorted(unique)]


def build_keyword_network(packages: list[Path], output_dir: Path, *,
                          max_cooccurrence_edges: int = _DEFAULT_MAX_COOCCURRENCE_EDGES,
                          max_cooccurrence_degree: int = _DEFAULT_MAX_COOCCURRENCE_DEGREE,
                          min_cooccurrence_document_frequency: int = _DEFAULT_MIN_COOCCURRENCE_DOCUMENT_FREQUENCY) -> dict[str, Any]:
    """Build a deterministic read-only network from validated packages."""
    if not isinstance(packages, list) or not packages:
        raise ValueError("packages must be a non-empty list")
    output = Path(output_dir)
    if output.exists():
        raise FileExistsError(f"output directory already exists: {output}")
    snapshots = []
    seen_manifests: set[str] = set()
    for package in packages:
        snapshot = _package_snapshot(Path(package))
        manifest_hash = hashlib.sha256((snapshot["path"] / "manifest.json").read_bytes()).hexdigest()
        if manifest_hash not in seen_manifests:
            seen_manifests.add(manifest_hash)
            snapshot["manifest_hash"] = manifest_hash
            snapshots.append(snapshot)
    scope_ids = {snapshot["scope"]["scope_id"] for snapshot in snapshots}
    if len(scope_ids) != 1:
        raise ValueError("all packages must use one research scope")
    scope_id = next(iter(scope_ids))
    observations: list[dict[str, Any]] = []
    source_index: list[dict[str, Any]] = []
    for snapshot in snapshots:
        observations.extend(_build_observations(snapshot, scope_id))
        source_index.append({
            "package_manifest_sha256": snapshot["manifest_hash"],
            "scope_id": scope_id, "paper_count": len(snapshot["papers"]),
            "run_count": len(snapshot["runs"]), "evidence_count": len(snapshot["evidence"]),
        })
    unique_observations = {item["observation_id"]: item for item in observations}
    observations = [unique_observations[key] for key in sorted(unique_observations)]
    all_keywords = [item for snapshot in snapshots for item in snapshot["keywords"]]
    nodes = _build_nodes(observations, all_keywords, scope_id)
    for name, value in (("max_cooccurrence_edges", max_cooccurrence_edges), ("max_cooccurrence_degree", max_cooccurrence_degree), ("min_cooccurrence_document_frequency", min_cooccurrence_document_frequency)):
        if type(value) is not int or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
    edges = _build_edges(
        observations, nodes, scope_id,
        max_cooccurrence_edges=max_cooccurrence_edges,
        max_cooccurrence_degree=max_cooccurrence_degree,
        min_cooccurrence_document_frequency=min_cooccurrence_document_frequency,
    )
    frontier = {
        "schema_version": SCHEMA_VERSION, "scope_id": scope_id,
        "selection_limit": 30, "selection_rule": "Candidate cooccurrence edges and observed nodes only; no semantic approval or query adoption.",
        "terms": [node for node in nodes if node["review_status"] == "pending"][:30],
        "edges": [edge for edge in edges if edge["status"] == "candidate"][:30],
        "deferred_count": max(0, sum(edge["status"] == "candidate" for edge in edges) - 30),
    }
    network = {
        "schema_version": SCHEMA_VERSION, "network_schema_version": "keyword-network-0.1",
        "scope_id": scope_id, "package_count": len(snapshots),
        "observation_count": len(observations), "node_count": len(nodes), "edge_count": len(edges),
        "reviewed_edge_count": 0, "approved_edge_count": 0,
        "candidate_node_count": len(nodes), "candidate_edge_count": sum(edge["status"] == "candidate" for edge in edges),
        "coverage_claim": "observed_package_records_only",
        "new_network_request_count": 0, "source_index": source_index,
        "cooccurrence_limits": {"max_edges": max_cooccurrence_edges, "max_degree": max_cooccurrence_degree,
                                "min_document_frequency": min_cooccurrence_document_frequency},
    }
    readme = """# Keyword Knowledge Network\n\nThis is a deterministic, read-only network built from validated Research Search Packages.\n\n- Observations retain paper fields, evidence IDs and run IDs.\n- Cooccurrence edges are candidates only; no edge is approved or adopted automatically.\n- No network requests were made.\n- Use the review workbench before any explicit adoption or query experiment.\n"""
    payloads = {
        "network.json": json.dumps(network, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        "nodes.jsonl": "".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in nodes),
        "edges.jsonl": "".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in edges),
        "observations.jsonl": "".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in observations),
        "candidate-frontier.json": json.dumps(frontier, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        "review-events.jsonl": "", "adoption-events.jsonl": "", "network-experiments.jsonl": "",
        "source-index.jsonl": "".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in source_index),
        "README.md": readme,
    }
    output.mkdir(parents=True, exist_ok=False)
    for name, content in payloads.items():
        (output / name).write_text(content, encoding="utf-8", newline="\n")
    manifest = {
        "schema_version": SCHEMA_VERSION, "status": "completed", "scope_id": scope_id,
        "network_schema_version": "keyword-network-0.1",
        "files": {name: hashlib.sha256(content.encode("utf-8")).hexdigest() for name, content in payloads.items()},
    }
    (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"network_schema_version": "keyword-network-0.1", "network": network, "frontier": frontier, "manifest": manifest}
