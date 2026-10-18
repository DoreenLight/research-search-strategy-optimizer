from research_search.models import Paper
from research_search.paper_deduplicator import deduplicate_papers


def test_replacement_updates_all_identifier_aliases_and_resolves_chains():
    papers = [Paper("a", "Title", doi="10.1/x", openalex_id="W1"),
              Paper("b", "Title", doi="10.1/x", openalex_id="https://openalex.org/W1", abstract="abstract"),
              Paper("c", "Title", openalex_id="W1", abstract="abstract", authors=["A"], database_keywords=["term"])]
    result = deduplicate_papers(papers)
    assert len(result.papers) == 1
    assert result.papers[0].paper_id == "c"
    assert result.merged_ids == {"a": "c", "b": "c"}


def test_shared_openalex_id_but_conflicting_doi_is_flagged():
    result = deduplicate_papers([Paper("a", "Title", openalex_id="W1", doi="10.1/a"),
                                Paper("b", "Title", openalex_id="W1", doi="10.1/b")])
    assert len(result.papers) == 2
    assert result.conflicts[0].kind == "identifier_conflict"


def test_blank_titles_do_not_merge_unidentified_records():
    assert len(deduplicate_papers([Paper("a", ""), Paper("b", "")]).papers) == 2
