# -*- coding: utf-8 -*-
"""Corrige accents frequents dans JSON client (livres, prestations, vitrines)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    ROOT / "src" / "data" / "livres.json",
    ROOT / "api" / "data" / "livres.json",
    ROOT / "src" / "data" / "prestations.json",
    ROOT / "api" / "data" / "prestations.json",
    ROOT / "src" / "data" / "vitrines.json",
    ROOT / "api" / "data" / "vitrines.json",
]

# Remplacements ordonnes (plus longs d'abord si besoin)
PAIRS = [
    ("a l'unite", "à l'unité"),
    ("qu'a l'unite", "qu'à l'unité"),
    ("apres paiement", "après paiement"),
    ("apres validation", "après validation"),
    ("envoye par e-mail", "envoyé par e-mail"),
    ("envoyes par e-mail", "envoyés par e-mail"),
    ("a telecharger", "à télécharger"),
    ("telecharger", "télécharger"),
    ("demarrer", "démarrer"),
    ("Debutant", "Débutant"),
    ("debutant", "débutant"),
    ("Intermediaire", "Intermédiaire"),
    ("intermediaire", "intermédiaire"),
    ("securite", "sécurité"),
    ("Securite", "Sécurité"),
    ("cafe", "café"),
    ("Economie", "Économie"),
    ("matieres", "matières"),
    ("derives", "dérivés"),
    ("equipe", "équipe"),
    ("avancee", "avancée"),
    ("methodologie", "méthodologie"),
    ("Ideal ", "Idéal "),
    ("ideal ", "idéal "),
]


def main() -> None:
    """Applique les corrections d'accents sur les catalogues."""
    for path in TARGETS:
        if not path.is_file():
            print(f"skip missing {path}")
            continue
        text = path.read_text(encoding="utf-8")
        total = 0
        for old, new in PAIRS:
            n = text.count(old)
            if n:
                text = text.replace(old, new)
                total += n
        if total:
            path.write_text(text, encoding="utf-8", newline="\n")
        print(f"{path.relative_to(ROOT).as_posix()}: {total}")


if __name__ == "__main__":
    main()
