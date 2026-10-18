"""Offline metadata handoff: no downloads, URL visits, logins or paywall bypass."""
from __future__ import annotations

from collections.abc import Mapping, Sequence
import hashlib
import json
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from .models import Paper
from .validation import validate_package, validate_record

SCHEMA_VERSION = "p3-acquisition-0.1"
_PAPER_FIELDS = set(Paper.__dataclass_fields__)
_ACCESS_FIELDS = (
    "open_access_url", "oa_url", "public_fulltext_url", "is_open_access",
    "open_access", "publicly_available", "oa_status", "user_supplied_fulltext",
    "availability",
)
_PUBLIC_STATUSES = {"open", "open_access", "public", "gold", "green", "hybrid", "bronze"}


def _json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, sort_keys=True, allow_nan=False)


def _digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _paper(record: Any) -> dict[str, Any]:
    if isinstance(record, Paper):
        record = record.to_dict()
    if not isinstance(record, Mapping):
        raise ValueError("each paper must be an object")
    try:
        # A JSON round trip copies nested lists and rejects non-data values.
        record = json.loads(_json(dict(record)))
        base = Paper(**{key: value for key, value in record.items() if key in _PAPER_FIELDS}).to_dict()
    except (TypeError, ValueError) as error:
        raise ValueError("invalid paper record") from error
    validate_record("paper", base)
    if not base["paper_id"].strip() or not base["title"].strip():
        raise ValueError("paper_id and title must not be blank")
    for key in ("is_open_access", "open_access", "publicly_available", "user_supplied_fulltext"):
        if key in record and type(record[key]) is not bool:
            raise ValueError(f"{key} must be a boolean")
    for key in ("open_access_url", "oa_url", "public_fulltext_url", "oa_status", "availability"):
        if key in record and record[key] is not None and not isinstance(record[key], str):
            raise ValueError(f"{key} must be a string or null")
    return {**base, **{key: record[key] for key in _ACCESS_FIELDS if key in record}}


