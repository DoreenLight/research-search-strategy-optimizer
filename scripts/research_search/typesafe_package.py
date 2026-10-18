"""Apply optional Jev reranking to an existing Research Search Package Top-K."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Callable, Mapping

from .typesafe_reranker import RerankConfig, rerank_papers


def _json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def rerank_package_topk(
    package_dir: str | Path,
    *,
    strategy: str,
    output_dir: str | Path,
    config: RerankConfig | None = None,
    judger: Callable[..., Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    package = Path(package_dir)
    output = Path(output_dir)
    if output.exists():
        raise FileExistsError(f"rerank output already exists: {output}")
    if not package.is_dir() or package.is_symlink():
        raise ValueError("package directory not found or is a symlink")
    plans = _json(package / "03-search-strategies.json")
    plan = next((item for item in plans if item.get("strategy") == strategy), None)
    if plan is None:
        raise ValueError(f"strategy not found: {strategy}")
    papers = [json.loads(line) for line in (package / "04-papers.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    result = rerank_papers(plan["query"], papers, config=config, judger=judger)
    output.mkdir(parents=True)
    payload = {
        "schema_version": "0.1-typesafe-rerank",
        "package_dir": str(package.resolve()),
        "strategy": strategy,
        "route": (config or RerankConfig()).route,
        "query": plan["query"],
        "candidate_count": len(papers),
        "top_k": (config or RerankConfig()).top_k,
        "candidate_set_changed": False,
        **result,
        "input_candidate_ids_sha256": hashlib.sha256(json.dumps([p["paper_id"] for p in papers], sort_keys=True).encode()).hexdigest(),
        "human_relevance_claim": False,
        "evaluation_note": "Jev scores reorder the existing shortlist only; they are not human relevance labels or retrieval truth.",
    }
    (output / "rerank.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest = {"schema_version": "0.1", "files": {"rerank.json": hashlib.sha256((output / "rerank.json").read_bytes()).hexdigest()}}
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return payload
