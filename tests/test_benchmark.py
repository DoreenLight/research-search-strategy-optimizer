import hashlib
import json
from pathlib import Path

import pytest

from research_search.benchmark import run_benchmark


def _run(
    baseline_id="A",
    *,
    status="success",
    mode="live",
    paper_ids=None,
    request_count=1,
    fetched_count=None,
    deduplicated_count=None,
    reported_count=None,
    estimated_cost_usd=None,
    screening_minutes=None,
    source_explanation="offline test fixture",
    **extra,
):
    paper_ids = ["p1", "p2"] if paper_ids is None else paper_ids
    if fetched_count is None:
        fetched_count = len(set(paper_ids))
    if deduplicated_count is None:
        deduplicated_count = len(set(paper_ids))
    return {
        "baseline_id": baseline_id,
        "status": status,
        "mode": mode,
        "paper_ids": paper_ids,
        "request_count": request_count,
        "fetched_count": fetched_count,
        "deduplicated_count": deduplicated_count,
        "reported_count": reported_count,
        "estimated_cost_usd": estimated_cost_usd,
        "screening_minutes": screening_minutes,
        "source_explanation": source_explanation,
        **extra,
    }


def _case(
    case_id="case-1",
    *,
    domain_kind="mature",
    split="discovery",
    reference_set=None,
    human_judgments=None,
    model_judgments=None,
    runs=None,
    **extra,
):
    return {
        "case_id": case_id,
        "domain_kind": domain_kind,
        "split": split,
        "reference_set": reference_set,
        "human_judgments": {} if human_judgments is None else human_judgments,
        "model_judgments": {} if model_judgments is None else model_judgments,
        "runs": [_run()] if runs is None else runs,
        **extra,
    }


def _manifest(cases=None, **extra):
    return {"cases": [_case()] if cases is None else cases, **extra}


def _read_report(output_dir):
    return json.loads((output_dir / "benchmark.json").read_text(encoding="utf-8"))


def test_no_truth_keeps_recall_and_precision_null(tmp_path):
    output = tmp_path / "no-truth"
    result = run_benchmark(_manifest(), output)
    run = result["cases"][0]["runs"][0]
    assert run["recall_at_k"] is None
    assert run["precision_at_k"] is None
    assert run["known_relevant_hits_at_k"] is None
    assert run["human_labels_used"] is False


def test_human_and_model_judgments_are_separate(tmp_path):
    case = _case(
        human_judgments={},
        model_judgments={"p1": "relevant", "p2": "irrelevant"},
        runs=[_run(paper_ids=["p1", "p2"], fetched_count=2, deduplicated_count=2)],
    )
    result = run_benchmark(_manifest([case], k=2), tmp_path / "separate")
    run = result["cases"][0]["runs"][0]
    assert run["precision_at_k"] is None
    assert run["model_labels_present"] is True
    assert run["model_labels_used"] is False
    queue = (tmp_path / "separate/review-queue.jsonl").read_text(encoding="utf-8")
    assert '"human_label": null' in queue
    assert "model_label" not in queue
    assert "baseline_id" not in queue
    assert result["cases"][0]["model_judgments"]["p1"] == "relevant"


def test_split_leakage_is_rejected_before_output(tmp_path):
    manifest = _manifest(training_seed_ids=["p1"], test_reference_ids=["p1"])
    with pytest.raises(ValueError, match="leak|overlap|交叉"):
        run_benchmark(manifest, tmp_path / "leak")
    assert not (tmp_path / "leak").exists()


def test_planned_case_count_is_not_claimed_as_actual(tmp_path):
    result = run_benchmark(_manifest(planned_case_count=4), tmp_path / "planned")
    assert result["planned_case_count"] == 4
    assert result["actual_case_count"] == 1
    assert result["case_count_match"] is False


