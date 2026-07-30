#!/usr/bin/env python3
"""Genere le manifest et le doc de prompts OG pour tous les articles du blog.

Usage :
  python scripts/generate_all_blog_og_prompts.py
  python scripts/generate_all_blog_og_prompts.py --legacy-non-ia
      → docs/prompt_og_images_articles_legacy.md
         + scripts/_blog_og_legacy_manifest.json
         (hors ia-*, OG absente ou mtime < 2026-07-17)
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "blog" / "content" / "articles"
OG_DIR = ROOT / "assets" / "images" / "og"
DOCS = ROOT / "docs"
MANIFEST = ROOT / "scripts" / "_blog_og_manifest.json"
OUT_DOC = DOCS / "prompt_og_images_articles_all.md"
LEGACY_MANIFEST = ROOT / "scripts" / "_blog_og_legacy_manifest.json"
LEGACY_DOC = DOCS / "prompt_og_images_articles_legacy.md"

# Articles ia-* rafraichis le 17/07 : exclus du lot « legacy »
IA_CUTOFF = datetime(2026, 7, 17)

SERIES_THEMES: dict[str, str] = {
    "seo-serie": "dashboard SEO, SERP, analytics, audit technique et contenu",
    "geo-serie": "moteur generatif, citations, visibilite IA, architecture de contenu",
    "marketing-digital-serie": "analytics marketing, campagnes, conversion, attribution",
    "ux-ui-serie": "design system, maquettes UI, parcours utilisateur, composants",
    "cybersecurite-secops-serie": "SOC, logs, menaces, pare-feu, securite applicative",
    "kubernetes-serie": "cluster Kubernetes, pods, services, orchestration",
    "docker-serie": "conteneurs Docker, images, reseaux, runtime",
    "ci-cd-serie": "pipeline CI/CD, build, test, deploiement, GitOps",
    "aws-serie": "architecture cloud AWS, compute, stockage, reseau, securite",
    "api-rest-graphql-serie": "API REST, GraphQL, endpoints, documentation, schemas",
    "communication-serie": "workflow editorial, collaboration, messagerie, contenu",
    "design-patterns-serie": "architecture logicielle, design patterns, UML, modules",
    "ia-prompts-serie": "prompt engineering, console, contexte, sortie modele",
    "ia-chatgpt-serie": "interface conversationnelle, taches, notes, checklists",
    "ia-claude-serie": "assistant de travail, documents, connecteurs, analyse",
    "ia-gemini-serie": "AI Studio, notebooks, sources, traitement Google",
    "ia-agents-serie": "workflow d'automatisation, orchestration, agents",
    "ia-images-serie": "pipeline image, calques, generation visuelle technique",
    "ia-formations-serie": "parcours d'apprentissage, modules, progression",
    "ia-nocode-serie": "editeur visuel, composants UI, flux no-code",
    "ia-outils-serie": "comparatif d'outils, interfaces cote a cote, mesures",
    "ia-metiers-serie": "tendances metiers, data, postes de travail modernes",
    "ia-productivite-serie": "tableau de bord, calendrier, automatisations, suivi",
}

STYLE_BASE = (
    "Visuel Open Graph technique et premium pour un article informatique, {theme}. "
    "Composition complexe mais lisible, avec plusieurs panneaux UI, elements logiciels, "
    "flux de donnees ou modules techniques selon le sujet. "
    "Palette claire premium : fond #f5f7fb vers #e9eef6, bleus #2563eb et #60a5fa, "
    "encre #0f172a, accent rouge #dc2626. "
    'Bandeau bas sombre avec titre en francais "{title}" et marque "DanielCraft". '
    "Style plus technique, plus logiciel, plus architecture web, moins cartoon, "
    "moins simplifie, pas de mascotte naive, pas de flat design vide. "
    "Si un humain apparait, il reste secondaire et sobre. "
    "Ratio 1.91:1, 1200x630. Export JPG puis convertir en WebP."
)


def parse_frontmatter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    data = yaml.safe_load(text[3:end].strip())
    return data if isinstance(data, dict) else None


def load_custom_prompts() -> dict[str, str]:
    custom: dict[str, str] = {}
    for doc in sorted(DOCS.glob("prompt_og_images_articles_*.md")):
        if doc.name in {
            "prompt_og_images_articles_all.md",
            "prompt_og_images_articles_legacy.md",
        }:
            continue
        text = doc.read_text(encoding="utf-8")
        for m in re.finditer(
            r"^##\s+([\w.-]+-1200x630)\.jpg\s*\n+(?:Article\s*:[^\n]*\n+)?```\s*\n(.*?)\n```",
            text,
            flags=re.M | re.S,
        ):
            custom[m.group(1)] = m.group(2).strip()
    return custom


def prompt_for(slug: str, title: str, series: str, custom: dict[str, str]) -> str:
    stem = f"{slug}-1200x630"
    if stem in custom:
        return custom[stem]
    theme = SERIES_THEMES.get(series, "workspace technique, dashboards et outils logiciels")
    short = title.replace('"', "'")[:48]
    return STYLE_BASE.format(theme=theme, title=short)


def og_needs_legacy_refresh(og_name: str, slug: str) -> bool:
    """True si hors ia-* et (fichier absent ou plus ancien que le cutoff)."""
    if slug.startswith("ia-"):
        return False
    path = OG_DIR / og_name
    if not path.is_file():
        # essayer stem standard
        alt = OG_DIR / f"{slug}-1200x630.jpg"
        path = alt if alt.is_file() else path
    if not path.is_file():
        return True
    mtime = datetime.fromtimestamp(path.stat().st_mtime)
    return mtime < IA_CUTOFF


def write_doc(
    items: list[dict],
    out_doc: Path,
    title: str,
    install_extra: str = "",
) -> None:
    blocks = [
        f"## {it['slug']}-1200x630.jpg\n\nArticle : {it['title']}\n\n```\n{it['prompt']}\n```\n"
        for it in items
    ]
    header = f"""# {title}

