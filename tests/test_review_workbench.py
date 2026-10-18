"""Export contract tests; interactive file:// acceptance belongs to browser E2E."""
from __future__ import annotations

import hashlib
import json
import re
import socket
from pathlib import Path

import pytest

from research_search.models import Paper, SearchRun
from research_search.review_workbench import export_review_workbench
from research_search.validation import validate_package


STAMP = "2026-10-18T00:00:00+00:00"
BLIND_FIELDS = {"paper_id", "title", "authors", "publication_year", "abstract", "database_keywords", "doi", "pmid", "openalex_id"}


def paper(paper_id: str, **values):
    return {
        **Paper(paper_id, "A source paper", abstract="Source abstract", publication_year=2024,
                authors=["A. Author"], doi="10.1234/example", pmid="123456", openalex_id="https://openalex.org/W1",
                author_keywords=["author-only"], database_keywords=["Database Term"],
                source_url="https://example.org/source", retrieved_at=STAMP, source_run_ids=["run-1"]).to_dict(),
        **values,
    }


def make_package(root: Path, records: list[dict], *, scope_id="scope-1", description="A fixed review scope", query="SECRET query"):
    """Small valid 0.1 fixture, independent from the changing workflow module."""
    root.mkdir()
    scope = {"schema_version": "0.1", "scope_id": scope_id, "description": description,
             "mode": "exploratory", "research_object": ["object"], "input_modality": ["input"],
             "research_task": ["task"], "method": [], "application": [], "constraints": {}, "unspecified": []}
    group = {"group_id": "g1", "label": "Object", "terms": ["object"]}
    plan = {"schema_version": "0.1", "plan_id": "plan-1", "version": 1, "strategy": "exploratory",
            "database": "openalex", "group_ids": ["g1"], "groups": [group],
            "logic": {"op": "AND", "groups": ["g1"]}, "query": query,
            "status": "planned", "reason": None, "syntax_status": "local_checked"}
    run = SearchRun("run-1", "plan-1", "success", returned_count=len(records), fetched_count=len(records),
                    deduplicated_count=len(records), request_count=0, started_at=STAMP, finished_at=STAMP,
                    paper_ids=[record["paper_id"] for record in records], mode="replay").to_dict()
    evidence = []
    keywords = []
    judgments = []
    if records:
        paper_id = records[0]["paper_id"]
        evidence = [{"schema_version": "0.1", "evidence_id": "ev-1", "source_type": "paper_metadata",
                     "source_url": "https://example.org/source", "evidence_level": "U", "retrieved_at": STAMP,
                     "locator": "title", "supports": "observed", "paper_id": paper_id,
                     "excerpt": records[0]["title"], "run_ids": ["run-1"]}]
        keywords = [{"schema_version": "0.1", "term_id": "term-1", "term": "SECRET inferred term",
                     "canonical_term": "SECRET inferred term", "category": "unclassified", "relationship": "unclassified",
                     "source_type": "paper_metadata", "evidence_status": "observed_in_paper", "evidence_ids": ["ev-1"],
                     "paper_ids": [paper_id], "document_frequency": 1, "retrieval_status": "untested", "adopted": False}]
        judgments = [{"schema_version": "0.1", "judgment_id": "SECRET judgment", "paper_id": paper_id,
                      "scope_id": scope_id, "label": "relevant", "judge_type": "human",
                      "rationale": "SECRET historical rationale", "judged_at": STAMP}]
    values = {"01-research-scope.json": scope, "02-keywords.json": keywords, "03-search-strategies.json": [plan],
              "06-evaluation.json": {"SECRET score": .99}, "input-case.json": {"SECRET candidate identity": True}}
    for name, value in values.items():
        (root / name).write_text(json.dumps(value, ensure_ascii=True) + "\n", encoding="utf-8")
    for name, values in {"04-papers.jsonl": records, "05-search-runs.jsonl": [run],
                         "07-evidence.jsonl": evidence, "10-judgments.jsonl": judgments}.items():
        (root / name).write_text("".join(json.dumps(value, ensure_ascii=True) + "\n" for value in values), encoding="utf-8")
    (root / "README.md").write_text("SECRET package identity\n", encoding="utf-8")
    manifest = {"package_schema_version": "0.1", "case_id": "SECRET-case", "snapshot_kind": "SECRET-snapshot",
                "files": {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in root.iterdir()}}
    (root / "manifest.json").write_text(json.dumps(manifest) + "\n", encoding="utf-8")
    validate_package(root)
    return root


