import copy
import json
from pathlib import Path

import pytest

from research_search.models import ConceptGroup
from research_search.optimization_session import run_optimization
from research_search.query_builder import build_strategy_plans

ROOT = Path(__file__).resolve().parents[1]


def case():
    return json.loads((ROOT / 'evals/cases/semg-joint-angle.json').read_text())


def replay(value, ids):
    groups = [ConceptGroup(g['group_id'], g['label'], g['terms'], g.get('role')) for g in value['concept_groups']]
    return {'schema_version': '0.1', 'snapshot_kind': 'live_capture', 'snapshots': [
        {'strategy': plan.strategy, 'query': plan.query, 'retrieved_at': '2026-10-18T00:00:00Z',
         'response': {'meta': {'count': len(ids)}, 'results': [
             {'id': 'https://openalex.org/' + pid, 'title': 'Surface EMG joint angle estimation'} for pid in ids]}}
        for plan in build_strategy_plans(groups) if plan.status != 'not_applicable']}


def config(*, candidate_ids=('W1', 'W2'), labels=None):
    base = case()
    candidate = copy.deepcopy(base)
    candidate['concept_groups'][0]['terms'].append('surface EMG')
    return {'session_id': 'quality', 'max_requests': 6, 'precision_k': 2, 'min_precision_at_k': 0.5,
        'rounds': [{'case': base, 'snapshots': replay(base, ['W1'])},
                   {'case': candidate, 'snapshots': replay(candidate, candidate_ids), 'reviewed_by': 'agent',
                    'rationale': 'Reviewed input variant', 'change_relationship': 'equivalent',
                    'judgments': [{'paper_id': 'https://openalex.org/' + pid, 'judge_type': 'human', 'label': label}
                                  for pid, label in (labels or {'W1': 'relevant', 'W2': 'relevant'}).items()]}]}


def test_version_pointers_and_audit_diff_follow_actual_active_parent(tmp_path):
    result = run_optimization(config(), tmp_path / 'session')
    history = json.loads((tmp_path / 'session/history.json').read_text())
    assert result['active_version'] == 1
    assert result['candidate_version'] is None
    assert result['rollback_version'] == 0
    assert history[1]['parent_version'] == 0
    assert history[1]['candidate_version'] == 1
    assert history[1]['changed_groups'] == ['input']
    assert history[1]['added_terms'] == {'input': ['surface EMG']}
    assert history[1]['removed_terms'] == {}
    assert history[1]['human_confirmed_relevant_ids'] == ['https://openalex.org/W2']
    assert history[1]['precision_gate']['passed'] is True


def test_no_positive_gain_never_retains_even_if_all_results_are_judged(tmp_path):
    cfg = config(candidate_ids=['W1'], labels={'W1': 'relevant'})
    cfg['precision_k'] = 1
    result = run_optimization(cfg, tmp_path / 'session')
    history = json.loads((tmp_path / 'session/history.json').read_text())
    assert result['active_version'] == 0
    assert history[1]['confirmed_gain'] == 0
    assert history[1]['decision'] == 'rollback_to_previous'


def test_drift_alarm_cannot_promote_positive_candidate(tmp_path):
    cfg = config()
    cfg['rounds'][1]['drift_rate'] = 0.9
    result = run_optimization(cfg, tmp_path / 'session')
    assert result['active_version'] == 0
    assert result['stop_reason'] == 'semantic_drift_alarm'
    history = json.loads((tmp_path / 'session/history.json').read_text())
    assert history[1]['decision'] == 'rollback_to_previous'


def test_partial_precision_labels_leave_candidate_pending(tmp_path):
    result = run_optimization(config(labels={'W2': 'relevant'}), tmp_path / 'session')
    assert result['active_version'] == 0
    assert result['candidate_version'] == 1
    assert result['status'] == 'pending_review'


def test_explicit_cost_budget_blocks_unknown_or_over_budget_retain(tmp_path):
    cfg = config()
    cfg['cost_budget_usd'] = 1.0
    cfg['rounds'][1]['estimated_cost_usd'] = 2.0
    result = run_optimization(cfg, tmp_path / 'over-budget')
    history = json.loads((tmp_path / 'over-budget/history.json').read_text())
    assert result['active_version'] == 0
    assert history[1]['decision'] == 'rollback_to_previous'
    assert history[1]['cost_gate']['passed'] is False

    cfg = config()
    cfg['cost_budget_usd'] = 1.0
    result = run_optimization(cfg, tmp_path / 'unknown-cost')
    history = json.loads((tmp_path / 'unknown-cost/history.json').read_text())
    assert result['active_version'] == 0
    assert history[1]['decision'] == 'pending_review'
    assert history[1]['cost_gate']['passed'] is False


def test_multiple_variable_groups_rejected_before_output(tmp_path):
    cfg = config()
    candidate = cfg['rounds'][1]['case']
    candidate['concept_groups'][1]['terms'].append('joint kinematics')
    cfg['rounds'][1]['snapshots'] = replay(candidate, ['W1', 'W2'])
    with pytest.raises(ValueError, match='one concept group'):
        run_optimization(cfg, tmp_path / 'session')
    assert not (tmp_path / 'session').exists()
