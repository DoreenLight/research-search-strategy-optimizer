---
name: research-search-strategy-optimizer
description: |
  Convert a natural-language academic research question into an evidence-grounded,
  executable, traceable search strategy. Load when the user asks for research
  keywords, literature search terms, Boolean queries, database search planning,
  or iterative search evaluation. Use for exploratory research discovery and
  structured search preparation; do not use it as a substitute for full-text
  acquisition, systematic-review compliance certification, or a generic paper
  summarizer.
compatibility: Requires the companion Python scripts and jsonschema>=4.23; network access is opt-in for OpenAlex, PubMed, and Semantic Scholar adapters.
metadata:
  version: "0.2.0"
  status: "p0-p4-code-complete"
---

# Research Search Strategy Optimizer

## Inputs to collect

- The user's original research description.
- Explicit object, input, task, method, application, population, date, language, and database constraints.
- Unspecified constraints that must remain open.
- Whether the goal is exploratory discovery or a more reproducible search record.
- A request budget and whether live network access is allowed.

## Procedure

1. Parse the research description into a structured research scope.
   Preserve unspecified constraints as open fields so the first query does not narrow the search by assumption.
2. Produce candidate concept groups and label every term with its dimension and relationship.
   Keep equivalent terms separate from broader concepts, related tasks, applications, and alternative methods.
3. Attach provenance to every adopted term.
   Treat model-generated candidates as unverified until a paper, database field, or controlled vocabulary supports them.
4. Build database-independent logic first, then render the target database query.
   Keep exploratory, focused, and method-specific strategies as separate versions.
5. Choose one execution mode explicitly: plan-only (zero network), synthetic replay (zero new network), or live OpenAlex (budgeted and logged).
   Run the deterministic companion scripts for field-preserving extraction, identifier deduplication, and metric calculation; record planned, executed, successful, partial, and failed runs separately.
6. Evaluate retrieval only against an explicitly defined reference set and human judgments.
   Report returned, fetched, and deduplicated counts separately; partial labels never become negative labels; leave recall/precision unavailable when the required reference or judgments are absent.
7. Export and validate a Research Search Package with scope, raw observations, bounded candidate terms, explicitly reviewed keywords, evidence, papers, strategies, run logs, evaluation, raw snapshots, judgments, and a manifest.

## Output contract

Return or write:

- Structured research scope.
- Keyword taxonomy with relationship, source, evidence status, and retrieval-test status.
- Exploratory, focused, and method-specific query plans.
- Paper records with source identifiers and retrieval date.
- Search-run logs and evaluation metrics.
- A limitations section distinguishing official claims, observed records, model judgments, inferences, and unverified candidates.
- P2 provider results with source and discovery-channel status when PubMed/MeSH or Semantic Scholar adapters are used.
- P3 metadata-only acquisition and reading exports; these do not download full text, bypass access controls, scan a Vault, or launch Obsidian.
- P4 benchmark summaries and human-review queues; missing labels remain unknown and do not become negative examples.
- P1 review workbench exports are offline and blinded; candidate ranking is not semantic approval, and only an explicit `adopt-keywords` action adds approved terms to a new case.
- Optional query caching is local, redacted, content-addressed, and cache hits do not consume network request budget.

## Failure handling

- If a database is unavailable, report the failed request and provide an unexecuted query export rather than claiming a search succeeded.
- If an abstract or identifier is missing, preserve the missing value and continue with the fields that exist.
- If two records share a title but have conflicting reliable identifiers, keep both and emit a deduplication conflict.
- If no independent relevance set exists, report engineering checks and exploratory metrics only.
- Keep credentials in environment variables; redact them from URLs, logs, and output packages.

## Canonical example

Input: `基于表面肌电预测人体关节角度，想了解 Transformer 和其他方法的研究情况。`

Expected first pass: separate input modality, research object, task, and method; create a broad object/task query before adding the method group; attach every discovered term to the paper field or database record that supplied it.

Read [execution](references/execution.md) before running scripts, [evidence rules](references/evidence-rules.md) before promoting terms, [output contract](references/output-contract.md) before delivery, and [typesafe-rerank](references/typesafe-rerank.md) before using `jev@typesafe`. The input case is an explicit Agent/user semantic interpretation, not a Python translation model. Keep discovered phrases unclassified until reviewed; co-occurrence alone does not establish equivalence. P0 executes OpenAlex; P2 adapters and TypeSafe reranking are explicit planned/live/replay channels, not implicit coverage.

## Windows (win32) platform notes

Use `py -3 scripts/research-search.py --help` instead of `python3`. Quote paths containing spaces. The CLI and ZIP packager use pathlib and require no Unix shell tools. Do not translate `PYTHONPATH=...` shell syntax into PowerShell; use the direct script entry.