def test_failed_run_is_not_a_real_success_or_gain(tmp_path):
    failed = _run(
        baseline_id="A",
        status="failed",
        mode="live",
        paper_ids=["p1", "p2"],
        request_count=1,
        fetched_count=2,
        deduplicated_count=2,
    )
    result = run_benchmark(_manifest([_case(runs=[failed])]), tmp_path / "failed")
    run = result["cases"][0]["runs"][0]
    assert run["eligible_for_metrics"] is False
    assert run["total_unique_count"] is None
    assert result["summary"]["real_successful_run_count"] == 0


def test_unknown_cost_stays_null_even_with_confirmed_new_relevance(tmp_path):
    runs = [
        _run("A", paper_ids=["p1"], fetched_count=1, deduplicated_count=1),
        _run("B", paper_ids=["p1", "p2"], fetched_count=2, deduplicated_count=2,
             estimated_cost_usd=None),
    ]
    case = _case(
        human_judgments={"p1": "irrelevant", "p2": "relevant"},
        runs=runs,
    )
    result = run_benchmark(_manifest([case], k=2), tmp_path / "unknown-cost")
    candidate = result["cases"][0]["runs"][1]
    assert candidate["new_unique_count"] == 1
    assert candidate["confirmed_new_relevant_count"] == 1
    assert candidate["cost_per_incremental_confirmed_relevant_usd"] is None


def test_duplicate_ids_do_not_inflate_unique_yield(tmp_path):
    runs = [
        _run("A", paper_ids=["p1", "p1"], fetched_count=2, deduplicated_count=1),
        _run("B", paper_ids=["p1", "p2", "p2"], fetched_count=3, deduplicated_count=2),
    ]
    result = run_benchmark(_manifest([_case(runs=runs)]), tmp_path / "unique")
    first, second = result["cases"][0]["runs"]
    assert first["total_unique_count"] == 1
    assert second["total_unique_count"] == 2
    assert second["new_unique_count"] == 1


def test_partial_judgment_does_not_become_negative_precision(tmp_path):
    case = _case(
        human_judgments={"p1": "relevant"},
        runs=[_run(paper_ids=["p1", "p2"], fetched_count=2, deduplicated_count=2)],
    )
    result = run_benchmark(_manifest([case], k=2), tmp_path / "partial")
    run = result["cases"][0]["runs"][0]
    assert run["precision_at_k"] is None
    assert run["judged_count"] == 1
    assert run["unjudged_count"] == 1
    queue_lines = (tmp_path / "partial/review-queue.jsonl").read_text(encoding="utf-8").splitlines()
    assert len(queue_lines) == 1
    assert json.loads(queue_lines[0])["paper_id"] == "p2"


def test_synthetic_results_do_not_claim_real_advantage(tmp_path):
    synthetic = _run(mode="synthetic", request_count=0, paper_ids=["p1"])
    result = run_benchmark(_manifest([_case(runs=[synthetic])]), tmp_path / "synthetic")
    run = result["cases"][0]["runs"][0]
    assert run["eligible_for_metrics"] is True
    assert run["real_evidence"] is False
    assert run["real_advantage_eligible"] is False
    assert result["summary"]["real_successful_run_count"] == 0


def test_existing_catalog_is_not_counted_as_incremental_coverage(tmp_path):
    runs = [
        _run("A", paper_ids=["catalog-1"], fetched_count=1, deduplicated_count=1),
        _run("B", paper_ids=["catalog-1", "new-1"], fetched_count=2, deduplicated_count=2),
    ]
    case = _case(runs=runs, existing_catalog_ids=["catalog-1"])
    result = run_benchmark(_manifest([case]), tmp_path / "catalog")
    candidate = result["cases"][0]["runs"][1]
    assert candidate["existing_catalog_overlap_count"] == 1
    assert candidate["new_unique_count"] == 1
    assert candidate["new_unique_ids"] == ["new-1"]


