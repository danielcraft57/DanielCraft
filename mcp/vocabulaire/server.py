#!/usr/bin/env python3
"""MCP DanielCraft - vocabulaire client (copy commerce Grand Est)."""

from __future__ import annotations

import json
import re
from pathlib import Path

from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parents[2]
LEXIQUE_PATH = ROOT / "src" / "data" / "vocabulaire-client.json"

mcp = FastMCP("danielcraft-vocabulaire")


def _load_lexique() -> dict:
    with LEXIQUE_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


@mcp.tool()
def check_copy(text: str) -> dict:
    """Detecte les formulations interdites ou trop vagues dans un texte marketing client."""
    lexique = _load_lexique()
    haystack = _normalize(text)
    hits: list[dict] = []

    for entry in lexique.get("interdit", []):
        phrases = [entry["phrase"], *entry.get("variantes", [])]
        for phrase in phrases:
            if _normalize(phrase) in haystack:
                hits.append(
                    {
                        "id": entry["id"],
                        "phrase": phrase,
                        "raison": entry["raison"],
                        "alternatives": entry.get("alternatives", []),
                    }
                )
                break

    return {
        "ok": len(hits) == 0,
        "hits": hits,
        "text_length": len(text),
    }


@mcp.tool()
def get_alternatives(phrase: str) -> dict:
    """Retourne des formulations approuvees pour remplacer une phrase vague ou interdite."""
    lexique = _load_lexique()
    needle = _normalize(phrase)

    for entry in lexique.get("interdit", []):
        candidates = [entry["phrase"], *entry.get("variantes", [])]
        if any(_normalize(c) == needle or _normalize(c) in needle for c in candidates):
            return {
                "found": True,
                "id": entry["id"],
                "phrase": entry["phrase"],
                "raison": entry["raison"],
                "alternatives": entry.get("alternatives", []),
            }

    return {
        "found": False,
        "phrase": phrase,
        "message": "Pas dans la liste interdite. Voir list_benefits pour des formulations approuvees.",
    }


@mcp.tool()
def list_benefits(category: str = "all") -> dict:
    """Liste les formulations benefice par categorie (telephone, google, vitesse, securite, sur_mesure, delai, all)."""
    lexique = _load_lexique()
    benefits: dict[str, list[str]] = lexique.get("benefices", {})

    if category == "all":
        return {"benefices": benefits}

    key = category.strip().lower()
    if key not in benefits:
        return {
            "error": f"Categorie inconnue: {category}",
            "categories": sorted(benefits.keys()),
        }

    return {"category": key, "phrases": benefits[key]}


@mcp.tool()
def list_banned() -> dict:
    """Liste toutes les formulations a eviter sur le site client."""
    lexique = _load_lexique()
    banned = [
        {
            "id": e["id"],
            "phrase": e["phrase"],
            "variantes": e.get("variantes", []),
            "raison": e["raison"],
        }
        for e in lexique.get("interdit", [])
    ]
    return {"count": len(banned), "interdit": banned}


@mcp.tool()
def get_zone_guidance(zone: str) -> dict:
    """Conseils et exemples pour une zone de page (hero_h1, hero_lead, checklist)."""
    lexique = _load_lexique()
    zones: dict = lexique.get("zones", {})
    key = zone.strip().lower()

    if key not in zones:
        return {"error": f"Zone inconnue: {zone}", "zones": sorted(zones.keys())}

    return {"zone": key, **zones[key]}


if __name__ == "__main__":
    mcp.run()
