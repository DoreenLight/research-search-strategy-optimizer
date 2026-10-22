from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import pytest

from research_search.p4_review import prepare_p4_review


STAMP = "2026-10-18T00:00:00+00:00"


def _run(*paper_ids: str) -> dict:
    return {
        "baseline_id": "A",
        "status": "success",
        "mode": "replay",
        "paper_ids": list(paper_ids),
        "request_count": 0,
        "fetched_count": len(paper_ids),
        "deduplicated_count": len(set(paper_ids)),
        "source_explanation": "offline fixture",
    }


def _manifest(*, papers=("p1", "p2"), include_discovery=False, model_judgments=None) -> dict:
    test_case = {
        "case_id": "test-case",
        "domain_kind": "mature",
        "split": "test",
        "reference_set": None,
        "human_judgments": {"old": "relevant"},
        "model_judgments": model_judgments or {"p1": "relevant"},
        "runs": [_run(*papers)],
    }
    cases = [test_case]
    if include_discovery:
        cases.insert(0, {
            "case_id": "discovery-case",
            "domain_kind": "emerging",
            "split": "discovery",
            "reference_set": None,
            "human_judgments": {},
            "model_judgments": {},
            "runs": [_run("d1")],
        })
    return {"schema_version": "0.1", "k": 2, "cases": cases}


