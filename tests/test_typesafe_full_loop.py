from research_search.typesafe_full_loop import (
    FullLoopConfig,
    judge_term_candidates,
    judge_paper_candidates,
    prioritize_review_queue,
    recommend_version_action,
)


def terms():
    return [
        {'term':'surface electromyography','category':'input','source_type':'paper_metadata','paper_ids':['p1'],'relationship':'unclassified'},
        {'term':'joint kinematics','category':'object','source_type':'paper_metadata','paper_ids':['p2'],'relationship':'unclassified'},
    ]


def papers():
    return [
        {'paper_id':'p1','title':'Surface EMG joint angle estimation','abstract':'Estimate joint angle from surface electromyography.','channel':'keyword'},
        {'paper_id':'p2','title':'Muscle fatigue study','abstract':'Fatigue unrelated to angle.','channel':'semantic','seed_ids':['p1']},
    ]


def judge(state, **kwargs):
    if 'candidate_term' in state:
        term=state['candidate_term']['term']
        return {'answers': {
            'direct_fit': {'type':'noul','noul':0.9 if term=='surface electromyography' else 0.55,'confidence':0.8},
            'scope_drift': {'type':'noul','noul':0.1 if term=='surface electromyography' else 0.7,'confidence':0.7},
            'relationship': {'type':'choice','choice':'equivalent' if term=='surface electromyography' else 'broader','confidence':0.8},
        }, 'model':'jev-test', 'usage':{'input_tokens':10,'output_tokens':5}}
    pid=state['paper']['paper_id']
    return {'answers': {
        'direct_relevance': {'type':'noul','noul':0.9 if pid=='p1' else 0.2,'confidence':0.8},
        'scope_fit': {'type':'noul','noul':0.85 if pid=='p1' else 0.3,'confidence':0.8},
    }, 'model':'jev-test', 'usage':{'input_tokens':10,'output_tokens':5}}


def test_missing_key_plan_only_never_adopts_or_labels_human():
    config=FullLoopConfig(api_key='', max_terms=10, max_papers=10)
    result=judge_term_candidates({'description':'sEMG angle'}, terms(), config=config)
    assert result['status']=='not_executed'
    assert result['request_count']==0
    assert all(item['adopted'] is False for item in result['judgments'])
    result=judge_paper_candidates({'description':'sEMG angle'}, papers(), config=config)
    assert result['status']=='not_executed'
    assert result['human_relevance_claim'] is False


def test_jev_judges_terms_without_automatic_equivalence():
    result=judge_term_candidates({'description':'sEMG angle'}, terms(), config=FullLoopConfig(api_key='test'), judger=judge)
    assert result['status']=='success'
    assert result['request_count']==2
    first=result['judgments'][0]
    assert first['relationship']=='equivalent'
    assert first['adopted'] is False
    assert first['action']=='human_review'
    second=result['judgments'][1]
    assert second['relationship']=='broader'
    assert second['action']=='test_as_separate_query_or_review'


def test_jev_judges_papers_and_keeps_model_signal_separate():
    result=judge_paper_candidates({'description':'sEMG angle'}, papers(), config=FullLoopConfig(api_key='test'), judger=judge)
    assert result['status']=='success'
    assert result['human_relevance_claim'] is False
    assert result['judgments'][0]['direct_relevance']==0.9
    assert result['judgments'][1]['channel']=='semantic'
    assert result['judgments'][1]['action']=='human_review'


def test_review_priority_puts_uncertain_independent_discovery_first():
    paper_result=judge_paper_candidates({'description':'sEMG angle'}, papers(), config=FullLoopConfig(api_key='test'), judger=judge)
    queue=prioritize_review_queue(papers(), paper_result['judgments'])
    assert queue[0]['paper_id']=='p2'
    assert queue[0]['priority_reason'] in {'independent_discovery_low_model_score','independent_discovery_low_confidence'}


def test_version_recommendation_requires_human_gate():
    model=[{'paper_id':'p2','direct_relevance':0.9,'scope_fit':0.9,'confidence':0.8}]
    result=recommend_version_action(['p1'], ['p1','p2'], model, human_labels={})
    assert result['recommended_action']=='pending_review'
    assert result['active_version_change'] is False
    result=recommend_version_action(['p1'], ['p1','p2'], model, human_labels={'p2':'relevant'})
    assert result['recommended_action']=='retain_candidate'
    assert result['active_version_change'] is False
    assert result['human_gate']=='satisfied_for_review_not_automatic_truth'


def test_term_and_paper_limits_are_bounded():
    config=FullLoopConfig(api_key='', max_terms=1, max_papers=1)
    result=judge_term_candidates({}, terms(), config=config)
    assert result['candidate_count']==1
    assert result['skipped_count']==1
    result=judge_paper_candidates({}, papers(), config=config)
    assert result['candidate_count']==1
    assert result['skipped_count']==1
