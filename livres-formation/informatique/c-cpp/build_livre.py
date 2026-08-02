#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble le livre C/C++ - Les bases et genere un PDF telechargeable."""

from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path
import sys as _sys

_sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _book_lib import extract_h2, finalize_pdf, get_book_css, md_to_html, slugify  # noqa: E402

BOOK_CSS = get_book_css("cpp")
ROOT = Path(__file__).resolve().parent
CHAPITRES = ROOT / "chapitres"
OUT_HTML = ROOT / "livre.html"
OUT_PDF = ROOT.parent.parent / "pdf" / "c-cpp-les-bases.pdf"

CHAPTER_FILES = [
    "01-cest-quoi.md",
    "02-installer.md",
    "03-premier-programme.md",
    "04-variables-types.md",
    "05-conditions.md",
    "06-boucles.md",
    "07-fonctions.md",
    "08-tableaux-vecteurs.md",
    "09-pointeurs-memoire.md",
    "10-classes-objets.md",
    "11-heritage-polymorphisme.md",
    "12-erreurs.md",
    "13-mini-projet.md",
    "14-retenir.md",
    "15-atelier-variables.md",
    "16-atelier-fonctions.md",
    "17-atelier-classes.md",
    "18-erreurs-classiques.md",
    "19-bonnes-pratiques.md",
    "20-quiz.md",
    "21-bravo.md",
]

CHAPTER_IMAGES: dict[int, list[tuple[str, str]]] = {
    1: [("cpp-cest-quoi.png", "C/C++ : performance et controle."), ("cpp-cover.png", "Univers C/C++.")],
    2: [("cpp-installer.png", "Compiler + CMake + IDE.")],
    3: [("cpp-premier-programme.png", "Premier programme C++.")],
    4: [("cpp-variables-types.png", "Types et variables.")],
    5: [("cpp-conditions.png", "Conditions if/else.")],
    6: [("cpp-boucles.png", "Boucles for/while.")],
    7: [("cpp-fonctions.png", "Fonctions et references."), ("cpp-scene1.png", "Coder en C++ au quotidien.")],
    8: [("cpp-tableaux-vecteurs.png", "Tableaux et vecteurs STL.")],
    9: [("cpp-pointeurs-memoire.png", "Pointeurs et memoire."), ("cpp-scene2.png", "Visualiser les pointeurs.")],
    10: [("cpp-classes-objets.png", "Classes et objets.")],
    11: [("cpp-heritage-polymorphisme.png", "Heritage et polymorphisme.")],
    12: [("cpp-erreurs.png", "Gestion d'erreurs C++."), ("cpp-scene3.png", "Optimisation et performance.")],
    13: [("cpp-mini-projet.png", "Mini-projet CLI.")],
    14: [("cpp-retenir.png", "Carte des notions C/C++.")],
    15: [("cpp-atelier-variables.png", "Atelier variables.")],
    16: [("cpp-atelier-fonctions.png", "Atelier fonctions.")],
    17: [("cpp-atelier-classes.png", "Atelier classes.")],
    18: [("cpp-erreurs-classiques.png", "Erreurs classiques.")],
    19: [("cpp-bonnes-pratiques.png", "Bonnes pratiques.")],
    20: [("cpp-quiz.png", "Quiz de revision.")],
    21: [("cpp-felicitations.png", "Felicitations !")],
}

COVER_IMAGE = "cpp-cover.png"
BOOK_TITLE = "C/C++ - Les bases"
BOOK_SHORT = "C/C++"
BOOK_LEAD = "Comprendre la performance, la memoire et les bases modernes."
BOOK_AUTHOR = "DanielCraft"
BOOK_SUBJECT = "Formation debutant C/C++ - Niveau Base"
BOOK_KEYWORDS = "C, C++, programmation, debutant, bases, memoire"
IMAGES_DIR = ROOT / "images"
PRINT_DIR = IMAGES_DIR / "print"


def compress_images(max_width: int = 1400, quality: int = 78) -> dict[str, str]:
    from PIL import Image

    PRINT_DIR.mkdir(parents=True, exist_ok=True)
    names = {COVER_IMAGE}
    for figs in CHAPTER_IMAGES.values():
        for src, _ in figs:
            names.add(src)
    mapping: dict[str, str] = {}
    for name in sorted(names):
        src = IMAGES_DIR / name
        if not src.exists():
            print(f"Image manquante: {src}", file=sys.stderr)
            continue
        out_name = f"{src.stem}.jpg"
        out = PRINT_DIR / out_name
        img = Image.open(src).convert("RGB")
        if img.width > max_width:
            ratio = max_width / float(img.width)
            img = img.resize((max_width, max(1, int(img.height * ratio))), Image.Resampling.LANCZOS)
        img.save(out, "JPEG", quality=88 if name == COVER_IMAGE else quality, optimize=True, progressive=True)
        mapping[name] = f"images/print/{out_name}"
    return mapping


def chapter_titles() -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    for idx, name in enumerate(CHAPTER_FILES, start=1):
        raw = (CHAPITRES / name).read_text(encoding="utf-8")
        m = re.match(r"^#\s+(.+)$", raw, re.M)
        out.append((idx, m.group(1).strip() if m else name))
    return out


