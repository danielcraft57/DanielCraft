#!/usr/bin/env python3
"""
Genere les images Open Graph (1200x630) du blog DanielCraft.

Usage (racine du projet) :
    python scripts/generate_blog_og_images.py
    python scripts/generate_blog_og_images.py --only blog seo-fondamentaux-referencement-naturel
    python scripts/generate_blog_og_images.py --include-design-patterns
    python scripts/generate_blog_og_images.py --dry-run

Sortie : assets/images/og/blog-1200x630.jpg + assets/images/og/<og_image des articles>
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable

try:
    import yaml
except ImportError:
    print("[ERREUR] pip install PyYAML")
    sys.exit(1)

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from _og_cartoon import CATEGORY_COLORS, render_og_card  # noqa: E402
from generate_site_og_images import _save_jpg  # noqa: E402

BLUE_MID = CATEGORY_COLORS["default"]

BASE_DIR = _SCRIPT_DIR.parent
OG_DIR = BASE_DIR / "assets" / "images" / "og"
ARTICLES_DIR = BASE_DIR / "blog" / "content" / "articles"
COLLECTIONS_DIR = BASE_DIR / "blog" / "content" / "collections"

DESIGN_PATTERNS_SERIES = "design-patterns-serie"

SERIES_META: dict[str, dict[str, str]] = {
    "seo-serie": {"badge": "SEO", "color": "#3d8b72", "scene": "visibilite"},
    "geo-serie": {"badge": "GEO", "color": "#4da9d6", "scene": "assistant"},
    "marketing-digital-serie": {"badge": "Marketing", "color": "#c97b4a", "scene": "catalog"},
    "ux-ui-serie": {"badge": "UX / UI", "color": "#6d5bd6", "scene": "brand"},
    "cybersecurite-secops-serie": {"badge": "Cybersécurité", "color": "#b91c1c", "scene": "report"},
    "kubernetes-serie": {"badge": "Kubernetes", "color": "#0891b2", "scene": "gear"},
    "docker-serie": {"badge": "Docker", "color": "#0e7490", "scene": "gear"},
    "ci-cd-serie": {"badge": "CI/CD", "color": "#5b6fd6", "scene": "process"},
    "aws-serie": {"badge": "AWS", "color": "#ea580c", "scene": "code"},
    "api-rest-graphql-serie": {"badge": "API", "color": "#4f46e5", "scene": "code"},
    "communication-serie": {"badge": "Communication", "color": "#be185d", "scene": "mail"},
    DESIGN_PATTERNS_SERIES: {"badge": "Design Patterns", "color": "#16a34a", "scene": "code"},
}


def _parse_frontmatter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    raw = text[3:end].strip()
    data = yaml.safe_load(raw)
    return data if isinstance(data, dict) else None


def _slug_from_path(path: Path) -> str:
    return path.stem


def _series_badge(series_id: str) -> tuple[str, str, str]:
    meta = SERIES_META.get(series_id, {})
    return meta.get("badge", "Article"), meta.get("color", BLUE_MID), meta.get("scene", "browser")


def _load_collection_titles() -> dict[str, str]:
    titles: dict[str, str] = {}
    if not COLLECTIONS_DIR.is_dir():
        return titles
    for path in COLLECTIONS_DIR.glob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        cid = (data.get("id") or data.get("slug") or path.stem).strip()
        title = (data.get("title") or cid).strip()
        if cid:
            titles[cid] = title
    return titles


def _article_chips(meta: dict) -> list[str]:
    tags = [str(t).strip() for t in (meta.get("tags") or []) if str(t).strip()]
    if tags:
        return tags[:3]
    article_type = str(meta.get("type") or "article").strip()
    return [article_type.replace("_", " ").title()]


def generate_blog_index(dry_run: bool) -> int:
    img = render_og_card(
        title="Blog DanielCraft",
        subtitle="Articles et tutoriels — SEO, GEO, IA, DevOps",
        badge="Blog",
        chips=["SEO", "GEO", "IA"],
        footer="DanielCraft — Articles & tutoriels",
        scene="catalog",
        cta="Lire l'article →",
    )
    _save_jpg(img, OG_DIR / "blog-1200x630.jpg", dry_run)
    return 1


def generate_articles(
    only: set[str] | None,
    dry_run: bool,
    include_design_patterns: bool,
) -> int:
    count = 0
    collection_titles = _load_collection_titles()

    for path in sorted(ARTICLES_DIR.glob("*.md")):
        slug = _slug_from_path(path)
        if only and slug not in only and "articles" not in only:
            continue

        meta = _parse_frontmatter(path)
        if not meta:
            print(f"[WARN] front matter absent : {path.name}")
            continue

        series = str(meta.get("series") or "").strip()
        if series == DESIGN_PATTERNS_SERIES and not include_design_patterns:
            continue

        og_name = str(meta.get("og_image") or f"{slug}-1200x630.jpg").strip()
        if not og_name:
            og_name = f"{slug}-1200x630.jpg"

        badge, color, scene = _series_badge(series)
        if series and series in collection_titles:
            badge = collection_titles[series].split(" - ")[0].split(" — ")[0][:24]

        title = str(meta.get("title") or slug).strip()
        subtitle = str(meta.get("excerpt") or "").strip()
        subtitle = re.sub(r"\s+", " ", subtitle)

        img = render_og_card(
            title=title,
            subtitle=subtitle,
            badge=badge[:24],
            color=color,
            chips=_article_chips(meta),
            footer="DanielCraft — Blog",
            scene=scene,
            cta="Lire l'article →",
        )
        _save_jpg(img, OG_DIR / og_name, dry_run)
        count += 1

    return count


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Genere les images OG du blog")
    parser.add_argument(
        "--only",
        nargs="*",
        help="Filtrer : blog, articles, ou slugs d'articles",
    )
    parser.add_argument(
        "--include-design-patterns",
        action="store_true",
        help="Regenerer aussi la serie Design Patterns (cartes avec diagrammes dediees sinon)",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)
    only = set(args.only) if args.only else None

    total = 0
    if not only or "blog" in only:
        total += generate_blog_index(args.dry_run)
    total += generate_articles(only, args.dry_run, args.include_design_patterns)

    print(f"\n[OK] {total} image(s) OG blog {'simulee(s)' if args.dry_run else 'generee(s)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
