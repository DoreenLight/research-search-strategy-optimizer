import copy
import json
from pathlib import Path

import pytest

from research_search.optimization_session import run_optimization
from research_search.iteration_optimizer import should_stop

ROOT = Path(__file__).resolve().parents[1]


def case():
    value = json.loads((ROOT / 'evals/cases/semg-joint-angle.json').read_text())
    value['concept_groups'] = value['concept_groups'][:2]
    value['research_scope']['method'] = []
    return value


def snapshot(strategy, ids):
    return {'strategy': strategy, 'retrieved_at': '2026-10-18T00:00:00+00:00',
            'response': {'meta': {'count': len(ids)}, 'results': [
                {'id': f'https://openalex.org/{i}', 'title': 'Surface EMG joint angle estimation',
                 'keywords': [{'display_name': 'surface EMG'}]} for i in ids]}}


def bundle(ids):
    return {'schema_version': '0.1', 'snapshot_kind': 'synthetic_test_fixture',
            'snapshots': [snapshot('exploratory', ids), snapshot('focused', ids)]}


def test_unknown_gain_is_not_zero_or_automatic_retain(tmp_path):
    base = case()
    updated = copy.deepcopy(base)
    updated['concept_groups'][0]['terms'].append('surface EMG')
    config = {'session_id': 'trial', 'max_rounds': 3, 'max_requests': 5, 'branches_remaining': 0,
              'rounds': [{'case': base, 'rationale': 'baseline', 'snapshots': bundle(['W1'])},
                         {'case': updated, 'rationale': 'observed input variant', 'reviewed_by': 'agent',
                          'change_relationship': 'equivalent', 'evidence_paper_ids': ['https://openalex.org/W1'],
                          'snapshots': bundle(['W1', 'W2'])}]}
    result = run_optimization(config, tmp_path / 'loop')
    assert result['request_count'] == 0
    assert result['actual_round_count'] == 2
    history = json.loads((tmp_path / 'loop/history.json').read_text())
    assert history[1]['confirmed_gain'] is None
    assert history[1]['decision'] == 'pending_review'
    assert history[1]['comparison']['new_ids'] == ['https://openalex.org/W2']
    assert result['current_version'] == 1
    assert result['active_version'] == 0
    assert result['stop_reason'] == 'awaiting_human_judgments'


def test_unknown_round_evidence_does_not_trigger_low_gain_stop():
    result = should_stop([{'new_relevant_count': None, 'new_term_count': 0, 'drift_rate': None}] * 2,
                         budget_remaining=4, branches_remaining=0)
    assert result['stop'] is False
    assert result['reason'] == 'awaiting_human_judgments'


def test_reject_scope_drift_before_any_output(tmp_path):
    base = case()
    changed = copy.deepcopy(base)
    changed['research_scope']['constraints'] = {'language': 'en'}
    with pytest.raises(ValueError, match='scope'):
        run_optimization({'session_id': 'x', 'max_rounds': 2, 'max_requests': 2, 'branches_remaining': 0,
                          'rounds': [{'case': base, 'rationale': 'baseline'},
                                     {'case': changed, 'rationale': 'narrowing', 'reviewed_by': 'agent',
                                      'change_relationship': 'equivalent', 'evidence_paper_ids': ['p']}]}, tmp_path / 'bad')
    assert not (tmp_path / 'bad').exists()


def test_unreviewed_variant_not_executed_and_output_not_overwritten(tmp_path):
    base = case()
    changed = copy.deepcopy(base)
    changed['concept_groups'][0]['terms'].append('surface EMG')
    config = {'session_id': 'x', 'max_rounds': 2, 'max_requests': 2, 'branches_remaining': 0,
              'rounds': [{'case': base, 'rationale': 'baseline'}, {'case': changed, 'rationale': 'candidate'}]}
    with pytest.raises(ValueError, match='review'):
        run_optimization(config, tmp_path / 'bad')


def test_broader_term_requires_separate_branch(tmp_path):
    base = case()
    updated = copy.deepcopy(base)
    updated['concept_groups'][1]['terms'].append('joint kinematics')
    config = {'session_id': 'x', 'max_rounds': 2, 'max_requests': 2, 'branches_remaining': 0,
              'rounds': [{'case': base, 'rationale': 'baseline'},
                         {'case': updated, 'rationale': 'broader branch', 'reviewed_by': 'agent',
                          'change_relationship': 'broader', 'evidence_paper_ids': ['p']}]}
    with pytest.raises(ValueError, match='branch'):
        run_optimization(config, tmp_path / 'bad')
