#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble le livre HTML/CSS et genere un PDF telechargeable."""

from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHAPITRES = ROOT / "chapitres"
OUT_HTML = ROOT / "livre.html"
OUT_PDF = ROOT.parent.parent / "pdf" / "html-css-les-bases.pdf"

CHAPTER_FILES = [
    "01-cest-quoi.md",
    "02-premier-fichier.md",
    "03-balises.md",
    "04-texte.md",
    "05-liens-images.md",
    "06-listes-tableaux.md",
    "07-formulaires.md",
    "08-css-arrive.md",
    "09-couleurs-polices.md",
    "10-boites.md",
    "11-flexbox.md",
    "12-responsive.md",
    "13-mini-projet.md",
    "14-retenir.md",
    "15-quiz.md",
    "16-bravo.md",
]

# Images a glisser juste apres le titre de chapitre (fichier dans images/)
CHAPTER_IMAGES: dict[int, list[tuple[str, str]]] = {
    1: [
        ("html-css-maison.png", "A gauche la structure. A droite la deco. HTML puis CSS."),
    ],
    2: [
        ("html-css-premier-fichier.png", "Ton fichier s'ouvre dans le navigateur. Magie."),
        ("html-css-structure.png", "La page, c'est des boites rangees les unes dans les autres."),
    ],
    3: [
        ("html-css-balises.png", "Une balise, c'est une etiquette posee sur un contenu."),
    ],
    10: [
        ("html-css-box-model.png", "Margin dehors, padding dedans, border entre les deux."),
    ],
    11: [
        ("html-css-flexbox.png", "Flexbox range les blocs en ligne ou en colonne."),
    ],
    12: [
        ("html-css-responsive.png", "Meme site, grand ecran ou telephone : ca s'adapte."),
    ],
    13: [
        ("html-css-page-perso.png", "Le but : une petite page a toi, claire et perso."),
    ],
    16: [
        ("html-css-felicitations.png", "Bravo. Tu es alle au bout. C'est deja une vraie victoire."),
    ],
}

COVER_IMAGE = "html-css-couverture.png"

BOOK_TITLE = "HTML et CSS - Les bases"
BOOK_AUTHOR = "DanielCraft"
BOOK_SUBJECT = "Formation debutant HTML et CSS"
BOOK_KEYWORDS = "HTML, CSS, formation, debutant, web"
IMAGES_DIR = ROOT / "images"
PRINT_DIR = IMAGES_DIR / "print"


def md_inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def md_to_html(md: str) -> str:
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    i = 0
    in_code = False
    code_lang = ""
    code_buf: list[str] = []
    in_ul = False
    in_ol = False
    in_table = False
    table_rows: list[str] = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def flush_table() -> None:
        nonlocal in_table, table_rows
        if not table_rows:
            return
        out.append('<div class="table-wrap"><table>')
        for idx, row in enumerate(table_rows):
            cells = [c.strip() for c in row.strip("|").split("|")]
            if idx == 1 and all(re.match(r"^:?-+:?$", c or "") for c in cells):
                continue
            tag = "th" if idx == 0 else "td"
            out.append("<tr>" + "".join(f"<{tag}>{md_inline(c)}</{tag}>" for c in cells) + "</tr>")
        out.append("</table></div>")
        table_rows = []
        in_table = False

    while i < len(lines):
        line = lines[i]

        if line.startswith("```"):
            close_lists()
            flush_table()
            if not in_code:
                in_code = True
                code_lang = line[3:].strip()
                code_buf = []
            else:
                cls = f' class="language-{html.escape(code_lang)}"' if code_lang else ""
                out.append(f"<pre><code{cls}>{html.escape(chr(10).join(code_buf))}</code></pre>")
                in_code = False
            i += 1
            continue

        if in_code:
            code_buf.append(line)
            i += 1
            continue

        if line.strip().startswith("|"):
            close_lists()
            in_table = True
            table_rows.append(line)
            i += 1
            continue
        if in_table:
            flush_table()

        if not line.strip():
            close_lists()
            i += 1
            continue

        if line.startswith("# "):
            close_lists()
            out.append(f"<h1>{md_inline(line[2:].strip())}</h1>")
        elif line.startswith("## "):
            close_lists()
            out.append(f"<h2>{md_inline(line[3:].strip())}</h2>")
        elif line.startswith("### "):
            close_lists()
            out.append(f"<h3>{md_inline(line[4:].strip())}</h3>")
        elif re.match(r"^- \[ \]", line):
            if not in_ul:
                close_lists()
                out.append("<ul class='check'>")
                in_ul = True
            out.append(f"<li>{md_inline(line[6:].strip())}</li>")
        elif line.startswith("- "):
            if not in_ul:
                close_lists()
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{md_inline(line[2:].strip())}</li>")
        elif re.match(r"^\d+\. ", line):
            if not in_ol:
                close_lists()
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{md_inline(re.sub(r'^\d+\. ', '', line).strip())}</li>")
        else:
            close_lists()
            out.append(f"<p>{md_inline(line.strip())}</p>")
        i += 1

    close_lists()
    flush_table()
    return "\n".join(out)


