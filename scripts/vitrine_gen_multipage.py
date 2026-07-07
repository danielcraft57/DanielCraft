#!/usr/bin/env python3
"""Génère les vitrines multi-pages (histoires + scénarios) depuis vitrine_scenarios.py."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from vitrine_ai_lib import (
    block_cards,
    block_chapters,
    block_gallery,
    block_story,
    block_timeline,
    build_nav,
    ensure_css,
    esc,
    write_ai_page,
)
from vitrine_scenarios import SCENARIOS


def _render_page(sc: dict, page: dict) -> str:
    parts: list[str] = ["<main>"]
    if page.get("hero"):
        h = page["hero"]
        parts.append(
            f"""<section class="ai-mp-hero">
  <h1>{esc(h["h1"])}</h1>
  <p class="ai-lead">{esc(h["lead"])}</p>
  <figure class="ai-mp-hero-img"><img src="images/{esc(h["img"])}" alt="{esc(h.get("alt", h["h1"]))}" fetchpriority="high" decoding="async"></figure>
</section>"""
        )
    if page.get("story"):
        t, paras = page["story"]
        parts.append(block_story(t, paras))
    if page.get("timeline"):
        parts.append(block_timeline(page["timeline"]))
    if page.get("chapters"):
        parts.append(block_chapters(page["chapters"]))
    if page.get("cards"):
        parts.append(block_cards(page["cards"]["title"], page["cards"]["items"]))
    if page.get("gallery"):
        parts.append(block_gallery(page["gallery"]))
    if page.get("cta"):
        c = page["cta"]
        parts.append(
            f"""<section class="ai-mp-cta-band">
  <p>{esc(c["text"])}</p>
  <a class="vt-btn ai-cta" href="{esc(c.get("href", "contact.html"))}">{esc(c["btn"])}</a>
</section>"""
        )
    parts.append("</main>")
    return "".join(parts)


def run() -> None:
    for sc in SCENARIOS:
        slug = sc["slug"]
        brand = sc["brand"]
        nav_pages = sc["nav"]
        for page in sc["pages"]:
            fname = page["file"]
            nav = build_nav(brand, nav_pages, fname, cta_label=sc.get("nav_cta", "Contact"))
            body = _render_page(sc, page)
            write_ai_page(
                slug,
                fname,
                page["title"],
                page["description"],
                body,
                layout=sc.get("layout", "ai-mp"),
                nav=nav,
            )
        ensure_css(slug, sc.get("css_extra", ""))
        print(f"OK multipage {slug} ({len(sc['pages'])} pages)")


if __name__ == "__main__":
    run()
