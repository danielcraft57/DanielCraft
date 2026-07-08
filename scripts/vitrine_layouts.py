"""Layouts vitrine alternatifs (split, bento, entonnoir) — inspirés bonnes pratiques landing UX."""
from __future__ import annotations

from vitrine_ai_lib import esc
from vitrine_site_blocks import vt_picture


def block_hero_split(
    h1: str,
    lead: str,
    img: str,
    alt: str,
    *,
    eyebrow: str,
    primary_href: str,
    primary_label: str,
    secondary_href: str = "",
    secondary_label: str = "",
) -> str:
    sec_btn = ""
    if secondary_href and secondary_label:
        sec_btn = f'<a class="btn btn-vt-outline rounded-pill px-4" href="{esc(secondary_href)}">{esc(secondary_label)}</a>'
    return f"""<section class="vt-hero-split">
  <div class="container-fluid px-0">
    <div class="row g-0 align-items-stretch min-vh-50">
      <div class="col-lg-5 d-flex align-items-center vt-hero-split-copy">
        <div class="p-4 p-lg-5">
          <p class="vt-eyebrow text-uppercase mb-2">{esc(eyebrow)}</p>
          <h1 class="vt-display display-5 mb-3">{esc(h1)}</h1>
          <p class="lead mb-4">{esc(lead)}</p>
          <div class="d-flex flex-wrap gap-3">
            <a class="btn btn-vt-primary btn-lg rounded-pill px-4" href="{esc(primary_href)}">{esc(primary_label)}</a>
            {sec_btn}
          </div>
        </div>
      </div>
      <div class="col-lg-7 vt-hero-split-media">
        {vt_picture(img, alt, css_class="w-100 h-100 vt-cover", loading=None, fetchpriority="high")}
      </div>
    </div>
  </div>
</section>"""


def block_trust_strip(items: list[tuple[str, str]]) -> str:
    cells = "".join(
        f"""<div class="col-6 col-md-3">
        <div class="vt-trust-cell">
          <strong>{esc(val)}</strong>
          <span>{esc(lbl)}</span>
        </div>
      </div>"""
        for val, lbl in items
    )
    return f"""<section class="vt-trust-strip py-4" aria-label="Preuves de confiance">
  <div class="container">
    <div class="row g-3 text-center">{cells}</div>
  </div>
</section>"""


def block_funnel_steps(title: str, steps: list[tuple[str, str]]) -> str:
    items = ""
    for i, (t, d) in enumerate(steps, 1):
        items += f"""<li class="vt-funnel-step">
        <span class="vt-funnel-num">{i}</span>
        <div>
          <strong>{esc(t)}</strong>
          <p class="mb-0 small text-secondary">{esc(d)}</p>
        </div>
      </li>"""
    return f"""<section class="vt-funnel py-5">
  <div class="container">
    <h2 class="vt-section-title text-center mb-4">{esc(title)}</h2>
    <ol class="vt-funnel-list list-unstyled mx-auto mb-0">{items}</ol>
  </div>
</section>"""


def block_bento_cards(cards: list[dict]) -> str:
    """cards: title, text, img, alt, size='lg'|'sm'"""
    items = ""
    for c in cards:
        size = c.get("size", "sm")
        col = "col-lg-8" if size == "lg" else "col-lg-4"
        items += f"""<div class="{col} col-md-6">
        <article class="vt-bento-card h-100">
          <figure class="vt-bento-img mb-0">{vt_picture(c["img"], c.get("alt", c["title"]), css_class="w-100 vt-cover")}</figure>
          <div class="vt-bento-body">
            <h3 class="h5">{esc(c["title"])}</h3>
            <p class="small text-secondary mb-0">{esc(c["text"])}</p>
          </div>
        </article>
      </div>"""
    return f"""<section class="vt-bento py-5">
  <div class="container">
    <div class="row g-3">{items}</div>
  </div>
</section>"""


def block_compact_features(items: list[dict]) -> str:
    """Liste numérotée + vignette — faible effort cognitif."""
    rows = ""
    for i, it in enumerate(items, 1):
        rows += f"""<article class="vt-compact-row row g-3 align-items-center py-4 border-bottom">
      <div class="col-auto"><span class="vt-compact-num">{i:02d}</span></div>
      <div class="col-md-4 col-lg-3">
        <figure class="mb-0 rounded-3 overflow-hidden">{vt_picture(it["img"], it.get("alt", it["title"]), css_class="w-100 vt-thumb")}</figure>
      </div>
      <div class="col">
        <h3 class="h5 mb-1">{esc(it["title"])}</h3>
        <p class="text-secondary mb-0 small">{esc(it["text"])}</p>
      </div>
    </article>"""
    return f"""<section class="vt-compact py-3">
  <div class="container">{rows}</div>
</section>"""


def block_hero_overlay(
    h1: str,
    lead: str,
    img: str,
    alt: str,
    *,
    eyebrow: str,
    primary_href: str,
    primary_label: str,
    secondary_href: str = "",
    secondary_label: str = "",
) -> str:
    """Hero pleine largeur — image de fond + overlay (garage / industriel)."""
    sec_btn = ""
    if secondary_href and secondary_label:
        sec_btn = f'<a class="btn btn-vt-outline btn-lg rounded-0 px-4" href="{esc(secondary_href)}">{esc(secondary_label)}</a>'
    return f"""<section class="vt-hero-overlay position-relative vt-reveal-fade">
  <div class="vt-hero-overlay-bg vt-ken-burns">{vt_picture(img, alt, css_class="w-100 h-100 vt-cover", loading=None, fetchpriority="high")}</div>
  <div class="vt-hero-overlay-shade"></div>
  <div class="container position-relative vt-hero-overlay-copy py-5 py-lg-6">
    <div class="col-lg-7 col-xl-6">
      <p class="vt-eyebrow text-uppercase mb-2">{esc(eyebrow)}</p>
      <h1 class="vt-display display-4 mb-3">{esc(h1)}</h1>
      <p class="lead mb-4">{esc(lead)}</p>
      <div class="d-flex flex-wrap gap-3">
        <a class="btn btn-vt-primary btn-lg rounded-0 px-4" href="{esc(primary_href)}">{esc(primary_label)}</a>
        {sec_btn}
      </div>
    </div>
  </div>
</section>"""


