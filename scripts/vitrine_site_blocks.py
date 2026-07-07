"""Blocs HTML réutilisables pour vitrines « vrai site » (Bootstrap 5 + thème sectoriel)."""
from __future__ import annotations

from vitrine_ai_lib import esc


HEAD_SPA = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_RESTAURATION = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

FOOT_SCRIPTS = """
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>"""


def vt_picture(
    filename: str,
    alt: str,
    *,
    css_class: str = "w-100",
    loading: str | None = "lazy",
    fetchpriority: str | None = None,
) -> str:
    """Picture WebP + fallback PNG (même nom de base)."""
    stem = filename.rsplit(".", 1)[0] if "." in filename else filename
    attrs = [f'class="{css_class}"', f'alt="{esc(alt)}"', 'decoding="async"']
    if loading:
        attrs.append(f'loading="{loading}"')
    if fetchpriority:
        attrs.append(f'fetchpriority="{fetchpriority}"')
    a = " ".join(attrs)
    return (
        f'<picture><source srcset="images/{esc(stem)}.webp" type="image/webp">'
        f'<img src="images/{esc(stem)}.png" {a}></picture>'
    )


HEAD_MEDICAL = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Instrument+Serif&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_GARAGE = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Barlow+Condensed:wght@600;700&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_RETAIL = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_CABINET = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_INDUSTRIAL = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_PROPERTY = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_EDUCATION = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_FACILITY = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_ASSOCIATION = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_PHOTO = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Source+Sans+3:wght@400;500;600&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_FITNESS = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_ARCHITECTURE = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""

HEAD_LEGAL = """
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link rel="stylesheet" href="../shared/vitrine-prose.css">
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="icon" href="images/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="stylesheet" href="styles.css">"""


def block_info_bar(*, status: str, address: str, phone: str, maps_href: str = "#") -> str:
    return f"""<div class="vt-topbar py-2" role="complementary" aria-label="Informations pratiques">
  <div class="container d-flex flex-wrap justify-content-center justify-content-lg-between align-items-center gap-2 small">
    <span class="vt-topbar-status">{esc(status)}</span>
    <a class="vt-topbar-link" href="{esc(maps_href)}">{esc(address)}</a>
    <a class="vt-topbar-link fw-semibold" href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a>
  </div>
</div>"""


def block_site_nav(brand: str, pages: list[dict], current: str, *, cta_label: str, cta_href: str) -> str:
    links = []
    for p in pages:
        f = p["file"]
        label = p["label"]
        active = " active" if f == current else ""
        aria = ' aria-current="page"' if f == current else ""
        links.append(f'<li class="nav-item"><a class="nav-link{active}" href="{esc(f)}"{aria}>{esc(label)}</a></li>')
    return f"""<header class="vt-header sticky-top">
  <nav class="navbar navbar-expand-lg vt-navbar">
    <div class="container">
      <a class="navbar-brand vt-brand" href="index.html">{esc(brand)}</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#vtNav" aria-controls="vtNav" aria-expanded="false" aria-label="Menu">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="vtNav">
        <ul class="navbar-nav mx-lg-auto mb-2 mb-lg-0">{"".join(links)}</ul>
        <a class="btn btn-vt-primary rounded-pill px-4" href="{esc(cta_href)}">{esc(cta_label)}</a>
      </div>
    </div>
  </nav>
</header>"""


def block_hero_rich(
    h1: str,
    lead: str,
    img: str,
    alt: str,
    *,
    eyebrow: str = "Bienvenue à la brasserie",
    primary_href: str,
    primary_label: str,
    secondary_href: str,
    secondary_label: str,
) -> str:
    return f"""<section class="vt-hero text-center">
  <div class="container py-5 py-lg-6">
    <p class="vt-eyebrow text-uppercase">{esc(eyebrow)}</p>
    <h1 class="display-5 vt-display">{esc(h1)}</h1>
    <p class="lead vt-lead mx-auto">{esc(lead)}</p>
    <div class="d-flex flex-wrap justify-content-center gap-3 mt-4">
      <a class="btn btn-vt-primary btn-lg rounded-pill px-4" href="{esc(primary_href)}">{esc(primary_label)}</a>
      <a class="btn btn-vt-outline btn-lg rounded-pill px-4" href="{esc(secondary_href)}">{esc(secondary_label)}</a>
    </div>
  </div>
  <figure class="vt-hero-media mb-0">
    {vt_picture(img, alt, css_class="w-100", loading=None, fetchpriority="high")}
  </figure>
</section>"""


def block_stats(items: list[tuple[str, str]]) -> str:
    cols = "".join(
        f"""<div class="col-4 col-md-4">
        <div class="vt-stat">
          <strong class="vt-stat-val">{esc(val)}</strong>
          <span class="vt-stat-lbl">{esc(lbl)}</span>
        </div>
      </div>"""
        for val, lbl in items
    )
    return f"""<section class="vt-stats-band" aria-label="Chiffres clés">
  <div class="container">
    <div class="row text-center g-0">{cols}
    </div>
  </div>
</section>"""


def block_story(title: str, paragraphs: list[str]) -> str:
    ps = "".join(f'<p class="mb-3">{esc(p)}</p>' for p in paragraphs)
    return f"""<section class="vt-story py-5">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-8 text-center">
        <h2 class="vt-section-title">{esc(title)}</h2>
        {ps}
      </div>
    </div>
  </div>
</section>"""


def block_chapters(chapters: list[dict]) -> str:
    parts = ['<section class="vt-chapters">']
    for i, ch in enumerate(chapters):
        flip = "flex-lg-row-reverse" if i % 2 else ""
        parts.append(f"""<article class="vt-chapter py-5">
  <div class="container">
    <div class="row align-items-center g-4 g-lg-5 {flip}">
      <div class="col-lg-6">
        <h3 class="vt-section-title h2">{esc(ch["title"])}</h3>
        <p class="text-secondary mb-0">{esc(ch["text"])}</p>
      </div>
      <div class="col-lg-6">
        <figure class="vt-media rounded-4 overflow-hidden mb-0 shadow-sm">
          {vt_picture(ch["img"], ch.get("alt", ch["title"]), css_class="w-100")}
        </figure>
      </div>
    </div>
  </div>
</article>""")
    parts.append("</section>")
    return "".join(parts)


def block_cards_bs(title: str, cards: list[dict]) -> str:
    items = ""
    for c in cards:
        items += f"""<div class="col-md-4">
        <article class="card vt-card h-100 border-0 shadow-sm">
          <figure class="mb-0 overflow-hidden">
            {vt_picture(c["img"], c.get("alt", c["title"]), css_class="card-img-top vt-card-img")}
          </figure>
          <div class="card-body p-4">
            <h3 class="card-title h5 vt-card-title">{esc(c["title"])}</h3>
            <p class="card-text text-secondary small mb-0">{esc(c["text"])}</p>
          </div>
        </article>
      </div>"""
    return f"""<section class="vt-signatures py-5">
  <div class="container">
    <h2 class="vt-section-title text-center mb-5">{esc(title)}</h2>
    <div class="row g-4">{items}
    </div>
  </div>
</section>"""


def block_gallery_full(items: list[dict]) -> str:
    figs = ""
    for it in items:
        figs += f"""<figure class="vt-gallery-figure mb-0">
      {vt_picture(it["img"], it.get("alt", ""), css_class="w-100")}
      <figcaption class="container py-3 small text-secondary">{esc(it.get("caption", ""))}</figcaption>
    </figure>"""
    return f'<section class="vt-gallery-full" aria-label="Galerie">{figs}</section>'


def block_cross_links(title: str, links: list[tuple[str, str]]) -> str:
    pills = "".join(f'<a class="btn btn-vt-pill rounded-pill" href="{esc(href)}">{esc(label)}</a>' for label, href in links)
    return f"""<section class="vt-cross py-5 text-center">
  <div class="container">
    <h2 class="h4 vt-section-title mb-4">{esc(title)}</h2>
    <div class="d-flex flex-wrap justify-content-center gap-2">{pills}</div>
  </div>
</section>"""


def block_trust(title: str, badges: list[str]) -> str:
    spans = "".join(f'<span class="badge rounded-pill vt-badge">{esc(b)}</span>' for b in badges)
    return f"""<section class="vt-trust py-5 bg-white text-center">
  <div class="container">
    <p class="vt-trust-lead fst-italic mb-4">{esc(title)}</p>
    <div class="d-flex flex-wrap justify-content-center gap-2">{spans}</div>
  </div>
</section>"""