BOOK_CSS = """
:root {
  --ink: #14221c;
  --muted: #3d5248;
  --paper: #f3f6f4;
  --paper-deep: #e5eee9;
  --band: #1a4d3e;
  --band-soft: #266b56;
  --accent: #c9a227;
  --code-bg: #133028;
  --code-fg: #e7f2ec;
  --card: #ffffff;
  --rule: #c5d4cc;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif;
  font-size: 17px;
  line-height: 1.55;
  color: var(--ink);
  background: var(--paper);
}
.page {
  width: min(100% - 2rem, 780px);
  margin: 0 auto;
  padding: 1.5rem 0 3rem;
}
.cover {
  display: grid;
  grid-template-rows: auto auto;
  margin: 0 0 2rem;
  border-radius: 14px;
  color: #f4faf7;
  background: #0f2f26;
  overflow: hidden;
}
.cover-art {
  display: block;
  width: 100%;
  max-height: 320px;
  height: auto;
  object-fit: cover;
  object-position: center;
}
.cover-copy {
  padding: 1.25rem 1.5rem 1.5rem;
  background: #0f2f26;
}
.cover-kicker {
  letter-spacing: 0.12em;
  text-transform: uppercase;
  font-size: 0.75rem;
  font-family: Segoe UI, Arial, sans-serif;
  opacity: 0.85;
}
.cover h1 {
  font-size: clamp(2rem, 5vw, 3rem);
  line-height: 1.1;
  margin: 0.45rem 0 0.6rem;
  max-width: 12ch;
  color: #f4faf7;
}
.cover .lead {
  font-size: 1.05rem;
  max-width: 38ch;
  margin: 0;
  opacity: 0.95;
}
.cover .meta {
  margin: 1rem 0 0;
  font-family: Segoe UI, Arial, sans-serif;
  font-size: 0.88rem;
  opacity: 0.8;
}
.illus {
  margin: 0.9rem 0 1rem;
  padding: 0;
  text-align: center;
}
.illus img {
  display: block;
  width: auto;
  max-width: min(100%, 520px);
  max-height: 220px;
  height: auto;
  margin: 0 auto;
  border-radius: 10px;
  border: 1px solid var(--rule);
  background: var(--paper-deep);
  object-fit: contain;
}
.illus.illus-wide img {
  max-width: min(100%, 640px);
  max-height: 260px;
}
.illus figcaption {
  margin-top: 0.45rem;
  font-size: 0.88rem;
  color: var(--muted);
  font-family: Segoe UI, Arial, sans-serif;
  line-height: 1.35;
  text-align: left;
}
body.eco {
  --paper: #ffffff;
  --paper-deep: #f3f3f3;
  --card: #ffffff;
  --code-bg: #222;
}
body.eco pre { border-left-color: #666; }
.toc {
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 12px;
  padding: 1.2rem 1.4rem;
  margin-bottom: 2rem;
}
.toc h2 { margin-top: 0; font-size: 1.25rem; }
.toc ol { padding-left: 1.2rem; margin: 0.4rem 0 0; }
.toc li { margin: 0.2rem 0; }
.toc a {
  color: var(--band);
  text-decoration: none;
}
.chapter {
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 12px;
  padding: 1.2rem 1.35rem 1.4rem;
  margin: 0 0 1.35rem;
}
.chapter-num {
  font-family: Segoe UI, Arial, sans-serif;
  font-size: 0.75rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--band-soft);
  margin: 0 0 0.15rem;
}
h1, h2, h3 { line-height: 1.25; color: var(--band); }
.chapter > h1 {
  font-size: 1.45rem;
  margin: 0.15rem 0 0.75rem;
  color: var(--ink);
}
h2 { font-size: 1.12rem; margin: 1.15rem 0 0.45rem; }
h3 { font-size: 1rem; margin: 0.95rem 0 0.35rem; color: var(--muted); }
p { margin: 0.55rem 0; }
ul, ol { margin: 0.45rem 0 0.7rem; padding-left: 1.25rem; }
li { margin: 0.18rem 0; }
code {
  font-family: Consolas, "Courier New", monospace;
  font-size: 0.9em;
  background: var(--paper-deep);
  padding: 0.08em 0.3em;
  border-radius: 4px;
}
pre {
  background: var(--code-bg);
  color: var(--code-fg);
  padding: 0.75rem 0.9rem;
  border-radius: 8px;
  overflow-x: auto;
  border-left: 4px solid var(--accent);
  font-size: 0.82rem;
  line-height: 1.4;
}
pre code {
  background: transparent;
  color: inherit;
  padding: 0;
  font-size: inherit;
}
.table-wrap { overflow-x: auto; margin: 0.8rem 0; }
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.92rem;
}
th, td {
  border: 1px solid var(--rule);
  padding: 0.45rem 0.6rem;
  text-align: left;
}
th { background: var(--paper-deep); }
.qa strong { color: var(--band); }
.footer-note {
  text-align: center;
  color: var(--muted);
  font-size: 0.92rem;
  padding: 1.5rem 1rem 0.5rem;
}
@media print {
  body {
    background: white !important;
    font-size: 10.5pt;
    line-height: 1.45;
    color: #111 !important;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  .page { width: auto; max-width: none; margin: 0; padding: 0; }
  .cover {
    min-height: 0 !important;
    height: auto !important;
    border-radius: 0;
    box-shadow: none;
    margin: 0 0 8mm;
    break-after: page;
    page-break-after: always;
    break-inside: avoid;
    page-break-inside: avoid;
  }
  .cover-art {
    min-height: 0 !important;
    max-height: 95mm !important;
    width: 100%;
    object-fit: cover;
  }
  .toc, .chapter {
    background: transparent !important;
    box-shadow: none;
    border: none;
    border-radius: 0;
    padding: 0;
    margin: 0 0 7mm;
    break-inside: auto !important;
    page-break-inside: auto !important;
  }
  .toc {
    break-after: page;
    page-break-after: always;
  }
  .chapter {
    break-before: auto;
    page-break-before: auto;
  }
  .chapter.chapter-break {
    break-before: page;
    page-break-before: always;
  }
  .chapter-num, h1, h2, h3 {
    break-after: avoid;
    page-break-after: avoid;
    break-inside: avoid;
    page-break-inside: avoid;
  }
  .chapter > h1 {
    font-size: 15pt;
    margin: 0 0 3mm;
  }
  h2 { font-size: 12pt; margin: 4.5mm 0 2mm; }
  h3 { font-size: 11pt; margin: 3.5mm 0 1.5mm; }
  p, li {
    orphans: 3;
    widows: 3;
  }
  .illus {
    break-inside: avoid;
    page-break-inside: avoid;
    margin: 3mm auto 4mm;
  }
  .illus img {
    max-width: 105mm !important;
    max-height: 55mm !important;
    width: auto !important;
    height: auto !important;
  }
  .illus.illus-wide img {
    max-width: 130mm !important;
    max-height: 65mm !important;
  }
  pre {
    break-inside: auto;
    page-break-inside: auto;
    white-space: pre-wrap;
    font-size: 8.5pt;
    border-radius: 0;
  }
  table { break-inside: auto; }
  a { color: inherit; text-decoration: none; }
  .footer-note { break-before: avoid; }
}
@page {
  size: A4;
  margin: 14mm 14mm 18mm;
}
"""


