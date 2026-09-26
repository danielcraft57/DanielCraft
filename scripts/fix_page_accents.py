# -*- coding: utf-8 -*-
"""Corrige accents manquants sur pages telechargement / meta JSON."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FIXES = {
    "src/pages/bouquins-telechargement.json": [
        (
            "Recupere ton bouquin PDF avec ton code unique apres paiement.",
            "Récupère ton bouquin PDF avec ton code unique après paiement.",
        ),
    ],
    "src/pages/livres-telechargement.json": [
        (
            "Recupere ton livre PDF avec ton code unique apres paiement.",
            "Récupère ton livre PDF avec ton code unique après paiement.",
        ),
    ],
}


def main() -> None:
    """Applique les corrections."""
    for rel, pairs in FIXES.items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        for old, new in pairs:
            if old not in text:
                print(f"miss {rel}: {old[:40]}")
                continue
            text = text.replace(old, new)
            print(f"ok {rel}")
        path.write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
