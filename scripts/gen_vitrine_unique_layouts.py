#!/usr/bin/env python3
"""Generate 19 unique vitrine demo layouts (index.html + styles.css)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"

SHARED_CSS = """  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="stylesheet" href="../shared/vitrine-media.css">
  <link rel="stylesheet" href="../shared/vitrine-layout-motion.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glightbox@3.2.0/dist/css/glightbox.min.css" crossorigin="anonymous">"""

SHARED_JS = """  <script src="https://cdn.jsdelivr.net/npm/glightbox@3.2.0/dist/js/glightbox.min.js" crossorigin="anonymous"></script>
  <script src="../shared/vitrine-images.js"></script>
  <script src="../shared/vitrine-layout-motion.js"></script>"""

FW = {
    "bootstrap": (
        '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">',
        '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>',
    ),
    "tailwind": (
        '<script src="https://cdn.tailwindcss.com"></script>',
        "",
    ),
    "pico": (
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css">',
        "",
    ),
    "daisy": (
        '<link href="https://cdn.jsdelivr.net/npm/daisyui@4.12.14/dist/full.min.css" rel="stylesheet">',
        '<script src="https://cdn.tailwindcss.com"></script>',
    ),
    "openprops": (
        '<link rel="stylesheet" href="https://unpkg.com/open-props/normalize.min.css">'
        '<link rel="stylesheet" href="https://unpkg.com/open-props/open-props.min.css">',
        "",
    ),
    "bulma": (
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css">',
        "",
    ),
}

FA = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" crossorigin="anonymous" referrerpolicy="no-referrer">'


def w(slug: str, layout: str, fw: str, title: str, desc: str, body: str, css: str, extra_head: str = "") -> None:
    css_link, js_fw = FW[fw]
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{desc}">
  <title>{title}</title>
  <!-- layout: {layout} -->
{css_link}
  {FA}
{SHARED_CSS}
{extra_head}
  <link rel="stylesheet" href="styles.css">
</head>
<body>
{body}
{SHARED_JS}
{js_fw}
</body>
</html>
"""
    d = ROOT / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(html.strip() + "\n", encoding="utf-8")
    (d / "styles.css").write_text(css.strip() + "\n", encoding="utf-8")


def fig(g: str, src: str, alt: str, title: str = "", lazy: bool = True) -> str:
    lp = ' loading="lazy" decoding="async"' if lazy else ' decoding="async" fetchpriority="high"'
    t = f' data-glightbox="title: {title}"' if title else ""
    return f"""<figure class="vitrine-figure mb-0">
  <a href="images/{src}" class="glightbox" data-gallery="{g}"{t}>
    <img src="images/{src}" alt="{alt}"{lp} style="width:100%;height:100%;object-fit:cover">
  </a>
</figure>"""


# Import layout bodies from companion module
from vitrine_layout_bodies import LAYOUTS  # noqa: E402

if __name__ == "__main__":
    for spec in LAYOUTS:
        w(*spec)
    print(f"Generated {len(LAYOUTS)} vitrine demos.")