def compress_images(*, max_width: int = 1400, quality: int = 75) -> dict[str, str]:
    """Compresse les PNG source vers images/print/*.jpg. Retourne nom_source -> chemin HTML."""
    from PIL import Image

    PRINT_DIR.mkdir(parents=True, exist_ok=True)
    mapping: dict[str, str] = {}
    sources = {COVER_IMAGE}
    for figs in CHAPTER_IMAGES.values():
        for src, _cap in figs:
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
        q = 88 if name == COVER_IMAGE else quality
        img.save(out_path, "JPEG", quality=q, optimize=True, progressive=True)
        mapping[name] = f"images/print/{out_name}"
        print(f"Compress: {name} -> {out_name} ({out_path.stat().st_size // 1024} Ko)")
    return mapping


def figure_html(src_html: str, caption: str, *, wide: bool = False) -> str:
    cls = "illus illus-wide" if wide else "illus"
    return (
        f'<figure class="{cls}">'
        f'<img src="{html.escape(src_html)}" alt="{html.escape(caption)}">'
        f"<figcaption>{html.escape(caption)}</figcaption>"
        "</figure>"
    )


def inject_figures(
    body_html: str,
    figures: list[tuple[str, str]],
    image_map: dict[str, str],
    *,
    wide: bool = False,
) -> str:
    if not figures:
        return body_html
    block = "\n".join(
        figure_html(image_map.get(src, f"images/{src}"), cap, wide=wide)
        for src, cap in figures
    )
    return re.sub(r"(</h1>)", r"\1\n" + block, body_html, count=1)


