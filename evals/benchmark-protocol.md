# P0 benchmark protocol

## Purpose

Compare engineering behavior and exploratory retrieval signals without confusing planned runs with actual runs.

## Cases

- `semg-joint-angle.json` is a fixture for strategy construction and field/provenance behavior.
- Future cases must keep seed papers, independent relevance labels, and runtime outputs in separate files.

## Baselines

1. A: small manually supplied term groups.
2. B: one-shot LLM candidates, saved with prompt/model metadata.
3. C: database-native query without evidence augmentation.
4. D: P0 evidence-grounded strategy.

## Required run record

- case ID
- baseline/strategy ID
- actual run count
- request count
- reported result count
- fetched count
- deduplicated count
- confirmed relevant count, if independently labeled
- evidence/provenance rate
- failure and limitation notes

No claim of superiority is allowed when the case lacks an independent relevance set.
