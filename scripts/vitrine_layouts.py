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


def block_assist_chips(chips: list[dict], *, aria: str = "Raccourcis") -> str:
    """Pills Material-like : {label, href, active?}."""
    items = []
    for i, c in enumerate(chips):
        on = " on" if c.get("active") else ""
        delay = f' style="animation-delay:{0.05 * i:.2f}s"'
        items.append(
            f'<a class="vt-chip{on}" href="{esc(c.get("href", "#"))}"{delay}>{esc(c["label"])}</a>'
        )
    return f"""<section class="vt-chips py-3" aria-label="{esc(aria)}">
  <div class="container">
    <div class="d-flex flex-wrap gap-2 vt-chip-row">{"".join(items)}</div>
  </div>
</section>"""


def block_slot_card(
    *,
    title: str = "Prochains creneaux",
    kicker: str = "Reservation",
    slots: list[dict],
    href: str = "contact.html",
    cta_label: str = "Prendre RDV",
    note: str = "",
) -> str:
    """Carte creneaux (spa, garage) — {day, times}."""
    rows = ""
    for s in slots:
        rows += (
            f'<li><span>{esc(s["day"])}</span>'
            f'<strong>{esc(s["times"])}</strong></li>'
        )
    note_html = f'<p class="vt-slot-note small mb-0">{esc(note)}</p>' if note else ""
    return f"""<section class="vt-slots py-4 vt-reveal" aria-labelledby="vt-slots-title">
  <div class="container">
    <div class="vt-slot-card">
      <p class="vt-slot-kicker mb-1">{esc(kicker)}</p>
      <h2 id="vt-slots-title" class="h5 mb-3">{esc(title)}</h2>
      <ul class="vt-slot-list list-unstyled mb-3">{rows}</ul>
      <a class="btn btn-vt-primary rounded-pill px-4" href="{esc(href)}">{esc(cta_label)}</a>
      {note_html}
    </div>
  </div>
</section>"""


def block_booking_strip(
    *,
    title: str = "Reserver une chambre",
    action: str = "contact.html",
    cta_label: str = "Voir les dispo",
) -> str:
    """Bandeau reservation hotel : arrivee, depart, chambre."""
    return f"""<section class="vt-booking-strip py-4 vt-reveal" aria-labelledby="vt-book-title">
  <div class="container">
    <form class="vt-booking-bar row g-2 align-items-end" action="{esc(action)}" method="get">
      <div class="col-12 col-lg-3">
        <p id="vt-book-title" class="vt-booking-title mb-0">{esc(title)}</p>
      </div>
      <div class="col-6 col-md-3 col-lg-2">
        <label class="form-label small mb-1" for="vt-book-in">Arrivée</label>
        <input class="form-control" id="vt-book-in" name="arrivee" type="date">
      </div>
      <div class="col-6 col-md-3 col-lg-2">
        <label class="form-label small mb-1" for="vt-book-out">Départ</label>
        <input class="form-control" id="vt-book-out" name="depart" type="date">
      </div>
      <div class="col-12 col-md-4 col-lg-3">
        <label class="form-label small mb-1" for="vt-book-room">Chambre</label>
        <select class="form-select" id="vt-book-room" name="chambre">
          <option>Toutes les chambres</option>
          <option>Chambre classique</option>
          <option>Chambre deluxe</option>
          <option>Suite</option>
        </select>
      </div>
      <div class="col-12 col-lg-2">
        <button class="btn btn-vt-primary w-100 rounded-pill" type="submit">{esc(cta_label)}</button>
      </div>
    </form>
  </div>
</section>"""


def block_spa_m3_nav(
    brand: str,
    pages: list[dict],
    current: str,
    *,
    city: str,
    phone: str,
    cta_label: str = "Prendre RDV",
    cta_href: str = "contact.html",
) -> str:
    """Nav maquette M3 Spa Thalie : liens + ville + tel + CTA (pas de topbar sombre)."""
    links = []
    for p in pages:
        f = p["file"]
        base = f.split("#", 1)[0]
        active = " active" if base == current and "#" not in f else ""
        aria = ' aria-current="page"' if active else ""
        links.append(
            f'<li class="nav-item"><a class="nav-link{active}" href="{esc(f)}"{aria}>{esc(p["label"])}</a></li>'
        )
    tel_href = "tel:" + "".join(c for c in phone if c.isdigit())
    return f"""<header class="vt-header sticky-top" itemscope itemtype="https://schema.org/WebSite">
  <nav class="navbar navbar-expand-lg vt-navbar vt-navbar-m3" aria-label="Navigation principale">
    <div class="container">
      <a class="navbar-brand vt-brand" href="index.html" itemprop="url"><span itemprop="name">{esc(brand)}</span></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#vtNav" aria-controls="vtNav" aria-expanded="false" aria-label="Menu">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="vtNav">
        <ul class="navbar-nav mx-lg-auto mb-2 mb-lg-0">{"".join(links)}</ul>
        <div class="vt-nav-meta d-flex flex-wrap align-items-center gap-3">
          <span class="vt-nav-city"><span aria-hidden="true">📍</span> {esc(city)}</span>
          <a class="vt-nav-phone" href="{esc(tel_href)}">{esc(phone)}</a>
          <a class="btn btn-vt-primary rounded-pill px-4" href="{esc(cta_href)}">{esc(cta_label)}</a>
        </div>
      </div>
    </div>
  </nav>
</header>"""


def block_spa_m3_hero(
    h1: str,
    lead: str,
    img: str,
    alt: str,
    *,
    eyebrow: str,
    primary_href: str,
    primary_label: str,
    facts: list[dict],
) -> str:
    """Hero split M3 : texte a gauche, photo arrondie a droite + bandeau infos."""
    facts_html = "".join(
        f"""<li class="vt-m3-fact">
          <span class="vt-m3-fact-ico" aria-hidden="true">{esc(f.get("icon", "•"))}</span>
          <span><strong>{esc(f["title"])}</strong><span class="d-block">{esc(f.get("text", ""))}</span></span>
        </li>"""
        for f in facts
    )
    return f"""<section class="vt-m3-hero">
  <div class="container">
    <div class="row align-items-center g-4 g-lg-5">
      <div class="col-lg-5">
        <p class="vt-eyebrow text-uppercase mb-2">{esc(eyebrow)}</p>
        <h1 class="vt-display display-5 mb-3">{esc(h1)}</h1>
        <p class="lead vt-lead mb-4">{esc(lead)}</p>
        <a class="btn btn-vt-primary btn-lg rounded-pill px-4" href="{esc(primary_href)}">{esc(primary_label)} <span aria-hidden="true">→</span></a>
        <ul class="vt-m3-facts list-unstyled mb-0 mt-4 pt-3">{facts_html}</ul>
      </div>
      <div class="col-lg-7">
        <figure class="vt-m3-hero-media mb-0">
          {vt_picture(img, alt, css_class="w-100", loading=None, fetchpriority="high")}
        </figure>
      </div>
    </div>
  </div>
</section>"""


