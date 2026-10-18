"""Build an offline, blinded human-review workbench for Research Search Packages.

The exporter is deliberately independent from the workflow/CLI layer.  It reads
validated P0/P1 packages, keeps detailed provenance in ``review-queue.jsonl``,
and puts only a small public paper projection in the self-contained HTML page.
No network access is performed by this module.
"""
from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
import hashlib
import json
from pathlib import Path
from typing import Any

from .validation import validate_package


SCHEMA_VERSION = "0.1"
_WORKBENCH_TEMPLATE = "review-workbench.html"
_REQUIRED_PACKAGE_FILES = (
    "01-research-scope.json",
    "02-keywords.json",
    "03-search-strategies.json",
    "04-papers.jsonl",
    "05-search-runs.jsonl",
    "07-evidence.jsonl",
    "10-judgments.jsonl",
    "manifest.json",
)
def _json_bytes(value: Any, *, ascii_only: bool = False) -> bytes:
    """Serialize JSON with stable ordering and no non-standard numbers."""
    return (
        json.dumps(
            value,
            ensure_ascii=ascii_only,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")


def _jsonl_bytes(values: Iterable[Mapping[str, Any]]) -> bytes:
    # Escaping Unicode line separators also keeps each JSON value on one line
    # for tools that use str.splitlines() rather than splitting only on LF.
    return b"".join(_json_bytes(value, ascii_only=True) for value in values)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as error:
        raise ValueError(f"cannot read JSON file: {path.name}") from error


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise ValueError(f"cannot read JSONL file: {path.name}") from error
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except ValueError as error:
            raise ValueError(f"invalid JSONL in {path.name} line {line_number}") from error
        if not isinstance(value, dict):
            raise ValueError(f"JSONL record must be an object: {path.name} line {line_number}")
        records.append(value)
    return records


def _canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _normalise_package_path(value: str | Path) -> Path:
    path = Path(value)
    if path.is_symlink() or not path.is_dir():
        raise ValueError(f"package directory not found or is a symlink: {path}")
    # Do not let a validated package contain an alias to data outside its root.
    if any(item.is_symlink() for item in path.rglob("*")):
        raise ValueError(f"package must not contain symlinks: {path}")
    return path.resolve()


def _check_package_files(package: Path) -> None:
    missing = [name for name in _REQUIRED_PACKAGE_FILES if not (package / name).is_file()]
    if missing:
        raise ValueError(f"package missing required files: {', '.join(missing)}")


def _safe_copy(value: Any) -> Any:
    """Copy JSON values and fail before any output is created."""
    try:
        return json.loads(_canonical(value))
    except (TypeError, ValueError) as error:
        raise ValueError("package metadata must contain JSON values") from error


def _paper_without_run_ids(paper: Mapping[str, Any]) -> dict[str, Any]:
    result = {key: _safe_copy(value) for key, value in paper.items() if key != "source_run_ids"}
    result.setdefault("source_run_ids", [])
    return result


def _scope_key(scope: Mapping[str, Any]) -> str:
    scope_id = scope.get("scope_id")
    if not isinstance(scope_id, str) or not scope_id.strip():
        raise ValueError("research scope must contain a non-empty scope_id")
    return scope_id


def _package_snapshot(package: Path, package_index: int) -> dict[str, Any]:
    """Read one already validated package into an immutable JSON snapshot."""
    _check_package_files(package)
    # Validation is intentionally called here, once per explicitly supplied package.
    validate_package(package)
    manifest = _read_json(package / "manifest.json")
    scope = _read_json(package / "01-research-scope.json")
    plans = _read_json(package / "03-search-strategies.json")
    papers = _read_jsonl(package / "04-papers.jsonl")
    runs = _read_jsonl(package / "05-search-runs.jsonl")
    evidence = _read_jsonl(package / "07-evidence.jsonl")
    if not isinstance(scope, dict) or not isinstance(plans, list):
        raise ValueError(f"invalid package top-level records: {package}")
    scope_id = _scope_key(scope)
    package_manifest_bytes = (package / "manifest.json").read_bytes()
    manifest_sha256 = _sha256(package_manifest_bytes)
    case_id = manifest.get("case_id") if isinstance(manifest, dict) else None
    if case_id is not None and not isinstance(case_id, str):
        raise ValueError("manifest.case_id must be a string or null")

    plan_by_id = {item.get("plan_id"): item for item in plans if isinstance(item, dict)}
    run_by_id = {item.get("run_id"): item for item in runs if isinstance(item, dict)}
    paper_ids = {item.get("paper_id") for item in papers}
    if None in paper_ids:
        raise ValueError(f"package paper record has no paper_id: {package}")

    paper_sources: dict[str, dict[str, Any]] = {}
    for paper in papers:
        paper_id = paper["paper_id"]
        source_run_ids = sorted({run_id for run_id in paper.get("source_run_ids", []) if isinstance(run_id, str)})
        source_runs = [
            _safe_copy(run_by_id[run_id])
            for run_id in source_run_ids
            if run_id in run_by_id
        ]
        plan_ids = sorted({run_by_id[run_id].get("plan_id") for run_id in source_run_ids if run_id in run_by_id})
        source_plans = [
            _safe_copy(plan_by_id[plan_id])
            for plan_id in plan_ids
            if plan_id in plan_by_id
        ]
        source_evidence = [
            _safe_copy(item)
            for item in evidence
            if item.get("paper_id") == paper_id
        ]
        paper_sources[paper_id] = {
            # Keep only the stable package digest plus records needed to trace
            # this paper; do not repeat package paths, full manifests, scores,
            # input cases, or historical judgments for every queue item.
            "package_manifest_sha256": manifest_sha256,
            "paper_metadata": _safe_copy(paper),
            "source_runs": source_runs,
            "source_plans": source_plans,
            "source_evidence": source_evidence,
        }
    return {
        "package": package,
        "package_index": package_index,
        "scope": _safe_copy(scope),
        "scope_id": scope_id,
        "manifest": _safe_copy(manifest),
        "manifest_sha256": manifest_sha256,
        "papers": [_safe_copy(item) for item in papers],
        "paper_sources": paper_sources,
    }


def _merge_papers(snapshots: Sequence[Mapping[str, Any]], scope_id: str) -> list[dict[str, Any]]:
    """Deduplicate papers by stable ID without depending on package order."""
    grouped: dict[str, list[tuple[dict[str, Any], dict[str, Any]]]] = {}
    for snapshot in snapshots:
        for paper in snapshot["papers"]:
            paper_id = paper.get("paper_id")
            if not isinstance(paper_id, str) or not paper_id.strip():
                raise ValueError("paper_id must be a non-empty string")
            source = snapshot["paper_sources"].get(paper_id)
            if source is None:
                raise ValueError(f"missing source audit for paper: {paper_id}")
            grouped.setdefault(paper_id, []).append((paper, source))

    records: list[dict[str, Any]] = []
    for paper_id, variants in grouped.items():
        # Ignore source-run identity while choosing the representative metadata;
        # a new strategy cannot reorder or replace the visible record.
        representative = min(
            (variant for variant, _source in variants),
            key=lambda item: _canonical(_paper_without_run_ids(item)),
        )
        merged = _safe_copy(representative)
        merged["source_run_ids"] = sorted({
            run_id
            for paper, _source in variants
            for run_id in paper.get("source_run_ids", [])
            if isinstance(run_id, str)
        })
        audits = [_safe_copy(source) for _paper, source in variants]
        # Exact duplicate source snapshots can occur when the same package was
        # supplied twice; retain one audit entry rather than inventing identity.
        unique_audits: dict[str, dict[str, Any]] = {
            _canonical(item): item for item in audits
        }
        merged["schema_version"] = str(merged.get("schema_version", SCHEMA_VERSION))
        record = {
            "schema_version": SCHEMA_VERSION,
            "scope_id": scope_id,
            **merged,
            "source_audit": [unique_audits[key] for key in sorted(unique_audits)],
        }
        records.append(record)
    return records


def _blind_projection(record: Mapping[str, Any]) -> dict[str, Any]:
    """Return the only paper fields allowed in the embedded UI data."""
    return {
        "paper_id": str(record.get("paper_id", "")),
        "title": str(record.get("title", "")),
        "authors": [str(value) for value in (record.get("authors") or [])],
        "publication_year": record.get("publication_year"),
        "abstract": record.get("abstract"),
        "database_keywords": [str(value) for value in (record.get("database_keywords") or [])],
        "doi": record.get("doi"),
        "pmid": record.get("pmid"),
        "openalex_id": record.get("openalex_id"),
    }


def _neutral_scope(scope: Mapping[str, Any]) -> dict[str, Any]:
    """Research criteria only, never strategy, evaluation or package identity."""
    return {
        "description": scope["description"],
        **{key: list(scope.get(key, [])) for key in (
            "research_object", "input_modality", "research_task", "method", "application", "unspecified"
        )},
        "constraints": _safe_copy(scope.get("constraints", {})),
    }


def _ordered_blind_items(records: Sequence[Mapping[str, Any]], scope_id: str) -> list[dict[str, Any]]:
    items = [_blind_projection(record) for record in records]
    return sorted(
        items,
        key=lambda item: (
            _sha256(f"{scope_id}\0{item['paper_id']}".encode("utf-8")),
            item["paper_id"],
        ),
    )


def _queue_fingerprint(scope_id: str, scope: Mapping[str, Any], items: Sequence[Mapping[str, Any]]) -> str:
    basis = {"schema_version": SCHEMA_VERSION, "scope_id": scope_id, "research_scope": dict(scope), "items": list(items)}
    return _sha256(_json_bytes(basis, ascii_only=True).rstrip(b"\n"))


def _render_html(scope_id: str, scope: Mapping[str, Any], items: Sequence[Mapping[str, Any]], fingerprint: str) -> bytes:
    template_path = Path(__file__).with_name(_WORKBENCH_TEMPLATE)
    try:
        template = template_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise ValueError(f"review workbench template is unavailable: {template_path}") from error
    data = {
        "schema_version": SCHEMA_VERSION,
        "scope_id": scope_id,
        "research_scope": _safe_copy(scope),
        "queue_fingerprint": fingerprint,
        "items": list(items),
    }
    # Escape every '<', '>' and '&' before embedding JSON in a script element;
    # ensure_ascii also keeps U+2028/U+2029 out of JavaScript source contexts.
    serialized = json.dumps(data, ensure_ascii=True, separators=(",", ":"), allow_nan=False)
    serialized = serialized.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    marker = "__WORKBENCH_DATA_JSON__"
    if template.count(marker) != 1:
        raise ValueError(f"workbench template must contain exactly one {marker} marker")
    return template.replace(marker, serialized).encode("utf-8")


def _readme(scope_id: str, paper_count: int, package_count: int) -> bytes:
    text = f"""# 本地人工审阅工作台

这是一个完全离线的 P1 审阅导出，共 {paper_count} 篇去重论文，来自 {package_count} 个已校验 Research Search Package，研究范围 ID 为 `{scope_id}`。

## 使用

1. 直接打开 `index.html`（`file://`）即可开始；页面初始队列已内嵌，不依赖网络或 CDN。
2. 填写 `reviewer_id`，逐篇选择“相关 / 不相关 / 待确认”，并填写原因与证据定位；保存后自动进入下一篇。
3. 可选择本目录的 `review-queue.jsonl` 重新载入队列，也可导入本人导出的 `judgments.jsonl`。导入文件必须属于当前研究范围、论文队列和审阅者。
4. 点击导出得到新的 `judgments.jsonl`；原始判断按审阅者保留，不会用另一位审阅者的记录覆盖。

## 文件

- `index.html`：不含检索策略、候选身份、模型分数或历史人工标签的盲审页面。
- `review-queue.jsonl`：完整论文元数据和来源审计（检索版本、Run、查询、证据等），供审阅后离线查看。
- `judgments.jsonl`：初始为空；页面导出的人工判断记录。
- `manifest.json`：除自身外所有文件的 SHA-256。

`localStorage` 仅尽力按研究范围、队列指纹和 `reviewer_id` 保存当前审阅者状态；浏览器对 `file://` 的本地存储限制不会阻止页面和文件导入/导出功能。此工作台只支持人工相关性判断，不证明检索收益或实验结论。
"""
    return text.encode("utf-8")


def export_review_workbench(packages: list[Path], output_dir: Path) -> dict[str, Any]:
    """Export a new, standalone offline review workbench.

    ``packages`` must contain one or more validated Research Search Packages.
    Each package is validated before any output directory is created.  The
    destination is exclusive and is never overwritten.
    """
    if not isinstance(packages, list) or not packages:
        raise ValueError("packages must be a non-empty list")
    output = Path(output_dir)
    if output.exists() or output.is_symlink():
        raise FileExistsError(f"review workbench output already exists: {output}")

    package_paths = [_normalise_package_path(package) for package in packages]
    output_resolved = output.resolve()
    if any(output_resolved.is_relative_to(package) for package in package_paths):
        raise ValueError("review workbench output must not be inside an input package")

    # All validation and reads happen before output.mkdir, so bad input leaves
    # no partially-created export behind.
    snapshots = [_package_snapshot(package, index) for index, package in enumerate(package_paths)]
    scope_ids = {snapshot["scope_id"] for snapshot in snapshots}
    if len(scope_ids) != 1:
        raise ValueError("all packages must use the same research scope")
    scope_id = next(iter(scope_ids))
    scope_values = {_canonical(snapshot["scope"]) for snapshot in snapshots}
    if len(scope_values) != 1:
        raise ValueError("all packages must use identical research scope metadata")

    records = _merge_papers(snapshots, scope_id)
    items = _ordered_blind_items(records, scope_id)
    neutral_scope = _neutral_scope(snapshots[0]["scope"])
    fingerprint = _queue_fingerprint(scope_id, neutral_scope, items)
    full_by_id = {record["paper_id"]: record for record in records}
    queue_records = [
        {**full_by_id[item["paper_id"]], "queue_fingerprint": fingerprint}
        for item in items
    ]

    payloads: dict[str, bytes] = {
        "index.html": _render_html(scope_id, neutral_scope, items, fingerprint),
        "review-queue.jsonl": _jsonl_bytes(queue_records),
        "judgments.jsonl": b"",
        "README.md": _readme(scope_id, len(items), len(package_paths)),
    }
    manifest: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "workbench_schema_version": "p1-review-workbench-0.1",
        "scope_id": scope_id,
        "queue_fingerprint": fingerprint,
        "paper_count": len(items),
        "package_count": len(package_paths),
        "files": {name: _sha256(data) for name, data in sorted(payloads.items())},
    }
    payloads["manifest.json"] = _json_bytes(manifest)

    output.mkdir(parents=True, exist_ok=False)
    # A filesystem failure may leave a partial directory for inspection. Never
    # remove or reuse it silently: a retry must choose a new destination.
    for relative, data in payloads.items():
        with (output / relative).open("xb") as handle:
            handle.write(data)
    return manifest


__all__ = ["export_review_workbench"]
