import copy
import hashlib
import json
import socket
from pathlib import Path

import pytest

from research_search.acquisition_handoff import (
    acquisition_handoff,
    build_acquisition_queue,
    compare_manifests,
    load_search_input,
    paper_metadata_hash,
    stable_paper_id,
    write_acquisition_handoff,
)
from research_search.models import Paper
from research_search.workflow import run_package


def paper(paper_id="p1", **values):
    return {**Paper(paper_id, "A paper", doi="10.1234/example", pmid="123", source_url="https://example.org/record").to_dict(), **values}


def make_package(path):
    case = {"schema_version": "0.1", "case_id": "p3-test",
            "research_scope": {"schema_version": "0.1", "scope_id": "scope-1", "description": "Offline engineering test",
                               "mode": "exploratory", "research_object": ["angle"], "input_modality": ["EMG"],
                               "research_task": ["estimation"], "method": [], "application": [], "constraints": {}, "unspecified": []},
            "concept_groups": [{"group_id": "input", "label": "Input", "role": "input", "terms": ["EMG"]},
                               {"group_id": "object", "label": "Object", "role": "object", "terms": ["angle"]}]}
    snapshots = {"schema_version": "0.1", "snapshot_kind": "synthetic_test_fixture", "snapshots": [
        {"strategy": "exploratory", "retrieved_at": "2026-10-17T00:00:00+00:00",
         "response": {"meta": {"count": 1}, "results": [{"id": "https://openalex.org/W123", "title": "EMG angle",
                       "doi": "https://doi.org/10.1234/example", "keywords": [{"display_name": "EMG"}]}]}}]}
    run_package(case, path, snapshots=snapshots)
    return path


def test_cli_acquisition_handoff_method_builds_or_writes(tmp_path):
    queue = acquisition_handoff(papers=[paper()])
    assert queue["schema_version"].startswith("p3-acquisition")
    target = tmp_path / "handoff.json"
    written = acquisition_handoff(papers=[paper()], output_path=target)
    assert json.loads(target.read_text()) == written


def test_metadata_queue_preserves_identifiers_and_requires_human():
    record = paper()
    result = build_acquisition_queue(papers=[record])
    item = result["items"][0]
    assert {key: item[key] for key in ("paper_id", "doi", "pmid", "source_url")} == {key: record[key] for key in ("paper_id", "doi", "pmid", "source_url")}
    assert item["availability"] == "metadata_only"
    assert item["open_access_url"] is None
    assert item["requires_human_follow_up"]
    assert item["provenance"]["record_index"] == 0
    assert result["policy"]["network_calls"] == 0


def test_explicit_public_candidate_has_provenance():
    result = build_acquisition_queue([paper(open_access_url="https://example.org/public.pdf", is_open_access=True)])
    item = result["items"][0]
    assert item["availability"] == "open_access_candidate"
    assert item["open_access_url"] == "https://example.org/public.pdf"
    assert {"open_access_url", "is_open_access"}.issubset(item["provenance"]["fields"])
    assert not item["provenance"]["access_assertion_verified_online"]


@pytest.mark.parametrize("fields", [
    {"open_access_url": "https://example.org/full.pdf"},
    {"doi": "https://doi.org/10.1234/x", "source_url": "https://example.org/full.pdf"},
    {"open_access_url": "https://example.org/full.pdf", "is_open_access": False},
    {"open_access_url": "https://example.org/full.pdf", "is_open_access": True, "oa_status": "closed"},
])
def test_no_open_access_is_guessed(fields):
    item = build_acquisition_queue([paper(**fields)])["items"][0]
    assert item["availability"] == "metadata_only"
    assert item["open_access_url"] is None


def test_public_alias_requires_original_assertion():
    item = build_acquisition_queue([paper(oa_url="https://example.org/x.pdf", publicly_available=True)])["items"][0]
    assert item["availability"] == "open_access_candidate"
    assert "publicly_available" in item["provenance"]["fields"]