def block_hero_split_reverse(
    h1: str,
    lead: str,
    img: str,
    alt: str,
    *,
    eyebrow: str,
    primary_href: str,
    primary_label: str,
    secondary_href: str = "",
    secondary_label: str = "",
) -> str:
    """Split inversé : visuel à gauche, texte à droite."""
    sec_btn = ""
    if secondary_href and secondary_label:
        sec_btn = f'<a class="btn btn-vt-outline rounded-0 px-4" href="{esc(secondary_href)}">{esc(secondary_label)}</a>'
    return f"""<section class="vt-hero-split vt-hero-split-reverse">
  <div class="container-fluid px-0">
    <div class="row g-0 align-items-stretch min-vh-50">
      <div class="col-lg-7 order-lg-1 vt-hero-split-media">
        {vt_picture(img, alt, css_class="w-100 h-100 vt-cover", loading=None, fetchpriority="high")}
      </div>
      <div class="col-lg-5 order-lg-2 d-flex align-items-center vt-hero-split-copy">
        <div class="p-4 p-lg-5">
          <p class="vt-eyebrow text-uppercase mb-2">{esc(eyebrow)}</p>
          <h1 class="vt-display display-5 mb-3">{esc(h1)}</h1>
          <p class="lead mb-4">{esc(lead)}</p>
          <div class="d-flex flex-wrap gap-3">
            <a class="btn btn-vt-primary btn-lg rounded-0 px-4" href="{esc(primary_href)}">{esc(primary_label)}</a>
            {sec_btn}
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""


def block_service_tiles(title: str, tiles: list[dict]) -> str:
    """Grille 3 services — une tuile peut être mise en avant (hot)."""
    items = ""
    for t in tiles:
        hot = " vt-svc-tile-hot" if t.get("hot") else ""
        items += f"""<div class="col-md-4">
        <article class="vt-svc-tile h-100{hot}">
          <h3 class="h5 text-uppercase">{esc(t["title"])}</h3>
          <ul class="small mb-0 ps-3">{"".join(f"<li>{esc(x)}</li>" for x in t.get("items", []))}</ul>
        </article>
      </div>"""
    return f"""<section class="vt-svc-tiles py-5">
  <div class="container">
    <h2 class="vt-section-title text-uppercase mb-4">{esc(title)}</h2>
    <div class="row g-3">{items}</div>
  </div>
</section>"""


def block_hero_editorial(
    h1: str,
    lead: str,
    img: str,
    alt: str,
    *,
    eyebrow: str,
    primary_href: str,
    primary_label: str,
    secondary_href: str = "",
    secondary_label: str = "",
) -> str:
    """Retail éditorial : texte + visuel encadré (layout frais / marché)."""
    sec_btn = ""
    if secondary_href and secondary_label:
        sec_btn = f'<a class="btn btn-vt-outline rounded-pill px-4" href="{esc(secondary_href)}">{esc(secondary_label)}</a>'
    return f"""<section class="vt-hero-editorial py-5 py-lg-6">
  <div class="container">
    <div class="row align-items-center g-4 g-lg-5">
      <div class="col-lg-6">
        <p class="vt-eyebrow text-uppercase mb-2">{esc(eyebrow)}</p>
        <h1 class="vt-display display-5 mb-3">{esc(h1)}</h1>
        <p class="lead mb-4">{esc(lead)}</p>
        <div class="d-flex flex-wrap gap-3">
          <a class="btn btn-vt-primary btn-lg rounded-pill px-4" href="{esc(primary_href)}">{esc(primary_label)}</a>
          {sec_btn}
        </div>
      </div>
      <div class="col-lg-6">
        <figure class="vt-hero-frame mb-0 rounded-4 overflow-hidden shadow-lg">
          {vt_picture(img, alt, css_class="w-100", loading=None, fetchpriority="high")}
        </figure>
      </div>
    </div>
  </div>
</section>"""


def block_promo_cards(cards: list[dict]) -> str:
    """Bandeau 3 promos retail — accent coloré par carte."""
    items = ""
    for c in cards:
        accent = c.get("accent", "green")
        items += f"""<div class="col-md-4">
        <article class="vt-promo-card h-100 vt-promo-{esc(accent)}">
          <div class="vt-promo-body">
            <h3 class="h5 mb-2">{esc(c["title"])}</h3>
            <p class="small mb-3">{esc(c["text"])}</p>
            <a class="btn btn-sm btn-vt-primary rounded-pill" href="{esc(c["href"])}">{esc(c["label"])}</a>
          </div>
        </article>
      </div>"""
    return f"""<section class="vt-promo-band py-5">
  <div class="container">
    <div class="row g-3">{items}</div>
  </div>
