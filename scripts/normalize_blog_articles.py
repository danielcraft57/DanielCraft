#!/usr/bin/env python3
"""
Normalise les articles du blog.

Objectifs :
- Supprimer les blocs de front matter dupliques colles au milieu des articles
  (pattern: une ligne '---' suivie immediatement de 'title:'), en tronquant la
  partie dupliquee.
- Repartir des dates plus "humaines" et espacees sur l'ensemble des articles,
  en respectant l'ordre des series (Docker, Kubernetes, CI/CD) et en etalant
  les autres themes (communication, marketing, SEO, GEO).

Usage (depuis la racine DanielCraftFr) :
    python scripts/normalize_blog_articles.py
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


BASE_DIR = Path(__file__).resolve().parent.parent
ARTICLES_DIR = BASE_DIR / "blog" / "content" / "articles"
COLLECTIONS_DIR = BASE_DIR / "blog" / "content" / "collections"


@dataclass(frozen=True)
class ScheduleRule:
    """Regle de planification (date depart, pas en jours, ordre des slugs)."""

    start: date
    step_pattern_days: List[int]
    slugs: List[str]


FRONT_MATTER_START = "---\n"
FRONT_MATTER_BOUNDARY = "\n---\n"


def _read_json(path: Path) -> dict:
    """Lit un fichier JSON et retourne un dict."""
    return json.loads(path.read_text(encoding="utf-8"))


def _load_collection_slugs(collection_id: str) -> List[str]:
    """Charge l'ordre des slugs depuis une collection JSON."""
    path = COLLECTIONS_DIR / f"{collection_id}.json"
    data = _read_json(path)
    slugs = data.get("articles", [])
    if not isinstance(slugs, list) or not all(isinstance(x, str) for x in slugs):
        raise ValueError(f"Collection invalide: {path}")
    return slugs


def _list_article_slugs() -> List[str]:
    """Liste tous les slugs d'articles (nom de fichier sans extension)."""
    return sorted(p.stem for p in ARTICLES_DIR.glob("*.md"))


def _extract_front_matter(text: str) -> Tuple[Optional[str], str]:
    """
    Extrait le front matter si present.

    Retourne (front_matter, body). front_matter contient les delimiteurs ---.
    """
    if not text.startswith(FRONT_MATTER_START):
        return None, text
    end_idx = text.find(FRONT_MATTER_BOUNDARY, len(FRONT_MATTER_START))
    if end_idx == -1:
        return None, text
    end_idx = end_idx + len(FRONT_MATTER_BOUNDARY) - 1  # garder le dernier \n
    front = text[: end_idx + 1]
    body = text[end_idx + 1 :]
    return front, body


def _truncate_duplicated_front_matter(body: str) -> Tuple[str, bool]:
    """
    Tronque le corps si on detecte un second front matter YAML colle.

    Pattern cherche : '\n---\n' suivi de 'title:' en debut de ligne.
    On garde uniquement la partie avant ce bloc.
    """
    marker = "\n---\n"
    pos = 0
    while True:
        idx = body.find(marker, pos)
        if idx == -1:
            return body, False
        # verifier que le prochain contenu ressemble a du YAML front matter
        after = body[idx + len(marker) :]
        if after.startswith("title:"):
            kept = body[:idx].rstrip() + "\n"
            return kept, True
        pos = idx + len(marker)


def _set_date_in_front_matter(front: str, new_date: date) -> Tuple[str, bool]:
    """
    Met a jour la ligne 'date:' dans le front matter.
    Retourne (front_modifie, changed).
    """
    lines = front.splitlines(keepends=True)
    if not lines or not lines[0].strip() == "---":
        return front, False

    in_yaml = True
    changed = False
    out: List[str] = []
    for line in lines:
        if in_yaml and line.strip() == "---" and out:
            in_yaml = False
        if in_yaml and line.startswith("date:"):
            desired = f"date: {new_date.isoformat()}\n"
            if line != desired:
                out.append(desired)
                changed = True
            else:
                out.append(line)
            continue
        out.append(line)
    return "".join(out), changed


