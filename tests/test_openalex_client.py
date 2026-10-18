import json
from urllib.parse import parse_qs, urlparse

import pytest

from research_search.openalex_client import OpenAlexClient


class FakeResponse:
    def __init__(self, payload=None, status=200, *, body=None, headers=None):
        self.status = status
        self.headers = headers or {}
        self._payload = json.dumps(payload).encode("utf-8") if body is None else body
        self.closed = False

    def read(self):
        return self._payload

    def close(self):
        self.closed = True


class FakeTransport:
    def __init__(self, *outcomes):
        self.outcomes = list(outcomes)
        self.requests = []
        self.timeouts = []

    def __call__(self, request, *, timeout=None):
        self.requests.append(request)
        self.timeouts.append(timeout)
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


def payload_for(*works, count=None):
    return {"meta": {"count": len(works) if count is None else count}, "results": list(works)}


def work_for(**overrides):
    return {"id": "https://openalex.org/W1", "title": "Joint angle estimation", **overrides}


def test_search_works_reconstructs_inverted_abstract_and_preserves_metadata():
    payload = payload_for(work_for(
        publication_year=2024,
        doi="https://doi.org/10.1000/example",
        ids={"pmid": "https://pubmed.ncbi.nlm.nih.gov/123/"},
        abstract_inverted_index={"Joint": [0], "angle": [1], "estimation": [2]},
        authorships=[{"author": {"display_name": "A. Researcher"}}],
        keywords=[{"display_name": "surface electromyography"}],
        primary_location={"source": {"display_name": "Example Journal"}},
    ))
    response = FakeResponse(payload)
    transport = FakeTransport(response)
    client = OpenAlexClient(request_fn=transport, max_retries=0, api_key="")

    result = client.search_works('"joint angle"', per_page=1)

    assert result.status == "success"
    assert result.total_count == 1
    assert result.fetched_count == 1
    assert result.papers[0].abstract == "Joint angle estimation"
    assert result.papers[0].doi == "https://doi.org/10.1000/example"
    assert result.papers[0].pmid == "123"
    assert result.papers[0].database_keywords == ["surface electromyography"]
    assert result.papers[0].author_keywords == []
    assert result.papers[0].authors == ["A. Researcher"]
    assert result.papers[0].source_title == "Example Journal"
    assert result.raw_response == payload
    assert result.raw_meta == {"count": 1}
    assert result.retrieved_at == result.papers[0].retrieved_at
    assert result.retrieved_at
    assert result.attempts == [{
        "request_url": result.request_url,
        "timestamp": result.attempts[0]["timestamp"],
        "status": 200,
        "error_type": None,
    }]
    assert result.warnings == []
    assert response.closed

    parsed = parse_qs(urlparse(transport.requests[0].full_url).query)
    assert parsed["search"] == ['"joint angle"']
    assert parsed["per-page"] == ["1"]


def test_search_works_returns_structured_failure_without_leaking_api_key():
    response = FakeResponse({"error": "bad key"}, status=403)
    transport = FakeTransport(response)
    test_credential = "fixture-" + "value"
    client = OpenAlexClient(request_fn=transport, max_retries=0, api_key=test_credential)

    result = client.search_works("test", per_page=1)

    assert result.status == "failed"
    assert result.error_type == "http_error"
    assert test_credential not in result.request_url
    assert test_credential not in result.error_message
    assert result.papers == []
    assert response.closed


@pytest.mark.parametrize("payload", [
    [],
    {},
    {"meta": {"count": True}, "results": []},
    {"meta": {"count": -1}, "results": []},
    {"meta": {"count": "1"}, "results": []},
    {"meta": {"count": 1}},
    {"meta": {"count": 1}, "results": {}},
    {"meta": {"count": 1}, "results": ["not-a-work"]},
])
def test_invalid_response_shape_is_not_a_success(payload):
    response = FakeResponse(payload)
    transport = FakeTransport(response)

    result = OpenAlexClient(request_fn=transport, max_retries=0, api_key="").search_works("test")

    assert result.status == "failed"
    assert result.error_type == "invalid_response"
    assert result.total_count is None
    assert result.papers == []
    assert result.request_count == 1
    assert result.attempts[0]["error_type"] == "invalid_response"
    assert response.closed