def block_spa_m3_phares(
    *,
    kicker: str,
    title: str,
    chips: list[dict],
    cards: list[dict],
) -> str:
    """Section soins phares : chips filtres + grille cartes duree/prix."""
    chip_html = "".join(
        f'<a class="vt-chip{" on" if c.get("active") else ""}" href="{esc(c.get("href", "#"))}">{esc(c["label"])}</a>'
        for c in chips
    )
    cards_html = ""
    for c in cards:
        cards_html += f"""<div class="col-6 col-lg-3">
        <article class="vt-m3-care-card h-100">
          <figure class="mb-0">{vt_picture(c["img"], c.get("alt", c["title"]), css_class="w-100")}</figure>
          <div class="vt-m3-care-body">
            <h3 class="h6 mb-2">{esc(c["title"])}</h3>
            <p class="small text-secondary mb-3">{esc(c["text"])}</p>
            <p class="vt-m3-care-meta mb-0"><span>{esc(c["duration"])}</span><strong>{esc(c["price"])}</strong></p>
          </div>
        </article>
      </div>"""
    return f"""<section class="vt-m3-phares py-5" aria-labelledby="phares-title">
  <div class="container">
    <div class="d-flex flex-wrap justify-content-between align-items-end gap-3 mb-4">
      <div>
        <p class="vt-eyebrow text-uppercase mb-1">{esc(kicker)}</p>
        <h2 id="phares-title" class="vt-section-title mb-0">{esc(title)}</h2>
      </div>
      <div class="d-flex flex-wrap gap-2 vt-chip-row" role="tablist" aria-label="Filtres">{chip_html}</div>
    </div>
    <div class="row g-3 g-lg-4">{cards_html}</div>
  </div>
</section>"""


def block_spa_fab(href: str = "contact.html", label: str = "Prendre rendez-vous") -> str:
    return f"""<a class="vt-fab" href="{esc(href)}" aria-label="{esc(label)}">
  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2" stroke="currentColor" stroke-width="1.8"/><path d="M3 10h18M8 3v4M16 3v4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
</a>"""


def block_garage_m3_nav(
    brand: str,
    pages: list[dict],
    current: str,
    *,
    cta_label: str = "Prendre RDV",
    cta_href: str = "contact.html",
) -> str:
    """Nav navy M3 Garage Central."""
    links = []
    for p in pages:
        f = p["file"]
        base = f.split("#", 1)[0]
        active = " active" if base == current and "#" not in f else ""
        aria = ' aria-current="page"' if active else ""
        links.append(
            f'<li class="nav-item"><a class="nav-link{active}" href="{esc(f)}"{aria}>{esc(p["label"])}</a></li>'
        )
    return f"""<header class="vt-header sticky-top" itemscope itemtype="https://schema.org/WebSite">
  <nav class="navbar navbar-expand-lg vt-navbar vt-navbar-garage-m3" aria-label="Navigation principale">
    <div class="container">
      <a class="navbar-brand vt-brand" href="index.html" itemprop="url"><span itemprop="name">{esc(brand)}</span></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#vtNav" aria-controls="vtNav" aria-expanded="false" aria-label="Menu">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="vtNav">
        <ul class="navbar-nav ms-lg-auto mb-2 mb-lg-0 align-items-lg-center gap-lg-1">{"".join(links)}</ul>
        <a class="btn btn-vt-nav-cta rounded-pill px-4 ms-lg-3" href="{esc(cta_href)}">{esc(cta_label)}</a>
      </div>
    </div>
  </nav>
</header>"""