</section>"""


def block_hero_proof_split(
    h1: str,
    lead: str,
    *,
    eyebrow: str,
    quote: str,
    quote_author: str,
    quote_role: str,
    stats: list[tuple[str, str]],
    primary_href: str,
    primary_label: str,
    secondary_href: str = "",
    secondary_label: str = "",
) -> str:
    """Hero cabinet : témoignage (gauche) + chiffres clés (droite) — tendance consulting 2026."""
    stat_cells = "".join(
        f"""<div class="vt-proof-stat">
        <strong class="vt-proof-stat-val">{esc(val)}</strong>
        <span class="vt-proof-stat-lbl">{esc(lbl)}</span>
      </div>"""
        for val, lbl in stats
    )
    sec_btn = ""
    if secondary_href and secondary_label:
        sec_btn = f'<a class="btn btn-vt-outline rounded-0 px-4" href="{esc(secondary_href)}">{esc(secondary_label)}</a>'
    return f"""<section class="vt-hero-proof py-5 py-lg-6">
  <div class="container">
    <p class="vt-eyebrow text-uppercase mb-2">{esc(eyebrow)}</p>
    <div class="row g-4 g-lg-5 align-items-stretch">
      <div class="col-lg-6">
        <blockquote class="vt-quote-card h-100">
          <p class="vt-quote-text">« {esc(quote)} »</p>
          <footer class="vt-quote-footer">
            <strong>{esc(quote_author)}</strong>
            <span>{esc(quote_role)}</span>
          </footer>
        </blockquote>
      </div>
      <div class="col-lg-6 d-flex flex-column">
        <div class="vt-proof-stats mb-4">{stat_cells}</div>
        <div class="mt-auto">
          <h1 class="vt-display h2 mb-2">{esc(h1)}</h1>
          <p class="mb-4">{esc(lead)}</p>
          <div class="d-flex flex-wrap gap-3">
            <a class="btn btn-vt-primary btn-lg rounded-0 px-4" href="{esc(primary_href)}">{esc(primary_label)}</a>
            {sec_btn}
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""


def block_credentials_strip(items: list[tuple[str, str]]) -> str:
    """Bandeau diplômes / labels — E-E-A-T cabinet comptable."""
    cells = "".join(
        f"""<div class="col-6 col-md-3">
        <div class="vt-cred-cell">
          <strong>{esc(title)}</strong>
          <span>{esc(sub)}</span>
        </div>
      </div>"""
        for title, sub in items
    )
    return f"""<section class="vt-credentials py-4" aria-label="Agréments et certifications">
  <div class="container">
    <div class="row g-3 text-center">{cells}</div>
  </div>
</section>"""


def block_comparison_table(title: str, rows: list[tuple[str, str, str]]) -> str:
    """Tableau avant / après — pattern consulting « situation → résultat »."""
    trs = "".join(
        f"""<tr>
        <th scope="row">{esc(sit)}</th>
        <td class="vt-cmp-before">{esc(before)}</td>
        <td class="vt-cmp-after">{esc(after)}</td>
      </tr>"""
        for sit, before, after in rows
    )
    return f"""<section class="vt-comparison py-5">
  <div class="container">
    <h2 class="vt-section-title text-center mb-4">{esc(title)}</h2>
    <div class="table-responsive">
      <table class="table vt-cmp-table align-middle">
        <thead>
          <tr>
            <th scope="col">Situation</th>
            <th scope="col">Avant</th>
            <th scope="col">Avec Verlaine &amp; Associés</th>
          </tr>
        </thead>
        <tbody>{trs}</tbody>
      </table>
    </div>
  </div>
</section>"""


def block_stat_narrative_rows(items: list[dict]) -> str:
    """Panneaux chiffre + récit alternés — rythme rapport actuariel."""
    rows = ""
    for i, it in enumerate(items):
        flip = "flex-lg-row-reverse" if i % 2 else ""
        rows += f"""<article class="vt-stat-narrative py-5">
      <div class="container">
        <div class="row align-items-center g-4 g-lg-5 {flip}">
          <div class="col-lg-4 text-center text-lg-start">
            <span class="vt-stat-big">{esc(it["stat"])}</span>
            <span class="vt-stat-big-lbl d-block">{esc(it.get("stat_label", ""))}</span>
          </div>
          <div class="col-lg-4">
            <figure class="mb-0 rounded-3 overflow-hidden shadow-sm">
              {vt_picture(it["img"], it.get("alt", it["title"]), css_class="w-100 vt-thumb")}
            </figure>
          </div>
          <div class="col-lg-4">
            <h3 class="h4 vt-section-title">{esc(it["title"])}</h3>
            <p class="text-secondary mb-0">{esc(it["text"])}</p>
          </div>
        </div>
      </div>
    </article>"""
    return f"""<section class="vt-stat-narratives">{rows}</section>"""


def block_faq_accordion(title: str, items: list[tuple[str, str]]) -> str:
    """FAQ accordéon Bootstrap — citations IA / featured snippets."""
    acc_id = "vtFaq"
    cards = ""
    for i, (q, a) in enumerate(items):
        hid = f"{acc_id}-{i}"
        cards += f"""<div class="accordion-item" itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
      <h3 class="accordion-header" id="h-{hid}">
        <button class="accordion-button{' collapsed' if i else ''}" type="button" data-bs-toggle="collapse" data-bs-target="#c-{hid}" aria-expanded="{'true' if i == 0 else 'false'}" aria-controls="c-{hid}">
          <span itemprop="name">{esc(q)}</span>
        </button>
      </h3>
      <div id="c-{hid}" class="accordion-collapse collapse{' show' if i == 0 else ''}" aria-labelledby="h-{hid}" data-bs-parent="#{acc_id}">
        <div class="accordion-body" itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
          <div itemprop="text">{esc(a)}</div>
        </div>
      </div>
    </div>"""
    return f"""<section class="vt-faq py-5" itemscope itemtype="https://schema.org/FAQPage">
  <div class="container">
    <h2 class="vt-section-title text-center mb-4">{esc(title)}</h2>
    <div class="accordion vt-faq-acc mx-auto" id="{acc_id}">{cards}</div>
  </div>
</section>"""


