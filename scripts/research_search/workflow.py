"""Write a bounded, auditable Research Search Package without semantic inference."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict, replace
from datetime import UTC, datetime
import hashlib
from itertools import combinations
import json
from pathlib import Path
from typing import Any

from .keyword_extractor import extract_terms
from .keyword_normalizer import normalize_term
from .keyword_pipeline import DEFAULT_CANDIDATE_LIMIT, keyword_layers
from .models import ConceptGroup, Evidence, KeywordCandidate, Paper, SearchRun, TermOccurrence
from .openalex_client import OpenAlexClient
from .providers.base import redact_value
from .providers.fusion import fuse_results
from .providers.execution import execute_provider_plan, validate_provider_plan
from .providers.fusion_export import _result as _provider_result, _safe_public
from .paper_deduplicator import deduplicate_papers
from .query_builder import build_strategy_plans
from .search_evaluator import evaluate_retrieval
from .validation import validate_case, validate_package


_SUPPORTED_CONSTRAINTS = {"date_from": "from_publication_date", "date_to": "to_publication_date", "language": "language"}


def _now() -> str:
    return datetime.now(UTC).isoformat()


def _write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")


def _write_jsonl(path: Path, values: list[dict[str, Any]]) -> None:
    path.write_text("".join(json.dumps(value, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n" for value in values), encoding="utf-8")


def _filters(case: dict[str, Any]) -> dict[str, str]:
    # Give unsupported restrictions a useful error instead of silently dropping them.
    scope = case.get("research_scope") if isinstance(case, dict) else None
    constraints = scope.get("constraints") if isinstance(scope, dict) else None
    if isinstance(constraints, dict):
        unsupported = set(constraints) - set(_SUPPORTED_CONSTRAINTS)
        if unsupported:
            raise ValueError(f"unsupported constraints: {sorted(unsupported)}")
    validate_case(case)
    constraints = case["research_scope"]["constraints"]
    return {
        target: str(constraints[key])
        for key, target in _SUPPORTED_CONSTRAINTS.items()
        if key in constraints
    }


def _concept_groups(case: dict[str, Any]) -> list[ConceptGroup]:
    return [ConceptGroup(item["group_id"], item["label"], item["terms"], item.get("role")) for item in case["concept_groups"]]


def _timestamp(value: Any) -> str:
    if not isinstance(value, str) or "T" not in value.upper():
        raise ValueError("snapshot retrieved_at must be an ISO date-time with timezone")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError("snapshot retrieved_at must be an ISO date-time with timezone") from error
    if parsed.tzinfo is None:
        raise ValueError("snapshot retrieved_at must include a timezone")
    return value


def _snapshot_by_strategy(bundle: dict[str, Any], plans: list[Any]) -> dict[str, dict[str, Any]]:
    if not isinstance(bundle, dict) or bundle.get("schema_version") != "0.1":
        raise ValueError("snapshot bundle schema_version must be '0.1'")
    if bundle.get("snapshot_kind") not in {"synthetic_test_fixture", "live_capture"}:
        raise ValueError("snapshot_kind must be synthetic_test_fixture or live_capture")
    if set(bundle) - {"schema_version", "snapshot_kind", "snapshots"} or not isinstance(bundle.get("snapshots"), list):
        raise ValueError("malformed snapshot bundle")
    by_strategy = {plan.strategy: plan for plan in plans}
    result: dict[str, dict[str, Any]] = {}
    for item in bundle["snapshots"]:
        if not isinstance(item, dict) or set(item) - {"strategy", "query", "retrieved_at", "response"}:
            raise ValueError("malformed replay snapshot")
        strategy = item.get("strategy")
        if not isinstance(strategy, str) or strategy not in by_strategy:
            raise ValueError("unknown snapshot strategy")
        if strategy in result:
            raise ValueError(f"duplicate snapshot strategy: {strategy}")
        if by_strategy[strategy].status == "not_applicable":
            raise ValueError(f"snapshot strategy is not applicable: {strategy}")
        _timestamp(item.get("retrieved_at"))
        if "response" not in item:
            raise ValueError("snapshot response is required")
        if bundle["snapshot_kind"] == "live_capture" and "query" not in item:
            raise ValueError("live_capture snapshot query is required")
        if "query" in item and item["query"] != by_strategy[strategy].query:
            raise ValueError(f"snapshot query does not match plan query: {strategy}")
        result[strategy] = item
    try:
        json.dumps(bundle, allow_nan=False)
    except (TypeError, ValueError) as error:
        raise ValueError("snapshot bundle must contain JSON values") from error
    return result


def _contains(paper: Paper, field: str, excerpt: str) -> bool:
    value = getattr(paper, field, None)
    return excerpt in value if isinstance(value, (str, list)) else False


def _make_keyword_records(
    papers: list[Paper], occurrences: list[TermOccurrence], *, snapshot_kind: str = "live_capture",
    source_papers: list[Paper] | None = None, aliases: dict[str, str] | None = None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    paper_by_id = {paper.paper_id: paper for paper in papers}
    originals: dict[str, list[Paper]] = defaultdict(list)
    for paper in source_papers if source_papers is not None else papers:
        originals[(aliases or {}).get(paper.paper_id, paper.paper_id)].append(paper)
    grouped: dict[tuple[str, str], dict[tuple[str, str], TermOccurrence]] = defaultdict(dict)
    for item in occurrences:
        if item.paper_id not in paper_by_id:
            raise ValueError("term occurrence has no canonical paper")
        source_type = "openalex_keyword" if item.source_field == "database_keywords" else "paper_metadata"
        grouped[(item.term, source_type)].setdefault((item.paper_id, item.source_field), item)
    keywords: list[dict[str, Any]] = []
    evidence: list[dict[str, Any]] = []
    raw_observations: list[dict[str, Any]] = []
    for (term, source_type), observations in sorted(grouped.items()):
        evidence_ids: list[str] = []
        paper_ids = sorted({paper_id for paper_id, _ in observations})
        for (paper_id, field), item in sorted(observations.items()):
            paper = paper_by_id[paper_id]
            excerpt = item.original_term
            raw_observations.append({
                "term": item.term,
                "source_field": field,
                "paper_id": paper_id,
                "excerpt": excerpt,
                "evidence_status": item.evidence_status,
            })
            if not excerpt or not _contains(paper, field, excerpt):
                raise ValueError("term excerpt is not locatable in its original field")
            sources = [source for source in originals[paper_id] if _contains(source, field, excerpt)]
            run_ids = sorted({run_id for source in sources for run_id in source.source_run_ids})
            evidence_id = f"evidence-{len(evidence) + 1:05d}"
            evidence_ids.append(evidence_id)
            evidence.append(Evidence(
                evidence_id=evidence_id, source_type=source_type, source_url=paper.source_url,
                evidence_level="U" if snapshot_kind == "synthetic_test_fixture" else "A",
                retrieved_at=next((source.retrieved_at for source in sources if source.retrieved_at), None),
                locator=field, supports="Field observation only; not semantic equivalence or relevance.",
                paper_id=paper_id, excerpt=excerpt, run_ids=run_ids,
            ).to_dict())
        keywords.append(KeywordCandidate(
            term_id=f"term-{len(keywords) + 1:05d}", term=term, canonical_term=term,
            category="unclassified", relationship="unclassified", source_type=source_type,
            evidence_status="database_assigned" if source_type == "openalex_keyword" else "observed_in_paper",
            evidence_ids=evidence_ids, paper_ids=paper_ids, document_frequency=len(paper_ids), adopted=False,
        ).to_dict())
    return keywords, evidence, raw_observations


def _add_concept_candidates(keywords: list[dict[str, Any]], groups: list[ConceptGroup]) -> None:
    existing = {item["term"].casefold() for item in keywords}
    for term in sorted({normalize_term(term) for group in groups for term in group.terms}):
        if term.casefold() in existing:
            continue
        keywords.append(KeywordCandidate(
            term_id=f"term-{len(keywords) + 1:05d}", term=term, canonical_term=term,
            category="unclassified", relationship="unclassified", source_type="llm_candidate",
            evidence_status="unverified_candidate", adopted=False,
        ).to_dict())


def _cooccurrence(occurrences: list[TermOccurrence]) -> dict[str, Any]:
    documents: dict[str, set[str]] = defaultdict(set)
    labels: set[str] = set()
    for item in occurrences:
        documents[item.term].add(item.paper_id)
        if item.source_field in {"author_keywords", "database_keywords"}:
            labels.add(item.term)
    eligible = [term for term in documents if len(term.split()) > 1 or term in labels]
    ranked = sorted(eligible, key=lambda term: (-len(documents[term]), term))[:30]
    nodes = [{"term": term, "document_frequency": len(documents[term]), "paper_ids": sorted(documents[term])} for term in ranked]
    edges = []
    for left, right in combinations(sorted(ranked), 2):
        shared = documents[left] & documents[right]
        if shared:
            edges.append({"source": left, "target": right, "document_frequency": len(shared), "paper_ids": sorted(shared)})
    return {"schema_version": "0.1", "document_count": len({item.paper_id for item in occurrences}),
            "selection_rule": "Top 30 multiword observations or author/database labels by descending document_frequency, then lexical term.",
            "note": "cooccurrence != semantic equivalence; statistical n-grams are not semantic terms; no automatic query adoption.",
            "nodes": nodes, "edges": edges}


def _labels(judgments: list[dict[str, Any]], judge_type: str) -> tuple[dict[str, str], list[str]]:
    by_paper: dict[str, set[str]] = defaultdict(set)
    for item in judgments:
        if item["judge_type"] == judge_type:
            by_paper[item["paper_id"]].add(item["label"])
    conflicts = sorted(paper_id for paper_id, labels in by_paper.items() if len(labels) > 1)
    return {paper_id: next(iter(labels)) if len(labels) == 1 else "uncertain" for paper_id, labels in by_paper.items()}, conflicts


def _evaluation(case: dict[str, Any], runs: list[dict[str, Any]], judgments: list[dict[str, Any]],
                aliases: dict[str, str], snapshot_kind: str | None, k: int) -> dict[str, Any]:
    reference = case.get("independent_relevance_set")
    reference_ids = {aliases.get(pid, pid) for pid in reference} if reference is not None else None
    human_labels, conflicts = _labels(judgments, "human")
    synthetic = snapshot_kind == "synthetic_test_fixture"
    strategies = []
    for run in runs:
        evaluated = run["status"] in {"success", "partial"} and not synthetic
        metrics = evaluate_retrieval(
            run["paper_ids"], reference_ids if evaluated else None,
            run["fetched_count"], run["deduplicated_count"], k,
            relevance_labels=human_labels if evaluated else None,
        ).to_dict()
        strategies.append({"plan_id": run["plan_id"], "status": run["status"], "metrics": metrics,
                           "database_reported_count": run["returned_count"], "effectiveness_evaluated": evaluated})
    return {"schema_version": "0.1", "scope": "engineering_and_exploratory_only" if synthetic or reference is None else "reference_set_defined",
            "snapshot_kind": snapshot_kind, "synthetic_fixture_only": synthetic,
            "interpretation": "Synthetic data tests engineering only; no real-world effectiveness claims." if synthetic else
                              "No strategy superiority claimed. Reference hits/recall use only the independent set; precision uses human judgments only.",
            "strategies": strategies, "independent_relevance_set_size": len(reference_ids) if reference_ids is not None else None,
            "human_judgment_count": sum(item["judge_type"] == "human" for item in judgments),
            "human_label_conflicts_treated_as_uncertain": conflicts,
            "model_judgments": {"count": sum(item["judge_type"] == "model" for item in judgments),
                                "judgment_ids": [item["judgment_id"] for item in judgments if item["judge_type"] == "model"],
                                "used_for_precision": False}}


def _summary(runs: list[dict[str, Any]], mode: str, paper_count: int, output: Path) -> dict[str, Any]:
    failed = sum(run["status"] == "failed" for run in runs)
    available = sum(run["status"] in {"success", "partial"} for run in runs)
    partial = sum(run["status"] == "partial" for run in runs)
    status = "planned" if mode == "planned" else "failed" if failed and not available else "partial" if failed or partial else f"{mode}_complete"
    return {"status": status, "request_count": sum(run["request_count"] for run in runs),
            "api_request_count": sum(run["request_count"] for run in runs),
            "metadata_bytes": sum(run.get("metadata_bytes", 0) for run in runs),
            "cache_hit_count": sum(run.get("cache_hit", False) for run in runs), "screening_minutes": None,
            "executed_plan_count": sum(run["mode"] == "live" and run["request_count"] > 0 for run in runs),
            "replayed_plan_count": sum(run["mode"] == "replay" and run["status"] != "not_executed" for run in runs),
            "failed_plan_count": failed, "partial_plan_count": partial, "paper_count": paper_count, "output_dir": str(output)}


def _readme(case: dict[str, Any], summary: dict[str, Any], keywords: list[dict[str, Any]], snapshot_kind: str | None) -> str:
    scope = case["research_scope"]
    def display(value: Any) -> str:
        return str(value).replace("|", "\\|").replace("\n", " ")
    rows = ["| 候选词（待审） | 来源 | 文档频率 |", "|---|---|---:|"]
    for item in sorted(keywords, key=lambda item: (-item["document_frequency"], item["term"], item["source_type"]))[:20]:
        rows.append(f"| {display(item['term'])} | {item['source_type']} | {item['document_frequency']} |")
    return (f"# Research Search Package\n\n案例：{display(case['case_id'])}；状态：{summary['status']}。\n\n"
            f"## 研究边界\n\n- 描述：{display(scope['description'])}\n- 对象：{display(scope['research_object'])}\n"
            f"- 输入：{display(scope['input_modality'])}；任务：{display(scope['research_task'])}\n"
            f"- 方法：{display(scope['method']) if scope['method'] else '未指定；方法专门式不执行'}\n"
            f"- 应用：{display(scope['application']) if scope['application'] else '未指定'}（P0 记录应用上下文，不自动作为过滤条件）\n"
            f"- 约束：{display(scope['constraints'])}；未指定：{display(scope['unspecified'])}\n"
            "- 概念分组由宿主 Agent 提供；不做自动语义解析、等价归并或相关性推断。系统检索准备不等于系统综述完成。\n\n"
            f"## 执行与证据\n\n- 实际新增网络 attempts：{summary['request_count']}；实际请求策略：{summary['executed_plan_count']}；回放策略：{summary['replayed_plan_count']}。\n"
            f"- 去重后论文：{summary['paper_count']}；失败策略：{summary['failed_plan_count']}。数据库总量、抓取量与逐策略去重量分别记录。\n"
            f"- 数据 origin：{snapshot_kind or 'planned'}。{'合成夹具证据均为 U，仅验证工程流程，不代表真实文献或真实检索效果。' if snapshot_kind == 'synthetic_test_fixture' else 'A 级仅表示 API 字段来源可追溯，不证明论文结论、相关性或术语等价。'}\n"
            "- 独立相关集只用于参考命中/召回；仅有人类完整标注时才能计算相应 precision。未标注文献不是负例；模型标注单列。\n"
            "- 原词片段保留大小写与连续文字，可在 Evidence.locator 指向的 Paper 字段定位；共现不代表语义等价。\n\n"
            "## 候选审阅（最多 20 条）\n\n标题/摘要的统计 n-gram 不是语义术语。全部候选保持 unclassified、adopted=false；发现词不自动加入查询。\n\n" + "\n".join(rows) +
            "\n\n## 文件索引\n\n01 研究范围；02 候选词数组；03 三类查询计划数组；04 论文 JSONL；05 逐策略运行 JSONL；06 评测；07 字段证据 JSONL；08 文档频率与共现边；09 去重记录；10 人工/模型标注 JSONL。\n\n"
            "`raw/` 保存各已执行/回放策略的原始响应（无响应时为 null）；`input-case.json` 保存输入；`replay-bundle.json`（若有可回放响应）记录捕获来源与时间；`manifest.json` 记录全部文件 SHA-256、内容摘要与完成状态。\n")


def _manifest(output: Path, metadata: dict[str, Any]) -> None:
    files = {str(path.relative_to(output)): hashlib.sha256(path.read_bytes()).hexdigest()
             for path in sorted(output.rglob("*")) if path.is_file() and path.name != "manifest.json"}
    _write_json(output / "manifest.json", {**metadata, "files": files})


def run_package(case: dict[str, Any], output_dir: Path, *, snapshots: dict[str, Any] | None = None,
                client: OpenAlexClient | None = None, per_page: int = 10, k: int = 10,
                candidate_limit: int = DEFAULT_CANDIDATE_LIMIT,
                provider_results: list[dict[str, Any]] | None = None,
                provider_plan: list[dict[str, Any]] | None = None,
                provider_live: bool = False,
                provider_max_requests: int = 0,
                provider_use_default_transport: bool = False) -> dict[str, Any]:
    """Plan, replay, or execute explicit OpenAlex strategies and write one package.

    Invalid inputs are rejected before output creation. Existing destinations are
    never overwritten. Network attempts count only calls reported by the live
    client; snapshot replay uses the public parser and always counts zero.
    """
    filters = _filters(case)
    if type(per_page) is not int or not 1 <= per_page <= 100 or type(k) is not int or k <= 0:
        raise ValueError("per_page must be 1..100 and k must be a positive integer")
    if type(candidate_limit) is not int or not 1 <= candidate_limit <= 500:
        raise ValueError("candidate_limit must be between 1 and 500")
    provider_payloads = []
    provider_fusion = None
    if provider_results is not None and provider_plan is not None:
        raise ValueError("provide provider_results or provider_plan, not both")
    if provider_plan is not None:
        provider_results = execute_provider_plan(validate_provider_plan(provider_plan), live=provider_live, max_requests=provider_max_requests,
                                                 use_default_public_transport=provider_use_default_transport)
    if provider_results is not None:
        if not isinstance(provider_results, list):
            raise ValueError("provider_results must be a list")
        provider_payloads = []
        provider_objects = []
        for item in provider_results:
            provider_object = _provider_result(item)
            provider_objects.append(provider_object)
            summary = dict(provider_object.to_dict())
            summary["raw_response"] = None
            summary["papers"] = [redact_value({**paper.to_dict(), "raw": None}) for paper in provider_object.papers]
            summary["query_type"] = item.get("query_type") or next((paper.channel for paper in provider_object.papers if paper.channel), "unknown")
            summary["channel"] = item.get("channel") or summary["query_type"]
            summary["plan_id"] = item.get("plan_id")
            summary["historical_request_count"] = item.get("historical_request_count", provider_object.request_count if not item.get("new_network_request_count") else 0)
            summary["new_network_request_count"] = item.get("new_network_request_count", 0)
            provider_payloads.append(redact_value(summary))
        provider_fusion = _safe_public(redact_value(fuse_results(provider_objects).to_dict()))
    if snapshots is not None and client is not None:
        raise ValueError("provide snapshots or a live client, not both")
    groups = _concept_groups(case)
    plans = build_strategy_plans(groups)
    replay = _snapshot_by_strategy(snapshots, plans) if snapshots is not None else None
    try:
        json.dumps(case, allow_nan=False)
    except (TypeError, ValueError) as error:
        raise ValueError("case must contain JSON values") from error
    output_dir = Path(output_dir)
    if output_dir.exists():
        raise FileExistsError(f"output directory already exists: {output_dir}")
    mode = "replay" if replay is not None else "live" if client is not None else "planned"
    snapshot_kind = snapshots["snapshot_kind"] if snapshots is not None else "live_capture" if client is not None else None
    metadata: dict[str, Any] = {"package_schema_version": "0.1", "created_at": _now(), "case_id": case["case_id"],
                                "mode": mode, "snapshot_kind": snapshot_kind, "status": "in_progress",
                                "execution_parameters": {"per_page": per_page, "k": k, "filters": filters, "candidate_limit": candidate_limit,
                                                         "provider_result_count": len(provider_payloads)}}
    output_dir.mkdir(parents=True, exist_ok=False)
    all_papers: list[Paper] = []
    runs: list[dict[str, Any]] = []
    try:
        _manifest(output_dir, metadata)
        (output_dir / "raw").mkdir()
        captured: list[dict[str, Any]] = []
        parser = OpenAlexClient(api_key="", max_retries=0) if replay is not None else None
        for plan in plans:
            run_id = f"run-{plan.plan_id}"
            item = replay.get(plan.strategy) if replay is not None else None
            if plan.status == "not_applicable" or mode == "planned" or (replay is not None and item is None):
                warning = plan.reason if plan.status == "not_applicable" else "No snapshot supplied; not executed." if replay is not None else "Plan only; no request made."
                runs.append(SearchRun(run_id, plan.plan_id, "not_executed", mode=mode, warnings=[warning]).to_dict())
                continue
            started = item["retrieved_at"] if item is not None else _now()
            if item is not None:
                result = parser.parse_response(item["response"], item["retrieved_at"])
                finished = item["retrieved_at"]
            else:
                result = client.search_works(plan.query, per_page=per_page, filters=filters)
                finished = _now()
            papers = [replace(paper, source_run_ids=[run_id], retrieved_at=result.retrieved_at or paper.retrieved_at)
                      for paper in result.papers]
            all_papers.extend(papers)
            raw_path = f"raw/{run_id}.json"
            _write_json(output_dir / raw_path, result.raw_response)
            if isinstance(result.raw_response, dict) and result.retrieved_at:
                captured.append({"strategy": plan.strategy, "query": plan.query, "retrieved_at": result.retrieved_at,
                                 "response": result.raw_response})
            runs.append(SearchRun(
                run_id, plan.plan_id, result.status, returned_count=result.total_count,
                fetched_count=result.fetched_count, request_count=0 if item is not None else result.request_count,
                started_at=started, finished_at=finished, request_url=None if item is not None else result.request_url,
                error_type=result.error_type, error_message=result.error_message, mode=mode,
                paper_ids=[paper.paper_id for paper in papers], raw_path=raw_path,
                attempts=[] if item is not None else result.attempts, warnings=result.warnings,
                cache_hit=bool(getattr(result, "cache_hit", False)), cache_key=getattr(result, "cache_key", None),
                metadata_bytes=0 if item is not None else int(getattr(result, "metadata_bytes", 0)),
            ).to_dict())

        deduped = deduplicate_papers(all_papers)
        # Resolve aliases defensively even if the deduplicator already flattened
        # them. A per-run unique count is not the global number of papers.
        def canonical(paper_id: str) -> str:
            seen: set[str] = set()
            while paper_id in deduped.merged_ids:
                if paper_id in seen:
                    raise ValueError("deduplication alias cycle")
                seen.add(paper_id)
                paper_id = deduped.merged_ids[paper_id]
            return paper_id
        aliases = {paper_id: canonical(paper_id) for paper_id in deduped.merged_ids}
        paper_runs: dict[str, set[str]] = defaultdict(set)
        for run in runs:
            run["paper_ids"] = [canonical(paper_id) for paper_id in run["paper_ids"]]
            run["deduplicated_count"] = len(set(run["paper_ids"]))
            for paper_id in run["paper_ids"]:
                paper_runs[paper_id].add(run["run_id"])
        papers = [replace(paper, source_run_ids=sorted(paper_runs[paper.paper_id])) for paper in deduped.papers]
        occurrences = [replace(item, paper_id=paper.paper_id) for paper in papers for item in extract_terms(paper)]
        keywords, evidence, raw_observations = _make_keyword_records(
            papers, occurrences, snapshot_kind=snapshot_kind or "live_capture",
            source_papers=all_papers, aliases=aliases,
        )
        _add_concept_candidates(keywords, groups)
        layers = keyword_layers(
            keywords, evidence, limit=candidate_limit, reviews=case.get("keyword_reviews", []),
        )
        raw_observations = layers["observations"]
        candidate_keywords = layers["candidates"]["terms"]
        reviewed_keywords = layers["reviewed"]
        keywords = layers["keywords"]
        judgments = [{**item, "paper_id": canonical(item["paper_id"])} for item in case.get("judgments", [])]
        scope = case["research_scope"]
        plan_records = [plan.to_dict() for plan in plans]
        paper_records = [paper.to_dict() for paper in papers]
        _write_json(output_dir / "input-case.json", case)
        _write_json(output_dir / "01-research-scope.json", scope)
        _write_json(output_dir / "02-keywords.json", keywords)
        _write_jsonl(output_dir / "raw-observations.jsonl", raw_observations)
        _write_json(output_dir / "candidate-terms.json", layers["candidates"])
        _write_json(output_dir / "reviewed-keywords.json", {
            "schema_version": "0.1",
            "adoption_rule": "Only explicitly reviewed and adopted terms are formal retrieval terms.",
            "terms": reviewed_keywords,
        })
        _write_json(output_dir / "03-search-strategies.json", plan_records)
        _write_jsonl(output_dir / "04-papers.jsonl", paper_records)
        _write_jsonl(output_dir / "05-search-runs.jsonl", runs)
        _write_json(output_dir / "06-evaluation.json", _evaluation(case, runs, judgments, aliases, snapshot_kind, k))
        _write_jsonl(output_dir / "07-evidence.jsonl", evidence)
        _write_json(output_dir / "08-cooccurrence.json", _cooccurrence(occurrences))
        _write_json(output_dir / "09-deduplication.json", {"schema_version": "0.1", "merged_ids": aliases,
                                                         "conflicts": [asdict(conflict) for conflict in deduped.conflicts]})
        _write_jsonl(output_dir / "10-judgments.jsonl", judgments)
        if provider_payloads:
            _write_jsonl(output_dir / "11-provider-results.jsonl", provider_payloads)
            _write_json(output_dir / "12-provider-fusion.json", provider_fusion)
        if captured:
            _write_json(output_dir / "replay-bundle.json", {"schema_version": "0.1", "snapshot_kind": snapshot_kind, "snapshots": captured})
        summary = _summary(runs, mode, len(papers), output_dir)
        summary.update({
            "provider_historical_request_count": sum(item.get("historical_request_count", item.get("request_count", 0)) for item in provider_payloads),
            "provider_new_network_request_count": sum(item.get("new_network_request_count", 0) for item in provider_payloads),
            "provider_unique_count": len((provider_fusion or {}).get("papers", [])),
            "provider_channel_count": len({item.get("query_type", "unknown") for item in provider_payloads}),
            "provider_result_count": len(provider_payloads),
        })
        (output_dir / "README.md").write_text(_readme(case, summary, keywords, snapshot_kind), encoding="utf-8")
        content = {"scope": scope, "plans": plan_records, "keywords": keywords, "papers": paper_records,
                   "provider_results": provider_payloads, "provider_fusion": provider_fusion}
        metadata.update(status="failed" if summary["status"] == "failed" else "partial" if summary["status"] == "partial" else "completed",
                        result_status=summary["status"], summary=summary,
                        content_hash=hashlib.sha256(json.dumps(content, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")).hexdigest())
        _manifest(output_dir, metadata)
        validate_package(output_dir)
        return summary
    except Exception as error:
        metadata.update(status="failed", error_type=type(error).__name__, error_message=str(error))
        _manifest(output_dir, metadata)
        raise
