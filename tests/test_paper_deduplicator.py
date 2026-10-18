from research_search.models import Paper
from research_search.paper_deduplicator import deduplicate_papers


def test_deduplicate_papers_merges_same_doi_and_keeps_richer_record():
    papers = [
        Paper(paper_id="a", title="A study", doi="10.1000/ABC", abstract=None),
        Paper(paper_id="b", title="A study", doi="https://doi.org/10.1000/abc", abstract="Useful abstract"),
    ]

    result = deduplicate_papers(papers)

    assert len(result.papers) == 1
    assert result.papers[0].paper_id == "b"
    assert result.merged_ids == {"a": "b"}


def test_same_title_without_reliable_identifier_is_merged_by_title_fingerprint():
    papers = [
        Paper(paper_id="a", title="A Study: on  sEMG"),
        Paper(paper_id="b", title="a study on semg"),
    ]

    result = deduplicate_papers(papers)

    assert len(result.papers) == 1
    assert result.merged_ids == {"a": "b"}


def test_conflicting_dois_with_same_title_are_not_silently_merged():
    papers = [
        Paper(paper_id="a", title="Same title", doi="10.1000/one"),
        Paper(paper_id="b", title="Same title", doi="10.1000/two"),
    ]

    result = deduplicate_papers(papers)

    assert len(result.papers) == 2
    assert result.conflicts[0].kind == "title_identifier_conflict"
