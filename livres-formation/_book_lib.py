# -*- coding: utf-8 -*-
"""Helpers partages pour assembler les livres de formation."""

from __future__ import annotations

import html
import re
from pathlib import Path


def slugify(text: str) -> str:
    text = text.lower().strip()
    table = {
        ord("à"): "a", ord("â"): "a", ord("ä"): "a",
        ord("é"): "e", ord("è"): "e", ord("ê"): "e", ord("ë"): "e",
        ord("î"): "i", ord("ï"): "i",
        ord("ô"): "o", ord("ö"): "o",
        ord("ù"): "u", ord("û"): "u", ord("ü"): "u",
        ord("ç"): "c",
    }
    text = text.translate(table)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "section"


def md_inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def md_to_html(md: str, *, id_prefix: str = "") -> str:
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
        out.append('<div class="table-wrap keep-block"><table>')
        for idx, row in enumerate(table_rows):
            cells = [c.strip() for c in row.strip("|").split("|")]
            if idx == 1 and all(re.match(r"^:?-+:?$", c or "") for c in cells):
                continue
            tag = "th" if idx == 0 else "td"
            out.append("<tr>" + "".join(f"<{tag}>{md_inline(c)}</{tag}>" for c in cells) + "</tr>")
        out.append("</table></div>")
        table_rows = []
        in_table = False

    def heading_id(title: str) -> str:
        slug = slugify(title)
        return f"{id_prefix}--{slug}" if id_prefix else slug

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
                keep = " keep-block" if len(code_buf) <= 18 else " code-long"
                code_html = html.escape("\n".join(code_buf))
                out.append(
                    f'<div class="code-block{keep}"><pre><code{cls}>{code_html}</code></pre></div>'
                )
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
            title = line[2:].strip()
            out.append(f'<h1 id="{heading_id(title)}">{md_inline(title)}</h1>')
        elif line.startswith("## "):
            close_lists()
            title = line[3:].strip()
            out.append(f'<h2 id="{heading_id(title)}">{md_inline(title)}</h2>')
        elif line.startswith("### "):
            close_lists()
            title = line[4:].strip()
            out.append(f'<h3 id="{heading_id(title)}">{md_inline(title)}</h3>')
        elif re.match(r"^- \[ \]", line):
            if not in_ul:
                close_lists()
                out.append('<ul class="check">')
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
            out.append(f"<li>{md_inline(re.sub(r'^\\d+\\. ', '', line).strip())}</li>")
        else:
            close_lists()
            out.append(f"<p>{md_inline(line.strip())}</p>")
        i += 1

    close_lists()
    flush_table()
    return "\n".join(out)


def extract_h2(md: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"^## (.+)$", md, re.M)]


PRINT_CSS_EXTRA = """
.toc-sub {
  list-style: disc;
  margin: 0.15rem 0 0.55rem 0.2rem;
  padding-left: 1.1rem;
}
.toc-sub li { margin: 0.12rem 0; font-size: 0.92em; }
.toc a { color: var(--band); text-decoration: none; }
.toc a:hover { text-decoration: underline; }
.code-block { margin: 0.65rem 0 0.9rem; }
.keep-block {
  break-inside: avoid;
  page-break-inside: avoid;
}
@media print {
  body {
    font-size: 11pt !important;
    line-height: 1.5 !important;
  }
  .toc a {
    color: var(--band) !important;
    text-decoration: underline !important;
  }
  .chapter {
    break-before: page !important;
    page-break-before: always !important;
    break-inside: auto !important;
    page-break-inside: auto !important;
    margin: 0 0 6mm !important;
  }
  .toc {
    break-after: page !important;
    page-break-after: always !important;
  }
  h1, h2, h3, .chapter-num {
    break-after: avoid !important;
    page-break-after: avoid !important;
    break-inside: avoid !important;
  }
  h2 + p, h2 + ul, h2 + ol, h2 + .code-block, h2 + .illus,
  h3 + p, h3 + ul, h3 + ol, h3 + .code-block,
  .chapter-num + h1, h1 + p, h1 + .illus, h1 + .code-block {
    break-before: avoid !important;
    page-break-before: avoid !important;
  }
  .keep-block, .illus, .table-wrap {
    break-inside: avoid !important;
    page-break-inside: avoid !important;
  }
  .code-long {
    break-inside: auto !important;
    page-break-inside: auto !important;
  }
  .code-long pre {
    break-inside: auto !important;
  }
  pre {
    white-space: pre-wrap !important;
    word-break: break-word;
  }
  p, li {
    orphans: 4;
    widows: 4;
  }
}
"""