def read_queue(root):
    return [json.loads(line) for line in (root / "review-queue.jsonl").read_text(encoding="utf-8").splitlines()]


def embedded(root):
    html = (root / "index.html").read_text(encoding="utf-8")
    match = re.search(r'<script type="application/json" id="initial-workbench-data">(.*?)</script>', html, re.S)
    assert match is not None
    return html, json.loads(match.group(1))


def test_old_01_package_export_is_offline_blinded_and_hashed(tmp_path, monkeypatch):
    package = make_package(tmp_path / "package", [paper("p1")])
    before = {path.name: path.read_bytes() for path in package.iterdir()}
    monkeypatch.setattr(socket, "create_connection", lambda *a, **kw: (_ for _ in ()).throw(AssertionError("network")))
    output = tmp_path / "workbench"
    result = export_review_workbench([package], output)
    assert result["paper_count"] == 1 and result["package_count"] == 1
    assert result["files"] == {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in output.iterdir() if path.name != "manifest.json"
    }
    assert set(path.name for path in output.iterdir()) == {
        "index.html", "review-queue.jsonl", "judgments.jsonl", "README.md", "manifest.json"
    }
    assert (output / "judgments.jsonl").read_bytes() == b""
    assert json.loads((output / "manifest.json").read_text()) == result
    html, data = embedded(output)
    assert set(data["items"][0]) == BLIND_FIELDS
    assert data["items"][0]["database_keywords"] == ["Database Term"]
    assert data["items"][0]["doi"] == "10.1234/example"
    assert data["items"][0]["pmid"] == "123456"
    assert data["items"][0]["openalex_id"] == "https://openalex.org/W1"
    assert data["research_scope"]["description"] == "A fixed review scope"
    assert data["research_scope"]["research_object"] == ["object"]
    assert data["research_scope"]["research_task"] == ["task"]
    assert "SECRET" not in html
    assert str(package.resolve()) not in html
    assert "author-only" not in html
    assert "fetch(" not in html and "XMLHttpRequest" not in html
    assert "<script src=" not in html
    assert "SECRET query" not in html and "SECRET-snapshot" not in html
    queue = read_queue(output)
    source = queue[0]["source_audit"][0]
    assert source["source_plans"][0]["query"] == "SECRET query"
    assert source["source_runs"][0]["run_id"] == "run-1"
    assert source["source_evidence"][0]["evidence_id"] == "ev-1"
    assert source["paper_metadata"]["author_keywords"] == ["author-only"]
    assert source["package_manifest_sha256"]
    assert "package_manifest" not in source
    assert "evaluation" not in source
    assert "input_case" not in source
    assert "historical_judgments" not in source
    assert "package_path" not in source
    assert "snapshot_kind" not in source
    assert {path.name: path.read_bytes() for path in package.iterdir()} == before