def test_missing_total_count_is_unknown_but_valid_results_are_successful():
    response = FakeResponse({"meta": {}, "results": [{"id": "https://openalex.org/W1", "title": "A"}]})
    result = OpenAlexClient(request_fn=FakeTransport(response), max_retries=0, api_key="").search_works("test")
    assert result.status == "success"
    assert result.total_count is None
    assert result.fetched_count == 1


@pytest.mark.parametrize("body", [b"not JSON", b"\xff", "not bytes"])
def test_invalid_json_utf8_or_body_type_is_structured_and_not_retried(body):
    response = FakeResponse(body=body)
    transport = FakeTransport(response)

    result = OpenAlexClient(request_fn=transport, max_retries=2, api_key="").search_works("test")

    assert result.status == "failed"
    assert result.error_type == "invalid_response"
    assert result.raw_response is None
    assert result.request_count == 1
    assert response.closed


def test_empty_page_with_known_zero_count_is_successful():
    result = OpenAlexClient(
        request_fn=FakeTransport(FakeResponse(payload_for())), api_key=""
    ).search_works("test", per_page=100, cursor="*")

    assert result.status == "success"
    assert result.total_count == 0
    assert result.fetched_count == 0
    assert result.raw_meta == {"count": 0}


def test_explicit_empty_api_key_disables_environment_authentication(monkeypatch):
    env_credential = "environment-" + "fixture"
    monkeypatch.setenv("OPENALEX_API_KEY", env_credential)
    anonymous = FakeTransport(FakeResponse(payload_for()))
    authenticated = FakeTransport(FakeResponse(payload_for()))
    OpenAlexClient(request_fn=anonymous, api_key="").search_works("test")
    OpenAlexClient(request_fn=authenticated).search_works("test")

    assert anonymous.requests[0].get_header("Authorization") is None
    assert authenticated.requests[0].get_header("Authorization") == "Bearer " + env_credential
    assert env_credential not in authenticated.requests[0].full_url


def test_parse_response_is_public_offline_and_uses_same_normalization():
    transport = FakeTransport()
    offline_credential = "offline-" + "fixture"
    client = OpenAlexClient(transport=transport, api_key=offline_credential)
    payload = payload_for(work_for())
    payload["request"] = {"Authorization": "Bearer " + offline_credential, "api_key": offline_credential}

    result = client.parse_response(payload, "2026-10-17T12:00:00+00:00")

    assert result.status == "success"
    assert result.request_count == 0
    assert result.request_url is None
    assert result.attempts == []
    assert result.retrieved_at == "2026-10-17T12:00:00+00:00"
    assert result.papers[0].retrieved_at == result.retrieved_at
    assert offline_credential not in json.dumps(result.raw_response)
    assert payload["request"]["api_key"] == offline_credential
    assert transport.requests == []


def test_module_parse_response_is_available_for_replay():
    from research_search.openalex_client import parse_response

    result = parse_response(payload_for(work_for()), "2026-10-17T12:00:00Z")

    assert result.status == "success"
    assert result.request_count == 0
    assert result.papers[0].paper_id == "https://openalex.org/W1"


class FakeClock:
    def __init__(self, value=1_700_000_000.0):
        self.value = value
        self.sleeps = []

    def __call__(self):
        return self.value

    def sleep(self, seconds):
        self.sleeps.append(seconds)
        self.value += seconds


