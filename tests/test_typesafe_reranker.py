import os

from research_search.typesafe_reranker import (
    RerankConfig,
    rerank_papers,
    normalize_typesafe_answer,
)


def papers():
    return [
        {'paper_id':'p1','title':'Surface EMG joint angle estimation','abstract':'Estimate joint angle from surface electromyography.'},
        {'paper_id':'p2','title':'Unrelated muscle fatigue study','abstract':'Muscle fatigue unrelated to angle estimation.'},
    ]


def test_missing_key_safe_degradation_preserves_original_order():
    result = rerank_papers('predict joint angle from surface EMG', papers(), config=RerankConfig(api_key=''))
    assert result['status'] == 'not_executed'
    assert result['ordered_paper_ids'] == ['p1','p2']
    assert result['model'] == 'jev-latest'
    assert result['human_relevance_claim'] is False


def test_injected_judger_reranks_and_keeps_raw_typed_scores():
    def judge(state, **kwargs):
        return {'answers': {'relevance': {'type':'noul','noul': 0.9 if state['paper']['paper_id']=='p2' else 0.2,
                                          'confidence': 0.8}}, 'model':'jev-test', 'usage': {'input_tokens': 10, 'output_tokens': 2}}
    result = rerank_papers('query', papers(), config=RerankConfig(api_key='test'), judger=judge)
    assert result['status'] == 'success'
    assert result['ordered_paper_ids'] == ['p2','p1']
    assert result['scores'][0]['noul'] == 0.9
    assert result['scores'][0]['confidence'] == 0.8
    assert result['human_relevance_claim'] is False
    assert result['request_count'] == 2


def test_invalid_answer_is_recorded_without_reordering():
    def judge(state, **kwargs):
        return {'answers': {}, 'model':'jev-test'}
    result = rerank_papers('query', papers(), config=RerankConfig(api_key='test'), judger=judge)
    assert result['status'] == 'partial'
    assert result['ordered_paper_ids'] == ['p1','p2']
    assert result['scores'][0]['error_type'] == 'invalid_answer'


def test_normalize_typesafe_answer_accepts_score_or_noul_only():
    assert normalize_typesafe_answer({'answers': {'relevance': {'noul': 0.5}}})['score'] == 0.5
    assert normalize_typesafe_answer({'answers': {'relevance': {'score': 2, 'probabilities': {'0':0.2,'1':0.8}}}})['score'] == 0.8