def test_test_recall_uses_only_independent_reference_set(tmp_path):
    test_case = _case(
        split="test",
        reference_set=["p1", "p3"],
        reference_set_independent=True,
        reference_set_source="independently frozen manual reference fixture",
        runs=[_run(paper_ids=["p1", "p2"], fetched_count=2, deduplicated_count=2)],
    )
    discovery_case = _case(
        case_id="discovery-case",
        split="discovery",
        reference_set=["p5", "p6"],
        runs=[_run(paper_ids=["p1", "p2"], fetched_count=2, deduplicated_count=2)],
    )
    result = run_benchmark(_manifest([test_case, discovery_case], k=2), tmp_path / "recall")
    assert result["cases"][0]["runs"][0]["known_relevant_hits_at_k"] == 1
    assert result["cases"][0]["runs"][0]["recall_at_k"] == 0.5
    assert result["cases"][1]["runs"][0]["recall_at_k"] is None


def test_reported_count_is_not_used_as_unique_count(tmp_path):
    run = _run(
        paper_ids=["p1", "p2"],
        fetched_count=2,
        deduplicated_count=2,
        reported_count=1000,
    )
    result = run_benchmark(_manifest([_case(runs=[run])]), tmp_path / "reported")
    item = result["cases"][0]["runs"][0]
    assert item["reported_count"] == 1000
    assert item["total_unique_count"] == 2


def test_mode_statistics_keep_live_requests_separate(tmp_path):
    runs = [
        _run("A", mode="live", request_count=2, paper_ids=["p1"]),
        _run("B", mode="replay", request_count=0, paper_ids=["p2"]),
        _run("C", mode="synthetic", request_count=0, paper_ids=["p3"]),
    ]
    result = run_benchmark(_manifest([_case(runs=runs)]), tmp_path / "modes")
    stats = result["cases"][0]["mode_stats"]
    assert stats["live"]["request_count"] == 2
    assert stats["replay"]["request_count"] == 0
    assert stats["synthetic"]["request_count"] == 0
    assert result["summary"]["actual_live_request_count"] == 2


def test_hash_manifest_matches_emitted_files(tmp_path):
    output = tmp_path / "hash"
    run_benchmark(_manifest(), output)
    hashes = json.loads((output / "manifest.jsonsha256").read_text(encoding="utf-8"))
    for name, digest in hashes["files"].items():
        assert hashlib.sha256((output / name).read_bytes()).hexdigest() == digest
    assert "manifest.jsonsha256" not in hashes["files"]


def test_unsafe_source_path_is_rejected_without_writing(tmp_path):
    unsafe = _run(raw_path="../outside.json")
    with pytest.raises(ValueError, match="path|路径|unsafe"):
        run_benchmark(_manifest([_case(runs=[unsafe])]), tmp_path / "unsafe")
    assert not (tmp_path / "unsafe").exists()


def test_existing_output_file_is_not_overwritten(tmp_path):
    output = tmp_path / "already"
    output.mkdir()
    (output / "benchmark.json").write_text("keep", encoding="utf-8")
    with pytest.raises(FileExistsError):
        run_benchmark(_manifest(), output)
    assert (output / "benchmark.json").read_text(encoding="utf-8") == "keep"


def test_multiple_sources_use_id_union_not_reported_count_sum(tmp_path):
    runs = [
        _run("A", database="db-one", paper_ids=["p1", "p2"], reported_count=100,
             estimated_cost_usd=1, screening_minutes=3),
        _run("A", database="db-two", paper_ids=["p2", "p3"], reported_count=200,
             estimated_cost_usd=None, screening_minutes=None),
    ]
    result = run_benchmark(_manifest([_case(runs=runs)]), tmp_path / "multi-source")
    group = result["cases"][0]["runs"][0]
    assert group["source_record_count"] == 2
    assert group["total_unique_count"] == 3
    assert group["reported_count"] is None
    assert [row["reported_count"] for row in group["reported_counts_by_source"]] == [100, 200]
    assert group["estimated_cost_usd"] is None
    assert group["screening_minutes"] is None


