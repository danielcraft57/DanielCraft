"""SEO vitrines — Open Graph, Twitter, canonical, Schema.org microdata inline."""
from __future__ import annotations

import json
import re
from typing import Any

from vitrine_ai_lib import esc

SITE_BASE = "https://danielcraft.fr"
VITRINES_BASE = f"{SITE_BASE}/echantillons"
SCHEMA = "https://schema.org"


def demo_base(slug: str) -> str:
    return f"{VITRINES_BASE}/{slug}/demo"


def page_url(slug: str, page_file: str) -> str:
    return f"{demo_base(slug)}/{page_file}"


def abs_image(slug: str, rel: str = "images/hero.webp") -> str:
    return f"{demo_base(slug)}/{rel}"


def _schema_type(type_name: str) -> str:
    return f"{SCHEMA}/{type_name}"


def _addr(street: str, locality: str, postal: str) -> dict[str, str]:
    return {
        "streetAddress": street,
        "addressLocality": locality,
        "postalCode": postal,
        "addressCountry": "FR",
    }


def _geo(lat: float, lon: float) -> dict[str, float]:
    return {"latitude": lat, "longitude": lon}


def _hours(days: list[str], opens: str, closes: str) -> dict[str, Any]:
    return {"dayOfWeek": days, "opens": opens, "closes": closes}


def _saas_entity(name: str, description: str, rating: str = "4.8", count: int = 120) -> dict[str, Any]:
    return {
        "type": "SoftwareApplication",
        "name": name,
        "description": description,
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "Web",
        "offers": {
            "price": "0",
            "priceCurrency": "EUR",
            "description": "Essai gratuit 14 jours",
        },
        "aggregateRating": {
            "ratingValue": rating,
            "ratingCount": count,
        },
    }


def _entity(type_name: str, **fields: Any) -> dict[str, Any]:
    return {"type": type_name, **fields}