def block_cta_band(text: str, btn: str, href: str = "contact.html") -> str:
    return f"""<section class="vt-cta-band py-5 text-center text-white">
  <div class="container">
    <p class="lead mb-4">{esc(text)}</p>
    <a class="btn btn-light btn-lg rounded-pill px-4" href="{esc(href)}">{esc(btn)}</a>
  </div>
</section>"""


def block_menu_section(title: str, intro: str, sections: list[dict]) -> str:
    blocks = ""
    for sec in sections:
        items_html = ""
        for it in sec["items"]:
            tags = "".join(f'<span class="badge vt-tag me-1">{esc(t)}</span>' for t in it.get("tags", []))
            desc = f'<p class="small text-secondary mb-1">{esc(it["desc"])}</p>' if it.get("desc") else ""
            items_html += f"""<li class="vt-menu-item py-3 border-bottom">
          <div class="d-flex justify-content-between align-items-baseline gap-3">
            <strong>{esc(it["name"])}</strong>
            <span class="vt-menu-price">{esc(it["price"])}</span>
          </div>
          {desc}
          <div>{tags}</div>
        </li>"""
        blocks += f"""<div class="col-lg-6">
        <h3 class="h5 vt-menu-cat border-bottom pb-2 mb-3">{esc(sec["title"])}</h3>
        <ul class="list-unstyled mb-0">{items_html}</ul>
      </div>"""
    return f"""<section class="vt-menu py-5 bg-white" aria-labelledby="menu-title">
  <div class="container">
    <div class="text-center mb-5">
      <h2 id="menu-title" class="vt-section-title">{esc(title)}</h2>
      <p class="text-secondary mx-auto" style="max-width:42rem">{esc(intro)}</p>
    </div>
    <div class="row g-5">{blocks}</div>
  </div>
</section>"""


def block_timeline(events: list[tuple[str, str]]) -> str:
    items = "".join(
        f"""<li class="vt-timeline-item pb-4">
        <strong class="d-block vt-timeline-date">{esc(d)}</strong>
        <span>{esc(t)}</span>
      </li>"""
        for d, t in events
    )
    return f"""<section class="py-5">
  <div class="container">
    <ol class="vt-timeline list-unstyled mx-auto mb-0">{items}</ol>
  </div>
</section>"""


def block_chef(name: str, role: str, bio: str) -> str:
    return f"""<section class="vt-chef py-5">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-8 text-center">
        <p class="vt-eyebrow text-uppercase">En cuisine</p>
        <h2 class="vt-section-title">{esc(name)}</h2>
        <p class="text-warning fw-semibold">{esc(role)}</p>
        <p class="text-secondary">{esc(bio)}</p>
      </div>
    </div>
  </div>
</section>"""


def block_reservation_form() -> str:
    return """<section class="vt-reserve py-5" aria-labelledby="reserve-title">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <h2 id="reserve-title" class="vt-section-title">Réserver une table</h2>
        <p class="text-secondary mb-4">Confirmation sous 2 h en semaine. Groupes de 8+ : appelez-nous directement.</p>
        <form class="row g-3" action="#" method="post">
          <div class="col-md-6"><label class="form-label">Date<input type="date" class="form-control" name="date" required></label></div>
          <div class="col-md-3"><label class="form-label">Heure<select class="form-select" name="time" required><option value="">Choisir…</option><option>12:00</option><option>12:30</option><option>13:00</option><option>19:00</option><option>19:30</option><option>20:00</option><option>20:30</option></select></label></div>
          <div class="col-md-3"><label class="form-label">Convives<select class="form-select" name="guests" required><option value="">Nb…</option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Nom<input type="text" class="form-control" name="name" autocomplete="name" required></label></div>
          <div class="col-md-6"><label class="form-label">Téléphone<input type="tel" class="form-control" name="phone" autocomplete="tel" required></label></div>
          <div class="col-12"><label class="form-label">E-mail<input type="email" class="form-control" name="email" autocomplete="email"></label></div>
          <div class="col-12"><label class="form-label">Message<textarea class="form-control" name="message" rows="3" placeholder="Allergie, anniversaire, terrasse si possible…"></textarea></label></div>
          <div class="col-12"><button type="submit" class="btn btn-vt-primary btn-lg rounded-pill px-5">Envoyer ma demande</button></div>
          <p class="small text-secondary mb-0">Démo vitrine — formulaire non connecté.</p>
        </form>
      </div>
      <aside class="col-lg-5">
        <div class="card border-0 shadow-sm p-4 h-100">
          <h2 class="h4 vt-section-title">Nous trouver</h2>
          <address class="text-secondary mb-3">
            <strong class="text-body">Brasserie Saint-Jacques</strong><br>
            12 place Saint-Jacques<br>
            57000 Metz
          </address>
          <p><a href="tel:0387751234">03 87 75 12 34</a><br>
          <a href="mailto:contact@brasserie-saint-jacques.fr">contact@brasserie-saint-jacques.fr</a></p>
          <table class="table table-sm vt-hours">
            <caption class="caption-top fw-semibold">Horaires</caption>
            <tbody>
              <tr><th>Mar – Ven</th><td>12h – 14h · 19h – 22h</td></tr>
              <tr><th>Samedi</th><td>12h – 14h30 · 19h – 23h</td></tr>
              <tr><th>Dimanche</th><td>Brunch 10h – 15h</td></tr>
              <tr><th>Lundi</th><td>Fermé</td></tr>
            </tbody>
          </table>
          <ul class="small text-secondary ps-3 mb-0">
            <li>Parking Saint-Jacques à 200 m</li>
            <li>Tram T2 — arrêt République</li>
            <li>Terrasse ouverte dès 12 °C</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def block_site_footer(
    brand: str,
    *,
    phone: str,
    address: str,
    email: str = "contact@brasserie-saint-jacques.fr",
    maps_href: str = "https://maps.google.com/?q=12+place+Saint-Jacques+57000+Metz",
    nav_links: list[tuple[str, str]] | None = None,
    hours_line: str = "Mar–sam midi & soir · Dim. brunch",
) -> str:
    if nav_links is None:
        nav_links = [
            ("La carte", "carte.html"),
            ("Notre histoire", "histoire.html"),
            ("Privatisation", "contact.html"),
            ("Recrutement", "contact.html"),
        ]
    nav_html = "".join(f'<a class="nav-link px-0" href="{esc(href)}">{esc(label)}</a>' for label, href in nav_links)
    email_line = f'<p class="mb-1"><a class="text-white" href="mailto:{esc(email)}">{esc(email)}</a></p>' if email else ""
    return f"""<footer class="vt-footer text-white">
  <div class="container py-5">
    <div class="row g-4">
      <div class="col-md-4">
        <strong class="vt-brand d-block mb-2">{esc(brand)}</strong>
        <p class="small opacity-75 mb-2">{esc(address)}</p>
        <a class="small" href="{esc(maps_href)}">Nous trouver →</a>
      </div>
      <div class="col-md-4">
        <nav class="nav flex-column small" aria-label="Pied de page">{nav_html}
        </nav>
      </div>
      <div class="col-md-4 small opacity-75">
        <p class="mb-1"><a class="text-white" href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a></p>
        {email_line}
        <p class="mb-0">{esc(hours_line)}</p>
      </div>
    </div>
    <hr class="border-secondary opacity-25 my-4">
    <p class="small opacity-50 mb-0"><a class="text-white" href="../index.html">← Catalogue vitrines DanielCraft</a> · Maquette démo</p>
  </div>
</footer>"""


def block_mobile_cta(label: str, href: str, phone: str) -> str:
    return f"""<div class="vt-mobile-bar d-lg-none" aria-label="Actions rapides">
  <a class="vt-mobile-bar-btn" href="tel:{esc(phone.replace(' ', ''))}">Appeler</a>
  <a class="vt-mobile-bar-btn vt-mobile-bar-primary" href="{esc(href)}">{esc(label)}</a>