def _json_file(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise ValueError(f"cannot read JSON input: {path}") from error


def _jsonl_file(path: Path) -> list[Any]:
    try:
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    except (OSError, ValueError) as error:
        raise ValueError(f"cannot read JSONL input: {path}") from error


def _load_input(source: Any = None, *, papers: Sequence[Mapping[str, Any]] | None = None) -> dict[str, Any]:
    """Private shared adapter; packages are always validated with hashes enabled."""
    if papers is not None:
        if source is not None:
            raise ValueError("provide source or papers, not both")
        source = papers
    context: dict[str, Any] = {"evidence": [], "keywords": [], "judgments": [], "runs": [],
                               "case_id": None, "manifest_sha256": None, "kind": "explicit_records"}
    if isinstance(source, (str, Path)):
        path = Path(source)
        if path.is_dir():
            # Reject linked input files before validation follows any fixed
            # package path. No scan outside the explicitly supplied package.
            if any(item.is_symlink() for item in path.rglob("*")):
                raise ValueError("package must not contain symlinks")
            validate_package(path)
            manifest = _json_file(path / "manifest.json")
            context.update(kind="research_search_package", case_id=manifest.get("case_id"),
                           manifest_sha256=_digest((path / "manifest.json").read_bytes()),
                           evidence=_jsonl_file(path / "07-evidence.jsonl"),
                           keywords=_json_file(path / "02-keywords.json"),
                           judgments=_jsonl_file(path / "10-judgments.jsonl"),
                           runs=_jsonl_file(path / "05-search-runs.jsonl"))
            source = _jsonl_file(path / "04-papers.jsonl")
        elif path.is_file():
            source = _jsonl_file(path) if path.suffix.lower() == ".jsonl" else _json_file(path)
        else:
            raise ValueError(f"input not found: {path}")
    if isinstance(source, Mapping):
        # Explicit records may carry the same optional context as a package;
        # their schema/ID validation is kept local and never opens URLs.
        for key, kind in (("evidence", "evidence"), ("keywords", "keyword"), ("judgments", "judgment"), ("runs", "search-run")):
            values = source.get(key, [])
            if not isinstance(values, list):
                raise ValueError(f"{key} must be an array")
            for value in values:
                validate_record(kind, value)
            context[key] = json.loads(_json(values))
        source = source.get("papers")
    if not isinstance(source, Sequence) or isinstance(source, (str, bytes)):
        raise ValueError("provide a saved package or an explicit papers array")
    records = [_paper(record) for record in source]
    ids = [record["paper_id"] for record in records]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate paper_id")
    known = set(ids)
    for item in context["evidence"] + context["judgments"]:
        if item.get("paper_id") not in known:
            raise ValueError("context has dangling paper_id")
    for item in context["keywords"]:
        if not set(item["paper_ids"]).issubset(known):
            raise ValueError("keyword has dangling paper_id")
    return {**context, "papers": records}


def _metadata_hash(record: Mapping[str, Any]) -> str:
    # Only source metadata/access assertions enter this hash; no reading status
    # or user-note fields are used for incremental metadata comparison.
    return _digest(_json(_paper(record)).encode("utf-8"))


def _queue(loaded: Mapping[str, Any]) -> dict[str, Any]:
    items = []
    for index, paper in enumerate(loaded["papers"]):
        url_field = next((key for key in ("open_access_url", "oa_url", "public_fulltext_url") if paper.get(key)), None)
        url = paper.get(url_field) if url_field else None
        # A URL alone is insufficient: the original record must explicitly
        # assert public availability. No URL is derived from a DOI/source URL.
        markers = [key for key in ("is_open_access", "open_access", "publicly_available") if paper.get(key) is True]
        if paper.get("oa_status", "") in _PUBLIC_STATUSES:
            markers.append("oa_status")
        public = bool(markers) and not any(paper.get(key) is False for key in ("is_open_access", "open_access", "publicly_available"))
        public = public and paper.get("availability") != "metadata_only" and paper.get("oa_status") != "closed"
        if public and url:
            try:
                parsed = urlsplit(url)
                safe_url = parsed.scheme.lower() in {"http", "https"} and bool(parsed.hostname) and not parsed.username and not parsed.password
            except ValueError:
                safe_url = False
            if not safe_url or any(char.isspace() or ord(char) < 32 for char in url):
                raise ValueError("open_access_url must be an absolute public HTTP(S) URL")
        else:
            url = None
        supplied = paper.get("user_supplied_fulltext") is True or paper.get("availability") == "user_supplied_fulltext"
        availability = "user_supplied_fulltext" if supplied else "open_access_candidate" if url else "metadata_only"
        fields = ["paper_id", "doi", "pmid", "source_url"]
        if url:
            fields += [url_field or "open_access_url", *markers]
        if supplied:
            fields += ["user_supplied_fulltext" if paper.get("user_supplied_fulltext") is True else "availability"]
        items.append({
            "paper_id": paper["paper_id"], "doi": paper.get("doi"), "pmid": paper.get("pmid"),
            "source_url": paper.get("source_url"), "open_access_url": url, "availability": availability,
            "provenance": {"input_kind": loaded["kind"], "record_index": index, "fields": fields,
                           "source_manifest_sha256": loaded["manifest_sha256"],
                           "record_sha256": _metadata_hash(paper), "access_assertion_verified_online": False},
            "requires_human_follow_up": True,
        })
    return {"schema_version": SCHEMA_VERSION, "items": items,
            "policy": {"network_calls": 0, "downloads": False, "login": False, "paywall_bypass": False,
                       "default_next_step": "human_follow_up"}}


def stable_paper_id(record: Mapping[str, Any]) -> str:
    """Return the explicit paper_id used for deterministic incremental identity."""
    paper_id = record.get("paper_id")
    if not isinstance(paper_id, str) or not paper_id.strip():
        raise ValueError("paper_id is required")
    return paper_id


def paper_metadata_hash(record: Mapping[str, Any]) -> str:
    """Hash source metadata only; user reading fields are not accepted here."""
    return _metadata_hash(record)


def load_search_input(source: Any = None, *, papers: Sequence[Mapping[str, Any]] | None = None) -> dict[str, Any]:
    """Load and validate a package or explicit records without writing files."""
    return _load_input(source, papers=papers)


def build_acquisition_queue(source: Any = None, *, papers: Sequence[Mapping[str, Any]] | None = None) -> dict[str, Any]:
    """Return a lawful handoff from a validated package or explicit records.

    Explicit records extend Paper with optional ``open_access_url`` plus
    ``is_open_access: true``, or ``user_supplied_fulltext: true``. These are
    producer assertions, not independently verified permissions or fetched files.
    """
    return _queue(_load_input(source, papers=papers))


def write_acquisition_handoff(source: Any, output_path: str | Path, *, papers: Sequence[Mapping[str, Any]] | None = None) -> dict[str, Any]:
    """Write a new JSON handoff, rejecting invalid input before making output."""
    output = Path(output_path)
    if output.exists() or output.is_symlink():
        raise FileExistsError(f"output already exists: {output}")
    queue = build_acquisition_queue(source, papers=papers)
    payload = _json(queue) + "\n"
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as handle:
        handle.write(payload)
    return queue


def acquisition_handoff(
    source: Any = None,
    output_path: str | Path | None = None,
    *,
    papers: Sequence[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """CLI-facing method: build in memory or write one new handoff file."""
    if output_path is None:
        return build_acquisition_queue(source, papers=papers)
    return write_acquisition_handoff(source, output_path, papers=papers)


def _old_entries(manifest: Any) -> dict[str, Any]:
    if manifest is None:
        return {}
    if isinstance(manifest, (str, Path)):
        manifest = _json_file(Path(manifest))
    if not isinstance(manifest, Mapping) or not isinstance(manifest.get("papers"), Mapping):
        raise ValueError("old manifest must contain a papers object")
    for paper_id, entry in manifest["papers"].items():
        if not isinstance(paper_id, str) or not isinstance(entry, Mapping) or not isinstance(entry.get("metadata_sha256"), str):
            raise ValueError("invalid old manifest paper entry")
    return dict(manifest["papers"])


def compare_manifests(old_manifest: Any, papers: Sequence[Mapping[str, Any]]) -> dict[str, list[str]]:
    """Compare exact stable paper_id/source metadata; report removals, never delete."""
    old = _old_entries(old_manifest)
    new = {paper["paper_id"]: _metadata_hash(paper) for paper in _load_input(papers)["papers"]}
    common = old.keys() & new.keys()
    return {"added": sorted(new.keys() - old.keys()),
            "updated": sorted(pid for pid in common if new[pid] != old[pid]["metadata_sha256"]),
            "unchanged": sorted(pid for pid in common if new[pid] == old[pid]["metadata_sha256"]),
            "removed_candidates": sorted(old.keys() - new.keys())}


__all__ = [
    "acquisition_handoff",
    "build_acquisition_queue",
    "compare_manifests",
    "load_search_input",
    "paper_metadata_hash",
    "stable_paper_id",
    "write_acquisition_handoff",
]
