#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble Java - Intermediaire + PDF."""

from __future__ import annotations

import html
import re
from pathlib import Path
import sys as _sys

_sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _book_lib import extract_h2, finalize_pdf, get_book_css, md_to_html, slugify  # noqa: E402

BOOK_CSS = get_book_css("java2") + """
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
OUT_PDF = ROOT.parent.parent / "pdf" / "java-intermediaire.pdf"

CHAPTER_FILES = [
    "01-apres-les-bases.md", "02-collections.md", "03-generics.md", "04-interfaces.md",
    "05-heritage-poly.md", "06-exceptions.md", "07-streams.md", "08-optional.md",
    "09-fichiers.md", "10-records.md", "11-enums.md", "12-packages.md",
    "13-tests-idee.md", "14-mini-projet.md", "15-retenir.md", "16-atelier-collections.md",
    "17-atelier-streams.md", "18-erreurs-classiques.md", "19-bonnes-pratiques.md",
    "20-quiz.md", "21-bravo.md",
]

CHAPTER_IMAGES: dict[int, list[tuple[str, str]]] = {
    1: [("java2-apres-les-bases.png", "Des bases aux outils du quotidien."), ("java2-cover.png", "Couverture Java Intermediaire.")],
    2: [("java2-collections.png", "List, Set, Map : choisir la bonne structure."), ("java2-scene1.png", "Collections en action.")],
    3: [("java2-generics.png", "Generics : typer sans caster.")],
    4: [("java2-interfaces.png", "Interface = contrat, abstraite = code commun.")],
    5: [("java2-heritage-poly.png", "Polymorphisme : meme appel, comportement adapte.")],
    6: [("java2-exceptions.png", "Exceptions : signaler, pas avaler.")],
    7: [("java2-streams.png", "Pipeline filter → map → terminal."), ("java2-scene2.png", "Streams en pipeline.")],
    8: [("java2-optional.png", "Optional : finir avec null.")],
    9: [("java2-fichiers.png", "Path + Files : API moderne.")],
    10: [("java2-records.png", "Record : donnees immuables.")],
    11: [("java2-enums.png", "Enum : etats finis nommes.")],
    12: [("java2-packages.png", "Packages : structure claire.")],
    13: [("java2-tests-idee.png", "Tests : verifier le comportement.")],
    14: [("java2-mini-projet.png", "Mini-projet carnet de taches."), ("java2-scene3.png", "Collections, streams et fichiers.")],
    15: [("java2-retenir.png", "Carte inter Java.")],
    16: [("java2-atelier-collections.png", "Atelier collections.")],
    17: [("java2-atelier-streams.png", "Atelier streams.")],
    18: [("java2-erreurs-classiques.png", "Pieges courants.")],
    19: [("java2-pratiques.png", "Discipline pro.")],
    20: [("java2-quiz.png", "Quiz Java intermediaire.")],
    21: [("java2-felicitations.png", "Bravo. Du Java clair, c'est du Java durable.")],
}

COVER_IMAGE = "java2-cover.png"
BOOK_TITLE = "Java - Intermediaire"
BOOK_SHORT = "Java"
BOOK_LEAD = "Collections, generics, streams, Optional et fichiers pour du Java pro au quotidien."
BOOK_AUTHOR = "DanielCraft"
BOOK_SUBJECT = "Formation Java - Niveau Intermediaire - Pack Java / langages"
BOOK_KEYWORDS = "Java, collections, generics, streams, Optional, fichiers, records, formation"
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


def figure_html(src: str, cap: str, *, scene: bool = False) -> str:
    cls = "illus illus-scene" if scene else "illus"
    return f'<figure class="{cls}"><img src="{html.escape(src)}" alt="{html.escape(cap)}"><figcaption>{html.escape(cap)}</figcaption></figure>'


def inject_figures(body: str, figs: list[tuple[str, str]], image_map: dict[str, str]) -> str:
    if not figs:
        return body
    schemas = [(s, c) for s, c in figs if "-scene" not in s]
    scenes = [(s, c) for s, c in figs if "-scene" in s]
    if schemas:
        block = "\n".join(figure_html(image_map.get(s, f"images/{s}"), c) for s, c in schemas)
        body = re.sub(r"(</h1>)", r"\1\n" + block, body, count=1)
    if scenes:
        block = "\n".join(figure_html(image_map.get(s, f"images/{s}"), c, scene=True) for s, c in scenes)
        for anchor in ("Petite histoire", "Exercice", "Astuce DanielCraft"):
            pat = rf"(<h2[^>]*>\s*{re.escape(anchor)}\s*</h2>)"
            if re.search(pat, body, flags=re.I):
                body = re.sub(pat, block + r"\n\1", body, count=1, flags=re.I)
                break
        else:
            body = re.sub(r"(</aside>)", r"\1\n" + block, body, count=1)
    return body


def chapter_titles() -> list[tuple[int, str]]:
    return [
        (i, (re.match(r"^#\s+(.+)$", (CHAPITRES / n).read_text(encoding="utf-8"), re.M) or [None, n])[1].strip())
        for i, n in enumerate(CHAPTER_FILES, 1)
    ]


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
    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><title>{html.escape(BOOK_TITLE)}</title><style>{BOOK_CSS}</style></head><body><div class="page">
<header class="cover"><img class="cover-art" src="{html.escape(cover)}" alt="Couverture"><div class="cover-copy"><div class="cover-kicker">Java - Intermediaire</div><h1>{html.escape(BOOK_SHORT)}</h1><p class="lead">{html.escape(BOOK_LEAD)}</p><p class="meta">{html.escape(BOOK_AUTHOR)} - Pack Java / langages</p></div></header>
<nav class="toc"><h2 id="sommaire">Sommaire</h2><ol>{"".join(toc)}</ol></nav>
{"".join(sections)}<p class="footer-note">Tu structures. Tu streams. Tu livres.</p></div></body></html>"""


def html_to_pdf(html_path: Path, pdf_path: Path) -> bool:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path.resolve().as_uri(), wait_until="networkidle", timeout=120_000)
        page.emulate_media(media="print")
        page.pdf(path=str(pdf_path.resolve()), format="A4", print_background=True,
                 display_header_footer=True, header_template="<span></span>",
                 footer_template=f'<div style="font-size:8px;width:100%;padding:0 14mm;display:flex;justify-content:space-between;font-family:sans-serif;color:#444"><span>{BOOK_AUTHOR}</span><span><span class="pageNumber"></span>/<span class="totalPages"></span></span><span>{html.escape(BOOK_SHORT)}</span></div>',
                 margin={"top": "14mm", "bottom": "18mm", "left": "14mm", "right": "14mm"})
        browser.close()
    return pdf_path.exists() and pdf_path.stat().st_size > 1000


def main() -> int:
    image_map = compress_images()
    OUT_HTML.write_text(build_html(image_map), encoding="utf-8")
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    if not html_to_pdf(OUT_HTML, OUT_PDF):
        return 1
    payload = [(i, t, extract_h2((CHAPITRES / CHAPTER_FILES[i - 1]).read_text(encoding="utf-8"))) for i, t in chapter_titles()]
    finalize_pdf(OUT_PDF, author=BOOK_AUTHOR, title=BOOK_TITLE, subject=BOOK_SUBJECT, keywords=BOOK_KEYWORDS, chapters=payload)
    print(f"OK: {OUT_PDF} ({OUT_PDF.stat().st_size / (1024 * 1024):.1f} Mo)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
