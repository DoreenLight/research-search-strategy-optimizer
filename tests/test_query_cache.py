from dataclasses import asdict, replace
import hashlib
import json
from pathlib import Path
import stat
from urllib.parse import quote, quote_plus

import pytest

from research_search.openalex_client import OpenAlexClient
from research_search.query_cache import CacheRequest, QueryCache


class Response:
    headers = {}

    def __init__(self, payload, status=200):
        self.status = status
        self.payload = json.dumps(payload).encode("utf-8")
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
        response = self.responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return response


def payload():
    return {
        "meta": {"count": 1},
        "results": [{"id": "https://openalex.org/W1", "title": "Joint angle estimation"}],
    }


def client_for(transport, cache_dir=None, **kwargs):
    return OpenAlexClient(transport=transport, api_key="", max_retries=0,
                          min_request_interval=0, cache_dir=cache_dir, **kwargs)


def stored_entry(cache_dir):
    entries = list(cache_dir.glob("*.json"))
    assert len(entries) == 1
    return entries[0]


def response_digest(response):
    serialized = json.dumps(response, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def populate(cache_dir):
    result = client_for(Transport(Response(payload())), cache_dir).search_works("joint angle", per_page=1)
    assert result.status == "success"
    return stored_entry(cache_dir), result


def test_cache_is_opt_in_and_uncached_calls_keep_using_transport(tmp_path):
    transport = Transport(Response(payload()), Response(payload()))
    client = client_for(transport)
    first = client.search_works("joint angle", per_page=1)
    second = client.search_works("joint angle", per_page=1)

    assert first.status == second.status == "success"
    assert first.request_count == second.request_count == 1
    assert not first.cache_hit and not second.cache_hit
    assert first.cache_key is second.cache_key is None
    assert first.warnings == second.warnings == []
    assert len(transport.requests) == 2
    assert list(tmp_path.iterdir()) == []


def test_cache_hit_replays_redacted_response_without_network_or_budget_use(tmp_path):
    transport = Transport(Response(payload()))
    cache_dir = tmp_path / "cache"
    first = client_for(transport, cache_dir, max_requests=1)
    first_result = first.search_works("joint angle", per_page=1, filters={"language": "en"})
    assert first_result.status == "success"
    assert first_result.request_count == 1
    assert first_result.metadata_bytes == len(json.dumps(payload()).encode("utf-8"))
    assert first_result.cache_key == stored_entry(cache_dir).stem
    assert not first_result.cache_hit

    second = client_for(transport, cache_dir, max_requests=0,
                        sleep=lambda _: pytest.fail("cache hits must not sleep"))
    second_result = second.search_works("joint angle", per_page=1, filters={"language": "en"})
    same_client_hit = first.search_works("joint angle", per_page=1, filters={"language": "en"})
    for hit in (second_result, same_client_hit):
        assert hit.status == "success"
        assert hit.cache_hit
        assert hit.cache_key == first_result.cache_key
        assert hit.metadata_bytes == 0
        assert hit.request_count == 0 and hit.attempts == []
        assert hit.retrieved_at == first_result.retrieved_at
        assert hit.papers[0].paper_id == "https://openalex.org/W1"
        assert hit.warnings == ["cache_hit"]
    assert len(transport.requests) == 1


def test_cache_key_normalizes_filter_order_bool_null_and_wire_scalar_values(tmp_path):
    transport = Transport(Response(payload()), Response(payload()))
    client = client_for(transport, tmp_path / "cache", max_requests=5)
    first = client.search_works("joint angle", per_page=1, cursor="*", filters={
        "language": "en", "is_oa": True, "publication_year": 2024, "ignored": None,
    })
    second = client.search_works("joint angle", per_page=1, cursor="*", filters={
        "publication_year": "2024", "is_oa": "true", "language": "en",
    })
    third = client.search_works("joint angle", per_page=1, cursor="next", filters={
        "language": "en", "is_oa": "true", "publication_year": "2024",
    })

    assert first.cache_key == second.cache_key != third.cache_key
    assert second.cache_hit and not third.cache_hit
    assert len(transport.requests) == 2


@pytest.mark.parametrize("change", [
    {"provider": "another-provider"}, {"query": "joint angle "}, {"filters": {"language": "fr"}},
    {"per_page": 2}, {"cursor": ""}, {"api_version": "works-v2"},
])
def test_key_includes_every_semantic_request_dimension(tmp_path, change):
    request = CacheRequest("openalex", "joint angle", {"language": "en"}, 1, None, "works-v1")
    changed = replace(request, **change)
    original_cache = QueryCache(tmp_path / "cache", provider=request.provider, api_version=request.api_version)
    changed_cache = QueryCache(tmp_path / "cache", provider=changed.provider, api_version=changed.api_version)
    assert original_cache.key(request) != changed_cache.key(changed)


@pytest.mark.parametrize("response", [
    Response({"error": "unavailable"}, 503), Response({"meta": [], "results": []}),
    Response({"meta": {"count": -1}, "results": []}), TimeoutError("timed out"),
])
def test_failed_requests_are_not_cached(tmp_path, response):
    cache_dir = tmp_path / "cache"
    result = client_for(Transport(response), cache_dir).search_works("joint angle", per_page=1)
    assert result.status == "failed"
    assert result.request_count == 1
    assert not cache_dir.exists()


def test_partial_success_can_be_replayed(tmp_path):
    response = payload()
    response["results"].append({"title": "missing identifier"})
    transport = Transport(Response(response))
    client = client_for(transport, tmp_path / "cache", max_requests=1)
    first = client.search_works("joint angle", per_page=1)
    second = client.search_works("joint angle", per_page=1)
    assert first.status == second.status == "partial"
    assert second.cache_hit and second.request_count == 0
    assert first.warnings == second.warnings[:-1]


def test_total_timeout_during_parsing_does_not_store_late_success(tmp_path):
    class Clock:
        value = 0.0

        def __call__(self):
            return self.value

    clock = Clock()

    class SlowParser(OpenAlexClient):
        def parse_response(self, response, retrieved_at):
            result = super().parse_response(response, retrieved_at)
            clock.value += 3
            return result

    cache_dir = tmp_path / "cache"
    result = SlowParser(transport=Transport(Response(payload())), api_key="", max_retries=0,
                        clock=clock, total_timeout=2, min_request_interval=0,
                        cache_dir=cache_dir).search_works("joint angle", per_page=1)
    assert result.status == "failed" and result.error_type == "timeout"
    assert result.papers == [] and result.request_count == 1
    assert not cache_dir.exists()


def test_cache_path_that_is_not_a_directory_does_not_fail_successful_request(tmp_path):
    cache_path = tmp_path / "cache"
    cache_path.write_text("user-owned file", encoding="utf-8")
    result = client_for(Transport(Response(payload())), cache_path).search_works("joint angle", per_page=1)
    assert result.status == "success" and result.request_count == 1
    assert any("cache_write_failed" in warning for warning in result.warnings)
    assert cache_path.read_text(encoding="utf-8") == "user-owned file"


def test_new_cache_directories_and_files_are_private_without_scratch(tmp_path):
    cache_dir = tmp_path / "private" / "cache"
    entry, _ = populate(cache_dir)
    assert stat.S_IMODE(cache_dir.stat().st_mode) == 0o700
    assert stat.S_IMODE(cache_dir.parent.stat().st_mode) == 0o700
    assert stat.S_IMODE(entry.stat().st_mode) == 0o600
    assert list(cache_dir.iterdir()) == [entry]
    record = json.loads(entry.read_text(encoding="utf-8"))
    assert record["request_sha256"] == entry.stem
    assert record["response_sha256"] == response_digest(record["response"])
    assert record["retrieved_at"]
    assert record["request_metadata"]["request_url"]


def test_atomic_write_failure_preserves_reportable_scratch_without_failing_request(tmp_path, monkeypatch):
    def fail_replace(*args, **kwargs):
        raise OSError("simulated rename failure")

    monkeypatch.setattr("research_search.query_cache.os.replace", fail_replace)
    cache_dir = tmp_path / "cache"
    result = client_for(Transport(Response(payload())), cache_dir).search_works("joint angle", per_page=1)
    assert result.status == "success" and result.request_count == 1
    scratch = list(cache_dir.glob("*.tmp"))
    assert len(scratch) == 1 and not list(cache_dir.glob("*.json"))
    assert stat.S_IMODE(scratch[0].stat().st_mode) == 0o600
    assert any("cache_write_failed" in warning and str(scratch[0]) in warning for warning in result.warnings)


@pytest.mark.parametrize("location", ["directory", "ancestor", "entry"])
def test_symlinks_are_not_followed_or_overwritten(tmp_path, location):
    target = tmp_path / "target"
    entry, _ = populate(target)
    before = entry.read_bytes()
    if location == "directory":
        cache_dir = tmp_path / "cache"
        cache_dir.symlink_to(target, target_is_directory=True)
    elif location == "ancestor":
        alias = tmp_path / "alias"
        alias.symlink_to(tmp_path, target_is_directory=True)
        cache_dir = alias / "target"
    else:
        cache_dir = tmp_path / "cache"
        cache_dir.mkdir(mode=0o700)
        (cache_dir / entry.name).symlink_to(entry)

    offline_transport = Transport()
    miss = client_for(offline_transport, cache_dir, max_requests=0).search_works("joint angle", per_page=1)
    assert miss.status == "failed" and miss.error_type == "budget_exhausted"
    assert not miss.cache_hit and offline_transport.requests == []
    fresh = client_for(Transport(Response(payload())), cache_dir).search_works("joint angle", per_page=1)
    assert fresh.status == "success"
    assert any("cache_write_failed" in warning for warning in fresh.warnings)
    assert entry.read_bytes() == before
    if location == "entry":
        assert (cache_dir / entry.name).is_symlink()


@pytest.mark.parametrize("corruption", [
    "not_json", "not_object", "schema", "request", "request_checksum", "response_checksum",
    "response_not_object", "response_nan", "response_overflow", "response_bad_shape", "response_bad_count",
    "metadata_null", "metadata_list", "metadata_bad_url", "timestamp", "too_deep", "duplicate_keys",
])
def test_corrupt_entries_are_ignored_without_network_or_crashing(tmp_path, corruption):
    cache_dir = tmp_path / "cache"
    entry, _ = populate(cache_dir)
    record = json.loads(entry.read_text(encoding="utf-8"))
    if corruption == "not_json":
        raw = "{"
    elif corruption == "not_object":
        raw = "[]"
    elif corruption == "too_deep":
        raw = "[" * 2000 + "0" + "]" * 2000
    elif corruption == "duplicate_keys":
        raw = entry.read_text(encoding="utf-8").replace('"schema_version":', '"schema_version": "wrong", "schema_version":')
    else:
        if corruption == "schema":
            record["schema_version"] = "unknown"
        elif corruption == "request":
            record["request"]["query"] = "another query"
        elif corruption == "request_checksum":
            record["request_sha256"] = "0" * 64
        elif corruption == "response_checksum":
            record["response_sha256"] = "0" * 64
        elif corruption == "response_not_object":
            record["response"] = []
        elif corruption in {"response_nan", "response_overflow"}:
            record["response"]["meta"]["bad_number"] = float("nan")
        elif corruption == "response_bad_shape":
            record["response"]["results"] = "not a list"
            record["response_sha256"] = response_digest(record["response"])
        elif corruption == "response_bad_count":
            record["response"]["meta"]["count"] = True
            record["response_sha256"] = response_digest(record["response"])
        elif corruption == "metadata_null":
            record["request_metadata"] = None
        elif corruption == "metadata_list":
            record["request_metadata"] = []
        elif corruption == "metadata_bad_url":
            record["request_metadata"]["request_url"] = 123
        elif corruption == "timestamp":
            record["retrieved_at"] = "not a timestamp"
        raw = json.dumps(record).replace("NaN", "1e999") if corruption == "response_overflow" else json.dumps(record)
    entry.write_text(raw, encoding="utf-8")

    transport = Transport()
    result = client_for(transport, cache_dir, max_requests=0).search_works("joint angle", per_page=1)
    assert result.status == "failed" and result.error_type == "budget_exhausted"
    assert not result.cache_hit and result.request_count == 0
    assert transport.requests == [] and entry.read_text(encoding="utf-8") == raw


def test_invalid_cached_response_falls_back_to_one_fresh_request(tmp_path):
    cache_dir = tmp_path / "cache"
    entry, _ = populate(cache_dir)
    record = json.loads(entry.read_text(encoding="utf-8"))
    record["response"] = {"meta": [], "results": []}
    record["response_sha256"] = response_digest(record["response"])
    entry.write_text(json.dumps(record), encoding="utf-8")
    transport = Transport(Response(payload()))
    result = client_for(transport, cache_dir, max_requests=1).search_works("joint angle", per_page=1)
    assert result.status == "success" and not result.cache_hit
    assert result.request_count == len(transport.requests) == 1


@pytest.mark.parametrize("field", ["query", "encoded_query", "double_encoded_query", "filter_value", "filter_key", "cursor", "api_version"])
def test_known_credential_in_request_payload_bypasses_cache_without_leaking(tmp_path, field):
    credential = "private/key+fixture with space"
    query, filters, cursor, api_version = "joint angle", {}, None, "works-v1"
    if field == "query":
        query += " " + credential
    elif field == "encoded_query":
        query += " " + quote_plus(credential)
    elif field == "double_encoded_query":
        query += " " + quote(quote(credential, safe=""), safe="")
    elif field == "filter_value":
        filters = {"language": credential}
    elif field == "filter_key":
        filters = {credential: "en"}
    elif field == "cursor":
        cursor = credential
    else:
        api_version = credential
    transport = Transport(Response(payload()), Response(payload()))
    cache_dir = tmp_path / "cache"
    client = OpenAlexClient(transport=transport, api_key=credential, cache_dir=cache_dir,
                            api_version=api_version, max_retries=0, min_request_interval=0)
    results = [client.search_works(query, per_page=1, filters=filters, cursor=cursor) for _ in range(2)]
    assert all(result.status == "success" and not result.cache_hit and result.cache_key is None for result in results)
    assert len(transport.requests) == 2 and not cache_dir.exists()
    for result in results:
        dumped = json.dumps(asdict(result))
        for variant in (credential, quote(credential, safe=""), quote_plus(credential)):
            assert variant not in dumped
        assert "cache_bypassed_sensitive_request" in result.warnings


@pytest.mark.parametrize("query, filters", [
    ("joint angle api_key=unknown-fixture", {}),
    ("joint angle Bearer unknown-fixture", {}),
    ("joint angle", {"api_key": "unknown-fixture"}),
    ("joint angle", {"client_secret": "unknown-fixture"}),
    ("joint angle api%5Fkey%3Dunknown-fixture", {}),
])
def test_named_credentials_are_not_cached_even_without_known_api_key(tmp_path, query, filters):
    transport = Transport(Response(payload()))
    cache_dir = tmp_path / "cache"
    result = client_for(transport, cache_dir).search_works(query, per_page=1, filters=filters)
    assert result.status == "success" and result.cache_key is None
    assert "cache_bypassed_sensitive_request" in result.warnings
    assert not cache_dir.exists()
    assert "unknown-fixture" not in json.dumps(asdict(result))


@pytest.mark.parametrize("value", [float("nan"), float("inf"), ["en"], {"value": "en"}])
def test_nonstandard_filter_values_bypass_cache_instead_of_breaking_existing_transport(tmp_path, value):
    transport = Transport(Response(payload()))
    cache_dir = tmp_path / "cache"
    result = client_for(transport, cache_dir).search_works("joint angle", filters={"language": value})
    assert result.status == "success" and len(transport.requests) == 1
    assert result.cache_key is None and not cache_dir.exists()
    assert "cache_bypassed_invalid_parameters" in result.warnings


def test_credentials_are_not_key_dimensions_and_response_and_metadata_are_redacted(tmp_path):
    credential = "private/key+fixture with space"
    reflected = payload()
    reflected["request"] = {"api_key": credential, "Authorization": "Bearer " + credential}
    reflected["echo"] = quote_plus(credential)
    cache_dir = tmp_path / "cache"
    first = OpenAlexClient(transport=Transport(Response(reflected)), api_key=credential, cache_dir=cache_dir,
                           max_retries=0, min_request_interval=0).search_works("joint angle", per_page=1)
    entry = stored_entry(cache_dir)
    on_disk = entry.read_text(encoding="utf-8")
    assert all(value not in on_disk for value in (credential, quote(credential, safe=""), quote_plus(credential)))
    record = json.loads(on_disk)
    # Treat metadata as untrusted even when the cached response checksum is valid.
    record["request_metadata"]["request_url"] = (
        "https://username:password@api.openalex.org/works?api_key=unknown-fixture&search=" + quote_plus(credential)
    )
    entry.write_text(json.dumps(record), encoding="utf-8")
    transport = Transport()
    replay = OpenAlexClient(transport=transport, api_key=credential, cache_dir=cache_dir,
                            max_requests=0).search_works("joint angle", per_page=1)
    anonymous = client_for(transport, cache_dir, max_requests=0).search_works("joint angle", per_page=1)
    assert first.cache_key == replay.cache_key == anonymous.cache_key
    assert replay.cache_hit and anonymous.cache_hit and transport.requests == []
    for result in (replay, anonymous):
        assert "unknown-fixture" not in result.request_url
        assert "username:password" not in result.request_url
    assert credential not in json.dumps(asdict(replay))


def test_metadata_bytes_counts_each_network_body_but_never_replays(tmp_path):
    error, success = Response({"error": "retry"}, 503), Response(payload())
    transport = Transport(error, success)
    client = OpenAlexClient(transport=transport, api_key="", cache_dir=tmp_path / "cache",
                            max_retries=1, backoff_factor=0, min_request_interval=0)
    result = client.search_works("joint angle", per_page=1)
    assert result.request_count == 2
    assert result.metadata_bytes == len(error.payload) + len(success.payload)
    replay = client.search_works("joint angle", per_page=1)
    assert replay.cache_hit and replay.metadata_bytes == 0 and replay.request_count == 0
