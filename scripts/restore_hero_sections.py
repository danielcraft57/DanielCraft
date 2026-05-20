#!/usr/bin/env python3
"""Inject hero + stats blocks into vitrine demo index.html files."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "assets" / "vitrines" / "demos"
MC = "vitrine-figure--" + "motion"
BAD = "<" + "motion" + "> NO"


def fig_tail(g, png, svg, alt, title):
    return [
        '            <div class="column is-6 vitrine-img-reveal">',
        f'              <figure class="vitrine-figure vitrine-hero-visual vitrine-figure--ken {MC} mb-0">',
        f'                <a href="images/{svg}" class="glightbox" data-gallery="{g}" data-glightbox="title: {title}">',
        f'                  <img src="images/{png}" width="1200" height="675" alt="{alt}" decoding="async" fetchpriority="high">',
        "                </a>",
        "              </figure>",
        "            </div>",
        "          </div>",
        "        </div>",
        "      </motion> NO",
        "    </motion> NO",
    ]


def fix_tail(lines):
    out = []
    for line in lines:
        if line.strip() in ("</motion> NO", "<motion> NO"):
            continue
        out.append(line.replace("</motion> NO", "</div>").replace("<motion> NO", ""))
    # fix last two closes: hero-body and section
    text = "\n".join(out)
    text = text.replace("      </div>\n    </div>", "      </div>\n    </section>", 1)
    if text.endswith("    </div>"):
        text = text[:-10] + "    </section>"
    return text


def stats_block(css, rows):
    cols = "\n".join(
        f'          <div class="column"><p class="title is-2 has-text-white mb-1">{a}</p>'
        f'<p class="subtitle is-6 has-text-white-ter">{b}</p></div>'
        for a, b in rows
    )
    return f"""
    <section class="section {css} py-5" aria-label="Chiffres clés">
      <div class="container">
        <div class="columns has-text-centered mb-0">
{cols}
        </div>
      </div>
    </section>