def test_429_status_response_retries_after_seconds_and_closes_before_sleep():
    clock = FakeClock()
    limited = FakeResponse({"error": "too many requests"}, status=429, headers={"Retry-After": "2"})
    success = FakeResponse(payload_for(work_for()))
    transport = FakeTransport(limited, success)

    def sleep(seconds):
        assert limited.closed
        clock.sleep(seconds)

    result = OpenAlexClient(
        transport=transport, api_key="", clock=clock, sleep=sleep,
        max_retries=1, max_requests=2, min_request_interval=0,
    ).search_works("test")

    assert result.status == "success"
    assert result.request_count == 2
    assert [attempt["status"] for attempt in result.attempts] == [429, 200]
    assert clock.sleeps == [2.0]
    assert limited.closed and success.closed


def test_429_httperror_retries_after_http_date_with_wait_cap():
    from datetime import UTC, datetime
    from email.utils import format_datetime
    from io import BytesIO
    from urllib.error import HTTPError

    clock = FakeClock()
    body = BytesIO(b'{"error": "slow down"}')
    error = HTTPError("https://api.openalex.org/works", 429, "rate limited", {
        "Retry-After": format_datetime(datetime.fromtimestamp(clock.value + 120, UTC), usegmt=True),
    }, body)
    transport = FakeTransport(error, FakeResponse(payload_for()))

    result = OpenAlexClient(
        transport=transport, api_key="", clock=clock, sleep=clock.sleep,
        max_retries=1, max_wait=3, min_request_interval=0, wall_clock=clock,
    ).search_works("test")

    assert result.status == "success"
    assert result.request_count == 2
    assert clock.sleeps == [3.0]
    assert body.closed


def test_http_status_retry_does_not_depend_on_json_error_body():
    clock = FakeClock()
    limited = FakeResponse(status=429, body=b"not JSON", headers={"Retry-After": "0"})
    transport = FakeTransport(limited, FakeResponse(payload_for()))

    result = OpenAlexClient(
        transport=transport, api_key="", clock=clock, sleep=clock.sleep,
        max_retries=1, min_request_interval=0,
    ).search_works("test")

    assert result.status == "success"
    assert result.request_count == 2
    assert limited.closed


def test_request_budget_counts_retries_and_does_not_wait_after_exhaustion():
    clock = FakeClock()
    transport = FakeTransport(FakeResponse({}, status=503))

    result = OpenAlexClient(
        transport=transport, api_key="", clock=clock, sleep=clock.sleep,
        max_requests=1, max_retries=5, min_request_interval=0,
    ).search_works("test")

    assert result.status == "failed"
    assert result.error_type == "budget_exhausted"
    assert result.request_count == 1
    assert len(transport.requests) == 1
    assert clock.sleeps == []


def test_zero_request_budget_does_not_call_transport():
    transport = FakeTransport()

    result = OpenAlexClient(transport=transport, api_key="", max_requests=0).search_works("test")

    assert result.error_type == "budget_exhausted"
    assert result.request_count == 0
    assert result.attempts == []
    assert transport.requests == []


def test_request_budget_is_shared_across_calls_on_same_client():
    clock = FakeClock()
    transport = FakeTransport(FakeResponse(payload_for()))
    client = OpenAlexClient(transport=transport, api_key="", max_requests=1, clock=clock, sleep=clock.sleep)

    assert client.search_works("first").status == "success"
    result = client.search_works("second")

    assert result.error_type == "budget_exhausted"
    assert result.request_count == 0
    assert len(transport.requests) == 1


@pytest.mark.parametrize("status", [401, 403])
def test_authentication_errors_do_not_retry(status):
    response = FakeResponse({"error": "authentication failed"}, status=status)
    transport = FakeTransport(response)
    explicit_credential = "explicit-" + "fixture"
    result = OpenAlexClient(transport=transport, max_retries=5, api_key=explicit_credential).search_works("test")

    assert result.error_type == "http_error"
    assert result.request_count == 1
    assert result.attempts[0]["status"] == status
    assert response.closed