def test_known_candidate_cost_per_incremental_human_positive(tmp_path):
    case = _case(
        human_judgments={"p1": "relevant", "p2": "relevant", "p3": "irrelevant"},
        runs=[
            _run("A", paper_ids=["p1"], estimated_cost_usd=2),
            _run("B", paper_ids=["p1", "p2", "p3"], estimated_cost_usd=6),
        ],
    )
    result = run_benchmark(_manifest([case], k=3), tmp_path / "cost")
    anchor, candidate = result["cases"][0]["runs"]
    assert candidate["precision_at_k"] == pytest.approx(2 / 3)
    assert candidate["confirmed_new_relevant_count"] == 1
    assert candidate["cost_per_incremental_confirmed_relevant_usd"] == 6
    assert anchor["cost_per_incremental_confirmed_relevant_usd"] is None


def test_only_reference_ids_are_not_treated_as_independent_or_human_truth(tmp_path):
    case = _case(split="test", reference_set=["p1", "p2"])
    result = run_benchmark(_manifest([case], k=2), tmp_path / "only-ids")
    run = result["cases"][0]["runs"][0]
    assert run["recall_at_k"] is None
    assert run["precision_at_k"] is None
    assert run["known_relevant_hits_at_k"] is None
    assert result["cases"][0]["reference_set_used_for_recall"] is False


def test_cross_case_discovery_reference_cannot_leak_into_test(tmp_path):
    cases = [
        _case("discovery", reference_set=["seed-1"]),
        _case("test", split="test", reference_set=["seed-1"]),
    ]
    with pytest.raises(ValueError, match="leak"):
        run_benchmark(_manifest(cases), tmp_path / "cross-leak")


def test_uncertain_and_off_pool_human_labels_do_not_create_zero_truth(tmp_path):
    case = _case(human_judgments={"p1": "uncertain", "outside": "relevant"})
    result = run_benchmark(_manifest([case], k=2), tmp_path / "uncertain")
    run = result["cases"][0]["runs"][0]
    assert run["known_relevant_hits_at_k"] is None
    assert run["metrics"]["relevant_found"] is None
    assert run["precision_at_k"] is None
    assert result["summary"]["pending_review_count"] == 2


def test_no_successful_same_mode_anchor_means_unknown_gain(tmp_path):
    case = _case(
        human_judgments={"p2": "relevant"},
        runs=[
            _run("A", mode="replay", request_count=0, paper_ids=["p1"]),
            _run("B", mode="live", paper_ids=["p2"], estimated_cost_usd=1),
        ],
    )
    result = run_benchmark(_manifest([case]), tmp_path / "no-anchor")
    candidate = result["cases"][0]["runs"][1]
    assert candidate["comparison_available"] is False
    assert candidate["new_unique_count"] is None
    assert candidate["cost_per_incremental_confirmed_relevant_usd"] is None
    assert candidate["real_advantage_eligible"] is False


def test_failed_source_invalidates_group_gain_but_keeps_live_request_audit(tmp_path):
    case = _case(runs=[
        _run("A", paper_ids=["p1"]),
        _run("B", database="good", paper_ids=["p2"]),
        _run("B", database="bad", status="failed", paper_ids=[], request_count=2),
    ])
    result = run_benchmark(_manifest([case]), tmp_path / "group-fail")
    candidate = result["cases"][0]["runs"][1]
    assert candidate["status"] == "partial"
    assert candidate["total_unique_count"] is None
    assert candidate["new_unique_count"] is None
    assert result["summary"]["actual_live_request_count"] == 4
    assert result["summary"]["mode_stats"]["live"]["failed_run_count"] == 1


def test_planned_and_not_executed_never_count_as_execution(tmp_path):
    case = _case(runs=[
        _run("A", status="planned", paper_ids=[], request_count=0),
        _run("B", status="not_executed", paper_ids=[], request_count=0),
    ])
    result = run_benchmark(_manifest([case], planned_run_count=10), tmp_path / "not-executed")
    assert result["planned_run_count"] == 10
    assert result["summary"]["actual_executed_run_count"] == 0
    assert result["summary"]["real_successful_run_count"] == 0
    assert all(run["total_unique_count"] is None for run in result["cases"][0]["runs"])