"""


def patch_slug(slug, accueil_lines, stats_css, stats_rows, broken_marker):
    path = ROOT / slug / "index.html"
    html = path.read_text(encoding="utf-8")
    if BAD in html:
        html = html.replace(BAD, "")
    hero = "\n".join(accueil_lines) + "\n" + fix_tail(fig_tail(*broken_marker[4:]))
    # broken_marker unused - pass fig args separately

    stats = stats_block(stats_css, stats_rows)
    pattern = rf'    <section id="accueil"[^>]*>.*?(?=    <section class="section vitrine-cta-banner)'
    if not re.search(pattern, html, re.DOTALL):
        pattern = rf'    <section id="accueil"[^>]*>.*?(?=    <section )'
    new_html, n = re.subn(pattern, hero + stats + "\n", html, count=1, flags=re.DOTALL)
    if n == 0:
        raise SystemExit(f"{slug}: accueil section not patched")
    path.write_text(new_html, encoding="utf-8")
    print(f"OK {slug}")


def resto():
    left = [
        '    <section id="accueil" class="hero is-medium resto-hero">',
        '      <div class="hero-body">',
        '        <div class="container">',
        '          <div class="columns is-vcentered is-variable is-8">',
        '            <div class="column is-6">',
        '              <p class="resto-eyebrow has-text-resto-gold mb-3">Metz · place Saint-Jacques · depuis 1987</p>',
        '              <p class="title is-1 has-text-white"><i class="fa-solid fa-wheat-awn mr-3 has-text-resto-gold" aria-hidden="true"></i>Cuisine de saison · terrasse</p>',
        '              <p class="subtitle is-4 has-text-white-ter">La Brasserie Saint-Jacques propose une cuisine de marché au cœur de Metz.</p>',
        '              <p class="subtitle is-6 has-text-white-ter mt-4">Produits lorrain, accords mets-vins et terrasse ombragée.</p>',
        '              <div class="buttons mt-5">',
        '                <a class="button is-warning is-medium hvr-shrink" href="#carte"><span class="icon"><i class="fa-solid fa-utensils" aria-hidden="true"></i></span><span>La carte</span></a>',
        '                <a class="button is-white is-outlined is-medium hvr-shrink" href="#reservation"><span class="icon"><i class="fa-solid fa-pen-to-square" aria-hidden="true"></i></span><span>Réserver</span></a>',
        "              </div>",
        "            </div>",
    ]
    tail = [
        '            <div class="column is-6 vitrine-img-reveal">',
        f'              <figure class="vitrine-figure vitrine-hero-visual vitrine-figure--ken {MC} mb-0">',
        '                <a href="images/hero.svg" class="glightbox" data-gallery="resto-visuels" data-glightbox="title: Brasserie — illustration">',
        '                  <img src="images/resto-salle.png" width="1200" height="675" alt="Salle de la brasserie" decoding="async" fetchpriority="high">',
        "                </a>",
        "              </figure>",
        "            </div>",
        "          </div>",
        "        </div>",
        "      </div>",
        "    </section>",
    ]
    hero = "\n".join(left + tail)
    stats = stats_block(
        "resto-stats-band",
        [("42", "couverts"), ("12", "vins au verre"), ("4,8", "note Google"), ("7j/7", "midi & soir")],
    )
    path = ROOT / "restauration" / "index.html"
    html = path.read_text(encoding="utf-8")
    html = html.replace(BAD, "")
    pat = r'    <section id="accueil"[^>]*>.*?(?=    <section class="section vitrine-cta-banner)'
    html, n = re.subn(pat, hero + stats + "\n", html, count=1, flags=re.DOTALL)
    if n == 0:
        raise SystemExit("restauration failed")
    path.write_text(html, encoding="utf-8")
    print("OK restauration")


def inject(slug, hero, stats_css, stats_rows, next_pat):
    path = ROOT / slug / "index.html"
    html = path.read_text(encoding="utf-8")
    html = html.replace(BAD, "")
    if "../shared/vitrine-media.css" not in html and "../shared/vitrine-images.css" in html:
        html = html.replace(
            '<link rel="stylesheet" href="../shared/vitrine-images.css">',
            '<link rel="stylesheet" href="../shared/vitrine-images.css">\n'
            '  <link rel="stylesheet" href="../shared/vitrine-media.css">',
            1,
        )
    stats = stats_block(stats_css, stats_rows)
    html, n = re.subn(
        rf"    <section id=\"accueil\"[^>]*>.*?(?={next_pat})",
        hero + stats + "\n",
        html,
        count=1,
        flags=re.DOTALL,
    )
    if n == 0:
        raise SystemExit(f"{slug}: patch failed")
    path.write_text(html, encoding="utf-8")
    print(f"OK {slug}")


def col_fig(g, png, svg, alt, title):
    return [
        '            <div class="column is-6 vitrine-img-reveal">',
        f'              <figure class="vitrine-figure vitrine-hero-visual vitrine-figure--ken {MC} mb-0">',
        f'                <a href="images/{svg}" class="glightbox" data-gallery="{g}" data-glightbox="title: {title}">',
        f'                  <img src="images/{png}" width="1200" height="675" alt="{alt}" decoding="async" fetchpriority="high">',
        "                </a>",
        "              </figure>",
        "            </div>",
    ]


def col_fig_ok(g, png, svg, alt, title):
    return [
        '            <div class="column is-6 vitrine-img-reveal">',
        f'              <figure class="vitrine-figure vitrine-hero-visual vitrine-figure--ken {MC} mb-0">',
        f'                <a href="images/{svg}" class="glightbox" data-gallery="{g}" data-glightbox="title: {title}">',
        f'                  <img src="images/{png}" width="1200" height="675" alt="{alt}" decoding="async" fetchpriority="high">',
        "                </a>",
        "              </figure>",
        "            </div>",
        "          </div>",
        "        </div>",
        "      </div>",
        "    </section>",
    ]


def beaute():
    left = [
        '    <section id="accueil" class="hero is-medium beaute-hero vitrine-hero-animate is-vitrine-prejs">',
        '      <div class="hero-body">',
        '        <div class="container">',
        '          <div class="columns is-vcentered is-variable is-8">',
        '            <div class="column is-6">',
        '              <p class="beaute-eyebrow has-text-beaute-rose mb-3">Metz centre · institut &amp; spa</p>',
        '              <p class="title is-1 has-text-white"><i class="fa-solid fa-wand-magic-sparkles mr-3 has-text-beaute-rose" aria-hidden="true"></i>Soins visage · corps · spa</p>',
        '              <p class="subtitle is-4 has-text-white-ter">Spa Thalie — équipes diplômées, cabines doubles et rituels bien-être sur rendez-vous.</p>',
        '              <p class="subtitle is-6 has-text-white-ter mt-4">Produits partenaires, ambiance feutrée et politique d’annulation 24&nbsp;h.</p>',
        '              <div class="buttons mt-5">',
        '                <a class="button is-warning is-medium" href="#soins"><span class="icon"><i class="fa-solid fa-list" aria-hidden="true"></i></span><span>Carte des soins</span></a>',
        '                <a class="button is-white is-outlined is-medium" href="#rdv"><span class="icon"><i class="fa-solid fa-calendar-plus" aria-hidden="true"></i></span><span>Prendre RDV</span></a>',
        "              </div>",
        "            </div>",
    ]
    hero = "\n".join(left + col_fig_ok("beaute-visuels", "beaute-spa.png", "hero.svg", "Cabine spa Thalie", "Spa — illustration"))
    inject(
        "beaute",
        hero,
        "beaute-stats-band",
        [("4", "cabines"), ("18", "ans d’expérience"), ("68 €", "soin dès"), ("4,9", "avis clients")],
        r'    <section class="section vitrine-cta-banner vitrine-cta-shimmer',
    )


def association():
    left = [
        '    <section id="accueil" class="hero is-success is-medium assoc-hero">',
        '      <div class="hero-body">',
        '        <div class="container">',
        '          <div class="columns is-vcentered is-variable is-8">',
        '            <div class="column is-6">',
        '              <p class="assoc-eyebrow has-text-warning mb-3">Metz Métropole · solidarité locale</p>',
        '              <p class="title is-1 has-text-white">Solidarité de proximité</p>',
        '              <p class="subtitle is-4 has-text-white-ter">Maraude, jeunesse et cuisines solidaires au service des quartiers de Metz.</p>',
        '              <p class="subtitle is-6 has-text-white-ter mt-4">Rejoignez nos équipes de bénévoles ou soutenez nos actions sur le terrain.</p>',
        '              <div class="buttons mt-5">',
        '                <a class="button is-warning is-medium has-text-weight-semibold" href="#actions">Découvrir nos actions</a>',
        '                <a class="button is-white is-outlined is-medium" href="#contact">Nous écrire</a>',
        "              </div>",
        "            </div>",
    ]
    hero = "\n".join(
        left
        + col_fig_ok(
            "assoc-visuels",
            "mission-benevoles.png",
            "hero.svg",
            "Bénévoles Solidarités Metz",
            "Association — illustration",
        )
    )
    inject(
        "association",
        hero,
        "assoc-stats-band",
        [("320", "bénévoles"), ("12", "actions / an"), ("4 800", "repas / an"), ("57", "communes")],
        r'    <section class="section vitrine-cta-banner vitrine-cta-aurora',
    )


def industrie():
    left = [
        '    <section id="accueil" class="hero is-dark is-medium industrie-hero vitrine-hero-glowspot vitrine-hero-scans">',
        '      <div class="hero-body">',
        '        <div class="container">',
        '          <div class="columns is-vcentered is-variable is-8">',
        '            <div class="column is-6">',
        '              <p class="ind-eyebrow has-text-warning mb-3">Saint-Avold · usinage de précision</p>',
        '              <p class="title is-1 has-text-warning">Usinage &amp; assemblage</p>',
        '              <p class="subtitle is-4 has-text-grey-lighter">Pièces unitaires et petites séries — prototypage express et contrôle qualité intégré.</p>',
        '              <p class="subtitle is-6 has-text-grey mt-4">De l’étude à la série, accompagnement technique et délais maîtrisés.</p>',
        '              <div class="buttons mt-5">',
        '                <a class="button is-warning is-medium" href="#prestations">Voir les prestations</a>',
        '                <a class="button is-light is-outlined is-medium" href="#contact">Demander une étude</a>',
        "              </div>",
        "            </div>",
    ]
    hero = "\n".join(
        left
        + col_fig_ok(
            "ind-visuels",
            "ligne-production.png",
            "hero.svg",
            "Ligne de production Mécano-Precision",
            "Usine — illustration",
        )
    )
    inject(
        "industrie",
        hero,
        "ind-stats-band",
        [("ISO*", "certifications procédé"), ("24 h", "faisabilité"), ("±2 µm", "tolérance cible"), ("48 h", "prototype express")],
        r"    <section class=\"section vitrine-cta-banner has-background-warning",
    )


if __name__ == "__main__":
    resto()
    beaute()
    association()
    industrie()
