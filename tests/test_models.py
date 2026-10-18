from research_search.models import SearchRun


def test_search_run_serializes_execution_and_counts_separately():
    run = SearchRun(
        run_id="run-1",
        plan_id="plan-1",
        status="partial",
        returned_count=100,
        fetched_count=10,
        deduplicated_count=8,
        request_count=2,
        error_message="one page failed",
    )

    payload = run.to_dict()

    assert payload["returned_count"] == 100
    assert payload["fetched_count"] == 10
    assert payload["deduplicated_count"] == 8
    assert payload["status"] == "partial"