</div>"""


def restaurant_jsonld() -> str:
    return """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "Brasserie Saint-Jacques",
  "servesCuisine": "Lorraine, French",
  "priceRange": "€€",
  "telephone": "+33387751234",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "12 place Saint-Jacques",
    "addressLocality": "Metz",
    "postalCode": "57000",
    "addressCountry": "FR"
  },
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Tuesday","Wednesday","Thursday","Friday"], "opens": "12:00", "closes": "22:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "12:00", "closes": "23:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "10:00", "closes": "15:00"}
  ]
}
</script>"""


def spa_jsonld() -> str:
    return """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BeautySalon",
  "name": "Spa Thalie",
  "telephone": "+33383567890",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "8 rue des Mésanges",
    "addressLocality": "Nancy",
    "postalCode": "54000",
    "addressCountry": "FR"
  },
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Tuesday","Wednesday","Thursday","Friday","Saturday"], "opens": "09:00", "closes": "20:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "10:00", "closes": "18:00"}
  ]
}
</script>"""


def block_appointment_form(
    *,
    brand: str = "Spa Thalie",
    address: str,
    phone: str,
    email: str,
) -> str:
    return f"""<section class="vt-reserve py-5" aria-labelledby="rdv-title">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <h2 id="rdv-title" class="vt-section-title">Prendre rendez-vous</h2>
        <p class="text-secondary mb-4">Confirmation sous 2 h. Annulation gratuite 24 h avant.</p>
        <form class="row g-3" action="#" method="post">
          <div class="col-md-6"><label class="form-label">Soin<select class="form-select" name="treatment" required><option value="">Choisir…</option><option>Soin visage éclat</option><option>Massage 60 min</option><option>Rituel Stanislas 90 min</option><option>Manucure spa</option></select></label></div>
          <div class="col-md-3"><label class="form-label">Date<input type="date" class="form-control" name="date" required></label></div>
          <div class="col-md-3"><label class="form-label">Heure<select class="form-select" name="time" required><option value="">Choisir…</option><option>10:00</option><option>11:30</option><option>14:00</option><option>16:00</option><option>18:00</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Prénom & nom<input type="text" class="form-control" name="name" autocomplete="name" required></label></div>
          <div class="col-md-6"><label class="form-label">Téléphone<input type="tel" class="form-control" name="phone" autocomplete="tel" required></label></div>
          <div class="col-12"><label class="form-label">E-mail<input type="email" class="form-control" name="email" autocomplete="email"></label></div>
          <div class="col-12"><label class="form-label">Message<textarea class="form-control" name="message" rows="3" placeholder="Première visite, allergies, préférences…"></textarea></label></div>
          <div class="col-12"><button type="submit" class="btn btn-vt-primary btn-lg rounded-pill px-5">Confirmer mon RDV</button></div>
          <p class="small text-secondary mb-0">Démo vitrine — formulaire non connecté.</p>
        </form>
      </div>
      <aside class="col-lg-5">
        <div class="card border-0 shadow-sm p-4 h-100">
          <h2 class="h4 vt-section-title">Accès & horaires</h2>
          <address class="text-secondary mb-3">
            <strong class="text-body">{esc(brand)}</strong><br>
            {esc(address)}
          </address>
          <p><a href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a><br>
          <a href="mailto:{esc(email)}">{esc(email)}</a></p>
          <table class="table table-sm vt-hours">
            <caption class="caption-top fw-semibold">Horaires</caption>
            <tbody>
              <tr><th>Mar – Sam</th><td>9h – 20h</td></tr>
              <tr><th>Dimanche</th><td>10h – 18h sur RDV</td></tr>
              <tr><th>Lundi</th><td>Fermé</td></tr>
            </tbody>
          </table>
          <ul class="small text-secondary ps-3 mb-0">
            <li>Tram T1 — arrêt Stanislas</li>
            <li>Parking Ville-Vieille à 150 m</li>
            <li>Visite institut : mer. 14h–17h</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def wrap_page(title: str, description: str, body: str, *, layout: str = "brasserie-bs") -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · Bootstrap 5 · vitrine site complet -->
{HEAD_RESTAURATION}
{restaurant_jsonld()}
</head>
<body class="vt-body">
{body.strip()}
{FOOT_SCRIPTS}
</body>
</html>
"""


def wrap_page_spa(title: str, description: str, body: str, *, layout: str = "spa-bs") -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · Bootstrap 5 · vitrine site complet -->
{HEAD_SPA}
{spa_jsonld()}
</head>
<body class="vt-body vt-body-spa">
{body.strip()}
{FOOT_SCRIPTS}
</body>
</html>
"""


def dental_jsonld() -> str:
    return """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dentist",
  "name": "Centre dentaire Mosaïque",
  "telephone": "+33382884500",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "42 avenue de la République",
    "addressLocality": "Thionville",
    "postalCode": "57100",
    "addressCountry": "FR"
  },
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "08:30", "closes": "19:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "08:00", "closes": "12:00"}
  ]
}
</script>"""


def block_dental_appointment_form(
    *,
    brand: str = "Centre dentaire Mosaïque",
    address: str,
    phone: str,
) -> str:
    return f"""<section class="vt-reserve py-5" aria-labelledby="rdv-title">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <h2 id="rdv-title" class="vt-section-title">Demander un rendez-vous</h2>
        <p class="text-secondary mb-4">Premier RDV découverte offert. Devis détaillé avant tout acte.</p>
        <form class="row g-3" action="#" method="post">
          <div class="col-md-6"><label class="form-label">Motif<select class="form-select" name="reason" required><option value="">Choisir…</option><option>Contrôle &amp; prévention</option><option>Douleur / urgence</option><option>Esthétique &amp; blanchiment</option><option>Orthodontie</option><option>Implant</option></select></label></div>
          <div class="col-md-3"><label class="form-label">Date<input type="date" class="form-control" name="date" required></label></div>
          <div class="col-md-3"><label class="form-label">Créneau<select class="form-select" name="time" required><option value="">Choisir…</option><option>8h30</option><option>10h</option><option>14h</option><option>16h30</option><option>18h</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Prénom &amp; nom<input type="text" class="form-control" name="name" autocomplete="name" required></label></div>
          <div class="col-md-6"><label class="form-label">Téléphone<input type="tel" class="form-control" name="phone" autocomplete="tel" required></label></div>
          <div class="col-12"><label class="form-label">E-mail<input type="email" class="form-control" name="email" autocomplete="email"></label></div>
          <div class="col-12"><label class="form-label">Message<textarea class="form-control" name="message" rows="3" placeholder="Première visite, mutuelle, préférence praticien…"></textarea></label></div>
          <div class="col-12"><button type="submit" class="btn btn-vt-primary btn-lg rounded-pill px-5">Confirmer ma demande</button></div>
          <p class="small text-secondary mb-0">Démo vitrine — formulaire non connecté.</p>
        </form>
      </div>
      <aside class="col-lg-5">
        <div class="card border-0 shadow-sm p-4 h-100">
          <h2 class="h4 vt-section-title">Accès &amp; urgences</h2>
          <address class="text-secondary mb-3">
            <strong class="text-body">{esc(brand)}</strong><br>
            {esc(address)}
          </address>
          <p><a href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a></p>
          <p class="small fw-semibold text-danger mb-2">Urgence douleur aiguë : appelez avant 11 h.</p>
          <table class="table table-sm vt-hours">
            <caption class="caption-top fw-semibold">Horaires</caption>
            <tbody>
              <tr><th>Lun – Ven</th><td>8h30 – 19h</td></tr>
              <tr><th>Samedi</th><td>8h – 12h</td></tr>
              <tr><th>Dimanche</th><td>Fermé</td></tr>
            </tbody>
          </table>
          <ul class="small text-secondary ps-3 mb-0">
            <li>Parking République</li>
            <li>Bus ligne 5 — Hôtel de Ville</li>
            <li>Tiers payant accepté</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def wrap_page_medical(title: str, description: str, body: str, *, layout: str = "medical-split") -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · Bootstrap 5 · vitrine site complet -->
{HEAD_MEDICAL}
{dental_jsonld()}
</head>
<body class="vt-body vt-body-medical">
{body.strip()}
{FOOT_SCRIPTS}
</body>
</html>
"""


def garage_jsonld() -> str:
    return """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AutoRepair",
  "name": "Garage Central Plappeville",
  "telephone": "+33387654321",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Zone artisanale des Gravières",
    "addressLocality": "Plappeville",
    "postalCode": "57050",
    "addressCountry": "FR"
  },
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "08:00", "closes": "18:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "08:00", "closes": "12:00"}
  ]
}
</script>"""