def block_hero_technical(
    h1: str,
    lead: str,
    img: str,
    alt: str,
    *,
    eyebrow: str,
    specs: list[tuple[str, str]],
    primary_href: str,
    primary_label: str,
    secondary_href: str = "",
    secondary_label: str = "",
) -> str:
    """Hero B2B industriel : specs visibles immédiatement + bande visuelle."""
    pills = "".join(
        f'<span class="vt-spec-pill"><strong>{esc(val)}</strong> {esc(lbl)}</span>'
        for val, lbl in specs
    )
    sec_btn = ""
    if secondary_href and secondary_label:
        sec_btn = f'<a class="btn btn-vt-outline btn-sm rounded-0 px-3" href="{esc(secondary_href)}">{esc(secondary_label)}</a>'
    return f"""<section class="vt-hero-tech">
  <div class="container py-5">
    <p class="vt-eyebrow text-uppercase mb-2">{esc(eyebrow)}</p>
    <div class="row g-4 align-items-end">
      <div class="col-lg-7">
        <h1 class="vt-display display-5 mb-3">{esc(h1)}</h1>
        <p class="lead mb-4">{esc(lead)}</p>
        <div class="vt-spec-pills d-flex flex-wrap gap-2 mb-4">{pills}</div>
        <div class="d-flex flex-wrap gap-2">
          <a class="btn btn-vt-primary rounded-0 px-4" href="{esc(primary_href)}">{esc(primary_label)}</a>
          {sec_btn}
        </div>
      </div>
      <div class="col-lg-5">
        <figure class="vt-hero-tech-frame mb-0 rounded-0 overflow-hidden">
          {vt_picture(img, alt, css_class="w-100", loading=None, fetchpriority="high")}
        </figure>
      </div>
    </div>
  </div>
</section>"""


def block_spec_grid(title: str, items: list[dict]) -> str:
    """Grille capacités techniques — cartes specs (tolerance, matériaux…)."""
    cells = ""
    for it in items:
        cells += f"""<div class="col-sm-6 col-lg-3">
        <article class="vt-spec-card h-100">
          <span class="vt-spec-card-label">{esc(it["label"])}</span>
          <strong class="vt-spec-card-val">{esc(it["value"])}</strong>
          <p class="small mb-0">{esc(it.get("detail", ""))}</p>
        </article>
      </div>"""
    return f"""<section class="vt-spec-grid py-5">
  <div class="container">
    <h2 class="vt-section-title text-uppercase mb-4">{esc(title)}</h2>
    <div class="row g-3">{cells}</div>
  </div>
</section>"""


def block_cert_strip(certs: list[tuple[str, str, str]]) -> str:
    """Bandeau certifications ISO / IATF — preuve qualité industrielle."""
    items = ""
    for code, name, detail in certs:
        items += f"""<div class="col-6 col-md-3">
        <div class="vt-cert-badge">
          <span class="vt-cert-code">{esc(code)}</span>
          <strong>{esc(name)}</strong>
          <small>{esc(detail)}</small>
        </div>
      </div>"""
    return f"""<section class="vt-cert-strip py-4" aria-label="Certifications">
  <div class="container">
    <div class="row g-3 text-center">{items}</div>
  </div>
</section>"""


def block_process_flow(title: str, steps: list[tuple[str, str]]) -> str:
    """Flux processus horizontal — parcours usinage / RFQ."""
    items = ""
    for i, (t, d) in enumerate(steps, 1):
        arrow = '<span class="vt-flow-arrow" aria-hidden="true">→</span>' if i < len(steps) else ""
        items += f"""<div class="vt-flow-step">
        <span class="vt-flow-num">{i:02d}</span>
        <div>
          <strong>{esc(t)}</strong>
          <p class="mb-0 small">{esc(d)}</p>
        </div>
        {arrow}
      </div>"""
    return f"""<section class="vt-process-flow py-5">
  <div class="container">
    <h2 class="vt-section-title text-uppercase mb-4">{esc(title)}</h2>
    <div class="vt-flow-track d-flex flex-wrap align-items-start gap-3">{items}</div>
  </div>
</section>"""


def block_specs_table(title: str, rows: list[tuple[str, str]]) -> str:
    """Tableau technique détaillé — tolérances, matériaux, capacités."""
    trs = "".join(
        f"<tr><th scope=\"row\">{esc(k)}</th><td>{esc(v)}</td></tr>"
        for k, v in rows
    )
    return f"""<section class="vt-specs-table py-5">
  <div class="container">
    <h2 class="vt-section-title text-uppercase mb-4">{esc(title)}</h2>
    <div class="table-responsive">
      <table class="table vt-tech-table">
        <tbody>{trs}</tbody>
      </table>
    </div>
  </div>
</section>"""


def block_sector_strip(sectors: list[tuple[str, str]]) -> str:
    """Bandeau secteurs clients — auto, aéro, médical…"""
    items = "".join(
        f"""<div class="col-6 col-md-3">
        <div class="vt-sector-cell">
          <strong>{esc(name)}</strong>
          <span>{esc(desc)}</span>
        </div>
      </div>"""
        for name, desc in sectors
    )
    return f"""<section class="vt-sector-strip py-4">
  <div class="container">
    <div class="row g-3 text-center">{items}</div>
  </div>
</section>"""