def _build_schedule_rules() -> List[ScheduleRule]:
    """Construit les regles de dates pour les articles connus."""
    docker = _load_collection_slugs("docker-serie")
    k8s = _load_collection_slugs("kubernetes-serie")
    cicd = _load_collection_slugs("ci-cd-serie")
    aws = _load_collection_slugs("aws-serie") if (COLLECTIONS_DIR / "aws-serie.json").exists() else []
    api = _load_collection_slugs("api-rest-graphql-serie") if (COLLECTIONS_DIR / "api-rest-graphql-serie.json").exists() else []
    uxui = _load_collection_slugs("ux-ui-serie") if (COLLECTIONS_DIR / "ux-ui-serie.json").exists() else []
    cyber = _load_collection_slugs("cybersecurite-secops-serie") if (COLLECTIONS_DIR / "cybersecurite-secops-serie.json").exists() else []

    all_slugs = _list_article_slugs()

    communication = sorted([s for s in all_slugs if s.startswith("communication-")])
    marketing = sorted([s for s in all_slugs if s.startswith("marketing-")])
    seo = sorted([s for s in all_slugs if s.startswith("seo-")])
    geo = sorted([s for s in all_slugs if s.startswith("geo-")])
    # l'article outils-geo est range avec GEO
    if "outils-geo-audit-suivi-citations" in all_slugs and "outils-geo-audit-suivi-citations" not in geo:
        geo.append("outils-geo-audit-suivi-citations")

    # Rythme "humain" : mardi/jeudi (cycle +2 / +5 jours)
    tue_thu = [2, 5]

    return [
        # 2024 : thèmes business (communication/marketing/SEO/GEO)
        ScheduleRule(start=date(2024, 3, 5), step_pattern_days=tue_thu, slugs=communication),
        ScheduleRule(start=date(2024, 5, 7), step_pattern_days=tue_thu, slugs=marketing),
        ScheduleRule(start=date(2024, 7, 2), step_pattern_days=tue_thu, slugs=seo),
        ScheduleRule(start=date(2024, 9, 3), step_pattern_days=tue_thu, slugs=geo),

        # 2024/2025 : séries techniques (conteneurs, k8s, CI/CD, cloud)
        ScheduleRule(start=date(2024, 11, 5), step_pattern_days=tue_thu, slugs=docker),
        ScheduleRule(start=date(2025, 1, 7), step_pattern_days=tue_thu, slugs=k8s),
        ScheduleRule(start=date(2025, 3, 4), step_pattern_days=tue_thu, slugs=cicd),
        ScheduleRule(start=date(2025, 5, 6), step_pattern_days=tue_thu, slugs=aws),

        # 2025 : comparatifs & produit
        ScheduleRule(start=date(2025, 7, 1), step_pattern_days=tue_thu, slugs=api),
        ScheduleRule(start=date(2025, 9, 2), step_pattern_days=tue_thu, slugs=uxui),
        ScheduleRule(start=date(2025, 11, 4), step_pattern_days=tue_thu, slugs=cyber),
    ]


def _make_date_map(rules: List[ScheduleRule], all_slugs: List[str]) -> Dict[str, date]:
    """Genere un mapping slug -> date a partir des regles."""
    mapping: Dict[str, date] = {}
    for rule in rules:
        d = rule.start
        step_idx = 0
        for slug in rule.slugs:
            mapping[slug] = d
            if rule.step_pattern_days:
                d = d + timedelta(days=rule.step_pattern_days[step_idx % len(rule.step_pattern_days)])
                step_idx += 1

    # fallback pour les slugs non couverts (au cas ou)
    remaining = [s for s in all_slugs if s not in mapping]
    if remaining:
        # on se cale apres la derniere date connue
        last = max(mapping.values()) if mapping else date(2024, 1, 1)
        d = last + timedelta(days=2)
        step_pattern = [2, 5]
        step_idx = 0
        for slug in sorted(remaining):
            mapping[slug] = d
            d = d + timedelta(days=step_pattern[step_idx % len(step_pattern)])
            step_idx += 1
    return mapping


def normalize_one(path: Path, desired_date: date) -> Tuple[bool, List[str]]:
    """Normalise un fichier et retourne (changed, actions)."""
    original = path.read_text(encoding="utf-8")
    front, body = _extract_front_matter(original)
    actions: List[str] = []

    text = original
    changed_any = False

    if front is not None:
        new_body, truncated = _truncate_duplicated_front_matter(body)
        if truncated:
            actions.append("tronque-duplicat-front-matter")
            changed_any = True
        new_front, changed_date = _set_date_in_front_matter(front, desired_date)
        if changed_date:
            actions.append("date-front-matter")
            changed_any = True
        text = new_front + new_body
    else:
        # si pas de front matter, on ne touche qu'au duplicat eventuel (rare)
        new_body, truncated = _truncate_duplicated_front_matter(body)
        if truncated:
            actions.append("tronque-duplicat-front-matter")
            changed_any = True
            text = new_body

    if not text.endswith("\n"):
        text = text + "\n"
        changed_any = True
        actions.append("newline-final")

    if changed_any and text != original:
        path.write_text(text, encoding="utf-8")
        return True, actions
    return False, actions


def main() -> int:
    if not ARTICLES_DIR.exists():
        print(f"[ERREUR] Dossier introuvable: {ARTICLES_DIR}")
        return 1

    all_slugs = _list_article_slugs()
    rules = _build_schedule_rules()
    date_map = _make_date_map(rules, all_slugs)

    changed = 0
    truncated = 0
    for slug in all_slugs:
        path = ARTICLES_DIR / f"{slug}.md"
        did_change, actions = normalize_one(path, date_map[slug])
        if did_change:
            changed += 1
            if "tronque-duplicat-front-matter" in actions:
                truncated += 1
            print(f"[OK] {slug}: {', '.join(actions)} -> {date_map[slug].isoformat()}")

    print(f"\nTermine. Fichiers modifies: {changed}. Tronques (duplicats): {truncated}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