Manifest pour **{len(items)}** articles.

**Format :** 1200x630 px (ratio 1.91:1), JPG puis WebP.
**Dossier cible :** `assets/images/og/`
**Style :** technique, premium, informatique, coherent sur tout le blog.
{install_extra}
## Installation

1. Genere chaque image avec le prompt ci-dessous (Flux, ChatGPT Images, Recraft...).
2. Place le JPG dans `assets/images/og/` ou dans le dossier assets Cursor.
3. Lance :

```bash
python scripts/install_ai_generated_blog_og.py
python scripts/install_blog_article_banners.py
python build.py
```

---

"""
    out_doc.write_text(header + "\n---\n\n".join(blocks), encoding="utf-8")


def collect_items(custom: dict[str, str]) -> list[dict]:
    items: list[dict] = []
    for path in sorted(ARTICLES.glob("*.md")):
        meta = parse_frontmatter(path)
        if not meta:
            continue
        slug = path.stem
        title = str(meta.get("title") or slug).strip()
        series = str(meta.get("series") or "").strip()
        og = str(meta.get("og_image") or f"{slug}-1200x630.jpg").strip()
        pr = prompt_for(slug, title, series, custom)
        items.append(
            {
                "slug": slug,
                "title": title,
                "series": series,
                "og": og,
                "prompt": pr,
            }
        )
    return items


def main() -> None:
    parser = argparse.ArgumentParser(description="Prompts OG blog DanielCraft")
    parser.add_argument(
        "--legacy-non-ia",
        action="store_true",
        help="Doc + manifest uniquement hors ia-* avec OG absente ou mtime < 2026-07-17",
    )
    args = parser.parse_args()

    custom = load_custom_prompts()
    all_items = collect_items(custom)

    MANIFEST.write_text(json.dumps(all_items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_doc(all_items, OUT_DOC, "Prompts OG / WebP - Tous les articles du blog")
    print(f"[DOC] {OUT_DOC.relative_to(ROOT)} ({len(all_items)} prompts)")
    print(f"[JSON] {MANIFEST.relative_to(ROOT)}")
    print(f"custom_prompts_reused={len(custom)}")

    if args.legacy_non_ia:
        legacy = [
            it
            for it in all_items
            if og_needs_legacy_refresh(it["og"], it["slug"])
        ]
        LEGACY_MANIFEST.write_text(
            json.dumps(legacy, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        extra = (
            "\n**Lot legacy :** articles hors `ia-*`, OG absente ou anterieure au "
            f"{IA_CUTOFF.date().isoformat()} (nouveau style technique).\n"
        )
        write_doc(
            legacy,
            LEGACY_DOC,
            "Prompts OG / WebP - Articles legacy (hors series IA rafraichies)",
            install_extra=extra,
        )
        print(f"[DOC] {LEGACY_DOC.relative_to(ROOT)} ({len(legacy)} prompts)")
        print(f"[JSON] {LEGACY_MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