def block_hero_property_search(
    h1: str,
    lead: str,
    img: str,
    alt: str,
    *,
    eyebrow: str = "Nancy · Grand Est",
    search_action: str = "biens.html",
) -> str:
    """Hero immobilier split + barre recherche (achat/louer/vendre)."""
    return f"""<section class="vt-hero-property">
  <div class="container-fluid px-0">
    <div class="row g-0 align-items-stretch">
      <div class="col-lg-5 d-flex align-items-center vt-hero-property-copy">
        <div class="p-4 p-lg-5">
          <p class="vt-eyebrow text-uppercase mb-2">{esc(eyebrow)}</p>
          <h1 class="vt-display display-5 mb-3">{esc(h1)}</h1>
          <p class="lead mb-4">{esc(lead)}</p>
          <form class="vt-search-bar row g-2" action="{esc(search_action)}" method="get" role="search">
            <div class="col-sm-4">
              <label class="visually-hidden" for="vt-search-type">Type de projet</label>
              <select class="form-select" id="vt-search-type" name="type">
                <option>Acheter</option><option>Louer</option><option>Vendre</option>
              </select>
            </div>
            <div class="col-sm-5">
              <label class="visually-hidden" for="vt-search-loc">Ville</label>
              <input class="form-control" id="vt-search-loc" name="ville" type="search" placeholder="Nancy, Metz, Thionville…">
            </div>
            <div class="col-sm-3">
              <button class="btn btn-vt-primary w-100" type="submit">Rechercher</button>
            </div>
          </form>
        </div>
      </div>
      <div class="col-lg-7 vt-hero-property-media">
        {vt_picture(img, alt, css_class="w-100 h-100 vt-cover", loading=None, fetchpriority="high")}
      </div>
    </div>
  </div>
</section>"""


def block_listing_grid(title: str, listings: list[dict], *, cta_href: str = "", cta_label: str = "") -> str:
    """Grille annonces immobilières — image, prix, specs."""
    cards = []
    for item in listings:
        badge = ""
        if item.get("badge"):
            badge = f'<span class="vt-listing-badge">{esc(item["badge"])}</span>'
        cards.append(f"""<div class="col-md-6 col-lg-4">
        <article class="card vt-listing-card h-100 border-0 shadow-sm">
          <div class="vt-listing-img-wrap position-relative">
            {vt_picture(item["img"], item.get("alt", item["title"]), css_class="card-img-top vt-listing-img")}
            {badge}
          </div>
          <div class="card-body">
            <p class="vt-listing-price mb-1">{esc(item["price"])}</p>
            <h3 class="h6 vt-listing-title mb-2">{esc(item["title"])}</h3>
            <p class="small text-secondary mb-2">{esc(item.get("specs", ""))}</p>
            <p class="small mb-0">{esc(item.get("text", ""))}</p>
          </div>
        </article>
      </div>""")
    cta = ""
    if cta_href and cta_label:
        cta = f"""<div class="text-center mt-4">
      <a class="btn btn-vt-outline rounded-pill px-4" href="{esc(cta_href)}">{esc(cta_label)}</a>
    </div>"""
    return f"""<section class="vt-listings py-5">
  <div class="container">
    <h2 class="vt-section-title text-center mb-4">{esc(title)}</h2>
    <div class="row g-4">{"".join(cards)}</div>
    {cta}
  </div>
</section>"""


def block_project_grid(title: str, projects: list[dict], *, cta_href: str = "", cta_label: str = "") -> str:
    """Grille projets architecture — année, typologie, surface."""
    cards = []
    for item in projects:
        badge = ""
        if item.get("badge"):
            badge = f'<span class="vt-project-badge">{esc(item["badge"])}</span>'
        cards.append(f"""<div class="col-md-6 col-lg-4">
        <article class="card vt-project-card h-100 border-0">
          <div class="vt-project-img-wrap position-relative">
            {vt_picture(item["img"], item.get("alt", item["title"]), css_class="card-img-top vt-project-img")}
            {badge}
          </div>
          <div class="card-body">
            <p class="vt-project-meta mb-1">{esc(item.get("year", ""))} · {esc(item.get("specs", ""))}</p>
            <h3 class="h6 vt-project-title mb-2">{esc(item["title"])}</h3>
            <p class="small mb-0 text-secondary">{esc(item.get("text", ""))}</p>
          </div>
        </article>
      </div>""")
    cta = ""
    if cta_href and cta_label:
        cta = f"""<div class="text-center mt-4">
      <a class="btn btn-vt-outline rounded-0 px-4" href="{esc(cta_href)}">{esc(cta_label)}</a>
    </div>"""
    return f"""<section class="vt-projects py-5">
  <div class="container">
    <h2 class="vt-section-title mb-4">{esc(title)}</h2>
    <div class="row g-4">{"".join(cards)}</div>
    {cta}
  </div>
</section>"""


def block_impact_goal(title: str, current: str, target: str, percent: int, label: str) -> str:
    """Jauge objectif dons / campagne — associations ESS."""
    return f"""<section class="vt-impact-goal py-4" aria-labelledby="impact-goal-title">
  <div class="container">
    <h2 id="impact-goal-title" class="h6 text-center text-uppercase letter-spacing mb-3">{esc(title)}</h2>
    <div class="vt-impact-bar mx-auto" role="progressbar" aria-valuenow="{percent}" aria-valuemin="0" aria-valuemax="100" aria-label="{esc(label)}">
      <div class="vt-impact-fill" style="width:{percent}%"></div>
      <span class="vt-impact-label">{esc(current)} / {esc(target)}</span>
    </div>
    <p class="text-center small text-secondary mb-0 mt-2">{esc(label)}</p>
  </div>
</section>"""


