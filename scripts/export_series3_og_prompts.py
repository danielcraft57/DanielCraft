#!/usr/bin/env python3
"""Exporte prompts + manifest pour les 3 series API / Cyber / UX-UI."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SERIES = (
    "api-rest-graphql-serie",
    "cybersecurite-secops-serie",
    "ux-ui-serie",
)


def main() -> None:
    ordered_slugs: list[str] = []
    for name in SERIES:
        data = json.loads(
            (ROOT / "blog" / "content" / "collections" / f"{name}.json").read_text(
                encoding="utf-8"
            )
        )
        ordered_slugs.extend(data.get("articles") or data.get("order") or [])

    manifest = json.loads(
        (ROOT / "scripts" / "_blog_og_manifest.json").read_text(encoding="utf-8")
    )
    by_slug = {it["slug"]: it for it in manifest}
    ordered = [by_slug[s] for s in ordered_slugs if s in by_slug]

    out_m = ROOT / "scripts" / "_blog_og_series3_manifest.json"
    out_m.write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Prompts OG — séries API REST/GraphQL, Cybersécurité, UX/UI",
        "",
        f"Manifest pour **{len(ordered)}** articles (régénération).",
        "",
        "**Format :** 1200×630 px (ratio 1.91:1), JPG puis WebP.",
        "**Dossier cible :** `assets/images/og/`",
        "**Style :** technique, premium, informatique (charte DanielCraft).",
        "",
        "## Installation",
        "",
        "```bash",
        "python scripts/install_ai_generated_blog_og.py  # lit Cursor assets + manifest",
        "python scripts/install_blog_article_banners.py",
        "python blog/build_blog.py",
        "```",
        "",
        f"Manifest : `scripts/_blog_og_series3_manifest.json`",
        "",
        "---",
        "",
    ]
    for i, it in enumerate(ordered, 1):
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

    doc = ROOT / "docs" / "prompt_og_images_articles_series3.md"
    doc.write_text("\n".join(lines), encoding="utf-8")
    print(f"[DOC] {doc.relative_to(ROOT)} ({len(ordered)} prompts)")
    print(f"[JSON] {out_m.relative_to(ROOT)}")
    for it in ordered:
        print(it["slug"])


if __name__ == "__main__":
    main()