def block_garage_m3_hero(
    h1: str,
    lead: str,
    img: str,
    alt: str,
    *,
    location: str,
    primary_href: str,
    primary_label: str,
    service_cards: list[dict],
) -> str:
    """Hero split M3 : texte + cartes services a gauche, photo + formulaire RDV a droite."""
    cards = ""
    for c in service_cards:
        cards += f"""<article class="vt-g-service-card">
          <span class="vt-g-service-ico" aria-hidden="true">{esc(c.get("icon", "•"))}</span>
          <h3 class="h6 mb-1">{esc(c["title"])}</h3>
          <p class="small text-secondary mb-2">{esc(c["text"])}</p>
          <a class="vt-g-more" href="{esc(c.get("href", "services.html"))}">En savoir plus →</a>
        </article>"""
    return f"""<section class="vt-g-hero">
  <div class="container">
    <div class="row g-4 g-xl-5 align-items-start">
      <div class="col-lg-6">
        <p class="vt-g-pin mb-3"><span aria-hidden="true">📍</span> {esc(location)}</p>
        <h1 class="vt-display display-4 mb-3">{esc(h1)}</h1>
        <p class="lead vt-lead mb-4">{esc(lead)}</p>
        <a class="btn btn-vt-primary btn-lg rounded-pill px-4 mb-4" href="{esc(primary_href)}">{esc(primary_label)} <span aria-hidden="true">→</span></a>
        <div class="vt-g-service-row">{cards}</div>
      </div>
      <div class="col-lg-6">
        <div class="vt-g-hero-aside">
          <figure class="vt-g-hero-media mb-0">
            {vt_picture(img, alt, css_class="w-100", loading=None, fetchpriority="high")}
          </figure>
          <div class="vt-g-rdv-card" id="rdv-rapide">
            <h2 class="h5 mb-1">Prendre rendez-vous</h2>
            <p class="small text-secondary mb-3">Un créneau rapide, un service efficace.</p>
            <form class="row g-2" action="contact.html" method="get">
              <div class="col-12"><label class="visually-hidden" for="g-name">Nom</label><input class="form-control" id="g-name" name="nom" placeholder="Nom complet" required></div>
              <div class="col-md-6"><label class="visually-hidden" for="g-tel">Téléphone</label><input class="form-control" id="g-tel" name="tel" type="tel" placeholder="Téléphone" required></div>
              <div class="col-md-6"><label class="visually-hidden" for="g-mail">Email</label><input class="form-control" id="g-mail" name="email" type="email" placeholder="Email"></div>
              <div class="col-md-6"><label class="visually-hidden" for="g-svc">Service</label><select class="form-select" id="g-svc" name="service"><option>Type de service</option><option>Entretien</option><option>Pneus</option><option>Carrosserie</option><option>Diagnostic</option></select></div>
              <div class="col-md-6"><label class="visually-hidden" for="g-date">Date</label><input class="form-control" id="g-date" name="date" type="date"></div>
              <div class="col-12"><label class="visually-hidden" for="g-msg">Message</label><textarea class="form-control" id="g-msg" name="message" rows="2" placeholder="Message (optionnel)"></textarea></div>
              <div class="col-12"><button class="btn btn-vt-primary w-100 rounded-pill" type="submit">Envoyer la demande</button></div>
            </form>
            <p class="small text-secondary mb-0 mt-2">Maquette : formulaire non connecté.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""


def block_garage_m3_stats(items: list[dict]) -> str:
    cells = []
    for it in items:
        count_end = it.get("count_end")
        suffix = it.get("count_suffix", "")
        prefix = it.get("count_prefix", "")
        if count_end is not None:
            val_html = (
                f'<strong class="vt-stat-val" data-vt-count-end="{int(count_end)}" '
                f'data-vt-count-suffix="{esc(suffix)}" data-vt-count-prefix="{esc(prefix)}">'
                f"{esc(prefix)}0{esc(suffix)}</strong>"
            )
        else:
            val_html = f"<strong>{esc(it['value'])}</strong>"
        cells.append(
            f"""<div class="col-6 col-md-3">
        <div class="vt-g-stat">
          <span class="vt-g-stat-ico" aria-hidden="true">{esc(it.get("icon", "•"))}</span>
          {val_html}
          <span>{esc(it["label"])}</span>
        </div>
      </div>"""
        )
    return f"""<section class="vt-g-stats py-4" aria-label="Chiffres cles">
  <div class="container"><div class="row g-3 text-center">{"".join(cells)}</div></div>
</section>"""


def block_garage_m3_local(
    title: str,
    text: str,
    checks: list[str],
    *,
    href: str = "contact.html",
    cta: str = "Nous contacter",
) -> str:
    lis = "".join(f'<li><span aria-hidden="true">✓</span> {esc(c)}</li>' for c in checks)
    return f"""<section class="vt-g-local py-5">
  <div class="container">
    <div class="row align-items-center g-4">
      <div class="col-lg-7">
        <h2 class="vt-section-title mb-3">{esc(title)}</h2>
        <p class="text-secondary mb-4">{esc(text)}</p>
        <ul class="vt-g-checks list-unstyled mb-0">{lis}</ul>
      </div>
      <div class="col-lg-5 text-lg-end">
        <a class="btn btn-vt-primary btn-lg rounded-pill px-4" href="{esc(href)}">{esc(cta)}</a>
      </div>
    </div>
  </div>
</section>"""


def block_phone_fab(phone: str, label: str = "Appeler") -> str:
    tel = "tel:" + "".join(c for c in phone if c.isdigit())
    return f"""<a class="vt-fab vt-fab-phone" href="{esc(tel)}" aria-label="{esc(label)} {esc(phone)}">
  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6.5 4.5h3l1.5 4-2 1.5a12 12 0 0 0 5.5 5.5l1.5-2 4 1.5v3a2 2 0 0 1-2 2A14.5 14.5 0 0 1 4.5 6.5a2 2 0 0 1 2-2Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
</a>"""


def block_immo_m3_nav(
    brand: str,
    pages: list[dict],
    current: str,
    *,
    phone: str,
    cta_label: str = "Estimation gratuite",
    cta_href: str = "estimation.html",
) -> str:
    links = []
    for p in pages:
        f = p["file"]
        base = f.split("#", 1)[0]
        active = " active" if base == current and "#" not in f else ""
        aria = ' aria-current="page"' if active else ""
        links.append(
            f'<li class="nav-item"><a class="nav-link{active}" href="{esc(f)}"{aria}>{esc(p["label"])}</a></li>'
        )
    tel = "tel:" + "".join(c for c in phone if c.isdigit())
    return f"""<header class="vt-header sticky-top" itemscope itemtype="https://schema.org/WebSite">
  <nav class="navbar navbar-expand-lg vt-navbar vt-navbar-immo-m3" aria-label="Navigation principale">
    <div class="container">
      <a class="navbar-brand vt-brand" href="index.html" itemprop="url"><span itemprop="name">{esc(brand)}</span></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#vtNav" aria-controls="vtNav" aria-expanded="false" aria-label="Menu">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="vtNav">
        <ul class="navbar-nav mx-lg-auto mb-2 mb-lg-0">{"".join(links)}</ul>
        <div class="d-flex flex-wrap align-items-center gap-3">
          <a class="vt-immo-phone" href="{esc(tel)}">{esc(phone)}</a>
          <a class="btn btn-vt-primary rounded-pill px-4" href="{esc(cta_href)}">{esc(cta_label)}</a>
        </div>
      </div>
    </div>
  </nav>
</header>"""


def block_immo_m3_hero(
    h1: str,
    lead: str,
    img: str,
    alt: str,
    *,
    primary_href: str,
    primary_label: str,
    secondary_href: str,
    secondary_label: str,
) -> str:
    return f"""<section class="vt-immo-hero">
  <div class="container">
    <div class="row align-items-center g-4 g-lg-5">
      <div class="col-lg-6">
        <h1 class="vt-display display-5 mb-3">{esc(h1)}</h1>
        <p class="lead vt-lead mb-4">{esc(lead)}</p>
        <div class="d-flex flex-wrap gap-3">
          <a class="btn btn-vt-primary btn-lg rounded-pill px-4" href="{esc(primary_href)}">{esc(primary_label)}</a>
          <a class="btn btn-vt-outline btn-lg rounded-pill px-4" href="{esc(secondary_href)}">{esc(secondary_label)}</a>
        </div>
      </div>
      <div class="col-lg-6">
        <figure class="vt-immo-hero-media mb-0">
          {vt_picture(img, alt, css_class="w-100", loading=None, fetchpriority="high")}
        </figure>
      </div>
    </div>
  </div>
