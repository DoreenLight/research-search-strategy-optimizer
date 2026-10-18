import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from research_search.openalex_client import OpenAlexClient
from research_search.workflow import run_package

ROOT = Path(__file__).resolve().parents[1]


def test_scope_filters_reach_openalex_as_fields_not_nested_filter(tmp_path):
    case = json.loads((ROOT / 'evals/cases/semg-joint-angle.json').read_text())
    case['research_scope']['constraints'] = {'date_from': '2020-01-01', 'language': 'en'}
    captured = []
    class Response:
        status = 200
        def read(self):
            return b'{"meta":{"count":0},"results":[]}'
        def close(self):
            pass
    def transport(request):
        captured.append(parse_qs(urlparse(request.full_url).query))
        return Response()
    client = OpenAlexClient(api_key='', transport=transport, min_request_interval=0, max_requests=3)
    run_package(case, tmp_path / 'filtered', client=client, per_page=1)
    assert len(captured) == 3
    for params in captured:
        assert params['filter'] == ['from_publication_date:2020-01-01,language:en']
