import csv
import hashlib
import json
from pathlib import Path

import pytest

from research_search.models import Evidence, Judgment, KeywordCandidate, Paper, SearchRun
from research_search.reading_export import export_reading, export_reading_material, open_obsidian, safe_note_filename
from research_search.acquisition_handoff import paper_metadata_hash


def paper(paper_id="p1", **values):
    return {**Paper(paper_id, "A / unsafe: title\nwith `ticks`", abstract=None, authors=["Author\nTwo"],
                     publication_year=2024, doi="10.1234/example", pmid="123", source_title="Journal",
                     source_url="https://example.org/record", retrieved_at="2026-10-17T00:00:00+00:00",
                     source_run_ids=["run-1"]).to_dict(), **values}


def context(records):
    return {"papers": records,
            "evidence": [Evidence("ev-1", "paper_metadata", "https://example.org/cite", "A",
                                   "2026-10-17T00:00:00+00:00", locator="abstract", supports="observed",
                                   paper_id=records[0]["paper_id"], excerpt="not provided", run_ids=["run-1"]).to_dict()],
            "keywords": [KeywordCandidate("term-1", "safe term", "safe term", "unclassified", "unclassified",
                                           "paper_metadata", "observed_in_paper", evidence_ids=["ev-1"],
                                           paper_ids=[records[0]["paper_id"]], document_frequency=1).to_dict()],
            "runs": [SearchRun("run-1", "plan-1", "success", paper_ids=[records[0]["paper_id"]]).to_dict()],
            "judgments": [Judgment("j-human", records[0]["paper_id"], "scope-1", "relevant", "human", "checked",
                                    "2026-10-17T00:00:00+00:00").to_dict(),
                           Judgment("j-model", records[0]["paper_id"], "scope-1", "irrelevant", "model", "model only",
                                    "2026-10-17T00:00:00+00:00").to_dict()]}


def manifest_files_match(root, manifest):
    actual = {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
              for path in root.rglob("*") if path.is_file() and path.name != "manifest.json"}
    assert manifest["files"] == actual
    assert "manifest.json" not in manifest["files"]


def test_cli_export_and_manual_open_methods_are_offline(tmp_path):
    root = tmp_path / "export"
    export_reading([paper()], root)
    opened = open_obsidian(root)
    assert opened["status"] == "manual_import_required"
    assert opened["opened"] is False
    assert opened["vault_scanned"] is False
    assert opened["vault_written"] is False


def test_safe_filename_is_deterministic_and_conflict_resistant():
    one = safe_note_filename("../same/title", "paper-1")
    two = safe_note_filename("same title", "paper-2")
    assert one != two
    assert "/" not in one and "\\" not in one and not one.startswith(".")
    assert one.endswith(hashlib.sha256(b"paper-1").hexdigest() + ".md")


def test_export_writes_index_notes_handoff_manifest_and_optional_metadata(tmp_path):
    records = [paper()]
    result = export_reading_material(context(records), tmp_path / "export", metadata_formats=["jsonl", "csv"])
    root = tmp_path / "export"
    assert {"index.md", "handoff.json", "metadata.jsonl", "metadata.csv"}.issubset(result["files"])
    assert (root / "manifest.json").is_file()
    note = next((root / "papers").glob("*.md"))
    text = note.read_text(encoding="utf-8")
    assert "# 阅读任务" in text and "## 摘要" in text
    assert "未提供" in text
    assert "https://example.org/cite" in text
    assert "模型相关性不代表人工确认" in text
    assert "irrelevant" in text and "relevant" in text
    manifest_files_match(root, result)
    assert json.loads((root / "handoff.json").read_text())["limits"]["vault_written"] is False


def test_frontmatter_is_json_yaml_compatible_and_untrusted_text_is_fenced(tmp_path):
    record = paper(title='A "quoted" title\n---\n<script>alert(1)</script>', abstract='line 1\nline 2\n```\nline 3')
    export_reading_material([record], tmp_path / "export")
    note = next((tmp_path / "export/papers").glob("*.md"))
    text = note.read_text(encoding="utf-8")
    front = text.split("\n---\n", 1)[0][4:]
    parsed = json.loads(front)
    assert parsed["title"].startswith("A ")
    assert "<script>" not in text.split("# 阅读任务", 1)[0]
    assert "```" in text


def test_missing_abstract_is_not_invented(tmp_path):
    export_reading_material([paper(abstract=None)], tmp_path / "export")
    text = next((tmp_path / "export/papers").glob("*.md")).read_text()
    assert "## 摘要" in text
    assert "未提供" in text
    assert "摘要不存在" not in text