def block_garage_appointment_form(
    *,
    brand: str = "Garage Central Plappeville",
    address: str,
    phone: str,
) -> str:
    return f"""<section class="vt-reserve py-5" aria-labelledby="rdv-title">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <h2 id="rdv-title" class="vt-section-title text-uppercase">Prendre rendez-vous atelier</h2>
        <p class="text-secondary mb-4">Devis clair avant intervention. Véhicule de courtoisie sur demande.</p>
        <form class="row g-3" action="#" method="post">
          <div class="col-md-6"><label class="form-label">Prestation<select class="form-select" name="service" required><option value="">Choisir…</option><option>Révision / vidange</option><option>Pneus &amp; géométrie</option><option>Freinage</option><option>Carrosserie / devis assurance</option><option>Diagnostic électronique</option></select></label></div>
          <div class="col-md-3"><label class="form-label">Date<input type="date" class="form-control" name="date" required></label></div>
          <div class="col-md-3"><label class="form-label">Créneau<select class="form-select" name="time" required><option value="">Choisir…</option><option>8h</option><option>10h</option><option>14h</option><option>16h</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Véhicule<input type="text" class="form-control" name="vehicle" placeholder="Marque, modèle, immat." required></label></div>
          <div class="col-md-6"><label class="form-label">Téléphone<input type="tel" class="form-control" name="phone" autocomplete="tel" required></label></div>
          <div class="col-md-6"><label class="form-label">Prénom &amp; nom<input type="text" class="form-control" name="name" autocomplete="name" required></label></div>
          <div class="col-md-6"><label class="form-label">E-mail<input type="email" class="form-control" name="email" autocomplete="email"></label></div>
          <div class="col-12"><label class="form-label">Description<textarea class="form-control" name="message" rows="3" placeholder="Symptômes, bruits, voyants allumés…"></textarea></label></div>
          <div class="col-12"><button type="submit" class="btn btn-vt-primary btn-lg rounded-0 px-5">Confirmer mon RDV</button></div>
          <p class="small text-secondary mb-0">Démo vitrine — formulaire non connecté.</p>
        </form>
      </div>
      <aside class="col-lg-5">
        <div class="card border-0 shadow-sm p-4 h-100 vt-aside-panel">
          <h2 class="h4 vt-section-title text-uppercase">Accès &amp; horaires</h2>
          <address class="text-secondary mb-3">
            <strong class="text-body">{esc(brand)}</strong><br>
            {esc(address)}
          </address>
          <p><a href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a></p>
          <p class="small fw-semibold mb-2">Dépannage 24h/24 — numéro dédié sur demande.</p>
          <table class="table table-sm vt-hours">
            <caption class="caption-top fw-semibold">Horaires</caption>
            <tbody>
              <tr><th>Lun – Ven</th><td>8h – 18h</td></tr>
              <tr><th>Samedi</th><td>8h – 12h</td></tr>
              <tr><th>Dimanche</th><td>Fermé</td></tr>
            </tbody>
          </table>
          <ul class="small text-secondary ps-3 mb-0">
            <li>Sortie A31 — Plappeville</li>
            <li>Parking client devant l'atelier</li>
            <li>Café &amp; wifi en salle d'attente</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def wrap_page_garage(title: str, description: str, body: str, *, layout: str = "garage-overlay") -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · Bootstrap 5 · vitrine site complet -->
{HEAD_GARAGE}
{garage_jsonld()}
</head>
<body class="vt-body vt-body-garage">
{body.strip()}
{FOOT_SCRIPTS}
</body>
</html>
"""


def retail_jsonld() -> str:
    return """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "GroceryStore",
  "name": "Halles Thionville",
  "telephone": "+33382534000",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rue du Mail",
    "addressLocality": "Thionville",
    "postalCode": "57100",
    "addressCountry": "FR"
  },
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"], "opens": "08:00", "closes": "20:00"},
    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "09:00", "closes": "12:30"}
  ]
}
</script>"""


def block_retail_contact_form(
    *,
    brand: str = "Halles Thionville",
    address: str,
    phone: str,
    email: str,
) -> str:
    return f"""<section class="vt-reserve py-5" aria-labelledby="contact-title">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <h2 id="contact-title" class="vt-section-title">Nous écrire</h2>
        <p class="text-secondary mb-4">Réclamation, suggestion ou demande carte fidélité Halles+.</p>
        <form class="row g-3" action="#" method="post">
          <div class="col-md-6"><label class="form-label">Sujet<select class="form-select" name="topic" required><option value="">Choisir…</option><option>Carte Halles+</option><option>Drive / commande</option><option>Produit ou rayon</option><option>Autre</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Prénom &amp; nom<input type="text" class="form-control" name="name" autocomplete="name" required></label></div>
          <div class="col-md-6"><label class="form-label">E-mail<input type="email" class="form-control" name="email" autocomplete="email" required></label></div>
          <div class="col-md-6"><label class="form-label">Téléphone<input type="tel" class="form-control" name="phone" autocomplete="tel"></label></div>
          <div class="col-12"><label class="form-label">Message<textarea class="form-control" name="message" rows="4" placeholder="Votre message…" required></textarea></label></div>
          <div class="col-12"><button type="submit" class="btn btn-vt-primary btn-lg rounded-pill px-5">Envoyer</button></div>
          <p class="small text-secondary mb-0">Démo vitrine — formulaire non connecté.</p>
        </form>
      </div>
      <aside class="col-lg-5">
        <div class="card border-0 shadow-sm p-4 h-100 vt-aside-panel">
          <h2 class="h4 vt-section-title">Service client</h2>
          <address class="text-secondary mb-3">
            <strong class="text-body">{esc(brand)}</strong><br>
            {esc(address)}
          </address>
          <p><a href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a><br>
          <a href="mailto:{esc(email)}">{esc(email)}</a></p>
          <table class="table table-sm vt-hours">
            <caption class="caption-top fw-semibold">Horaires magasin</caption>
            <tbody>
              <tr><th>Lun – Sam</th><td>8h – 20h</td></tr>
              <tr><th>Dimanche</th><td>9h – 12h30</td></tr>
            </tbody>
          </table>
          <ul class="small text-secondary ps-3 mb-0">
            <li>Parking gratuit 200 places</li>
            <li>Drive : 15 emplacements couverts</li>
            <li>Bus ligne 5 — arrêt Mail</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def wrap_page_retail(title: str, description: str, body: str, *, layout: str = "retail-editorial") -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · Bootstrap 5 · vitrine site complet -->
{HEAD_RETAIL}
{retail_jsonld()}
</head>
<body class="vt-body vt-body-retail">
{body.strip()}
{FOOT_SCRIPTS}
</body>
</html>
"""


def accounting_jsonld() -> str:
    return """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AccountingService",
  "name": "Verlaine & Associés",
  "telephone": "+33387759012",
  "knowsAbout": ["Tenue comptable", "Paie et DSN", "Conseil dirigeant", "Fiscalité PME", "Bilan flash"],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "14 rue Serpenoise",
    "addressLocality": "Metz",
    "postalCode": "57000",
    "addressCountry": "FR"
  },
  "openingHoursSpecification": [
    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "09:00", "closes": "18:00"}
  ]
}
</script>"""


