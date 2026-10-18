"""Provider contracts are tested with local payloads and injected transports only."""
import json
from urllib.parse import parse_qs, urlsplit

import pytest

from research_search.providers import Provider, PubMedProvider, SearchRequest, SemanticScholarProvider


class FakeResponse:
    def __init__(self, payload, status=200):
        self.status = status
        self.body = payload.encode() if isinstance(payload, str) else json.dumps(payload).encode()
        self.closed = False

    def read(self, *args):
        return self.body

    def close(self):
        self.closed = True


class FakeTransport:
    def __init__(self, *outcomes):
        self.outcomes = list(outcomes)
        self.requests = []

    def __call__(self, request, *, timeout):
        self.requests.append(request)
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


@pytest.mark.parametrize("provider_type", [PubMedProvider, SemanticScholarProvider])
def test_planned_requests_never_call_even_an_injected_transport(provider_type):
    transport = FakeTransport()
    provider = provider_type(transport=transport)
    result = provider.search(SearchRequest("joint angle"))
    assert isinstance(provider, Provider)
    assert result.status == "planned"
    assert result.request_count == result.fetched_count == 0
    assert result.reported_count is None
    assert result.executed_at is None
    assert result.raw_response["plan"]
    assert transport.requests == []


@pytest.mark.parametrize("provider_type", [PubMedProvider, SemanticScholarProvider])
def test_live_without_transport_is_explicitly_not_executed(provider_type):
    result = provider_type().search(SearchRequest("joint angle", mode="live"))
    assert result.status == "not_executed"
    assert result.error_type == "transport_not_configured"
    assert result.request_count == 0
    assert result.executed_at is None


def test_pubmed_plan_keeps_title_abstract_and_filters_explicit():
    request = SearchRequest('("joint angle" OR "knee flexion") AND EMG',
                            {"date_from": "2020-01-01", "date_to": "2025-12-31", "language": "en"}, 7)
    result = PubMedProvider().search(request)
    params = result.raw_response["plan"][0]["params"]
    assert params["field"] == "title/abstract"
    assert '"english"[Language]' in params["term"]
    assert request.query in params["term"]
    assert params["mindate"] == "2020/01/01"
    assert params["maxdate"] == "2025/12/31"
    assert params["datetype"] == "pdat"
    assert params["retmax"] == 7
    assert "MeSH" not in params["term"]


def test_query_hash_is_stable_across_mode_and_filter_key_order():
    provider = PubMedProvider()
    one = provider.search(SearchRequest("EMG", {"language": "en", "date_from": "2020-01-01"}))
    two = provider.search(SearchRequest("EMG", {"date_from": "2020-01-01", "language": "en"}, mode="live"))
    changed = provider.search(SearchRequest("EEG", {"language": "en", "date_from": "2020-01-01"}))
    assert len(one.query_hash) == 64
    assert one.query_hash == two.query_hash
    assert one.query_hash != changed.query_hash


PUBMED_XML = """<?xml version="1.0"?>
<!DOCTYPE PubmedArticleSet SYSTEM "https://example.invalid/never-fetch.dtd">
<PubmedArticleSet><PubmedArticle><MedlineCitation>
<PMID>123</PMID><Article><Journal><JournalIssue><PubDate><Year>2024</Year></PubDate></JournalIssue><Title>Example Journal</Title></Journal>
<ArticleTitle>Joint <i>angle</i> estimation</ArticleTitle>
<Abstract><AbstractText Label="BACKGROUND">Signal <b>analysis</b>.</AbstractText><AbstractText Label="RESULTS">Works offline.</AbstractText></Abstract>
<AuthorList><Author><LastName>Lee</LastName><ForeName>Ada</ForeName></Author><Author><CollectiveName>Study Group</CollectiveName></Author></AuthorList>
</Article><MeshHeadingList><MeshHeading><DescriptorName UI="D000001">Electromyography</DescriptorName><QualifierName>methods</QualifierName></MeshHeading></MeshHeadingList>
<KeywordList Owner="NOTNLM"><Keyword>surface EMG</Keyword></KeywordList>
</MedlineCitation><PubmedData><ArticleIdList><ArticleId IdType="doi">10.1000/example</ArticleId></ArticleIdList></PubmedData>
</PubmedArticle></PubmedArticleSet>"""


