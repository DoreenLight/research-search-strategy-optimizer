"""P1 auditable optimization sessions over versioned Research Search Packages."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .iteration_optimizer import compare_strategy_versions, should_stop
from .openalex_client import OpenAlexSearchResult
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
    drift_alarm_index = next((index for index, item in enumerate(rounds[1:], 1)
                              if item.get("drift_rate") is not None and float(item["drift_rate"]) >= 0.6), None)
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
    stop_reason = "continue"
    executed_round_count = 0
    replayed_round_count = 0
    live_budget = _SessionBudgetClient(client, max_requests) if client is not None else None

    for index, round_config in enumerate(rounds):
        is_baseline = index == 0
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
            if round_config.get("separate_branch", False):
                decision = "branch_only"
            elif synthetic or not human or conflicts or new_unjudged:
                decision = "pending_review"
                stop_reason = "awaiting_human_judgments"
            else:
                confirmed_gain = sum(human.get(paper_id) == "relevant" for paper_id in new_ids)
                if lost_relevant_ids:
                    decision = "rollback_to_previous"
                elif confirmed_gain > 0 or not new_ids:
                    decision = "retain"
                    active_case = round_config["case"]
                    active_ids = current_ids
                    active_relevant_ids = (active_relevant_ids & set(current_ids)) | {
                        paper_id for paper_id, label in human.items() if label == "relevant" and paper_id in current_ids
                    }
                    active_version = index
                else:
                    decision = "rollback_to_previous"
        history.append({
            "round_index": index, "version": index, "case_fingerprint": _case_fingerprint(round_config["case"]),
            "rationale": round_config.get("rationale", ""), "reviewed_by": round_config.get("reviewed_by"),
            "relationship": round_config.get("change_relationship", "baseline"), "package_status": package_summary["status"],
            "request_count": round_requests, "comparison": comparison, "confirmed_gain": confirmed_gain,
            "lost_relevant_ids": lost_relevant_ids, "human_label_conflicts": conflicts, "decision": decision,
            "new_terms": round_config.get("new_terms", []), "coverage_claim": "not_proven_complete",
        })
        if drift_alarm_index is not None and index >= drift_alarm_index:
            stop_reason = "semantic_drift_alarm"
            break
        if stop_reason in {"awaiting_human_judgments", "execution_failed"}:
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
        "current_version": len(history) - 1, "active_version": active_version, "stop_reason": stop_reason,
        "coverage_claim": "not_proven_complete",
    }
    if active_version is None or stop_reason == "execution_failed":
        summary["status"] = "failed"
    elif stop_reason == "awaiting_human_judgments":
        summary["status"] = "pending_review"
    _dump(output_dir / "history.json", history)
    _dump(output_dir / "summary.json", summary)
    _dump(output_dir / "active-case.json", active_case)
    metadata = {"schema_version": "0.1", "session_id": config["session_id"], "status": "completed", "summary": summary}
    _write_manifest(output_dir, metadata)
    return summary