def block_gallery_masonry(title: str, items: list[dict], *, cta_href: str = "", cta_label: str = "") -> str:
    """Galerie photos décalée — 2e colonne descendue sur desktop (portfolio photo)."""
    cards = []
    for i, item in enumerate(items):
        offset = " vt-masonry-offset" if i % 3 == 1 else ""
        cards.append(f"""<div class="col-md-4{offset}">
        <article class="vt-masonry-card h-100">
          {vt_picture(item["img"], item.get("alt", item["title"]), css_class="vt-masonry-img w-100")}
          <h3 class="h6 vt-masonry-title mt-3 mb-1">{esc(item["title"])}</h3>
          <p class="small text-secondary mb-0">{esc(item.get("text", ""))}</p>
        </article>
      </div>""")
    cta = ""
    if cta_href and cta_label:
        cta = f"""<div class="text-center mt-5">
      <a class="btn btn-vt-outline px-4" href="{esc(cta_href)}">{esc(cta_label)}</a>
    </div>"""
    return f"""<section class="vt-masonry py-5" aria-labelledby="masonry-title">
  <div class="container">
    <h2 id="masonry-title" class="vt-section-title mb-4">{esc(title)}</h2>
    <div class="row g-4">{"".join(cards)}</div>
    {cta}
  </div>
</section>"""


def block_schedule_grid(
    title: str,
    intro: str,
    headers: list[str],
    rows: list[list[str]],
    *,
    quote: str = "",
    quote_author: str = "",
) -> str:
    """Planning hebdo — grille horaire type salle de sport."""
    head_cells = "".join(f'<th scope="col">{esc(h)}</th>' for h in headers)
    body_rows = ""
    for row in rows:
        cells = "".join(f"<td>{esc(cell)}</td>" for cell in row)
        body_rows += f"<tr>{cells}</tr>"
    quote_block = ""
    if quote:
        cite = f" — {esc(quote_author)}" if quote_author else ""
        quote_block = (
            f'<blockquote class="vt-schedule-quote text-center mt-4 mb-0">'
            f'<p class="mb-0">« {esc(quote)} »<cite class="d-block small mt-2 not-italic">{cite}</cite></p>'
            f"</blockquote>"
        )
    return f"""<section class="vt-schedule py-5" aria-labelledby="schedule-title">
  <div class="container">
    <div class="text-center mb-4">
      <h2 id="schedule-title" class="vt-section-title">{esc(title)}</h2>
      <p class="text-secondary mx-auto" style="max-width:42rem">{esc(intro)}</p>
    </div>
    <div class="table-responsive vt-schedule-scroll">
      <table class="table vt-schedule-table mb-0">
        <thead><tr>{head_cells}</tr></thead>
        <tbody>{body_rows}</tbody>
      </table>
    </div>
    {quote_block}
  </div>
</section>"""


def block_neighborhood_strip(title: str, areas: list[tuple[str, str]]) -> str:
    """Quartiers / villes desservies."""
    items = "".join(
        f"""<div class="col-6 col-md-4 col-lg-2">
        <div class="vt-hood-cell text-center">
          <strong>{esc(name)}</strong>
          <span class="d-block small">{esc(count)}</span>
        </div>
      </div>"""
        for name, count in areas
    )
    return f"""<section class="vt-hood-strip py-5 bg-light">
  <div class="container">
    <h2 class="vt-section-title text-center mb-4">{esc(title)}</h2>
    <div class="row g-3">{items}</div>
  </div>
</section>"""


def block_marquee_strip(labels: list[str]) -> str:
    """Bandeau défilant — labels partenaires, distinctions, tags."""
    dup = labels + labels
    items = "".join(f'<span class="vt-marquee-item">{esc(lbl)}</span>' for lbl in dup)
    return f"""<section class="vt-marquee py-3 vt-reveal-fade" aria-hidden="true">
  <div class="vt-marquee-track">{items}</div>
</section>"""


def block_snap_chapters(chapters: list[dict]) -> str:
    """Chapitres plein écran avec scroll-snap — hôtellerie / storytelling."""
    rows = ""
    for i, ch in enumerate(chapters):
        flip = " vt-snap-chapter--flip" if i % 2 else ""
        rows += f"""<article class="vt-snap-chapter{flip}">
      <div class="container py-5">
        <div class="row g-4 align-items-center">
          <div class="col-lg-6">
            <figure class="vt-ken-burns rounded-0 overflow-hidden mb-0 vt-reveal">
              {vt_picture(ch["img"], ch.get("alt", ch["title"]), css_class="w-100")}
            </figure>
          </div>
          <div class="col-lg-6 vt-reveal">
            <h2 class="vt-section-title h3">{esc(ch["title"])}</h2>
            <p class="text-secondary mb-0">{esc(ch["text"])}</p>
          </div>
        </div>
      </div>
    </article>"""
    return f"""<section class="vt-snap-series vt-scroll-snap-y">{rows}</section>"""


def block_motion_progress() -> str:
    """Barre de progression de lecture (fixe en haut)."""
    return '<div class="vt-read-progress" aria-hidden="true"></div>'


