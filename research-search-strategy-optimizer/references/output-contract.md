# P0 output contract

Each package contains input-case.json, 01-research-scope.json, 02-keywords.json, 03-search-strategies.json, 04-papers.jsonl, 05-search-runs.jsonl, 06-evaluation.json, 07-evidence.jsonl, 08-cooccurrence.json, 09-deduplication.json, 10-judgments.jsonl, report.md, README.md and manifest.json. Raw responses are saved only when a response exists.

- Scope preserves unspecified constraints. Strategy IDs and AND/OR concept logic are stable and distinguish local syntax checks from actual execution.
- Keywords link to evidence IDs and paper IDs; evidence links to an original source field, excerpt and run. Machine-assigned tags remain database_assigned, not author keywords.
- Runs separate database-reported count (unknown=null), fetched records and per-run deduplicated records. Replayed requests are not new network attempts. Overall union size is a different count.
- Known relevant IDs yield coverage against that reference set, not global recall. Precision requires complete human labels for the specified K; judged-only precision is separately named. Unjudged records are not negatives.
- Synthetic fixtures are conspicuously labeled and cannot support claims about real literature or retrieval superiority.
- Manifest inventories SHA-256 hashes and status. A failed/partial package remains auditable, not silently labeled complete. Validation checks schema, references and hashes.
