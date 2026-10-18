import copy
import json
from pathlib import Path

import pytest

from research_search.validation import validate_package
from research_search.workflow import run_package

ROOT = Path(__file__).resolve().parents[1]


def case():
    return json.loads((ROOT / 'evals/cases/semg-joint-angle.json').read_text())


def snapshot():
    return {'schema_version': '0.1', 'snapshot_kind': 'synthetic_test_fixture', 'snapshots': [
        {'strategy': 'exploratory', 'retrieved_at': '2026-10-18T00:00:00Z', 'response': {
            'meta': {'count': 1}, 'results': [{'id': 'W1', 'title': 'Surface EMG joint angle estimation 123',
                'abstract_inverted_index': {'Single': [0], 'abstract': [1], 'fragment': [2]},
                'keywords': [{'display_name': 'surface EMG'}]}]}}]}


def test_package_separates_all_observations_from_bounded_review_candidates(tmp_path):
    output = tmp_path / 'package'
    run_package(case(), output, snapshots=snapshot(), candidate_limit=5)
    raw = [json.loads(line) for line in (output / 'raw-observations.jsonl').read_text().splitlines()]
    candidates = json.loads((output / 'candidate-terms.json').read_text())
    assert any(item['term'] == '123' for item in raw)
    assert len(candidates['terms']) == 5
    assert len({item['term'] for item in candidates['terms']}) == 5
    assert not any(item['term'].isdigit() for item in candidates['terms'])
    assert not any(item['term'] == 'single abstract fragment' for item in candidates['terms'])
    assert all(not item['adopted'] and item['relationship'] == 'unclassified' for item in candidates['terms'])
    assert len(json.loads((output / '02-keywords.json').read_text())) == 5
    assert json.loads((output / 'reviewed-keywords.json').read_text())['terms'] == []
    assert validate_package(output)['papers'] == 1


def test_only_explicit_classified_evidence_supported_keyword_reviews_can_be_adopted(tmp_path):
    reviewed = copy.deepcopy(case())
    reviewed['keyword_reviews'] = [{'term': 'surface EMG', 'relationship': 'equivalent', 'review_status': 'approved',
        'reviewed_by': 'host-agent', 'reviewed_at': '2026-10-18T00:00:00Z', 'reason': 'Input modality variant witnessed in title.',
        'retrieval_status': 'untested', 'adopted': True}]
    run_package(reviewed, tmp_path / 'reviewed', snapshots=snapshot())
    terms = json.loads((tmp_path / 'reviewed/reviewed-keywords.json').read_text())['terms']
    assert len(terms) == 1
    assert terms[0]['term'] == 'surface emg'
    assert terms[0]['evidence_ids']
    assert terms[0]['reviewed_by'] == 'host-agent'
    assert terms[0]['adopted'] is True

    invalid = copy.deepcopy(reviewed)
    invalid['keyword_reviews'][0]['relationship'] = 'unclassified'
    with pytest.raises(ValueError):
        run_package(invalid, tmp_path / 'invalid', snapshots=snapshot())
    assert not (tmp_path / 'invalid').exists()