</section>"""


def block_immo_m3_search(*, action: str = "biens.html") -> str:
    return f"""<section class="vt-immo-search" aria-label="Recherche de biens">
  <div class="container">
    <form class="vt-immo-search-card row g-2 align-items-end" action="{esc(action)}" method="get" role="search">
      <div class="col-6 col-lg">
        <label class="form-label small mb-1" for="im-loc">Localisation</label>
        <input class="form-control" id="im-loc" name="ville" type="search" placeholder="Metz, Nancy…">
      </div>
      <div class="col-6 col-lg">
        <label class="form-label small mb-1" for="im-type">Type de bien</label>
        <select class="form-select" id="im-type" name="type"><option>Tous</option><option>Appartement</option><option>Maison</option><option>Terrain</option></select>
      </div>
      <div class="col-6 col-lg">
        <label class="form-label small mb-1" for="im-prix">Prix max.</label>
        <select class="form-select" id="im-prix" name="prix"><option>Indifférent</option><option>200 000 €</option><option>400 000 €</option><option>600 000 €</option></select>
      </div>
      <div class="col-6 col-lg">
        <label class="form-label small mb-1" for="im-pieces">Pièces min.</label>
        <select class="form-select" id="im-pieces" name="pieces"><option>Toutes</option><option>2</option><option>3</option><option>4+</option></select>
      </div>
      <div class="col-6 col-lg">
        <label class="form-label small mb-1" for="im-surf">Surface min.</label>
        <select class="form-select" id="im-surf" name="surface"><option>Toutes</option><option>50 m²</option><option>80 m²</option><option>120 m²</option></select>
      </div>
      <div class="col-6 col-lg-auto">
        <button class="btn btn-vt-primary rounded-pill px-4 w-100" type="submit">Rechercher</button>
      </div>
    </form>
  </div>
</section>"""


def block_immo_m3_listings(
    title: str,
    listings: list[dict],
    *,
    count_label: str = "",
    cta_href: str = "",
    cta_label: str = "",
) -> str:
    cards = []
    for item in listings:
        city = item.get("city", "")
        kind = item.get("kind", "Vente")
        dpe = item.get("dpe", "")
        dpe_html = f'<span class="vt-immo-dpe" data-dpe="{esc(dpe)}">{esc(dpe)}</span>' if dpe else ""
        meta = []
        if item.get("surface"):
            meta.append(esc(item["surface"]))
        if item.get("rooms"):
            meta.append(esc(item["rooms"]))
        if item.get("baths"):
            meta.append(esc(item["baths"]))
        meta_html = " · ".join(meta)
        cards.append(f"""<div class="col-md-6 col-xl-4">
        <article class="vt-immo-card h-100">
          <div class="vt-immo-card-media">
            {vt_picture(item["img"], item.get("alt", item["title"]), css_class="w-100")}
            <div class="vt-immo-badges">
              <span class="vt-immo-badge navy">{esc(city)}</span>
              <span class="vt-immo-badge soft">{esc(kind)}</span>
            </div>
          </div>
          <div class="vt-immo-card-body">
            <h3 class="h6 mb-1">{esc(item["title"])}</h3>
            <p class="small text-secondary mb-2">{esc(item.get("address", item.get("specs", "")))}</p>
            <p class="vt-immo-price mb-2">{esc(item["price"])}</p>
            <div class="d-flex justify-content-between align-items-center gap-2">
              <p class="small text-secondary mb-0">{meta_html}</p>
              {dpe_html}
            </div>
          </div>
        </article>
      </div>""")
    head = f'<h2 class="vt-section-title mb-0">{esc(title)}</h2>'
    if count_label:
        head = f'<div class="d-flex flex-wrap justify-content-between align-items-center gap-2 mb-4"><h2 class="vt-section-title mb-0">{esc(count_label)}</h2><span class="small text-secondary">Trier par : Plus récents</span></div>'
    else:
        head = f'<h2 class="vt-section-title text-center mb-4">{esc(title)}</h2>'
    cta = ""
    if cta_href and cta_label:
        cta = f'<div class="text-center mt-4"><a class="btn btn-vt-outline rounded-pill px-4" href="{esc(cta_href)}">{esc(cta_label)}</a></div>'
    return f"""<section class="vt-immo-listings py-5">
  <div class="container">
    {head}
    <div class="row g-4">{"".join(cards)}</div>
    {cta}
  </div>
</section>"""

def block_photo_m3_nav(
    brand: str,
    *,
    city: str,
    chips: list[dict],
    cta_label: str = "Demander un devis",
    cta_href: str = "contact.html",
) -> str:
    chip_html = "".join(
        f'<a class="vt-ph-chip{" on" if c.get("active") else ""}" href="{esc(c.get("href", "#"))}">{esc(c["label"])}</a>'
        for c in chips
    )
    return f"""<header class="vt-header sticky-top vt-ph-header" itemscope itemtype="https://schema.org/WebSite">
  <nav class="navbar navbar-expand-lg vt-navbar-photo-m3" aria-label="Navigation principale">
    <div class="container-fluid px-3 px-lg-4">
      <a class="navbar-brand vt-brand" href="index.html" itemprop="url"><span itemprop="name">{esc(brand)}</span> <small>{esc(city)}</small></a>
      <div class="d-flex flex-wrap align-items-center gap-2 ms-auto">
        {chip_html}
        <a class="btn btn-vt-nav-cta rounded-pill px-3" href="{esc(cta_href)}">{esc(cta_label)}</a>
      </div>
    </div>
  </nav>
</header>"""


def block_photo_m3_masonry(items: list[dict]) -> str:
    cells = ""
    for i, it in enumerate(items):
        tall = " tall" if i % 3 == 0 else ""
        cells += f"""<figure class="vt-ph-tile{tall}">
      {vt_picture(it["img"], it.get("alt", it.get("title", "")), css_class="w-100")}
      <figcaption><strong>{esc(it.get("title", ""))}</strong></figcaption>
    </figure>"""
    return f"""<section class="vt-ph-masonry" aria-label="Portfolio">
  <div class="vt-ph-grid">{cells}</div>
