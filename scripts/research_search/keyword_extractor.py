"""Extract bounded, field-preserving observations from paper metadata."""
from __future__ import annotations

from dataclasses import replace
import re

from .keyword_normalizer import normalize_term
from .models import Paper, TermOccurrence


# Keep the extractor deterministic and bounded.  These are observations from
# fields, not semantic classifications or synonym expansion.
_TOKEN_RE = re.compile(r"[\w]+(?:[-'][\w]+)*", re.UNICODE)
_BOUNDARY_RE = re.compile(r"[^\w\s'-]+", re.UNICODE)
_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "been", "being", "by",
    "for", "from", "in", "into", "is", "it", "of", "on", "or", "our",
    "that", "the", "their", "these", "this", "those", "to", "using", "was",
    "were", "we", "with", "without", "method", "methods", "study", "studies",
}
_MAX_TOKENS_PER_FIELD = 512
_MAX_CANDIDATES_PER_FIELD = 192
_MAX_NGRAM_SIZE = 3


def _segments(text: str) -> list[list[tuple[str, int, int]]]:
    """Return token spans split at punctuation, preserving source offsets."""
    if not isinstance(text, str) or not text:
        return []
    segments: list[list[tuple[str, int, int]]] = []
    current: list[tuple[str, int, int]] = []
    token_count = 0
    for match in _TOKEN_RE.finditer(text):
        if token_count >= _MAX_TOKENS_PER_FIELD:
            break
        # Any punctuation between the previous token and this token is a hard
        # boundary. Hyphens/apostrophes remain part of a token by _TOKEN_RE.
        if current:
            gap = text[current[-1][2] : match.start()]
            if _BOUNDARY_RE.search(gap):
                segments.append(current)
                current = []
        current.append((match.group(0), match.start(), match.end()))
        token_count += 1
    if current:
        segments.append(current)
    return segments


def _phrase_ngrams(text: str, max_size: int = _MAX_NGRAM_SIZE) -> list[tuple[str, str]]:
    """Generate bounded contiguous observations and their exact source spans."""
    phrases: list[tuple[str, str]] = []
    seen: set[str] = set()
    for segment in _segments(text):
        for size in range(1, min(max_size, len(segment)) + 1):
            for start in range(0, len(segment) - size + 1):
                window = segment[start : start + size]
                tokens = [item[0] for item in window]
                normalized_tokens = [normalize_term(token) for token in tokens]
                if not normalized_tokens or all(token in _STOPWORDS for token in normalized_tokens):
                    continue
                if normalized_tokens[0] in _STOPWORDS or normalized_tokens[-1] in _STOPWORDS:
                    continue
                original = text[window[0][1] : window[-1][2]]
                term = normalize_term(original)
                if not term or term in seen:
                    continue
                seen.add(term)
                phrases.append((term, original))
                if len(phrases) >= _MAX_CANDIDATES_PER_FIELD:
                    return phrases
    return phrases


def _append_occurrences(
    output: list[TermOccurrence],
    terms: list[tuple[str, str]] | list[str],
    source_field: str,
    *,
    evidence_status: str,
) -> None:
    seen = {(item.term, item.source_field) for item in output}
    for item in terms:
        if isinstance(item, tuple):
            term, original_term = item
        else:
            original_term = item.strip() if isinstance(item, str) else ""
            term = normalize_term(original_term)
        if not isinstance(term, str) or not term:
            continue
        key = (term, source_field)
        if key in seen:
            continue
        output.append(TermOccurrence(term=term, source_field=source_field,
                                     evidence_status=evidence_status,
                                     original_term=original_term))
        seen.add(key)


def extract_terms(paper: Paper) -> list[TermOccurrence]:
    """Extract observable, contiguous terms while preserving field provenance.

    Title and abstract candidates are bounded contiguous n-grams split at
    punctuation. Author/database keyword values are retained as supplied. No
    semantic equivalence, synonym expansion, or automatic query adoption is
    performed here.
    """
    occurrences: list[TermOccurrence] = []
    _append_occurrences(occurrences, _phrase_ngrams(paper.title or ""), "title",
                        evidence_status="observed_in_paper")
    _append_occurrences(occurrences, _phrase_ngrams(paper.abstract or ""), "abstract",
                        evidence_status="observed_in_paper")
    _append_occurrences(occurrences, paper.author_keywords, "author_keywords",
                        evidence_status="observed_in_paper")
    _append_occurrences(occurrences, paper.database_keywords, "database_keywords",
                        evidence_status="database_assigned")
    return [replace(item, original_term=item.original_term or item.term) for item in occurrences]
