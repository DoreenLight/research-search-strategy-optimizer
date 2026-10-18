# P0 execution

Use the full project checkout or the self-contained release ZIP. In the checkout the scripts and schemas are at the project root; in the ZIP they are inside the `research-search-strategy-optimizer` directory beside SKILL.md. If only this SKILL.md and references were copied from the source checkout, scripts are missing: stop and request the complete release rather than pretend retrieval ran.

Requirements: Python 3.11+ and `jsonschema>=4.23,<5`. Install only in an approved environment (for example a project-local virtual environment). Scripts use the standard library for HTTP.

## Agent input

Read `schemas/research-case.schema.json` and `examples/semg-joint-angle.json` in the release (checkout: `evals/cases/semg-joint-angle.json`). Write a case with original Chinese scope, unprovided constraints open, and English literal concept groups. Each group uses an explicit `role`: input/object/task/method/application. Two core roles are required. Place only equivalent or deliberately approved alternatives within one OR group; related tasks and broader terms need their own reviewed case/query.

P0 numeric scripts do not automatically translate or infer scope. Only date_from, date_to and language filters are implemented. Retain other supplied restrictions in the original description and stop to design supported groups or report that they require manual review; do not silently drop restrictions.

## Commands (from project or release root)

- Plan without network: `python3 scripts/research-search.py run <case.json> --output <new-package-dir>`
- Replay: add `--snapshots <snapshot-bundle.json>`; zero new network requests.
- Live: add `--live --per-page 10 --max-requests 3`; explicit opt-in, anonymous by default, at most three HTTP attempts including retries. Existing files are not overwritten.
- Validate: `python3 scripts/research-search.py validate-package <package-dir>`.
- Compile only: `python3 scripts/research-search.py build-query <case.json>`.

Use `--help` for the current exact interface. A deliberate `--use-api-key` opts into OPENALEX_API_KEY; otherwise no account key or paid allowance is consumed. No signup, paid /text labeling, semantic endpoint, auto-citation expansion, or account changes are made. Public free allowance can still be exhausted; report 429/403 and stop at the configured budget.

## OpenAlex literal query subset

The official Works [Search documentation](https://help.openalex.org/api/searching/) (read 2026-10-17) supports uppercase AND/OR and quoted phrases. P0 compiles only this conservative subset: `("surface electromyography" OR "sEMG") AND ("joint angle")`. Keep variants within approved concept groups, adding task/method groups only in their respective strategies. Local rendering is not remote execution; disclose that distinction instead of avoiding all documented Boolean syntax. Terms containing raw query operators are rejected; advanced NOT/proximity/truncation are outside this version.

## After retrieval

Read the evidence and candidate output. Separate model-generated candidates, text occurrences, author keywords, and machine-assigned OpenAlex tags. A literal phrase observation establishes occurrence, not relevance or synonymy. Write human/model judgments separately if supplied; lack of labels makes Precision unavailable. Do not claim PRESS/PRISMA-S compliance certification or complete recall.
