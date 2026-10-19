from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from research_search.keyword_network import build_keyword_network
from research_search.workflow import run_package

ROOT = Path(__file__).resolve().parents[1]


def case():
    value = json.loads((ROOT / 'evals/cases/semg-joint-angle.json').read_text())
    value['concept_groups'] = value['concept_groups'][:2]
    value['research_scope']['method'] = []
    return value


def snapshots():
    return {'schema_version': '0.1', 'snapshot_kind': 'live_capture', 'snapshots': [
        {'strategy': 'exploratory', 'query': '("surface electromyography" OR "sEMG") AND ("joint angle")', 'retrieved_at': '2026-10-18T00:00:00Z', 'response': {
            'meta': {'count': 2}, 'results': [
                {'id': 'https://openalex.org/W1', 'title': 'Surface EMG joint angle estimation',
                 'abstract_inverted_index': {'Surface': [0], 'EMG': [1], 'joint': [2], 'angle': [3]},
                 'keywords': [{'display_name': 'surface electromyography'}, {'display_name': 'joint angle'}]},
                {'id': 'https://openalex.org/W2', 'title': 'sEMG joint angle prediction',
                 'keywords': [{'display_name': 'sEMG'}, {'display_name': 'joint angle'}]},
            ]}}
    ]}


def test_build_keyword_network_is_read_only_stable_and_traceable(tmp_path):
    package = tmp_path / 'package'
    run_package(case(), package, snapshots=snapshots())
    output = tmp_path / 'network'

    first = build_keyword_network([package], output)

    assert first['network_schema_version'] == 'keyword-network-0.1'
    assert first['network']['observation_count'] > 0
    assert first['network']['node_count'] > 0
    assert first['network']['edge_count'] > 0
    assert first['network']['reviewed_edge_count'] == 0
    assert first['network']['approved_edge_count'] == 0
    assert {path.name for path in output.iterdir()} == {
        'network.json', 'nodes.jsonl', 'edges.jsonl', 'observations.jsonl',
        'candidate-frontier.json', 'review-events.jsonl', 'adoption-events.jsonl',
        'network-experiments.jsonl', 'source-index.jsonl', 'README.md', 'manifest.json'
    }
    observations = [json.loads(line) for line in (output / 'observations.jsonl').read_text().splitlines()]
    assert observations
    assert all(item['observation_id'].startswith('obs-') for item in observations)
    assert all(item['status'] == 'observed' for item in observations)
    assert all(item['evidence_ids'] for item in observations)
    assert all(item['source_level'] == 'A' for item in observations)
    edges = [json.loads(line) for line in (output / 'edges.jsonl').read_text().splitlines()]
    predicates = {item['predicate'] for item in edges}
    assert 'observed_in' in predicates
    assert 'database_assigned' in predicates
    assert 'cooccurs_with' in predicates
    assert all(item['status'] != 'approved' for item in edges)
    assert all(item['predicate'] != 'equivalent_to' for item in edges)
    assert len(edges) <= 50_000
    assert first['network']['cooccurrence_limits']['max_degree'] == 25
    assert hashlib.sha256((output / 'network.json').read_bytes()).hexdigest()

    second = tmp_path / 'network-second'
    build_keyword_network([package], second)
    for name in ('network.json', 'nodes.jsonl', 'edges.jsonl', 'observations.jsonl', 'source-index.jsonl'):
        assert (output / name).read_bytes() == (second / name).read_bytes()
    assert (package / 'manifest.json').is_file()


def test_network_rejects_existing_output_and_invalid_package_before_writing(tmp_path):
    package = tmp_path / 'package'
    run_package(case(), package, snapshots=snapshots())
    output = tmp_path / 'network'
    build_keyword_network([package], output)
    before = (output / 'network.json').read_bytes()
    with pytest.raises(FileExistsError):
        build_keyword_network([package], output)
    assert (output / 'network.json').read_bytes() == before

    invalid = tmp_path / 'invalid'
    invalid.mkdir()
    with pytest.raises(ValueError):
        build_keyword_network([invalid], tmp_path / 'bad')
    assert not (tmp_path / 'bad').exists()


def test_network_deduplicates_same_package_and_keeps_source_index_without_absolute_paths(tmp_path):
    package = tmp_path / 'package'
    run_package(case(), package, snapshots=snapshots())
    output = tmp_path / 'network'
    result = build_keyword_network([package, package], output)
    source_index = [json.loads(line) for line in (output / 'source-index.jsonl').read_text().splitlines()]
    assert result['network']['package_count'] == 1
    assert len(source_index) == 1
    serialized = output.joinpath('network.json').read_text()
    assert str(tmp_path) not in serialized
    assert all(item['package_manifest_sha256'] for item in source_index)