BOOK_CSS_BASE = """
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
  /* Ne pas tuer les liens du sommaire a l'impression */
  a { color: inherit; text-decoration: none; }
  .toc a {
    color: var(--band) !important;
    text-decoration: underline !important;
  }
  .footer-note { break-before: avoid; }
}
@page {
  size: A4;
  margin: 14mm 14mm 18mm;
}
"""


def finalize_pdf(
    pdf_path: Path,
    *,
    author: str,
    title: str,
    subject: str,
    keywords: str,
    chapters: list[tuple[int, str, list[str]]],
) -> None:
    """Metadonnees + signets + liens cliquables du sommaire (PyMuPDF).

    chapters: liste (numero, titre_h1, [sous_titres_h2...])
    """
    import fitz  # PyMuPDF

    doc = fitz.open(str(pdf_path))
    page_count = doc.page_count

    def page_text(i: int) -> str:
        return re.sub(r"\s+", " ", doc[i].get_text("text") or "")

    # Pages du sommaire (souvent 1-2)
    toc_pages: list[int] = []
    for i in range(min(4, page_count)):
        t = page_text(i)
        if re.search(r"\bSommaire\b", t) and (
            "Clique un chapitre" in t or "Chapitre 1" in t or "chapitre" in t.lower()
        ):
            toc_pages.append(i)
    if not toc_pages and page_count > 1:
        toc_pages = [1]

    # Trouver la page de chaque chapitre / sous-chapitre
    chapter_page: dict[int, int] = {}
    sub_page: dict[tuple[int, str], int] = {}

    for i in range(page_count):
        t = page_text(i)
        for num, ch_title, subs in chapters:
            if num not in chapter_page:
                needle_ok = False
                if re.search(rf"\bChapitre\s+{num}\b", t, re.I):
                    needle_ok = True
                elif "quiz" in ch_title.lower() and re.search(r"\bQuiz\b", t):
                    needle_ok = True
                elif "bravo" in ch_title.lower() and re.search(r"\bBravo\b", t):
                    needle_ok = True
                # label Final / Quiz dans chapter-num
                short = re.sub(r"^Chapitre\s+\d+\s*-\s*", "", ch_title).strip()
                if short and short[:28] in t and i not in toc_pages:
                    # evite de matcher le sommaire
                    if not (toc_pages and i in toc_pages):
                        needle_ok = True
                if needle_ok and i not in toc_pages:
                    chapter_page[num] = i
            for sub in subs:
                key = (num, sub)
                if key in sub_page:
                    continue
                # sous-chapitre : chercher apres la page du chapitre si connue
                start = chapter_page.get(num, 0)
                if i >= start and sub in t and i not in toc_pages:
                    sub_page[key] = i

    # Liens cliquables sur le sommaire
    links_added = 0
    for ti in toc_pages:
        page = doc[ti]
        for num, ch_title, subs in chapters:
            target = chapter_page.get(num)
            if target is None:
                continue
            # Cherche plusieurs formes de texte presentes dans le TOC
            candidates = [
                ch_title,
                re.sub(r"^Chapitre\s+\d+\s*-\s*", "", ch_title).strip(),
                f"Chapitre {num}",
            ]
            for cand in candidates:
                if len(cand) < 3:
                    continue
                rects = page.search_for(cand[:60])
                for rect in rects:
                    page.insert_link(
                        {
                            "kind": fitz.LINK_GOTO,
                            "from": rect,
                            "page": target,
                            "to": fitz.Point(50, 50),
                        }
                    )
                    links_added += 1
                    break
                if rects:
                    break
            for sub in subs:
                target_sub = sub_page.get((num, sub), chapter_page.get(num))
                if target_sub is None:
                    continue
                rects = page.search_for(sub[:50])
                for rect in rects:
                    page.insert_link(
                        {
                            "kind": fitz.LINK_GOTO,
                            "from": rect,
                            "page": target_sub,
                            "to": fitz.Point(50, 70),
                        }
                    )
                    links_added += 1
                    break

    # Signets (panneau lateral)
    outline: list[list] = [[1, "Couverture", 1]]
    if toc_pages:
        outline.append([1, "Sommaire", toc_pages[0] + 1])
    for num, ch_title, subs in chapters:
        p = chapter_page.get(num)
        if p is None:
            continue
        short = re.sub(r"^Chapitre\s+\d+\s*-\s*", "", ch_title).strip()
        outline.append([1, f"{num}. {short}", p + 1])
        for sub in subs:
            sp = sub_page.get((num, sub), p)
            outline.append([2, sub, sp + 1])
    try:
        doc.set_toc(outline)
    except Exception as exc:  # noqa: BLE001
        print(f"Signets partiels: {exc}")

    doc.set_metadata(
        {
            "author": author,
            "title": title,
            "subject": subject,
            "keywords": keywords,
            "creator": "DanielCraft - livres-formation",
            "producer": "DanielCraft build_livre.py + PyMuPDF",
        }
    )

    tmp = pdf_path.with_suffix(".nav.pdf")
    doc.save(str(tmp), garbage=3, deflate=True)
    doc.close()
    tmp.replace(pdf_path)
    print(
        f"PDF navigable: {links_added} liens sommaire, "
        f"{len(chapter_page)}/{len(chapters)} chapitres cibles, auteur={author}"
    )