def figure(src: str, cap: str) -> str:
    return f'<figure class="illus"><img src="{html.escape(src)}" alt="{html.escape(cap)}"><figcaption>{html.escape(cap)}</figcaption></figure>'


def inject_figures(body_html: str, figs: list[tuple[str, str]], image_map: dict[str, str]) -> str:
    if not figs:
        return body_html
    schema = [(s, c) for s, c in figs if "-scene" not in s]
    scenes = [(s, c) for s, c in figs if "-scene" in s]
    if schema:
        block = "\n".join(figure(image_map.get(s, f"images/{s}"), c) for s, c in schema)
        body_html = re.sub(r"(</h1>)", r"\1\n" + block, body_html, count=1)
    if scenes:
        block = "\n".join(figure(image_map.get(s, f"images/{s}"), c) for s, c in scenes)
        body_html = re.sub(r"(</h1>)", r"\1\n" + block, body_html, count=1)
    return body_html


def build_html(image_map: dict[str, str]) -> str:
    sections, toc = [], []
    for idx, title in chapter_titles():
        name = CHAPTER_FILES[idx - 1]
        raw = (CHAPITRES / name).read_text(encoding="utf-8")
        anchor = f"chapitre-{idx:02d}"
        subs = extract_h2(raw)
        toc_item = [f'<li><a href="#{anchor}">{html.escape(title)}</a>']
        if subs:
            toc_item.append('<ol class="toc-sub">')
            for sub in subs:
                toc_item.append(f'<li><a href="#{anchor}--{slugify(sub)}">{html.escape(sub)}</a></li>')
            toc_item.append("</ol>")
        toc_item.append("</li>")
        toc.append("".join(toc_item))

        body = inject_figures(md_to_html(raw, id_prefix=anchor), CHAPTER_IMAGES.get(idx, []), image_map)
        label = "Quiz" if "quiz" in name else ("Final" if "bravo" in name else f"Chapitre {idx}")
        sections.append(f'<article class="chapter chapter-break" id="{anchor}"><div class="chapter-num">{label}</div>{body}</article>')

    cover = image_map.get(COVER_IMAGE, f"images/{COVER_IMAGE}")
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="author" content="{html.escape(BOOK_AUTHOR)}">
  <meta name="description" content="{html.escape(BOOK_SUBJECT)}">
  <title>{html.escape(BOOK_TITLE)}</title>
  <style>{BOOK_CSS}</style>
</head>
<body>
  <div class="page">
    <header class="cover">
      <img class="cover-art" src="{html.escape(cover)}" alt="Couverture {html.escape(BOOK_SHORT)}">
      <div class="cover-copy">
        <div class="cover-kicker">Formation C/C++ - Les bases</div>
        <h1>{html.escape(BOOK_SHORT)}</h1>
        <p class="lead">{html.escape(BOOK_LEAD)}</p>
        <p class="meta">{html.escape(BOOK_AUTHOR)} - Livre debutant - Pack Systeme</p>
      </div>
    </header>
    <nav class="toc" aria-label="Sommaire"><h2 id="sommaire">Sommaire</h2><ol>{"".join(toc)}</ol></nav>
    {"".join(sections)}
    <p class="footer-note">Tu as les briques. Maintenant, code.</p>
  </div>
</body>
</html>"""


def html_to_pdf(html_path: Path, pdf_path: Path) -> bool:
    from playwright.sync_api import sync_playwright

    uri = html_path.resolve().as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(uri, wait_until="networkidle", timeout=120_000)
        page.emulate_media(media="print")
        page.pdf(
            path=str(pdf_path.resolve()),
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template="<span></span>",
            footer_template=f'<div style="font-size:8px;width:100%;padding:0 14mm;color:#445544;font-family:Helvetica,Arial,sans-serif;display:flex;justify-content:space-between;"><span>{BOOK_AUTHOR}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span><span>{html.escape(BOOK_SHORT)}</span></div>',
            margin={"top": "14mm", "bottom": "18mm", "left": "14mm", "right": "14mm"},
        )
        browser.close()
    return pdf_path.exists() and pdf_path.stat().st_size > 1000


def enrich_pdf(pdf_path: Path) -> None:
    payload = []
    for idx, title in chapter_titles():
        raw = (CHAPITRES / CHAPTER_FILES[idx - 1]).read_text(encoding="utf-8")
        payload.append((idx, title, extract_h2(raw)))
    finalize_pdf(
        pdf_path,
        author=BOOK_AUTHOR,
        title=BOOK_TITLE,
        subject=BOOK_SUBJECT,
        keywords=BOOK_KEYWORDS,
        chapters=payload,
    )


def main() -> int:
    image_map = compress_images()
    OUT_HTML.write_text(build_html(image_map), encoding="utf-8")
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    if not html_to_pdf(OUT_HTML, OUT_PDF):
        print("PDF generation failed", file=sys.stderr)
        return 1
    enrich_pdf(OUT_PDF)
    print(f"OK: {OUT_PDF} ({OUT_PDF.stat().st_size / (1024 * 1024):.1f} Mo)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
