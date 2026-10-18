import json

from research_search.providers.execution import execute_provider_plan


class Response:
    status = 200
    headers = {}

    def __init__(self, payload):
        self.payload = json.dumps(payload).encode()
        self.closed = False

    def read(self):
        return self.payload

    def close(self):
        self.closed = True


class Transport:
    def __init__(self, *responses):
        self.responses = list(responses)
        self.requests = []

    def __call__(self, request, *, timeout):
        self.requests.append(request)
        return self.responses.pop(0)


def test_live_pubmed_plan_uses_injected_transport_and_shared_budget():
    transport = Transport(
        Response({'esearchresult': {'count': '1', 'idlist': ['123']}}),
        Response('<PubmedArticleSet/>'),
    )
    plan = [{'provider': 'pubmed', 'query': 'surface EMG', 'filters': {}, 'limit': 1}]
    results = execute_provider_plan(plan, live=True, transports={'pubmed': transport}, max_requests=2)
    assert results[0]['request_count'] == 2
    assert results[0]['new_network_request_count'] == 2
    assert len(transport.requests) == 2


def test_planned_provider_plan_has_zero_new_requests():
    plan = [{'provider': 'pubmed', 'query': 'surface EMG', 'filters': {}, 'limit': 1}]
    results = execute_provider_plan(plan, live=False, max_requests=0)
    assert results[0]['status'] == 'planned'
    assert results[0]['request_count'] == 0
    assert results[0]['new_network_request_count'] == 0
