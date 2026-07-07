"""Construction du payload Prestafacture /produits depuis prestations.json (API livrables + techStack)."""
from __future__ import annotations

from typing import Any

# Heures totales réalistes (freelance solo : brief, prod, relectures, mise en ligne).
ESTIMATED_HOURS_BY_SKU: dict[str, float] = {
    "SITE-VITRINE-ESSENTIEL": 18,
    "SITE-VITRINE": 26,
    "SITE-VITRINE-ECO": 24,
    "IDENTITE-MULTI": 22,
    "PACK-SEO-GOOGLE-CHATGPT": 16,
    "SEO-BASIQUE": 7,
    "SEO-CHATGPT": 11,
    "IA-FAQ-SITE": 30,
    "IA-SUPPORT-EMAIL": 34,
    "MAINT-MENSUEL": 1.5,
    "IA-CONTENUS-WEB": 14,
    "IA-REDACTION-COMMERCIALE": 11,
    "IA-ANALYSE-DONNEES": 32,
    "IA-CHATBOT-ECOMMERCE": 36,
    "IA-AUTOMATISATION-TACHES": 28,
    "IA-MAINTENANCE-MENSUEL": 1.5,
    "IA-EVOLUTION-FEATURE": 7,
    "IA-AUDIT-USAGE": 7,
    "CONSEIL-ARCHI": 6,
    "INTEG-CRM": 7,
    "MIGRATION-DONNEES": 9,
    "INTEG-API": 5,
    "RAPPORT-PERF": 4,
    "PAGE-SUPP": 2.5,
    "FORM-AVANCE": 3.5,
    "REFONTE-LEGERE": 10,
    "MAJ-CONTENU-5H": 5,
    "HEBERG-DOMAIN": 2.5,
    "BACKUP-SECU": 4,
    "SSL-CONFIG": 2,
    "SUPPORT-ABO": 0.5,
    "DEPANNAGE-2H": 2,
    "ACCOMP-H": 1,
    "SUPPORT-H": 1,
    "ECO-AUDIT-SITE": 5,
    "ECO-MEDIAS-OPTIMIZE": 7,
    "ECO-PERF-FIX": 10,
    "ECO-PAGE-RSE": 3,
    "ECO-MONITOR-MENSUEL": 0.5,
    "ECO-FORMATION-2H": 2.5,
    "ECO-IMAGES-EXTRA": 1,
}

