import json
from pathlib import Path

from research_search.keyword_network import build_keyword_network
from research_search.workflow import run_package


def case():
    value = json.loads((Path(__file__).resolve().parents[1] / 'evals/cases/semg-joint-angle.json').read_text())
    value['concept_groups'] = value['concept_groups'][:2]
    value['research_scope']['method'] = []
    return value


def snapshots():
    return {'schema_version': '0.1', 'snapshot_kind': 'live_capture', 'snapshots': [
        {'strategy': 'exploratory', 'query': '("surface electromyography" OR "sEMG") AND ("joint angle")',
         'retrieved_at': '2026-10-18T00:00:00Z', 'response': {
            'meta': {'count': 2}, 'results': [
                {'id': 'https://openalex.org/W1', 'title': 'Surface EMG joint angle estimation',
                 'abstract_inverted_index': {'Surface': [0], 'EMG': [1], 'joint': [2], 'angle': [3]},
                 'keywords': [{'display_name': 'surface electromyography'}, {'display_name': 'joint angle'}]},
                {'id': 'https://openalex.org/W2', 'title': 'sEMG joint angle prediction',
                 'keywords': [{'display_name': 'sEMG'}, {'display_name': 'joint angle'}]},
            ]}}
    ]}


def test_cooccurrence_evidence_contains_only_endpoint_observations(tmp_path):
    package = tmp_path / 'package'
    run_package(case(), package, snapshots=snapshots())
    output = tmp_path / 'network'
    build_keyword_network([package], output)
    observations = [json.loads(line) for line in (output / 'observations.jsonl').read_text().splitlines()]
    by_evidence = {}
    for item in observations:
        by_evidence.setdefault(item['evidence_id'], []).append(item)
    nodes = {item['node_id']: item for item in (json.loads(line) for line in (output / 'nodes.jsonl').read_text().splitlines())}
    for edge in (json.loads(line) for line in (output / 'edges.jsonl').read_text().splitlines()):
        if edge['predicate'] != 'cooccurs_with':
            continue
        endpoint_nodes = {edge['subject'], edge['object']}
        endpoint_terms = {nodes[node_id]['normalized_label'] for node_id in endpoint_nodes}
        assert all(any(item['normalized_term'] in endpoint_terms for item in by_evidence[evidence_id]) for evidence_id in edge['evidence_ids'])


def test_same_observation_semantics_have_stable_ids_across_package_runs(tmp_path):
    first_package = tmp_path / 'package-1'
    second_package = tmp_path / 'package-2'
    run_package(case(), first_package, snapshots=snapshots())
    run_package(case(), second_package, snapshots=snapshots())
    first = tmp_path / 'network-1'
    second = tmp_path / 'network-2'
    build_keyword_network([first_package], first)
    build_keyword_network([second_package], second)
    assert (first / 'observations.jsonl').read_bytes() == (second / 'observations.jsonl').read_bytes()
    assert (first / 'edges.jsonl').read_bytes() == (second / 'edges.jsonl').read_bytes()