</section>"""


def block_photo_toast(message: str = "Votre demande a bien ete envoyee", close_href: str = "#") -> str:
    return f"""<div class="vt-ph-toast" role="status">
  <span aria-hidden="true">✓</span>
  <p class="mb-0">{esc(message)} <a href="{esc(close_href)}">Fermer</a></p>
</div>"""


def block_plus_fab(href: str = "contact.html", label: str = "Nouveau projet") -> str:
    return f"""<a class="vt-fab vt-fab-plus" href="{esc(href)}" aria-label="{esc(label)}">
  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
</a>"""


def block_hotel_m3_nav(
    brand: str,
    pages: list[dict],
    current: str,
    *,
    cta_label: str = "Reserver",
    cta_href: str = "contact.html",
) -> str:
    links = []
    for p in pages:
        f = p["file"]
        base = f.split("#", 1)[0]
        active = " active" if base == current and "#" not in f else ""
        aria = ' aria-current="page"' if active else ""
        links.append(
            f'<li class="nav-item"><a class="nav-link{active}" href="{esc(f)}"{aria}>{esc(p["label"])}</a></li>'
        )
    return f"""<header class="vt-header sticky-top" itemscope itemtype="https://schema.org/WebSite">
  <nav class="navbar navbar-expand-lg vt-navbar-hotel-m3" aria-label="Navigation principale">
    <div class="container">
      <a class="navbar-brand vt-brand" href="index.html" itemprop="url"><span itemprop="name">{esc(brand)}</span></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#vtNav" aria-controls="vtNav" aria-expanded="false" aria-label="Menu">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="vtNav">
        <ul class="navbar-nav mx-lg-auto mb-2 mb-lg-0">{"".join(links)}</ul>
        <a class="btn btn-vt-nav-cta rounded-pill px-4" href="{esc(cta_href)}">{esc(cta_label)}</a>
      </div>
    </div>
  </nav>
</header>"""


def block_hotel_m3_hero(
    h1: str,
    lead: str,
    img: str,
    alt: str,
    *,
    primary_href: str,
    primary_label: str,
) -> str:
    return f"""<section class="vt-ht-hero">
  <div class="vt-ht-hero-media">
    {vt_picture(img, alt, css_class="w-100", loading=None, fetchpriority="high")}
    <div class="vt-ht-hero-copy">
      <div class="container">
        <h1 class="vt-display display-4 text-white mb-3">{esc(h1)}</h1>
        <p class="lead text-white-50 mb-4">{esc(lead)}</p>
        <a class="btn btn-vt-primary btn-lg rounded-pill px-4" href="{esc(primary_href)}">{esc(primary_label)}</a>
      </div>
    </div>
  </div>
</section>"""


def block_hotel_m3_booking(*, action: str = "contact.html", cta_label: str = "Voir les disponibilites") -> str:
    return f"""<section class="vt-ht-book" aria-label="Reservation">
  <div class="container">
    <form class="vt-ht-book-card row g-2 align-items-end" action="{esc(action)}" method="get">
      <div class="col-6 col-lg">
        <label class="form-label small mb-1" for="ht-in">Arrivee</label>
        <input class="form-control" id="ht-in" name="arrivee" type="date">
      </div>
      <div class="col-6 col-lg">
        <label class="form-label small mb-1" for="ht-out">Depart</label>
        <input class="form-control" id="ht-out" name="depart" type="date">
      </div>
      <div class="col-6 col-lg">
        <label class="form-label small mb-1" for="ht-guests">Voyageurs</label>
        <select class="form-select" id="ht-guests" name="guests"><option>2 voyageurs, 1 chambre</option><option>1 voyageur</option><option>2 voyageurs, 2 chambres</option><option>Famille</option></select>
      </div>
      <div class="col-6 col-lg-auto">
        <button class="btn btn-vt-primary rounded-pill px-4 w-100" type="submit">{esc(cta_label)}</button>
      </div>
    </form>
  </div>
</section>"""


def block_hotel_m3_rooms(title: str, lead: str, rooms: list[dict]) -> str:
    cards = ""
    for r in rooms:
        cards += f"""<div class="col-md-4">
        <article class="vt-ht-room h-100">
          <figure class="mb-0">{vt_picture(r["img"], r.get("alt", r["title"]), css_class="w-100")}</figure>
          <div class="vt-ht-room-body">
            <div class="d-flex justify-content-between gap-2 mb-1">
              <h3 class="h5 mb-0">{esc(r["title"])}</h3>
              <p class="vt-ht-price mb-0">{esc(r["price"])}</p>
            </div>
            <p class="small text-secondary mb-3">{esc(r["meta"])}</p>
            <a class="btn btn-vt-primary btn-sm rounded-pill px-3" href="{esc(r.get("href", "contact.html"))}">Reserver</a>
          </div>
        </article>
      </div>"""
    return f"""<section class="vt-ht-rooms py-5">
  <div class="container">
    <div class="mb-4">
      <h2 class="vt-section-title mb-2">{esc(title)}</h2>
      <p class="text-secondary mb-0">{esc(lead)}</p>
    </div>
    <div class="row g-4">{cards}</div>
  </div>
</section>"""


def block_motives_m3(
    *,
    title: str,
    lead: str,
    seek: str,
    avoid: str,
    leave_with: str,
    kicker: str = "Pourquoi nous",
    label_seek: str = "Tu cherches",
    label_avoid: str = "On evite",
    label_leave: str = "Tu repart avec",
) -> str:
    """Pourquoi venir ici : 3 pastilles client (pas de jargon persona)."""
    return f"""<section class="vt-motives vt-reveal" aria-labelledby="vt-motives-title">
  <div class="container">
    <div class="vt-motives-shell">
      <p class="vt-eyebrow text-uppercase mb-1">{esc(kicker)}</p>
      <h2 id="vt-motives-title" class="vt-section-title mb-2">{esc(title)}</h2>
      <p class="vt-motives-lead mb-4">{esc(lead)}</p>
      <div class="row g-3">
        <div class="col-md-4">
          <article class="vt-motives-pill h-100">
            <span class="vt-motives-label">{esc(label_seek)}</span>
            <p class="mb-0">{esc(seek)}</p>
          </article>
        </div>
        <div class="col-md-4">
          <article class="vt-motives-pill h-100">
            <span class="vt-motives-label">{esc(label_avoid)}</span>
            <p class="mb-0">{esc(avoid)}</p>
          </article>
        </div>
        <div class="col-md-4">
          <article class="vt-motives-pill h-100">
            <span class="vt-motives-label">{esc(label_leave)}</span>
            <p class="mb-0">{esc(leave_with)}</p>
          </article>
        </div>
      </div>
    </div>
  </div>