def test_case_with_no_runs_is_registered_not_executed(tmp_path):
    result = run_benchmark(_manifest([_case(runs=[])]), tmp_path / "no-runs")
    assert result["actual_case_count"] == 1
    assert result["summary"]["actual_executed_run_count"] == 0
    assert result["summary"]["actual_executed_case_count"] == 0
    assert "not_executed" in (tmp_path / "no-runs/benchmark.md").read_text(encoding="utf-8")


def test_unknown_new_relevance_is_not_zero(tmp_path):
    case = _case(
        runs=[_run("A", paper_ids=["p1"]), _run("B", paper_ids=["p1", "p2"])],
        model_judgments={"p2": "relevant"},
    )
    result = run_benchmark(_manifest([case]), tmp_path / "unknown-new")
    candidate = result["cases"][0]["runs"][1]
    assert candidate["new_unique_count"] == 1
    assert candidate["confirmed_new_relevant_count"] is None
    assert candidate["unjudged_new_count"] == 1
    assert candidate["real_advantage_eligible"] is False


def test_full_labels_but_fewer_than_k_does_not_claim_precision_at_k(tmp_path):
    case = _case(human_judgments={"p1": "relevant", "p2": "irrelevant"})
    result = run_benchmark(_manifest([case], k=3), tmp_path / "short-pool")
    run = result["cases"][0]["runs"][0]
    assert run["precision_at_k"] is None
    assert run["metrics"]["precision_at_available"] == 0.5
    assert run["metrics"]["effective_k"] == 2


def test_empty_output_directory_is_also_not_overwritten(tmp_path):
    output = tmp_path / "empty-existing"
    output.mkdir()
    with pytest.raises(FileExistsError):
        run_benchmark(_manifest(), output)
    assert list(output.iterdir()) == []


def test_output_symlink_parent_is_rejected(tmp_path):
    real_parent = tmp_path / "real"
    real_parent.mkdir()
    link = tmp_path / "link"
    link.symlink_to(real_parent, target_is_directory=True)
    with pytest.raises(ValueError, match="symlink"):
        run_benchmark(_manifest(), link / "report")
    assert not (real_parent / "report").exists()


def test_input_manifest_is_unchanged_and_hash_is_canonical(tmp_path):
    manifest = _manifest(k=2, benchmark_id="stable")
    before = json.dumps(manifest, sort_keys=True)
    result = run_benchmark(manifest, tmp_path / "stable-1")
    reordered = dict(reversed(list(manifest.items())))
    other = run_benchmark(reordered, tmp_path / "stable-2")
    assert json.dumps(manifest, sort_keys=True) == before
    assert result["input_manifest_sha256"] == other["input_manifest_sha256"]
    canonical = json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    assert result["input_manifest_sha256"] == hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def test_exact_output_inventory_and_chinese_report(tmp_path):
    output = tmp_path / "inventory"
    result = run_benchmark(_manifest(), output)
    assert {path.name for path in output.iterdir()} == {
        "benchmark.json", "benchmark.md", "review-queue.jsonl", "manifest.jsonsha256",
    }
    assert _read_report(output) == result
    text = (output / "benchmark.md").read_text(encoding="utf-8")
    assert "人工审阅" in text
    assert "未知" in text


@pytest.mark.parametrize("field,value", [
    ("request_count", True),
    ("request_count", None),
    ("request_count", -1),
    ("fetched_count", "2"),
    ("deduplicated_count", 99),
    ("reported_count", -1),
    ("estimated_cost_usd", float("nan")),
    ("estimated_cost_usd", float("inf")),
    ("estimated_cost_usd", True),
    ("screening_minutes", -1),
    ("status", "done"),
    ("baseline_id", "E"),
    ("source_explanation", ""),
    ("unexpected", 1),
])
def test_strict_run_validation_happens_before_writes(tmp_path, field, value):
    run = _run()
    run[field] = value
    output = tmp_path / "invalid"
    with pytest.raises(ValueError):
        run_benchmark(_manifest([_case(runs=[run])]), output)
    assert not output.exists()


