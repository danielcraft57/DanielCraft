# -*- coding: utf-8 -*-
"""Passe orthographe FR elargie (accents frequents) sur contenu src/."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROOTS = [
    ROOT / "src" / "pages",
    ROOT / "src" / "includes",
    ROOT / "src" / "data",
    ROOT / "api" / "data",
]

# Plus longs d'abord pour eviter les collisions partielles
PAIRS = [
    ("Pret a telecharger", "Prêt à télécharger"),
    ("Fichiers a telecharger", "Fichiers à télécharger"),
    ("PDF a telecharger", "PDF à télécharger"),
    ("a telecharger tout de suite", "à télécharger tout de suite"),
    ("a telecharger", "à télécharger"),
    ("tu telecharges", "tu télécharges"),
    ("si ca te parle", "si ça te parle"),
    ("Combien de temps ca prend", "Combien de temps ça prend"),
    ("python debutant", "python débutant"),
    ("points cles", "points clés"),
    ("lien recu par email", "lien reçu par email"),
    ("code unique recu", "code unique reçu"),
    ("Paiement securise", "Paiement sécurisé"),
    ("apres paiement", "après paiement"),
    ("apres validation", "après validation"),
    ("envoye par e-mail", "envoyé par e-mail"),
    ("envoyes par e-mail", "envoyés par e-mail"),
    ("a l'unite", "à l'unité"),
    ("qu'a l'unite", "qu'à l'unité"),
    ("demarrer", "démarrer"),
    ("Debutant", "Débutant"),
    ("debutant", "débutant"),
    ("Intermediaire", "Intermédiaire"),
    ("intermediaire", "intermédiaire"),
    ("Securite", "Sécurité"),
    ("securite", "sécurité"),
    ("securise", "sécurisé"),
    ("cafe", "café"),
    ("Economie", "Économie"),
    ("matieres", "matières"),
    ("derives", "dérivés"),
    ("equipe", "équipe"),
    ("avancee", "avancée"),
    ("methodologie", "méthodologie"),
    ("Ideal ", "Idéal "),
    ("ideal ", "idéal "),
    ("Recupere ", "Récupère "),
    ("delai ", "délai "),
    ("precise ", "précise "),
    ("depend ", "dépend "),
    # Attention: ne pas toucher aux slugs / attributs data-*-query=debutant etc.
]

# Ne pas modifier ces sous-chaines (slugs, attributs techniques)
SKIP_IF_CONTAINS = (
    "data-livres-search-query=",
    "data-livres-search-chip=",
    "pack-demarrer-",
    "service_slug",
    '"slug":',
)


def should_skip_line(line: str) -> bool:
    """Ignore les lignes techniques (slugs, chips de recherche)."""
    low = line.lower()
    return any(s in low for s in SKIP_IF_CONTAINS)


def fix_text(text: str) -> tuple[str, int]:
    """Applique les corrections ligne par ligne.

    @returns: (texte, nombre de remplacements)
    """
    lines = text.splitlines(keepends=True)
    total = 0
    out = []
    for line in lines:
        if should_skip_line(line):
            out.append(line)
            continue
        new = line
        for old, new_s in PAIRS:
            c = new.count(old)
            if c:
                new = new.replace(old, new_s)
                total += c
        out.append(new)
    return "".join(out), total


def main() -> None:
    """Parcourt src/data, pages, includes."""
    files = 0
    total = 0
    for base in ROOTS:
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.suffix.lower() not in {".html", ".json"}:
                continue
            # Skip embeds regenerables lourds? On les corrige aussi (source of truth elsewhere)
            try:
                original = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            fixed, n = fix_text(original)
            if n:
                path.write_text(fixed, encoding="utf-8", newline="\n")
                files += 1
                total += n
                print(f"{path.relative_to(ROOT).as_posix()}: {n}")
    print(f"files={files} replacements={total}")


if __name__ == "__main__":
    main()
