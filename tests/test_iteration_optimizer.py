from research_search.iteration_optimizer import (
    compare_strategy_versions,
    propose_iteration,
    should_stop,
)


def test_compare_versions_separates_new_ids_and_confirmed_relevant():
    result = compare_strategy_versions(
        baseline_ids=["a", "b"],
        candidate_ids=["b", "c", "d"],
        human_labels={"c": "relevant", "d": "uncertain"},
        model_labels={"d": "relevant"},
    )
    assert result["new_ids"] == ["c", "d"]
    assert result["new_relevant_ids"] == ["c"]
    assert result["new_unjudged_ids"] == ["d"]
    assert result["model_only_relevant_ids"] == ["d"]


def test_propose_iteration_marks_unverified_term_instead_of_auto_adopting():
    proposal = propose_iteration(
        current_terms={"surface electromyography", "joint angle"},
        discovered_terms=[
            {"term": "joint kinematics", "source_paper_ids": ["p1"], "relationship": "broader"},
            {"term": "joint angle", "source_paper_ids": ["p2"], "relationship": "equivalent"},
        ],
        budget_remaining=2,
    )
    assert proposal["candidates"][0]["term"] == "joint kinematics"
    assert proposal["candidates"][0]["status"] == "candidate"
    assert proposal["candidates"][0]["adopted"] is False
    assert proposal["candidates"][0]["action"] == "test_as_separate_query"
    assert proposal["skipped_existing_count"] == 1


def test_stop_after_two_low_gain_rounds_and_never_claims_complete_coverage():
    result = should_stop(
        rounds=[
            {"new_relevant_count": 0, "new_term_count": 0, "drift_rate": 0.0},
            {"new_relevant_count": 0, "new_term_count": 1, "drift_rate": 0.1},
        ],
        budget_remaining=5,
        branches_remaining=2,
    )
    assert result["stop"] is False
    result = should_stop(
        rounds=[
            {"new_relevant_count": 0, "new_term_count": 0, "drift_rate": 0.0},
            {"new_relevant_count": 0, "new_term_count": 0, "drift_rate": 0.0},
        ],
        budget_remaining=5,
        branches_remaining=0,
    )
    assert result["stop"] is True
    assert result["reason"] == "two_low_gain_rounds_and_no_unexplored_branches"
    assert result["coverage_claim"] == "not_proven_complete"


def test_budget_and_drift_stop_conditions_are_explicit():
    assert should_stop([], budget_remaining=0, branches_remaining=3)["reason"] == "budget_exhausted"
    assert should_stop([{"new_relevant_count": 5, "new_term_count": 3, "drift_rate": 0.8}], budget_remaining=3, branches_remaining=1)["reason"] == "semantic_drift_alarm"
