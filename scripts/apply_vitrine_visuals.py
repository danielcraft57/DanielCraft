#!/usr/bin/env python3
"""Apply image + animation markup to architecture, fitness, photographie demos."""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"
TAG = "m" + "o" + "t" + "i" + "o" + "n"  # erroneous tag to fix if present

HEAD = """
  <link rel="stylesheet" href="../shared/vitrine-images.css">
  <link rel="stylesheet" href="../shared/vitrine-media.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glightbox@3.2.0/dist/css/glightbox.min.css" crossorigin="anonymous">"""

FOOT = """
  <script src="https://cdn.jsdelivr.net/npm/glightbox@3.2.0/dist/js/glightbox.min.js" crossorigin="anonymous"></script>
  <script src="../shared/vitrine-images.js"></script>"""


def inject_common(html: str) -> str:
    if "vitrine-images.css" not in html:
        html = html.replace(
            '  <link rel="stylesheet" href="styles.css">',
            HEAD + '\n  <link rel="stylesheet" href="styles.css">',
            1,
        )
    if "vitrine-images.js" not in html:
        html = html.replace("</body>", FOOT + "\n</body>", 1)
    return html


def fix_tags(html: str) -> str:
    return html.replace("<" + TAG, "<div").replace("</" + TAG + ">", "</motion>").replace("</motion>", "</div>")


def project_article(img: str, loc: str, title: str, status: str) -> str:
    return f"""        <article class="arch-project vitrine-img-reveal">
          <figure class="vitrine-figure vitrine-figure--motion mb-3" style="margin:-2rem -2rem 1rem -2rem">
            <a href="images/{img}" class="glightbox" data-gallery="arch-visuels" data-glightbox="title: {title}">
              <img src="images/{img}" width="720" height="480" alt="Illustration projet {title}" loading="lazy" decoding="async">
            </a>
          </figure>
          <p class="arch-mono">{loc}</p>
          <h3 style="font-size:1.5rem;margin:0.5rem 0">{title}</h3>
          <p class="arch-accent arch-mono">{status}</p>
        </article>"""


# --- architecture ---
arch = inject_common((BASE / "architecture" / "index.html").read_text(encoding="utf-8"))
arch = re.sub(
    r'<section id="accueil" class="arch-hero container">.*?</section>',
    """    <section id="accueil" class="arch-hero container">
      <div style="display:grid;gap:2rem;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));align-items:end">
        <div>
          <p class="arch-mono arch-accent mb-3">Architecture · Urbanisme · Metz</p>
          <h1>Bâtir<br>avec<br>mesure</h1>
          <p style="max-width:32rem;margin-top:2rem;font-size:1.15rem;line-height:1.6">
            Atelier Nord-Est — illustrations vectorielles façon plan, animations Ken Burns et lightbox.
          </p>
          <p style="margin-top:1.5rem">
            <a href="#projets" role="button" class="outline">Voir les réalisations</a>
            <a href="#contact" role="button" style="margin-left:0.5rem">Échanger sur un projet</a>
          </p>
        </motion>
        <div class="vitrine-img-reveal">
          <figure class="vitrine-figure vitrine-figure--ken vitrine-figure--motion mb-0">
            <a href="images/hero.svg" class="glightbox" data-gallery="arch-visuels" data-glightbox="title: Façade contemporaine">
              <img src="images/hero.svg" width="1200" height="560" alt="Dessin architectural façade contemporaine" decoding="async" fetchpriority="high">
            </a>
          </figure>
        </div>
      </div>
    </section>""",
    arch,
    count=1,
    flags=re.DOTALL,
)
grid = "\n".join([
    project_article("projet-metz.svg", "Résidentiel · Metz Queuleu", "24 logements passifs", "Livré 2025"),
    project_article("projet-lux.svg", "Tertiaire · Luxembourg", "Siège social 3 200 m²", "En cours"),
    project_article("projet-verdun.svg", "Patrimoine · Verdun", "Réhabilitation caserne", "Concours 2024"),
    project_article("projet-metz.svg", "Équipements · Thionville", "Médiathèque intercommunale", "Étude APS"),
])
arch = re.sub(
    r'<section id="projets" class="container" style="padding:4rem 0">.*?</section>',
    f"""    <section id="projets" class="container" style="padding:4rem 0">
      <h2 class="arch-mono" style="margin-bottom:2rem">Sélection 2024–2026</h2>
      <div class="arch-grid-projects">
{grid}
      </div>
    </section>""",
    arch,
    count=1,
    flags=re.DOTALL,
)
(BASE / "architecture" / "index.html").write_text(fix_tags(arch), encoding="utf-8")
print("architecture ok")

