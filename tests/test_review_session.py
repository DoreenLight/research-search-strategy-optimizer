import json
from pathlib import Path

from research_search.optimization_session import run_optimization
from research_search.review_session import review_optimization_session

ROOT = Path(__file__).resolve().parents[1]


def case():
    value = json.loads((ROOT / 'evals/cases/semg-joint-angle.json').read_text())
    value['concept_groups'] = value['concept_groups'][:2]
    value['research_scope']['method'] = []
    return value


def bundle(ids):
    return {'schema_version': '0.1', 'snapshot_kind': 'live_capture', 'snapshots': [
        {'strategy': 'exploratory', 'query': '("surface electromyography" OR "sEMG") AND ("joint angle")',
         'retrieved_at': '2026-10-18T00:00:00Z', 'response': {'meta': {'count': len(ids)}, 'results': [
            {'id': f'https://openalex.org/{item}', 'title': 'Surface EMG joint angle estimation'} for item in ids]}}
    ]}


def test_offline_review_replay_preserves_judgments_and_creates_new_session(tmp_path):
    base = case()
    candidate = json.loads(json.dumps(base))
    candidate['concept_groups'][0]['terms'].append('surface EMG')
    config = {'session_id': 'source', 'max_requests': 0, 'precision_k': 1, 'min_precision_at_k': 0,
              'rounds': [{'case': base, 'snapshots': bundle(['W1']), 'rationale': 'base'},
                         {'case': candidate, 'snapshots': bundle(['W1', 'W2']), 'reviewed_by': 'agent',
                          'rationale': 'candidate', 'change_relationship': 'equivalent'}]}
    config['rounds'][1]['snapshots']['snapshots'][0]['query'] = '("surface electromyography" OR "sEMG" OR "surface EMG") AND ("joint angle")'
    source = tmp_path / 'source'
    run_optimization(config, source)
    judgments = tmp_path / 'judgments.jsonl'
    rows = [
        {'schema_version': '0.1', 'judgment_id': 'j1', 'paper_id': 'https://openalex.org/W1', 'scope_id': base['research_scope']['scope_id'],
         'label': 'relevant', 'judge_type': 'human', 'rationale': 'In scope', 'judged_at': '2026-10-18T00:00:00Z',
         'reviewer_id': 'reviewer-a', 'evidence_locator': 'abstract'},
        {'schema_version': '0.1', 'judgment_id': 'j2', 'paper_id': 'https://openalex.org/W2', 'scope_id': base['research_scope']['scope_id'],
         'label': 'relevant', 'judge_type': 'human', 'rationale': 'In scope', 'judged_at': '2026-10-18T00:00:00Z',
         'reviewer_id': 'reviewer-a', 'evidence_locator': 'title'},
    ]
    judgments.write_text(''.join(json.dumps(row) + '\n' for row in rows))
    output = tmp_path / 'reviewed'
    result = review_optimization_session(source, [judgments], output)
    assert result['request_count'] == 0
    assert result['active_version'] == 1
    imported = json.loads((output / 'review-import.json').read_text())
    assert len(imported['human_judgments']) == 2
    assert imported['new_network_requests'] == 0
    assert (source / 'history.json').read_bytes() != (output / 'history.json').read_bytes()