def chapter_titles() -> list[tuple[int, str]]:
    titles: list[tuple[int, str]] = []
    for idx, name in enumerate(CHAPTER_FILES, start=1):
        raw = (CHAPITRES / name).read_text(encoding="utf-8")
        title_match = re.match(r"^#\s+(.+)$", raw, re.M)
        title = title_match.group(1).strip() if title_match else name
        titles.append((idx, title))
    return titles


def build_html(*, eco: bool = False, image_map: dict[str, str] | None = None) -> str:
    image_map = image_map or {}
    sections: list[str] = []
    toc: list[str] = []
    # Nouveau "vrai" chapitre / section speciale : saut de page propre
    break_chapters = {1, 8, 13, 15, 16}

    for idx, title in chapter_titles():
        name = CHAPTER_FILES[idx - 1]
        raw = (CHAPITRES / name).read_text(encoding="utf-8")
        anchor = f"chapitre-{idx:02d}"
        toc.append(f'<li><a href="#{anchor}">{html.escape(title)}</a></li>')
        body = inject_figures(
            md_to_html(raw),
            CHAPTER_IMAGES.get(idx, []),
            image_map,
            wide=(idx in {1, 16}),
        )
        extra = " chapter-break" if idx in break_chapters else ""
        label = "Quiz" if idx == 15 else ("Final" if idx == 16 else f"Chapitre {idx}")
        sections.append(
            f'<article class="chapter{extra}" id="{anchor}">'
            f'<div class="chapter-num">{html.escape(label)}</div>'
            f"{body}"
            f"</article>"
        )

    cover_src = image_map.get(COVER_IMAGE, f"images/{COVER_IMAGE}")
    body_class = ' class="eco"' if eco else ""
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
<body{body_class}>
  <div class="page">
    <header class="cover">
      <img class="cover-art" src="{html.escape(cover_src)}" alt="Couverture du livre HTML et CSS">
      <div class="cover-copy">
        <div class="cover-kicker">Formation informatique</div>
        <h1>HTML et CSS</h1>
        <p class="lead">Les bases pour construire une page web. Explique simplement, sans blabla inutile.</p>
        <p class="meta">{html.escape(BOOK_AUTHOR)} - Livre debutant</p>
      </div>
    </header>

    <nav class="toc" aria-label="Sommaire">
      <h2>Sommaire</h2>
      <ol>
        {''.join(toc)}
      </ol>
    </nav>

    {''.join(sections)}

    <p class="footer-note">Tu as les briques. Maintenant, construis.</p>
  </div>
