# Optional Top-K reranking with `jev@typesafe`

The workflow alias is `jev@typesafe`; the official TypeSafe SDK model name is `jev-latest`.

Use this only after deterministic provider retrieval has produced a shortlist. Jev scores each existing `(research query, paper candidate)` pair with a typed Noul question and reorders the shortlist. It never expands the candidate set.

## Command

```bash
python3 scripts/research-search.py rerank-topk \
  artifacts/p0-live-20261018 \
  --strategy focused \
  --output artifacts/jev-rerank-plan
```

This is plan-only when `TYPESAFE_API_KEY` is absent. It keeps original order, makes zero TypeSafe requests, and marks `human_relevance_claim=false`.

Live use requires an explicit environment variable and flag:

```bash
export TYPESAFE_API_KEY='...'
python3 scripts/research-search.py rerank-topk \
  artifacts/p0-live-20261018 \
  --strategy focused \
  --top-k 20 \
  --use-typesafe \
  --output artifacts/jev-rerank-live
```

## Result boundaries

- `ordered_paper_ids` is a reordered existing shortlist; `candidate_set_changed` must remain false.
- `scores` records Jev's typed score/noul, confidence, model, usage and errors.
- A Jev score is not a human relevance label, Recall, Precision, or proof that the paper is relevant.
- Compare original and reranked order only after human review of the same candidates.
- Service errors, missing key, low confidence, and invalid typed answers preserve the original order and are reported as `not_executed` or `partial`.
- Never write the TypeSafe key to source files, package output, logs, or chat-delivered artifacts.

References:

- TypeSafe API: https://docs.typesafe.ai/api.md
- Python SDK: https://docs.typesafe.ai/sdk/python.md
- Noul: https://docs.typesafe.ai/primitives/noul.md
- Reranking cookbook: https://docs.typesafe.ai/cookbooks/rerank_typesafe.md