</section>"""


def block_friction_m3(
    *,
    problem: str,
    solution: str,
    note: str = "",
    kicker: str = "Ce qui change",
    title: str = "Moins de flou, plus de clarte",
    label_problem: str = "Le frein",
    label_solution: str = "Chez nous",
) -> str:
    """Frein vs reponse concrete - langage client, pas canvas Lean."""
    note_html = ""
    if note:
        note_html = f"""<div class="col-12">
        <p class="vt-friction-note mb-0">{esc(note)}</p>
      </div>"""
    return f"""<section class="vt-friction vt-reveal" aria-labelledby="vt-friction-title">
  <div class="container">
    <p class="vt-eyebrow text-uppercase text-center mb-1">{esc(kicker)}</p>
    <h2 id="vt-friction-title" class="vt-section-title text-center mb-4">{esc(title)}</h2>
    <div class="row g-3 g-lg-4 align-items-stretch">
      <div class="col-md-6">
        <article class="vt-friction-card vt-friction-problem h-100">
          <span class="vt-friction-tag">{esc(label_problem)}</span>
          <p class="mb-0">{esc(problem)}</p>
        </article>
      </div>
      <div class="col-md-6">
        <article class="vt-friction-card vt-friction-solution h-100">
          <span class="vt-friction-tag">{esc(label_solution)}</span>
          <p class="mb-0">{esc(solution)}</p>
        </article>
      </div>
      {note_html}
    </div>
  </div>
</section>"""


def block_journey_m3(
    title: str,
    steps: list[dict],
    *,
    kicker: str = "Comment ca se passe",
    lead: str = "",
) -> str:
    """Parcours client M3 : stepper numerote, sans hint meta UX."""
    cells = ""
    n = len(steps)
    for i, step in enumerate(steps, 1):
        emotion = step.get("emotion") or ""
        emotion_html = (
            f'<p class="vt-journey-emotion mb-0">{esc(emotion)}</p>' if emotion else ""
        )
        cells += f"""<div class="vt-journey-step">
        <article class="vt-journey-card h-100">
          <span class="vt-journey-num" aria-hidden="true">{i:02d}</span>
          <h3 class="h6 mb-2">{esc(step["title"])}</h3>
          <p class="small text-secondary mb-2">{esc(step["text"])}</p>
          {emotion_html}
        </article>
      </div>"""
    lead_html = (
        f'<p class="vt-journey-lead text-center text-secondary mb-4">{esc(lead)}</p>'
        if lead
        else '<div class="mb-4"></div>'
    )
    return f"""<section class="vt-journey vt-reveal" aria-labelledby="vt-journey-title">
  <div class="container">
    <p class="vt-eyebrow text-uppercase text-center mb-1">{esc(kicker)}</p>
    <h2 id="vt-journey-title" class="vt-section-title text-center mb-2">{esc(title)}</h2>
    {lead_html}
    <div class="vt-journey-track" data-steps="{n}">{cells}</div>
  </div>
</section>"""


def block_surface_band_m3(
    inner_html: str,
    *,
    tone: str = "soft",
    aria_label: str = "",
) -> str:
    """Bandeau surface M3 pour rythmer le body (soft | tint | deep)."""
    tone_cls = {
        "soft": "vt-surface-band--soft",
        "tint": "vt-surface-band--tint",
        "deep": "vt-surface-band--deep",
    }.get(tone, "vt-surface-band--soft")
    aria = f' aria-label="{esc(aria_label)}"' if aria_label else ""
    return f"""<div class="vt-surface-band {tone_cls}"{aria}>
  {inner_html}
</div>"""


def block_photo_chapters_m3(
    chapters: list[dict],
    *,
    kicker: str = "Sur place",
    title: str = "",
) -> str:
    """Chapitres photo + texte alternes (body M3)."""
    head = ""
    if title:
        head = f"""<div class="container">
      <p class="vt-eyebrow text-uppercase text-center mb-1">{esc(kicker)}</p>
      <h2 class="vt-section-title text-center mb-4">{esc(title)}</h2>
    </div>"""
    rows = ""
    for i, ch in enumerate(chapters):
        flip = " vt-photo-chapter--flip" if i % 2 else ""
        rows += f"""<article class="vt-photo-chapter{flip} vt-reveal">
      <div class="container">
        <div class="row g-4 align-items-center">
          <div class="col-lg-6">
            <figure class="vt-photo-chapter-media mb-0">
              {vt_picture(ch["img"], ch.get("alt", ch["title"]), css_class="w-100")}
            </figure>
          </div>
          <div class="col-lg-6">
            <h3 class="vt-section-title h3 mb-2">{esc(ch["title"])}</h3>
            <p class="text-secondary mb-0">{esc(ch["text"])}</p>
          </div>
        </div>
      </div>
    </article>"""
    return f"""<section class="vt-photo-chapters" aria-label="{esc(title or kicker)}">
  {head}
  {rows}
