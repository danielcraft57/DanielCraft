#!/usr/bin/env python3
"""Apply hero/stats/CSS patches to 9 vitrine demos."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"
MEDIA = '  <link rel="stylesheet" href="../shared/vitrine-media.css">\n'
MC = "vitrine-figure--" + "motion"
D = "motion"  # only for building class name above


def fig(gallery, png, svg, alt, title, col="column is-6"):
    return f"""            <div class="{col} vitrine-img-reveal">
              <figure class="vitrine-figure vitrine-hero-visual vitrine-figure--ken {MC} mb-0">
                <a href="images/{svg}" class="glightbox" data-gallery="{gallery}" data-glightbox="title: {title}">
                  <img src="images/{png}" width="1200" height="675" alt="{alt}" decoding="async" fetchpriority="high">
                </a>
              </figure>
            </div>"""


def stats(css, rows):
    cols = "".join(
        f'          <div class="column"><p class="title is-2 has-text-white mb-1">{a}</p>'
        f'<p class="subtitle is-6 has-text-white-ter">{b}</p></div>\n'
        for a, b in rows
    )
    return f"""
    <section class="section {css} py-5" aria-label="Chiffres clés">
      <div class="container">
        <div class="columns has-text-centered mb-0">
{cols}        </div>
      </div>
    </section>
"""


def ensure_media(html):
    if "vitrine-media.css" in html:
        return html
    if "../shared/vitrine-images.css" in html:
        return html.replace(
            '<link rel="stylesheet" href="../shared/vitrine-images.css">',
            '<link rel="stylesheet" href="../shared/vitrine-images.css">\n' + MEDIA.strip(),
            1,
        )
    if "</head>" in html and "vitrine-images.css" not in html:
        return html.replace("</head>", MEDIA + "</head>", 1)
    return html


def add_fonts(html, link):
    if link.strip() in html:
        return html
    return html.replace("</head>", link + "</head>", 1)


def insert_after_accueil(html, block):
    if block.strip()[:60] in html:
        return html
    i = html.find('id="accueil"')
    j = html.find("</section>", i) + len("</section>")
    return html[:j] + block + html[j:]


def replace_between(html, start_marker, end_marker, new_block):
  if start_marker not in html:
    raise ValueError(f"start not found: {start_marker[:40]}")
  s = html.index(start_marker)
  e = html.index(end_marker, s) + len(end_marker)
  return html[:s] + new_block + html[e:]


CONFIG = {
    "technologie": {
        "fonts": '  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">\n',
        "start": '      <motion> NO',
        "end": '      </div>\n    </section>\n    <section class="section vitrine-cta-banner',
        "hero": lambda: (
            '      <div class="hero-body">\n        <div class="container">\n'
            '          <div class="columns is-vcentered is-variable is-8">\n'
            '            <div class="column is-6">\n'
            '              <p class="tech-eyebrow has-text-tech-accent mb-3">Metz · Grand Est · cloud souverain</p>\n'
            '              <p class="title is-1 has-text-white"><span class="icon-text"><span class="icon has-text-tech-accent">'
            '<i class="fa-solid fa-cloud-arrow-up" aria-hidden="true"></i></span>'
            '<span>Produits numériques &amp; cloud régional</span></span></p>\n'
            '              <p class="subtitle is-4 has-text-grey-lighter">Synapse Lorraine conçoit des outils métiers pour PME '
            "et collectivités&nbsp;: API documentées, tableaux de bord et automatisation des flux.</p>\n"
            '              <p class="subtitle is-6 has-text-grey mt-4">Livraisons incrémentales, ateliers de cadrage et '
            "documentation vivante — hébergement UE.</p>\n"
            '              <div class="buttons mt-5">\n'
            '                <a class="button is-link is-medium has-text-weight-semibold" href="#solutions">'
            '<span class="icon"><i class="fa-solid fa-arrow-right" aria-hidden="true"></i></span>'
            "<span>Voir les solutions</span></a>\n"
            '                <a class="button is-white is-outlined is-medium" href="#demo">'
            '<span class="icon"><i class="fa-regular fa-calendar" aria-hidden="true"></i></span>'
            "<span>Planifier une démo</span></a>\n"
            "              </div>\n            </div>\n"
            + fig("tech-visuels", "tech-datacenter.png", "hero.svg", "Salle serveurs et cloud régional", "Datacenter — illustration")
            + "          </div>\n        </div>\n      </div>\n    </section>\n    <section class=\"section vitrine-cta-banner"
        ),
        "stats": stats(
            "tech-stats-band has-background-dark",
            [("120+", "clients actifs"), ("99,9 %", "SLA plateforme"), ("48 h", "délai audit"), ("UE", "données hébergées")],
        ),
    },
}

print("incomplete config")
