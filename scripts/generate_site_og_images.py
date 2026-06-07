#!/usr/bin/env python3
"""
Genere les images Open Graph (1200x630) pour les pages du site (hors blog).

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
from typing import Iterable, Sequence

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("[ERREUR] pip install pillow")
    sys.exit(1)

BASE_DIR = Path(__file__).resolve().parent.parent
OG_DIR = BASE_DIR / "assets" / "images" / "og"
DATA_DIR = BASE_DIR / "src" / "data"

BRAND_RED = "#dc2626"
BG_PAGE = "#eef2f7"
BG_CARD = "#ffffff"
TEXT_DARK = "#111827"
TEXT_MUTED = "#6b7280"
TEXT_FOOTER = "#9ca3af"
BORDER = "#dbeafe"

CATEGORY_COLORS = {
    "identite": "#dc2626",
    "ia": "#2563eb",
    "technique": "#059669",
    "site-contenu": "#d97706",
    "maintenance": "#6366f1",
    "web": "#dc2626",
    "tools": "#2563eb",
    "mobile": "#7c3aed",
    "iot": "#0891b2",
    "specialized": "#be185d",
    "learning": "#ca8a04",
    "desktop": "#475569",
    "vitrine": "#dc2626",
    "default": "#dc2626",
}

STATIC_PAGES: list[dict] = [
    {
        "slug": "home",
        "badge": "Accueil",
        "title": "DanielCraft",
        "subtitle": "Site vitrine & visibilité Google — Metz & Lorraine",
        "chips": ["Sans jargon", "Devis e-mail", "Assistants IA"],
    },
    {
        "slug": "audit",
        "badge": "Audit",
        "title": "Audit de site web",
        "subtitle": "Gratuit par e-mail ou rapport premium à 199 € TTC",
        "chips": ["Visibilité", "Crédibilité", "Parcours visiteur"],
    },
    {
        "slug": "prestations",
        "badge": "Catalogue",
        "title": "Prestations web",
        "subtitle": "Site vitrine, Google, assistants intelligents, entretien",
        "chips": ["Prix indicatifs", "Pages détaillées", "Devis simple"],
    },
    {
        "slug": "vitrines",
        "badge": "Modèles",
        "title": "Sites par métier",
        "subtitle": "19 maquettes prêtes à personnaliser — démo live",
        "chips": ["Restaurant", "Commerce", "Professions libérales"],
    },
    {
        "slug": "processus",
        "badge": "Méthode",
        "title": "Comment je travaille",
        "subtitle": "Échange, devis, mise en ligne — à votre rythme",
        "chips": ["Transparent", "Sans jargon", "Accompagnement"],
    },
    {
        "slug": "metz",
        "badge": "Metz 57000",
        "title": "Création site web à Metz",
        "subtitle": "Artisans, commerces et indépendants en Lorraine",
        "chips": ["Site vitrine", "Visibilité", "Assistants IA"],
    },
    {
        "slug": "portfolio",
        "badge": "Réalisations",
        "title": "Portfolio DanielCraft",
        "subtitle": "Sites vitrines et outils livrés en Lorraine et en France",
        "chips": ["Sites web", "Outils métier", "Open source"],
    },
    {
        "slug": "projets",
        "badge": "Open source",
        "title": "Projets & code",
        "subtitle": "Applications web, mobile et outils publiés sur GitHub",
        "chips": ["TypeScript", "React", "Node.js"],
    },
    {
        "slug": "statistiques",
        "badge": "Chiffres",
        "title": "Statistiques",
        "subtitle": "Projets livrés, technologies et années d'expérience",
        "chips": ["Activité", "Technos", "Parcours"],
    },
    {
        "slug": "analyse",
        "badge": "Rapport",
        "title": "Analyse de site",
        "subtitle": "Performance, SEO et sécurité — lien partageable",
        "chips": ["Performance", "SEO", "Sécurité"],
    },
    {
        "slug": "desabonnement",
        "badge": "E-mail",
        "title": "Désabonnement",
        "subtitle": "Ne plus recevoir de prospection ou de relances",
        "chips": ["RGPD", "Préférences", "Contact"],
    },
    {
        "slug": "mentions-legales",
        "badge": "Légal",
        "title": "Mentions légales",
        "subtitle": "Éditeur, hébergeur et contact du site danielcraft.fr",
        "chips": ["SIRET", "Hébergeur", "Contact"],
    },
    {
        "slug": "cgv",
        "badge": "Légal",
        "title": "Conditions générales de vente",
        "subtitle": "Prestations web et services DanielCraft",
        "chips": ["Devis", "Livraison", "Garanties"],
    },
    {
        "slug": "cgu",
        "badge": "Légal",
        "title": "Conditions d'utilisation",
        "subtitle": "Utilisation du site danielcraft.fr",
        "chips": ["Site web", "Données", "Responsabilité"],
    },
    {
        "slug": "politique-confidentialite",
        "badge": "RGPD",
        "title": "Politique de confidentialité",
        "subtitle": "Données personnelles et cookies",
        "chips": ["RGPD", "Cookies", "Vos droits"],
    },
]


def _font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    paths = [
        Path("C:/Windows/Fonts/segoeuib.ttf"),
        Path("C:/Windows/Fonts/segoeui.ttf"),
        Path("C:/Windows/Fonts/arialbd.ttf"),
        Path("C:/Windows/Fonts/arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for p in paths:
        if p.is_file():
            try:
                return ImageFont.truetype(str(p), size)
            except OSError:
                continue
    return ImageFont.load_default()


def _wrap_lines(draw: ImageDraw.ImageDraw, text: str, font, max_width: int, max_lines: int = 2) -> list[str]:
    words = (text or "").split()
    if not words:
        return [""]
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        trial = " ".join(current + [word])
        if draw.textlength(trial, font=font) <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
            if len(lines) >= max_lines:
                break
    if current and len(lines) < max_lines:
        lines.append(" ".join(current))
    if len(lines) == max_lines and len(" ".join(words)) > len(" ".join(lines)):
        last = lines[-1]
        while last and draw.textlength(last + "…", font=font) > max_width:
            last = last[:-1]
        lines[-1] = (last.rstrip(".,; ") + "…") if last else "…"
    return lines or [""]


def render_og_card(
    *,
    title: str,
    subtitle: str = "",
    badge: str = "DanielCraft",
    color: str = BRAND_RED,
    chips: Sequence[str] | None = None,
    footer: str = "DanielCraft — Metz & Lorraine",
    width: int = 1200,
    height: int = 630,
) -> Image.Image:
    scale = width / 1200
    pad = int(48 * scale)
    font_title = _font(max(28, int(52 * scale)))
    font_sub = _font(max(16, int(28 * scale)))
    font_small = _font(max(14, int(22 * scale)))

    img = Image.new("RGB", (width, height), BG_PAGE)
    draw = ImageDraw.Draw(img)

    bar_h = max(8, int(10 * scale))
    draw.rectangle([0, 0, width, bar_h], fill=color)
    draw.rounded_rectangle(
        [pad, pad, width - pad, height - pad],
        radius=max(12, int(20 * scale)),
        fill=BG_CARD,
        outline=BORDER,
        width=max(1, int(2 * scale)),
    )

    inner_x = pad + int(24 * scale)
    badge_w = min(int(320 * scale), max(int(120 * scale), int(draw.textlength(badge[:24], font=font_small) + 32 * scale)))
    badge_h = int(52 * scale)
    draw.rounded_rectangle(
        [inner_x, pad + int(24 * scale), inner_x + badge_w, pad + int(24 * scale) + badge_h],
        radius=max(8, int(12 * scale)),
        fill=color,
    )
    draw.text((inner_x + int(16 * scale), pad + int(34 * scale)), badge[:24], fill="#ffffff", font=font_small)

    ty = pad + int(24 * scale) + badge_h + int(20 * scale)
    max_text_w = width - 2 * pad - int(48 * scale)
    for line in _wrap_lines(draw, title, font_title, max_text_w, 2):
        draw.text((inner_x, ty), line, fill=TEXT_DARK, font=font_title)
        ty += int(58 * scale)

    if subtitle:
        for line in _wrap_lines(draw, subtitle, font_sub, max_text_w, 2):
            draw.text((inner_x, ty), line, fill=TEXT_MUTED, font=font_sub)
            ty += int(34 * scale)

    chip_list = [c for c in (chips or []) if c][:3]
    if chip_list:
        cx = inner_x
        cy = height - pad - int(120 * scale)
        for chip in chip_list:
            label = chip[:22]
            cw = int(draw.textlength(label, font=font_small) + 28 * scale)
            ch = int(40 * scale)
            draw.rounded_rectangle(
                [cx, cy, cx + cw, cy + ch],
                radius=int(20 * scale),
                fill="#f8fafc",
                outline=color,
                width=max(1, int(2 * scale)),
            )
            draw.text((cx + int(14 * scale), cy + int(10 * scale)), label, fill=TEXT_DARK, font=font_small)
            cx += cw + int(14 * scale)

    draw.text((inner_x, height - pad - int(28 * scale)), footer[:60], fill=TEXT_FOOTER, font=font_small)
    return img


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
            color=CATEGORY_COLORS.get(cat, BRAND_RED),
            chips=[item.get("price_label") or "Forfait", "Devis e-mail"],
            footer="DanielCraft — Prestations web",
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
        )
        _save_jpg(img, out_dir / f"{slug}-1200x630.jpg", dry_run)
        count += 1
    return count


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
            color=CATEGORY_COLORS.get(cat, BRAND_RED),
            chips=techs or ["Open source"],
            footer="DanielCraft — Projets",
        )
        _save_jpg(img, out_dir / f"{slug}-1200x630.jpg", dry_run)
        count += 1
    return count


# Labels projets (alignés build.py)
CATEGORY_LABELS = {
    "web": "Web",
    "tools": "Outils",
    "mobile": "Mobile",
    "iot": "IoT",
    "specialized": "Spécialisé",
    "learning": "Apprentissage",
    "desktop": "Desktop",
}


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