</section>"""


def block_reviews_m3(
    *,
    title: str,
    reviews: list[dict],
    kicker: str = "Ils en parlent",
    rating: str = "4,9/5",
    rating_label: str = "avis clients",
) -> str:
    """Preuve sociale M3 : note + 3 cartes avis (fiction locale)."""
    cards = ""
    for r in reviews:
        stars = int(r.get("stars", 5))
        stars = max(1, min(5, stars))
        star_html = "★" * stars + "☆" * (5 - stars)
        cards += f"""<div class="col-md-4">
        <figure class="vt-review-card h-100">
          <div class="vt-review-stars" aria-label="{stars} sur 5">{star_html}</div>
          <blockquote class="vt-review-quote mb-3">
            <p class="mb-0">{esc(r["text"])}</p>
          </blockquote>
          <figcaption>
            <strong>{esc(r["name"])}</strong>
            <span class="d-block small text-secondary">{esc(r.get("meta", ""))}</span>
          </figcaption>
        </figure>
      </div>"""
    return f"""<section class="vt-reviews" aria-labelledby="vt-reviews-title">
  <div class="container">
    <div class="d-flex flex-wrap justify-content-between align-items-end gap-3 mb-4">
      <div>
        <p class="vt-eyebrow text-uppercase mb-1">{esc(kicker)}</p>
        <h2 id="vt-reviews-title" class="vt-section-title mb-0">{esc(title)}</h2>
      </div>
      <p class="vt-reviews-score mb-0"><strong>{esc(rating)}</strong> <span>{esc(rating_label)}</span></p>
    </div>
    <div class="row g-3 g-lg-4">{cards}</div>
  </div>
</section>"""


def block_dialog_m3(
    *,
    dialog_id: str,
    title: str,
    lead: str,
    primary_label: str,
    primary_href: str,
    secondary_label: str = "Fermer",
    fields_html: str = "",
) -> str:
    """Modale commerciale M3 (dialog + backdrop)."""
    return f"""<div class="vt-dialog-backdrop" id="{esc(dialog_id)}" hidden data-vt-dialog>
  <div class="vt-dialog" role="dialog" aria-modal="true" aria-labelledby="{esc(dialog_id)}-title">
    <h2 id="{esc(dialog_id)}-title">{esc(title)}</h2>
    <p>{esc(lead)}</p>
    {fields_html}
    <div class="vt-dialog-actions">
      <button type="button" class="btn btn-vt-outline" data-vt-dialog-close>{esc(secondary_label)}</button>
      <a class="btn btn-vt-primary" href="{esc(primary_href)}">{esc(primary_label)}</a>
    </div>
  </div>
</div>"""


def block_snackbar_m3(message: str, *, snack_id: str = "vtSnack") -> str:
    return f'<div class="vt-snackbar" id="{esc(snack_id)}" role="status" aria-live="polite">{esc(message)}</div>'


def block_fab_menu_m3(
    actions: list[dict],
    *,
    main_label: str = "Actions",
) -> str:
    """FAB + speed dial (actions: label, href ou data-vt-dialog-open)."""
    items = ""
    for a in actions:
        if a.get("dialog"):
            items += (
                f'<button type="button" data-vt-dialog-open="{esc(a["dialog"])}">{esc(a["label"])}</button>'
            )
        else:
            items += f'<a href="{esc(a.get("href", "#"))}">{esc(a["label"])}</a>'
    return f"""<div class="vt-fab-menu" data-vt-fab-menu>
  <div class="vt-fab-menu-actions">{items}</div>
  <button type="button" class="vt-fab-menu-main" aria-expanded="false" aria-label="{esc(main_label)}">+</button>
</div>"""


def block_menu_h_cards_m3(
    items: list[dict],
    *,
    kicker: str,
    title: str,
    chips: list[dict] | None = None,
) -> str:
    """Carrousel horizontal de plats / offres (maquette resto M3)."""
    chip_html = ""
    if chips:
        chip_html = (
            '<div class="d-flex flex-wrap gap-2 mb-3 vt-chip-row" role="tablist">'
            + "".join(
                f'<button type="button" class="vt-chip{" on" if c.get("active") else ""}">{esc(c["label"])}</button>'
                for c in chips
            )
            + "</div>"
        )
    cards = ""
    for it in items:
        feat = " vt-menu-card--feat" if it.get("featured") else ""
        cards += f"""<article class="vt-menu-card{feat}">
      {vt_picture(it["img"], it.get("alt", it["title"]), css_class="")}
      <div class="vt-menu-card-body">
        <h3 class="h6 mb-1">{esc(it["title"])}</h3>
        <p class="small text-secondary mb-2">{esc(it.get("text", ""))}</p>
        <p class="fw-bold mb-0">{esc(it.get("price", ""))}</p>
      </div>
      <button type="button" class="vt-menu-card-add" data-vt-snack="Ajoute au panier demo : {esc(it["title"])}" aria-label="Ajouter">+</button>
    </article>"""
    return f"""<section class="py-5 vt-reveal" aria-labelledby="vt-menu-h-title">
  <div class="container">
    <p class="vt-eyebrow text-uppercase mb-1">{esc(kicker)}</p>
    <h2 id="vt-menu-h-title" class="vt-section-title mb-3">{esc(title)}</h2>
    {chip_html}
    <div class="vt-h-scroll vt-reveal-stagger">{cards}</div>
  </div>
</section>"""


def block_sticky_cta_m3(text: str, btn: str, href: str, *, dialog: str = "") -> str:
    open_attr = f' data-vt-dialog-open="{esc(dialog)}"' if dialog else ""
    if dialog:
        btn_html = f'<button type="button" class="btn btn-vt-primary"{open_attr}>{esc(btn)}</button>'
    else:
        btn_html = f'<a class="btn btn-vt-primary" href="{esc(href)}">{esc(btn)}</a>'
    return f"""<div class="vt-sticky-cta d-lg-none">
  <div class="d-flex align-items-center justify-content-between gap-2">
    <span class="small">{esc(text)}</span>
    {btn_html}
  </div>
</div>"""


def block_nav_rail_m3(
    brand: str,
    pages: list[dict],
    current: str,
    *,
    hours: str = "",
    address: str = "",
    phone: str = "",
    tagline: str = "",
) -> str:
    """Rail gauche Material (resto / retail dark) - desktop; compact mobile via CSS."""
    links = ""
    for p in pages:
        active = " is-active" if p["file"] == current else ""
        links += (
            f'<a class="vt-rail-link{active}" href="{esc(p["file"])}">'
            f'<span class="vt-rail-dot" aria-hidden="true"></span>'
            f'{esc(p["label"])}</a>'
        )
    meta = ""
    if hours:
        meta += f'<p class="vt-rail-meta">{esc(hours)}</p>'
    if address:
        meta += f'<p class="vt-rail-meta">{esc(address)}</p>'
    if phone:
        tel = phone.replace(" ", "")
        meta += f'<a class="vt-rail-meta" href="tel:{esc(tel)}">{esc(phone)}</a>'
    return f"""<aside class="vt-rail" aria-label="Navigation">
  <div class="vt-rail-brand">
    <a href="index.html">{esc(brand)}</a>
    {f'<p class="vt-rail-tag">{esc(tagline)}</p>' if tagline else ""}
  </div>
  <nav class="vt-rail-nav">{links}</nav>
  <div class="vt-rail-foot">{meta}</div>
