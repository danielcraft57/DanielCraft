#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble le livre Ruby - Les bases et genere un PDF telechargeable."""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path
import sys as _sys

_sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _book_lib import extract_h2, finalize_pdf, get_book_css, md_to_html, slugify  # noqa: E402

BOOK_CSS = get_book_css("ruby") + """
.illus.illus-scene { margin: 1.7rem 0 1.9rem; padding: 0.35rem 0; }
.illus.illus-scene img { max-width: min(100%, 560px); max-height: 240px; border-radius: 6px; }
@media print {
  .illus.illus-scene { margin: 6mm auto 7mm; }
  .illus.illus-scene img { max-width: 115mm !important; max-height: 58mm !important; }
}
"""

ROOT = Path(__file__).resolve().parent
CHAPITRES = ROOT / "chapitres"
OUT_HTML = ROOT / "livre.html"
OUT_PDF = ROOT.parent.parent / "pdf" / "ruby-les-bases.pdf"

CHAPTER_FILES = [
    "01-cest-quoi.md", "02-installer.md", "03-premier-programme.md", "04-variables.md",
    "05-types.md", "06-conditions.md", "07-boucles.md", "08-methodes.md",
    "09-symbols-hashes.md", "10-classes-objets.md", "11-modules-heritage.md",
    "12-erreurs.md", "13-mini-projet.md", "14-retenir.md", "15-atelier-variables.md",
    "16-atelier-methodes.md", "17-atelier-classes.md", "18-erreurs-classiques.md",
    "19-bonnes-pratiques.md", "20-quiz.md", "21-bravo.md",
]

CHAPTER_IMAGES: dict[int, list[tuple[str, str]]] = {
    1: [("ruby-cest-quoi.png", "Ruby : elegance et productivite."), ("ruby-cover.png", "Couverture Ruby.")],
    2: [("ruby-installer.png", "Ruby + gem + irb.")],
    3: [("ruby-premier-programme.png", "puts et interpolation #{ }.")],
    4: [("ruby-variables.png", "Assignation et constantes.")],
    5: [("ruby-types.png", "Typage dynamique et nil.")],
    6: [("ruby-conditions.png", "if et case/when.")],
    7: [("ruby-boucles.png", ".each, while, times."), ("ruby-scene1.png", "Coder en Ruby au quotidien.")],
    8: [("ruby-methodes.png", "Methodes, blocs et yield.")],
    9: [("ruby-symbols-hashes.png", "Symboles :cle et hashes."), ("ruby-scene2.png", "Gems et ecosysteme.")],
    10: [("ruby-classes-objets.png", "Classes et @instance.")],
    11: [("ruby-modules-heritage.png", "Heritage et mixins.")],
    12: [("ruby-erreurs.png", "begin / rescue / raise."), ("ruby-scene3.png", "Ruby on Rails.")],
    13: [("ruby-mini-projet.png", "Mini-projet : gestionnaire de taches.")],
    14: [("ruby-retenir.png", "Carte des notions Ruby.")],
    15: [("ruby-atelier-variables.png", "Atelier : variables.")],
    16: [("ruby-atelier-methodes.png", "Atelier : methodes.")],
    17: [("ruby-atelier-classes.png", "Atelier : classes.")],
    18: [("ruby-erreurs-classiques.png", "Pieges classiques Ruby.")],
    19: [("ruby-pratiques.png", "RuboCop et bonnes pratiques.")],
    20: [("ruby-quiz.png", "Quiz Ruby bases.")],
    21: [("ruby-felicitations.png", "Bravo. Tu codes en Ruby.")],
}

COVER_IMAGE = "ruby-cover.png"
BOOK_TITLE = "Ruby - Les bases"
BOOK_SHORT = "Ruby"
BOOK_LEAD = "Apprendre le langage elegant de Matz, pas a pas."
BOOK_AUTHOR = "DanielCraft"
BOOK_SUBJECT = "Formation debutant Ruby - Niveau Base"
BOOK_KEYWORDS = "Ruby, Rails, programmation, debutant, formation, bases, web"
IMAGES_DIR = ROOT / "images"
PRINT_DIR = IMAGES_DIR / "print"


