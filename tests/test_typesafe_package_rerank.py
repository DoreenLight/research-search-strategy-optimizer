import json
from pathlib import Path

from research_search.typesafe_package import rerank_package_topk
from research_search.typesafe_reranker import RerankConfig


def package(tmp_path):
    root = tmp_path / 'package'
    root.mkdir()
    (root / '04-papers.jsonl').write_text(
        '\n'.join(json.dumps(item) for item in [
            {'paper_id': 'p1', 'title': 'Surface EMG joint angle', 'abstract': 'Angle estimation from EMG.'},
            {'paper_id': 'p2', 'title': 'Unrelated fatigue study', 'abstract': 'Fatigue only.'},
        ]) + '\n'
    )
    (root / '03-search-strategies.json').write_text(json.dumps([
        {'plan_id': 'plan-focused', 'strategy': 'focused', 'query': '"surface EMG" AND "joint angle"'}
    ]))
    return root


def test_package_rerank_plan_only_is_explicit_and_preserves_candidate_set(tmp_path):
    result = rerank_package_topk(
        package(tmp_path),
        strategy='focused',
        output_dir=tmp_path / 'rerank',
        config=RerankConfig(api_key=''),
    )
    assert result['status'] == 'not_executed'
    assert result['candidate_count'] == 2
    assert result['ordered_paper_ids'] == ['p1', 'p2']
    assert result['candidate_set_changed'] is False
    assert (tmp_path / 'rerank/rerank.json').is_file()
    assert (tmp_path / 'rerank/manifest.json').is_file()


def test_package_rerank_injected_judger_writes_ranked_order(tmp_path):
    def judge(state, **kwargs):
        return {'answers': {'relevance': {'type': 'noul', 'noul': 0.95 if state['paper']['paper_id'] == 'p2' else 0.1,
                                          'confidence': 0.9}}, 'model': 'jev-test'}
    result = rerank_package_topk(
        package(tmp_path),
        strategy='focused',
        output_dir=tmp_path / 'rerank',
        config=RerankConfig(api_key='test', top_k=2),
        judger=judge,
    )
    assert result['status'] == 'success'
    assert result['ordered_paper_ids'] == ['p2', 'p1']
    assert result['request_count'] == 2
    assert result['human_relevance_claim'] is False


def test_package_rerank_refuses_existing_output(tmp_path):
    output = tmp_path / 'rerank'
    output.mkdir()
    try:
        rerank_package_topk(package(tmp_path), strategy='focused', output_dir=output,
                            config=RerankConfig(api_key=''))
    except FileExistsError:
        pass
    else:
        raise AssertionError('existing output must not be overwritten')
