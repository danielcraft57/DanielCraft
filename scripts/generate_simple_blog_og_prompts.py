#!/usr/bin/env python3
"""Genere prompts + manifest OG pour les articles simplifies (style debutant).

Sans bannieres : le hero article = l'image OG uniquement.

Usage:
  python scripts/generate_simple_blog_og_prompts.py

Puis generer les JPG via le doc, puis:
  python scripts/install_ai_generated_blog_og.py
  # (utilise scripts/_blog_og_simple_manifest.json si --simple)

  python scripts/install_ai_generated_blog_og.py --simple
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "blog" / "content" / "articles"
DOCS = ROOT / "docs"
MANIFEST = ROOT / "scripts" / "_blog_og_simple_manifest.json"
OUT_DOC = DOCS / "prompt_og_images_articles_simple.md"

# Series deja passees en ton simple
SERIES = {
    "api-rest-graphql-serie",
    "cybersecurite-secops-serie",
    "ux-ui-serie",
    "docker-serie",
    "aws-serie",
    "ci-cd-serie",
    "kubernetes-serie",
    "seo-serie",
    "geo-serie",
    "marketing-digital-serie",
    "communication-serie",
    "design-patterns-serie",
}

SERIES_THEMES: dict[str, str] = {
    "api-rest-graphql-serie": (
        "metaphore restaurant / menu, echanges site-serveur, bulles de dialogue claires, "
        "icones simples API"
    ),
    "cybersecurite-secops-serie": (
        "metaphore maison et cles, bouclier doux, alarme, cadenas, sans violence ni gore"
    ),
    "ux-ui-serie": (
        "ecrans amicaux, parcours utilisateur, smileys sobres d'etats UI, design accueillant"
    ),
    "docker-serie": (
        "metaphore recette et gateau / boites empilees, conteneurs coloris sobres, atelier propre"
    ),
    "aws-serie": (
        "nuages stylises, batiments de services, carte simple du cloud, ambiance claire"
    ),
    "ci-cd-serie": (
        "chaine de montage ludique et propre, tapis roulant, cases verte/rouge, sans usine sombre"
    ),
    "kubernetes-serie": (
        "boites sur des plateaux, chef d'orchestre doux, cluster explique en image simple"
    ),
    "seo-serie": (
        "loupe, pages web rangees, fleches vers Google stylise, tableau simple et accueillant"
    ),
    "geo-serie": (
        "bulles de conversation IA, citations, etoiles de confiance, ambiance pedagogique"
    ),
    "marketing-digital-serie": (
        "entonnoir simple, canaux clairs, tableau de bord accueillant, sans dashboard charge"
    ),
    "communication-serie": (
        "bulles de dialogue, megaphone doux, charte couleurs, ambiance humaine et claire"
    ),
    "design-patterns-serie": (
        "blocs de Lego / pieces qui s'assemblent, schemas simples, atelier code accueillant"
    ),
}

STYLE = (
    "Visuel Open Graph attirant et pedagogique pour un article grand public / debutant, {theme}. "
    "Une seule idee visuelle claire, composition simple et accueillante (pas un dashboard charge). "
    "Metaphores du quotidien, formes lisibles, espace blanc genereux. "
    "Palette claire premium DanielCraft : fond #f5f7fb vers #e9eef6, bleus #2563eb et #60a5fa, "
    "encre #0f172a, accent rouge #dc2626 utilise avec parcimonie. "
    'Bandeau bas sombre avec le titre EXACT en francais "{title}" (lisible, ne pas tronquer trop tot) '
    'et marque "DanielCraft". '
    "Style friendly-premium : clair, moderne, rassurant, pour quelqu'un qui debute. "
    "Pas de jargon illisible dans l'image, pas de mascotte enfantine, pas de flat design vide, "
    "pas de collage de 10 panneaux techniques. "
    "Ratio 1.91:1, 1200x630. Export JPG (puis WebP a l'install). "
    "PAS de banniere separee : cette image sert aussi de hero article."
)


def parse_fm(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    try:
        return yaml.safe_load(text[3:end]) or {}
    except Exception:
        # fallback title/og via regex if YAML broken
        title_m = re.search(r'^title:\s*"(.*)"\s*$', text[3:end], re.M)
        og_m = re.search(r'^og_image:\s*(\S+)', text[3:end], re.M)
        series_m = re.search(r'^series:\s*(\S+)', text[3:end], re.M)
        return {
            "title": title_m.group(1) if title_m else path.stem,
            "og_image": og_m.group(1) if og_m else f"{path.stem}-1200x630.jpg",
            "series": series_m.group(1) if series_m else "",
        }


def collect() -> list[dict]:
    items = []
    for path in sorted(ARTICLES.glob("*.md")):
        meta = parse_fm(path)
        if not meta:
            continue
        series = str(meta.get("series") or "")
        if series not in SERIES:
            continue
        slug = path.stem
        title = str(meta.get("title") or slug)
        og = str(meta.get("og_image") or f"{slug}-1200x630.jpg").strip()
        theme = SERIES_THEMES.get(series, "sujet informatique explique simplement")
        # titre bandeau : max ~70 chars pour lisibilite
        title_band = title if len(title) <= 72 else title[:69].rstrip() + "…"
        prompt = STYLE.format(theme=theme, title=title_band)
        items.append(
            {
                "slug": slug,
                "title": title,
                "series": series,
                "og": og,
                "prompt": prompt,
            }
        )
    return items


def write_doc(items: list[dict]) -> None:
    lines = [
        "# Prompts OG — articles simplifies (ton debutant)",
        "",
        f"**{len(items)}** articles. Style : clair, attirant, pedagogique.",
        "**Format :** 1200×630 (1.91:1), JPG puis WebP a l'install.",
        "**Cible :** `assets/images/og/`",
        "**Pas de bannieres** : l'OG sert aussi de hero article.",
        "",
        "## Installation",
        "",
        "```bash",
        "# 1. Generer les JPG (IA) avec les prompts ci-dessous",
        "# 2. Les deposer dans le dossier Cursor assets (voir install_ai_generated_blog_og.py)",
        "python scripts/install_ai_generated_blog_og.py --simple",
        "python blog/build_blog.py --output dist/blog",
        "# NE PAS lancer install_blog_article_banners.py",
        "```",
        "",
        f"Manifest : `scripts/_blog_og_simple_manifest.json`",
        "",
        "---",
        "",
    ]
    for i, it in enumerate(items, 1):
        lines.append(f"## {i}. {it['title']}")
        lines.append(f"- slug: `{it['slug']}`")
        lines.append(f"- fichier: `{it['og']}`")
        lines.append("")
        lines.append("```")
        lines.append(it["prompt"])
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")
    OUT_DOC.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    items = collect()
    MANIFEST.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_doc(items)
    print(f"articles={len(items)}")
    print(f"doc={OUT_DOC.relative_to(ROOT)}")
    print(f"manifest={MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
