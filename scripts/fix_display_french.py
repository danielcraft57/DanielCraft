# -*- coding: utf-8 -*-
"""Corrige orthographe des textes visibles livres/vitrines/prestations (pas les slugs)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Remplacements sur chaines affichables uniquement
TEXT_PAIRS: list[tuple[str, str]] = [
    ("Acces a vie au fichier envoyé", "Accès à vie au fichier envoyé"),
    ("Acces a vie au fichier envoye", "Accès à vie au fichier envoyé"),
    ("exercices et schemas", "exercices et schémas"),
    ("bons reflexes", "bons réflexes"),
    ("pedagogie", "pédagogie"),
    ("expliques simplement", "expliqués simplement"),
    ("expliques sans", "expliqués sans"),
    ("expliquees simplement", "expliquées simplement"),
    ("explique clairement", "expliqué clairement"),
    ("explique simplement", "expliqué simplement"),
    ("explique sans", "expliqué sans"),
    ("Meme pedagogie", "Même pédagogie"),
    ("Meme ", "Même "),
    ("roles Scrum", "rôles Scrum"),
    ("Le role ", "Le rôle "),
    ("Marches, produits", "Marchés, produits"),
    ("Apprends a ", "Apprends à "),
    (" et a la ", " et à la "),
    ("Ajoute des types a ", "Ajoute des types à "),
    (" et ecris ", " et écris "),
    ("pour debuter", "pour débuter"),
    ("Decouvre ", "Découvre "),
    ("memoire et", "mémoire et"),
    ("base de donnees", "base de données"),
    ("Passe a des", "Passe à des"),
    ("(idee)", "(idée)"),
    ("Fenetres,", "Fenêtres,"),
    ("Travailler a plusieurs", "Travailler à plusieurs"),
    ("mieux proteger", "mieux protéger"),
    ("modeles de menaces", "modèles de menaces"),
    ("et ethique", "et éthique"),
    ("ethique.", "éthique."),
    ("Regression,", "Régression,"),
    ("mecanismes,", "mécanismes,"),
    ("pieges.", "pièges."),
    ("cadre legal", "cadre légal"),
    ("presentations et", "présentations et"),
    ("vs iteratif", "vs itératif"),
    ("ceremonies,", "cérémonies,"),
    ("a eviter", "à éviter"),
    ("flex avance", "flex avancé"),
    ("composants reutilisables", "composants réutilisables"),
    ("A gouter", "À goûter"),
    ("a gouter", "à goûter"),
    ("au marche", "au marché"),
    ("tu goutes", "tu goûtes"),
    ("Chocolaterie a Metz", "Chocolaterie à Metz"),
    (" - a gouter", " - à goûter"),
    ("Livre a 0,50", "Livre à 0,50"),
    ("qu'a l'unite", "qu'à l'unité"),
    ("d'un cafe", "d'un café"),
    ("et securite", "et sécurité"),
    ("roles ", "rôles "),
    ("Preferer ", "Préférer "),
    ("un element ", "un élément "),
    ("(numero,", "(numéro,"),
]

# Champs JSON a corriger (pas slug / keywords / id)
DISPLAY_KEYS = {
    "title",
    "tagline",
    "short_description",
    "description",
    "price_note",
    "price_label",
    "seo_title",
    "seo_description",
    "promo",
    "excerpt",
    "urgency",
    "badge",
    "cta_label",
    "nav_label",
    "name",
    "label",
    "text",
    "q",
    "a",
    "page_description",
    "page_title",
    "raison",
    "phrase",
    "alternatives",
    "variantes",
}


def fix_string(value: str) -> str:
    """Applique les remplacements sur une chaine affichable."""
    out = value
    for old, new in TEXT_PAIRS:
        if old in out:
            out = out.replace(old, new)
    return out


def walk(node, *, in_display: bool = False):
    """Parcourt le JSON et corrige les chaines de champs affichables."""
    if isinstance(node, dict):
        out = {}
        for key, val in node.items():
            if key in {"slug", "service_slug", "keywords", "image", "href", "url", "icon", "id"}:
                out[key] = val
                continue
            if key in DISPLAY_KEYS:
                out[key] = walk(val, in_display=True)
            elif key in {"includes", "benefits", "before", "examples", "faq", "highlights", "categories", "items"}:
                out[key] = walk(val, in_display=True)
            else:
                out[key] = walk(val, in_display=False)
        return out
    if isinstance(node, list):
        return [walk(x, in_display=in_display) for x in node]
    if isinstance(node, str) and in_display:
        return fix_string(node)
    return node


def fix_file(path: Path) -> int:
    """Corrige un fichier JSON. Retourne une estimation de changements."""
    raw = path.read_text(encoding="utf-8")
    data = json.loads(raw)
    fixed = walk(data)
    new_raw = json.dumps(fixed, ensure_ascii=False, indent=2) + "\n"
    # Compter diffs approximatifs via paires
    n = 0
    for old, new in TEXT_PAIRS:
        n += raw.count(old)
    if new_raw != raw:
        path.write_text(new_raw, encoding="utf-8", newline="\n")
    return n


def fix_html_snippets(path: Path) -> int:
    """Corrige quelques locutions dans un HTML genere / template."""
    if not path.is_file():
        return 0
    text = path.read_text(encoding="utf-8")
    n = 0
    out = text
    for old, new in TEXT_PAIRS:
        c = out.count(old)
        if c:
            out = out.replace(old, new)
            n += c
    if n:
        try:
            path.write_text(out, encoding="utf-8", newline="\n")
        except OSError as exc:
            print(f"[SKIP] {path.name}: {exc}")
            return 0
    return n


def main() -> None:
    """Corrige catalogues + quelques pages HTML."""
    targets = [
        ROOT / "src" / "data" / "livres.json",
        ROOT / "api" / "data" / "livres.json",
        ROOT / "src" / "data" / "vitrines.json",
        ROOT / "api" / "data" / "vitrines.json",
        ROOT / "src" / "data" / "prestations.json",
        ROOT / "api" / "data" / "prestations.json",
        ROOT / "src" / "data" / "vocabulaire-client.json",
    ]
    for path in targets:
        if path.is_file():
            n = fix_file(path)
            print(f"{path.relative_to(ROOT).as_posix()}: ~{n}")

    html_targets = [
        ROOT / "src" / "pages" / "livre-detail.html",
        ROOT / "src" / "pages" / "bouquins.html",
        ROOT / "src" / "pages" / "index.html",
        ROOT / "src" / "includes" / "livres-deal-week.html",
        ROOT / "src" / "includes" / "nos-offres-commerce-intro.html",
    ]
    for path in html_targets:
        n = fix_html_snippets(path)
        if n:
            print(f"{path.relative_to(ROOT).as_posix()}: {n}")


if __name__ == "__main__":
    main()
