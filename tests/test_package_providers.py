import json
from pathlib import Path

import pytest

from research_search.workflow import run_package

ROOT = Path(__file__).resolve().parents[1]


def case():
    value = json.loads((ROOT / 'evals/cases/semg-joint-angle.json').read_text())
    value['concept_groups'] = value['concept_groups'][:2]
    value['research_scope']['method'] = []
    return value


def snapshots():
    return {'schema_version': '0.1', 'snapshot_kind': 'synthetic_test_fixture', 'snapshots': [
        {'strategy': 'exploratory', 'retrieved_at': '2026-10-18T00:00:00Z', 'response': {
            'meta': {'count': 1}, 'results': [{'id': 'https://openalex.org/W1', 'title': 'Surface EMG joint angle'}]}}
    ]}


def provider(provider, paper_id, title, *, doi, channel='keyword', discovery=False, request_count=1):
    return {
        'provider': provider, 'status': 'success', 'request_count': request_count,
        'reported_count': 10, 'fetched_count': 1, 'query_type': channel,
        'papers': [{'provider': provider, 'paper_id': paper_id, 'title': title, 'doi': doi,
                    'channel': channel, 'discovery_channel': discovery,
                    'seed_ids': ['seed'] if discovery else [],
                    'candidate_reason': channel if discovery else None,
                    'raw': {'api_key': 'must-not-be-exported'}}],
        'raw_response': {'Authorization': 'must-not-be-exported'}, 'query_hash': 'qhash',
    }


def test_run_package_ingests_p2_results_without_polluting_p0_papers(tmp_path):
    result = run_package(case(), tmp_path / 'package', snapshots=snapshots(), provider_results=[
        provider('pubmed', 'pmid-1', 'Joint angle', doi='10.1000/example'),
        provider('semantic_scholar', 's2-1', 'Joint angle', doi='10.1000/example', request_count=0),
    ])
    assert result['provider_historical_request_count'] == 1
    assert result['provider_new_network_request_count'] == 0
    assert result['provider_unique_count'] == 1
    assert json.loads((tmp_path / 'package/04-papers.jsonl').read_text().splitlines()[0])['paper_id'] == 'https://openalex.org/W1'
    provider_lines = [json.loads(line) for line in (tmp_path / 'package/11-provider-results.jsonl').read_text().splitlines()]
    assert len(provider_lines) == 2
    assert all(item['raw_response'] is None for item in provider_lines)
    assert 'api_key' not in (tmp_path / 'package/12-provider-fusion.json').read_text()
    assert (tmp_path / 'package/manifest.json').is_file()


def test_provider_result_validation_happens_before_package_creation(tmp_path):
    with pytest.raises(ValueError):
        run_package(case(), tmp_path / 'bad', snapshots=snapshots(), provider_results=[{'provider': 'pubmed'}])
    assert not (tmp_path / 'bad').exists()


def test_plan_only_can_ingest_p2_history_without_network(tmp_path):
    result = run_package(case(), tmp_path / 'planned', provider_results=[
        provider('pubmed', 'pmid-1', 'Joint angle', doi='10.1000/example', request_count=2)
    ])
    assert result['status'] == 'planned'
    assert result['provider_historical_request_count'] == 2
    assert result['provider_new_network_request_count'] == 0