def test_union_deduplicates_and_has_strategy_independent_stable_order(tmp_path):
    first = make_package(tmp_path / "base", [paper("p1"), paper("p2")], query="SECRET base")
    second = make_package(tmp_path / "candidate", [paper("p2"), paper("p3")], query="SECRET candidate")
    one, two, single = tmp_path / "one", tmp_path / "two", tmp_path / "single"
    result = export_review_workbench([first, second], one)
    export_review_workbench([second, first], two)
    export_review_workbench([first], single)
    queue = read_queue(one)
    assert len(queue) == 3 and {item["paper_id"] for item in queue} == {"p1", "p2", "p3"}
    assert len(next(item for item in queue if item["paper_id"] == "p2")["source_audit"]) == 2
    assert (one / "index.html").read_bytes() == (two / "index.html").read_bytes()
    expected_order = sorted(["p1", "p2", "p3"], key=lambda pid: (hashlib.sha256(("scope-1\0" + pid).encode()).hexdigest(), pid))
    assert [item["paper_id"] for item in queue] == expected_order
    old_order = [item["paper_id"] for item in read_queue(single)]
    assert [pid for pid in expected_order if pid in {"p1", "p2"}] == old_order
    assert result["queue_fingerprint"] == embedded(two)[1]["queue_fingerprint"]
    assert set(next(item for item in queue if item["paper_id"] == "p2")["source_audit"][0]) == {
        "package_manifest_sha256", "paper_metadata", "source_runs", "source_plans", "source_evidence"
    }


def test_all_input_validation_precedes_output_and_existing_exports_are_protected(tmp_path):
    package = make_package(tmp_path / "package", [paper("p1")])
    output = tmp_path / "output"
    with pytest.raises(ValueError, match="non-empty list"):
        export_review_workbench([], output)
    assert not output.exists()
    other = make_package(tmp_path / "other", [paper("p2")], scope_id="other")
    with pytest.raises(ValueError, match="same research scope"):
        export_review_workbench([package, other], output)
    assert not output.exists()
    changed_scope = make_package(tmp_path / "changed-scope", [paper("p3")], description="Changed boundary")
    with pytest.raises(ValueError, match="identical research scope"):
        export_review_workbench([package, changed_scope], output)
    assert not output.exists()
    (other / "README.md").write_text("tampered")
    with pytest.raises(ValueError, match="hash mismatch"):
        export_review_workbench([package, other], output)
    assert not output.exists()
    with pytest.raises(ValueError, match="inside an input package"):
        export_review_workbench([package], package / "nested-output")
    export_review_workbench([package], output)
    before = {path.name: path.read_bytes() for path in output.iterdir()}
    with pytest.raises(FileExistsError):
        export_review_workbench([package], output)
    assert {path.name: path.read_bytes() for path in output.iterdir()} == before


def test_linked_inputs_and_destination_are_rejected(tmp_path):
    package = make_package(tmp_path / "package", [paper("p1")])
    linked = tmp_path / "linked-package"
    linked.symlink_to(package, target_is_directory=True)
    with pytest.raises(ValueError, match="symlink"):
        export_review_workbench([linked], tmp_path / "output")
    output = tmp_path / "linked-output"
    output.symlink_to(tmp_path / "does-not-exist", target_is_directory=True)
    with pytest.raises(FileExistsError):
        export_review_workbench([package], output)


def test_embedded_json_safely_preserves_untrusted_metadata(tmp_path):
    malicious = '</script><script>globalThis.injected=true</script> & "quotes"\u2028\u2029'
    package = make_package(tmp_path / "package", [paper("p1", title=malicious, abstract=malicious, database_keywords=[malicious])])
    output = tmp_path / "output"
    export_review_workbench([package], output)
    html, data = embedded(output)
    assert data["items"][0]["title"] == malicious
    assert data["items"][0]["abstract"] == malicious
    assert data["items"][0]["database_keywords"] == [malicious]
    assert malicious not in html
    assert "\\u003c/script\\u003e" in html
    assert len((output / "review-queue.jsonl").read_text().splitlines()) == 1
    assert read_queue(output)[0]["title"] == malicious


def test_empty_package_exports_an_empty_valid_workbench(tmp_path):
    package = make_package(tmp_path / "package", [])
    output = tmp_path / "output"
    result = export_review_workbench([package], output)
    assert result["paper_count"] == 0
    assert embedded(output)[1]["items"] == []
    assert (output / "review-queue.jsonl").read_bytes() == b""