def block_cabinet_contact_form(
    *,
    brand: str = "Verlaine & Associés",
    address: str,
    phone: str,
    email: str,
) -> str:
    return f"""<section class="vt-reserve py-5" aria-labelledby="contact-title">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <h2 id="contact-title" class="vt-section-title">Consultation gratuite</h2>
        <p class="text-secondary mb-4">Réponse sous 24 h ouvrées. Premier échange sans engagement.</p>
        <form class="row g-3" action="#" method="post">
          <div class="col-md-6"><label class="form-label">Besoin<select class="form-select" name="need" required><option value="">Choisir…</option><option>Création d'entreprise</option><option>Tenue &amp; fiscalité</option><option>Paie &amp; social</option><option>Conseil dirigeant</option><option>Reprise de dossier</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Effectif<select class="form-select" name="size"><option value="">Choisir…</option><option>0–5 salariés</option><option>6–20</option><option>21–50</option><option>50+</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Prénom &amp; nom<input type="text" class="form-control" name="name" autocomplete="name" required></label></div>
          <div class="col-md-6"><label class="form-label">Société<input type="text" class="form-control" name="company"></label></div>
          <div class="col-md-6"><label class="form-label">Téléphone<input type="tel" class="form-control" name="phone" autocomplete="tel" required></label></div>
          <div class="col-md-6"><label class="form-label">E-mail<input type="email" class="form-control" name="email" autocomplete="email" required></label></div>
          <div class="col-12"><label class="form-label">Votre situation<textarea class="form-control" name="message" rows="4" placeholder="Création, reprise, difficultés de trésorerie…"></textarea></label></div>
          <div class="col-12"><button type="submit" class="btn btn-vt-primary btn-lg rounded-0 px-5">Envoyer ma demande</button></div>
          <p class="small text-secondary mb-0">Démo vitrine — formulaire non connecté.</p>
        </form>
      </div>
      <aside class="col-lg-5">
        <div class="card border-0 shadow-sm p-4 h-100 vt-aside-panel">
          <h2 class="h4 vt-section-title">Cabinet</h2>
          <address class="text-secondary mb-3">
            <strong class="text-body">{esc(brand)}</strong><br>
            {esc(address)}
          </address>
          <p><a href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a><br>
          <a href="mailto:{esc(email)}">{esc(email)}</a></p>
          <table class="table table-sm vt-hours">
            <caption class="caption-top fw-semibold">Horaires</caption>
            <tbody>
              <tr><th>Lun – Ven</th><td>9h – 18h</td></tr>
              <tr><th>Samedi</th><td>Sur RDV</td></tr>
            </tbody>
          </table>
          <ul class="small text-secondary ps-3 mb-0">
            <li>Ordre des experts-comptables — Grand Est</li>
            <li>Bilan flash sous 48 h</li>
            <li>Metz &amp; Thionville</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def wrap_page_cabinet(title: str, description: str, body: str, *, layout: str = "cabinet-proof") -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · Bootstrap 5 · vitrine site complet -->
{HEAD_CABINET}
{accounting_jsonld()}
</head>
<body class="vt-body vt-body-cabinet">
{body.strip()}
{FOOT_SCRIPTS}
</body>
</html>
"""


def industrial_jsonld() -> str:
    return """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Précisite Usinage",
  "description": "Usinage de précision 5 axes, automobile et aéronautique",
  "telephone": "+33387224466",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Zone industrielle des Hauts Champs",
    "addressLocality": "Yutz",
    "postalCode": "57970",
    "addressCountry": "FR"
  }
}
</script>"""


def block_industrial_rfq_form(
    *,
    brand: str = "Précisite Usinage",
    address: str,
    phone: str,
    email: str,
) -> str:
    return f"""<section class="vt-reserve py-5" aria-labelledby="rfq-title">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <h2 id="rfq-title" class="vt-section-title text-uppercase">Demande de devis (RFQ)</h2>
        <p class="text-secondary mb-4">Réponse technique sous 48 h. Plans STEP/IGES acceptés.</p>
        <form class="row g-3" action="#" method="post">
          <div class="col-md-6"><label class="form-label">Procédé<select class="form-select" name="process" required><option value="">Choisir…</option><option>Usinage 5 axes</option><option>Tournage CNC</option><option>Fraisage</option><option>Contrôle 3D</option><option>Série / prototype</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Matériau<input type="text" class="form-control" name="material" placeholder="Alu 7075, acier, titane…"></label></div>
          <div class="col-md-4"><label class="form-label">Quantité<input type="text" class="form-control" name="qty" placeholder="ex. 500 pièces/an"></label></div>
          <div class="col-md-4"><label class="form-label">Tolérance<input type="text" class="form-control" name="tolerance" placeholder="ex. ±0,01 mm"></label></div>
          <div class="col-md-4"><label class="form-label">Délai souhaité<input type="text" class="form-control" name="deadline" placeholder="ex. S32 2026"></label></div>
          <div class="col-md-6"><label class="form-label">Société<input type="text" class="form-control" name="company" required></label></div>
          <div class="col-md-6"><label class="form-label">Contact<input type="text" class="form-control" name="name" autocomplete="name" required></label></div>
          <div class="col-md-6"><label class="form-label">E-mail<input type="email" class="form-control" name="email" autocomplete="email" required></label></div>
          <div class="col-md-6"><label class="form-label">Téléphone<input type="tel" class="form-control" name="phone" autocomplete="tel"></label></div>
          <div class="col-12"><label class="form-label">Spécifications<textarea class="form-control" name="message" rows="4" placeholder="Référence pièce, finition, secteur (auto, aéro)…"></textarea></label></div>
          <div class="col-12"><button type="submit" class="btn btn-vt-primary rounded-0 px-5">Envoyer la RFQ</button></div>
          <p class="small text-secondary mb-0">Démo vitrine — formulaire non connecté.</p>
        </form>
      </div>
      <aside class="col-lg-5">
        <div class="card border-0 shadow-sm p-4 h-100 vt-aside-panel">
          <h2 class="h4 vt-section-title text-uppercase">Site de production</h2>
          <address class="text-secondary mb-3">
            <strong class="text-body">{esc(brand)}</strong><br>
            {esc(address)}
          </address>
          <p><a href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a><br>
          <a href="mailto:{esc(email)}">{esc(email)}</a></p>
          <table class="table table-sm vt-hours">
            <caption class="caption-top fw-semibold">Horaires</caption>
            <tbody>
              <tr><th>Lun – Ven</th><td>7h – 18h</td></tr>
              <tr><th>Samedi</th><td>Sur demande</td></tr>
            </tbody>
          </table>
          <ul class="small text-secondary ps-3 mb-0">
            <li>ISO 9001 · IATF 16949</li>
            <li>12 centres 5 axes</li>
            <li>Métrologie 3D sur site</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def wrap_page_industrial(title: str, description: str, body: str, *, layout: str = "industrial-spec") -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · Bootstrap 5 · vitrine site complet -->
{HEAD_INDUSTRIAL}
{industrial_jsonld()}
</head>
<body class="vt-body vt-body-industrial">
{body.strip()}
{FOOT_SCRIPTS}
</body>
</html>
"""


def property_jsonld() -> str:
    return """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "RealEstateAgent",
  "name": "Patrimoine Lorraine",
  "description": "Agence immobilière Nancy — vente, location et estimation",
  "telephone": "+33383352890",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "8 place Stanislas",
    "addressLocality": "Nancy",
    "postalCode": "54000",
    "addressCountry": "FR"
  }
}
</script>"""


def block_property_estimation_form(
    *,
    brand: str = "Patrimoine Lorraine",
    address: str,
    phone: str,
    email: str,
) -> str:
    return f"""<section class="vt-reserve py-5" aria-labelledby="estim-title">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <h2 id="estim-title" class="vt-section-title">Estimation gratuite</h2>
        <p class="text-secondary mb-4">Réponse sous 72 h — visite optionnelle à Nancy et environs.</p>
        <form class="row g-3" action="#" method="post">
          <div class="col-md-6"><label class="form-label">Type de bien<select class="form-select" name="type" required><option value="">Choisir…</option><option>Maison</option><option>Appartement</option><option>Terrain</option><option>Immeuble</option><option>Local commercial</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Surface (m²)<input type="number" class="form-control" name="surface" min="10" placeholder="ex. 95"></label></div>
          <div class="col-12"><label class="form-label">Adresse du bien<input type="text" class="form-control" name="address" placeholder="Rue, code postal, ville" required></label></div>
          <div class="col-md-6"><label class="form-label">Projet<select class="form-select" name="project"><option>Vendre</option><option>Louer</option><option>Estimer seulement</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Délai souhaité<input type="text" class="form-control" name="deadline" placeholder="ex. sous 3 mois"></label></div>
          <div class="col-md-6"><label class="form-label">Nom<input type="text" class="form-control" name="name" autocomplete="name" required></label></div>
          <div class="col-md-6"><label class="form-label">Téléphone<input type="tel" class="form-control" name="phone" autocomplete="tel" required></label></div>
          <div class="col-12"><label class="form-label">E-mail<input type="email" class="form-control" name="email" autocomplete="email" required></label></div>
          <div class="col-12"><label class="form-label">Précisions<textarea class="form-control" name="message" rows="3" placeholder="État, travaux, stationnement…"></textarea></label></div>
          <div class="col-12"><button type="submit" class="btn btn-vt-primary rounded-pill px-5">Recevoir mon estimation</button></div>
          <p class="small text-secondary mb-0">Démo vitrine — formulaire non connecté.</p>
        </form>
      </div>
      <aside class="col-lg-5">
        <div class="card border-0 shadow-sm p-4 h-100 vt-aside-panel">
          <h2 class="h4 vt-section-title">Agence Nancy</h2>
          <address class="text-secondary mb-3">
            <strong class="text-body">{esc(brand)}</strong><br>
            {esc(address)}
          </address>
          <p><a href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a><br>
          <a href="mailto:{esc(email)}">{esc(email)}</a></p>
          <table class="table table-sm vt-hours">
            <caption class="caption-top fw-semibold">Permanences</caption>
            <tbody>
              <tr><th>Lun – Ven</th><td>9h – 19h</td></tr>
              <tr><th>Samedi</th><td>10h – 13h</td></tr>
            </tbody>
          </table>
          <ul class="small text-secondary ps-3 mb-0">
            <li>Estimation gratuite sous 72 h</li>
            <li>340+ ventes par an</li>
            <li>Nancy, Metz, Thionville</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def wrap_page_property(title: str, description: str, body: str, *, layout: str = "property-search") -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · Bootstrap 5 · vitrine site complet -->
{HEAD_PROPERTY}
{property_jsonld()}
</head>
<body class="vt-body vt-body-property">
{body.strip()}
{FOOT_SCRIPTS}
</body>
</html>
"""


