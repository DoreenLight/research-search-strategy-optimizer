import json
from pathlib import Path

from research_search.cli import main


def test_cli_build_query_writes_three_strategy_plans(tmp_path, capsys):
    groups_path = tmp_path / "groups.json"
    groups_path.write_text(
        json.dumps([
            {"group_id": "input", "label": "Input", "terms": ["sEMG"]},
            {"group_id": "object", "label": "Object", "terms": ["joint angle"]},
            {"group_id": "task", "label": "Task", "terms": ["estimation"]},
        ]),
        encoding="utf-8",
    )

    assert main(["build-query", str(groups_path)]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert len(payload) == 3
    assert payload[0]["strategy"] == "exploratory"


def test_cli_evaluate_keeps_recall_unavailable_without_reference_set(tmp_path, capsys):
    returned_path = tmp_path / "returned.json"
    returned_path.write_text('["a", "b"]', encoding="utf-8")

    assert main([
        "evaluate",
        str(returned_path),
        "--fetched-count",
        "2",
        "--deduplicated-count",
        "2",
        "--k",
        "2",
    ]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["returned_count"] == 2
    assert payload["recall_at_k"] is None
