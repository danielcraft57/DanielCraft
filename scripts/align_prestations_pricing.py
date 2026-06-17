#!/usr/bin/env python3
"""Aligne prix et heures estimées sur prestations.json (repères marché TPE / Lorraine)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRESTATIONS_JSON = ROOT / "src" / "data" / "prestations.json"

# Prix HT + heures (solo, hors réunions client légères).
# Taux effectif cible : 55–65 €/h ; offres « entry » volontairement sous le marché national.
ALIGNMENT: dict[str, dict] = {
    "site-vitrine": {"price_eur": 490, "estimated_hours": 9, "price_tier": "entry"},
    "site-vitrine-eco": {"price_eur": 490, "estimated_hours": 9, "price_tier": "entry"},
    "identite-harmonieuse": {"price_eur": 990, "estimated_hours": 16},
    "visibilite-complete": {"price_eur": 749, "estimated_hours": 12},
    "referencement-google": {"price_eur": 329, "estimated_hours": 5},
    "visible-assistants-ia": {"price_eur": 490, "estimated_hours": 8},
    "repondeur-intelligent": {"price_eur": 1190, "estimated_hours": 18},
    "aide-emails-clients": {"price_eur": 1290, "estimated_hours": 20},
    "entretien-mensuel": {
        "price_eur": 45,
        "estimated_hours": 1,
        "hours_period": "month",
        "price_tier": "entry",
    },
    "ia-contenus": {"price_eur": 590, "estimated_hours": 10},
    "ia-redaction": {"price_eur": 490, "estimated_hours": 7},
    "ia-analyse": {"price_eur": 1490, "estimated_hours": 22},
    "ia-boutique": {"price_eur": 1690, "estimated_hours": 24},
    "ia-automatisation": {"price_eur": 1290, "estimated_hours": 20},
    "ia-maint-mensuelle": {"price_eur": 69, "estimated_hours": 1, "hours_period": "month"},
    "ia-evolution": {"price_eur": 350, "estimated_hours": 5},
    "ia-audit": {"price_eur": 390, "estimated_hours": 6},
    "conseil-projet": {"price_eur": 390, "estimated_hours": 6},
    "connexion-crm": {"price_eur": 349, "estimated_hours": 5},
    "transfert-donnees": {"price_eur": 390, "estimated_hours": 6},
    "liaison-outils": {"price_eur": 199, "estimated_hours": 3},
    "rapport-vitesse": {"price_eur": 129, "estimated_hours": 2, "price_tier": "entry"},
    "page-supplementaire": {"price_eur": 69, "estimated_hours": 1, "price_tier": "entry"},
    "formulaire-sur-mesure": {"price_eur": 119, "estimated_hours": 2},
    "nouveau-look": {"price_eur": 390, "estimated_hours": 6},
    "maj-contenus": {"price_eur": 275, "estimated_hours": 5},
    "hebergement-domaine": {"price_eur": 89, "estimated_hours": 1},
    "sauvegardes-securite": {"price_eur": 119, "estimated_hours": 2},
    "https-site": {"price_eur": 49, "estimated_hours": 1, "price_tier": "entry"},
    "support-mensuel": {
        "price_eur": 29,
        "estimated_hours": 0.5,
        "hours_period": "month",
        "price_tier": "entry",
    },
    "depannage-2h": {"price_eur": 129, "estimated_hours": 2},
    "accompagnement-heure": {"price_eur": 59, "estimated_hours": 1},
    "support-prioritaire": {"price_eur": 69, "estimated_hours": 1},
    "audit-eco-numerique": {"price_eur": 149, "estimated_hours": 2.5, "price_tier": "entry"},
    "alleger-medias": {"price_eur": 199, "estimated_hours": 3.5},
    "site-allege": {"price_eur": 349, "estimated_hours": 6},
    "page-engagement-numerique": {"price_eur": 89, "estimated_hours": 1.5, "price_tier": "entry"},
    "suivi-eco-mensuel": {
        "price_eur": 35,
        "estimated_hours": 0.5,
        "hours_period": "month",
        "price_tier": "entry",
    },
    "atelier-eco-web": {"price_eur": 129, "estimated_hours": 2},
}

ADDON_ALIGNMENT: dict[str, dict[str, dict]] = {
    "site-vitrine": {
        "page_extra": {"price_eur": 69},
        "form_advanced": {"price_eur": 119},
    },
    "repondeur-intelligent": {"maint_ia": {"price_eur": 69}},
    "alleger-medias": {"images_extra": {"price_eur": 49}},
}

PRICE_NOTE_UPDATES: dict[str, str] = {
    "site-vitrine": "Forfait TPE — jusqu'à 5 pages",
    "site-vitrine-eco": "Forfait TPE — site sobre dès la création",
    "audit-eco-numerique": "Bilan express (pas un audit RGESN complet)",
    "referencement-google": "Audit léger + corrections prioritaires",
    "repondeur-intelligent": "Assistant FAQ sur votre site",
    "connexion-crm": "Connecteur simple — devis si ERP complexe",
    "liaison-outils": "Première liaison — chaque flux supplémentaire en sus",
}


def main() -> None:
    data = json.loads(PRESTATIONS_JSON.read_text(encoding="utf-8"))
    updated = 0
    for item in data.get("items", []):
        slug = item.get("slug", "")
        if slug not in ALIGNMENT:
            continue
        spec = ALIGNMENT[slug]
        item["price_eur"] = spec["price_eur"]
        item["estimated_hours"] = spec["estimated_hours"]
        if "hours_period" in spec:
            item["estimated_hours_period"] = spec["hours_period"]
        elif "estimated_hours_period" in item:
            del item["estimated_hours_period"]
        if "price_tier" in spec:
            item["price_tier"] = spec["price_tier"]
        elif "price_tier" in item:
            del item["price_tier"]
        if slug in PRICE_NOTE_UPDATES:
            item["price_note"] = PRICE_NOTE_UPDATES[slug]
        for addon in item.get("addons") or []:
            aid = addon.get("id", "")
            if slug in ADDON_ALIGNMENT and aid in ADDON_ALIGNMENT[slug]:
                addon["price_eur"] = ADDON_ALIGNMENT[slug][aid]["price_eur"]
        updated += 1

    PRESTATIONS_JSON.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Mis à jour : {updated} prestations dans {PRESTATIONS_JSON}")


if __name__ == "__main__":
    main()
