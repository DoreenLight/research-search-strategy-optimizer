from research_search.keyword_normalizer import (
    normalize_term,
    deduplicate_exact_terms,
)


def test_normalize_term_preserves_scientific_hyphenated_terms():
    assert normalize_term("  Surface–Electromyography  ") == "surface-electromyography"


def test_normalize_term_removes_outer_quotes_and_collapses_spaces():
    assert normalize_term('  "Joint   Angle"  ') == "joint angle"


def test_deduplicate_exact_terms_does_not_claim_semantic_equivalence():
    terms = ["sEMG", "semg", "surface electromyography", "intramuscular electromyography"]

    assert deduplicate_exact_terms(terms) == [
        "semg",
        "surface electromyography",
        "intramuscular electromyography",
    ]
