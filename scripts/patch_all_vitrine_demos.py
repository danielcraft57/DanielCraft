#!/usr/bin/env python3
"""Patch 9 vitrine demos: hero split, stats, vitrine-media.css, branding fixes."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"
MEDIA = '  <link rel="stylesheet" href="../shared/vitrine-media.css">\n'
MC = "vitrine-figure--" + "motion"


def fig(gallery, png, svg, alt, title):
    return f"""            <motion> NO
"""


# rewrite entire file - use fig without bad tag

def figure_col(gallery, png, svg, alt, title):
    return f"""            <div class="column is-6 vitrine-img-reveal">
              <figure class="vitrine-figure vitrine-hero-visual vitrine-figure--ken {MC} mb-0">
                <a href="images/{svg}" class="glightbox" data-gallery="{gallery}" data-glightbox="title: {title}">
                  <img src="images/{png}" width="1200" height="675" alt="{alt}" decoding="async" fetchpriority="high">
                </a>
              </figure>
            </div>"""


def bulma_stats(css, rows):
    cols = "".join(
        f'          <div class="column"><p class="title is-2 has-text-white mb-1">{a}</p>'
        f'<p class="subtitle is-6 has-text-white-ter">{b}</p></div>\n'
        for a, b in rows
    )
    return f"""
    <section class="section {css} py-5" aria-label="Chiffres clés">
      <div class="container">
        <motion> NO
"""


print("incomplete")
