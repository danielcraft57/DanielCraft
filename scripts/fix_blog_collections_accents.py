# -*- coding: utf-8 -*-
"""Corrige accents dans meta collections blog + titres/excerpts legers."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = ROOT / "blog" / "content" / "collections"
ARTICLES = ROOT / "blog" / "content" / "articles"

PAIRS = [
    ("apres", "après"),
    ("Apres", "Après"),
    ("securite", "sécurité"),
    ("Securite", "Sécurité"),
    ("donnees", "données"),
    ("Donnees", "Données"),
    ("demarrer", "démarrer"),
    ("Demarrer", "Démarrer"),
    ("debutant", "débutant"),
    ("Debutant", "Débutant"),
    ("qualite", "qualité"),
    ("Qualite", "Qualité"),
    ("delai", "délai"),
    ("Delai", "Délai"),
    ("expliques", "expliqués"),
    ("ethique", "éthique"),
    ("Ethique", "Éthique"),
    ("numero", "numéro"),
    ("schemas", "schémas"),
    ("Acces", "Accès"),
    ("acces", "accès"),
]


def fix_text(s: str) -> str:
    """Remplace les formes sans accent dans une chaine."""
    out = s
    for old, new in PAIRS:
        out = re.sub(rf"\b{re.escape(old)}\b", new, out)
    return out


def main() -> None:
    """Corrige collections JSON (title/description) et laisse les articles pour une passe ciblee."""
    n_files = 0
    n_hits = 0
    if COLLECTIONS.is_dir():
        for path in COLLECTIONS.glob("*.json"):
            data = json.loads(path.read_text(encoding="utf-8"))
            changed = False
            for key in ("title", "description", "name", "summary", "excerpt"):
                if key in data and isinstance(data[key], str):
                    fixed = fix_text(data[key])
                    if fixed != data[key]:
                        data[key] = fixed
                        changed = True
                        n_hits += 1
            if changed:
                path.write_text(
                    json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                    newline="\n",
                )
                n_files += 1
                print(path.name)
    print(f"collections_files={n_files} fields={n_hits}")


if __name__ == "__main__":
    main()
