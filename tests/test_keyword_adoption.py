import json
from pathlib import Path

from research_search.keyword_adoption import adopt_reviewed_keywords

ROOT = Path(__file__).resolve().parents[1]


def test_adoption_is_explicit_and_writes_a_new_case(tmp_path):
    case = json.loads((ROOT / 'evals/cases/semg-joint-angle.json').read_text())
    case_path = tmp_path / 'case.json'
    case_path.write_text(json.dumps(case))
    review_path = tmp_path / 'reviewed.json'
    review_path.write_text(json.dumps({'terms': [{
        'schema_version': '0.1', 'term_id': 'term-1', 'term': 'surface EMG', 'canonical_term': 'surface EMG',
        'category': 'unclassified', 'relationship': 'equivalent', 'source_type': 'paper_metadata',
        'evidence_status': 'reviewed', 'evidence_ids': ['e1'], 'retrieval_status': 'untested',
        'paper_ids': ['p1'], 'document_frequency': 1, 'adopted': True,
    }]}))
    output = tmp_path / 'new-case.json'
    result = adopt_reviewed_keywords(case_path, review_path, output, group_id='input')
    assert result['adopted_terms'] == ['surface EMG']
    assert 'surface EMG' in json.loads(output.read_text())['concept_groups'][0]['terms']
    assert 'surface EMG' not in json.loads(case_path.read_text())['concept_groups'][0]['terms']
