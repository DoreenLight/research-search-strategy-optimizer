from __future__ import annotations

import json
from pathlib import Path

import pytest

from research_search.keyword_network_ops import aggregate_edge_reviews


def frontier(path: Path) -> Path:
    payload = {
        'scope_id': 'scope-1',
        'edges': [
            {'edge_id': 'edge-1', 'predicate': 'cooccurs_with', 'subject': 'A', 'object': 'B',
             'evidence_ids': ['ev-1'], 'supporting_paper_ids': ['p1'], 'status': 'candidate'},
            {'edge_id': 'edge-2', 'predicate': 'cooccurs_with', 'subject': 'C', 'object': 'D',
             'evidence_ids': ['ev-2'], 'supporting_paper_ids': ['p2'], 'status': 'candidate'},
            {'edge_id': 'edge-3', 'predicate': 'cooccurs_with', 'subject': 'E', 'object': 'F',
             'evidence_ids': ['ev-3'], 'supporting_paper_ids': ['p3'], 'status': 'candidate'},
        ]
    }
    path.write_text(json.dumps(payload) + '\n')
    return path


def row(edge_id: str, reviewer: str, label: str) -> dict:
    return {'review_event_id': f'{reviewer}-{edge_id}', 'edge_id': edge_id,
            'reviewer_id': reviewer, 'label': label, 'predicate': 'cooccurs_with',
            'adopted_term': None, 'group_id': None, 'rationale': 'synthetic review fixture',
            'evidence_locator': 'observations', 'judged_at': '2026-10-19T01:00:00+00:00',
            'review_status': label, 'synthetic_review': True}


def write(path: Path, rows: list[dict]) -> Path:
    path.write_text(''.join(json.dumps(item) + '\n' for item in rows))
    return path


def test_dual_review_consensus_preserves_conflicts_and_missing(tmp_path):
    f = frontier(tmp_path / 'frontier.json')
    a = write(tmp_path / 'a.jsonl', [row('edge-1', 'a', 'approved'), row('edge-2', 'a', 'approved')])
    b = write(tmp_path / 'b.jsonl', [row('edge-1', 'b', 'approved'), row('edge-2', 'b', 'rejected')])
    result = aggregate_edge_reviews(f, [a, b], tmp_path / 'out')
    records = [json.loads(line) for line in (tmp_path / 'out/edge-consensus.jsonl').read_text().splitlines()]
    by_id = {item['edge_id']: item for item in records}
    assert by_id['edge-1']['consensus_label'] == 'approved'
    assert by_id['edge-1']['conflict'] is False
    assert by_id['edge-2']['consensus_label'] == 'pending_review'
    assert by_id['edge-2']['adjudication_status'] == 'pending_adjudication'
    assert by_id['edge-3']['judgments'][0] is None and by_id['edge-3']['judgments'][1] is None
    assert by_id['edge-3']['adjudication_status'] == 'missing_reviewer'
    assert result['summary']['approved_count'] == 1
    assert result['summary']['conflict_count'] == 1
    assert result['summary']['missing_count'] == 1
    assert result['summary']['synthetic_review'] is True


def test_adjudication_is_explicit_and_does_not_overwrite_raw_reviews(tmp_path):
    f = frontier(tmp_path / 'frontier.json')
    a = write(tmp_path / 'a.jsonl', [row('edge-1', 'a', 'approved'), row('edge-2', 'a', 'approved')])
    b = write(tmp_path / 'b.jsonl', [row('edge-1', 'b', 'rejected'), row('edge-2', 'b', 'approved')])
    adjudication = write(tmp_path / 'adjudication.jsonl', [{
        'adjudication_id': 'adj-1', 'edge_id': 'edge-1', 'adjudicator_id': 'arbiter-synthetic',
        'label': 'approved', 'rationale': 'synthetic arbitration fixture', 'evidence_locator': 'edge evidence',
        'judged_at': '2026-10-19T02:00:00+00:00', 'synthetic_review': True,
    }])
    result = aggregate_edge_reviews(f, [a, b], tmp_path / 'out', adjudication_path=adjudication)
    records = [json.loads(line) for line in (tmp_path / 'out/edge-consensus.jsonl').read_text().splitlines()]
    edge = next(item for item in records if item['edge_id'] == 'edge-1')
    assert [item['label'] for item in edge['judgments']] == ['approved', 'rejected']
    assert edge['consensus_label'] == 'approved'
    assert edge['adjudication_status'] == 'adjudicated'
    assert result['summary']['adjudicated_count'] == 1
    assert json.loads((tmp_path / 'out/manifest.json').read_text())['status'] == 'completed'


def test_review_input_rejects_duplicate_reviewer_or_unknown_edge_before_output(tmp_path):
    f = frontier(tmp_path / 'frontier.json')
    duplicate_reviewer = write(tmp_path / 'same.jsonl', [row('edge-1', 'same', 'approved')])
    with pytest.raises(ValueError, match='two distinct|reviewer'):
        aggregate_edge_reviews(f, [duplicate_reviewer, duplicate_reviewer], tmp_path / 'bad-1')
    unknown = write(tmp_path / 'unknown.jsonl', [row('unknown', 'b', 'approved')])
    with pytest.raises(ValueError, match='edge'):
        aggregate_edge_reviews(f, [duplicate_reviewer, unknown], tmp_path / 'bad-2')
    assert not (tmp_path / 'bad-1').exists()
    assert not (tmp_path / 'bad-2').exists()