# --- fitness ---
fit = inject_common((BASE / "fitness" / "index.html").read_text(encoding="utf-8"))
fit = fit.replace(
    """          <div class="lg:w-1/2">
            <motion class="aspect-video rounded-box bg-gradient-to-br from-lime-900/40 to-base-300 flex items-center justify-center border border-neon/20">
              <p class="fit-display text-6xl text-neon/80">24/7</p>
            </motion>
          </motion>""".replace("<motion", "<div"),
    """          <div class="lg:w-1/2 vitrine-img-reveal">
            <figure class="vitrine-figure vitrine-figure--ken vitrine-figure--motion mb-0 rounded-box overflow-hidden border border-neon/20">
              <a href="images/hero.svg" class="glightbox" data-gallery="fit-visuels" data-glightbox="title: Salle Pulse Fitness">
                <img src="images/hero.svg" width="1200" height="520" alt="Illustration salle de sport" decoding="async" fetchpriority="high" class="w-full">
              </a>
            </figure>
          </div>""",
)
def fit_card(img: str, alt: str, icon: str, title: str, schedule: str) -> str:
    return f"""        <article class="card fit-card-plan vitrine-img-reveal overflow-hidden">
          <figure class="vitrine-figure vitrine-figure--motion mb-0">
            <a href="images/{img}" class="glightbox" data-gallery="fit-visuels"><img src="images/{img}" width="640" height="400" alt="{alt}" loading="lazy"></a>
          </figure>
          <div class="card-body">
            <p class="text-neon"><i class="fa-solid {icon}" aria-hidden="true"></i></p>
            <h3 class="card-title">{title}</h3>
            <p class="text-sm text-gray-400">{schedule}</p>
          </div>
        </article>"""

fit = re.sub(
    r'<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">.*?</motion>\s*</section>',
    "<div class=\"grid sm:grid-cols-2 lg:grid-cols-4 gap-4\">\n"
    + fit_card("cours-hiit.svg", "Cours HIIT", "fa-fire", "HIIT Burn", "Lun · Mer · 19h — 45 min")
    + "\n"
    + fit_card("cours-hiit.svg", "Cross training", "fa-person-running", "Cross Training", "Mar · Jeu · 18h30")
    + "\n"
    + fit_card("cours-yoga.svg", "Yoga", "fa-spa", "Yoga Flow", "Dim · 10h — récup")
    + "\n"
    + fit_card("cours-cycling.svg", "Cycling", "fa-bicycle", "Cycling", "Ven · 20h — salle dédiée")
    + "\n      </div>\n    </section>",
    fit,
    count=1,
    flags=re.DOTALL,
)
(BASE / "fitness" / "index.html").write_text(fix_tags(fit), encoding="utf-8")
print("fitness ok")

# --- photographie ---
ph = inject_common((BASE / "photographie" / "index.html").read_text(encoding="utf-8"))
tiles = [
    ("portfolio-mariage.svg", "photo-tile photo-tile--wide", "Mariage · Château de Malbrouck"),
    ("portfolio-portrait.svg", "photo-tile", "Portrait · série Silences"),
    ("portfolio-corporate.svg", "photo-tile", "Corporate · Synapse Lorraine"),
    ("portfolio-reportage.svg", "photo-tile", "Reportage · ESS Metz"),
    ("portfolio-architecture.svg", "photo-tile photo-tile--wide", "Architecture · Atelier Nord-Est"),
    ("portfolio-mode.svg", "photo-tile", "Mode · lookbook automne"),
]
masonry = ['    <section id="portfolio" class="photo-masonry" aria-label="Portfolio">']
for img, cls, cap in tiles:
    masonry.append(f"""      <article class="{cls} vitrine-img-reveal">
        <figure class="vitrine-figure vitrine-figure--motion mb-0 h-full">
          <a href="images/{img}" class="glightbox" data-gallery="photo-visuels" data-glightbox="title: {cap}">
            <img src="images/{img}" alt="Illustration {cap}" loading="lazy" decoding="async" style="width:100%;height:100%;object-fit:cover;min-height:200px">
          </a>
        </figure>
      </article>""")
masonry.append("    </section>")
ph = re.sub(
    r'<section id="portfolio" class="photo-masonry" aria-label="Portfolio">.*?</section>',
    "\n".join(masonry),
    ph,
    count=1,
    flags=re.DOTALL,
)
ph = ph.replace(
    """      <div>
        <p style="font-size:var(--font-size-2);max-width:28ch;color:var(--sand-11)">
          Maquette portfolio sans framework UI lourd&nbsp;: <strong>Open Props</strong> pour les tokens, grille masonry CSS et typo Instrument Serif pour un rendu galerie d'art / photographe indépendant.
        </p>""",
    """      <div>
        <figure class="vitrine-figure vitrine-figure--ken vitrine-figure--motion mb-4 vitrine-img-reveal">
          <a href="images/hero.svg" class="glightbox" data-gallery="photo-visuels"><img src="images/hero.svg" width="1000" height="700" alt="Illustration studio photo" loading="lazy" style="width:100%;border-radius:4px"></a>
        </figure>
        <p style="font-size:var(--font-size-2);max-width:28ch;color:var(--sand-11)">
          Galerie illustrée — masonry animée, lightbox GLightbox et reveal au scroll.
        </p>""",
)
(BASE / "photographie" / "index.html").write_text(fix_tags(ph), encoding="utf-8")
print("photographie ok")
