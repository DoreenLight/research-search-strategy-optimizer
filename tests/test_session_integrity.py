import copy
import hashlib
import json
from pathlib import Path

import pytest

from research_search.optimization_session import run_optimization
from research_search.query_builder import build_strategy_plans
from research_search.models import ConceptGroup

ROOT = Path(__file__).resolve().parents[1]


def base():
    return json.loads((ROOT / 'evals/cases/semg-joint-angle.json').read_text())


def snapshots(case, ids):
    groups = [ConceptGroup(g['group_id'], g['label'], g['terms'], g.get('role')) for g in case['concept_groups']]
    return {'schema_version': '0.1', 'snapshot_kind': 'live_capture', 'snapshots': [
        {'strategy': p.strategy, 'query': p.query, 'retrieved_at': '2026-10-18T00:00:00+00:00',
         'response': {'meta': {'count': len(ids)}, 'results': [
             {'id': f'https://openalex.org/W{pid[1:]}', 'title': 'Surface EMG joint angle estimation'} for pid in ids]}}
        for p in build_strategy_plans(groups) if p.status != 'not_applicable']}


def config():
    c = base()
    return {'session_id': 'integrity', 'max_rounds': 3, 'max_requests': 6, 'branches_remaining': 1,
            'rounds': [{'case': c, 'rationale': 'baseline', 'snapshots': snapshots(c, ['p1'])}]}


def test_manifest_covers_nested_manifests_not_only_payloads(tmp_path):
    cfg = config()
    run_optimization(cfg, tmp_path / 'session')
    manifest = json.loads((tmp_path / 'session/manifest.json').read_text())
    assert 'round-00/manifest.json' in manifest['files']
    assert hashlib.sha256((tmp_path / 'session/round-00/manifest.json').read_bytes()).hexdigest() == manifest['files']['round-00/manifest.json']


def test_method_scope_cannot_change_silently(tmp_path):
    cfg = config()
    changed = copy.deepcopy(cfg['rounds'][0]['case'])
    changed['research_scope']['method'] = ['unrequested method']
    cfg['rounds'].append({'case': changed, 'reviewed_by': 'agent', 'rationale': 'changed method',
                           'change_relationship': 'equivalent', 'snapshots': snapshots(changed, ['p1'])})
    with pytest.raises(ValueError, match='scope'):
        run_optimization(cfg, tmp_path / 'bad')
    assert not (tmp_path / 'bad').exists()


def test_drift_alarm_applied_before_later_rounds(tmp_path):
    cfg = config()
    candidate = copy.deepcopy(cfg['rounds'][0]['case'])
    candidate['concept_groups'][0]['terms'].append('surface EMG')
    cfg['rounds'].append({'case': candidate, 'reviewed_by': 'agent', 'rationale': 'test',
                         'change_relationship': 'equivalent', 'drift_rate': 0.9,
                         'snapshots': snapshots(candidate, ['p1', 'p2']),
                         'judgments': [{'paper_id': 'https://openalex.org/W2', 'label': 'irrelevant', 'judge_type': 'human'}]})
    cfg['rounds'].append(copy.deepcopy(cfg['rounds'][1]))
    summary = run_optimization(cfg, tmp_path / 'drift')
    assert summary['actual_round_count'] == 2
    assert summary['stop_reason'] == 'semantic_drift_alarm'
    assert summary['active_version'] == 0


def test_same_unjudged_results_do_not_create_confirmed_gain(tmp_path):
    cfg = config()
    cfg['rounds'].append({'case': copy.deepcopy(cfg['rounds'][0]['case']), 'reviewed_by': 'agent',
                         'rationale': 'repeat', 'change_relationship': 'equivalent',
                         'snapshots': snapshots(cfg['rounds'][0]['case'], ['p1'])})
    summary = run_optimization(cfg, tmp_path / 'repeat')
    assert summary['status'] == 'pending_review'
    assert summary['stop_reason'] == 'awaiting_human_judgments'


def test_unexpected_round_relationship_fails_before_output(tmp_path):
    cfg = config()
    cfg['rounds'].append({'case': copy.deepcopy(cfg['rounds'][0]['case']), 'reviewed_by': 'agent',
                         'rationale': 'bad', 'change_relationship': 'anything',
                         'snapshots': snapshots(cfg['rounds'][0]['case'], ['p1'])})
    with pytest.raises(ValueError, match='relationship'):
        run_optimization(cfg, tmp_path / 'bad')
    assert not (tmp_path / 'bad').exists()
