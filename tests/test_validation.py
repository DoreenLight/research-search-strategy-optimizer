from pathlib import Path
import pytest
from research_search.validation import validate_record, validate_case
from research_search.models import Paper, SearchRun


def test_schema_rejects_missing_required_and_unknown_keys():
    with pytest.raises(ValueError):
        validate_record("keyword", {"term": "test"})
    with pytest.raises(ValueError):
        validate_record("paper", {**Paper("id", "Title").to_dict(), "api_key": "bad"})


def test_models_match_versioned_schema():
    validate_record("paper", Paper("id", "Title").to_dict())
    validate_record("search-run", SearchRun("run-1", "plan-1", "not_executed", mode="planned").to_dict())


def test_input_rejects_invented_constraint_before_network():
    with pytest.raises(ValueError):
        validate_case({"schema_version": "0.1", "case_id": "x", "research_scope": {"description": "test", "constraints": {"real_time": True}}, "concept_groups": []})