def get_book_css(theme: str = "default") -> str:
    """Retourne le CSS du livre. Themes: python, git, commerce."""
    css = BOOK_CSS_BASE + PRINT_CSS_EXTRA
    themes = {
        "python": """
/* Theme Python : bleu encre + abricot */
:root {
  --ink: #1a2332;
  --muted: #4a5568;
  --paper: #f2f4f8;
  --paper-deep: #e3e8f0;
  --band: #2c4a6e;
  --band-soft: #3d5f8a;
  --accent: #e07a3d;
  --code-bg: #1e293b;
  --code-fg: #e8eef6;
  --card: #ffffff;
  --rule: #c5ced9;
}
.cover,
.cover-copy {
  background: #1e3a5f !important;
  color: #f4f7fb !important;
}
.cover h1 { color: #f4f7fb !important; }
pre {
  border-left-color: #e07a3d !important;
}
button, .btn-like {
  background: #2c4a6e;
}
@media print {
  .toc a { color: #2c4a6e !important; }
}
""",
        "git": """
/* Theme Git : graphite + corail */
:root {
  --ink: #1a1a1f;
  --muted: #5c5c66;
  --paper: #f7f4f2;
  --paper-deep: #ebe4df;
  --band: #2b2d42;
  --band-soft: #3d405b;
  --accent: #ef476f;
  --code-bg: #1e1f2b;
  --code-fg: #f4eef0;
  --card: #ffffff;
  --rule: #d9d0c8;
}
.cover,
.cover-copy {
  background: #2b2d42 !important;
  color: #f7f4f2 !important;
}
.cover h1 { color: #f7f4f2 !important; }
pre {
  border-left-color: #ef476f !important;
}
button, .btn-like {
  background: #2b2d42;
}
@media print {
  .toc a { color: #2b2d42 !important; }
}
""",
        "commerce": """
/* Theme Commerce : sarcelle + or sable */
:root {
  --ink: #1a2a32;
  --muted: #5a6a72;
  --paper: #f3f7f6;
  --paper-deep: #e2ece9;
  --band: #264653;
  --band-soft: #2a6f7a;
  --accent: #e9c46a;
  --code-bg: #1d3557;
  --code-fg: #f4f1e8;
  --card: #ffffff;
  --rule: #c5d4d0;
}
.cover,
.cover-copy {
  background: #1d3557 !important;
  color: #f4f1e8 !important;
}
.cover h1 { color: #f4f1e8 !important; }
pre {
  border-left-color: #e9c46a !important;
}
button, .btn-like {
  background: #264653;
}
@media print {
  .toc a { color: #264653 !important; }
}
""",
    }
    extra = themes.get(theme, "")
    return css + extra