# Livrables courts (2 à 3 max) — montants + heures alignés sur le réel.
LIVRABLES_BY_SKU: dict[str, list[dict[str, Any]]] = {
    "SITE-VITRINE-ESSENTIEL": [
        {"livrable": "Pages essentielles (jusqu'à 3)", "montant": 280, "heures": 12},
        {"livrable": "Mise en ligne, formulaire et HTTPS", "montant": 110, "heures": 6},
    ],
    "SITE-VITRINE": [
        {"livrable": "Pages + intégration (jusqu'à 5)", "montant": 440, "heures": 20},
        {"livrable": "Mise en ligne et formulaire contact", "montant": 150, "heures": 6},
    ],
    "SITE-VITRINE-ECO": [
        {"livrable": "Vitrine éco-conçue (5 pages max)", "montant": 440, "heures": 18},
        {"livrable": "Médias optimisés + page engagement", "montant": 150, "heures": 6},
    ],
    "IDENTITE-MULTI": [
        {"livrable": "Charte et déclinaisons visuelles", "montant": 520, "heures": 13},
        {"livrable": "Adaptation site et supports", "montant": 370, "heures": 9},
    ],
    "PACK-SEO-GOOGLE-CHATGPT": [
        {"livrable": "Audit SEO + plan d'action", "montant": 260, "heures": 6},
        {"livrable": "Corrections et contenus structurés IA", "montant": 430, "heures": 10},
    ],
    "SEO-BASIQUE": [
        {"livrable": "Audit et rapport", "montant": 120, "heures": 3},
        {"livrable": "Corrections prioritaires", "montant": 170, "heures": 4},
    ],
    "SEO-CHATGPT": [
        {"livrable": "Analyse et structuration", "montant": 179, "heures": 4},
        {"livrable": "FAQ / données structurées", "montant": 270, "heures": 7},
    ],
    "IA-FAQ-SITE": [
        {"livrable": "Installation et configuration", "montant": 590, "heures": 18},
        {"livrable": "Entraînement contenus + mise en service", "montant": 400, "heures": 12},
    ],
    "IA-SUPPORT-EMAIL": [
        {"livrable": "Configuration assistant e-mail", "montant": 650, "heures": 20},
        {"livrable": "Formation et ajustements", "montant": 440, "heures": 14},
    ],
    "MAINT-MENSUEL": [
        {"livrable": "Maintenance mensuelle (1 site)", "montant": 49, "heures": 1.5},
    ],
    "IA-CONTENUS-WEB": [
        {"livrable": "Brief et rédaction pages", "montant": 320, "heures": 9},
        {"livrable": "Relecture et mise en forme web", "montant": 170, "heures": 5},
    ],
    "IA-REDACTION-COMMERCIALE": [
        {"livrable": "Configuration et modèles", "montant": 269, "heures": 6},
        {"livrable": "Formation + ajustements", "montant": 180, "heures": 5},
    ],
    "IA-ANALYSE-DONNEES": [
        {"livrable": "Tableau de bord sur mesure", "montant": 860, "heures": 22},
        {"livrable": "Documentation et prise en main", "montant": 430, "heures": 10},
    ],
    "IA-CHATBOT-ECOMMERCE": [
        {"livrable": "Connexion catalogue + réponses", "montant": 960, "heures": 24},
        {"livrable": "Tests et mise en ligne", "montant": 530, "heures": 12},
    ],
    "IA-AUTOMATISATION-TACHES": [
        {"livrable": "Recensement et automatisation", "montant": 750, "heures": 19},
        {"livrable": "Tests et notice", "montant": 340, "heures": 9},
    ],
    "IA-MAINTENANCE-MENSUEL": [
        {"livrable": "Mise à jour assistant (mensuel)", "montant": 69, "heures": 1.5},
    ],
    "IA-EVOLUTION-FEATURE": [
        {"livrable": "Nouvelle fonction assistant", "montant": 330, "heures": 7},
    ],
    "IA-AUDIT-USAGE": [
        {"livrable": "Entretien et analyse usages", "montant": 169, "heures": 3},
        {"livrable": "Rapport et restitution", "montant": 180, "heures": 4},
    ],
    "CONSEIL-ARCHI": [
        {"livrable": "Étude faisabilité et budget", "montant": 349, "heures": 6},
    ],
    "INTEG-CRM": [
        {"livrable": "Connexion site → logiciel", "montant": 299, "heures": 7},
    ],
    "MIGRATION-DONNEES": [
        {"livrable": "Migration et contrôle", "montant": 349, "heures": 9},
    ],
    "INTEG-API": [
        {"livrable": "Liaison API / webhook", "montant": 179, "heures": 5},
    ],
    "RAPPORT-PERF": [
        {"livrable": "Mesure et rapport vitesse", "montant": 129, "heures": 4},
    ],
    "PAGE-SUPP": [
        {"livrable": "Page supplémentaire", "montant": 59, "heures": 2.5},
    ],
    "FORM-AVANCE": [
        {"livrable": "Formulaire sur mesure", "montant": 99, "heures": 3.5},
    ],
    "REFONTE-LEGERE": [
        {"livrable": "Refonte visuelle", "montant": 349, "heures": 10},
    ],
    "MAJ-CONTENU-5H": [
        {"livrable": "Pack 5 h de mises à jour", "montant": 249, "heures": 5},
    ],
    "HEBERG-DOMAIN": [
        {"livrable": "Hébergement + domaine (1 an)", "montant": 89, "heures": 2.5},
    ],
    "BACKUP-SECU": [
        {"livrable": "Sauvegardes et sécurisation", "montant": 119, "heures": 4},
    ],
    "SSL-CONFIG": [
        {"livrable": "Certificat HTTPS", "montant": 49, "heures": 2},
    ],
    "SUPPORT-ABO": [
        {"livrable": "Support e-mail mensuel", "montant": 29, "heures": 0.5},
    ],
    "DEPANNAGE-2H": [
        {"livrable": "Intervention 2 h", "montant": 139, "heures": 2},
    ],
    "ACCOMP-H": [
        {"livrable": "Accompagnement (1 h)", "montant": 65, "heures": 1},
    ],
    "SUPPORT-H": [
        {"livrable": "Support prioritaire (1 h)", "montant": 75, "heures": 1},
    ],
    "ECO-AUDIT-SITE": [
        {"livrable": "Audit sobriété + rapport", "montant": 110, "heures": 3.5},
        {"livrable": "Échange de restitution (30 min)", "montant": 39, "heures": 1.5},
    ],
    "ECO-MEDIAS-OPTIMIZE": [
        {"livrable": "Optimisation images (~30)", "montant": 149, "heures": 5},
        {"livrable": "Vidéos au clic + mise en ligne", "montant": 50, "heures": 2},
    ],
    "ECO-PERF-FIX": [
        {"livrable": "Corrections techniques prioritaires", "montant": 259, "heures": 7},
        {"livrable": "Mesure avant/après", "montant": 70, "heures": 3},
    ],
    "ECO-PAGE-RSE": [
        {"livrable": "Page engagement numérique", "montant": 89, "heures": 3},
    ],
    "ECO-MONITOR-MENSUEL": [
        {"livrable": "Veille sobriété mensuelle", "montant": 35, "heures": 0.5},
    ],
    "ECO-FORMATION-2H": [
        {"livrable": "Atelier 2 h (bonnes pratiques)", "montant": 129, "heures": 2.5},
    ],
    "ECO-IMAGES-EXTRA": [
        {"livrable": "15 images supplémentaires", "montant": 49, "heures": 1},
    ],
}