def compress_images(*, max_width: int = 1400, quality: int = 75) -> dict[str, str]:
    from PIL import Image

    PRINT_DIR.mkdir(parents=True, exist_ok=True)
    mapping: dict[str, str] = {}
    sources = {COVER_IMAGE}
    for figs in CHAPTER_IMAGES.values():
        for src, _ in figs:
            sources.add(src)
    for name in sorted(sources):
        src_path = IMAGES_DIR / name
        if not src_path.exists():
            print(f"Image manquante: {src_path}", file=sys.stderr)
            continue
        out_name = src_path.stem + ".jpg"
        out_path = PRINT_DIR / out_name
        img = Image.open(src_path).convert("RGB")
        if img.width > max_width:
            ratio = max_width / float(img.width)
            img = img.resize((max_width, max(1, int(img.height * ratio))), Image.Resampling.LANCZOS)
        img.save(out_path, "JPEG", quality=88 if name == COVER_IMAGE else quality, optimize=True, progressive=True)
        mapping[name] = f"images/print/{out_name}"
    return mapping


def figure_html(src_html: str, caption: str, *, scene: bool = False) -> str:
    cls = "illus illus-scene" if scene else "illus"
    return f'<figure class="{cls}"><img src="{html.escape(src_html)}" alt="{html.escape(caption)}"><figcaption>{html.escape(caption)}</figcaption></figure>'


def inject_figures(body_html: str, figures: list[tuple[str, str]], image_map: dict[str, str]) -> str:
    if not figures:
        return body_html
    schemas = [(s, c) for s, c in figures if "-scene" not in s]
    scenes = [(s, c) for s, c in figures if "-scene" in s]
    if schemas:
        block = "\n".join(figure_html(image_map.get(s, f"images/{s}"), c) for s, c in schemas)
        body_html = re.sub(r"(</h1>)", r"\1\n" + block, body_html, count=1)
    if scenes:
        block = "\n".join(figure_html(image_map.get(s, f"images/{s}"), c, scene=True) for s, c in scenes)
        for anchor in ("Petite histoire", "En vrai", "Astuce DanielCraft"):
            pat = rf"(<h2[^>]*>\s*{re.escape(anchor)}\s*</h2>)"
            if re.search(pat, body_html, flags=re.I):
                body_html = re.sub(pat, block + r"\n\1", body_html, count=1, flags=re.I)
                break
        else:
            body_html = re.sub(r"(</aside>)", r"\1\n" + block, body_html, count=1)
    return body_html


def chapter_titles() -> list[tuple[int, str]]:
    out = []
    for idx, name in enumerate(CHAPTER_FILES, start=1):
        raw = (CHAPITRES / name).read_text(encoding="utf-8")
        m = re.match(r"^#\s+(.+)$", raw, re.M)
        out.append((idx, m.group(1).strip() if m else name))
    return out


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
        <div class="cover-kicker">Formation Ruby - Les bases</div>
        <h1>{html.escape(BOOK_SHORT)}</h1>
        <p class="lead">{html.escape(BOOK_LEAD)}</p>
        <p class="meta">{html.escape(BOOK_AUTHOR)} - Livre debutant - Pack Web</p>
      </div>
    </header>
    <nav class="toc" aria-label="Sommaire"><h2 id="sommaire">Sommaire</h2><p class="toc-help">Clique un chapitre ou un sous-chapitre pour y aller.</p><ol>{"".join(toc)}</ol></nav>
    {"".join(sections)}
    <p class="footer-note">Tu as les briques. Maintenant, code avec joie.</p>
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
            path=str(pdf_path.resolve()), format="A4", print_background=True,
            display_header_footer=True, header_template="<span></span>",
            footer_template=f'<div style="font-size:8px;width:100%;padding:0 14mm;color:#445544;font-family:Helvetica,Arial,sans-serif;display:flex;justify-content:space-between;"><span>{BOOK_AUTHOR}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span><span>{html.escape(BOOK_SHORT)}</span></div>',
            margin={"top": "14mm", "bottom": "18mm", "left": "14mm", "right": "14mm"},
        )
        browser.close()
    return pdf_path.exists() and pdf_path.stat().st_size > 1000


def main() -> int:
    image_map = compress_images()
    OUT_HTML.write_text(build_html(image_map), encoding="utf-8")
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    if not html_to_pdf(OUT_HTML, OUT_PDF):
        return 1
    payload = [(idx, t, extract_h2((CHAPITRES / CHAPTER_FILES[idx - 1]).read_text(encoding="utf-8"))) for idx, t in chapter_titles()]
    finalize_pdf(OUT_PDF, author=BOOK_AUTHOR, title=BOOK_TITLE, subject=BOOK_SUBJECT, keywords=BOOK_KEYWORDS, chapters=payload)
    print(f"OK: {OUT_PDF} ({OUT_PDF.stat().st_size / (1024 * 1024):.1f} Mo)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
