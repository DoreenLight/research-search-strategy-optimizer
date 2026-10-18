import copy
import json
from pathlib import Path

import pytest

from research_search.openalex_client import OpenAlexClient
from research_search.optimization_session import run_optimization

ROOT = Path(__file__).resolve().parents[1]


def base_case():
    case = json.loads((ROOT / 'evals/cases/semg-joint-angle.json').read_text())
    case['concept_groups'] = case['concept_groups'][:2]
    case['research_scope']['method'] = []
    return case


def replay(ids):
    return {'schema_version': '0.1', 'snapshot_kind': 'live_capture', 'snapshots': [
        {'strategy': 'focused', 'query': '("surface electromyography" OR "sEMG") AND ("joint angle")',
         'retrieved_at': '2026-10-18T00:00:00+00:00',
         'response': {'meta': {'count': len(ids)}, 'results': [
             {'id': x, 'title': 'Joint angle estimation from surface EMG'} for x in ids]}}]}


def cfg():
    case = base_case()
    return {'session_id': 'test', 'max_rounds': 3, 'max_requests': 4, 'branches_remaining': 0,
            'rounds': [{'case': case, 'rationale': 'base', 'snapshots': replay(['https://openalex.org/W1'])}]}


def next_round(config, ids, labels):
    case = copy.deepcopy(config['rounds'][0]['case'])
    case['concept_groups'][0]['terms'].append('surface EMG')
    snap = replay(ids)
    snap['snapshots'][0]['query'] = '("surface electromyography" OR "sEMG" OR "surface EMG") AND ("joint angle")'
    return {'case': case, 'rationale': 'test witnessed variant', 'reviewed_by': 'agent', 'change_relationship': 'equivalent',
            'evidence_paper_ids': ['https://openalex.org/W1'], 'snapshots': snap,
            'judgments': [{'paper_id': p, 'judge_type': 'human', 'label': v} for p, v in labels.items()]}


def test_complete_human_positive_gain_retains_and_writes_active_case(tmp_path):
    config = cfg()
    config['rounds'].append(next_round(config, ['https://openalex.org/W1', 'https://openalex.org/W2'],
                                             {'https://openalex.org/W2': 'relevant'}))
    result = run_optimization(config, tmp_path / 'loop')
    assert result['active_version'] == 1
    history = json.loads((tmp_path / 'loop/history.json').read_text())
    assert history[1]['decision'] == 'retain'
    assert json.loads((tmp_path / 'loop/active-case.json').read_text())['concept_groups'][0]['terms'][-1] == 'surface EMG'


def test_partial_judgments_do_not_turn_unknown_gain_into_zero(tmp_path):
    config = cfg()
    config['rounds'].append(next_round(config, ['https://openalex.org/W1', 'https://openalex.org/W2', 'https://openalex.org/W3'],
                                             {'https://openalex.org/W2': 'irrelevant'}))
    result = run_optimization(config, tmp_path / 'loop')
    assert result['active_version'] == 0
    history = json.loads((tmp_path / 'loop/history.json').read_text())
    assert history[1]['confirmed_gain'] is None
    assert history[1]['decision'] == 'pending_review'


def test_conflicting_human_labels_become_uncertain_not_last_write_wins(tmp_path):
    config = cfg()
    candidate = next_round(config, ['https://openalex.org/W1', 'https://openalex.org/W2'], {'https://openalex.org/W2': 'relevant'})
    candidate['judgments'].append({'paper_id': 'https://openalex.org/W2', 'judge_type': 'human', 'label': 'irrelevant'})
    config['rounds'].append(candidate)
    result = run_optimization(config, tmp_path / 'loop')
    assert result['active_version'] == 0
    assert result['stop_reason'] == 'awaiting_human_judgments'


def test_losing_confirmed_relevant_paper_rolls_back(tmp_path):
    config = cfg()
    config['rounds'][0]['judgments'] = [{'paper_id': 'https://openalex.org/W1', 'judge_type': 'human', 'label': 'relevant'}]
    config['rounds'].append(next_round(config, ['https://openalex.org/W2'], {'https://openalex.org/W2': 'relevant'}))
    result = run_optimization(config, tmp_path / 'loop')
    history = json.loads((tmp_path / 'loop/history.json').read_text())
    assert history[1]['decision'] == 'rollback_to_previous'
    assert history[1]['lost_relevant_ids'] == ['https://openalex.org/W1']
    assert result['active_version'] == 0


def test_live_session_budget_blocks_next_network_attempt(tmp_path):
    config = cfg()
    config['max_requests'] = 1
    config['rounds'][0].pop('snapshots')
    candidate = next_round(config, [], {})
    candidate.pop('snapshots')
    config['rounds'].append(candidate)
    requests = []
    class Response:
        status = 200
        def read(self):
            return b'{"meta":{"count":0},"results":[]}'
        def close(self):
            pass
    def transport(request):
        requests.append(request.full_url)
        return Response()
    client = OpenAlexClient(api_key='', transport=transport, max_requests=8, min_request_interval=0)
    result = run_optimization(config, tmp_path / 'live', client=client)
    assert len(requests) == 1
    assert result['request_count'] == 1
    assert result['stop_reason'] == 'budget_exhausted'
    assert result['actual_round_count'] == 1


def test_plan_only_round_is_not_a_completed_experiment(tmp_path):
    config = cfg()
    config['rounds'][0].pop('snapshots')
    result = run_optimization(config, tmp_path / 'plan')
    assert result['executed_round_count'] == 0
    assert result['request_count'] == 0
    assert result['stop_reason'] == 'plan_only'


def test_malformed_later_round_rejected_before_baseline_writes(tmp_path):
    config = cfg()
    candidate = next_round(config, [], {})
    candidate['case']['research_scope']['description'] = ''
    config['rounds'].append(candidate)
    with pytest.raises(ValueError):
        run_optimization(config, tmp_path / 'bad')
    assert not (tmp_path / 'bad').exists()


def test_session_manifest_hashes_match(tmp_path):
    config = cfg()
    run_optimization(config, tmp_path / 'one')
    import hashlib
    manifest = json.loads((tmp_path / 'one/manifest.json').read_text())
    for rel, digest in manifest['files'].items():
        assert hashlib.sha256((tmp_path / 'one' / rel).read_bytes()).hexdigest() == digest


def test_omission_candidates_require_relevant_discovery_and_distinct_channel(tmp_path):
    from research_search.iteration_optimizer import analyze_omissions
    papers = [{'paper_id': 'p2', 'title': 'Novel muscle synergy angle prediction', 'channel': 'semantic', 'seed_ids': ['p1']}]
    result = analyze_omissions(['p1'], papers, human_labels={'p2': 'relevant'})
    assert result['missed_relevant_ids'] == ['p2']
    assert result['candidate_terms']
    assert all(x['status'] == 'candidate' and x['adopted'] is False for x in result['candidate_terms'])
    assert analyze_omissions(['p1'], papers, human_labels={})['missed_relevant_ids'] == []