def test_urls_are_retained_as_citations_without_fetch(tmp_path, monkeypatch):
    import urllib.request
    monkeypatch.setattr(urllib.request, "urlopen", lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("network")))
    export_reading_material(context([paper()]), tmp_path / "export")
    assert "https://example.org/cite" in next((tmp_path / "export/papers").glob("*.md")).read_text()


def test_csv_formula_prefix_is_escaped(tmp_path):
    record = paper(title="=SUM(A1:A2)", source_url="+cmd")
    export_reading_material([record], tmp_path / "export", metadata_formats="csv")
    with (tmp_path / "export/metadata.csv").open(newline="", encoding="utf-8") as handle:
        row = next(csv.DictReader(handle))
    assert row["title"].startswith("'")
    assert row["source_url"].startswith("'")


def test_invalid_input_creates_no_export_directory(tmp_path):
    invalid = paper()
    invalid["authors"] = "not a list"
    with pytest.raises(ValueError):
        export_reading_material([invalid], tmp_path / "bad")
    assert not (tmp_path / "bad").exists()


def test_existing_export_is_not_overwritten(tmp_path):
    output = tmp_path / "export"
    export_reading_material([paper()], output)
    before = {path.relative_to(output): path.read_bytes() for path in output.rglob("*") if path.is_file()}
    with pytest.raises(FileExistsError):
        export_reading_material([paper("other")], output)
    after = {path.relative_to(output): path.read_bytes() for path in output.rglob("*") if path.is_file()}
    assert after == before


def test_original_records_are_not_mutated(tmp_path):
    record = paper()
    before = json.loads(json.dumps(record))
    export_reading_material([record], tmp_path / "export")
    assert record == before


def test_incremental_added_changed_removed_and_manifest_hash(tmp_path):
    old_root = tmp_path / "old"
    export_reading_material([paper("same"), paper("changed"), paper("removed")], old_root)
    old_files = {str(path.relative_to(old_root)): path.read_bytes() for path in old_root.rglob("*") if path.is_file()}
    changed = paper("changed", abstract="new source metadata")
    new_root = tmp_path / "new"
    new_manifest = export_reading_material([paper("same"), changed, paper("added")], new_root,
                                           old_manifest=old_root / "manifest.json")
    assert new_manifest["incremental"] == {"added": ["added"], "removed_candidates": ["removed"],
                                            "unchanged": ["same"], "updated": ["changed"]}
    assert new_manifest["user_note_changes"]["modified"] == []
    manifest_files_match(new_root, new_manifest)
    assert {str(path.relative_to(old_root)): path.read_bytes() for path in old_root.rglob("*") if path.is_file()} == old_files


def test_user_modified_old_note_is_preserved_separately(tmp_path):
    old_root = tmp_path / "old"
    old_manifest = export_reading_material([paper()], old_root)
    old_note = next((old_root / "papers").glob("*.md"))
    old_note.write_text(old_note.read_text() + "\nUSER EDIT\n", encoding="utf-8")
    new_root = tmp_path / "new"
    manifest = export_reading_material([paper()], new_root, old_manifest=old_root / "manifest.json")
    assert manifest["user_note_changes"] == {"missing": [], "modified": ["p1"], "not_checked": []}
    preserved = list((new_root / "preserved-user-notes").glob("*.txt"))
    assert len(preserved) == 1 and "USER EDIT" in preserved[0].read_text()
    assert "USER EDIT" not in next((new_root / "papers").glob("*.md")).read_text()


def test_mapping_old_manifest_reports_not_checked_without_vault_scan(tmp_path):
    old_manifest = {"papers": {"p1": {"metadata_sha256": paper_metadata_hash(paper()), "path": "papers/does-not-exist.md", "note_sha256": "x"}}}
    result = export_reading_material([paper()], tmp_path / "new", old_manifest=old_manifest)
    assert result["user_note_changes"] == {"missing": [], "modified": [], "not_checked": ["p1"]}


def test_removed_candidates_are_not_deleted_and_old_directory_is_untouched(tmp_path):
    old_root = tmp_path / "old"
    export_reading_material([paper("old")], old_root)
    export_reading_material([paper("new")], tmp_path / "new", old_manifest=old_root / "manifest.json")
    assert next((old_root / "papers").glob("*.md")).exists()


def test_metadata_jsonl_is_one_safe_json_object_per_line(tmp_path):
    export_reading_material([paper(title='a\nb')], tmp_path / "export", metadata_formats="jsonl")
    lines = (tmp_path / "export/metadata.jsonl").read_text().splitlines()
    assert len(lines) == 1
    assert json.loads(lines[0])["paper_id"] == "p1"
