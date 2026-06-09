"""Construction du payload Facturio /produits depuis prestations.json (API livrables + techStack)."""
from __future__ import annotations

from typing import Any

ESTIMATED_HOURS_BY_SKU: dict[str, int] = {
    "SITE-VITRINE": 10,
    "IDENTITE-MULTI": 18,
    "PACK-SEO-GOOGLE-CHATGPT": 14,
    "SEO-BASIQUE": 8,
    "SEO-CHATGPT": 10,
    "IA-FAQ-SITE": 20,
    "IA-SUPPORT-EMAIL": 24,
    "MAINT-MENSUEL": 2,
    "IA-CONTENUS-WEB": 12,
    "IA-REDACTION-COMMERCIALE": 10,
    "IA-ANALYSE-DONNEES": 28,
    "IA-CHATBOT-ECOMMERCE": 32,
    "IA-AUTOMATISATION-TACHES": 24,
    "IA-MAINTENANCE-MENSUEL": 2,
    "IA-EVOLUTION-FEATURE": 8,
    "IA-AUDIT-USAGE": 6,
    "CONSEIL-ARCHI": 8,
    "INTEG-CRM": 10,
    "MIGRATION-DONNEES": 12,
    "INTEG-API": 6,
    "RAPPORT-PERF": 4,
    "PAGE-SUPP": 2,
    "FORM-AVANCE": 4,
    "REFONTE-LEGERE": 8,
    "MAJ-CONTENU-5H": 5,
    "HEBERG-DOMAIN": 2,
    "BACKUP-SECU": 4,
    "SSL-CONFIG": 1,
    "SUPPORT-ABO": 1,
    "DEPANNAGE-2H": 2,
    "ACCOMP-H": 1,
    "SUPPORT-H": 1,
}

# Livrables explicites (alignes catalogue Facturio) — prioritaire sur includes[]
LIVRABLES_BY_SKU: dict[str, list[dict[str, Any]]] = {
    "IA-AUDIT-USAGE": [
        {"livrable": "Audit de vos usages IA", "montant": 250, "heures": 3},
        {"livrable": "Recommandations prioritaires", "montant": 150, "heures": 3},
    ],
}

TECH_LANGUAGES_BY_CATEGORY: dict[str, list[str]] = {
    "identite": ["HTML", "CSS", "PHP"],
    "ia": ["Python", "TypeScript"],
    "technique": ["TypeScript", "Python", "Node.js"],
    "site-contenu": ["HTML", "CSS", "JavaScript", "PHP"],
    "maintenance": ["PHP", "Linux", "Nginx"],
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
}

TECH_AI_BY_SKU: dict[str, list[str]] = {
    "SEO-CHATGPT": ["OpenAI", "ChatGPT API"],
    "PACK-SEO-GOOGLE-CHATGPT": ["OpenAI"],
    "IA-CONTENUS-WEB": ["OpenAI"],
    "IA-REDACTION-COMMERCIALE": ["OpenAI"],
    "IA-ANALYSE-DONNEES": ["OpenAI", "Python"],
    "IA-AUTOMATISATION-TACHES": ["OpenAI", "n8n"],
    "IA-SUPPORT-EMAIL": ["OpenAI"],
}

FACTURIO_META_BY_CATEGORY: dict[str, dict[str, str]] = {
    "identite": {"category": "THEME", "purpose": "SHOWCASE", "iconName": "window-maximize"},
    "ia": {"category": "DEV", "purpose": "SAAS", "iconName": "robot"},
    "technique": {"category": "API", "purpose": "WEBSITE", "iconName": "plug"},
    "site-contenu": {"category": "THEME", "purpose": "WEBSITE", "iconName": "paint-brush"},
    "maintenance": {"category": "DEV", "purpose": "WEBSITE", "iconName": "shield-alt"},
}

FA_ICON_TO_FACTURIO: dict[str, str] = {
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
}


def _category_key(entry: dict, parent: dict | None) -> str:
    source = parent if parent else entry
    return (source.get("category") or "technique").strip()


def product_meta(entry: dict, parent: dict | None = None) -> dict[str, str]:
    cat = _category_key(entry, parent)
    meta = dict(FACTURIO_META_BY_CATEGORY.get(cat, FACTURIO_META_BY_CATEGORY["technique"]))
    source = parent if parent else entry
    fa = (source.get("icon") or "").strip()
    if fa in FA_ICON_TO_FACTURIO:
        meta["iconName"] = FA_ICON_TO_FACTURIO[fa]
    return meta