def pubmed_live(*outcomes, **kwargs):
    transport = FakeTransport(*outcomes)
    result = PubMedProvider(transport=transport, **kwargs).search(SearchRequest("EMG", limit=1, mode="live"))
    return result, transport


def test_pubmed_xml_inline_text_mesh_and_author_keyword_provenance_are_separate():
    result, transport = pubmed_live(
        FakeResponse({"esearchresult": {"count": "100", "idlist": ["123"]}}), FakeResponse(PUBMED_XML))
    assert result.status == "success"
    assert result.request_count == 2
    assert result.reported_count == 100
    assert result.fetched_count == 1
    paper = result.papers[0]
    assert paper.pmid == "123"
    assert paper.title == "Joint angle estimation"
    assert paper.abstract == "BACKGROUND: Signal analysis. RESULTS: Works offline."
    assert paper.authors == ["Lee, Ada", "Study Group"]
    assert paper.journal == "Example Journal"
    assert paper.publication_year == 2024
    assert paper.mesh_terms == ["Electromyography"]
    assert paper.author_keywords == ["surface EMG"]
    assert paper.database_keywords == []
    assert "MeshHeadingList" in paper.field_sources["mesh_terms"]
    assert "KeywordList" in paper.field_sources["author_keywords"]
    assert paper.doi == "10.1000/example"
    assert len(transport.requests) == 2
    assert result.executed_at
    json.dumps(result.to_dict())  # raw XML must remain serializable evidence


def test_pubmed_esearch_xml_and_empty_results_do_not_fetch():
    result, transport = pubmed_live(FakeResponse("<eSearchResult><Count>0</Count><IdList/></eSearchResult>"))
    assert result.status == "success"
    assert result.reported_count == result.fetched_count == 0
    assert result.request_count == len(transport.requests) == 1


def test_pubmed_esearch_xml_ids_are_parsed_and_followed_by_efetch():
    result, transport = pubmed_live(FakeResponse("<eSearchResult><Count>1</Count><IdList><Id>123</Id></IdList></eSearchResult>"),
                                     FakeResponse(PUBMED_XML))
    assert result.status == "success"
    assert result.papers[0].pmid == "123"


def test_pubmed_offline_parser_never_calls_transport():
    transport = FakeTransport()
    provider = PubMedProvider(transport=transport)
    result = provider.parse_response(PUBMED_XML, SearchRequest("EMG"), reported_count=77)
    assert result.status == "success"
    assert result.request_count == 0
    assert result.executed_at is None
    assert result.reported_count == 77
    assert result.fetched_count == 1
    assert transport.requests == []


@pytest.mark.parametrize("payload", [{}, {"error": "upstream refused"}, {"esearchresult": {"ERROR": "bad query"}},
                                     "<eSearchResult><ERROR>bad query</ERROR></eSearchResult>"])
def test_pubmed_error_or_wrong_shape_is_not_empty_success(payload):
    result, _ = pubmed_live(FakeResponse(payload))
    assert result.status == "failed"
    assert result.error_type in {"provider_error", "invalid_response"}
    assert result.fetched_count == 0


def test_pubmed_fetch_error_is_structured_and_preserves_search_count():
    result, _ = pubmed_live(FakeResponse({"esearchresult": {"count": "12", "idlist": ["123"]}}),
                            FakeResponse("not XML or JSON"))
    assert result.status in {"failed", "partial"}
    assert result.error_type == "invalid_response"
    assert result.reported_count == 12
    assert result.request_count == 2


@pytest.mark.parametrize("provider_type", [PubMedProvider, SemanticScholarProvider])
def test_zero_request_budget_never_calls_transport(provider_type):
    transport = FakeTransport()
    result = provider_type(transport=transport, max_requests=0).search(SearchRequest("EMG", mode="live"))
    assert result.status == "not_executed"
    assert result.error_type == "budget_exhausted"
    assert result.request_count == 0
    assert result.executed_at is None
    assert transport.requests == []


