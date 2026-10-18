from __future__ import annotations

import re
import unicodedata


_OUTER_QUOTES = '"\'“”‘’«»'
_DASHES = str.maketrans({
    "–": "-",
    "—": "-",
    "‑": "-",
    "−": "-",
})


def normalize_term(value: str) -> str:
    """Apply deterministic text cleanup without asserting semantic equivalence."""
    if not isinstance(value, str):
        raise TypeError("term must be a string")

    term = unicodedata.normalize("NFKC", value).translate(_DASHES).strip()
    if len(term) >= 2 and term[0] in _OUTER_QUOTES and term[-1] in _OUTER_QUOTES:
        term = term[1:-1].strip()
    term = re.sub(r"\s+", " ", term)
    return term.casefold()


def deduplicate_exact_terms(terms: list[str]) -> list[str]:
    """Deduplicate only after deterministic normalization, preserving first-seen order."""
    result: list[str] = []
    seen: set[str] = set()
    for raw_term in terms:
        term = normalize_term(raw_term)
        if term and term not in seen:
            seen.add(term)
            result.append(term)
    return result
