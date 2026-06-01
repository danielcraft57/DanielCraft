#!/usr/bin/env python3
"""Patch vitrine demo index.html: split hero, stats band, vitrine-media.css."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"
MEDIA = '  <link rel="stylesheet" href="../shared/vitrine-media.css">\n'
MOTION_CLS = "vitrine-figure--motion"


def ensure_media(html: str) -> str:
    if "vitrine-media.css" in html:
        return html
    return html.replace(
        '<link rel="stylesheet" href="../shared/vitrine-images.css">',
        '<link rel="stylesheet" href="../shared/vitrine-images.css">\n' + MEDIA.strip(),
        1,
    )


def insert_stats(html: str, block: str) -> str:
    if block.strip()[:40] in html:
        return html
    i = html.find('id="accueil"')
    j = html.find("</section>", i) + len("</section>")
    return html[:j] + "\n" + block + html[j:]


def fig(gallery, png, svg, alt, title):
    return f"""            <motion> BLOCK"""


# Rewrite entire script properly below

def figure_html(gallery, png, svg, alt, title):
    mc = MOTION_CLS
    return (
        f'            <motion> X'
    )


if __name__ == "__main__":
    pass