def test_total_timeout_caps_network_timeout_and_prevents_late_success():
    clock = FakeClock()
    response = FakeResponse(payload_for())
    seen_timeouts = []

    def transport(request, *, timeout):
        seen_timeouts.append(timeout)
        clock.value += 5
        return response

    result = OpenAlexClient(
        transport=transport, api_key="", timeout=20, total_timeout=2,
        clock=clock, sleep=clock.sleep, min_request_interval=0,
    ).search_works("test")

    assert seen_timeouts == [2.0]
    assert result.status == "failed"
    assert result.error_type == "timeout"
    assert result.request_count == 1
    assert response.closed


def test_timeout_error_is_structured_and_limited_by_retry_count():
    clock = FakeClock()
    transport = FakeTransport(TimeoutError("timed out"), TimeoutError("timed out"))
    result = OpenAlexClient(
        transport=transport, api_key="", max_retries=1, clock=clock,
        sleep=clock.sleep, min_request_interval=0, backoff_factor=0.5,
    ).search_works("test")

    assert result.error_type == "timeout"
    assert result.request_count == 2
    assert len(result.attempts) == 2
    assert clock.sleeps == [0.5]


def test_retry_after_larger_than_remaining_total_timeout_stops_without_another_request():
    clock = FakeClock()
    transport = FakeTransport(FakeResponse({}, status=429, headers={"Retry-After": "10"}))
    result = OpenAlexClient(
        transport=transport, api_key="", max_retries=5, total_timeout=2,
        clock=clock, sleep=clock.sleep, min_request_interval=0,
    ).search_works("test")

    assert result.error_type == "timeout"
    assert result.request_count == 1
    assert sum(clock.sleeps) <= 2


def test_client_rate_limits_requests_across_search_calls():
    clock = FakeClock()
    transport = FakeTransport(FakeResponse(payload_for()), FakeResponse(payload_for()))
    client = OpenAlexClient(
        transport=transport, api_key="", clock=clock, sleep=clock.sleep,
        min_request_interval=0.25,
    )

    client.search_works("first")
    client.search_works("second")

    assert clock.sleeps == [0.25]


@pytest.mark.parametrize("index, reason", [
    ({"one": [0], "three": [2]}, "gap"),
    ({"one": [0], "another": [0]}, "collision"),
    ({"one": [True]}, "invalid_offset"),
    ({"one": [-1]}, "invalid_offset"),
    ({"one": [10**12]}, "position_limit"),
    ({"one": "not-a-list"}, "invalid"),
])
def test_unsafe_abstracts_remain_none_with_warning_and_raw_index(index, reason):
    result = OpenAlexClient(
        transport=FakeTransport(FakeResponse(payload_for(work_for(abstract_inverted_index=index)))), api_key="",
    ).search_works("test")

    assert result.papers[0].abstract is None
    assert any(reason in warning for warning in result.warnings)
    assert result.raw_response["results"][0]["abstract_inverted_index"] == index


def test_abstract_token_and_byte_limits_are_enforced_without_truncating_raw():
    payload = payload_for(work_for(abstract_inverted_index={"word": [0, 1, 2]}))
    result = OpenAlexClient(api_key="", max_abstract_tokens=2).parse_response(payload, "now")
    assert result.papers[0].abstract is None
    assert any("too_large" in warning for warning in result.warnings)
    assert result.raw_response == payload

    result = OpenAlexClient(api_key="", max_abstract_bytes=5).parse_response(payload, "now")
    assert result.papers[0].abstract is None
    assert any("size_limit" in warning for warning in result.warnings)


def test_long_valid_abstract_and_raw_text_are_not_truncated():
    token = "longword" * 100
    payload = payload_for(work_for(abstract_inverted_index={token: [0]}))
    payload["raw_echo"] = "raw-value" * 100
    result = OpenAlexClient(api_key="").parse_response(payload, "now")

    assert len(result.papers[0].abstract) > 500
    assert result.papers[0].abstract == token
    assert len(result.raw_response["raw_echo"]) > 500
    assert result.raw_response["raw_echo"] == payload["raw_echo"]
    assert result.raw_response == payload


def test_default_request_interval_is_one_second():
    assert OpenAlexClient(api_key="").min_request_interval == 1.0


