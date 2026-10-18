import json
from pathlib import Path

from research_search.cli import main

ROOT = Path(__file__).resolve().parents[1]


def case():
    value = json.loads((ROOT / 'evals/cases/semg-joint-angle.json').read_text())
    value['concept_groups'] = value['concept_groups'][:2]
    value['research_scope']['method'] = []
    return value


def test_provider_plan_is_offline_by_default_and_stored_in_package(tmp_path):
    case_path = tmp_path / 'case.json'
    case_path.write_text(json.dumps(case()))
    plan_path = tmp_path / 'plan.json'
    plan_path.write_text(json.dumps([{'provider': 'pubmed', 'query': 'surface EMG joint angle', 'filters': {}, 'limit': 1}]))
    output = tmp_path / 'package'
    assert main(['run', str(case_path), '--provider-plan', str(plan_path), '--output', str(output)]) == 0
    summary = json.loads((output / 'manifest.json').read_text())['summary']
    assert summary['provider_new_network_request_count'] == 0
    assert json.loads((output / '11-provider-results.jsonl').read_text().splitlines()[0])['status'] == 'planned'


def test_provider_plan_invalid_entry_fails_before_output(tmp_path):
    case_path = tmp_path / 'case.json'
    case_path.write_text(json.dumps(case()))
    plan_path = tmp_path / 'plan.json'
    plan_path.write_text(json.dumps([{'provider': 'unknown', 'query': 'x'}]))
    output = tmp_path / 'package'
    assert main(['run', str(case_path), '--provider-plan', str(plan_path), '--output', str(output)]) == 2
    assert not output.exists()
