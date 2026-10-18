"""P1 auditable optimization sessions over versioned Research Search Packages."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .iteration_optimizer import compare_strategy_versions, should_stop
from .openalex_client import OpenAlexSearchResult
from .search_evaluator import evaluate_retrieval
from .validation import validate_case
from .query_builder import build_strategy_plans
from .workflow import _concept_groups, _snapshot_by_strategy, run_package


def _dump(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _case_fingerprint(case: dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(case, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:16]


def _scope_signature(case: dict[str, Any]) -> dict[str, Any]:
    scope = case["research_scope"]
    return {key: scope.get(key) for key in ("description", "research_object", "input_modality", "research_task", "method", "application", "constraints", "unspecified")}


def _concept_diff(parent: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    parent_groups = {item["group_id"]: item for item in parent["concept_groups"]}
    candidate_groups = {item["group_id"]: item for item in candidate["concept_groups"]}
    changed: list[str] = []
    added: dict[str, list[str]] = {}
    removed: dict[str, list[str]] = {}
    for group_id in sorted(set(parent_groups) | set(candidate_groups)):
        before = set(parent_groups.get(group_id, {}).get("terms", []))
        after = set(candidate_groups.get(group_id, {}).get("terms", []))
        if before != after:
            changed.append(group_id)
            if after - before:
                added[group_id] = sorted(after - before)
            if before - after:
                removed[group_id] = sorted(before - after)
    return {"changed_groups": changed, "added_terms": added, "removed_terms": removed}


def _resolve_labels(round_config: dict[str, Any]) -> tuple[dict[str, str], dict[str, str], list[str]]:
    allowed = {"relevant", "irrelevant", "uncertain"}
    human_values: dict[str, set[str]] = {}
    model: dict[str, str] = {}
    for item in round_config.get("judgments", []):
        paper_id = item.get("paper_id")
        label = item.get("label")
        if not isinstance(paper_id, str) or label not in allowed:
            raise ValueError("invalid optimization judgment")
        if item.get("judge_type") == "human":
            human_values.setdefault(paper_id, set()).add(label)
        elif item.get("judge_type") == "model":
            model[paper_id] = label
        else:
            raise ValueError("judge_type must be human or model")
    conflicts = sorted(paper_id for paper_id, labels in human_values.items() if len(labels) > 1)
    human = {paper_id: next(iter(labels)) if len(labels) == 1 else "uncertain" for paper_id, labels in human_values.items()}
    return human, model, conflicts


def _precision_gate(package_dir: Path, labels: dict[str, str], k: int, minimum: float) -> dict[str, Any]:
    runs = [json.loads(line) for line in (package_dir / "05-search-runs.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    results = []
    for run in runs:
        if run["status"] not in {"success", "partial"}:
            continue
        metrics = evaluate_retrieval(run["paper_ids"], None, run["fetched_count"], run["deduplicated_count"],
                                     k, relevance_labels=labels)
        results.append({"plan_id": run["plan_id"], "precision_at_k": metrics.precision_at_k,
                        "judged_precision": metrics.judged_precision, "effective_k": metrics.effective_k})
    known = bool(results) and all(item["precision_at_k"] is not None for item in results)
    return {"k": k, "minimum": minimum, "strategies": results,
            "passed": all(item["precision_at_k"] >= minimum for item in results) if known else None}


def _ids_from_package(package_dir: Path) -> list[str]:
    path = package_dir / "04-papers.jsonl"
    if not path.exists():
        return []
    return [json.loads(line)["paper_id"] for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


class _SessionBudgetClient:
    """Share a request ceiling across all plans in one optimization session."""

    def __init__(self, client: Any, remaining: int) -> None:
        self.client = client
        self.remaining = remaining
        self.request_count = 0

    def search_works(self, search: str, *, per_page: int, filters: dict[str, str] | None = None) -> Any:
        if self.remaining <= 0:
            return OpenAlexSearchResult(status="failed", error_type="budget_exhausted",
                                        error_message="optimization session request budget exhausted")
        original_budget = getattr(self.client, "max_requests", None)
        made = getattr(self.client, "_requests_made", 0)
        if hasattr(self.client, "max_requests"):
            ceiling = made + self.remaining
            self.client.max_requests = min(original_budget, ceiling) if original_budget is not None else ceiling
        try:
            result = self.client.search_works(search, per_page=per_page, filters=filters)
        finally:
            if hasattr(self.client, "max_requests"):
                self.client.max_requests = original_budget
        used = int(getattr(result, "request_count", 0) or 0)
        self.remaining -= used
        self.request_count += used
        return result


def _write_manifest(output_dir: Path, metadata: dict[str, Any]) -> None:
    files = {
        str(path.relative_to(output_dir)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(output_dir.rglob("*"))
        if path.is_file() and path != output_dir / "manifest.json"
    }
    _dump(output_dir / "manifest.json", {**metadata, "files": files})


def run_optimization(
    config: dict[str, Any],
    output_dir: Path,
    *,
    client: Any | None = None,
    per_page: int = 10,
) -> dict[str, Any]:
    if not isinstance(config, dict) or not isinstance(config.get("session_id"), str) or not isinstance(config.get("rounds"), list):
        raise ValueError("optimization config requires session_id and rounds")
    max_rounds = config.get("max_rounds", len(config["rounds"]))
    max_requests = config.get("max_requests", 0)
    precision_k = config.get("precision_k", 10)
    min_precision = config.get("min_precision_at_k", 0.5)
    cost_budget = config.get("cost_budget_usd")
    if cost_budget is not None and (type(cost_budget) not in (int, float) or cost_budget < 0):
        raise ValueError("cost_budget_usd must be non-negative or null")
    if type(precision_k) is not int or precision_k <= 0:
        raise ValueError("precision_k must be a positive integer")
    if type(min_precision) not in (int, float) or not 0 <= min_precision <= 1:
        raise ValueError("min_precision_at_k must be in [0,1]")
    if type(max_rounds) is not int or max_rounds <= 0 or type(max_requests) is not int or max_requests < 0:
        raise ValueError("invalid optimization budget")
    if type(per_page) is not int or not 1 <= per_page <= 100:
        raise ValueError("per_page must be between 1 and 100")
    if output_dir.exists():
        raise FileExistsError(f"output directory already exists: {output_dir}")
    rounds = config["rounds"][:max_rounds]
    if not rounds:
        raise ValueError("at least one round is required")
    # Validate every case before creating output so a malformed later round leaves no partial session.
    for round_config in rounds:
        if not isinstance(round_config, dict) or not isinstance(round_config.get("case"), dict):
            raise ValueError("each round requires a case")
        validate_case(round_config["case"])
    baseline_scope = _scope_signature(rounds[0]["case"])
    for round_config in rounds:
        if round_config.get("snapshots") is not None:
            plans = build_strategy_plans(_concept_groups(round_config["case"]))
            _snapshot_by_strategy(round_config["snapshots"], plans)
    for index, round_config in enumerate(rounds):
        if _scope_signature(round_config["case"]) != baseline_scope:
            raise ValueError("scope drift is not an iteration; create a new research case")
        if index and not round_config.get("reviewed_by"):
            raise ValueError("each non-baseline round needs review before execution")
        relationship = round_config.get("change_relationship", "baseline")
        allowed_relationships = {"equivalent", "broader", "narrower", "related_task", "alternative_method", "application", "unclassified"}
        if index and relationship not in allowed_relationships:
            raise ValueError("candidate relationship must be explicitly classified")
        drift = round_config.get("drift_rate")
        if drift is not None and (type(drift) not in (int, float) or not 0 <= drift <= 1):
            raise ValueError("drift_rate must be in [0,1] or null")
        if index and relationship in {"broader", "narrower", "related_task", "alternative_method", "application"} and not round_config.get("separate_branch", False):
            raise ValueError("broader or related changes require a separate branch")
        if index:
            parent = rounds[index - 1]["case"]
            diff = _concept_diff(parent, round_config["case"])
            if len(diff["changed_groups"]) > 1:
                raise ValueError("one concept group may change in each round")
        if index and round_config.get("snapshots") is None and client is None:
            raise ValueError("candidate round needs snapshots or a live client")
        _resolve_labels(round_config)

    output_dir.mkdir(parents=True)
    history: list[dict[str, Any]] = []
    total_requests = 0
    active_version = 0
    active_case = rounds[0]["case"]
    active_ids: list[str] = []
    active_relevant_ids: set[str] = set()
    candidate_version: int | None = None
    rollback_version: int | None = None
    stop_reason = "continue"
    executed_round_count = 0
    replayed_round_count = 0
    live_budget = _SessionBudgetClient(client, max_requests) if client is not None else None

    for index, round_config in enumerate(rounds):
        is_baseline = index == 0
        parent_version = None if is_baseline else active_version
        difference = {"changed_groups": [], "added_terms": {}, "removed_terms": {}} if is_baseline else _concept_diff(active_case, round_config["case"])
        if len(difference["changed_groups"]) > 1:
            raise ValueError("one concept group may change in each round")
        snapshot = round_config.get("snapshots")
        if snapshot is None and total_requests >= max_requests and client is not None:
            stop_reason = "budget_exhausted"
            break
        round_dir = output_dir / f"round-{index:02d}"
        if snapshot is not None:
            package_summary = run_package(round_config["case"], round_dir, snapshots=snapshot, per_page=per_page)
            replayed_round_count += 1
        else:
            package_summary = run_package(round_config["case"], round_dir, client=live_budget, per_page=per_page)
        round_requests = package_summary["request_count"]
        total_requests += round_requests
        if round_requests > 0:
            executed_round_count += 1
        current_ids = _ids_from_package(round_dir)
        human, model, conflicts = _resolve_labels(round_config)
        comparison = None if is_baseline else compare_strategy_versions(
            active_ids, current_ids, human_labels=human, model_labels=model
        )
        decision = "baseline"
        confirmed_gain: int | None = None
        lost_relevant_ids: list[str] = []
        estimated_cost = round_config.get("estimated_cost_usd")
        if estimated_cost is not None and (type(estimated_cost) not in (int, float) or estimated_cost < 0):
            raise ValueError("estimated_cost_usd must be non-negative or null")
        cost_gate = {"budget_usd": cost_budget, "estimated_cost_usd": estimated_cost,
                     "known": estimated_cost is not None,
                     "passed": True if cost_budget is None else (
                         estimated_cost is not None and estimated_cost <= cost_budget)}
        if not is_baseline:
            rollback_version = active_version
        precision_gate = _precision_gate(round_dir, human, precision_k, min_precision)
        if is_baseline:
            active_case = round_config["case"]
            active_ids = current_ids
            active_relevant_ids = {paper_id for paper_id, label in human.items() if label == "relevant" and paper_id in current_ids}
            if package_summary["status"] in {"failed", "partial"}:
                decision = "execution_partial"
                active_version = None
                stop_reason = "execution_failed" if total_requests < max_requests else "budget_exhausted"
        elif package_summary["status"] in {"failed", "partial"}:
            decision = "execution_failed"
            stop_reason = "execution_failed" if total_requests < max_requests else "budget_exhausted"
        else:
            new_ids = comparison["new_ids"]
            lost_relevant_ids = sorted(active_relevant_ids - set(current_ids))
            lost_relabelled = sorted(paper_id for paper_id in active_relevant_ids if human.get(paper_id) == "irrelevant")
            lost_relevant_ids = sorted(set(lost_relevant_ids + lost_relabelled))
            new_unjudged = [paper_id for paper_id in new_ids if human.get(paper_id) not in {"relevant", "irrelevant"}]
            synthetic = snapshot is not None and snapshot.get("snapshot_kind") == "synthetic_test_fixture"
            labels_complete = not synthetic and bool(human) and not new_unjudged and not conflicts
            confirmed_gain = sum(human.get(paper_id) == "relevant" for paper_id in new_ids) if labels_complete else None
            drifted = round_config.get("drift_rate") is not None and float(round_config["drift_rate"]) >= 0.6
            if drifted:
                decision = "rollback_to_previous"
                stop_reason = "semantic_drift_alarm"
            elif round_config.get("separate_branch", False):
                decision = "branch_only"
            elif lost_relevant_ids or confirmed_gain == 0 or precision_gate["passed"] is False or (cost_gate["passed"] is False and cost_gate["known"]):
                decision = "rollback_to_previous"
            elif synthetic or not human or conflicts or new_unjudged or precision_gate["passed"] is not True or cost_gate["passed"] is not True or round_config.get("change_relationship") == "unclassified":
                decision = "pending_review"
                candidate_version = index
                stop_reason = "awaiting_human_judgments"
            elif confirmed_gain > 0:
                decision = "retain"
                active_case = round_config["case"]
                active_ids = current_ids
                active_relevant_ids = (active_relevant_ids & set(current_ids)) | {
                    paper_id for paper_id, label in human.items() if label == "relevant" and paper_id in current_ids
                }
                active_version = index
                candidate_version = None
            else:
                decision = "rollback_to_previous"
                rollback_version = active_version
        history.append({
            "round_index": index, "version": index, "parent_version": parent_version,
            "candidate_version": index if not is_baseline else None,
            "case_fingerprint": _case_fingerprint(round_config["case"]),
            "rationale": round_config.get("rationale", ""), "reviewed_by": round_config.get("reviewed_by"),
            "relationship": round_config.get("change_relationship", "baseline"), "package_status": package_summary["status"],
            "request_count": round_requests, "comparison": comparison, "confirmed_gain": confirmed_gain,
            "human_confirmed_relevant_ids": comparison["new_relevant_ids"] if comparison else [],
            "lost_relevant_ids": lost_relevant_ids, "human_label_conflicts": conflicts, "decision": decision,
            "changed_groups": difference["changed_groups"], "added_terms": difference["added_terms"],
            "removed_terms": difference["removed_terms"], "evidence_ids": round_config.get("evidence_paper_ids", []),
            "precision_gate": precision_gate, "cost_gate": cost_gate, "estimated_cost_usd": estimated_cost,
            "drift_rate": round_config.get("drift_rate"),
            "new_terms": round_config.get("new_terms", []), "coverage_claim": "not_proven_complete",
        })
        if stop_reason in {"awaiting_human_judgments", "execution_failed", "semantic_drift_alarm"}:
            break
        if client is not None and total_requests >= max_requests:
            stop_reason = "budget_exhausted"
            break

    if not history:
        stop_reason = "budget_exhausted" if client is not None else "plan_only"
    elif stop_reason == "continue":
        if client is None and all(item.get("request_count", 0) == 0 for item in history):
            stop_reason = "plan_only"
        else:
            stop_result = should_stop(
                [{"new_relevant_count": item["confirmed_gain"], "new_term_count": len(item["new_terms"]), "drift_rate": None} for item in history],
                budget_remaining=max(0, max_requests - total_requests),
                branches_remaining=config.get("branches_remaining", 0),
            )
            stop_reason = stop_result["reason"]

    summary = {
        "session_id": config["session_id"], "status": "complete", "total_request_count": total_requests,
        "request_count": total_requests, "actual_round_count": len(history), "executed_round_count": executed_round_count,
        "replayed_round_count": replayed_round_count,
        "current_version": len(history) - 1, "active_version": active_version,
        "candidate_version": candidate_version, "rollback_version": rollback_version, "stop_reason": stop_reason,
        "coverage_claim": "not_proven_complete",
    }
    if active_version is None or stop_reason == "execution_failed":
        summary["status"] = "failed"
    elif stop_reason == "awaiting_human_judgments":
        summary["status"] = "pending_review"
    _dump(output_dir / "history.json", history)
    _dump(output_dir / "summary.json", summary)
    _dump(output_dir / "active-case.json", active_case)
    _dump(output_dir / "session-config.json", {**config, "precision_k": precision_k, "min_precision_at_k": min_precision, "cost_budget_usd": cost_budget})
    metadata = {"schema_version": "0.1", "session_id": config["session_id"], "status": "completed", "summary": summary}
    _write_manifest(output_dir, metadata)
    return summary
