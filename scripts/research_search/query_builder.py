"""Compile explicit concept roles into a conservative OpenAlex literal subset."""
from __future__ import annotations

import hashlib
import json
import re

from .keyword_normalizer import normalize_term
from .models import ConceptGroup, SearchPlan

ROLES = {"input", "object", "task", "method", "application"}
ROLE_ALIASES = {"input_modality": "input", "research_object": "object", "research_task": "task"}


def _quote(term: str) -> str:
    if not isinstance(term, str) or not term.strip():
        raise ValueError("query terms must be non-empty strings")
    if re.search(r'[\x00-\x1f\x7f"\\()*?~:{}\[\]]', term):
        raise ValueError("literal query term contains a reserved operator or control character")
    return f'"{" ".join(term.split())}"'


def _group_query(group: ConceptGroup) -> str:
    seen: set[str] = set()
    terms: list[str] = []
    if not isinstance(group.terms, list):
        raise ValueError("concept terms must be an array")
    for term in group.terms:
        quoted = _quote(term)
        key = normalize_term(term)
        if key not in seen:
            terms.append(quoted)
            seen.add(key)
    if not terms:
        raise ValueError(f"concept group {group.group_id!r} has no usable terms")
    return f"({' OR '.join(terms)})"


def build_query(groups: list[ConceptGroup]) -> str:
    if not groups:
        raise ValueError("at least one concept group is required")
    return " AND ".join(_group_query(group) for group in groups)


def _plan(strategy: str, groups: list[ConceptGroup], *, applicable: bool = True) -> SearchPlan:
    ids = [group.group_id for group in groups]
    logic = {"op": "AND", "groups": ids}
    serialized = [{"group_id": g.group_id, "label": g.label, "terms": g.terms,
                   "role": ROLE_ALIASES.get(g.role or g.group_id, g.role or g.group_id)} for g in groups]
    digest = hashlib.sha256(json.dumps([strategy, serialized], sort_keys=True).encode()).hexdigest()[:12]
    return SearchPlan(strategy=strategy, database="openalex", group_ids=ids,
                      query=build_query(groups), plan_id=f"plan-{digest}", logic=logic,
                      groups=serialized, status="planned" if applicable else "not_applicable",
                      reason=None if applicable else "No method specified; focused query shown only as reference, not a distinct method search.")


def build_strategy_plans(groups: list[ConceptGroup]) -> list[SearchPlan]:
    by_role: dict[str, ConceptGroup] = {}
    seen_ids: set[str] = set()
    for group in groups:
        role = ROLE_ALIASES.get(group.role or group.group_id, group.role or group.group_id)
        if role not in ROLES:
            raise ValueError(f"unknown concept role {role!r}; specify input/object/task/method/application")
        if role in by_role or group.group_id in seen_ids:
            raise ValueError("duplicate concept role or group ID")
        _group_query(group)
        by_role[role] = group
        seen_ids.add(group.group_id)
    core = [by_role[role] for role in ("input", "object", "task") if role in by_role]
    if len(core) < 2:
        raise ValueError("at least two core concept roles (input/object/task) are required")
    exploratory = core[:2]
    method = [by_role["method"]] if "method" in by_role else []
    return [_plan("exploratory", exploratory), _plan("focused", core),
            _plan("method_specific", core + method, applicable=bool(method))]