def test_pubmed_budget_counts_two_stage_search_without_faking_papers():
    result, transport = pubmed_live(FakeResponse({"esearchresult": {"count": "12", "idlist": ["123"]}}), max_requests=1)
    assert result.error_type == "budget_exhausted"
    assert result.reported_count == 12
    assert result.request_count == len(transport.requests) == 1
    assert result.fetched_count == 0


def test_semantic_scholar_search_preserves_ids_and_explicit_citation_field_sources():
    payload = {"total": 20, "data": [{"paperId": "s2-a", "title": "Signal study", "abstract": "Abstract",
        "externalIds": {"DOI": "10.1000/a", "PubMed": "123"}, "authors": [{"name": "Ada Lee"}],
        "venue": "Journal", "year": 2024, "citationCount": 8,
        "citations": [{"paperId": "citing-a"}], "references": [{"paperId": "cited-a"}]}]}
    result = SemanticScholarProvider().parse_response(payload, SearchRequest("EMG"))
    assert result.status == "success"
    assert result.reported_count == 20
    assert result.request_count == 0
    paper = result.papers[0]
    assert paper.s2_paper_id == "s2-a"
    assert paper.doi == "10.1000/a"
    assert paper.pmid == "123"
    assert paper.authors == ["Ada Lee"]
    assert paper.citation_ids == ["citing-a"]
    assert paper.reference_ids == ["cited-a"]
    assert "citations" in paper.citation_source
    assert "references" in paper.references_source
    assert paper.channel == "keyword"
    assert paper.discovery_channel is False


@pytest.mark.parametrize("payload", [{}, {"error": "rate limit"}, {"data": "wrong"}, {"total": True, "data": []}])
def test_semantic_scholar_invalid_response_is_not_empty_success(payload):
    result = SemanticScholarProvider(transport=FakeTransport(FakeResponse(payload))).search(SearchRequest("EMG", mode="live"))
    assert result.status == "failed"
    assert result.error_type in {"provider_error", "invalid_response"}


def test_semantic_empty_response_and_shared_budget_are_distinct():
    transport = FakeTransport(FakeResponse({"total": 0, "data": []}))
    provider = SemanticScholarProvider(transport=transport, max_requests=1)
    empty = provider.search(SearchRequest("EMG", mode="live"))
    exhausted = provider.search(SearchRequest("EEG", mode="live"))
    assert empty.status == "success"
    assert empty.reported_count == empty.fetched_count == 0
    assert exhausted.status == "not_executed"
    assert exhausted.error_type == "budget_exhausted"
    assert exhausted.request_count == 0
    assert len(transport.requests) == 1


def test_recommendation_is_discovery_not_a_direct_citation():
    provider = SemanticScholarProvider(transport=FakeTransport(FakeResponse({"recommendedPapers": [
        {"paperId": "s2-new", "title": "Recommendation"}]})))
    result = provider.recommend(["s2-seed"], limit=2, mode="live")
    paper = result.papers[0]
    assert paper.discovery_channel is True
    assert paper.channel == "semantic_recommendation"
    assert paper.candidate_reason == "semantic_recommendation"
    assert paper.seed_ids == ["s2-seed"]
    assert paper.citation_source is None
    assert paper.references_source is None
    assert paper.citation_ids == paper.reference_ids == []
    params = parse_qs(urlsplit(provider.transport.requests[0].full_url).query)
    assert params["limit"] == ["2"]


def test_citations_and_references_use_explicit_edge_direction_only():
    provider = SemanticScholarProvider(transport=FakeTransport(
        FakeResponse({"data": [{"citingPaper": {"paperId": "citing", "title": "Citing paper"}}]}),
        FakeResponse({"data": [{"citedPaper": {"paperId": "cited", "title": "Cited paper"}}]})))
    citing = provider.citations("seed", mode="live").papers[0]
    cited = provider.citations("seed", direction="references", mode="live").papers[0]
    assert citing.channel == "citation" and citing.seed_ids == ["seed"]
    assert cited.channel == "reference" and cited.seed_ids == ["seed"]
    assert citing.citation_source and cited.references_source
    assert citing.discovery_channel and cited.discovery_channel