TECH_LANGUAGES_BY_CATEGORY: dict[str, list[str]] = {
    "identite": ["HTML", "CSS", "PHP"],
    "ia": ["Python", "TypeScript"],
    "technique": ["TypeScript", "Python", "Node.js"],
    "site-contenu": ["HTML", "CSS", "JavaScript", "PHP"],
    "maintenance": ["PHP", "Linux", "Nginx"],
    "eco": ["HTML", "CSS", "PHP"],
}

TECH_LANGUAGES_BY_SKU: dict[str, list[str]] = {
    "IA-FAQ-SITE": ["Python", "TypeScript"],
    "IA-CHATBOT-ECOMMERCE": ["Python", "TypeScript"],
    "INTEG-CRM": ["TypeScript", "Python", "Node.js"],
    "MIGRATION-DONNEES": ["Python", "TypeScript", "Node.js"],
    "INTEG-API": ["TypeScript", "Node.js"],
}

TECH_AI_BY_CATEGORY: dict[str, list[str]] = {
    "ia": ["OpenAI", "ChatGPT API"],
    "identite": [],
    "technique": [],
    "site-contenu": [],
    "maintenance": [],
    "eco": [],
}

TECH_AI_BY_SKU: dict[str, list[str]] = {
    "SEO-CHATGPT": ["OpenAI", "ChatGPT API"],
    "PACK-SEO-GOOGLE-CHATGPT": ["OpenAI"],
    "IA-CONTENUS-WEB": ["OpenAI"],
    "IA-REDACTION-COMMERCIALE": ["OpenAI"],
    "IA-ANALYSE-DONNEES": ["OpenAI", "Python"],
    "IA-AUTOMATISATION-TACHES": ["OpenAI", "n8n"],
    "IA-SUPPORT-EMAIL": ["OpenAI"],
    "SITE-VITRINE": ["Cursor", "Claude"],
    "SITE-VITRINE-ESSENTIEL": ["Cursor", "Claude"],
    "SITE-VITRINE-ECO": ["Cursor", "Claude"],
}

PRESTAFACTURE_META_BY_CATEGORY: dict[str, dict[str, str]] = {
    "identite": {"category": "THEME", "purpose": "SHOWCASE", "iconName": "window-maximize"},
    "ia": {"category": "DEV", "purpose": "SAAS", "iconName": "robot"},
    "technique": {"category": "API", "purpose": "WEBSITE", "iconName": "plug"},
    "site-contenu": {"category": "THEME", "purpose": "WEBSITE", "iconName": "paint-brush"},
    "maintenance": {"category": "DEV", "purpose": "WEBSITE", "iconName": "shield-alt"},
    "eco": {"category": "THEME", "purpose": "WEBSITE", "iconName": "leaf"},
}