def test_missing_abstract_is_none_without_inferred_text():
    result = OpenAlexClient(api_key="").parse_response(payload_for(work_for()), "now")
    assert result.papers[0].abstract is None
    assert result.warnings == []


def test_works_missing_identifier_or_title_are_skipped_and_reported_partial():
    payload = payload_for(work_for(), {"title": "no ID", "doi": "fallback-forbidden"}, {"id": "W3"})
    result = OpenAlexClient(api_key="").parse_response(payload, "now")

    assert result.status == "partial"
    assert result.total_count == 3
    assert result.fetched_count == 1
    assert result.papers[0].paper_id == "https://openalex.org/W1"
    assert any("missing_id" in warning for warning in result.warnings)
    assert any("missing_title" in warning for warning in result.warnings)


def test_openalex_identifiers_are_canonical_and_invalid_ids_are_not_fabricated():
    result = OpenAlexClient(api_key="").parse_response(payload_for(
        work_for(id="http://openalex.org/w123/"),
        work_for(id="not-an-openalex-id"),
    ), "now")

    assert result.status == "partial"
    assert [paper.paper_id for paper in result.papers] == ["https://openalex.org/W123"]
    assert result.papers[0].openalex_id == "https://openalex.org/W123"


def test_filters_and_cursor_are_encoded_without_altering_the_search():
    transport = FakeTransport(FakeResponse(payload_for()))
    query = '("joint angle" OR "knee flexion") AND EMG'
    result = OpenAlexClient(transport=transport, api_key="").search_works(
        query, per_page=100, cursor="a+/=", filters={"publication_year": 2024, "is_oa": True},
    )
    params = parse_qs(urlparse(transport.requests[0].full_url).query)

    assert result.status == "success"
    assert params["search"] == [query]
    assert params["cursor"] == ["a+/="]
    assert params["filter"] == ["publication_year:2024,is_oa:true"]


def test_url_over_4094_bytes_is_rejected_before_transport_without_changing_query():
    transport = FakeTransport()
    query = "膝" * 1000
    result = OpenAlexClient(transport=transport, api_key="").search_works(query)

    assert result.status == "failed"
    assert result.error_type == "url_too_long"
    assert result.request_count == 0
    assert transport.requests == []
    assert parse_qs(urlparse(result.request_url).query)["search"] == [query]


def test_error_and_raw_reflections_redact_credentials_including_url_encoding():
    from dataclasses import asdict
    from urllib.parse import quote, quote_plus

    key = "private" + "/key+value with space"
    reflected_one = "other-" + "secret"
    reflected_two = "other-query-" + "secret"
    message = " ".join([key, quote(key, safe=""), quote_plus(key), "Bearer " + reflected_one, "api_key=" + reflected_two])
    payload = {"error": message, "request": {"Authorization": "Bearer " + key, "api_key": key}, key: key}
    transport = FakeTransport(FakeResponse(payload, status=401))
    result = OpenAlexClient(transport=transport, api_key=key).search_works("test")
    dumped = json.dumps(asdict(result))

    for value in (key, quote(key, safe=""), quote_plus(key), reflected_one, reflected_two):
        assert value not in dumped
    assert "Authorization" not in json.dumps(result.attempts)
    assert "headers" not in json.dumps(result.attempts)
    assert "body" not in json.dumps(result.attempts)


def test_invalid_nested_work_types_return_structured_failure():
    result = OpenAlexClient(api_key="").parse_response(payload_for(work_for(keywords=123)), "now")

    assert result.status == "failed"
    assert result.error_type == "invalid_response"
    assert result.raw_response["results"][0]["keywords"] == 123


@pytest.mark.parametrize("per_page", [0, 101, True, 1.5, "25"])
def test_invalid_per_page_is_rejected_before_request(per_page):
    transport = FakeTransport()
    with pytest.raises(ValueError):
        OpenAlexClient(transport=transport, api_key="").search_works("test", per_page=per_page)
    assert transport.requests == []