def legal_jsonld() -> str:
    return """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "name": "Rivière & Partenaires",
  "description": "Cabinet d'avocats Metz — droit des affaires, social et contentieux",
  "telephone": "+33387759012",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "12 avenue Foch",
    "addressLocality": "Metz",
    "postalCode": "57000",
    "addressCountry": "FR"
  }
}
</script>"""


def block_legal_consultation_form(
    *,
    brand: str = "Rivière & Partenaires",
    address: str,
    phone: str,
    email: str,
) -> str:
    return f"""<section class="vt-reserve py-5" aria-labelledby="legal-title">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <h2 id="legal-title" class="vt-section-title">Demande de consultation</h2>
        <p class="text-secondary mb-4">Réponse sous 24 h ouvrées — premier échange confidentiel.</p>
        <form class="row g-3" action="#" method="post">
          <div class="col-md-6"><label class="form-label">Domaine<select class="form-select" name="domain" required><option value="">Choisir…</option><option>Droit des sociétés</option><option>Droit social</option><option>Contentieux commercial</option><option>Transmission d'entreprise</option><option>Immobilier d'affaires</option><option>Famille &amp; patrimoine</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Urgence<select class="form-select" name="urgency"><option>Standard</option><option>Sous 48 h</option><option>Urgent</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Prénom &amp; nom<input type="text" class="form-control" name="name" autocomplete="name" required></label></div>
          <div class="col-md-6"><label class="form-label">Société / statut<input type="text" class="form-control" name="company" placeholder="PME, dirigeant, particulier…"></label></div>
          <div class="col-md-6"><label class="form-label">Téléphone<input type="tel" class="form-control" name="phone" autocomplete="tel" required></label></div>
          <div class="col-md-6"><label class="form-label">E-mail<input type="email" class="form-control" name="email" autocomplete="email" required></label></div>
          <div class="col-12"><label class="form-label">Votre situation<textarea class="form-control" name="message" rows="4" placeholder="Contexte, enjeux, documents disponibles…"></textarea></label></div>
          <div class="col-12"><button type="submit" class="btn btn-vt-primary btn-lg rounded-0 px-5">Demander une consultation</button></div>
          <p class="small text-secondary mb-0">Démo vitrine — formulaire non connecté. Secret professionnel simulé.</p>
        </form>
      </div>
      <aside class="col-lg-5">
        <div class="card border-0 shadow-sm p-4 h-100 vt-aside-panel vt-aside-legal">
          <h2 class="h4 vt-section-title">Cabinet Metz</h2>
          <address class="text-secondary mb-3">
            <strong class="text-body">{esc(brand)}</strong><br>
            {esc(address)}
          </address>
          <p><a href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a><br>
          <a href="mailto:{esc(email)}">{esc(email)}</a></p>
          <table class="table table-sm vt-hours">
            <caption class="caption-top fw-semibold">Permanences</caption>
            <tbody>
              <tr><th>Lun – Ven</th><td>9h – 18h</td></tr>
              <tr><th>Samedi</th><td>Sur RDV</td></tr>
            </tbody>
          </table>
          <ul class="small text-secondary ps-3 mb-0">
            <li>Barreau de Metz — 6 associés</li>
            <li>Forfait découverte 290 € HT</li>
            <li>Médiation et arbitrage</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def wrap_page_legal(title: str, description: str, body: str, *, layout: str = "legal-overlay") -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · Bootstrap 5 · vitrine site complet -->
{HEAD_LEGAL}
{legal_jsonld()}
</head>
<body class="vt-body vt-body-legal">
{body.strip()}
{FOOT_SCRIPTS}
</body>
</html>
"""


def architecture_jsonld() -> str:
    return """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Atelier Nord-Est",
  "description": "Agence d'architecture Metz — réhabilitation et conception durable",
  "telephone": "+33387661234",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "14 rue du XXe Corps",
    "addressLocality": "Metz",
    "postalCode": "57000",
    "addressCountry": "FR"
  }
}
</script>"""


def education_jsonld() -> str:
    return """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "EducationalOrganization",
  "name": "Institut Mercure",
  "description": "Centre de formation professionnelle Thionville — alternance et reconversion",
  "telephone": "+33382884500",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "15 avenue des Deux Fontaines",
    "addressLocality": "Thionville",
    "postalCode": "57100",
    "addressCountry": "FR"
  }
}
</script>"""


