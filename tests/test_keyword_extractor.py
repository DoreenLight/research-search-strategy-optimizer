from research_search.keyword_extractor import extract_terms
from research_search.models import Paper


def test_extract_terms_keeps_field_provenance():
    paper = Paper(
        paper_id="W1",
        title="Surface EMG for joint angle estimation",
        abstract="We predict joint angles from surface electromyography.",
        author_keywords=["sEMG", "joint angle estimation"],
        database_keywords=["electromyography"],
    )

    occurrences = extract_terms(paper)
    by_term = {(item.term, item.source_field) for item in occurrences}

    assert ("semg", "author_keywords") in by_term
    assert ("joint angle estimation", "author_keywords") in by_term
    assert ("electromyography", "database_keywords") in by_term
    assert any(item.source_field == "title" for item in occurrences)
    assert any(item.source_field == "abstract" for item in occurrences)
    assert all(item.original_term for item in occurrences)
    assert all(item.evidence_status == "observed_in_paper" for item in occurrences
               if item.source_field != "database_keywords")
    assert all(item.evidence_status == "database_assigned" for item in occurrences
               if item.source_field == "database_keywords")


def test_extracted_excerpt_is_a_contiguous_source_span_and_stopwords_are_removed():
    paper = Paper(
        paper_id="W2",
        title="Surface EMG, for joint-angle estimation",
        abstract="We This method predicts joint angles.",
    )
    occurrences = extract_terms(paper)
    assert all(item.original_term in getattr(paper, item.source_field) for item in occurrences)
    assert not any(item.term in {"we", "this", "method"} for item in occurrences)
    assert any(item.term == "surface emg" and item.original_term == "Surface EMG" for item in occurrences)
    assert not any(item.term == "emg for joint" for item in occurrences)