def estimate_hours(sku: str, price_eur: int, category: str) -> int:
    if sku in ESTIMATED_HOURS_BY_SKU:
        return ESTIMATED_HOURS_BY_SKU[sku]
    if price_eur <= 0:
        return 2
    if category == "maintenance" and price_eur < 80:
        return 1
    if price_eur < 100:
        return 2
    if price_eur < 300:
        return 6
    if price_eur < 600:
        return 10
    if price_eur < 1000:
        return 16
    if price_eur < 1500:
        return 24
    return 32


def _split_int(total: int, parts: int) -> list[int]:
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


def _livrable_labels(entry: dict, parent: dict | None, name: str) -> list[str]:
    explicit = entry.get("facturio_livrables")
    if isinstance(explicit, list) and explicit:
        labels: list[str] = []
        for item in explicit:
            if isinstance(item, dict) and item.get("livrable"):
                labels.append(str(item["livrable"]).strip())
            elif isinstance(item, str) and item.strip():
                labels.append(item.strip())
        if labels:
            return labels[:12]

    labels = []
    for key in ("includes", "benefits"):
        raw = entry.get(key)
        if (not raw or not isinstance(raw, list)) and parent:
            raw = parent.get(key)
        if not isinstance(raw, list):
            continue
        for item in raw:
            if isinstance(item, str) and item.strip():
                labels.append(item.strip()[:200])
    if labels:
        return labels[:12]

    desc = (entry.get("description") or entry.get("short_description") or name).strip()
    return [desc[:200] if desc else name[:200]]


def build_livrables(
    entry: dict,
    sku: str,
    name: str,
    price_eur: int,
    parent: dict | None = None,
) -> list[dict[str, Any]]:
    """Tableau { livrable, montant, heures } pour PATCH/POST produit."""
    if sku in LIVRABLES_BY_SKU:
        return [dict(item) for item in LIVRABLES_BY_SKU[sku]]

    explicit = entry.get("facturio_livrables")
    if isinstance(explicit, list) and explicit and isinstance(explicit[0], dict):
        out: list[dict[str, Any]] = []
        for item in explicit:
            if not isinstance(item, dict):
                continue
            label = str(item.get("livrable") or "").strip()
            if not label:
                continue
            out.append({
                "livrable": label[:200],
                "montant": int(item.get("montant") or 0),
                "heures": int(item.get("heures") or 0),
            })
        if out:
            return out

    category = _category_key(entry, parent)
    total_hours = estimate_hours(sku, price_eur, category)
    labels = _livrable_labels(entry, parent, name)
    montants = _split_int(max(0, price_eur), len(labels))
    heures = _split_int(max(1, total_hours), len(labels))

    return [
        {
            "livrable": label,
            "montant": montants[i],
            "heures": heures[i],
        }
        for i, label in enumerate(labels)
    ]


def build_tech_stack(sku: str, category: str) -> dict[str, list[str]]:
    """techStack API Facturio : { languages, ai }."""
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
    parts: list[str] = []
    tagline = (entry.get("tagline") or (parent or {}).get("tagline") or "").strip()
    if tagline:
        parts.append(tagline)

    long_desc = (entry.get("description") or (parent or {}).get("description") or "").strip()
    short = (entry.get("short_description") or "").strip()
    if long_desc:
        parts.append(long_desc)
    elif short:
        parts.append(short)

    promo = (entry.get("promo") or (parent or {}).get("promo") or "").strip()
    if promo:
        parts.append(promo)

    price_note = (entry.get("price_note") or (parent or {}).get("price_note") or "").strip()
    price_label = (entry.get("price_label") or (parent or {}).get("price_label") or "Forfait").strip()
    if price_eur > 0:
        price_line = f"{price_label} : {price_eur} EUR HT"
        if price_note:
            price_line += f" — {price_note}"
        parts.append(price_line)

    if slug:
        parts.append(f"Catalogue : danielcraft.fr/prestations/{slug}/")

    text = "\n\n".join(p for p in parts if p)
    return text[:2000] if text else name[:500]


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
    total_hours = sum(int(x.get("heures") or 0) for x in livrables)

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
    total_h = sum(int(x.get("heures") or 0) for x in livrables)
    return f"{len(livrables)} livrable(s), {total_m} EUR HT, {total_h}h"
