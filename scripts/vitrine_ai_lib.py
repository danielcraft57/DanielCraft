"""Bibliothèque vitrines IA — pages multiples, navigation, assets."""
from __future__ import annotations

import html as html_lib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"

HEAD_COMMON = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="stylesheet" href="../shared/vitrine-multipage.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HUB_FOOT = """
<footer class="ai-foot">
  <p><a href="../index.html">← Catalogue vitrines DanielCraft</a></p>
</footer>"""


def esc(s: str) -> str:
    return html_lib.escape(str(s), quote=True)


def build_nav(brand: str, pages: list[dict], current: str, *, cta_label: str = "Contact") -> str:
    """Navigation multi-pages : pages = [{file, label}, ...]."""
    links = []
    for p in pages:
        f = p["file"]
        label = p["label"]
        cls = ' class="ai-mp-nav-active"' if f == current else ""
        links.append(f'<a href="{esc(f)}"{cls}>{esc(label)}</a>')
    contact = pages[-1]["file"] if pages else "contact.html"
    return f"""<header class="ai-nav">
  <a class="ai-logo" href="index.html">{esc(brand)}</a>
  <nav aria-label="Navigation principale">{"".join(links)}</nav>
  <a class="vt-btn ai-nav-cta" href="{esc(contact)}">{esc(cta_label)}</a>
</header>"""


def write_ai_page(
    slug: str,
    filename: str,
    title: str,
    description: str,
    body: str,
    *,
    layout: str = "ai-mp",
    nav: str = "",
) -> None:
    d = ROOT / slug
    d.mkdir(parents=True, exist_ok=True)
    if nav:
        body = nav + "\n" + body.strip() + "\n" + HUB_FOOT
    elif HUB_FOOT.strip() not in body:
        body = body.rstrip() + "\n" + HUB_FOOT
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · généré IA multi-pages -->
{HEAD_COMMON}
</head>
<body>
{body.strip()}
</body>
</html>
"""
    (d / filename).write_text(html, encoding="utf-8")


def write_ai_site(slug: str, title: str, description: str, body: str, css: str, *, layout: str = "ai") -> None:
    """Compatibilité mono-page — délègue à write_ai_page index.html."""
    write_ai_page(slug, "index.html", title, description, body, layout=layout)
    d = ROOT / slug
    css_path = d / "styles.css"
    if css.strip():
        css_path.write_text(css.strip() + "\n", encoding="utf-8")


def ensure_css(slug: str, extra: str = "") -> None:
    """Préserve styles.css existant ; ajoute extra si absent."""
    css_path = ROOT / slug / "styles.css"
    base = css_path.read_text(encoding="utf-8") if css_path.is_file() else ""
    if extra and extra.strip() not in base:
        css_path.write_text(base.rstrip() + "\n\n" + extra.strip() + "\n", encoding="utf-8")
    elif not css_path.is_file():
        css_path.write_text(
            'body{font-family:"Plus Jakarta Sans",system-ui,sans-serif;font-size:17px;line-height:1.6;margin:0}\n',
            encoding="utf-8",
        )


def block_hero(h1: str, lead: str, img: str, alt: str = "") -> str:
    alt = alt or h1
    return f"""<main>
<section class="ai-mp-hero">
  <h1>{esc(h1)}</h1>
  <p class="ai-lead">{esc(lead)}</p>
  <figure class="ai-mp-hero-img"><img src="images/{esc(img)}" alt="{esc(alt)}" fetchpriority="high" decoding="async"></figure>
</section>"""


def block_story(title: str, paragraphs: list[str]) -> str:
    ps = "".join(f"<p>{esc(p)}</p>" for p in paragraphs)
    return f"""<section class="ai-mp-story"><div class="ai-mp-story-inner">
  <h2>{esc(title)}</h2>{ps}
</div></section>"""


def block_chapters(chapters: list[dict]) -> str:
    parts = ['<section class="ai-mp-chapters">']
    for i, ch in enumerate(chapters):
        flip = " ai-mp-chapter--flip" if i % 2 else ""
        parts.append(f"""<article class="ai-mp-chapter{flip}">
  <div>
    <h3>{esc(ch["title"])}</h3>
    <p>{esc(ch["text"])}</p>
  </div>
  <figure><img src="images/{esc(ch["img"])}" alt="{esc(ch.get("alt", ch["title"]))}" loading="lazy" decoding="async"></figure>
</article>""")
    parts.append("</section>")
    return "".join(parts)


def block_gallery(items: list[dict]) -> str:
    figs = "".join(
        f'<figure><img src="images/{esc(it["img"])}" alt="{esc(it.get("alt",""))}" loading="lazy"><figcaption>{esc(it.get("caption",""))}</figcaption></figure>'
        for it in items
    )
    return f'<section class="ai-mp-gallery" aria-label="Galerie">{figs}</section>'


def block_timeline(events: list[tuple[str, str]]) -> str:
    lis = "".join(f"<li><strong>{esc(d)}</strong>{esc(t)}</li>" for d, t in events)
    return f'<ol class="ai-mp-timeline">{lis}</ol>'


def block_cta(text: str, btn: str, href: str = "contact.html") -> str:
    return f"""<section class="ai-mp-cta-band">
  <p>{esc(text)}</p>
  <a class="vt-btn ai-cta" href="{esc(href)}">{esc(btn)}</a>
</section></main>"""


def block_cards(title: str, cards: list[dict]) -> str:
    items = "".join(
        f"""<article class="ai-card">
  <figure class="ai-card-img"><img src="images/{esc(c["img"])}" alt="{esc(c.get("alt", c["title"]))}" loading="lazy"></figure>
  <h3>{esc(c["title"])}</h3><p>{esc(c["text"])}</p>
</article>"""
        for c in cards
    )
    return f"""<section class="ai-offers"><div class="ai-wrap">
  <h2>{esc(title)}</h2>
  <div class="ai-cards">{items}</div>
</div></section>"""