def _write_reviewer(path: Path, reviewer_id: str, rows: list[dict]) -> Path:
    path.write_text(
        "".join(json.dumps({"reviewer_id": reviewer_id, **row}, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
    )
    return path


def _row(paper_id: str, label: str = "relevant", *, judged_at: str = STAMP, rationale: str = "meets scope", evidence_locator: str = "abstract") -> dict:
    return {
        "paper_id": paper_id,
        "label": label,
        "rationale": rationale,
        "evidence_locator": evidence_locator,
        "judged_at": judged_at,
    }


def _reviewers(tmp_path: Path, rows1: list[dict] | None = None, rows2: list[dict] | None = None) -> list[Path]:
    rows1 = rows1 or [_row("p1"), _row("p2", "irrelevant")]
    rows2 = rows2 or [_row("p1"), _row("p2", "irrelevant")]
    return [
        _write_reviewer(tmp_path / "reviewer-a.jsonl", "r-a", rows1),
        _write_reviewer(tmp_path / "reviewer-b.jsonl", "r-b", rows2),
    ]


def _jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def test_successful_dual_agreement_writes_consensus_and_counts(tmp_path):
    output = tmp_path / "p4-review"
    result = prepare_p4_review(
        _manifest(), ["p1", "ref-only"], "external manual freeze 2026-10-18", _reviewers(tmp_path), output,
        test_case_id="test-case",
    )

    assert result["benchmark_manifest"]["cases"][0]["human_judgments"] == {
        "p1": "relevant", "p2": "irrelevant"
    }
    assert result["summary"]["actual_review_count"] == 4
    assert result["summary"]["coverage_count"] == 2
    assert result["summary"]["pending_count"] == 0
    assert result["summary"]["conflict_count"] == 0
    assert result["summary"]["reference_set"] == ["p1", "ref-only"]
    assert result["summary"]["reference_set_source"] == "external manual freeze 2026-10-18"
    reviewed = _jsonl(output / "reviewed.jsonl")
    assert len(reviewed) == 2
    assert reviewed[0]["judgments"][0]["reviewer_id"] in {"r-a", "r-b"}
    assert reviewed[0]["consensus_label"] == "relevant"
    assert reviewed[0]["conflict"] is False
    assert reviewed[0]["adjudication_status"] == "not_needed"
    assert "rationale" in reviewed[0]["judgments"][0]
    assert "evidence_locator" in reviewed[0]["judgments"][0]


def test_conflict_preserves_both_judgments_and_does_not_adjudicate(tmp_path):
    reviewers = _reviewers(tmp_path, [_row("p1", "relevant"), _row("p2")], [_row("p1", "irrelevant"), _row("p2")])
    result = prepare_p4_review(
        _manifest(), ["p1"], "freeze source", reviewers, tmp_path / "output", test_case_id="test-case"
    )

    reviewed = _jsonl(tmp_path / "output/reviewed.jsonl")
    p1 = next(item for item in reviewed if item["paper_id"] == "p1")
    assert [item["label"] for item in p1["judgments"]] == ["relevant", "irrelevant"]
    assert p1["consensus_label"] == "pending"
    assert p1["conflict"] is True
    assert p1["adjudication_status"] == "pending_adjudication"
    assert result["benchmark_manifest"]["cases"][0]["human_judgments"] == {"p2": "relevant"}
    conflicts = _jsonl(tmp_path / "output/conflicts.jsonl")
    assert any(item["paper_id"] == "p1" and item["reason"] == "conflict" for item in conflicts)
    assert result["summary"]["conflict_count"] == 1


def test_missing_coverage_is_pending_and_conflict_is_recorded(tmp_path):
    reviewers = _reviewers(tmp_path, [_row("p1")], [_row("p1"), _row("p2")])
    result = prepare_p4_review(
        _manifest(), ["p1"], "freeze source", reviewers, tmp_path / "output", test_case_id="test-case"
    )

    reviewed = {item["paper_id"]: item for item in _jsonl(tmp_path / "output/reviewed.jsonl")}
    assert reviewed["p2"]["judgments"][0] is not None
    assert reviewed["p2"]["judgments"][1] is None
    assert reviewed["p2"]["consensus_label"] == "pending"
    assert reviewed["p2"]["conflict"] is True
    assert reviewed["p2"]["adjudication_status"] == "missing_reviewer"
    assert result["benchmark_manifest"]["cases"][0]["human_judgments"] == {"p1": "relevant"}
    conflicts = _jsonl(tmp_path / "output/conflicts.jsonl")
    assert any(item["paper_id"] == "p2" and item["reason"] == "missing_reviewer" for item in conflicts)
    assert result["summary"]["coverage_count"] == 1
    assert result["summary"]["pending_count"] == 1


def test_reference_set_is_independent_and_only_target_test_case_changes(tmp_path):
    manifest = _manifest(include_discovery=True)
    before = copy.deepcopy(manifest)
    result = prepare_p4_review(
        manifest, ["ref-1", "ref-2"], "author-held external source", _reviewers(tmp_path), tmp_path / "output",
        test_case_id="test-case",
    )

    assert manifest == before
    output_manifest = result["benchmark_manifest"]
    discovery, test = output_manifest["cases"]
    assert discovery == before["cases"][0]
    assert test["split"] == "test"
    assert test["reference_set"] == ["ref-1", "ref-2"]
    assert test["reference_set_independent"] is True
    assert test["reference_set_source"] == "author-held external source"
    assert test["human_judgments"] == {"p1": "relevant", "p2": "irrelevant"}
    assert test["model_judgments"] == before["cases"][1]["model_judgments"]


def test_pending_never_enters_benchmark_human_judgments(tmp_path):
    reviewers = _reviewers(tmp_path, [_row("p1", "pending"), _row("p2", "irrelevant")], [_row("p1", "uncertain"), _row("p2", "irrelevant")])
    result = prepare_p4_review(
        _manifest(), ["p1"], "freeze source", reviewers, tmp_path / "output", test_case_id="test-case"
    )
    assert result["benchmark_manifest"]["cases"][0]["human_judgments"] == {"p2": "irrelevant"}
    reviewed = {item["paper_id"]: item for item in _jsonl(tmp_path / "output/reviewed.jsonl")}
    assert reviewed["p1"]["consensus_label"] == "pending"


def test_output_hash_covers_three_payloads_not_itself(tmp_path):
    output = tmp_path / "output"
    prepare_p4_review(
        _manifest(), ["p1"], "freeze source", _reviewers(tmp_path), output, test_case_id="test-case"
    )
    hashes = json.loads((output / "manifest.sha256.json").read_text(encoding="utf-8"))
    assert set(hashes["files"]) == {"reviewed.jsonl", "conflicts.jsonl", "benchmark-manifest.json"}
    assert "manifest.sha256.json" not in hashes["files"]
    for name, digest in hashes["files"].items():
        assert hashlib.sha256((output / name).read_bytes()).hexdigest() == digest
    assert (output / "reviewed.jsonl").read_bytes().endswith(b"\n")
    assert (output / "benchmark-manifest.json").read_bytes().endswith(b"\n")


def test_existing_output_is_rejected_without_overwrite(tmp_path):
    output = tmp_path / "output"
    output.mkdir()
    marker = output / "marker"
    marker.write_text("keep", encoding="utf-8")
    with pytest.raises(FileExistsError):
        prepare_p4_review(
            _manifest(), ["p1"], "freeze source", _reviewers(tmp_path), output, test_case_id="test-case"
        )
    assert marker.read_text(encoding="utf-8") == "keep"


@pytest.mark.parametrize("mutate", [
    lambda rows: rows.__setitem__(0, _row("p1", "maybe")),
    lambda rows: rows.__setitem__(0, _row("p1", "relevant", judged_at="2026-10-18")),
    lambda rows: rows.extend([_row("p1")]),
])
def test_invalid_label_date_and_duplicate_paper_are_rejected_before_output(tmp_path, mutate):
    rows = [_row("p1"), _row("p2", "irrelevant")]
    mutate(rows)
    reviewers = [
        _write_reviewer(tmp_path / "reviewer-a.jsonl", "r-a", rows),
        _write_reviewer(tmp_path / "reviewer-b.jsonl", "r-b", [_row("p1"), _row("p2", "irrelevant")]),
    ]
    output = tmp_path / "output"
    with pytest.raises(ValueError):
        prepare_p4_review(_manifest(), ["p1"], "freeze source", reviewers, output, test_case_id="test-case")
    assert not output.exists()


def test_duplicate_reviewer_ids_are_rejected_before_output(tmp_path):
    reviewers = [
        _write_reviewer(tmp_path / "reviewer-a.jsonl", "same", [_row("p1"), _row("p2")]),
        _write_reviewer(tmp_path / "reviewer-b.jsonl", "same", [_row("p1"), _row("p2")]),
    ]
    output = tmp_path / "output"
    with pytest.raises(ValueError, match="reviewer"):
        prepare_p4_review(_manifest(), ["p1"], "freeze source", reviewers, output, test_case_id="test-case")
    assert not output.exists()