</aside>
<nav class="vt-rail-mobile" aria-label="Navigation mobile">{links}</nav>"""


def block_rail_topbar_m3(
    *,
    search_placeholder: str = "Reserver une table",
    cta_label: str = "Reserver",
    cta_dialog: str = "",
    cta_href: str = "contact.html",
) -> str:
    if cta_dialog:
        cta = (
            f'<button type="button" class="btn btn-vt-primary btn-sm px-3" '
            f'data-vt-dialog-open="{esc(cta_dialog)}">{esc(cta_label)}</button>'
        )
    else:
        cta = f'<a class="btn btn-vt-primary btn-sm px-3" href="{esc(cta_href)}">{esc(cta_label)}</a>'
    return f"""<div class="vt-rail-topbar">
  <label class="vt-rail-search">
    <span class="visually-hidden">{esc(search_placeholder)}</span>
    <input type="search" placeholder="{esc(search_placeholder)}" readonly>
  </label>
  <div class="vt-rail-topbar-actions">{cta}</div>
</div>"""


def block_marquee_m3(items: list[str], *, aria_hidden: bool = True) -> str:
    doubled = items + items
    spans = "".join(f"<span>{esc(x)}</span>" for x in doubled)
    ah = ' aria-hidden="true"' if aria_hidden else ""
    return f'<div class="vt-marquee"{ah}><div class="vt-marquee-track">{spans}</div></div>'


def block_health_booking_hero_m3(
    title: str,
    lead: str,
    *,
    badge: str,
    primary_label: str = "Voir plus de disponibilites",
    dialog: str = "rdvDent",
    inset_img: str = "scene-1.png",
    inset_alt: str = "Cabinet",
    status: str = "Consultations sur rendez-vous",
    times: list[str] | None = None,
) -> str:
    """Hero sante M3 (maquette osteo) : copy + carte creneaux a gauche, grande photo a droite."""
    times = times or ["09:00", "11:00", "14:30"]
    time_html = "".join(
        f'<button type="button" class="vt-time-chip{" on" if i == 0 else ""}">{esc(t)}</button>'
        for i, t in enumerate(times)
    )
    return f"""<section class="vt-health-hero vt-reveal">
  <div class="container">
    <div class="row g-4 g-xl-5 align-items-center">
      <div class="col-lg-6">
        <p class="vt-health-badge">{esc(badge)}</p>
        <h1 class="vt-display display-5 mb-3">{esc(title)}</h1>
        <p class="lead mb-3">{esc(lead)}</p>
        <p class="vt-health-status mb-4"><span aria-hidden="true">✓</span> {esc(status)}</p>
        <div class="vt-booking-widget vt-booking-widget--inline" data-vt-booking>
          <div class="d-flex align-items-start gap-2 mb-3">
            <span class="vt-booking-ico" aria-hidden="true">📅</span>
            <div>
              <p class="fw-semibold mb-1">Quand souhaitez-vous venir ?</p>
              <p class="small text-secondary mb-0">Choisissez un creneau - on confirme sous 24 h.</p>
            </div>
          </div>
          <div class="vt-time-grid vt-time-grid--3 mb-3">{time_html}</div>
          <button type="button" class="btn btn-link px-0" data-vt-dialog-open="{esc(dialog)}">{esc(primary_label)} →</button>
        </div>
      </div>
      <div class="col-lg-6">
        <figure class="vt-health-hero-media mb-0">
          {vt_picture(inset_img, inset_alt, css_class="w-100", loading=None, fetchpriority="high")}
        </figure>
      </div>
    </div>
  </div>
</section>"""


def block_health_stats_m3(items: list[dict]) -> str:
    """Bandeau 4 preuves - maquette osteo."""
    cells = "".join(
        f"""<div class="col-6 col-lg-3">
        <article class="vt-health-stat">
          <span class="vt-health-stat-ico" aria-hidden="true">{esc(it.get("icon", "•"))}</span>
          <div>
            <strong>{esc(it.get("value", ""))}</strong>
            <span>{esc(it.get("label", ""))}</span>
          </div>
        </article>
      </div>"""
        for it in items
    )
    return f"""<section class="vt-health-stats vt-reveal" aria-label="En chiffres">
  <div class="container"><div class="row g-3">{cells}</div></div>
</section>"""


def block_pill_appbar_m3(
    brand: str,
    pages: list[dict],
    current: str,
    *,
    phone: str,
    cta_label: str = "Prendre rendez-vous",
    cta_dialog: str = "",
    cta_href: str = "contact.html",
    subtitle: str = "",
) -> str:
    """App bar flottante style osteo M3."""
    links = ""
    for p in pages:
        active = " is-active" if p["file"] == current else ""
        links += f'<a class="vt-pill-link{active}" href="{esc(p["file"])}">{esc(p["label"])}</a>'
    if cta_dialog:
        cta = (
            f'<button type="button" class="btn btn-light btn-sm rounded-pill px-3" '
            f'data-vt-dialog-open="{esc(cta_dialog)}">{esc(cta_label)}</button>'
        )
    else:
        cta = (
            f'<a class="btn btn-light btn-sm rounded-pill px-3" href="{esc(cta_href)}">'
            f'{esc(cta_label)}</a>'
        )
    tel = phone.replace(" ", "")
    sub = f'<span class="vt-pill-sub">{esc(subtitle)}</span>' if subtitle else ""
    return f"""<header class="vt-pill-appbar" itemscope itemtype="https://schema.org/WebSite">
  <a class="vt-pill-brand" href="index.html" itemprop="url">
    <span itemprop="name">{esc(brand)}</span>{sub}
  </a>
  <nav class="vt-pill-nav" aria-label="Principal">{links}</nav>
  <div class="vt-pill-actions">
    <a class="vt-pill-phone" href="tel:{esc(tel)}">{esc(phone)}</a>
    {cta}
  </div>
</header>"""
