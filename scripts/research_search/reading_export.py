"""Offline reading exports into a caller-selected, new project directory.

No Vault discovery, download, login, permission resolution or network access.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
import csv
import hashlib
import io
import json
from pathlib import Path
import re
from typing import Any
import unicodedata
from urllib.parse import quote

from .acquisition_handoff import (
    _old_entries,
    _queue,
    compare_manifests,
    load_search_input,
    paper_metadata_hash,
)

SCHEMA_VERSION = "p3-reading-export-0.1"
_CSV_FIELDS = ("paper_id", "title", "authors", "publication_year", "doi", "pmid", "abstract",
               "source_title", "source_url", "retrieved_at", "source_run_ids")


def _json(value: Any) -> str:
    # ASCII escapes keep U+0085/U+2028/U+2029 and control characters inside
    # JSON/YAML strings instead of accidentally creating extra source lines.
    return json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True, allow_nan=False).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026") + "\n"


def _hash(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def safe_note_filename(title: str, paper_id: str) -> str:
    """Safe UTF-8-bounded title plus deterministic full stable-ID SHA-256."""
    slug = unicodedata.normalize("NFKC", title)
    slug = re.sub(r"[^\w-]+", "-", slug).strip("-_") or "paper"
    # Bound bytes, not characters, to fit common 255-byte filesystem limits.
    slug = slug.encode("utf-8")[:100].decode("utf-8", errors="ignore").rstrip("-_") or "paper"
    return f"{slug}--{_hash(paper_id.encode('utf-8'))}.md"


def _literal(value: Any) -> str:
    """Render untrusted metadata only inside a non-executable Markdown fence."""
    if value is None or value == "" or value == []:
        text = "未提供"
    elif isinstance(value, (list, dict)):
        text = _json(value).rstrip()
    else:
        text = str(value)
    # Normalize unusual Markdown line separators before choosing a fence.
    text = text.replace("\r", "\n").replace("\x85", "\n").replace("\u2028", "\n").replace("\u2029", "\n")
    fence = "`" * max(3, 1 + max((len(run) for run in re.findall(r"`+", text)), default=0))
    return f"{fence}\n{text}\n{fence}\n"


def _relevance(judgments: Sequence[Mapping[str, Any]], paper_id: str) -> dict[str, Any]:
    by_type = {
        kind: sorted({item["label"] for item in judgments if item["paper_id"] == paper_id and item["judge_type"] == kind})
        for kind in ("human", "model")
    }
    human = by_type["human"]
    return {"relevance_status": human[0] if len(human) == 1 else "待人工确认",
            "human_judgments": human, "model_judgments": by_type["model"],
            "model_promoted_to_human": False}


def _note(paper: Mapping[str, Any], loaded: Mapping[str, Any]) -> tuple[bytes, str]:
    paper_id = paper["paper_id"]
    relevance = _relevance(loaded["judgments"], paper_id)
    evidence = [item for item in loaded["evidence"] if item["paper_id"] == paper_id]
    evidence_ids = {item["evidence_id"] for item in evidence}
    keywords = [item for item in loaded["keywords"]
                if paper_id in item["paper_ids"] or evidence_ids.intersection(item["evidence_ids"])]
    runs = [item for item in loaded["runs"] if item["run_id"] in paper["source_run_ids"]]
    front = {"schema_version": SCHEMA_VERSION,
             **{key: paper.get(key) for key in _CSV_FIELDS if key != "abstract"},
             "reading_status": "待确认", "reading_status_options": ["待确认", "待读", "已读"],
             "translation": "", "innovation_points": "", "case_id": loaded["case_id"], **relevance}
    # JSON is valid YAML 1.2: no YAML tags, hand-written quoting or executable data.
    sections = ["---\n" + _json(front) + "---\n\n# 阅读任务\n",
                "状态默认为 **待确认**；可人工改为 **待读** / **已读**。模型相关性不代表人工确认。\n",
                "## 标题\n" + _literal(paper["title"]),
                "## 作者\n" + _literal(paper["authors"]),
                "## 年份 / DOI / PMID\n" + _literal({key: paper[key] for key in ("publication_year", "doi", "pmid")}),
                "## 摘要\n" + _literal(paper["abstract"]),
                "## 来源\n" + _literal({key: paper[key] for key in ("source_title", "source_url", "retrieved_at")}),
                "## 检索 / 运行 ID\n" + _literal({"case_id": loaded["case_id"], "source_run_ids": paper["source_run_ids"],
                                                        "plan_ids": [item["plan_id"] for item in runs]}),
                "## 相关性状态\n" + _literal(relevance),
                "## 关键词（保留来源，不自动采用）\n" + _literal(keywords),
                "## 证据与引用 URL\n" + _literal(evidence),
                "## 译文\n未分析，留空供人工填写。\n",
                "## 创新点\n未分析，留空供人工填写。\n",
                "## 用户笔记\n\n"]
    return "\n".join(sections).encode("utf-8"), relevance["relevance_status"]


def _old_manifest(value: Any) -> tuple[Mapping[str, Any] | None, Path | None]:
    root = None
    if isinstance(value, (str, Path)):
        path = Path(value)
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            raise ValueError(f"invalid old manifest: {path}") from error
        root = path.parent.resolve()
    _old_entries(value)  # Shape check; do not reject legitimate user-edited notes.
    return value, root


def _previous_notes(manifest: Mapping[str, Any] | None, root: Path | None) -> tuple[dict[str, bytes], dict[str, list[str]]]:
    changed: dict[str, bytes] = {}
    state: dict[str, list[str]] = {"modified": [], "missing": [], "not_checked": []}
    for paper_id, entry in _old_entries(manifest).items():
        if root is None:
            state["not_checked"].append(paper_id)
            continue
        relative = entry.get("path")
        if not isinstance(relative, str) or Path(relative).is_absolute() or ".." in Path(relative).parts:
            raise ValueError("unsafe old note path")
        path = root / relative
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            raise ValueError("unsafe old note path")
        if not path.is_file():
            state["missing"].append(paper_id)
            continue
        try:
            data = path.read_bytes()
        except OSError as error:
            raise ValueError(f"cannot read previous note: {relative}") from error
        if _hash(data) != entry.get("note_sha256"):
            changed[paper_id] = data
            state["modified"].append(paper_id)
    return changed, {key: sorted(values) for key, values in state.items()}


def _csv_value(value: Any) -> str:
    text = "" if value is None else json.dumps(value, ensure_ascii=True) if isinstance(value, list) else str(value)
    # Defend leading whitespace/control characters as well as direct formulas.
    first = re.sub(r"^[\s\x00-\x20\x7f\ufeff]+", "", text)[:1]
    return "'" + text if first in {"=", "+", "-", "@"} else text


def _metadata(records: Sequence[Mapping[str, Any]], formats: set[str]) -> dict[str, bytes]:
    rows = [{key: paper[key] for key in _CSV_FIELDS} for paper in records]
    output = {}
    if "jsonl" in formats:
        output["metadata.jsonl"] = "".join(json.dumps(row, ensure_ascii=True, sort_keys=True, allow_nan=False) + "\n" for row in rows).encode("utf-8")
    if "csv" in formats:
        stream = io.StringIO(newline="")
        writer = csv.DictWriter(stream, fieldnames=_CSV_FIELDS)
        writer.writeheader()
        writer.writerows({key: _csv_value(value) for key, value in row.items()} for row in rows)
        output["metadata.csv"] = stream.getvalue().encode("utf-8")
    return output


def _index(records: Sequence[Mapping[str, Any]], entries: Mapping[str, Any], statuses: Mapping[str, str], delta: Mapping[str, Any], preserved: Mapping[str, str]) -> bytes:
    lines = ["# 阅读导出索引\n", "仅在指定的新项目导出目录创建文件；未扫描/写入用户 Vault，未下载全文、登录、绕过付费墙或解决访问权限。\n",
             "阅读状态：待确认 / 待读 / 已读。模型标注不自动成为人工相关性；译文与创新点未分析。\n", "## 论文\n"]
    for number, paper in enumerate(records, 1):
        paper_id = paper["paper_id"]
        lines += [f"### {number}. [阅读卡片]({quote(entries[paper_id]['path'], safe='/')})\n",
                  _literal({"标题": paper["title"], "年份": paper["publication_year"], "阅读状态": "待确认", "人工相关性": statuses[paper_id]})]
    lines += ["## 增量（removed_candidates 仅报告，未删除）\n", _literal(delta),
              "## 用户编辑保留副本\n", "旧笔记不覆盖；修改内容作为逐字节 `.txt` 副本保留，不自动合并到新元数据笔记。\n", _literal(preserved)]
    return "\n".join(lines).encode("utf-8")


def export_reading_material(
    source: Any,
    output_dir: str | Path,
    *,
    papers: Sequence[Mapping[str, Any]] | None = None,
    old_manifest: Mapping[str, Any] | str | Path | None = None,
    metadata_formats: Sequence[str] | str = (),
) -> dict[str, Any]:
    """Create new notes/index/handoff/hashed manifest; never overwrite old notes.

    ``old_manifest`` may be a path (checks only explicitly named old notes), or
    a mapping (metadata comparison only; note checks reported as not_checked).
    The caller must select a new project export directory, not a live Vault.
    """
    output = Path(output_dir)
    if output.exists() or output.is_symlink():
        raise FileExistsError(f"export directory already exists: {output}")
    if not isinstance(metadata_formats, (str, Sequence)):
        raise ValueError("metadata_formats must be jsonl/csv or a sequence")
    formats = {metadata_formats} if isinstance(metadata_formats, str) else set(metadata_formats)
    if not formats.issubset({"jsonl", "csv"}):
        raise ValueError("metadata_formats supports only jsonl and csv")
    # All input validation/formatting happens before any directory is created.
    loaded = load_search_input(source, papers=papers)
    records = sorted(loaded["papers"], key=lambda item: item["paper_id"])
    queue = _queue(loaded)
    previous, previous_root = _old_manifest(old_manifest)
    if previous_root is not None and output.resolve().is_relative_to(previous_root):
        raise ValueError("new export must not be inside the previous export")
    if isinstance(source, (str, Path)) and Path(source).is_dir() and output.resolve().is_relative_to(Path(source).resolve()):
        raise ValueError("export must not modify the source package")
    delta = compare_manifests(previous, records)
    modified_notes, note_changes = _previous_notes(previous, previous_root)
    files: dict[str, bytes] = {}
    entries, statuses = {}, {}
    for paper in records:
        paper_id = paper["paper_id"]
        path = "papers/" + safe_note_filename(paper["title"], paper_id)
        if path in files:
            raise ValueError("note filename hash collision")
        files[path], statuses[paper_id] = _note(paper, loaded)
        entries[paper_id] = {"path": path, "metadata_sha256": paper_metadata_hash(paper), "note_sha256": _hash(files[path])}
    preserved = {}
    for paper_id, data in sorted(modified_notes.items()):
        path = f"preserved-user-notes/{_hash(paper_id.encode('utf-8'))}.md.txt"
        files[path] = data
        preserved[paper_id] = path
    files.update(_metadata(records, formats))
    files["index.md"] = _index(records, entries, statuses, delta, preserved)
    handoff = {"schema_version": SCHEMA_VERSION, "acquisition_queue": queue, "incremental": delta,
               "user_note_changes": note_changes, "preserved_user_notes": preserved,
               "source": {"kind": loaded["kind"], "case_id": loaded["case_id"], "manifest_sha256": loaded["manifest_sha256"]},
               "limits": {"network_calls": 0, "fulltext_downloaded": False, "vault_scanned": False,
                          "vault_written": False, "permissions_resolved": False, "old_notes_deleted": False}}
    files["handoff.json"] = _json(handoff).encode("utf-8")
    manifest = {"schema_version": SCHEMA_VERSION, "papers": entries, "incremental": delta,
                "user_note_changes": note_changes, "preserved_user_notes": preserved,
                "source": handoff["source"], "files": {path: _hash(data) for path, data in sorted(files.items())}}
    files["manifest.json"] = _json(manifest).encode("utf-8")
    # Exclusive creation prevents overwriting an existing directory/notes,
    # including a concurrent exporter. No input errors can leave an output.
    output.mkdir(parents=True, exist_ok=False)
    (output / "papers").mkdir()
    for relative, data in files.items():
        path = output / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as handle:
            handle.write(data)
    return manifest


def export_reading(
    source: Any,
    output_dir: str | Path,
    *,
    papers: Sequence[Mapping[str, Any]] | None = None,
    old_manifest: Mapping[str, Any] | str | Path | None = None,
    metadata_formats: Sequence[str] | str = (),
) -> dict[str, Any]:
    """CLI-facing spelling of export_reading_material; identical return contract."""
    return export_reading_material(source, output_dir, papers=papers,
                                   old_manifest=old_manifest, metadata_formats=metadata_formats)


def open_obsidian(export_dir: str | Path) -> dict[str, Any]:
    """Validate an export and return manual-open instructions; launch nothing.

    Obsidian/Vault integration is intentionally not performed by P3. No Vault
    name/path or obsidian:// command is guessed or executed.
    """
    root = Path(export_dir)
    if not root.is_dir() or root.is_symlink():
        raise ValueError("reading export directory not found or is a symlink")
    try:
        manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise ValueError("invalid reading export manifest") from error
    if not isinstance(manifest, dict) or manifest.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("not a P3 reading export")
    files = manifest.get("files")
    if not isinstance(files, dict) or not {"index.md", "handoff.json"}.issubset(files):
        raise ValueError("invalid reading export inventory")
    paths = list(root.rglob("*"))
    if any(path.is_symlink() for path in paths):
        raise ValueError("reading export must not contain symlinks")
    actual = {str(path.relative_to(root)) for path in paths if path.is_file() and path != root / "manifest.json"}
    if set(files) != actual:
        raise ValueError("reading export inventory mismatch")
    for relative, digest in files.items():
        path = root / relative
        if Path(relative).is_absolute() or ".." in Path(relative).parts or not path.resolve().is_relative_to(root.resolve()):
            raise ValueError("unsafe reading export path")
        if _hash(path.read_bytes()) != digest:
            raise ValueError(f"reading export hash mismatch: {relative}")
    return {"status": "manual_import_required", "opened": False,
            "export_dir": str(root.resolve()), "index_path": str((root / "index.md").resolve()),
            "vault_scanned": False, "vault_written": False, "network_calls": 0,
            "instruction": "请人工查看 index.md；如需导入 Obsidian，请自行选择 Vault 并复制已确认的笔记。"}


__all__ = ["export_reading", "export_reading_material", "open_obsidian", "safe_note_filename"]
