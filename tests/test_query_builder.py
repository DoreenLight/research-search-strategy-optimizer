from research_search.models import ConceptGroup
from research_search.query_builder import build_strategy_plans, build_query


def test_build_query_groups_terms_with_and_or():
    groups = [
        ConceptGroup(group_id="input", label="Input", terms=["surface EMG", "sEMG"]),
        ConceptGroup(group_id="task", label="Task", terms=["joint angle estimation"]),
    ]

    assert build_query(groups) == '("surface EMG" OR "sEMG") AND ("joint angle estimation")'


def test_build_strategy_plans_do_not_add_unspecified_method():
    groups = [
        ConceptGroup(group_id="input", label="Input", terms=["sEMG"]),
        ConceptGroup(group_id="object", label="Object", terms=["joint angle"]),
        ConceptGroup(group_id="task", label="Task", terms=["estimation"]),
    ]

    plans = build_strategy_plans(groups)

    assert [plan.strategy for plan in plans] == ["exploratory", "focused", "method_specific"]
    assert plans[0].group_ids == ["input", "object"]
    assert plans[1].group_ids == ["input", "object", "task"]
    assert plans[2].group_ids == ["input", "object", "task"]
    assert "method" not in plans[2].query.lower()
    assert plans[2].status == "not_applicable"
    assert plans[2].reason


def test_build_strategy_plans_adds_method_only_when_present():
    groups = [
        ConceptGroup(group_id="input", label="Input", terms=["sEMG"]),
        ConceptGroup(group_id="object", label="Object", terms=["joint angle"]),
        ConceptGroup(group_id="task", label="Task", terms=["estimation"]),
        ConceptGroup(group_id="method", label="Method", terms=["Transformer"]),
    ]

    plans = build_strategy_plans(groups)

    assert plans[-1].group_ids == ["input", "object", "task", "method"]
    assert '"Transformer"' in plans[-1].query
