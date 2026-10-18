import pytest
from research_search.search_evaluator import evaluate_retrieval, compare_retrieval


def test_partial_labels_are_not_treated_as_negatives():
    metrics = evaluate_retrieval(["a", "b"], {"b", "d"}, 2, 2, 2,
                                 relevance_labels={"b": "relevant"})
    assert metrics.precision_at_k is None
    assert metrics.judged_count == 1
    assert metrics.unjudged_count == 1
    assert metrics.judged_precision == 1.0
    assert metrics.recall_at_k == 0.5


def test_full_labels_allow_precision_and_k_larger_than_pool_is_explicit():
    metrics = evaluate_retrieval(["a", "b"], None, 2, 2, 50,
                                 relevance_labels={"a": "irrelevant", "b": "relevant"})
    assert metrics.precision_at_k is None
    assert metrics.precision_at_available == 0.5
    assert metrics.effective_k == 2
    assert metrics.recall_at_k is None


def test_duplicate_ids_do_not_inflate_rank_precision():
    metrics = evaluate_retrieval(["a", "a", "b"], {"a"}, 3, 2, 2,
                                 relevance_labels={"a": "relevant", "b": "irrelevant"})
    assert metrics.precision_at_k == 0.5
    assert metrics.relevant_found == 1


@pytest.mark.parametrize("fetched,dedup", [(-1, 0), (1, 2)])
def test_invalid_counts_rejected(fetched, dedup):
    with pytest.raises(ValueError):
        evaluate_retrieval(["a"], None, fetched, dedup, 1)


def test_unconfirmed_version_gain_not_reported_as_confirmed():
    result = compare_retrieval(["a"], ["a", "b", "c"], {"b": "relevant"})
    assert result["new_ids"] == ["b", "c"]
    assert result["new_relevant_ids"] == ["b"]
    assert result["unjudged_new_count"] == 1
