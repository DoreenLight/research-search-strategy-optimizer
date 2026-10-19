import copy
import json
from pathlib import Path

import pytest

from research_search.keyword_network_ops import adopt_edge, build_network_experiment_config
from research_search.workflow import run_package

ROOT = Path(__file__).resolve().parents[1]


def _case():
    value = json.loads((ROOT / 'evals/cases/semg-joint-angle.json').read_text())
    value['concept_groups'] = value['concept_groups'][:2]
    value['research_scope']['method'] = []
    return value


def _snapshots():
    return {'schema_version': '0.1', 'snapshot_kind': 'live_capture', 'snapshots': [
        {'strategy': 'exploratory', 'query': '("surface electromyography" OR "sEMG") AND ("joint angle")',
         'retrieved_at': '2026-10-18T00:00:00Z', 'response': {'meta': {'count': 2}, 'results': [
             {'id': 'https://openalex.org/W1', 'title': 'Surface EMG joint angle', 'keywords': [{'display_name': 'surface electromyography'}]},
             {'id': 'https://openalex.org/W2', 'title': 'sEMG joint angle', 'keywords': [{'display_name': 'sEMG'}]},
        ]}}
    ]}


def network(tmp_path):
    package = tmp_path / 'package'
    run_package(_case(), package, snapshots=_snapshots())
    output = tmp_path / 'network'
    from research_search.keyword_network import build_keyword_network
    build_keyword_network([package], output)
    return package, output


def test_adopt_edge_requires_two_reviewer_approved_consensus_and_candidate_edge(tmp_path):
    _package, network_dir = network(tmp_path)
    edge_id = json.loads((network_dir / 'edges.jsonl').read_text().splitlines()[0])['edge_id']
    pending = tmp_path / 'pending.jsonl'
    pending.write_text(json.dumps({'edge_id': edge_id, 'reviewer_id': 'a', 'label': 'approved', 'review_status': 'approved'}) + '\n')
    with pytest.raises(ValueError, match='two|consensus|candidate'):
        adopt_edge(_package / 'input-case.json', network_dir, pending, edge_id, tmp_path / 'case.json')


def test_network_experiment_rejects_group_addition_or_deletion_and_records_all_changed_groups(tmp_path):
    _package, _network_dir = network(tmp_path)
    base_case = json.loads((_package / 'input-case.json').read_text())
    candidate = copy.deepcopy(base_case)
    candidate['concept_groups'].append({'group_id': 'task', 'label': 'task', 'terms': ['estimation']})
    with pytest.raises(ValueError, match='one concept group|existing concept group'):
        build_network_experiment_config({'session_id': 'x', 'rounds': [{'case': base_case}]}, candidate,
                                        edge_id='edge', review_event_ids=['review'], output_path=tmp_path / 'bad.json')
