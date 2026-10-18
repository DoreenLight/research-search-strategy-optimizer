"""Offline P4 benchmarking; no retrieval, model calls, or implicit relevance labels.

Public API: run_benchmark(manifest: dict, output_dir: Path) -> dict.
The versioned input contract and review protocol are in
``docs/plans/p4-quality-protocol.md``. Only new output directories are accepted.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any
from urllib.parse import urlsplit

from .search_evaluator import compare_retrieval, evaluate_retrieval

__all__ = ["run_benchmark"]

_MODES = ("live", "replay", "synthetic")
_BASELINES = {"A", "B", "C", "D"}
_STATUSES = {"success", "partial", "failed", "not_executed", "planned"}
# ``pending`` is the public protocol spelling for 待审. ``uncertain`` is
# retained as a compatibility spelling used by search_evaluator.py.
_LABELS = {"relevant", "irrelevant", "pending", "uncertain"}
_DECISIVE = {"relevant", "irrelevant"}
_DOMAINS = {"mature", "emerging", "interdisciplinary", "medical"}
_FILES = ("benchmark.json", "benchmark.md", "review-queue.jsonl")


def _object(value: Any, allowed: set[str], required: set[str], where: str) -> None:
    if type(value) is not dict:
        raise ValueError(f"{where} must be an object")
    if any(type(key) is not str for key in value):
        raise ValueError(f"{where} keys must be strings")
    if required - value.keys():
        raise ValueError(f"{where} missing fields: {sorted(required - value.keys())}")
    if value.keys() - allowed:
        raise ValueError(f"{where} unknown fields: {sorted(value.keys() - allowed)}")


def _text(value: Any, where: str) -> None:
    if type(value) is not str or not value.strip() or any(ord(char) < 32 for char in value):
        raise ValueError(f"{where} must be a nonblank single-line string")


def _enum(value: Any, choices: set[str], where: str) -> None:
    if type(value) is not str or value not in choices:
        raise ValueError(f"{where} must be one of {sorted(choices)}")


def _count(value: Any, where: str, *, nullable: bool = False, positive: bool = False) -> None:
    if nullable and value is None:
        return
    if type(value) is not int or value < (1 if positive else 0):
        raise ValueError(f"{where} must be a {'positive' if positive else 'non-negative'} integer")


def _amount(value: Any, where: str) -> None:
    if value is None:
        return
    if type(value) not in {int, float} or not math.isfinite(value) or value < 0:
        raise ValueError(f"{where} must be a finite non-negative number or null")


def _ids(value: Any, where: str, *, nullable: bool = False, unique: bool = True) -> None:
    if nullable and value is None:
        return
    if type(value) is not list:
        raise ValueError(f"{where} must be an ID array{' or null' if nullable else ''}")
    for item in value:
        _text(item, f"{where} ID")
    if unique and len(set(value)) != len(value):
        raise ValueError(f"{where} contains duplicate IDs")


def _judgments(value: Any, where: str) -> None:
    if type(value) is not dict:
        raise ValueError(f"{where} must be an ID-to-label object, not an ID list")
    for paper_id, label in value.items():
        _text(paper_id, f"{where} ID")
        _enum(label, _LABELS, f"{where} label")


def _relative_path(value: Any, where: str) -> None:
    _text(value, where)
    parts = value.split("/")
    if ("\\" in value or ":" in value or PurePosixPath(value).is_absolute()
            or PureWindowsPath(value).drive or any(part in {"", ".", ".."} for part in parts)):
        raise ValueError(f"{where} is an unsafe relative path")


def _validate_run(run: Any, where: str) -> None:
    required = {"baseline_id", "status", "mode", "paper_ids", "request_count",
                "fetched_count", "deduplicated_count", "source_explanation"}
    strings = {"source_explanation", "run_id", "database", "source_type", "retrieved_at",
               "query", "error_type", "error_message"}
    allowed = required | strings | {"reported_count", "estimated_cost_usd", "screening_minutes",
                                    "raw_path", "source_url", "evidence_level"}
    _object(run, allowed, required, where)
    _enum(run["baseline_id"], _BASELINES, f"{where}.baseline_id")
    _enum(run["mode"], set(_MODES), f"{where}.mode")
    _enum(run["status"], _STATUSES, f"{where}.status")
    _ids(run["paper_ids"], f"{where}.paper_ids", unique=False)
    for field in ("request_count", "fetched_count", "deduplicated_count"):
        _count(run[field], f"{where}.{field}")
    _count(run.get("reported_count"), f"{where}.reported_count", nullable=True)
    for field in ("estimated_cost_usd", "screening_minutes"):
        _amount(run.get(field), f"{where}.{field}")
    for field in strings & run.keys():
        _text(run[field], f"{where}.{field}")
    if run["deduplicated_count"] != len(set(run["paper_ids"])):
        raise ValueError(f"{where}.deduplicated_count must equal unique paper_ids")
    if run["deduplicated_count"] > run["fetched_count"]:
        raise ValueError(f"{where}.deduplicated_count cannot exceed fetched_count")
    if run["mode"] != "live" and run["request_count"] != 0:
        raise ValueError(f"{where} offline mode cannot claim new requests")
    if run["status"] in {"planned", "not_executed"}:
        if any(run[key] != 0 for key in ("request_count", "fetched_count", "deduplicated_count")):
            raise ValueError(f"{where} not_executed/planned counts must be explicitly zero")
        if any(run.get(key) not in {None, 0} for key in ("estimated_cost_usd", "screening_minutes")):
            raise ValueError(f"{where} not_executed/planned cannot claim incurred cost or screening")
    if run["mode"] == "live" and run["status"] == "success" and run["request_count"] == 0:
        raise ValueError(f"{where} live success must record at least one request")
    if run.get("raw_path") is not None:
        _relative_path(run["raw_path"], f"{where}.raw_path")
    if run.get("source_url") is not None:
        _text(run["source_url"], f"{where}.source_url")
        url = urlsplit(run["source_url"])
        if url.scheme not in {"https", "http"} or not url.netloc or url.username or url.password:
            raise ValueError(f"{where}.source_url must be a public HTTP(S) locator without credentials")
    if "evidence_level" in run:
        _enum(run["evidence_level"], {"A", "B", "C", "U"}, f"{where}.evidence_level")


def _validate_manifest(manifest: Any) -> None:
    counts = {"planned_case_count", "planned_run_count", "theoretical_search_space_size",
              "historical_run_count", "retained_configuration_count"}
    allowed = {"schema_version", "benchmark_id", "k", "comparison_baseline_id", "cases",
               "training_seed_ids", "test_reference_ids", "notes"} | counts
    _object(manifest, allowed, {"cases"}, "manifest")
    if "schema_version" in manifest and manifest["schema_version"] != "0.1":
        raise ValueError("manifest.schema_version must be 0.1")
    _count(manifest.get("k", 20), "manifest.k", positive=True)
    _enum(manifest.get("comparison_baseline_id", "A"), _BASELINES, "comparison_baseline_id")
    for field in counts & manifest.keys():
        _count(manifest[field], f"manifest.{field}", nullable=True)
    for field in {"benchmark_id", "notes"} & manifest.keys():
        _text(manifest[field], f"manifest.{field}")
    training: set[str] = set()
    test: set[str] = set()
    for field, target in (("training_seed_ids", training), ("test_reference_ids", test)):
        _ids(manifest.get(field, []), f"manifest.{field}")
        target.update(manifest.get(field, []))
    cases = manifest["cases"]
    if type(cases) is not list or not cases:
        raise ValueError("manifest.cases must be a non-empty array")
    case_ids: set[str] = set()
    required = {"case_id", "domain_kind", "split", "reference_set", "human_judgments", "runs"}
    allowed = required | {"model_judgments", "training_seed_ids", "test_reference_ids",
                          "existing_catalog_ids", "reference_set_independent", "reference_set_source",
                          "case_fixture", "notes"}
    for index, case in enumerate(cases):
        where = f"cases[{index}]"
        _object(case, allowed, required, where)
        _text(case["case_id"], f"{where}.case_id")
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", case["case_id"]):
            raise ValueError(f"{where}.case_id is unsafe")
        if case["case_id"] in case_ids:
            raise ValueError("duplicate case_id")
        case_ids.add(case["case_id"])
        _enum(case["domain_kind"], _DOMAINS, f"{where}.domain_kind")
        _enum(case["split"], {"discovery", "test"}, f"{where}.split")
        _ids(case["reference_set"], f"{where}.reference_set", nullable=True)
        _judgments(case["human_judgments"], f"{where}.human_judgments")
        _judgments(case.get("model_judgments", {}), f"{where}.model_judgments")
        for field in ("training_seed_ids", "test_reference_ids", "existing_catalog_ids"):
            _ids(case.get(field, []), f"{where}.{field}")
        training.update(case.get("training_seed_ids", []))
        test.update(case.get("test_reference_ids", []))
        (test if case["split"] == "test" else training).update(case["reference_set"] or [])
        if "reference_set_independent" in case and type(case["reference_set_independent"]) is not bool:
            raise ValueError(f"{where}.reference_set_independent must be boolean")
        for field in {"reference_set_source", "notes"} & case.keys():
            _text(case[field], f"{where}.{field}")
        if case.get("reference_set_independent"):
            if case["split"] != "test" or case["reference_set"] is None or not case.get("reference_set_source"):
                raise ValueError(f"{where} independent reference requires test split, reference_set and source")
            if any(case["human_judgments"].get(pid) in {"irrelevant", "uncertain", "pending"}
                   for pid in case["reference_set"]):
                raise ValueError(f"{where} human judgment conflicts with independent reference")
        if "case_fixture" in case:
            _relative_path(case["case_fixture"], f"{where}.case_fixture")
        if type(case["runs"]) is not list:
            raise ValueError(f"{where}.runs must be an array")
        run_ids: set[str] = set()
        for run_index, run in enumerate(case["runs"]):
            _validate_run(run, f"{where}.runs[{run_index}]")
            if "run_id" in run:
                if run["run_id"] in run_ids:
                    raise ValueError(f"{where} duplicate run_id")
                run_ids.add(run["run_id"])
    if training & test:
        raise ValueError("split leakage: training_seed/discovery reference IDs overlap test reference IDs")


def _json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n"


def _input_hash(manifest: dict[str, Any]) -> str:
    canonical = json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _stats(runs: list[dict[str, Any]]) -> dict[str, dict[str, int]]:
    result = {}
    for mode in _MODES:
        subset = [run for run in runs if run["mode"] == mode]
        result[mode] = {
            "registered_run_count": len(subset),
            "executed_run_count": sum(run["status"] in {"success", "partial", "failed"} for run in subset),
            "successful_run_count": sum(run["status"] == "success" for run in subset),
            "failed_run_count": sum(run["status"] == "failed" for run in subset),
            "partial_run_count": sum(run["status"] == "partial" for run in subset),
            "not_executed_run_count": sum(run["status"] in {"planned", "not_executed"} for run in subset),
            "request_count": sum(run["request_count"] for run in subset),
        }
    return result


def _sum_known(runs: list[dict[str, Any]], field: str) -> float | int | None:
    values = [run.get(field) for run in runs]
    return sum(values) if all(value is not None for value in values) else None


def _group_runs(case: dict[str, Any], k: int) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for run in case["runs"]:
        groups.setdefault((run["baseline_id"], run["mode"]), []).append(run)
    reference = (set(case["reference_set"]) if case["split"] == "test"
                 and case.get("reference_set_independent") else None)
    labels = {pid: ("uncertain" if label == "pending" else label)
              for pid, label in case["human_judgments"].items()}
    results = []
    for (baseline_id, mode), source_runs in groups.items():
        statuses = {run["status"] for run in source_runs}
        status = next(iter(statuses)) if len(statuses) == 1 else "partial"
        eligible = status == "success"
        paper_ids = [pid for run in source_runs for pid in run["paper_ids"]]
        unique_ids = list(dict.fromkeys(paper_ids))
        fetched = sum(run["fetched_count"] for run in source_runs)
        metrics = (evaluate_retrieval(paper_ids, reference, fetched, len(unique_ids), k,
                                      relevance_labels=labels).to_dict() if eligible else None)
        # The shared helper keeps partial labels out of precision, but its
        # ``relevant_found`` field can be 0 when the supplied label mapping is
        # non-empty yet no top-K item has a decisive label.  At benchmark level
        # that is unknown, never a measured zero.
        if metrics is not None and reference is None and metrics["judged_count"] == 0:
            metrics["relevant_found"] = None
        item = {
            "baseline_id": baseline_id, "mode": mode, "status": status,
            "source_record_count": len(source_runs), "source_records": source_runs,
            "eligible_for_metrics": eligible, "real_evidence": eligible and mode == "live",
            "real_advantage_eligible": False,
            "human_labels_used": eligible and any(pid in labels and labels[pid] in _DECISIVE for pid in unique_ids),
            "model_labels_present": bool(case.get("model_judgments")), "model_labels_used": False,
            "paper_ids": unique_ids, "observed_unique_count": len(unique_ids),
            "total_unique_count": len(unique_ids) if eligible else None,
            "fetched_count": fetched, "deduplicated_count": len(unique_ids),
            "request_count": sum(run["request_count"] for run in source_runs),
            "reported_count": source_runs[0].get("reported_count") if len(source_runs) == 1 else None,
            "reported_counts_by_source": [{"source_record_index": i, "database": run.get("database"),
                                            "reported_count": run.get("reported_count")}
                                           for i, run in enumerate(source_runs)],
            "estimated_cost_usd": _sum_known(source_runs, "estimated_cost_usd"),
            "screening_minutes": _sum_known(source_runs, "screening_minutes"),
            "metrics": metrics,
            "known_relevant_hits_at_k": (metrics["reference_hits_at_k"] if reference is not None else
                                          metrics["relevant_found"] if metrics["judged_count"] else None)
                                         if metrics else None,
            "reference_hits_at_k": metrics["reference_hits_at_k"] if metrics else None,
            "recall_at_k": metrics["recall_at_k"] if metrics else None,
            "precision_at_k": metrics["precision_at_k"] if metrics else None,
            "judged_count": metrics["judged_count"] if metrics else None,
            "unjudged_count": metrics["unjudged_count"] if metrics else None,
            "relevance_basis": ("independent_test_reference" if reference is not None else
                                "human_labels_only" if any(label in _DECISIVE for label in labels.values()) else
                                "unavailable"),
        }
        results.append(item)
    return results


def _case_report(case: dict[str, Any], k: int, baseline_id: str) -> dict[str, Any]:
    runs = _group_runs(case, k)
    anchors = {run["mode"]: run for run in runs if run["baseline_id"] == baseline_id and run["eligible_for_metrics"]}
    for run in runs:
        anchor = anchors.get(run["mode"])
        available = run["eligible_for_metrics"] and anchor is not None
        comparison = (compare_retrieval(anchor["paper_ids"] + case.get("existing_catalog_ids", []),
                                        run["paper_ids"], case["human_judgments"]) if available else None)
        new = comparison["new_ids"] if comparison else None
        confirmed = (len(comparison["new_relevant_ids"]) if not new or any(
            case["human_judgments"].get(pid) in _DECISIVE for pid in new) else None) if comparison else None
        cost = run["estimated_cost_usd"]
        run.update({
            "comparison_baseline_id": baseline_id,
            "comparison_available": available,
            "new_unique_ids": new,
            "new_unique_count": len(new) if new is not None else None,
            "confirmed_new_relevant_ids": comparison["new_relevant_ids"] if comparison else None,
            "confirmed_new_relevant_count": confirmed,
            "unjudged_new_count": comparison["unjudged_new_count"] if comparison else None,
            "new_relevance_complete": comparison["unjudged_new_count"] == 0 if comparison else None,
            "existing_catalog_overlap_count": len(set(run["paper_ids"]) & set(case.get("existing_catalog_ids", [])))
                                              if run["eligible_for_metrics"] else None,
            "cost_per_incremental_confirmed_relevant_usd": cost / confirmed
                if cost is not None and confirmed is not None and confirmed > 0 else None,
            "cost_basis": "candidate_total_cost_not_candidate_minus_anchor",
            "gain_attribution": "strategy_version_not_individual_terms",
            "real_advantage_eligible": bool(run["mode"] == "live" and available and confirmed is not None
                                            and confirmed > 0 and comparison["unjudged_new_count"] == 0),
        })
    return {
        "case_id": case["case_id"], "domain_kind": case["domain_kind"], "split": case["split"],
        "reference_set_used_for_recall": case["split"] == "test" and bool(case.get("reference_set_independent")),
        "human_judgments": case["human_judgments"], "model_judgments": case.get("model_judgments", {}),
        "mode_stats": _stats(case["runs"]), "runs": runs,
    }


def _queue(cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result = []
    for case in cases:
        paper_ids = dict.fromkeys(pid for run in case["runs"] for pid in run["paper_ids"])
        for pid in paper_ids:
            label = case["human_judgments"].get(pid)
            if label not in _DECISIVE:
                result.append({
                    "review_id": hashlib.sha256(f"{case['case_id']}\0{pid}".encode("utf-8")).hexdigest()[:20],
                    "case_id": case["case_id"], "domain_kind": case["domain_kind"], "split": case["split"],
                    "paper_id": pid, "human_label": label, "review_status": "pending",
                })
    return result


def _cell(value: Any) -> str:
    if value is None:
        return "未知 / 不可用"
    return str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def _markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# P4 质量基准与人工审阅报告", "",
        "这是离线汇总，不发起请求，也不自动宣告策略优势或产品化。live 为输入声明，未在本次评测中重新联网验证。",
        "未知、不适用和未审阅均不按 0 或负例处理。synthetic 仅供工程验证，replay 只复用历史记录。", "",
        f"- 预计划 case 数：{_cell(report['planned_case_count'])}；本次输入 case 数：{report['actual_case_count']}。",
        f"- 实际登记执行记录：{summary['actual_executed_run_count']}；live 成功记录：{summary['real_successful_run_count']}。",
        f"- 输入记录中的新增 live 请求：{summary['actual_live_request_count']}；本评测函数新增联网请求：0。",
        f"- 待人工审阅：{summary['pending_review_count']}；K={report['k']}；比较锚点：{report['comparison_baseline_id']}（同 mode）。", "",
        "## 分模式执行账本", "",
        "| 模式 | 登记 | 已执行 | 成功 | 失败 | partial | 未执行 | 新请求 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for mode, stats in summary["mode_stats"].items():
        fields = ("registered_run_count", "executed_run_count", "successful_run_count", "failed_run_count",
                  "partial_run_count", "not_executed_run_count", "request_count")
        lines.append("| " + " | ".join([mode] + [str(stats[field]) for field in fields]) + " |")
    lines += ["", "## 分 case、baseline、mode 比较", "",
              "total_unique 仅来自成功组内 ID 并集；多库 reported_count 不相加。不同 mode 永不互作比较锚点。",
              "一个组含失败、未执行或 partial 来源时，保留原记录，但整组不计质量或增量收益。", "",
              "| Case / 类别 / split | Baseline / mode | 状态 | reported_count | total_unique | new_unique | K 内已知相关 | Recall@K | P@K | 成本 USD | 每新增确认相关成本 USD | 筛选分钟 |",
              "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for case in report["cases"]:
        if not case["runs"]:
            lines.append(f"| {case['case_id']} / {case['domain_kind']} / {case['split']} | 无记录 | not_executed | — | — | — | — | — | — | — | — | — |")
        for run in case["runs"]:
            fields = [f"{case['case_id']} / {case['domain_kind']} / {case['split']}",
                      f"{run['baseline_id']} / {run['mode']}", run["status"], run["reported_count"],
                      run["total_unique_count"], run["new_unique_count"], run["known_relevant_hits_at_k"],
                      run["recall_at_k"], run["precision_at_k"], run["estimated_cost_usd"],
                      run["cost_per_incremental_confirmed_relevant_usd"], run["screening_minutes"]]
            lines.append("| " + " | ".join(_cell(value) for value in fields) + " |")
    lines += ["", "## 来源与解释", "",
              "| Case | Baseline / mode | 来源 | 状态 | 单来源 reported_count | 来源说明 |",
              "|---|---|---|---|---:|---|"]
    for case in report["cases"]:
        for group in case["runs"]:
            for source in group["source_records"]:
                fields = [case["case_id"], f"{group['baseline_id']} / {group['mode']}", source.get("database"),
                          source["status"], source.get("reported_count"), source["source_explanation"]]
                lines.append("| " + " | ".join(_cell(value) for value in fields) + " |")
    lines += ["", "## 指标边界与审阅", "",
              "- Recall 仅对显式独立、有来源说明的 test reference_set；discovery 或只给 ID 的集合不形成召回率。",
              "- P@K 只在前 K 个去重结果全部有人工 relevant/irrelevant 标签且确有 K 个结果时计算；uncertain 不作负例。",
              "- K 内已知相关是独立测试集命中，或人工已确认命中的下界；不是全部相关文献估计。模型标签从不进入质量指标。",
              "- new_unique 相对同 mode 锚点与 existing_catalog_ids 的并集；缺少成功锚点则未知。A 对自身新增为 0。",
              "- 每新增确认相关成本 = 候选组全部已知成本 / 人工确认新增相关数；不是候选减锚点的成本差。未知成本、无确认新增均为空。",
              "- review-queue.jsonl 不含 baseline、mode 或模型判断；审阅员应在单独盲化材料中审阅，再由协调人回填标签。",
              "- PRESS/PRISMA-S 是审查与报告指针，不是本实现获得合规认证。协议：docs/plans/p4-quality-protocol.md。", ""]
    return "\n".join(lines)


def _check_output(output_dir: Path) -> None:
    if not isinstance(output_dir, Path) or not output_dir.parts or ".." in output_dir.parts:
        raise ValueError("output_dir must be a concrete pathlib.Path without traversal")
    if any(path.is_symlink() for path in (output_dir, *output_dir.parents)):
        raise ValueError("output path cannot contain symlinks")
    if output_dir.exists():
        raise FileExistsError(f"refusing to overwrite existing output: {output_dir}")


def run_benchmark(manifest: dict, output_dir: Path) -> dict:
    """Validate and summarize supplied observations; create four hashed local files.

    Raises ValueError for invalid input or unsafe paths, FileExistsError if the
    destination exists, and OSError for filesystem errors. No input paths are
    opened. Validation and serialization finish before creating the destination.
    """
    _validate_manifest(manifest)
    _check_output(output_dir)
    # Snapshot caller-owned input without mutating it; canonical hashing is stable.
    snapshot = json.loads(_json(manifest))
    k = snapshot.get("k", 20)
    baseline_id = snapshot.get("comparison_baseline_id", "A")
    cases = snapshot["cases"]
    source_runs = [run for case in cases for run in case["runs"]]
    queue = _queue(cases)
    stats = _stats(source_runs)
    planned_count = snapshot.get("planned_case_count")
    report = {
        "schema_version": "0.1", "benchmark_id": snapshot.get("benchmark_id"),
        "scope": "offline_benchmark_and_human_review_not_productization",
        "k": k, "comparison_baseline_id": baseline_id,
        "planned_case_count": planned_count, "actual_case_count": len(cases),
        "case_count_match": planned_count == len(cases) if planned_count is not None else None,
        "planned_run_count": snapshot.get("planned_run_count"),
        "theoretical_search_space_size": snapshot.get("theoretical_search_space_size"),
        "historical_run_count": snapshot.get("historical_run_count"),
        "retained_configuration_count": snapshot.get("retained_configuration_count"),
        "input_manifest_sha256": _input_hash(snapshot), "input_manifest": snapshot,
        "summary": {
            "mode_stats": stats,
            "registered_run_count": len(source_runs),
            "actual_executed_run_count": sum(item["executed_run_count"] for item in stats.values()),
            "actual_executed_case_count": sum(any(run["status"] in {"success", "partial", "failed"}
                                                   for run in case["runs"]) for case in cases),
            "real_successful_case_count": sum(any(run["mode"] == "live" and run["status"] == "success"
                                                   for run in case["runs"]) for case in cases),
            "real_successful_run_count": stats["live"]["successful_run_count"],
            "actual_live_request_count": stats["live"]["request_count"],
            "benchmark_new_request_count": 0,
            "pending_review_count": len(queue),
            "real_advantage_demonstrated": False,
        },
        "cases": [_case_report(case, k, baseline_id) for case in cases],
    }
    contents = {
        "benchmark.json": _json(report),
        "benchmark.md": _markdown(report),
        "review-queue.jsonl": "".join(json.dumps(item, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n" for item in queue),
    }
    hash_manifest = {
        "schema_version": "0.1", "status": "completed", "algorithm": "sha256",
        "input_manifest_sha256": report["input_manifest_sha256"],
        "files": {name: hashlib.sha256(contents[name].encode("utf-8")).hexdigest() for name in _FILES},
    }
    contents["manifest.jsonsha256"] = _json(hash_manifest)
    output_dir.mkdir(parents=True, exist_ok=False)
    for name, content in contents.items():
        with (output_dir / name).open("x", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
    return report