def block_education_enrollment_form(
    *,
    brand: str = "Institut Mercure",
    address: str,
    phone: str,
    email: str,
) -> str:
    return f"""<section class="vt-reserve py-5" aria-labelledby="enroll-title">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <h2 id="enroll-title" class="vt-section-title">Demande d'inscription</h2>
        <p class="text-secondary mb-4">Réponse sous 48 h — entretien d'orientation offert.</p>
        <form class="row g-3" action="#" method="post">
          <div class="col-md-6"><label class="form-label">Prénom<input type="text" class="form-control" name="firstname" autocomplete="given-name" required></label></div>
          <div class="col-md-6"><label class="form-label">Nom<input type="text" class="form-control" name="lastname" autocomplete="family-name" required></label></div>
          <div class="col-md-6"><label class="form-label">E-mail<input type="email" class="form-control" name="email" autocomplete="email" required></label></div>
          <div class="col-md-6"><label class="form-label">Téléphone<input type="tel" class="form-control" name="phone" autocomplete="tel" required></label></div>
          <div class="col-md-6"><label class="form-label">Parcours visé<select class="form-select" name="program" required><option value="">Choisir…</option><option>Développeur web (alternance)</option><option>BTS Management</option><option>Comptabilité — titre pro</option><option>Marketing digital</option><option>VAE / bilan compétences</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Situation<select class="form-select" name="status"><option value="">Choisir…</option><option>Demandeur d'emploi</option><option>Salarié en reconversion</option><option>Étudiant</option><option>Alternant</option></select></label></div>
          <div class="col-12"><label class="form-label">Message<textarea class="form-control" name="message" rows="3" placeholder="Objectifs, financement CPF, date de début souhaitée…"></textarea></label></div>
          <div class="col-12"><button type="submit" class="btn btn-vt-primary btn-lg px-5">Envoyer ma demande</button></div>
          <p class="small text-secondary mb-0">Démo vitrine — formulaire non connecté.</p>
        </form>
      </div>
      <aside class="col-lg-5">
        <div class="card border-0 p-4 h-100 vt-aside-panel">
          <h2 class="h4 vt-section-title">Campus Thionville</h2>
          <address class="text-secondary mb-3">
            <strong class="text-body">{esc(brand)}</strong><br>
            {esc(address)}
          </address>
          <p><a href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a><br>
          <a href="mailto:{esc(email)}">{esc(email)}</a></p>
          <ul class="small text-secondary ps-3 mb-0">
            <li>Certifié Qualiopi</li>
            <li>Financement CPF / OPCO</li>
            <li>92 % d'insertion à 6 mois</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def facility_jsonld() -> str:
    return """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Proprio Facility",
  "description": "Facility management et conciergerie pour immeubles tertiaires en Lorraine",
  "telephone": "+33387654321",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "8 place Saint-Jacques",
    "addressLocality": "Metz",
    "postalCode": "57000",
    "addressCountry": "FR"
  }
}
</script>"""


def block_facility_quote_form(
    *,
    brand: str = "Proprio Facility",
    address: str,
    phone: str,
    email: str,
) -> str:
    return f"""<section class="vt-reserve py-5" aria-labelledby="quote-title">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <h2 id="quote-title" class="vt-section-title">Demande de devis FM</h2>
        <p class="text-secondary mb-4">Audit gratuit sur site — proposition sous 5 jours ouvrés.</p>
        <form class="row g-3" action="#" method="post">
          <div class="col-md-6"><label class="form-label">Type de site<select class="form-select" name="site_type" required><option value="">Choisir…</option><option>Immeuble de bureaux</option><option>Centre commercial</option><option>Établissement de santé</option><option>Entrepôt / logistique</option><option>Site mixte</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Surface (m²)<input type="text" class="form-control" name="surface" placeholder="ex. 12 000" required></label></div>
          <div class="col-md-6"><label class="form-label">Offre visée<select class="form-select" name="offer"><option value="">Choisir…</option><option>Essentiel — maintenance</option><option>Premium — FM intégré</option><option>Sur mesure — multi-sites</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Prestations<select class="form-select" name="services" multiple size="1"><option>Maintenance CVC</option><option>Accueil &amp; standard</option><option>Conciergerie</option><option>Nettoyage</option><option>Sécurité &amp; accès</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Société / syndic<input type="text" class="form-control" name="company" required></label></div>
          <div class="col-md-6"><label class="form-label">Contact<input type="text" class="form-control" name="name" autocomplete="name" required></label></div>
          <div class="col-md-6"><label class="form-label">E-mail<input type="email" class="form-control" name="email" autocomplete="email" required></label></div>
          <div class="col-md-6"><label class="form-label">Téléphone<input type="tel" class="form-control" name="phone" autocomplete="tel" required></label></div>
          <div class="col-12"><label class="form-label">Contexte<textarea class="form-control" name="message" rows="3" placeholder="Adresse du site, horaires d'exploitation, contraintes…"></textarea></label></div>
          <div class="col-12"><button type="submit" class="btn btn-vt-primary btn-lg px-5">Envoyer ma demande</button></div>
          <p class="small text-secondary mb-0">Démo vitrine — formulaire non connecté.</p>
        </form>
      </div>
      <aside class="col-lg-5">
        <div class="card border-0 p-4 h-100 vt-aside-panel">
          <h2 class="h4 vt-section-title">Agence Metz</h2>
          <address class="text-secondary mb-3">
            <strong class="text-body">{esc(brand)}</strong><br>
            {esc(address)}
          </address>
          <p><a href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a><br>
          <a href="mailto:{esc(email)}">{esc(email)}</a></p>
          <ul class="small text-secondary ps-3 mb-0">
            <li>ISO 9001 · ISO 14001</li>
            <li>Astreinte 24 h / 24 — 7 j / 7</li>
            <li>200+ sites gérés en Grand Est</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def association_jsonld() -> str:
    return """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "NGO",
  "name": "Solidarités Metz Métropole",
  "description": "Association d'utilité publique Metz — aide alimentaire, insertion et bénévolat",
  "telephone": "+33387345678",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "22 rue du Sablon",
    "addressLocality": "Metz",
    "postalCode": "57000",
    "addressCountry": "FR"
  }
}
</script>"""


def block_association_contact_form(
    *,
    brand: str = "Solidarités Metz Métropole",
    address: str,
    phone: str,
    email: str,
) -> str:
    return f"""<section class="vt-reserve py-5" aria-labelledby="engage-title">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <h2 id="engage-title" class="vt-section-title">Je m'engage</h2>
        <p class="text-secondary mb-4">Don ponctuel ou candidature bénévole — réponse sous 48 h.</p>
        <form class="row g-3" action="#" method="post">
          <div class="col-12"><label class="form-label">Je souhaite<select class="form-select" name="intent" required><option value="">Choisir…</option><option>Faire un don</option><option>Devenir bénévole</option><option>Les deux</option><option>Entreprise mécène</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Prénom et nom<input type="text" class="form-control" name="name" autocomplete="name" required></label></div>
          <div class="col-md-6"><label class="form-label">E-mail<input type="email" class="form-control" name="email" autocomplete="email" required></label></div>
          <div class="col-md-6"><label class="form-label">Téléphone<input type="tel" class="form-control" name="phone" autocomplete="tel"></label></div>
          <div class="col-md-6"><label class="form-label">Montant du don (€)<input type="number" class="form-control" name="amount" min="5" step="5" placeholder="ex. 50"></label></div>
          <div class="col-12"><label class="form-label">Disponibilités bénévole<select class="form-select" name="availability"><option value="">Choisir…</option><option>Week-ends</option><option>Soirées en semaine</option><option>1/2 journée par mois</option><option>Maraude uniquement</option></select></label></div>
          <div class="col-12"><label class="form-label">Message<textarea class="form-control" name="message" rows="3" placeholder="Compétences, motivation, questions…"></textarea></label></div>
          <div class="col-12"><button type="submit" class="btn btn-vt-primary btn-lg px-5">Envoyer ma demande</button></div>
          <p class="small text-secondary mb-0">Démo vitrine — formulaire non connecté. Reçu fiscal sur demande pour les dons.</p>
        </form>
      </div>
      <aside class="col-lg-5">
        <div class="card border-0 p-4 h-100 vt-aside-panel">
          <h2 class="h4 vt-section-title">Siège Metz</h2>
          <address class="text-secondary mb-3">
            <strong class="text-body">{esc(brand)}</strong><br>
            {esc(address)}
          </address>
          <p><a href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a><br>
          <a href="mailto:{esc(email)}">{esc(email)}</a></p>
          <ul class="small text-secondary ps-3 mb-0">
            <li>Association loi 1901 — utilité publique</li>
            <li>120 bénévoles · 45 salariés</li>
            <li>Don déductible à 66 %</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def photo_jsonld() -> str:
    return """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Studio Lumière Grise",
  "description": "Photographe mariage et corporate à Nancy — reportages et portraits",
  "telephone": "+33383321840",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "8 place Stanislas",
    "addressLocality": "Nancy",
    "postalCode": "54000",
    "addressCountry": "FR"
  }
}
</script>"""


def block_photo_quote_form(
    *,
    brand: str = "Studio Lumière Grise",
    address: str,
    phone: str,
    email: str,
) -> str:
    return f"""<section class="vt-reserve py-5" aria-labelledby="quote-title">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <h2 id="quote-title" class="vt-section-title">Demande de devis</h2>
        <p class="text-secondary mb-4">Réponse personnalisée sous 24 h — sans engagement.</p>
        <form class="row g-3" action="#" method="post">
          <div class="col-md-6"><label class="form-label">Nom<input type="text" class="form-control" name="name" autocomplete="name" required></label></div>
          <div class="col-md-6"><label class="form-label">E-mail<input type="email" class="form-control" name="email" autocomplete="email" required></label></div>
          <div class="col-md-6"><label class="form-label">Téléphone<input type="tel" class="form-control" name="phone" autocomplete="tel"></label></div>
          <div class="col-md-6"><label class="form-label">Type de projet<select class="form-select" name="type" required><option value="">Choisir…</option><option>Portrait</option><option>Mariage</option><option>Corporate</option><option>Éditorial</option><option>Architecture</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Date souhaitée<input type="date" class="form-control" name="date"></label></div>
          <div class="col-md-6"><label class="form-label">Lieu<input type="text" class="form-control" name="place" placeholder="Nancy, Metz, Grand Est…"></label></div>
          <div class="col-12"><label class="form-label">Décrivez votre projet<textarea class="form-control" name="message" rows="4" placeholder="Ambiance, nombre de personnes, livrables attendus…"></textarea></label></div>
          <div class="col-12"><button type="submit" class="btn btn-vt-primary px-5">Envoyer ma demande</button></div>
          <p class="small text-secondary mb-0">Démo vitrine — formulaire non connecté.</p>
        </form>
      </div>
      <aside class="col-lg-5">
        <div class="card border-0 p-4 h-100 vt-aside-panel">
          <h2 class="h4 vt-section-title">Studio Nancy</h2>
          <address class="text-secondary mb-3">
            <strong class="text-body">{esc(brand)}</strong><br>
            {esc(address)}
          </address>
          <p><a href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a><br>
          <a href="mailto:{esc(email)}">{esc(email)}</a></p>
          <ul class="small text-secondary ps-3 mb-0">
            <li>240+ mariages depuis 2010</li>
            <li>Déplacements Grand Est</li>
            <li>Livraison web + tirages</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def fitness_jsonld() -> str:
    return """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SportsActivityLocation",
  "name": "Pulse Fitness Metz",
  "description": "Salle de sport Metz — cours collectifs, musculation et essai gratuit",
  "telephone": "+33387554000",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "42 avenue de Strasbourg",
    "addressLocality": "Metz",
    "postalCode": "57000",
    "addressCountry": "FR"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "opens": "06:00",
    "closes": "23:00"
  }
}
</script>"""


