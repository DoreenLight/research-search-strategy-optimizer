import hashlib
import json
from pathlib import Path

import pytest

from research_search.models import Paper
from research_search.openalex_client import OpenAlexSearchResult
from research_search.workflow import run_package

ROOT = Path(__file__).resolve().parents[1]


def case():
    return {"schema_version": "0.1", "case_id": "toy",
            "research_scope": {"schema_version": "0.1", "scope_id": "scope-1", "description": "表面肌电关节角度估计", "mode": "exploratory",
                               "research_object": ["joint angle"], "input_modality": ["surface EMG"], "research_task": ["estimation"],
                               "method": [], "application": [], "constraints": {}, "unspecified": ["joint"]},
            "concept_groups": [{"group_id": "input", "label": "输入", "role": "input", "terms": ["surface EMG"]},
                               {"group_id": "object", "label": "对象", "role": "object", "terms": ["joint angle"]},
                               {"group_id": "task", "label": "任务", "role": "task", "terms": ["estimation"]}]}


def test_offline_replay_has_linked_evidence_and_no_new_network_calls(tmp_path):
    response = {"meta": {"count": 3}, "results": [{"id": "https://openalex.org/W123", "title": "Joint angle estimation from surface EMG",
                 "keywords": [{"display_name": "electromyography"}]}]}
    bundle = {"schema_version": "0.1", "snapshot_kind": "synthetic_test_fixture", "snapshots": [
        {"strategy": "exploratory", "retrieved_at": "2026-10-17T00:00:00+00:00", "response": response}]}
    result = run_package(case(), tmp_path / "package", snapshots=bundle)
    assert result["request_count"] == 0
    assert result["status"] == "replay_complete"
    runs = [json.loads(line) for line in (tmp_path / "package/05-search-runs.jsonl").read_text().splitlines()]
    assert runs[0]["mode"] == "replay"
    assert runs[0]["request_count"] == 0
    assert runs[0]["returned_count"] == 3
    keywords = json.loads((tmp_path / "package/02-keywords.json").read_text())
    evidence = [json.loads(line) for line in (tmp_path / "package/07-evidence.jsonl").read_text().splitlines()]
    assert any(k["evidence_status"] == "database_assigned" for k in keywords)
    assert all(k["relationship"] == "unclassified" for k in keywords if k["evidence_ids"])
    ids = {e["evidence_id"] for e in evidence}
    assert all(set(k["evidence_ids"]).issubset(ids) for k in keywords)
    assert all(e["paper_id"] == "https://openalex.org/W123" for e in evidence)
    assert (tmp_path / "package/08-cooccurrence.json").exists()
    assert (tmp_path / "package/manifest.json").exists()
    evaluation = json.loads((tmp_path / "package/06-evaluation.json").read_text())
    assert evaluation["scope"] == "engineering_and_exploratory_only"
    assert evaluation["strategies"][0]["metrics"]["precision_at_k"] is None


def test_plan_only_has_no_papers_and_is_not_claimed_executed(tmp_path):
    result = run_package(case(), tmp_path / "planned")
    assert result["status"] == "planned"
    assert result["executed_plan_count"] == 0
    assert result["request_count"] == 0


def test_existing_output_is_not_overwritten(tmp_path):
    output = tmp_path / "package"
    run_package(case(), output)
    with pytest.raises(FileExistsError):
        run_package(case(), output)


def test_invalid_input_rejected_before_creating_output(tmp_path):
    invalid = case()
    invalid["research_scope"]["description"] = ""
    with pytest.raises(ValueError):
        run_package(invalid, tmp_path / "bad")
    assert not (tmp_path / "bad").exists()


def test_scope_constraints_not_silently_ignored(tmp_path):
    invalid = case()
    invalid["research_scope"]["constraints"] = {"real_time": True}
    with pytest.raises(ValueError, match="unsupported"):
        run_package(invalid, tmp_path / "bad")


def test_malformed_replay_is_failed_not_successful_empty(tmp_path):
    snapshots = {"schema_version": "0.1", "snapshot_kind": "synthetic_test_fixture", "snapshots": [
        {"strategy": "exploratory", "retrieved_at": "2026-10-17T00:00:00+00:00", "response": {"error": "broken"}}]}
    result = run_package(case(), tmp_path / "bad-response", snapshots=snapshots)
    assert result["failed_plan_count"] == 1
    assert result["status"] == "failed"


