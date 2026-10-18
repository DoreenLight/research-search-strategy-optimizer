"""Command-line entry. Live network access is opt-in and budgeted."""
from __future__ import annotations

import argparse
from dataclasses import asdict
import json
from pathlib import Path
import sys

from .models import ConceptGroup
from .openalex_client import OpenAlexClient
from .query_builder import build_strategy_plans
from .search_evaluator import evaluate_retrieval
from .validation import validate_case, validate_package


def _json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _groups(path: Path) -> list[ConceptGroup]:
    payload = _json(path)
    if isinstance(payload, dict):
        validate_case(payload)
        payload = payload["concept_groups"]
    if not isinstance(payload, list):
        raise ValueError("input must be a concept array or versioned research case")
    if any(not isinstance(item, dict) for item in payload):
        raise ValueError("each concept group must be an object")
    return [ConceptGroup(item["group_id"], item.get("label", item["group_id"]), item["terms"], item.get("role")) for item in payload]


def _dump(payload) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evidence-grounded research strategy P0")
    commands = parser.add_subparsers(dest="command", required=True)
    query = commands.add_parser("build-query", help="Compile three role-based query plans without networking")
    query.add_argument("groups", type=Path)
    evaluate = commands.add_parser("evaluate", help="Compute metrics; partial judgments are not negatives")
    evaluate.add_argument("returned_ids", type=Path)
    evaluate.add_argument("--known-relevant", type=Path)
    evaluate.add_argument("--relevance-labels", type=Path)
    evaluate.add_argument("--fetched-count", type=int, required=True)
    evaluate.add_argument("--deduplicated-count", type=int, required=True)
    evaluate.add_argument("--k", type=int, default=10)
    search = commands.add_parser("search-openalex", help="One anonymous Works search (uses network)")
    search.add_argument("search")
    search.add_argument("--per-page", type=int, default=10)
    search.add_argument("--use-api-key", action="store_true", help="Explicitly use OPENALEX_API_KEY; default anonymous")
    search.add_argument("--max-requests", type=int, default=1)
    search.add_argument("--output", type=Path, help="Save complete redacted search response; refuses overwrite")
    run = commands.add_parser("run", help="Create a linked Research Search Package")
    run.add_argument("case", type=Path)
    run.add_argument("--output", type=Path, required=True)
    mode = run.add_mutually_exclusive_group()
    mode.add_argument("--snapshots", type=Path, help="Offline snapshot replay (zero new network requests)")
    mode.add_argument("--live", action="store_true", help="Explicit live OpenAlex search; default plan-only")
    run.add_argument("--per-page", type=int, default=10)
    run.add_argument("--max-requests", type=int, default=3)
    run.add_argument("--use-api-key", action="store_true")
    optimize = commands.add_parser("optimize", help="Run a versioned P1 plan/replay/live optimization session")
    optimize.add_argument("config", type=Path)
    optimize.add_argument("--output", type=Path, required=True)
    optimize.add_argument("--live", action="store_true")
    optimize.add_argument("--per-page", type=int, default=10)
    optimize.add_argument("--max-requests", type=int, default=None)
    optimize.add_argument("--use-api-key", action="store_true")
    acquisition = commands.add_parser("acquisition-handoff", help="Build a lawful metadata-only acquisition queue")
    acquisition.add_argument("source", type=Path)
    acquisition.add_argument("--output", type=Path)
    reading = commands.add_parser("reading-export", help="Export validated papers into a new reading directory")
    reading.add_argument("source", type=Path)
    reading.add_argument("--output", type=Path, required=True)
    reading.add_argument("--metadata-format", action="append", choices=["jsonl", "csv"])
    validate_reading = commands.add_parser("validate-reading", help="Validate a local reading export")
    validate_reading.add_argument("export_dir", type=Path)
    benchmark = commands.add_parser("benchmark", help="Summarize supplied P4 benchmark observations offline")
    benchmark.add_argument("manifest", type=Path)
    benchmark.add_argument("--output", type=Path, required=True)
    provider_search = commands.add_parser("provider-search", help="Plan or execute an injected P2 provider search")
    provider_search.add_argument("provider", choices=["pubmed", "semantic_scholar"])
    provider_search.add_argument("query")
    provider_search.add_argument("--output", type=Path, required=True)
    provider_search.add_argument("--live", action="store_true")
    provider_search.add_argument("--limit", type=int, default=20)
    provider_discover = commands.add_parser("provider-discover", help="Plan P2 citation/reference/recommendation discovery")
    provider_discover.add_argument("channel", choices=["citation", "reference", "recommendation"])
    provider_discover.add_argument("seed")
    provider_discover.add_argument("--output", type=Path, required=True)
    provider_discover.add_argument("--live", action="store_true")
    provider_discover.add_argument("--limit", type=int, default=20)
    rerank = commands.add_parser("rerank-topk", help="Optionally rerank an existing shortlist with TypeSafe Jev")
    rerank.add_argument("package", type=Path)
    rerank.add_argument("--strategy", default="focused")
    rerank.add_argument("--output", type=Path, required=True)
    rerank.add_argument("--top-k", type=int, default=20)
    rerank.add_argument("--use-typesafe", action="store_true", help="Explicitly use TYPESAFE_API_KEY")
    validate = commands.add_parser("validate-package", help="Validate schemas, links and file hashes")
    validate.add_argument("package", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "build-query":
            _dump([asdict(plan) for plan in build_strategy_plans(_groups(args.groups))])
        elif args.command == "evaluate":
            reference = _json(args.known_relevant) if args.known_relevant else None
            if reference is not None and (not isinstance(reference, list) or any(not isinstance(x, str) for x in reference)):
                raise ValueError("known-relevant must be an array of paper IDs")
            labels = _json(args.relevance_labels) if args.relevance_labels else None
            if labels is not None and not isinstance(labels, dict):
                raise ValueError("relevance-labels must be a mapping")
            metrics = evaluate_retrieval(_json(args.returned_ids), set(reference) if reference is not None else None,
                                         args.fetched_count, args.deduplicated_count, args.k, relevance_labels=labels)
            _dump(metrics.to_dict())
        elif args.command == "search-openalex":
            if args.output and args.output.exists():
                raise FileExistsError("output exists; choose a new filename")
            client = OpenAlexClient(api_key=None if args.use_api_key else "", max_retries=0,
                                    max_requests=args.max_requests, timeout=15)
            result = client.search_works(args.search, per_page=args.per_page)
            payload = asdict(result)
            if args.output:
                args.output.parent.mkdir(parents=True, exist_ok=True)
                args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                _dump({"status": result.status, "total_count": result.total_count,
                       "fetched_count": result.fetched_count, "request_count": result.request_count,
                       "error_type": result.error_type, "output": str(args.output.resolve())})
            else:
                _dump(payload)
            return 0 if result.status == "success" else 2
        elif args.command == "run":
            from .workflow import run_package
            case = _json(args.case)
            client = OpenAlexClient(api_key=None if args.use_api_key else "", max_retries=0,
                                    max_requests=args.max_requests, timeout=15) if args.live else None
            summary = run_package(case, args.output, snapshots=_json(args.snapshots) if args.snapshots else None,
                                  client=client, per_page=args.per_page)
            _dump(summary)
            return 2 if summary["status"] in {"failed", "partial"} else 0
        elif args.command == "optimize":
            from .optimization_session import run_optimization
            config = _json(args.config)
            if args.max_requests is not None:
                config["max_requests"] = args.max_requests
            request_budget = config.get("max_requests", 0)
            client = OpenAlexClient(api_key=None if args.use_api_key else "", max_retries=0,
                                    max_requests=request_budget, timeout=15) if args.live else None
            _dump(run_optimization(config, args.output, client=client, per_page=args.per_page))
        elif args.command == "acquisition-handoff":
            from .acquisition_handoff import acquisition_handoff
            _dump(acquisition_handoff(args.source, args.output))
        elif args.command == "reading-export":
            from .reading_export import export_reading
            _dump(export_reading(args.source, args.output, metadata_formats=args.metadata_format or ()))
        elif args.command == "validate-reading":
            from .reading_export import open_obsidian
            _dump(open_obsidian(args.export_dir))
        elif args.command == "benchmark":
            from .benchmark import run_benchmark
            _dump(run_benchmark(_json(args.manifest), args.output))
        elif args.command == "provider-search":
            from .providers import PubMedProvider, SearchRequest, SemanticScholarProvider
            provider = PubMedProvider() if args.provider == "pubmed" else SemanticScholarProvider()
            result = provider.search(SearchRequest(args.query, limit=args.limit, mode="live" if args.live else "planned"))
            if args.output.exists():
                raise FileExistsError("output exists; choose a new filename")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(result.to_dict(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            _dump({"status": result.status, "request_count": result.request_count, "output": str(args.output.resolve())})
            return 0 if result.status in {"planned", "success", "partial", "not_executed"} else 2
        elif args.command == "provider-discover":
            from .providers import SearchRequest, SemanticScholarProvider
            provider = SemanticScholarProvider()
            if args.channel == "recommendation":
                result = provider.recommend(args.seed, limit=args.limit, mode="live" if args.live else "planned")
            else:
                result = provider.citations(args.seed, direction="citations" if args.channel == "citation" else "references", limit=args.limit, mode="live" if args.live else "planned")
            if args.output.exists():
                raise FileExistsError("output exists; choose a new filename")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(result.to_dict(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            _dump({"status": result.status, "request_count": result.request_count, "output": str(args.output.resolve())})
            return 0 if result.status in {"planned", "success", "partial", "not_executed"} else 2
        elif args.command == "rerank-topk":
            from .typesafe_package import rerank_package_topk
            from .typesafe_reranker import RerankConfig
            config = RerankConfig(api_key=None if args.use_typesafe else "", top_k=args.top_k)
            _dump(rerank_package_topk(args.package, strategy=args.strategy, output_dir=args.output, config=config))
        elif args.command == "validate-package":
            _dump({"status": "valid", **validate_package(args.package)})
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
