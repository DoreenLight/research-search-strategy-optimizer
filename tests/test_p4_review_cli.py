import json

from research_search.cli import main


def test_p4_review_cli_writes_offline_intake(tmp_path):
    manifest = {
        'schema_version': '0.1', 'k': 2, 'cases': [{
            'case_id': 'test-case', 'domain_kind': 'mature', 'split': 'test', 'reference_set': None,
            'human_judgments': {}, 'model_judgments': {}, 'runs': [{
                'baseline_id': 'A', 'status': 'success', 'mode': 'replay', 'paper_ids': ['p1'],
                'request_count': 0, 'fetched_count': 1, 'deduplicated_count': 1,
                'source_explanation': 'fixture'
            }]
        }]
    }
    manifest_path = tmp_path / 'benchmark.json'
    manifest_path.write_text(json.dumps(manifest))
    reviewer_a = tmp_path / 'a.jsonl'
    reviewer_b = tmp_path / 'b.jsonl'
    row = {'paper_id': 'p1', 'label': 'relevant', 'rationale': 'in scope', 'evidence_locator': 'abstract',
           'judged_at': '2026-10-18T00:00:00+00:00'}
    reviewer_a.write_text(json.dumps({'reviewer_id': 'a', **row}) + '\n')
    reviewer_b.write_text(json.dumps({'reviewer_id': 'b', **row}) + '\n')
    output = tmp_path / 'review'
    assert main(['p4-review', str(manifest_path), '--reference-ids', 'p1', '--reference-source', 'frozen fixture',
                  '--reviewers', str(reviewer_a), str(reviewer_b), '--test-case-id', 'test-case',
                  '--output', str(output)]) == 0
    result = json.loads((output / 'benchmark-manifest.json').read_text())
    assert result['cases'][0]['reference_set_independent'] is True
    assert result['cases'][0]['human_judgments'] == {'p1': 'relevant'}
