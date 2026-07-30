#!/usr/bin/env python3
"""
Genere les images Open Graph (1200x630) pour les pages du site (hors blog).

Style cartoon / BD, charte bleu DanielCraft (#4da9d6, #0f3550).

Usage (racine du projet) :
    python scripts/generate_site_og_images.py
    python scripts/generate_site_og_images.py --only home audit metz
    python scripts/generate_site_og_images.py --dry-run

Sortie : assets/images/og/ (+ sous-dossiers prestations/, vitrines/, projets/)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from _og_cartoon import (  # noqa: E402
    CATEGORY_COLORS,
    PRESTATION_SCENES,
    PROJECT_SCENES,
    STATIC_SCENES,
    render_og_card,
)

try:
    from PIL import Image
except ImportError:
    print("[ERREUR] pip install pillow numpy")
    sys.exit(1)

BASE_DIR = _SCRIPT_DIR.parent
OG_DIR = BASE_DIR / "assets" / "images" / "og"
DATA_DIR = BASE_DIR / "src" / "data"

STATIC_PAGES: list[dict] = [
    {
        "slug": "home",
        "badge": "Accueil",
        "title": "DanielCraft",
        "subtitle": "Site vitrine & visibilité Google — Metz & Lorraine",
        "chips": ["Sans jargon", "Devis e-mail"],
        "cta": "Demander un devis →",
    },
    {
        "slug": "audit",
        "badge": "Audit",
        "title": "Audit de site web",
        "subtitle": "Gratuit par e-mail ou rapport premium à 199 € TTC",
        "chips": ["Visibilité", "Crédibilité"],
        "cta": "Audit gratuit →",
    },
    {
        "slug": "prestations",
        "badge": "Catalogue",
        "title": "Prestations web",
        "subtitle": "Site vitrine, Google, assistants IA, entretien",
        "chips": ["Tarifs HT", "Devis simple"],
        "cta": "Voir le catalogue →",
    },
    {
        "slug": "vitrines",
        "badge": "Modèles",
        "title": "Sites par métier",
        "subtitle": "19 maquettes prêtes à personnaliser — démo live",
        "chips": ["Restaurant", "Démo live"],
        "cta": "Voir les modèles →",
    },
    {
        "slug": "processus",
        "badge": "Méthode",
        "title": "Comment je travaille",
        "subtitle": "Échange, devis, mise en ligne — à votre rythme",
        "chips": ["Transparent", "Sans jargon"],
        "cta": "Découvrir →",
    },
    {
        "slug": "metz",
        "badge": "Metz 57000",
        "title": "Création site web à Metz",
        "subtitle": "Artisans, commerces et indépendants en Lorraine",
        "chips": ["Site vitrine", "Visibilité Google"],
        "cta": "Devis Metz →",
    },
    {
        "slug": "portfolio",
        "badge": "Réalisations",
        "title": "Portfolio DanielCraft",
        "subtitle": "Sites vitrines et outils livrés en Lorraine et en France",
        "chips": ["Sites web", "Open source"],
        "cta": "Voir les projets →",
    },
    {
        "slug": "projets",
        "badge": "Open source",
        "title": "Projets & code",
        "subtitle": "Applications web, mobile et outils publiés sur GitHub",
        "chips": ["TypeScript", "React"],
        "cta": "Explorer le code →",
    },
    {
        "slug": "statistiques",
        "badge": "Chiffres",
        "title": "Statistiques",
        "subtitle": "Projets livrés, technologies et activité depuis juillet 2011",
        "chips": ["Activité", "Technos"],
        "cta": "En savoir plus →",
    },
    {
        "slug": "analyse",
        "badge": "Rapport",
        "title": "Analyse de site",
        "subtitle": "Performance, SEO et sécurité — lien partageable",
        "chips": ["Performance", "SEO"],
        "cta": "Voir un rapport →",
    },
    {
        "slug": "desabonnement",
        "badge": "E-mail",
        "title": "Désabonnement",
        "subtitle": "Ne plus recevoir de prospection ou de relances",
        "chips": ["RGPD", "Contact"],
        "cta": "Gérer mes préférences →",
    },
    {
        "slug": "mentions-legales",
        "badge": "Légal",
        "title": "Mentions légales",
        "subtitle": "Éditeur, hébergeur et contact du site danielcraft.fr",
        "chips": ["SIRET", "Contact"],
        "cta": "Consulter →",
    },
    {
        "slug": "cgv",
        "badge": "Légal",
        "title": "Conditions générales de vente",
        "subtitle": "Prestations web et services DanielCraft",
        "chips": ["Devis", "Livraison"],
        "cta": "Consulter →",
    },
    {
        "slug": "cgu",
        "badge": "Légal",
        "title": "Conditions d'utilisation",
        "subtitle": "Utilisation du site danielcraft.fr",
        "chips": ["Site web", "Données"],
        "cta": "Consulter →",
    },
    {
        "slug": "politique-confidentialite",
        "badge": "RGPD",
        "title": "Politique de confidentialité",
        "subtitle": "Données personnelles et cookies",
        "chips": ["RGPD", "Cookies"],
        "cta": "Consulter →",
    },
]


def _save_jpg(img: Image.Image, path: Path, dry_run: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if dry_run:
        print(f"[dry-run] {path.relative_to(BASE_DIR)}")
        return
    img.save(path, "JPEG", quality=88, optimize=True, progressive=True)
    print(f"[OK] {path.relative_to(BASE_DIR)}")


def _load_json(name: str) -> dict | list:
    with open(DATA_DIR / name, encoding="utf-8") as f:
        return json.load(f)


def _prestation_scene(slug: str, category: str) -> str:
    if "visibilite" in slug or "google" in slug or "referencement" in slug:
        return "visibilite"
    if "eco" in slug or "allege" in slug:
        return "browser"
    return PRESTATION_SCENES.get(category, "browser")


def generate_static(only: set[str] | None, dry_run: bool) -> int:
    count = 0
    for page in STATIC_PAGES:
        slug = page["slug"]
        if only and slug not in only and "static" not in only:
            continue
        img = render_og_card(
            title=page["title"],
            subtitle=page["subtitle"],
            badge=page["badge"],
            chips=page.get("chips"),
            scene=STATIC_SCENES.get(slug, "browser"),
            cta=page.get("cta", "En savoir plus →"),
        )
        _save_jpg(img, OG_DIR / f"{slug}-1200x630.jpg", dry_run)
        count += 1
    return count


def generate_prestations(only: set[str] | None, dry_run: bool) -> int:
    data = _load_json("prestations.json")
    cats = {c["id"]: c.get("title", c["id"]) for c in data.get("categories", [])}
    count = 0
    out_dir = OG_DIR / "prestations"
    for item in data.get("items", []):
        if not item.get("has_page"):
            continue
        slug = (item.get("slug") or "").strip()
        if not slug:
            continue
        if only and slug not in only and "prestations" not in only:
            continue
        cat = item.get("category") or "default"
        badge = cats.get(cat, "Prestation")[:24]
        img = render_og_card(
            title=(item.get("title") or slug).strip(),
            subtitle=(item.get("tagline") or item.get("short_description") or "").strip(),
            badge=badge,
            color=CATEGORY_COLORS.get(cat, CATEGORY_COLORS["default"]),
            chips=[item.get("price_label") or "Forfait", "Devis e-mail"],
            footer="DanielCraft — Prestations web",
            scene=_prestation_scene(slug, cat),
            cta="Demander un devis →",
        )
        _save_jpg(img, out_dir / f"{slug}-1200x630.jpg", dry_run)
        count += 1
    return count


def generate_vitrines(only: set[str] | None, dry_run: bool) -> int:
    data = _load_json("vitrines.json")
    count = 0
    out_dir = OG_DIR / "vitrines"
    for item in data.get("items", []):
        slug = (item.get("slug") or "").strip()
        if not slug:
            continue
        if only and slug not in only and "vitrines" not in only:
            continue
        price = item.get("price_eur") or item.get("price") or ""
        chips = ["Démo live", "Mobile"]
        if price:
            chips.insert(0, f"À partir de {price} € HT")
        img = render_og_card(
            title=(item.get("title") or slug).strip(),
            subtitle=(item.get("tagline") or item.get("excerpt") or "").strip(),
            badge="Modèle web",
            color=CATEGORY_COLORS["vitrine"],
            chips=chips,
            footer="DanielCraft — Modèles de sites",
            scene="templates",
            cta="Voir la démo →",
        )
        _save_jpg(img, out_dir / f"{slug}-1200x630.jpg", dry_run)
        count += 1
    return count


CATEGORY_LABELS = {
    "web": "Web",
    "tools": "Outils",
    "mobile": "Mobile",
    "iot": "IoT",
    "specialized": "Spécialisé",
    "learning": "Apprentissage",
    "desktop": "Desktop",
}


def generate_projets(only: set[str] | None, dry_run: bool) -> int:
    projects = _load_json("projects.json")
    if not isinstance(projects, list):
        return 0
    count = 0
    out_dir = OG_DIR / "projets"
    for p in projects:
        slug = (p.get("slug") or p.get("id") or "").strip()
        if not slug:
            continue
        if only and slug not in only and "projets" not in only:
            continue
        cat = p.get("category") or "default"
        techs = (p.get("technologies") or [])[:2]
        img = render_og_card(
            title=(p.get("title") or slug).strip(),
            subtitle=(p.get("description") or "")[:100],
            badge=CATEGORY_LABELS.get(cat, cat.title()) if isinstance(cat, str) else "Projet",
            color=CATEGORY_COLORS.get(cat, CATEGORY_COLORS["default"]),
            chips=techs or ["Open source"],
            footer="DanielCraft — Projets",
            scene=PROJECT_SCENES.get(cat, "code"),
            cta="Voir le projet →",
        )
        _save_jpg(img, out_dir / f"{slug}-1200x630.jpg", dry_run)
        count += 1
    return count


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Genere les images OG du site (hors blog)")
    parser.add_argument(
        "--only",
        nargs="*",
        help="Filtrer : slugs (home, audit…) ou groupes static, prestations, vitrines, projets",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)
    only = set(args.only) if args.only else None

    total = 0
    total += generate_static(only, args.dry_run)
    total += generate_prestations(only, args.dry_run)
    total += generate_vitrines(only, args.dry_run)
    total += generate_projets(only, args.dry_run)

    print(f"\n[OK] {total} image(s) OG {'simulee(s)' if args.dry_run else 'generee(s)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
