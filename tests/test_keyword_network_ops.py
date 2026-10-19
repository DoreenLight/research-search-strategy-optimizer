from __future__ import annotations

import json
from pathlib import Path

import pytest

from research_search.keyword_network import build_keyword_network
from research_search.keyword_network_ops import (
    adopt_edge,
    build_network_experiment_config,
    export_edge_review_workbench,
    score_keyword_frontier,
)
from research_search.workflow import run_package

ROOT = Path(__file__).resolve().parents[1]


def case():
    value = json.loads((ROOT / 'evals/cases/semg-joint-angle.json').read_text())
    value['concept_groups'] = value['concept_groups'][:2]
    value['research_scope']['method'] = []
    return value


def snapshots():
    return {'schema_version': '0.1', 'snapshot_kind': 'live_capture', 'snapshots': [
        {'strategy': 'exploratory', 'query': '("surface electromyography" OR "sEMG") AND ("joint angle")',
         'retrieved_at': '2026-10-18T00:00:00Z', 'response': {'meta': {'count': 2}, 'results': [
             {'id': 'https://openalex.org/W1', 'title': 'Surface EMG joint angle estimation',
              'keywords': [{'display_name': 'surface electromyography'}, {'display_name': 'joint angle'}]},
             {'id': 'https://openalex.org/W2', 'title': 'sEMG joint angle prediction',
              'keywords': [{'display_name': 'sEMG'}, {'display_name': 'joint angle'}]},
        ]}}
    ]}


def network(tmp_path):
    package = tmp_path / 'package'
    run_package(case(), package, snapshots=snapshots())
    output = tmp_path / 'network'
    build_keyword_network([package], output)
    return package, output


def test_frontier_scoring_is_bounded_and_deterministic(tmp_path):
    _package, network_dir = network(tmp_path)
    first = score_keyword_frontier(network_dir, tmp_path / 'frontier-a', limit=3)
    second = score_keyword_frontier(network_dir, tmp_path / 'frontier-b', limit=3)
    assert first['selection_limit'] == 3
    assert len(first['edges']) <= 3
    assert first['edges'] == second['edges']
    assert all(item['status'] == 'candidate' for item in first['edges'])
    assert all(item['adopted'] is False for item in first['edges'])
    assert all('priority_components' in item for item in first['edges'])


def test_edge_review_workbench_exports_blind_candidate_queue(tmp_path):
    _package, network_dir = network(tmp_path)
    frontier_dir = tmp_path / 'frontier'
    score_keyword_frontier(network_dir, frontier_dir, limit=2)
    output = tmp_path / 'edge-review'
    result = export_edge_review_workbench(network_dir, frontier_dir / 'candidate-frontier.json', output)
    assert result['edge_count'] == 2
    assert (output / 'index.html').is_file()
    assert (output / 'edge-review-queue.jsonl').is_file()
    assert (output / 'review-events.jsonl').read_text() == ''
    html = (output / 'index.html').read_text()
    assert 'approved' in html and 'pending_review' in html
    assert 'candidate-frontier' not in html
    assert (output / 'manifest.json').is_file()


def test_adopt_edge_requires_explicit_approved_review_and_writes_new_case(tmp_path):
    package, network_dir = network(tmp_path)
    frontier_dir = tmp_path / 'frontier'
    frontier = score_keyword_frontier(network_dir, frontier_dir, limit=1)
    edge = frontier['edges'][0]
    review = tmp_path / 'review-events.jsonl'
    review.write_text(json.dumps({
        'review_event_id': 'review-1', 'edge_id': edge['edge_id'], 'reviewer_id': 'reviewer-a',
        'label': 'approved', 'predicate': edge['predicate'], 'adopted_term': 'surface EMG',
        'group_id': 'input', 'rationale': 'Synthetic edge-review fixture', 'evidence_locator': 'title',
        'judged_at': '2026-10-19T00:00:00+00:00', 'review_status': 'approved',
    }) + '\n')
    output = tmp_path / 'adopted-case.json'
    result = adopt_edge(package / 'input-case.json', network_dir, review, edge['edge_id'], output)
    assert result['status'] == 'written'
    adopted = json.loads(output.read_text())
    assert 'surface EMG' in adopted['concept_groups'][0]['terms']
    adoption = json.loads((tmp_path / 'adopted-case.json.adoption.json').read_text())
    assert adoption['edge_id'] == edge['edge_id']
    assert adoption['synthetic_review'] is True


def test_adopt_edge_rejects_pending_or_unreviewed_edges(tmp_path):
    package, network_dir = network(tmp_path)
    frontier_dir = tmp_path / 'frontier'
    frontier = score_keyword_frontier(network_dir, frontier_dir, limit=1)
    review = tmp_path / 'pending.jsonl'
    review.write_text(json.dumps({'review_event_id': 'review-1', 'edge_id': frontier['edges'][0]['edge_id'],
                                  'label': 'pending_review'}) + '\n')
    with pytest.raises(ValueError, match='approved'):
        adopt_edge(package / 'input-case.json', network_dir, review, frontier['edges'][0]['edge_id'], tmp_path / 'case.json')


def test_network_experiment_config_declares_one_variable_group_and_provenance(tmp_path):
    base = {'session_id': 'p1', 'max_requests': 2, 'rounds': [{'case': case(), 'rationale': 'baseline'}]}
    candidate = json.loads(json.dumps(case()))
    candidate['concept_groups'][0]['terms'].append('surface EMG')
    output = tmp_path / 'experiment.json'
    result = build_network_experiment_config(base, candidate, edge_id='edge-1', review_event_ids=['review-1'], output_path=output)
    assert result['status'] == 'written'
    config = json.loads(output.read_text())
    assert len(config['rounds']) == 2
    assert config['rounds'][1]['keyword_network_edge_ids'] == ['edge-1']
    assert config['rounds'][1]['review_event_ids'] == ['review-1']
    assert config['rounds'][1]['change_relationship'] == 'unclassified'
