# -*- coding: utf-8 -*-
"""Corrige accents manquants dans les chaines client de build.py."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "build.py"

PAIRS = [
    (
        "Le pack coute souvent moins cher qu'a l'unite",
        "Le pack coûte souvent moins cher qu'à l'unité",
    ),
    (
        "Combien de temps ca prend ?",
        "Combien de temps ça prend ?",
    ),
    (
        "Le delai calendaire depend de vos retours (textes, acces, validations).",
        "Le délai calendaire dépend de vos retours (textes, accès, validations).",
    ),
    (
        "On precise ensuite le planning ensemble.",
        "On précise ensuite le planning ensemble.",
    ),
    (
        "Que se passe-t-il apres la livraison ?",
        "Que se passe-t-il après la livraison ?",
    ),
    (
        "Livre a 0,50&nbsp;€ - packs moins cher qu'a l'unite (remise volume).",
        "Livre à 0,50&nbsp;€ - packs moins cher qu'à l'unité (remise volume).",
    ),
    (
        "PDF · envoi e-mail apres paiement",
        "PDF - envoi e-mail après paiement",
    ),
    (
        "PDF a telecharger tout de suite - sans paiement",
        "PDF à telecharger tout de suite - sans paiement",
    ),
    (
        "PDF envoye par e-mail apres paiement securise.",
        "PDF envoyé par e-mail après paiement sécurisé.",
    ),
    (
        "TTC - PDF envoye par e-mail apres paiement",
        "TTC - PDF envoyé par e-mail après paiement",
    ),
]


def main() -> None:
    """Applique les corrections d'accents."""
    text = TARGET.read_text(encoding="utf-8")
    total = 0
    for old, new in PAIRS:
        count = text.count(old)
        if count:
            text = text.replace(old, new)
            total += count
            print(f"ok {count}: {old[:48]}")
        else:
            print(f"miss: {old[:60]}")
    TARGET.write_text(text, encoding="utf-8", newline="\n")
    print(f"total={total}")


if __name__ == "__main__":
    main()