def block_fitness_trial_form(
    *,
    brand: str = "Pulse Fitness Metz",
    address: str,
    phone: str,
    email: str,
) -> str:
    return f"""<section class="vt-reserve py-5" aria-labelledby="trial-title">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <h2 id="trial-title" class="vt-section-title">Réserver mon essai gratuit</h2>
        <p class="text-secondary mb-4">Séance découverte offerte — réponse sous 24 h.</p>
        <form class="row g-3" action="#" method="post">
          <div class="col-md-6"><label class="form-label">Prénom<input type="text" class="form-control" name="firstname" autocomplete="given-name" required></label></div>
          <div class="col-md-6"><label class="form-label">Nom<input type="text" class="form-control" name="lastname" autocomplete="family-name" required></label></div>
          <div class="col-md-6"><label class="form-label">Téléphone<input type="tel" class="form-control" name="phone" autocomplete="tel" required></label></div>
          <div class="col-md-6"><label class="form-label">E-mail<input type="email" class="form-control" name="email" autocomplete="email"></label></div>
          <div class="col-12"><label class="form-label">Cours souhaité<select class="form-select" name="course" required><option value="">Choisir…</option><option>HIIT &amp; Cross</option><option>Cycling</option><option>Yoga Flow</option><option>Musculation libre</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Créneau préféré<select class="form-select" name="slot"><option value="">Choisir…</option><option>Matin (6h–10h)</option><option>Midi (12h–14h)</option><option>Soir (18h–21h)</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Objectif<select class="form-select" name="goal"><option value="">Choisir…</option><option>Perte de poids</option><option>Renforcement</option><option>Cardio</option><option>Bien-être</option></select></label></div>
          <div class="col-12"><label class="form-label">Message<textarea class="form-control" name="message" rows="3" placeholder="Première visite, niveau sportif, contrainte médicale…"></textarea></label></div>
          <div class="col-12"><button type="submit" class="btn btn-vt-primary btn-lg px-5">Je réserve mon essai</button></div>
          <p class="small text-secondary mb-0">Démo vitrine — formulaire non connecté.</p>
        </form>
      </div>
      <aside class="col-lg-5">
        <div class="card border-0 p-4 h-100 vt-aside-panel">
          <h2 class="h4 vt-section-title">Club Metz Sablon</h2>
          <address class="text-secondary mb-3">
            <strong class="text-body">{esc(brand)}</strong><br>
            {esc(address)}
          </address>
          <p><a href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a><br>
          <a href="mailto:{esc(email)}">{esc(email)}</a></p>
          <ul class="small text-secondary ps-3 mb-0">
            <li>Ouvert 6h–23h, 7j/7</li>
            <li>1 200 m² — vestiaires premium</li>
            <li>8 coachs certifiés</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def block_architecture_brief_form(
    *,
    brand: str = "Atelier Nord-Est",
    address: str,
    phone: str,
    email: str,
) -> str:
    return f"""<section class="vt-reserve py-5" aria-labelledby="brief-title">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <h2 id="brief-title" class="vt-section-title">Brief projet</h2>
        <p class="text-secondary mb-4">Réponse sous 48 h — premier échange sans engagement.</p>
        <form class="row g-3" action="#" method="post">
          <div class="col-md-6"><label class="form-label">Type de projet<select class="form-select" name="type" required><option value="">Choisir…</option><option>Réhabilitation</option><option>Logement neuf</option><option>Extension</option><option>ERP / équipement public</option><option>Aménagement intérieur</option></select></label></div>
          <div class="col-md-6"><label class="form-label">Budget indicatif<select class="form-select" name="budget"><option value="">Choisir…</option><option>&lt; 200 k€</option><option>200 – 500 k€</option><option>500 k€ – 1 M€</option><option>&gt; 1 M€</option></select></label></div>
          <div class="col-12"><label class="form-label">Adresse / commune du projet<input type="text" class="form-control" name="site" placeholder="Metz, Thionville, Nancy…"></label></div>
          <div class="col-md-6"><label class="form-label">Surface (m²)<input type="number" class="form-control" name="surface" min="20" placeholder="ex. 180"></label></div>
          <div class="col-md-6"><label class="form-label">Délai souhaité<input type="text" class="form-control" name="deadline" placeholder="ex. permis en 2026"></label></div>
          <div class="col-md-6"><label class="form-label">Nom<input type="text" class="form-control" name="name" autocomplete="name" required></label></div>
          <div class="col-md-6"><label class="form-label">Téléphone<input type="tel" class="form-control" name="phone" autocomplete="tel" required></label></div>
          <div class="col-12"><label class="form-label">E-mail<input type="email" class="form-control" name="email" autocomplete="email" required></label></div>
          <div class="col-12"><label class="form-label">Description du projet<textarea class="form-control" name="message" rows="4" placeholder="Programme, contraintes, inspirations…"></textarea></label></div>
          <div class="col-12"><button type="submit" class="btn btn-vt-primary rounded-0 px-5">Envoyer mon brief</button></div>
          <p class="small text-secondary mb-0">Démo vitrine — formulaire non connecté.</p>
        </form>
      </div>
      <aside class="col-lg-5">
        <div class="card border-0 p-4 h-100 vt-aside-panel">
          <h2 class="h4 vt-section-title">Atelier Metz</h2>
          <address class="text-secondary mb-3">
            <strong class="text-body">{esc(brand)}</strong><br>
            {esc(address)}
          </address>
          <p><a href="tel:{esc(phone.replace(' ', ''))}">{esc(phone)}</a><br>
          <a href="mailto:{esc(email)}">{esc(email)}</a></p>
          <ul class="small text-secondary ps-3 mb-0">
            <li>Ordre des architectes — Grand Est</li>
            <li>RE2020 &amp; réhabilitation patrimoine</li>
            <li>Metz, Nancy, Thionville</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def wrap_page_facility(title: str, description: str, body: str, *, layout: str = "facility-fm") -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · Bootstrap 5 · vitrine site complet -->
{HEAD_FACILITY}
{facility_jsonld()}
</head>
<body class="vt-body vt-body-facility">
{body.strip()}
{FOOT_SCRIPTS}
</body>
</html>
"""


def wrap_page_education(title: str, description: str, body: str, *, layout: str = "campus-academic") -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · Bootstrap 5 · vitrine site complet -->
{HEAD_EDUCATION}
{education_jsonld()}
</head>
<body class="vt-body vt-body-education">
{body.strip()}
{FOOT_SCRIPTS}
</body>
</html>
"""


def wrap_page_association(title: str, description: str, body: str, *, layout: str = "ess-impact") -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · Bootstrap 5 · vitrine site complet -->
{HEAD_ASSOCIATION}
{association_jsonld()}
</head>
<body class="vt-body vt-body-association">
{body.strip()}
{FOOT_SCRIPTS}
</body>
</html>
"""


def wrap_page_photo(title: str, description: str, body: str, *, layout: str = "photo-masonry") -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · Bootstrap 5 · vitrine site complet -->
{HEAD_PHOTO}
{photo_jsonld()}
</head>
<body class="vt-body vt-body-photo">
{body.strip()}
{FOOT_SCRIPTS}
</body>
</html>
"""


def wrap_page_fitness(title: str, description: str, body: str, *, layout: str = "fitness-schedule") -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · Bootstrap 5 · vitrine site complet -->
{HEAD_FITNESS}
{fitness_jsonld()}
</head>
<body class="vt-body vt-body-fitness">
{body.strip()}
{FOOT_SCRIPTS}
</body>
</html>
"""


def wrap_page_architecture(title: str, description: str, body: str, *, layout: str = "architecture-editorial") -> str:
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(description)}">
  <title>{esc(title)}</title>
  <!-- layout: {layout} · Bootstrap 5 · vitrine site complet -->
{HEAD_ARCHITECTURE}
{architecture_jsonld()}
</head>
<body class="vt-body vt-body-architecture">
{body.strip()}
{FOOT_SCRIPTS}
</body>
</html>
"""
