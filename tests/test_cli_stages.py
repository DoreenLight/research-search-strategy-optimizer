import json
from pathlib import Path

from research_search.cli import main

ROOT = Path(__file__).resolve().parents[1]


def test_reading_and_acquisition_cli_work_with_explicit_metadata(tmp_path, capsys):
    source = tmp_path / 'papers.json'
    source.write_text(json.dumps([{'paper_id':'p1','title':'Safe Title'}]))
    assert main(['acquisition-handoff', str(source), '--output', str(tmp_path/'queue.json')]) == 0
    assert json.loads((tmp_path/'queue.json').read_text())['items'][0]['availability'] == 'metadata_only'
    assert main(['reading-export', str(source), '--output', str(tmp_path/'reading')]) == 0
    assert main(['validate-reading', str(tmp_path/'reading')]) == 0
    assert (tmp_path/'reading/index.md').is_file()


def test_benchmark_cli_does_not_create_fake_live_runs(tmp_path, capsys):
    input_path = tmp_path/'benchmark.json'
    input_path.write_text(json.dumps({'cases':[{'case_id':'one','domain_kind':'mature','split':'discovery',
                                               'reference_set':None,'human_judgments':{},'runs':[]}]}))
    assert main(['benchmark',str(input_path),'--output',str(tmp_path/'report')]) == 0
    report = json.loads((tmp_path/'report/benchmark.json').read_text())
    assert report['summary']['benchmark_new_request_count'] == 0
    assert report['summary']['real_advantage_demonstrated'] is False


def test_provider_cli_is_plan_only_without_live_flag(tmp_path, capsys):
    assert main(['provider-search','pubmed','surface EMG joint angle','--output',str(tmp_path/'pubmed.json')]) == 0
    report = json.loads((tmp_path/'pubmed.json').read_text())
    assert report['status'] == 'planned'
    assert report['request_count'] == 0


def test_provider_discovery_plan_preserves_seed(tmp_path, capsys):
    assert main(['provider-discover','citation','DOI:10.3390/s23125404','--output',str(tmp_path/'citation.json')]) == 0
    report=json.loads((tmp_path/'citation.json').read_text())
    assert report['status']=='planned'
    assert report['request_count']==0
    assert report['raw_response']['plan']['seed_ids']==['DOI:10.3390/s23125404']


def test_provider_output_exists_fails_without_requests(tmp_path):
    output=tmp_path/'existing.json'
    output.write_text('{}')
    assert main(['provider-search','pubmed','test','--live','--output',str(output)])==2
    assert output.read_text()=='{}'