def block_hero_saas_product(
    h1: str,
    lead: str,
    img: str,
    alt: str,
    *,
    eyebrow: str,
    primary_href: str,
    primary_label: str,
    secondary_href: str = "",
    secondary_label: str = "",
) -> str:
    """Hero SaaS : orbes animés + mockup flottant."""
    sec_btn = ""
    if secondary_href and secondary_label:
        sec_btn = f'<a class="btn btn-vt-outline btn-lg px-4" href="{esc(secondary_href)}">{esc(secondary_label)}</a>'
    return f"""<section class="vt-hero-saas vt-orbs-field py-5 py-lg-6">
  <div class="vt-orb vt-orb-1" aria-hidden="true"></div>
  <div class="vt-orb vt-orb-2" aria-hidden="true"></div>
  <div class="container position-relative">
    <div class="row align-items-center g-5">
      <div class="col-lg-6 vt-reveal">
        <p class="vt-eyebrow text-uppercase mb-2">{esc(eyebrow)}</p>
        <h1 class="vt-display display-4 mb-3">{esc(h1)}</h1>
        <p class="lead mb-4">{esc(lead)}</p>
        <div class="d-flex flex-wrap gap-2">
          <a class="btn btn-vt-primary btn-lg px-4" href="{esc(primary_href)}">{esc(primary_label)}</a>
          {sec_btn}
        </div>
      </div>
      <div class="col-lg-6 vt-reveal vt-reveal-delay-2">
        <figure class="vt-float-mockup mb-0">
          {vt_picture(img, alt, css_class="w-100", loading=None, fetchpriority="high")}
        </figure>
      </div>
    </div>
  </div>
</section>"""


def block_feature_tabs(title: str, tabs: list[dict]) -> str:
    """Onglets fonctionnalités — panneaux image + texte (animés via vitrine-motion.js)."""
    nav_btns = ""
    panels = ""
    for i, tab in enumerate(tabs):
        tid = f"vt-tab-{i}"
        active = " active" if i == 0 else ""
        nav_btns += f"""<button type="button" class="vt-tab-btn{active}" role="tab" aria-selected="{"true" if i == 0 else "false"}" data-vt-tab-target="{tid}">{esc(tab["label"])}</button>"""
        panels += f"""<div class="vt-tab-panel{active}" id="{tid}" role="tabpanel">
        <div class="row g-4 align-items-center">
          <div class="col-md-6">
            <figure class="mb-0 rounded-3 overflow-hidden vt-ken-burns">
              {vt_picture(tab["img"], tab.get("alt", tab["label"]), css_class="w-100")}
            </figure>
          </div>
          <div class="col-md-6">
            <h3 class="h4 vt-section-title">{esc(tab["title"])}</h3>
            <p class="text-secondary mb-0">{esc(tab["text"])}</p>
          </div>
        </div>
      </div>"""
    return f"""<section class="vt-feature-tabs py-5 vt-reveal">
  <div class="container">
    <h2 class="vt-section-title text-center mb-4">{esc(title)}</h2>
    <div class="vt-tabs-nav d-flex flex-wrap justify-content-center gap-2 mb-4" role="tablist" data-vt-tabs>{nav_btns}</div>
    <div class="vt-tabs-panels">{panels}</div>
  </div>
</section>"""


def block_pricing_tiers(title: str, tiers: list[dict]) -> str:
    """Grille tarifs SaaS — carte mise en avant animée au survol."""
    cards = ""
    for t in tiers:
        hot = " vt-pricing-tier--hot" if t.get("hot") else ""
        cards += f"""<div class="col-md-4">
        <article class="vt-pricing-tier h-100{hot} vt-tilt-card">
          <h3 class="h5 mb-1">{esc(t["name"])}</h3>
          <p class="vt-pricing-price mb-3">{esc(t["price"])}</p>
          <ul class="small ps-3 mb-4">{"".join(f"<li>{esc(x)}</li>" for x in t.get("features", []))}</ul>
          <a class="btn btn-vt-primary w-100" href="{esc(t["href"])}">{esc(t["cta"])}</a>
        </article>
      </div>"""
    return f"""<section class="vt-pricing py-5 vt-reveal">
  <div class="container">
    <h2 class="vt-section-title text-center mb-5">{esc(title)}</h2>
    <div class="row g-4 vt-reveal-stagger">{cards}</div>
  </div>
</section>"""


def block_hero_tech_glow(
    h1: str,
    lead: str,
    img: str,
    alt: str,
    *,
    eyebrow: str,
    specs: list[tuple[str, str]],
    primary_href: str,
    primary_label: str,
    secondary_href: str = "",
    secondary_label: str = "",
) -> str:
    """Hero tech B2B avec scan lines + specs + ken burns."""
    pills = "".join(
        f'<span class="vt-spec-pill"><strong>{esc(val)}</strong> {esc(lbl)}</span>'
        for val, lbl in specs
    )
    sec_btn = ""
    if secondary_href and secondary_label:
        sec_btn = f'<a class="btn btn-vt-outline btn-sm rounded-0 px-3" href="{esc(secondary_href)}">{esc(secondary_label)}</a>'
    return f"""<section class="vt-hero-tech vt-hero-scan vt-reveal">
  <div class="container py-5">
    <p class="vt-eyebrow text-uppercase mb-2">{esc(eyebrow)}</p>
    <div class="row g-4 align-items-end">
      <div class="col-lg-7">
        <h1 class="vt-display display-5 mb-3">{esc(h1)}</h1>
        <p class="lead mb-4">{esc(lead)}</p>
        <div class="vt-spec-pills d-flex flex-wrap gap-2 mb-4">{pills}</div>
        <div class="d-flex flex-wrap gap-2">
          <a class="btn btn-vt-primary rounded-0 px-4" href="{esc(primary_href)}">{esc(primary_label)}</a>
          {sec_btn}
        </div>
      </div>
      <div class="col-lg-5">
        <figure class="vt-hero-tech-frame vt-ken-burns mb-0 rounded-0 overflow-hidden">
          {vt_picture(img, alt, css_class="w-100", loading=None, fetchpriority="high")}
        </figure>
      </div>
    </div>
  </div>
</section>"""