def _response(*works, count=None):
    return {"meta": {"count": len(works) if count is None else count}, "results": list(works)}


def _work(paper_id, title, *, keywords=None):
    return {"id": paper_id, "title": title, "keywords": [{"display_name": item} for item in (keywords or [])]}


def test_replay_requires_plan_query_match_and_preserves_unknown_count(tmp_path):
    plans = None
    mismatched = {"schema_version": "0.1", "snapshot_kind": "synthetic_test_fixture", "snapshots": [
        {"strategy": "exploratory", "query": "wrong", "retrieved_at": "2026-10-17T00:00:00+00:00",
         "response": _response(_work("W1", "A"), count=None)}]}
    with pytest.raises(ValueError, match="query"):
        run_package(case(), tmp_path / "mismatch", snapshots=mismatched)


def test_replay_missing_strategy_is_not_executed_and_unknown_count_is_none(tmp_path):
    bundle = {"schema_version": "0.1", "snapshot_kind": "synthetic_test_fixture", "snapshots": [
        {"strategy": "exploratory", "retrieved_at": "2026-10-17T00:00:00+00:00",
         "response": {"meta": {}, "results": [_work("W1", "A")]}}]}
    result = run_package(case(), tmp_path / "unknown-count", snapshots=bundle)
    runs = [json.loads(line) for line in (tmp_path / "unknown-count/05-search-runs.jsonl").read_text().splitlines()]
    assert result["status"] == "replay_complete"
    assert runs[0]["returned_count"] is None
    assert any(run["status"] == "not_executed" for run in runs)


def test_multiple_runs_preserve_paper_provenance_and_partial_status(tmp_path):
    class Client:
        def __init__(self):
            self.calls = 0

        def search_works(self, search, *, per_page, filters):
            self.calls += 1
            if self.calls == 1:
                paper = Paper("W1", "A", database_keywords=["observed"])
                return OpenAlexSearchResult(status="success", papers=[paper], total_count=1,
                                             fetched_count=1, request_count=1, raw_response=_response(_work("W1", "A")),
                                             retrieved_at="2026-10-17T00:00:00+00:00")
            return OpenAlexSearchResult(status="failed", total_count=None, fetched_count=0, request_count=1,
                                         error_type="http_error", error_message="no", raw_response={"error": "no"},
                                         retrieved_at="2026-10-17T00:00:01+00:00")

    result = run_package(case(), tmp_path / "partial", client=Client())
    assert result["status"] == "partial"
    assert result["executed_plan_count"] == 2
    assert result["request_count"] == 2
    runs = [json.loads(line) for line in (tmp_path / "partial/05-search-runs.jsonl").read_text().splitlines()]
    papers = [json.loads(line) for line in (tmp_path / "partial/04-papers.jsonl").read_text().splitlines()]
    assert len(papers) == 1
    assert len(papers[0]["source_run_ids"]) == 1
    assert runs[0]["paper_ids"] == ["W1"]


def test_manifest_hashes_match_and_completed_manifest_excludes_itself(tmp_path):
    output = tmp_path / "hashes"
    run_package(case(), output)
    manifest = json.loads((output / "manifest.json").read_text())
    assert manifest["status"] == "completed"
    for relative, digest in manifest["files"].items():
        assert hashlib.sha256((output / relative).read_bytes()).hexdigest() == digest
    assert "manifest.json" not in manifest["files"]


def test_synthetic_replay_marks_evidence_unverified_and_does_not_claim_real_effect(tmp_path):
    plans = None
    bundle = {"schema_version": "0.1", "snapshot_kind": "synthetic_test_fixture", "snapshots": [
        {"strategy": "exploratory", "retrieved_at": "2026-10-17T00:00:00+00:00",
         "response": _response(_work("W1", "A", keywords=["database term"]))}]}
    run_package(case(), tmp_path / "synthetic", snapshots=bundle)
    evidence = [json.loads(line) for line in (tmp_path / "synthetic/07-evidence.jsonl").read_text().splitlines()]
    assert evidence
    assert all(item["evidence_level"] == "U" for item in evidence)


def test_concept_groups_are_emitted_as_unverified_candidates(tmp_path):
    run_package(case(), tmp_path / "candidates")
    keywords = json.loads((tmp_path / "candidates/02-keywords.json").read_text())
    assert any(item["source_type"] == "llm_candidate" and item["evidence_status"] == "unverified_candidate"
               and not item["evidence_ids"] for item in keywords)