FA_ICON_TO_PRESTAFACTURE: dict[str, str] = {
    "fa-globe": "window-maximize",
    "fa-fingerprint": "palette",
    "fa-robot": "robot",
    "fa-plug": "plug",
    "fa-paint-brush": "paint-brush",
    "fa-shield-alt": "shield-alt",
    "fa-wpforms": "file-alt",
    "fa-server": "server",
    "fa-lock": "lock",
    "fa-headset": "headset",
    "fa-tools": "wrench",
    "fa-bolt": "bolt",
    "fa-edit": "edit",
    "fa-palette": "palette",
    "fa-save": "save",
    "fa-user-cog": "user-cog",
    "fa-chart-line": "chart-line",
    "fa-search": "search",
    "fa-comments": "comments",
    "fa-envelope": "envelope",
    "fa-cogs": "cogs",
    "fa-database": "database",
    "fa-code": "code",
    "fa-tachometer-alt": "tachometer-alt",
    "fa-leaf": "leaf",
    "fa-seedling": "seedling",
    "fa-image": "image",
    "fa-feather-alt": "feather",
    "fa-hand-holding-heart": "heart",
    "fa-chalkboard-teacher": "chalkboard-teacher",
}

DESCRIPTION_MAX_LEN = 220
LIVRABLE_LABEL_MAX = 120
MAX_FALLBACK_LIVRABLES = 3


def _category_key(entry: dict, parent: dict | None) -> str:
    source = parent if parent else entry
    return (source.get("category") or "technique").strip()


def product_meta(entry: dict, parent: dict | None = None) -> dict[str, str]:
    cat = _category_key(entry, parent)
    meta = dict(PRESTAFACTURE_META_BY_CATEGORY.get(cat, PRESTAFACTURE_META_BY_CATEGORY["technique"]))
    source = parent if parent else entry
    fa = (source.get("icon") or "").strip()
    if fa in FA_ICON_TO_PRESTAFACTURE:
        meta["iconName"] = FA_ICON_TO_PRESTAFACTURE[fa]
    return meta


def estimate_hours(sku: str, price_eur: int, category: str) -> float:
    if sku in ESTIMATED_HOURS_BY_SKU:
        return float(ESTIMATED_HOURS_BY_SKU[sku])
    if price_eur <= 0:
        return 1.0
    if category == "maintenance" and price_eur < 80:
        return 1.0
    if price_eur < 100:
        return 1.5
    if price_eur < 300:
        return 4.0
    if price_eur < 600:
        return 8.0
    if price_eur < 1000:
        return 12.0
    if price_eur < 1500:
        return 18.0
    return 24.0


def _split_amount(total: int, parts: int) -> list[int]:
    if parts <= 0:
        return []
    if total <= 0:
        return [0] * parts
    base = total // parts
    remainder = total % parts
    amounts = [base] * parts
    for i in range(remainder):
        amounts[i] += 1
    return amounts


def _split_hours(total: float, parts: int) -> list[float]:
    if parts <= 0:
        return []
    if total <= 0:
        return [0.0] * parts
    base = round(total / parts, 2)
    amounts = [base] * parts
    diff = round(total - sum(amounts), 2)
    if amounts:
        amounts[-1] = round(amounts[-1] + diff, 2)
    return amounts


def _livrable_labels(entry: dict, parent: dict | None, name: str) -> list[str]:
    explicit = entry.get("prestafacture_livrables")
    if isinstance(explicit, list) and explicit:
        labels: list[str] = []
        for item in explicit:
            if isinstance(item, dict) and item.get("livrable"):
                labels.append(str(item["livrable"]).strip())
            elif isinstance(item, str) and item.strip():
                labels.append(item.strip())
        if labels:
            return [label[:LIVRABLE_LABEL_MAX] for label in labels[:MAX_FALLBACK_LIVRABLES]]

    labels = []
    raw = entry.get("includes")
    if (not raw or not isinstance(raw, list)) and parent:
        raw = parent.get("includes")
    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, str) and item.strip():
                labels.append(item.strip()[:LIVRABLE_LABEL_MAX])
            if len(labels) >= MAX_FALLBACK_LIVRABLES:
                break
    if labels:
        return labels

    return [name[:LIVRABLE_LABEL_MAX]]