def block_progress_wizard(title: str, steps: list[dict]) -> str:
    """Parcours onboarding — barre de progression animée + étapes cliquables."""
    step_btns = ""
    panels = ""
    for i, step in enumerate(steps):
        active = " active" if i == 0 else ""
        step_btns += f"""<button type="button" class="vt-wizard-step{active}" data-vt-wizard-step="{i}" aria-current="{"step" if i == 0 else "false"}">
        <span class="vt-wizard-num">{i + 1}</span>
        <span class="vt-wizard-label">{esc(step["label"])}</span>
      </button>"""
        panels += f"""<div class="vt-wizard-panel{active}" data-vt-wizard-panel="{i}">
        <h3 class="h5 vt-section-title">{esc(step["title"])}</h3>
        <p class="text-secondary mb-3">{esc(step["text"])}</p>
        <figure class="mb-0 rounded-3 overflow-hidden vt-ken-burns">
          {vt_picture(step["img"], step.get("alt", step["title"]), css_class="w-100")}
        </figure>
      </div>"""
    pct = int(100 / max(len(steps), 1))
    return f"""<section class="vt-wizard py-5 vt-reveal" data-vt-progress-wizard data-vt-step-count="{len(steps)}">
  <div class="container">
    <h2 class="vt-section-title text-center mb-4">{esc(title)}</h2>
    <div class="vt-wizard-bar mb-4" aria-hidden="true">
      <div class="vt-wizard-bar-fill" style="--vt-wizard-pct: {pct}%"></div>
    </div>
    <div class="vt-wizard-steps d-flex flex-wrap justify-content-center gap-2 mb-4">{step_btns}</div>
    <div class="vt-wizard-panels">{panels}</div>
  </div>
</section>"""


def block_kpi_grid(title: str, kpis: list[dict]) -> str:
    """Cartes KPI dashboard — pulse live + compteurs animés."""
    cards = ""
    for k in kpis:
        count_attr = ""
        inner_val = esc(k["value"])
        if k.get("count_end") is not None:
            count_attr = f' data-vt-count-end="{k["count_end"]}" data-vt-count-suffix="{esc(k.get("count_suffix", ""))}" data-vt-count-prefix="{esc(k.get("count_prefix", ""))}"'
            inner_val = "0"
        delta = ""
        if k.get("delta"):
            delta = f'<span class="vt-kpi-delta">{esc(k["delta"])}</span>'
        cards += f"""<div class="col-6 col-lg-3">
        <article class="vt-kpi-card h-100">
          <span class="vt-kpi-pulse" aria-hidden="true"></span>
          <p class="vt-kpi-label small text-uppercase mb-1">{esc(k["label"])}</p>
          <p class="vt-kpi-value vt-stat-val mb-0"{count_attr}>{inner_val}</p>
          {delta}
        </article>
      </div>"""
    return f"""<section class="vt-kpi-grid py-5 vt-reveal">
  <div class="container">
    <h2 class="vt-section-title text-center mb-4">{esc(title)}</h2>
    <div class="row g-3 vt-reveal-stagger">{cards}</div>
  </div>
</section>"""


def block_state_morph(title: str, before: dict, after: dict) -> str:
    """Avant / après — crossfade au survol pour empty states."""
    return f"""<section class="vt-state-morph py-5 vt-reveal">
  <div class="container">
    <h2 class="vt-section-title text-center mb-4">{esc(title)}</h2>
    <div class="row g-4 align-items-center">
      <div class="col-lg-6">
        <div class="vt-morph-stage" data-vt-state-morph tabindex="0" role="img" aria-label="Comparaison avant et après">
          <figure class="vt-morph-layer vt-morph-before mb-0">
            {vt_picture(before["img"], before.get("alt", before["title"]), css_class="w-100")}
            <figcaption class="vt-morph-caption">{esc(before["title"])}</figcaption>
          </figure>
          <figure class="vt-morph-layer vt-morph-after mb-0">
            {vt_picture(after["img"], after.get("alt", after["title"]), css_class="w-100")}
            <figcaption class="vt-morph-caption vt-morph-caption--after">{esc(after["title"])}</figcaption>
          </figure>
        </div>
      </div>
      <div class="col-lg-6">
        <p class="text-secondary mb-2"><strong>Avant :</strong> {esc(before["text"])}</p>
        <p class="text-secondary mb-0"><strong>Après :</strong> {esc(after["text"])}</p>
        <p class="small text-muted mt-3 mb-0">Survolez l'image pour voir la transformation.</p>
      </div>
    </div>
  </div>
</section>"""


def block_notification_feed(title: str, items: list[dict]) -> str:
    """Flux notifications in-app — entrée en cascade."""
    rows = ""
    for it in items:
        urgent = " vt-notif--urgent" if it.get("urgent") else ""
        badge = f'<span class="vt-notif-badge">{esc(it["type"])}</span>'
        rows += f"""<article class="vt-notif-card{urgent}">
        <div class="d-flex justify-content-between align-items-start gap-2 mb-1">
          {badge}
          <time class="vt-notif-time small text-muted">{esc(it["time"])}</time>
        </div>
        <h3 class="h6 mb-1">{esc(it["title"])}</h3>
        <p class="small text-secondary mb-0">{esc(it["text"])}</p>
      </article>"""
    return f"""<section class="vt-notif-feed py-5 vt-reveal">
  <div class="container">
    <h2 class="vt-section-title text-center mb-4">{esc(title)}</h2>
    <div class="vt-notif-stack mx-auto vt-reveal-stagger">{rows}</div>
  </div>
</section>"""
