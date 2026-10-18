from research_search.search_evaluator import evaluate_retrieval


def test_evaluate_retrieval_separates_result_size_from_relevant_yield():
    metrics = evaluate_retrieval(
        returned_ids=["a", "b", "c"],
        known_relevant_ids={"b", "d"},
        fetched_count=2,
        deduplicated_count=2,
        k=2,
    )

    assert metrics.returned_count == 3
    assert metrics.fetched_count == 2
    assert metrics.deduplicated_count == 2
    assert metrics.relevant_found == 1
    assert metrics.recall_at_k == 0.5
    assert metrics.precision_at_k is None
    assert metrics.reference_hits_at_k == 1


def test_evaluate_retrieval_reports_unavailable_recall_without_reference_set():
    metrics = evaluate_retrieval(
        returned_ids=["a"],
        known_relevant_ids=None,
        fetched_count=1,
        deduplicated_count=1,
        k=1,
    )

    assert metrics.recall_at_k is None
    assert metrics.precision_at_k is None
    assert metrics.relevant_found is None
