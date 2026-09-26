# -*- coding: utf-8 -*-
"""Corrige fautes d'accents / orthographe frequentes sur pages et meta visibles."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Fichiers pages / includes / meta (pas tout livres.json ici)
TARGETS = [
    ROOT / "src" / "pages",
    ROOT / "src" / "includes",
]

PAIRS = [
    ("Pret a telecharger", "Prêt à télécharger"),
    ("Pret à telecharger", "Prêt à télécharger"),
    ("Fichiers a telecharger", "Fichiers à télécharger"),
    ("PDF a telecharger", "PDF à télécharger"),
    ("a telecharger", "à télécharger"),
    ("tu telecharges", "tu télécharges"),
    ("si ca te parle", "si ça te parle"),
    ("python debutant", "python débutant"),
    ("livres gratuits a telecharger", "livres gratuits à télécharger"),
    ("le reste a prix d'appel", "le reste à prix d'appel"),
    ("points cles", "points clés"),
    ("lien recu par email", "lien reçu par email"),
    ("Paiement securise", "Paiement sécurisé"),
    ("Recupere ", "Récupère "),
    ("apres paiement", "après paiement"),
]


def main() -> None:
    """Applique les corrections sur les fichiers texte des pages."""
    changed_files = 0
    total = 0
    for base in TARGETS:
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.suffix.lower() not in {".html", ".json"}:
                continue
            text = path.read_text(encoding="utf-8")
            n = 0
            for old, new in PAIRS:
                c = text.count(old)
                if c:
                    text = text.replace(old, new)
                    n += c
            if n:
                path.write_text(text, encoding="utf-8", newline="\n")
                changed_files += 1
                total += n
                print(f"{path.relative_to(ROOT).as_posix()}: {n}")
    print(f"files={changed_files} replacements={total}")


if __name__ == "__main__":
    main()
