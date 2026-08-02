#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble le livre Rust - Les bases et genere un PDF telechargeable."""

from __future__ import annotations

import html
import re
import subprocess
import sys
from pathlib import Path
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _book_lib import extract_h2, finalize_pdf, get_book_css, md_inline, md_to_html, slugify  # noqa: E402
BOOK_CSS = get_book_css("rust") + """
.illus.illus-scene {
  margin: 1.7rem 0 1.9rem;
  padding: 0.35rem 0;
}
.illus.illus-scene img {
  max-width: min(100%, 560px);
  max-height: 240px;
  border-radius: 6px;
}
@media print {
  .illus.illus-scene {
    margin: 6mm auto 7mm;
  }
  .illus.illus-scene img {
    max-width: 115mm !important;
    max-height: 58mm !important;
  }
}
"""

ROOT = Path(__file__).resolve().parent
CHAPITRES = ROOT / "chapitres"
OUT_HTML = ROOT / "livre.html"
OUT_PDF = ROOT.parent.parent / "pdf" / "rust-les-bases.pdf"

CHAPTER_FILES = [
    "01-cest-quoi.md",
    "02-installer.md",
    "03-premier-programme.md",
    "04-variables.md",
    "05-types.md",
    "06-conditions.md",
    "07-boucles.md",
    "08-fonctions.md",
    "09-ownership.md",
    "10-structs.md",
    "11-enums-pattern.md",
    "12-erreurs.md",
    "13-mini-projet.md",
    "14-retenir.md",
    "15-atelier-variables.md",
    "16-atelier-fonctions.md",
    "17-atelier-structs.md",
    "18-erreurs-classiques.md",
    "19-bonnes-pratiques.md",
    "20-quiz.md",
    "21-bravo.md",
]

CHAPTER_IMAGES: dict[int, list[tuple[str, str]]] = {
    1: [
        ("rust-cest-quoi.png", "Rust : securite memoire + performance."),
        ("rust-cover.png", "Le crabe Ferris, mascotte de Rust."),
    ],
    2: [("rust-installer.png", "rustup + cargo : pret en 2 minutes.")],
    3: [("rust-premier.png", "fn main() et println! : premier programme.")],
    4: [("rust-variables.png", "let immutable, let mut mutable.")],
    5: [("rust-types.png", "i32, f64, &str, String : types scalaires.")],
    6: [("rust-conditions.png", "if expression + match exhaustif.")],
    7: [
        ("rust-boucles.png", "loop, while, for in : les boucles Rust."),
        ("rust-scene1.png", "Sam decouvre les iterateurs Rust."),
    ],
    8: [("rust-fonctions.png", "Fonctions et closures.")],
    9: [
        ("rust-ownership.png", "Ownership : le coeur de Rust."),
        ("rust-scene2.png", "Securite memoire sans garbage collector."),
    ],
    10: [("rust-structs.png", "Structs et impl.")],
    11: [("rust-enums-pattern.png", "Enums + Option + match.")],
    12: [
        ("rust-erreurs.png", "Result<T,E> et l'operateur ?."),
        ("rust-scene3.png", "Max refactorise avec Result."),
    ],
    13: [("rust-mini-projet.png", "Mini-projet : outil CLI de notes.")],
    14: [("rust-retenir.png", "Carte des notions Rust.")],
    15: [("rust-atelier-variables.png", "Atelier : variables et types.")],
    16: [("rust-atelier-fonctions.png", "Atelier : fonctions.")],
    17: [("rust-atelier-structs.png", "Atelier : structs et enums.")],
    18: [("rust-erreurs-classiques.png", "Pieges classiques Rust.")],
    19: [("rust-pratiques.png", "cargo fmt, clippy, test.")],
    20: [("rust-quiz.png", "Quiz Rust bases.")],
    21: [("rust-felicitations.png", "Bravo. Tu codes en Rust.")],
}

COVER_IMAGE = "rust-cover.png"

BOOK_TITLE = "Rust - Les bases"
BOOK_SHORT = "Rust"
BOOK_LEAD = "Apprendre le langage systeme le plus aime, pas a pas."
BOOK_AUTHOR = "DanielCraft"
BOOK_SUBJECT = "Formation debutant Rust - Niveau Base"
BOOK_KEYWORDS = "Rust, programmation, debutant, formation, bases, systeme"
IMAGES_DIR = ROOT / "images"
PRINT_DIR = IMAGES_DIR / "print"



def compress_images(*, max_width: int = 1400, quality: int = 75) -> dict[str, str]:
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


