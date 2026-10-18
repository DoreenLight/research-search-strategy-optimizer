"""Conservative identity merging with resolved aliases and explicit conflicts."""
from __future__ import annotations

from dataclasses import dataclass, field, replace
import re
from urllib.parse import unquote

from .keyword_normalizer import normalize_term
from .models import Paper


@dataclass(frozen=True)
class DedupConflict:
    kind: str
    paper_ids: tuple[str, ...]
    message: str


@dataclass
class DeduplicationResult:
    papers: list[Paper]
    merged_ids: dict[str, str] = field(default_factory=dict)
    conflicts: list[DedupConflict] = field(default_factory=list)


def _identifier(value: str | None, kind: str) -> str | None:
    if not value:
        return None
    text = unquote(value).strip().casefold().rstrip("/")
    if kind == "doi":
        text = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", text)
    elif kind == "pmid":
        text = re.sub(r"^(?:https?://pubmed\.ncbi\.nlm\.nih\.gov/|pmid:\s*)", "", text)
    elif kind == "openalex":
        text = text.rsplit("/", 1)[-1]
    return text or None


def _keys(paper: Paper) -> dict[str, str]:
    return {kind: normalized for kind, value in (("doi", paper.doi), ("pmid", paper.pmid),
             ("openalex", paper.openalex_id)) if (normalized := _identifier(value, kind))}


def _title(paper: Paper) -> str:
    return re.sub(r"[^\w]+", "", normalize_term(paper.title))


def _richness(paper: Paper) -> int:
    return sum(bool(value) for value in (paper.abstract, paper.doi, paper.pmid,
               paper.openalex_id, paper.authors, paper.author_keywords, paper.database_keywords))


def deduplicate_papers(papers: list[Paper]) -> DeduplicationResult:
    unique: list[Paper] = []
    aliases: dict[str, str] = {}
    all_keys: dict[str, dict[str, str]] = {}
    conflicts: list[DedupConflict] = []
    for paper in papers:
        keys = _keys(paper)
        matches = [item for item in unique if any(all_keys[item.paper_id].get(k) == v for k, v in keys.items())]
        conflicting = [item for item in matches if any(k in all_keys[item.paper_id] and
                       all_keys[item.paper_id][k] != v for k, v in keys.items())]
        if conflicting or len(matches) > 1:
            conflicts.append(DedupConflict("identifier_conflict", tuple([p.paper_id for p in matches] + [paper.paper_id]),
                                           "Reliable identifiers conflict or bridge existing records; kept separate."))
            unique.append(paper)
            all_keys[paper.paper_id] = keys
            continue
        title_matches = [item for item in unique if _title(paper) and _title(item) == _title(paper)]
        if not matches and title_matches:
            unidentified = [item for item in title_matches if not keys and not all_keys[item.paper_id]]
            if len(unidentified) == 1:
                matches = unidentified
            else:
                conflicts.append(DedupConflict("title_identifier_conflict", (title_matches[0].paper_id, paper.paper_id),
                                               "Same title fingerprint without safe identifier agreement; kept separate."))
        if not matches:
            unique.append(paper)
            all_keys[paper.paper_id] = keys
            continue
        old = matches[0]
        winner, other = (paper, old) if _richness(paper) >= _richness(old) else (old, paper)
        combined_keys = {**all_keys[old.paper_id], **keys}
        winner = replace(winner,
                         doi=winner.doi or other.doi, pmid=winner.pmid or other.pmid,
                         openalex_id=winner.openalex_id or other.openalex_id,
                         abstract=winner.abstract or other.abstract,
                         source_run_ids=list(dict.fromkeys(old.source_run_ids + paper.source_run_ids)))
        unique[unique.index(old)] = winner
        all_keys.pop(old.paper_id, None)
        all_keys[winner.paper_id] = combined_keys
        aliases[other.paper_id] = winner.paper_id
        for alias, target in list(aliases.items()):
            if target == other.paper_id:
                aliases[alias] = winner.paper_id
        aliases.pop(winner.paper_id, None)
    return DeduplicationResult(unique, aliases, conflicts)
