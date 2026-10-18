import pytest

from research_search.models import ConceptGroup
from research_search.query_builder import build_query, build_strategy_plans


def test_strategy_uses_roles_independently_of_input_order():
    groups = [ConceptGroup("method", "Method", ["Transformer"]),
              ConceptGroup("task", "Task", ["estimation"]),
              ConceptGroup("object", "Object", ["joint angle"]),
              ConceptGroup("input", "Input", ["sEMG"]),
              ConceptGroup("application", "Application", ["rehabilitation"])]
    plans = build_strategy_plans(groups)
    assert plans[0].group_ids == ["input", "object"]
    assert plans[1].group_ids == ["input", "object", "task"]
    assert plans[2].group_ids == ["input", "object", "task", "method"]
    assert "rehabilitation" not in plans[2].query
    assert plans[0].logic == {"op": "AND", "groups": ["input", "object"]}


@pytest.mark.parametrize("term", ['word\" OR anything', 'a\\b', 'term*', 'term\nelse', '(term)'])
def test_literal_terms_reject_embedded_query_operators(term):
    with pytest.raises(ValueError):
        build_query([ConceptGroup("input", "Input", [term])])


def test_empty_group_and_duplicate_role_rejected():
    with pytest.raises(ValueError):
        build_query([ConceptGroup("input", "Input", [])])
    with pytest.raises(ValueError):
        build_strategy_plans([ConceptGroup("input", "Input", ["sEMG"]),
                              ConceptGroup("other", "Other", ["EEG"], role="input")])


def test_two_component_topics_can_use_task_without_object():
    plans = build_strategy_plans([ConceptGroup("input", "Input", ["sEMG"]),
                                  ConceptGroup("task", "Task", ["angle estimation"])])
    assert plans[0].group_ids == ["input", "task"]
    assert plans[1].query == plans[0].query