def test_user_supplied_fulltext_is_assertion_not_file_read(tmp_path):
    missing = tmp_path / "not-downloaded.pdf"
    item = build_acquisition_queue([paper(user_supplied_fulltext=True, fulltext_path=str(missing))])["items"][0]
    assert item["availability"] == "user_supplied_fulltext"
    assert item["requires_human_follow_up"]
    assert not missing.exists()


@pytest.mark.parametrize("url", ["javascript:alert(1)", "file:///etc/passwd", "https://user:secret@example.org/x", "https://example.org/a\nb"])
def test_invalid_explicit_public_url_is_rejected(url):
    with pytest.raises(ValueError, match="open_access_url"):
        build_acquisition_queue([paper(open_access_url=url, is_open_access=True)])


def test_validated_package_is_read_only(tmp_path):
    package = make_package(tmp_path / "package")
    before = {str(path.relative_to(package)): path.read_bytes() for path in package.rglob("*") if path.is_file()}
    queue = build_acquisition_queue(package)
    assert queue["items"][0]["provenance"]["source_manifest_sha256"] == hashlib.sha256((package / "manifest.json").read_bytes()).hexdigest()
    after = {str(path.relative_to(package)): path.read_bytes() for path in package.rglob("*") if path.is_file()}
    assert after == before


def test_tampered_package_fails_before_handoff_is_created(tmp_path):
    package = make_package(tmp_path / "package")
    (package / "README.md").write_text("edited", encoding="utf-8")
    output = tmp_path / "new" / "handoff.json"
    with pytest.raises(ValueError, match="hash mismatch"):
        write_acquisition_handoff(package, output)
    assert not output.parent.exists()


def test_invalid_and_duplicate_papers_fail_before_output(tmp_path):
    for records in ([{"title": "missing id"}], [paper(), paper()], [paper(authors="not a list")]):
        with pytest.raises(ValueError):
            write_acquisition_handoff(records, tmp_path / "new" / "handoff.json")
        assert not (tmp_path / "new").exists()


def test_existing_handoff_refuses_overwrite(tmp_path):
    path = tmp_path / "handoff.json"
    write_acquisition_handoff([paper()], path)
    before = path.read_bytes()
    with pytest.raises(FileExistsError):
        write_acquisition_handoff([paper("other")], path)
    assert path.read_bytes() == before


def test_json_and_jsonl_explicit_input(tmp_path):
    json_path, jsonl_path = tmp_path / "papers.json", tmp_path / "papers.jsonl"
    json_path.write_text(json.dumps({"papers": [paper()]}), encoding="utf-8")
    jsonl_path.write_text(json.dumps(paper()) + "\n", encoding="utf-8")
    assert build_acquisition_queue(json_path) == build_acquisition_queue(jsonl_path)


def test_incremental_added_updated_unchanged_removed():
    previous = {"papers": {pid: {"metadata_sha256": paper_metadata_hash(paper(pid))} for pid in ("same", "changed", "removed")}}
    delta = compare_manifests(previous, [paper("same"), paper("changed", abstract="changed"), paper("added")])
    assert delta == {"added": ["added"], "updated": ["changed"], "unchanged": ["same"], "removed_candidates": ["removed"]}


def test_user_fields_are_not_metadata_changes_and_input_is_not_mutated():
    record = paper()
    original = copy.deepcopy(record)
    baseline = paper_metadata_hash(record)
    record.update(reading_status="已读", user_notes="my notes", translation="human text")
    assert paper_metadata_hash(record) == baseline
    build_acquisition_queue([record])
    assert {key: record[key] for key in original} == original
    assert stable_paper_id(record) == "p1"


def test_queue_has_no_network_calls(monkeypatch):
    def blocked(*args, **kwargs):
        raise AssertionError("network attempted")
    monkeypatch.setattr(socket, "create_connection", blocked)
    build_acquisition_queue([paper(open_access_url="https://example.org/full.pdf", is_open_access=True)])


def test_input_requires_one_source_and_rejects_symlink_package(tmp_path):
    with pytest.raises(ValueError, match="source or papers"):
        load_search_input([paper()], papers=[paper()])
    package = make_package(tmp_path / "package")
    (package / "outside-link").symlink_to(tmp_path / "missing")
    with pytest.raises(ValueError, match="symlinks"):
        build_acquisition_queue(package)