def figure_html(src_html: str, caption: str, *, wide: bool = False, scene: bool = False) -> str:
    classes = ["illus"]
    if wide:
        classes.append("illus-wide")
    if scene:
        classes.append("illus-scene")
    cls = " ".join(classes)
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

    schemas = [(src, cap) for src, cap in figures if "-scene" not in str(src)]
    scenes = [(src, cap) for src, cap in figures if "-scene" in str(src)]

    if schemas:
        block = "\n".join(
            figure_html(image_map.get(src, f"images/{src}"), cap, wide=wide)
            for src, cap in schemas
        )
        body_html = re.sub(r"(</h1>)", r"\1\n" + block, body_html, count=1)

    if scenes:
        scene_block = "\n".join(
            figure_html(image_map.get(src, f"images/{src}"), cap, scene=True)
            for src, cap in scenes
        )
        placed = False
        for anchor in ("Petite histoire", "Erreur classique", "En vrai", "A toi"):
            pattern = rf"(<h2[^>]*>\s*{re.escape(anchor)}\s*</h2>)"
            if re.search(pattern, body_html, flags=re.I):
                body_html = re.sub(
                    pattern,
                    scene_block + r"\n\1",
                    body_html,
                    count=1,
                    flags=re.I,
                )
                placed = True
                break
        if not placed:
            body_html, n = re.subn(
                r"(</aside>)",
                r"\1\n" + scene_block,
                body_html,
                count=1,
            )
            if n == 0:
                body_html = re.sub(r"(</h1>)", r"\1\n" + scene_block, body_html, count=1)

    return body_html


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

    for idx, title in chapter_titles():
        name = CHAPTER_FILES[idx - 1]
        raw = (CHAPITRES / name).read_text(encoding="utf-8")
        anchor = f"chapitre-{idx:02d}"
        subs = extract_h2(raw)
        toc_item = [f'<li><a href="#{anchor}">{html.escape(title)}</a>']
        if subs:
            toc_item.append('<ol class="toc-sub">')
            for sub in subs:
                sid = f"{anchor}--{slugify(sub)}"
                toc_item.append(f'<li><a href="#{sid}">{html.escape(sub)}</a></li>')
            toc_item.append("</ol>")
        toc_item.append("</li>")
        toc.append("".join(toc_item))

        body = inject_figures(
            md_to_html(raw, id_prefix=anchor),
            CHAPTER_IMAGES.get(idx, []),
            image_map,
            wide=(idx in {1, 19}),
        )
        if "quiz" in name:
            label = "Quiz"
        elif "bravo" in name:
            label = "Final"
        else:
            label = f"Chapitre {idx}"
        sections.append(
            f'<article class="chapter chapter-break" id="{anchor}">'
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
      <img class="cover-art" src="{html.escape(cover_src)}" alt="Couverture {html.escape(BOOK_SHORT)}">
      <div class="cover-copy">
        <div class="cover-kicker">Formation Rust - Les bases</div>
        <h1>{html.escape(BOOK_SHORT)}</h1>
        <p class="lead">{html.escape(BOOK_LEAD)}</p>
        <p class="meta">{html.escape(BOOK_AUTHOR)} - Livre debutant - Pack Systeme</p>
      </div>
    </header>

    <nav class="toc" aria-label="Sommaire">
      <h2 id="sommaire">Sommaire</h2>
      <p class="toc-help">Clique un chapitre ou un sous-chapitre pour y aller.</p>
      <ol>
        {"".join(toc)}
      </ol>
    </nav>

    {"".join(sections)}

    <p class="footer-note">Tu as les briques. Maintenant, compile.</p>
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
                    f"<span>{html.escape(BOOK_SHORT)}</span>"
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
    chapters_payload = []
    for idx, title in chapter_titles():
        name = CHAPTER_FILES[idx - 1]
        raw = (CHAPITRES / name).read_text(encoding="utf-8")
        chapters_payload.append((idx, title, extract_h2(raw)))
    finalize_pdf(
        pdf_path,
        author=BOOK_AUTHOR,
        title=BOOK_TITLE,
        subject=BOOK_SUBJECT,
        keywords=BOOK_KEYWORDS,
        chapters=chapters_payload,
    )


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Assemble le livre Rust + PDF")
    parser.add_argument("--eco", action="store_true")
    parser.add_argument("--pdf-name", default="")
    parser.add_argument("--skip-compress", action="store_true")
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

    pdf_name = args.pdf_name or ("rust-les-bases-eco.pdf" if args.eco else "rust-les-bases.pdf")
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
        print("PDF generation failed - install playwright or Chrome", file=sys.stderr)
        return 1

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
