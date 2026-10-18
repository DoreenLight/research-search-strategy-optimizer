import json
from pathlib import Path

import pytest

from research_search.openalex_client import OpenAlexClient
from research_search.optimization_session import run_optimization

ROOT = Path(__file__).resolve().parents[1]


def base():
    return json.loads((ROOT/'evals/cases/semg-joint-angle.json').read_text())


def test_session_retries_cannot_exceed_shared_budget(tmp_path):
    calls = []
    class Response:
        status = 503
        headers = {}
        def read(self): return b'{"error":"unavailable"}'
        def close(self): pass
    def transport(request):
        calls.append(request.full_url)
        return Response()
    client = OpenAlexClient(api_key='', transport=transport, max_requests=10, max_retries=3,
                            min_request_interval=0, backoff_factor=0)
    summary = run_optimization({'session_id':'bounded','max_requests':1,'max_rounds':2,
        'rounds':[{'case':base(),'rationale':'baseline'}]}, tmp_path/'bounded', client=client)
    assert len(calls) == 1
    assert summary['request_count'] == 1
    assert summary['stop_reason'] == 'budget_exhausted'
    assert summary['active_version'] is None
    assert summary['status'] != 'complete'


def test_all_replay_no_client_request_even_when_session_client_present(tmp_path):
    calls = []
    def transport(request):
        calls.append(request.full_url)
        raise AssertionError('replay must not request')
    client = OpenAlexClient(api_key='', transport=transport, max_requests=2)
    case = base()
    snapshots = json.loads((ROOT/'tests/fixtures/semg-synthetic-snapshots.json').read_text())
    summary = run_optimization({'session_id':'replay','max_requests':2,'max_rounds':1,
        'rounds':[{'case':case,'rationale':'snapshot','snapshots':snapshots}]},tmp_path/'replay',client=client)
    assert not calls
    assert summary['request_count'] == 0
    assert summary['replayed_round_count'] == 1


def test_snapshot_input_mismatch_rejected_before_session_output(tmp_path):
    snapshots = json.loads((ROOT/'tests/fixtures/semg-synthetic-snapshots.json').read_text())
    snapshots['snapshots'][0]['query'] = 'not the case query'
    with pytest.raises(ValueError):
        run_optimization({'session_id':'bad','max_requests':2,'max_rounds':1,
            'rounds':[{'case':base(),'rationale':'bad snapshot','snapshots':snapshots}]},tmp_path/'bad')
    assert not (tmp_path/'bad').exists()


def test_separate_branch_is_tested_but_not_automatic_equivalent_adoption(tmp_path):
    case = base()
    expanded = json.loads(json.dumps(case))
    expanded['concept_groups'][1]['terms'].append('joint kinematics')
    snapshots = json.loads((ROOT/'tests/fixtures/semg-synthetic-snapshots.json').read_text())
    for snap in snapshots['snapshots']:
        snap.pop('query', None)
    summary = run_optimization({'session_id':'branch','max_requests':8,'max_rounds':2,'rounds':[
        {'case':case,'rationale':'base','snapshots':snapshots},
        {'case':expanded,'rationale':'explore broader','snapshots':snapshots,'reviewed_by':'agent',
         'change_relationship':'broader','separate_branch':True,
         'judgments':[{'paper_id':'https://openalex.org/W900000000001','judge_type':'human','label':'relevant'}]}]},tmp_path/'branch')
    history=json.loads((tmp_path/'branch/history.json').read_text())
    assert history[1]['decision'] in {'pending_review','branch_only'}
    assert history[1]['confirmed_gain'] is None
    assert summary['active_version'] == 0