def test_discovery_plans_never_execute_without_explicit_mode_and_transport():
    transport = FakeTransport()
    provider = SemanticScholarProvider(transport=transport)
    assert provider.recommend(["seed"]).status == "planned"
    assert provider.citations("seed").status == "planned"
    assert SemanticScholarProvider().recommend(["seed"], mode="live").status == "not_executed"
    assert transport.requests == []


@pytest.mark.parametrize("provider_type", [PubMedProvider, SemanticScholarProvider])
def test_http_errors_close_response_and_redact_sensitive_reflections(provider_type):
    secret = "private" + "/key+ space"
    reflected_one = "hidden-" + "other"
    reflected_two = "hidden-" + "bearer"
    credential_field = "api" + "_" + "key"
    response = FakeResponse({"error": credential_field + "=" + reflected_one + " Bearer " + reflected_two + " " + secret}, status=429)
    transport = FakeTransport(response)
    result = provider_type(transport=transport, api_key=secret).search(SearchRequest("EMG", mode="live"))
    assert result.status == "failed"
    assert result.error_type == "http_error"
    serialized = json.dumps(result.to_dict())
    for secret in (secret, reflected_one, reflected_two):
        assert secret not in serialized
    assert response.closed


def test_pubmed_api_key_in_filters_does_not_escape_into_error_or_plan(capsys):
    secret = "parameter-" + "secret"
    provider = PubMedProvider(transport=FakeTransport(TimeoutError("api_key=" + secret)))
    request = SearchRequest("EMG", {"api_key": secret}, mode="live")
    result = provider.search(request)
    assert secret not in json.dumps(result.to_dict())
    assert secret not in capsys.readouterr().out
    assert result.error_type == "timeout"


def test_fusion_merges_shared_doi_and_preserves_each_source_record_without_run_ids():
    from research_search.models import Paper
    from research_search.providers import ProviderPaper, fuse_results
    left = Paper("https://openalex.org/W1", "A study", openalex_id="https://openalex.org/W1", doi="10.1000/a")
    right = ProviderPaper("semantic_scholar", "s2-a", "A study", s2_paper_id="s2-a", doi="https://doi.org/10.1000/A")
    result = fuse_results([{"provider": "openalex", **left.to_dict()}, right])
    assert len(result.papers) == 1
    assert sum(map(len, result.source_records.values())) == 2
    assert result.provider_ids == {"openalex": ["https://openalex.org/W1"], "semantic_scholar": ["s2-a"]}
    assert all(not record.get("source_run_ids") for records in result.source_records.values() for record in records)
    assert result.coverage_by_provider["openalex"]["unique_count"] == 1
    assert result.coverage_by_provider["semantic_scholar"]["unique_count"] == 1
    assert result.merge_events  # never silently merge, even without a conflict


def test_fusion_conflicting_doi_on_shared_pmid_is_retained_separately():
    from research_search.providers import ProviderPaper, fuse_results
    result = fuse_results([
        ProviderPaper("pubmed", "1", "Same title", pmid="1", doi="10.1000/a"),
        ProviderPaper("semantic_scholar", "s2-a", "Same title", pmid="1", doi="10.1000/b", s2_paper_id="s2-a")])
    assert len(result.papers) == 2
    assert result.conflicts
    assert any(conflict.kind == "identifier_conflict" for conflict in result.conflicts)
    assert sum(map(len, result.source_records.values())) == 2


def test_fusion_same_title_with_different_ids_never_silently_merges():
    from research_search.providers import ProviderPaper, fuse_results
    result = fuse_results([
        ProviderPaper("pubmed", "1", "Same-title", pmid="1"),
        ProviderPaper("pubmed", "2", "Same title", pmid="2")])
    assert len(result.papers) == 2
    assert result.conflicts
    assert len(result.source_records) == 2


def test_fusion_title_only_duplicates_have_audited_merge():
    from research_search.providers import ProviderPaper, fuse_results
    result = fuse_results([ProviderPaper("a", "local-a", "A study"), ProviderPaper("b", "local-b", "A: study")])
    assert len(result.papers) == 1
    assert result.merge_events[0]["matched_by"] == ["title_fingerprint"]


