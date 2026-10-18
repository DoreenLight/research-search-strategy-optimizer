import json
from pathlib import Path

import pytest

from research_search.providers.fusion_export import export_provider_fusion


def provider_result(provider, *, paper_id, title, doi, pmid=None, channel="keyword", discovery=False, request_count=1, raw_response=None, paper_raw=None):
    return {
        "provider": provider,
        "status": "success",
        "request_count": request_count,
        "reported_count": 10,
        "fetched_count": 1,
        "papers": [{
            "provider": provider,
            "paper_id": paper_id,
            "title": title,
            "doi": doi,
            "pmid": pmid,
            "s2_paper_id": paper_id if provider == "semantic_scholar" else None,
            "channel": channel,
            "discovery_channel": discovery,
            "seed_ids": ["seed-1"] if discovery else [],
            "candidate_reason": "semantic_recommendation" if discovery else None,
            "raw": paper_raw,
        }],
        "raw_response": raw_response if raw_response is not None else {"redacted": True},
        "query_type": channel,
        "query_hash": "qhash",
    }


def write_result(path: Path, payload: dict) -> Path:
    path.write_text(json.dumps(payload, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def test_offline_fusion_exports_provider_coverage_sources_and_conflicts(tmp_path):
    pubmed = write_result(tmp_path / "pubmed.json", provider_result(
        "pubmed", paper_id="123", title="Joint angle study", doi="10.1000/example", pmid="123"))
    s2 = write_result(tmp_path / "s2.json", provider_result(
        "semantic_scholar", paper_id="s2-a", title="Joint angle study", doi="https://doi.org/10.1000/EXAMPLE", pmid="123"))
    output = tmp_path / "fusion"

    report = export_provider_fusion([pubmed, s2], output)

    assert report["mode"] == "offline_fusion"
    assert report["new_network_request_count"] == 0
    assert report["historical_request_count"] == 2
    assert report["fusion"]["papers"]
    assert report["fusion"]["coverage_by_provider"]["pubmed"]["reported_count"] == 10
    assert report["fusion"]["coverage_by_provider"]["semantic_scholar"]["fetched_count"] == 1
    assert report["source_coverage"]["pubmed"]["query_types"] == ["keyword"]
    assert report["source_coverage"]["pubmed"]["deduplicated_count"] == 1
    source_record = json.loads((output / "source-records.jsonl").read_text().splitlines()[0])
    assert str(tmp_path) not in json.dumps(source_record)
    assert len(report["fusion"]["source_records"]) == 1
    assert (output / "fusion.json").is_file()
    assert (output / "papers.jsonl").is_file()
    assert (output / "source-records.jsonl").is_file()
    assert (output / "conflicts.jsonl").is_file()
    assert (output / "manifest.json").is_file()


def test_discovery_channel_remains_separate_from_keyword_retrieval(tmp_path):
    keyword = write_result(tmp_path / "keyword.json", provider_result(
        "pubmed", paper_id="123", title="Joint angle study", doi="10.1000/example", pmid="123"))
    discovery = write_result(tmp_path / "recommendation.json", provider_result(
        "semantic_scholar", paper_id="s2-a", title="Joint angle study", doi="10.1000/example", pmid="123",
        channel="semantic_recommendation", discovery=True, request_count=0))

    report = export_provider_fusion([keyword, discovery], tmp_path / "fusion")
    fused = report["fusion"]
    assert len(fused["retrieval_papers"]) == 1
    assert len(fused["discovery_papers"]) == 1
    assert fused["discovery_papers"][0]["discovery_channel"] is True
    assert fused["paper_channels"]


def test_export_rejects_invalid_provider_result_before_output(tmp_path):
    invalid = tmp_path / "invalid.json"
    invalid.write_text(json.dumps({"provider": "pubmed", "status": "success", "papers": "bad"}), encoding="utf-8")
    output = tmp_path / "fusion"

    with pytest.raises(ValueError):
        export_provider_fusion([invalid], output)
    assert not output.exists()


def test_export_does_not_overwrite_existing_directory(tmp_path):
    source = write_result(tmp_path / "source.json", provider_result(
        "pubmed", paper_id="123", title="Study", doi="10.1000/example", pmid="123"))
    output = tmp_path / "fusion"
    export_provider_fusion([source], output)
    before = (output / "fusion.json").read_bytes()

    with pytest.raises(FileExistsError):
        export_provider_fusion([source], output)
    assert (output / "fusion.json").read_bytes() == before
