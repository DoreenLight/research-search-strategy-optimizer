import json

import pytest

from research_search.p4_review import prepare_p4_review


def test_reviewer_text_is_redacted_in_audit_output(tmp_path):
    manifest = {'cases': [{'case_id': 'test', 'split': 'test', 'domain_kind': 'mature', 'reference_set': None,
                           'human_judgments': {}, 'model_judgments': {}, 'runs': [{'paper_ids': ['p1']}]}]}
    rows = []
    for reviewer in ['a', 'b']:
        path = tmp_path / f'{reviewer}.jsonl'
        path.write_text(json.dumps({'reviewer_id': reviewer, 'paper_id': 'p1', 'label': 'relevant',
                                    'rationale': 'api_key=fixture-value file=/Users/private',
                                    'evidence_locator': 'file:///Users/private/key',
                                    'judged_at': '2026-10-18T00:00:00+00:00'}) + '\n')
        rows.append(path)
    output = tmp_path / 'out'
    with pytest.raises(ValueError, match='credential-shaped|local path'):
        prepare_p4_review(manifest, ['p1'], 'frozen external source', rows, output, test_case_id='test')
    assert not output.exists()