def test_fusion_keeps_keyword_and_discovery_views_separate_when_same_paper():
    from research_search.providers import ProviderPaper, ProviderResult, fuse_results
    keyword = ProviderPaper("pubmed", "123", "Same", pmid="123", channel="keyword")
    discovery = ProviderPaper("semantic_scholar", "s2-a", "Same", pmid="123", s2_paper_id="s2-a",
        channel="semantic_recommendation", discovery_channel=True, candidate_reason="semantic_recommendation", seed_ids=["seed"])
    planned = ProviderResult(provider="unexecuted", status="planned")
    result = fuse_results([keyword, discovery, planned])
    assert len(result.papers) == 1
    assert len(result.retrieval_papers) == len(result.discovery_papers) == 1
    assert result.retrieval_papers[0].discovery_channel is False
    assert result.discovery_papers[0].candidate_reason == "semantic_recommendation"
    assert result.coverage_by_provider["semantic_scholar"]["discovery_count"] == 1
    assert result.coverage_by_provider["semantic_scholar"]["retrieval_count"] == 0
    assert result.coverage_by_provider["unexecuted"]["raw_count"] == 0
    assert "recall" not in result.to_dict()


def test_fusion_preserves_existing_run_ids_but_does_not_invent_them():
    from research_search.models import Paper
    from research_search.providers import fuse_results
    source = Paper("W1", "Study", openalex_id="W1", source_run_ids=["existing-run"])
    result = fuse_results([source])
    assert next(iter(result.source_records.values()))[0]["source_run_ids"] == ["existing-run"]


def test_limit_caps_local_payloads_without_overstating_fetched_count():
    result = SemanticScholarProvider().parse_response({"total": 100, "data": [
        {"paperId": "a", "title": "A"}, {"paperId": "b", "title": "B"}]}, SearchRequest("test", limit=1))
    assert result.reported_count == 100
    assert result.fetched_count == len(result.papers) == 1


def test_fusion_unrelated_records_do_not_create_identifier_conflict():
    from research_search.providers import ProviderPaper, fuse_results
    fused = fuse_results([ProviderPaper("pubmed", "1", "First study", pmid="1", doi="10.1000/a"),
                          ProviderPaper("pubmed", "2", "Different study", pmid="2", doi="10.1000/b")])
    assert len(fused.papers) == 2
    assert fused.conflicts == []


def test_fusion_same_doi_conflicting_pmid_preserves_both_source_groups():
    from research_search.providers import ProviderPaper, fuse_results
    fused = fuse_results([ProviderPaper("pubmed", "1", "Study", pmid="1", doi="10.1000/a"),
                          ProviderPaper("pubmed", "2", "Study", pmid="2", doi="10.1000/a")])
    assert len(fused.papers) == 2
    assert len(fused.source_records) == 2
    assert sum(map(len, fused.source_records.values())) == 2
    assert fused.conflicts


def test_fusion_checks_identifiers_accumulated_from_all_sources():
    from research_search.providers import ProviderPaper, fuse_results
    fused = fuse_results([
        ProviderPaper("a", "a", "Study", doi="10.1000/a"),
        ProviderPaper("b", "b", "Study", doi="10.1000/a", pmid="1"),
        ProviderPaper("c", "c", "Study", doi="10.1000/a", pmid="2")])
    assert len(fused.papers) == 2
    assert fused.conflicts


def test_pubmed_offline_summary_json_keeps_absent_abstract_and_mesh_absent():
    payload = {"result": {"uids": ["123"], "123": {"uid": "123", "title": "Summary", "authors": [{"name": "Lee A"}],
        "fulljournalname": "Journal", "articleids": [{"idtype": "doi", "value": "10.1000/summary"}]}}}
    result = PubMedProvider().parse_response(payload, SearchRequest("test"))
    assert result.status == "success"
    assert result.papers[0].abstract is None
    assert result.papers[0].mesh_terms == result.papers[0].author_keywords == []
    assert result.papers[0].doi == "10.1000/summary"


def test_pubmed_sensitive_xml_reflection_is_redacted_in_paper_raw_too():
    secret = "reflection-" + "secret"
    payload = PUBMED_XML.replace("Works offline.", "api_key=" + secret)
    result = PubMedProvider(api_key=secret).parse_response(payload, SearchRequest("test"))
    assert result.status == "success"
    assert secret not in json.dumps(result.to_dict())
