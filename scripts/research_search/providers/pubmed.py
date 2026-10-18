"""PubMed ESearch (JSON/XML) and EFetch XML, offline unless explicitly injected."""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import replace
from datetime import date
import json
import re
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request
import xml.etree.ElementTree as ET

from .base import Provider, ProviderFailure, coerce_request, decode_json_count, now_utc, redact_value
from .models import ProviderPaper, ProviderResult, SearchRequest


def _decode(payload: Any) -> Any:
    if isinstance(payload, (str, bytes)):
        text = payload.decode("utf-8") if isinstance(payload, bytes) else payload
        if text.lstrip().startswith("<"):
            # Ordinary external DTD declarations are not fetched by ElementTree;
            # internal entity declarations are unnecessary for PubMed metadata.
            if re.search(r"<!ENTITY\b", text, re.IGNORECASE):
                raise ValueError("XML entity declarations are not accepted")
            return ET.fromstring(text)
        return json.loads(text)
    return payload


def _raw(payload: Any) -> Any:
    return ET.tostring(payload, encoding="unicode") if isinstance(payload, ET.Element) else payload


def _text(node: ET.Element | None) -> str | None:
    return re.sub(r"\s+", " ", "".join(node.itertext())).strip() or None if node is not None else None


class PubMedProvider(Provider):
    """At most one ESearch and one EFetch per call; no pagination or retries.

    ESearch supports the documented JSON and XML formats. EFetch always requests
    native PubMed XML (not a fictitious EFetch JSON endpoint). ``parse_response``
    also accepts official ESummary JSON for metadata-only offline replay.
    """

    name = "pubmed"
    esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    efetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    languages = {"en": "english", "eng": "english", "zh": "chinese", "de": "german",
                 "fr": "french", "es": "spanish", "ja": "japanese", "ko": "korean", "ru": "russian"}

    def __init__(self, *, email: str | None = None, tool: str | None = None, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.email, self.tool = email, tool

    def _search_params(self, request: SearchRequest) -> dict[str, Any]:
        allowed = {"date_from", "date_to", "language", "retmode", "api_key", "email", "tool", "mesh_terms"}
        if set(request.filters) - allowed:
            raise ValueError("unsupported PubMed filters")
        if request.limit > 10000:
            raise ValueError("PubMed adapter limit must be at most 10000; pagination is not implemented")
        retmode = request.filters.get("retmode", "json")
        if retmode not in {"json", "xml"}:
            raise ValueError("ESearch retmode must be json or xml")
        # ESearch's documented default field restricts unqualified text terms.
        # Explicit Language/MeSH tags below remain distinct query clauses.
        term = request.query
        mesh = request.filters.get("mesh_terms", [])
        if not isinstance(mesh, list) or any(not isinstance(value, str) or not value.strip() or re.search(r'["\[\]\x00-\x1f]', value) for value in mesh):
            raise ValueError("mesh_terms must be an array of literal descriptor names")
        if mesh:
            term = f'({term}) AND (' + " OR ".join(f'"{value.strip()}"[MeSH Terms]' for value in mesh) + ")"
        language = request.filters.get("language")
        if language is not None:
            if not isinstance(language, str) or not re.fullmatch(r"[A-Za-z -]{2,40}", language):
                raise ValueError("language must be a language name or supported code")
            language = self.languages.get(language.casefold(), language.casefold())
            term = f'({term}) AND "{language}"[Language]'
        params: dict[str, Any] = {"db": "pubmed", "term": term, "field": "title/abstract",
                                  "retmax": request.limit, "retmode": retmode}
        for source, target in (("date_from", "mindate"), ("date_to", "maxdate")):
            if source in request.filters:
                value = request.filters[source]
                if not isinstance(value, str):
                    raise ValueError("date filters must use YYYY-MM-DD")
                params[target] = date.fromisoformat(value).strftime("%Y/%m/%d")
                params["datetype"] = "pdat"
        if request.filters.get("date_from", "") > request.filters.get("date_to", "9999-12-31"):
            raise ValueError("date_from must not exceed date_to")
        return self._auth(params, request)

    def _auth(self, params: dict[str, Any], request: SearchRequest) -> dict[str, Any]:
        for key, default in (("api_key", self.api_key), ("email", self.email), ("tool", self.tool)):
            value = request.filters.get(key, default)
            if value:
                if not isinstance(value, str):
                    raise ValueError("authentication/contact parameters must be strings")
                params[key] = value
        return params

    def _fetch_params(self, ids: list[str], request: SearchRequest) -> dict[str, Any]:
        return self._auth({"db": "pubmed", "id": ",".join(ids), "retmode": "xml"}, request)

    def _plan(self, request: SearchRequest) -> list[dict[str, Any]]:
        return redact_value([
            {"endpoint": self.esearch_url, "method": "GET", "params": self._search_params(request)},
            {"endpoint": self.efetch_url, "method": "GET", "params": self._fetch_params(["<ESearch PMID list>"], request)},
        ], self._secrets(request))

    def search(self, request: SearchRequest | Mapping[str, Any]) -> ProviderResult:
        request = coerce_request(request)
        try:
            plan = self._plan(request)
        except (TypeError, ValueError) as error:
            return self._failed(request, {}, ProviderFailure("invalid_request", str(error)))
        deferred = self._preflight(request, plan)
        if deferred:
            return deferred
        before, executed_at = self._requests_made, now_utc()
        raw: dict[str, Any] = {"plan": plan}
        reported_count = None
        try:
            search_url = self.esearch_url + "?" + urlencode(self._search_params(request))
            payload = self._send(Request(search_url), secrets=self._secrets(request))
            raw["esearch"] = _raw(_decode(payload))
            reported_count, ids = self.parse_search_response(payload)
            ids = ids[:request.limit]
            if not ids:
                return ProviderResult(self.name, "success", request_count=self._requests_made - before,
                                      reported_count=reported_count, raw_response=redact_value(raw, self._secrets(request)),
                                      source_level="A", executed_at=executed_at, query_hash=request.query_hash)
            fetch_url = self.efetch_url + "?" + urlencode(self._fetch_params(ids, request))
            payload = self._send(Request(fetch_url), secrets=self._secrets(request))
            raw["efetch"] = _raw(_decode(payload))
            result = self.parse_response(payload, request, reported_count=reported_count)
            result.request_count, result.executed_at = self._requests_made - before, executed_at
            result.raw_response = redact_value(raw, self._secrets(request))
            expected = set(ids)
            result.papers = [paper for paper in result.papers if paper.pmid in expected]
            result.fetched_count = len(result.papers)
            if result.status == "success" and {paper.pmid for paper in result.papers} != expected:
                result.status, result.error_type = "partial", "missing_records"
                result.error_message = "EFetch did not supply every requested PMID"
            return result
        except (ValueError, TypeError, ET.ParseError, UnicodeError) as error:
            return self._failed(request, raw, error, request_count=self._requests_made - before,
                                executed_at=executed_at, reported_count=reported_count)

    @staticmethod
    def parse_search_response(payload: Any) -> tuple[int, list[str]]:
        payload = _decode(payload)
        if isinstance(payload, ET.Element):
            if payload.tag != "eSearchResult":
                raise ValueError("expected eSearchResult XML")
            if payload.find(".//ERROR") is not None or payload.find(".//ErrorList") is not None:
                raise ProviderFailure("provider_error", "PubMed ESearch reported an error")
            count = decode_json_count(payload.findtext("Count"))
            if payload.find("IdList") is None:
                raise ValueError("ESearch XML is missing IdList")
            values = [node.text for node in payload.findall("./IdList/Id")]
        elif isinstance(payload, Mapping):
            result = payload.get("esearchresult")
            if payload.get("error") or (isinstance(result, Mapping) and (result.get("ERROR") or result.get("errorlist"))):
                raise ProviderFailure("provider_error", "PubMed ESearch reported an error")
            if not isinstance(result, Mapping) or "idlist" not in result:
                raise ValueError("expected ESearch JSON with esearchresult.count/idlist")
            count = decode_json_count(result.get("count"))
            values = result["idlist"]
        else:
            raise ValueError("expected ESearch JSON or XML")
        if not isinstance(values, list) or any(not isinstance(value, str) or not value.isdigit() for value in values):
            raise ValueError("ESearch PMID list must contain numeric strings")
        return count, list(dict.fromkeys(values))

    def parse_response(self, payload: Any, request: SearchRequest, *, reported_count: int | None = None) -> ProviderResult:
        """Offline parse only: request_count=0 and executed_at=None."""
        request = coerce_request(request)
        raw = None
        try:
            parsed = _decode(payload)
            raw = redact_value(_raw(parsed), self._secrets(request))
            papers, warnings = self.parse_fetch_response(parsed)
            # The parser keeps source XML as evidence in ProviderPaper.raw.  It
            # must follow the same credential redaction policy as the result.
            secrets = self._secrets(request)
            papers = [ProviderPaper(**redact_value(paper.to_dict(), secrets)) for paper in papers[:request.limit]]
            return ProviderResult(self.name, "partial" if warnings else "success", reported_count=reported_count,
                                  fetched_count=len(papers), papers=papers, raw_response=raw,
                                  error_type="partial_records" if warnings else None,
                                  error_message="; ".join(warnings) if warnings else None,
                                  source_level="A", query_hash=request.query_hash)
        except (ValueError, TypeError, ET.ParseError, UnicodeError) as error:
            return self._failed(request, raw, error, reported_count=reported_count)

    @classmethod
    def parse_fetch_response(cls, payload: Any) -> tuple[list[ProviderPaper], list[str]]:
        payload = _decode(payload)
        if isinstance(payload, Mapping):
            return cls._summary_json(payload)
        if not isinstance(payload, ET.Element) or payload.tag not in {"PubmedArticleSet", "PubmedArticle"}:
            raise ValueError("expected native PubmedArticleSet XML or ESummary JSON")
        if payload.find(".//ERROR") is not None:
            raise ProviderFailure("provider_error", "PubMed EFetch reported an error")
        articles = [payload] if payload.tag == "PubmedArticle" else list(payload)
        papers, warnings = [], []
        for article in articles:
            if article.tag != "PubmedArticle":
                warnings.append("unsupported_pubmed_record_type")
                continue
            paper = cls._paper_xml(article)
            if paper:
                papers.append(paper)
            else:
                warnings.append("article_missing_pmid_or_title")
        return papers, warnings

    @staticmethod
    def _paper_xml(article: ET.Element) -> ProviderPaper | None:
        pmid, title = _text(article.find("./MedlineCitation/PMID")), _text(article.find(".//ArticleTitle"))
        if not pmid or not pmid.isdigit() or not title:
            return None
        authors = []
        for author in article.findall(".//AuthorList/Author"):
            name = _text(author.find("CollectiveName")) or ", ".join(value for value in (
                _text(author.find("LastName")), _text(author.find("ForeName")) or _text(author.find("Initials"))) if value)
            if name:
                authors.append(name)
        abstract = []
        for node in article.findall(".//Abstract/AbstractText"):
            text = _text(node)
            if text:
                abstract.append(f"{node.attrib['Label']}: {text}" if node.attrib.get("Label") else text)
        doi_node = next((node for node in article.findall(".//ArticleId") if node.get("IdType") == "doi"), None)
        doi_source = "PubmedData/ArticleIdList/ArticleId[@IdType='doi']"
        if doi_node is None:
            doi_node = next((node for node in article.findall(".//ELocationID") if node.get("EIdType") == "doi"), None)
            doi_source = "Article/ELocationID[@EIdType='doi']"
        year = _text(article.find(".//Journal/JournalIssue/PubDate/Year")) or _text(article.find(".//Journal/JournalIssue/PubDate/MedlineDate")) or ""
        year_match = re.search(r"\b\d{4}\b", year)
        sources = {"pmid": "MedlineCitation/PMID", "title": "Article/ArticleTitle",
                   "abstract": "Article/Abstract/AbstractText", "authors": "Article/AuthorList",
                   "journal": "Article/Journal/Title", "mesh_terms": "MedlineCitation/MeshHeadingList",
                   "author_keywords": "MedlineCitation/KeywordList"}
        if doi_node is not None:
            sources["doi"] = doi_source
        return ProviderPaper(
            "pubmed", pmid, title, pmid=pmid, doi=_text(doi_node), abstract=" ".join(abstract) or None,
            authors=authors, journal=_text(article.find(".//Journal/Title")),
            publication_year=int(year_match.group()) if year_match else None,
            mesh_terms=[text for node in article.findall(".//MeshHeading/DescriptorName") if (text := _text(node))],
            author_keywords=[text for node in article.findall(".//KeywordList/Keyword") if (text := _text(node))],
            channel="keyword", source_url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            field_sources={key: "PubMed XML / " + value for key, value in sources.items()},
            raw={"xml": ET.tostring(article, encoding="unicode")},
        )

    @staticmethod
    def _summary_json(payload: Mapping[str, Any]) -> tuple[list[ProviderPaper], list[str]]:
        if payload.get("error"):
            raise ProviderFailure("provider_error", "PubMed ESummary reported an error")
        result = payload.get("result")
        if not isinstance(result, Mapping) or not isinstance(result.get("uids"), list):
            raise ValueError("expected ESummary JSON result.uids")
        papers, warnings = [], []
        for uid in result["uids"]:
            record = result.get(str(uid))
            if not isinstance(record, Mapping) or not isinstance(record.get("title"), str) or not record["title"].strip():
                warnings.append("summary_missing_pmid_or_title")
                continue
            doi = next((item.get("value") for item in record.get("articleids", [])
                        if isinstance(item, Mapping) and item.get("idtype") == "doi"), None)
            papers.append(ProviderPaper(
                "pubmed", str(uid), record["title"].strip(), pmid=str(uid), doi=doi,
                authors=[author["name"] for author in record.get("authors", []) if isinstance(author, Mapping) and author.get("name")],
                journal=record.get("fulljournalname"), source_url=f"https://pubmed.ncbi.nlm.nih.gov/{uid}/", channel="keyword",
                field_sources={"pmid": "PubMed ESummary JSON / uid", "title": "PubMed ESummary JSON / title",
                               "authors": "PubMed ESummary JSON / authors", "journal": "PubMed ESummary JSON / fulljournalname"},
                raw=dict(record),
            ))
        return papers, warnings

    parse_esearch = parse_search_response
    parse_efetch = parse_fetch_response