@pytest.mark.parametrize("field,value", [
    ("k", True),
    ("k", 0),
    ("planned_case_count", -1),
    ("comparison_baseline_id", "other"),
    ("unexpected", 1),
])
def test_strict_manifest_validation_happens_before_writes(tmp_path, field, value):
    manifest = _manifest()
    manifest[field] = value
    with pytest.raises(ValueError):
        run_benchmark(manifest, tmp_path / "invalid-manifest")
    assert not (tmp_path / "invalid-manifest").exists()


@pytest.mark.parametrize("labels", [
    ["p1"], {"p1": True}, {"p1": "maybe"}, {"": "relevant"},
])
def test_invalid_human_judgments_do_not_become_truth(tmp_path, labels):
    with pytest.raises(ValueError):
        run_benchmark(_manifest([_case(human_judgments=labels)]), tmp_path / "invalid-label")


def test_offline_mode_cannot_claim_new_requests(tmp_path):
    with pytest.raises(ValueError, match="offline"):
        run_benchmark(_manifest([_case(runs=[_run(mode="synthetic", request_count=1)])]),
                      tmp_path / "offline-request")


def test_reference_independence_requires_source_and_no_human_conflict(tmp_path):
    case = _case(split="test", reference_set=["p1"], reference_set_independent=True)
    with pytest.raises(ValueError, match="source"):
        run_benchmark(_manifest([case]), tmp_path / "no-reference-source")
    case["reference_set_source"] = "independent frozen set"
    case["human_judgments"] = {"p1": "irrelevant"}
    with pytest.raises(ValueError, match="conflict"):
        run_benchmark(_manifest([case]), tmp_path / "conflict")


@pytest.mark.parametrize("field,value", [
    ("case_id", "../escape"),
    ("case_fixture", "/outside/case.json"),
    ("case_fixture", "C:\\outside\\case.json"),
])
def test_unsafe_case_paths_and_ids_are_rejected(tmp_path, field, value):
    case = _case()
    case[field] = value
    with pytest.raises(ValueError):
        run_benchmark(_manifest([case]), tmp_path / "bad-path")
    assert not (tmp_path / "bad-path").exists()


def test_existing_evaluation_helpers_are_used(tmp_path, monkeypatch):
    import research_search.benchmark as benchmark

    calls = {"evaluate": 0, "compare": 0}
    evaluate = benchmark.evaluate_retrieval
    compare = benchmark.compare_retrieval

    def wrapped_evaluate(*args, **kwargs):
        calls["evaluate"] += 1
        return evaluate(*args, **kwargs)

    def wrapped_compare(*args, **kwargs):
        calls["compare"] += 1
        return compare(*args, **kwargs)

    monkeypatch.setattr(benchmark, "evaluate_retrieval", wrapped_evaluate)
    monkeypatch.setattr(benchmark, "compare_retrieval", wrapped_compare)
    run_benchmark(_manifest(), tmp_path / "helpers")
    assert calls == {"evaluate": 1, "compare": 1}


def test_pending_is_unjudged_and_normalized_for_existing_evaluator(tmp_path):
    case = _case(human_judgments={"p1": "pending", "p2": "irrelevant"})
    result = run_benchmark(_manifest([case], k=2), tmp_path / "pending-label")
    run = result["cases"][0]["runs"][0]
    assert run["precision_at_k"] is None
    assert run["judged_count"] == 1
    assert run["unjudged_count"] == 1
    assert result["summary"]["pending_review_count"] == 1
    assert result["cases"][0]["human_judgments"]["p1"] == "pending"


def test_four_p4_case_fixtures_follow_existing_schema_and_have_no_truth():
    from research_search.validation import validate_case

    root = Path(__file__).resolve().parents[1]
    fixtures = sorted((root / "evals/cases").glob("p4-*.json"))
    assert len(fixtures) == 4
    for path in fixtures:
        case = json.loads(path.read_text(encoding="utf-8"))
        validate_case(case)
        assert case["independent_relevance_set"] is None
        assert case["judgments"] == []
        assert "人工真值未提供" in case["notes"]
