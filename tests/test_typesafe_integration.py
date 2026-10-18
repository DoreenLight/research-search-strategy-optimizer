import json
from pathlib import Path

from research_search.typesafe_full_loop import FullLoopConfig, judge_paper_candidates, prioritize_review_queue


def test_typesafe_judgments_can_be_attached_without_overwriting_human_labels(tmp_path):
    papers=[{'paper_id':'p1','title':'Direct','abstract':'Direct task','channel':'keyword'},
            {'paper_id':'p2','title':'Discovery','abstract':'Adjacent','channel':'semantic','seed_ids':['p1']}]
    def judge(state, **kwargs):
        return {'answers': {'direct_relevance': {'noul': 0.9 if state['paper']['paper_id']=='p1' else 0.4, 'confidence':0.8},
                            'scope_fit': {'noul': 0.8,'confidence':0.8}}, 'model':'jev-test'}
    result=judge_paper_candidates({'description':'query'},papers,config=FullLoopConfig(api_key='test'),judger=judge)
    records=[dict(p, jev_judgment=result['judgments'][i]) for i,p in enumerate(papers)]
    human_labels={'p1':'relevant'}
    assert human_labels['p1']=='relevant'
    assert all(record['jev_judgment']['human_label'] is None for record in records)
    queue=prioritize_review_queue(papers,result['judgments'])
    assert queue[0]['paper_id']=='p2'