</body>
</html>
"""


def find_browser() -> str | None:
    local = Path.home() / "AppData" / "Local"
    candidates = [
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
        Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
        local / "Google" / "Chrome" / "Application" / "chrome.exe",
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        local / "Microsoft" / "Edge" / "Application" / "msedge.exe",
    ]
    for c in candidates:
        if c.exists():
            return str(c)
    return None


def html_to_pdf(html_path: Path, pdf_path: Path) -> bool:
    """Genere le PDF. Preferer Playwright (rendu complet), sinon Chrome CLI."""
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    uri = html_path.resolve().as_uri()

    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(uri, wait_until="networkidle", timeout=120_000)
            page.emulate_media(media="print")
            page.evaluate(
                """() => Promise.all([...document.images].map(img =>
                  img.complete ? null : new Promise(r => { img.onload = img.onerror = r; })
                ))"""
            )
            page.pdf(
                path=str(pdf_path.resolve()),
                format="A4",
                print_background=True,
                display_header_footer=True,
                header_template="<span></span>",
                footer_template=(
                    '<div style="font-size:8px;width:100%;padding:0 14mm;color:#445544;'
                    'font-family:Helvetica,Arial,sans-serif;display:flex;'
                    'justify-content:space-between;align-items:center;">'
                    f"<span>{BOOK_AUTHOR}</span>"
                    '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span>'
                    "<span>HTML &amp; CSS</span>"
                    "</div>"
                ),
                margin={"top": "14mm", "bottom": "18mm", "left": "14mm", "right": "14mm"},
            )
            browser.close()
        ok = pdf_path.exists() and pdf_path.stat().st_size > 1000
        if ok:
            html_to_pdf.used_playwright = True  # type: ignore[attr-defined]
        return ok
    except Exception as exc:  # noqa: BLE001
        print(f"Playwright PDF impossible ({exc}), fallback Chrome CLI...", file=sys.stderr)

    html_to_pdf.used_playwright = False  # type: ignore[attr-defined]
    browser = find_browser()
    if not browser:
        return False
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=20000",
        f"--print-to-pdf={pdf_path.resolve()}",
        uri,
    ]
    result = subprocess.run(cmd, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr[-1000:] if result.stderr else "chrome error", file=sys.stderr)
        return False
    return pdf_path.exists() and pdf_path.stat().st_size > 1000


html_to_pdf.used_playwright = False  # type: ignore[attr-defined]


def enrich_pdf(pdf_path: Path, *, stamp_footers: bool = True) -> None:
    """Metadonnees, numeros de page (annotations), signets chapitres.

    Important: on n'utilise plus merge_page + compress (ca donnait des pages blanches
    sur les PDF generes par Chrome).
    """
    from datetime import datetime, timezone

    from PyPDF2 import PdfReader, PdfWriter
    from PyPDF2.generic import AnnotationBuilder

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter()
    total = len(reader.pages)

    found_chapters: dict[int, int] = {}
    sommaire_page: int | None = None
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        compact = re.sub(r"\s+", " ", text)
        if sommaire_page is None and re.search(r"\bSommaire\b", compact):
            sommaire_page = i
        for num, _title in chapter_titles():
            if num in found_chapters:
                continue
            if num == 15 and re.search(r"\bQuiz\b", compact):
                found_chapters[num] = i
            elif num == 16 and re.search(r"\bBravo\.\b|\bBravo\b", compact):
                found_chapters[num] = i
            elif re.search(rf"\bChapitre\s+{num}\b", compact):
                found_chapters[num] = i

    for i, page in enumerate(reader.pages):
        writer.add_page(page)

    if stamp_footers:
        for i in range(1, total):  # saute la couverture
            page = writer.pages[i]
            w = float(page.mediabox.width)
            # Pied centre : numero
            try:
                writer.add_annotation(
                    i,
                    AnnotationBuilder.free_text(
                        f"{i + 1} / {total}",
                        rect=(w / 2 - 35, 12, w / 2 + 35, 28),
                        font="Helvetica",
                        font_size="8pt",
                        font_color="445544",
                        border_color="ffffff",
                        background_color="ffffff",
                    ),
                )
                writer.add_annotation(
                    i,
                    AnnotationBuilder.free_text(
                        BOOK_AUTHOR,
                        rect=(36, 12, 160, 28),
                        font="Helvetica",
                        font_size="8pt",
                        font_color="445544",
                        border_color="ffffff",
                        background_color="ffffff",
                    ),
                )
            except Exception as exc:  # noqa: BLE001
                print(f"Annotation page {i + 1} ignoree: {exc}", file=sys.stderr)

    now = datetime.now(timezone.utc).strftime("D:%Y%m%d%H%M%SZ")
    writer.add_metadata(
        {
            "/Author": BOOK_AUTHOR,
            "/Title": BOOK_TITLE,
            "/Subject": BOOK_SUBJECT,
            "/Keywords": BOOK_KEYWORDS,
            "/Creator": "DanielCraft - livres-formation",
            "/Producer": "DanielCraft build_livre.py",
            "/CreationDate": now,
            "/ModDate": now,
        }
    )

    writer.add_outline_item("Couverture", 0)
    if sommaire_page is not None:
        writer.add_outline_item("Sommaire", sommaire_page)
    for num, title in chapter_titles():
        page_idx = found_chapters.get(num)
        if page_idx is not None:
            short = re.sub(r"^Chapitre\s+\d+\s*-\s*", "", title).strip()
            writer.add_outline_item(f"{num}. {short}", page_idx)

    tmp = pdf_path.with_suffix(".tmp.pdf")
    with tmp.open("wb") as f:
        writer.write(f)
    tmp.replace(pdf_path)
    print(
        f"PDF enrichi: metadonnees ({BOOK_AUTHOR}), "
        f"pieds={'annotations' if stamp_footers else 'non'}, "
        f"{len(found_chapters)} signets"
    )


def fallback_pdf_reportlab(pdf_path: Path) -> None:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.platypus import PageBreak, Paragraph, Preformatted, SimpleDocTemplate, Spacer

    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "BookTitle",
        parent=styles["Title"],
        fontName="Times-Bold",
        fontSize=28,
        leading=34,
        spaceAfter=12,
        textColor="#1a4d3e",
    )
    h1 = ParagraphStyle(
        "H1",
        parent=styles["Heading1"],
        fontName="Times-Bold",
        fontSize=16,
        leading=20,
        spaceBefore=14,
        spaceAfter=8,
        textColor="#14221c",
    )
    h2 = ParagraphStyle(
        "H2",
        parent=styles["Heading2"],
        fontName="Times-Bold",
        fontSize=13,
        leading=17,
        spaceBefore=10,
        spaceAfter=6,
        textColor="#1a4d3e",
    )
    body = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontName="Times-Roman",
        fontSize=11,
        leading=16,
        spaceAfter=6,
    )
    code = ParagraphStyle(
        "Code",
        parent=styles["Code"],
        fontName="Courier",
        fontSize=8.5,
        leading=11,
        backColor="#133028",
        textColor="#e7f2ec",
        leftIndent=4,
        rightIndent=4,
        spaceBefore=6,
        spaceAfter=8,
    )

    story = [
        Paragraph(BOOK_TITLE, title),
        Paragraph(
            "Les bases pour construire une page web. Explique simplement, sans blabla inutile.",
            body,
        ),
        Paragraph(f"Auteur : {BOOK_AUTHOR}", body),
        Spacer(1, 8 * mm),
        PageBreak(),
    ]

    for name in CHAPTER_FILES:
        raw = (CHAPITRES / name).read_text(encoding="utf-8")
        in_code = False
        buf: list[str] = []
        for line in raw.splitlines():
            if line.startswith("```"):
                if not in_code:
                    in_code = True
                    buf = []
                else:
                    story.append(Preformatted("\n".join(buf)[:4000], code))
                    in_code = False
                continue
            if in_code:
                buf.append(line)
                continue
            safe = html.escape(line).replace("`", "")
            safe = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", safe)
            if line.startswith("# "):
                story.append(Paragraph(html.escape(line[2:]), h1))
            elif line.startswith("## "):
                story.append(Paragraph(html.escape(line[3:]), h2))
            elif line.startswith("### "):
                story.append(Paragraph(f"<b>{html.escape(line[4:])}</b>", body))
            elif line.strip():
                story.append(Paragraph(safe, body))
            else:
                story.append(Spacer(1, 2 * mm))
        story.append(PageBreak())

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=16 * mm,
        bottomMargin=16 * mm,
        title=BOOK_TITLE,
        author=BOOK_AUTHOR,
        subject=BOOK_SUBJECT,
        creator="DanielCraft - livres-formation",
    )
    doc.build(story)


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Assemble le livre HTML/CSS + PDF")
    parser.add_argument(
        "--eco",
        action="store_true",
        help="Version eco impression (fonds plus clairs, contrastes sobres)",
    )
    parser.add_argument(
        "--pdf-name",
        default="",
        help="Nom du PDF dans livres-formation/pdf/ (sinon auto)",
    )
    parser.add_argument(
        "--skip-compress",
        action="store_true",
        help="Ne pas recompresser les images",
    )
    args = parser.parse_args()

    image_map = (
        {
            name: f"images/print/{Path(name).stem}.jpg"
            for name in [COVER_IMAGE, *[s for figs in CHAPTER_IMAGES.values() for s, _ in figs]]
            if (PRINT_DIR / f"{Path(name).stem}.jpg").exists()
        }
        if args.skip_compress
        else compress_images()
    )

    html_doc = build_html(eco=args.eco, image_map=image_map)
    OUT_HTML.write_text(html_doc, encoding="utf-8")
    print(f"HTML: {OUT_HTML}")

    pdf_name = args.pdf_name or (
        "html-css-les-bases-eco.pdf" if args.eco else "html-css-les-bases.pdf"
    )
    pdf_path = OUT_PDF.parent / pdf_name
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    made = False
    try:
        if html_to_pdf(OUT_HTML, pdf_path):
            print(f"PDF (navigateur): {pdf_path}")
            made = True
    except Exception as exc:  # noqa: BLE001
        print(f"Navigateur PDF impossible ({exc}), fallback reportlab...", file=sys.stderr)

    if not made:
        fallback_pdf_reportlab(pdf_path)
        print(f"PDF (reportlab): {pdf_path}")

    try:
        enrich_pdf(pdf_path, stamp_footers=not html_to_pdf.used_playwright)
    except Exception as exc:  # noqa: BLE001
        print(f"Enrichissement PDF partiel/echoue: {exc}", file=sys.stderr)
        return 1

    size_mo = pdf_path.stat().st_size / (1024 * 1024)
    print(f"OK: {pdf_path} ({size_mo:.1f} Mo)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