ENTITIES: dict[str, dict[str, Any]] = {
    "restauration": _entity(
        "Restaurant",
        name="Brasserie Saint-Jacques",
        servesCuisine="Lorraine, French",
        priceRange="€€",
        telephone="+33387751234",
        address=_addr("12 place Saint-Jacques", "Metz", "57000"),
        geo=_geo(49.1193, 6.1757),
        openingHours=[
            _hours(["Tuesday", "Wednesday", "Thursday", "Friday"], "12:00", "22:00"),
            _hours(["Saturday"], "12:00", "23:00"),
            _hours(["Sunday"], "10:00", "15:00"),
        ],
    ),
    "beaute": _entity(
        "BeautySalon",
        name="Spa Thalie",
        telephone="+33387174280",
        address=_addr("8 rue des Clercs", "Metz", "57000"),
        geo=_geo(49.1097, 6.1761),
        openingHours=[
            _hours(["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "10:00", "19:00"),
        ],
    ),
    "odontologie": _entity(
        "Dentist",
        name="Centre dentaire Mosaïque",
        telephone="+33382884500",
        address=_addr("42 avenue de la République", "Thionville", "57100"),
        geo=_geo(49.3578, 6.1694),
        openingHours=[
            _hours(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "08:30", "19:00"),
            _hours(["Saturday"], "08:00", "12:00"),
        ],
    ),
    "automobile": _entity(
        "AutoRepair",
        name="Garage Central Plappeville",
        telephone="+33387654321",
        address=_addr("Zone artisanale des Gravières", "Plappeville", "57050"),
        geo=_geo(49.1080, 6.0700),
        openingHours=[
            _hours(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "08:00", "18:00"),
            _hours(["Saturday"], "08:00", "12:00"),
        ],
    ),
    "commerce": _entity(
        "GroceryStore",
        name="Halles Thionville",
        telephone="+33382534000",
        address=_addr("Rue du Mail", "Thionville", "57100"),
        geo=_geo(49.3578, 6.1694),
        openingHours=[
            _hours(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "08:00", "20:00"),
            _hours(["Sunday"], "09:00", "12:30"),
        ],
    ),
    "comptable": _entity(
        "AccountingService",
        name="Verlaine & Associés",
        telephone="+33387759012",
        knowsAbout=["Tenue comptable", "Paie et DSN", "Conseil dirigeant", "Fiscalité PME", "Bilan flash"],
        address=_addr("14 rue Serpenoise", "Metz", "57000"),
        geo=_geo(49.1193, 6.1757),
        openingHours=[_hours(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "09:00", "18:00")],
    ),
    "industrie": _entity(
        "ProfessionalService",
        name="Précisite Usinage",
        description="Usinage de précision 5 axes, automobile et aéronautique",
        telephone="+33387224466",
        address=_addr("Zone industrielle des Hauts Champs", "Yutz", "57970"),
        geo=_geo(49.3550, 6.1920),
    ),
    "immobilier": _entity(
        "RealEstateAgent",
        name="Patrimoine Lorraine Metz",
        description="Agence immobilière Metz — vente, location et estimation",
        telephone="+33387361214",
        address=_addr("14 rue des Clercs", "Metz", "57000"),
        geo=_geo(49.1097, 6.1761),
    ),
    "juridique": _entity(
        "LegalService",
        name="Rivière & Partenaires",
        description="Cabinet d'avocats Metz — droit des affaires, social et contentieux",
        telephone="+33387759012",
        address=_addr("12 avenue Foch", "Metz", "57000"),
        geo=_geo(49.1193, 6.1757),
    ),
    "architecture": _entity(
        "ProfessionalService",
        name="Atelier Nord-Est",
        description="Agence d'architecture Metz — réhabilitation et conception durable",
        telephone="+33387661234",
        address=_addr("14 rue du XXe Corps", "Metz", "57000"),
        geo=_geo(49.1193, 6.1757),
    ),
    "fitness": _entity(
        "SportsActivityLocation",
        name="Pulse Fitness Metz",
        description="Salle de sport Metz — cours collectifs, musculation et essai gratuit",
        telephone="+33387554000",
        address=_addr("42 avenue de Strasbourg", "Metz", "57000"),
        geo=_geo(49.1193, 6.1757),
        openingHours=[
            _hours(
                ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                "06:00",
                "23:00",
            )
        ],
    ),
    "photographie": _entity(
        "ProfessionalService",
        name="Studio Lumière Grise",
        description="Photographe mariage et corporate à Metz — reportages et portraits",
        telephone="+33387214560",
        address=_addr("12 rue des Clercs", "Metz", "57000"),
        geo=_geo(49.1097, 6.1761),
    ),
    "association": _entity(
        "NGO",
        name="Solidarités Metz Métropole",
        description="Association d'utilité publique Metz — aide alimentaire, insertion et bénévolat",
        telephone="+33387345678",
        address=_addr("22 rue du Sablon", "Metz", "57000"),
        geo=_geo(49.1193, 6.1757),
    ),
    "education": _entity(
        "EducationalOrganization",
        name="Institut Mercure",
        description="Centre de formation professionnelle Thionville — alternance et reconversion",
        telephone="+33382884500",
        address=_addr("15 avenue des Deux Fontaines", "Thionville", "57100"),
        geo=_geo(49.3578, 6.1694),
    ),
    "services": _entity(
        "ProfessionalService",
        name="Proprio Facility",
        description="Facility management et conciergerie pour immeubles tertiaires en Lorraine",
        telephone="+33387654321",
        address=_addr("8 place Saint-Jacques", "Metz", "57000"),
        geo=_geo(49.1193, 6.1757),
    ),
    "etablissement": _entity(
        "Hotel",
        name="Hôtel Stanislas Collection",
        description="Hôtel 4 étoiles Nancy — place Stanislas, spa et séminaires",
        telephone="+33383541234",
        starRating="4",
        address=_addr("2 place Stanislas", "Nancy", "54000"),
        geo=_geo(48.6921, 6.1844),
    ),
    "technologie": _saas_entity(
        "Synapse Lorraine",
        "Plateforme data B2B pour industriels du Grand Est — lakehouse, pipelines et catalogues",
        "4.7",
        45,
    ),
    "saas-landing": _saas_entity(
        "FlowMetrics",
        "SaaS analytics pour équipes produit — funnels, rétention et activation",
    ),
    "saas-onboarding": _saas_entity(
        "TalentLoop",
        "Onboarding RH en 4 étapes — parcours guidé et barre de progression",
    ),
    "saas-dashboard": _saas_entity(
        "MetricPulse",
        "Dashboard activation produit — KPIs time-to-value et funnel onboarding",
        "4.7",
        95,
    ),
    "saas-empty": _saas_entity(
        "QueryBase",
        "Empty states et recherche intelligente — zéro impasse utilisateur",
        "4.6",
        80,
    ),
    "saas-notifications": _saas_entity(
        "PingFlow",
        "Centre de notifications in-app hiérarchisé et actionnable",
        "4.9",
        140,
    ),
    "boulangerie": _entity(
        "Bakery",
        name="Maison Lemaire",
        telephone="+33383351240",
        address=_addr("14 allee de la Pepiniere", "Nancy", "54000"),
        geo=_geo(48.6921, 6.1844),
        openingHours=[
            _hours(["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "07:00", "19:00"),
        ],
    ),
    "artisan": _entity(
        "Plumber",
        name="Clanche & Cuivre",
        telephone="+33387219040",
        address=_addr("Zone artisanale Nord", "Metz", "57070"),
        geo=_geo(49.1193, 6.1757),
    ),
    "fleuriste": _entity(
        "Florist",
        name="Atelier Corolle",
        telephone="+33388241750",
        address=_addr("22 rue de l'Orangerie", "Strasbourg", "67000"),
        geo=_geo(48.5846, 7.7701),
        openingHours=[
            _hours(["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "09:00", "19:00"),
        ],
    ),
    "caviste": _entity(
        "Store",
        name="Cave de la Gare",
        telephone="+33382531890",
        address=_addr("5 place de la Gare", "Thionville", "57100"),
        geo=_geo(49.3578, 6.1694),
        openingHours=[
            _hours(["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "10:00", "19:30"),
        ],
    ),
    "osteo": _entity(
        "MedicalBusiness",
        name="Cabinet des Ponts",
        telephone="+33387362210",
        address=_addr("9 quai Felix Marechal", "Metz", "57000"),
        geo=_geo(49.1193, 6.1757),
        openingHours=[
            _hours(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "08:30", "19:00"),
        ],
    ),
}


def get_entity(slug: str, **overrides: Any) -> dict[str, Any]:
    base = ENTITIES.get(slug)
    if base is None:
        base = _entity("Organization", name=overrides.pop("name", slug), description=overrides.pop("description", ""))
    entity = json.loads(json.dumps(base))
    entity.update({k: v for k, v in overrides.items() if v is not None})
    return entity


def breadcrumbs_from_nav(nav: list[dict], page_file: str, home_label: str) -> list[tuple[str, str]]:
    crumbs: list[tuple[str, str]] = [(home_label, "index.html")]
    if page_file == "index.html":
        return crumbs
    for item in nav:
        if item.get("file") == page_file:
            crumbs.append((item.get("label", page_file), page_file))
            break
    return crumbs


def seo_head_meta(
    title: str,
    description: str,
    slug: str,
    page_file: str,
    site_name: str,
    og_image: str = "images/hero.webp",
) -> str:
    url = page_url(slug, page_file)
    img = abs_image(slug, og_image)
    return f"""  <link rel="canonical" href="{esc(url)}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:site_name" content="{esc(site_name)}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{esc(url)}">
  <meta property="og:image" content="{esc(img)}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="520">
  <meta property="og:image:alt" content="{esc(title)}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(description)}">
  <meta name="twitter:image" content="{esc(img)}">
  <meta name="twitter:image:alt" content="{esc(title)}">"""


def block_breadcrumbs_visible(slug: str, crumbs: list[tuple[str, str]]) -> str:
    """Fil d'Ariane visible + microdata BreadcrumbList."""
    if len(crumbs) <= 1:
        return ""
    items = []
    for i, (label, file) in enumerate(crumbs, 1):
        href = page_url(slug, file)
        if i == len(crumbs):
            items.append(
                f"""      <li class="breadcrumb-item active" aria-current="page" itemprop="itemListElement" itemscope itemtype="{_schema_type("ListItem")}">
        <meta itemprop="position" content="{i}">
        <span itemprop="name">{esc(label)}</span>
      </li>"""
            )
        else:
            items.append(
                f"""      <li class="breadcrumb-item" itemprop="itemListElement" itemscope itemtype="{_schema_type("ListItem")}">
        <meta itemprop="position" content="{i}">
        <a itemprop="item" href="{esc(href)}"><span itemprop="name">{esc(label)}</span></a>
      </li>"""
            )
    return f"""<nav class="vt-breadcrumb py-2 border-bottom bg-light" aria-label="Fil d'Ariane" itemscope itemtype="{_schema_type("BreadcrumbList")}">
  <div class="container">
    <ol class="breadcrumb mb-0 small">
{chr(10).join(items)}
    </ol>
  </div>
</nav>"""


def enrich_body_semantic(
    body: str,
    title: str,
    description: str,
    slug: str,
    page_file: str,
    nav: list[dict],
    site_name: str,
) -> str:
    """Microdata sur le contenu réel : fil d'Ariane, main, h1, chapô, image hero."""
    crumbs = breadcrumbs_from_nav(nav, page_file, site_name)
    bc = block_breadcrumbs_visible(slug, crumbs)
    if bc and "</header>" in body:
        body = body.replace("</header>", f"</header>\n{bc}", 1)

    page_link = f'<link itemprop="url" href="{esc(page_url(slug, page_file))}">'
    if "<main>" in body:
        body = body.replace(
            "<main>",
            f'<main itemscope itemtype="{_schema_type("WebPage")}">\n{page_link}\n<meta itemprop="inLanguage" content="fr-FR">',
            1,
        )

    body = re.sub(r"(<h1\b)", r'\1 itemprop="name"', body, count=1)

    if re.search(r'\blead\b', body):
        body = re.sub(r'(<p class="[^"]*\blead\b[^"]*")', r'\1 itemprop="description"', body, count=1)
    else:
        body = re.sub(
            r'(<h1\b[^>]*itemprop="name"[^>]*>.*?</h1>\s*)(<p\b)',
            r'\1\2 itemprop="description" ',
            body,
            count=1,
            flags=re.DOTALL,
        )

    body = re.sub(
        r"(<main itemscope[^>]*>.*?)(<img )",
        r'\1\2 itemprop="image" ',
        body,
        count=1,
        flags=re.DOTALL,
    )

    return body