def _normalize_livrable_row(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "livrable": str(item.get("livrable") or "")[:LIVRABLE_LABEL_MAX],
        "montant": int(item.get("montant") or 0),
        "heures": round(float(item.get("heures") or 0), 2),
    }


def build_livrables(
    entry: dict,
    sku: str,
    name: str,
    price_eur: int,
    parent: dict | None = None,
) -> list[dict[str, Any]]:
    """Tableau { livrable, montant, heures } pour PATCH/POST produit."""
    if sku in LIVRABLES_BY_SKU:
        return [_normalize_livrable_row(item) for item in LIVRABLES_BY_SKU[sku]]

    explicit = entry.get("prestafacture_livrables")
    if isinstance(explicit, list) and explicit and isinstance(explicit[0], dict):
        out = []
        for item in explicit:
            if isinstance(item, dict) and item.get("livrable"):
                out.append(_normalize_livrable_row(item))
        if out:
            return out

    category = _category_key(entry, parent)
    total_hours = estimate_hours(sku, price_eur, category)
    labels = _livrable_labels(entry, parent, name)
    montants = _split_amount(max(0, price_eur), len(labels))
    heures = _split_hours(total_hours, len(labels))

    return [
        {
            "livrable": label,
            "montant": montants[i],
            "heures": heures[i],
        }
        for i, label in enumerate(labels)
    ]


def build_tech_stack(sku: str, category: str) -> dict[str, list[str]]:
    """techStack API Prestafacture : { languages, ai }."""
    languages = list(TECH_LANGUAGES_BY_SKU.get(sku, TECH_LANGUAGES_BY_CATEGORY.get(category, ["PHP"])))
    ai = list(TECH_AI_BY_SKU.get(sku, TECH_AI_BY_CATEGORY.get(category, [])))
    stack: dict[str, list[str]] = {"languages": languages}
    if ai:
        stack["ai"] = ai
    return stack


def product_description(
    entry: dict,
    name: str,
    price_eur: int,
    parent: dict | None = None,
    slug: str = "",
) -> str:
    """Description courte pour le catalogue Prestafacture (pas le long texte marketing)."""
    short = (entry.get("short_description") or (parent or {}).get("short_description") or "").strip()
    tagline = (entry.get("tagline") or (parent or {}).get("tagline") or "").strip()
    text = short or tagline or name.strip()

    price_label = (entry.get("price_label") or (parent or {}).get("price_label") or "Forfait").strip()
    if price_eur > 0:
        text = f"{text} — {price_label} {price_eur} € HT"

    return text[:DESCRIPTION_MAX_LEN] if text else name[:DESCRIPTION_MAX_LEN]


def build_rich_product_body(
    entry: dict,
    sku: str,
    name: str,
    price_eur: int,
    parent: dict | None = None,
    slug: str = "",
) -> dict[str, Any]:
    """Payload POST/PATCH /produits — champs catalogue + livrables + techStack."""
    category_key = _category_key(entry, parent)
    meta = product_meta(entry, parent)
    icon = meta["iconName"]
    livrables = build_livrables(entry, sku, name, price_eur, parent)
    tech_stack = build_tech_stack(sku, category_key)
    total_hours = round(sum(float(x.get("heures") or 0) for x in livrables), 2)

    body: dict[str, Any] = {
        "name": name[:200],
        "sku": sku,
        "kind": "SERVICE",
        "unitPrice": price_eur,
        "defaultTaxRateId": 1,
        "category": meta["category"],
        "purpose": meta["purpose"],
        "visualType": "library",
        "iconName": icon,
        "imageData": f"library:{icon}",
        "description": product_description(entry, name, price_eur, parent, slug),
        "livrables": livrables,
        "techStack": tech_stack,
    }
    if total_hours > 0:
        body["estimatedHours"] = total_hours
    return body


def livrables_summary(livrables: list[dict[str, Any]]) -> str:
    if not livrables:
        return "0 livrable"
    total_m = sum(int(x.get("montant") or 0) for x in livrables)
    total_h = round(sum(float(x.get("heures") or 0) for x in livrables), 2)
    return f"{len(livrables)} livrable(s), {total_m} EUR HT, {total_h}h"
