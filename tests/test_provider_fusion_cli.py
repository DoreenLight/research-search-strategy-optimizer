import json

from research_search.cli import main


def test_provider_fusion_cli_is_offline_and_writes_audited_output(tmp_path):
    source = tmp_path / "result.json"
    source.write_text(json.dumps({
        "provider": "pubmed", "status": "success", "request_count": 1,
        "reported_count": 1, "fetched_count": 1,
        "papers": [{"provider": "pubmed", "paper_id": "1", "title": "Study", "pmid": "1"}],
    }))
    output = tmp_path / "fusion"
    assert main(["provider-fusion", str(source), "--output", str(output)]) == 0
    report = json.loads((output / "fusion.json").read_text())
    assert report["new_network_request_count"] == 0
    assert report["historical_request_count"] == 1
    assert json.loads((output / "manifest.json").read_text())["status"] == "completed"
