# -*- coding: utf-8 -*-
"""Passe orthographe / accents francais sur contenus visibles du site.

Remplacements prudents (mots entiers / locutions courantes).
Ne touche pas aux slugs, URLs, classes CSS, ni aux fichiers purement techniques.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# (pattern regex, remplacement) - ordre : plus specifique d'abord
REPLACEMENTS: list[tuple[str, str]] = [
    # Locutions frequentes
    (r"\bPret a telecharger\b", "Prêt à télécharger"),
    (r"\bPret à telecharger\b", "Prêt à télécharger"),
    (r"\ba telecharger\b", "à télécharger"),
    (r"\bA telecharger\b", "À télécharger"),
    (r"\bPDF a telecharger\b", "PDF à télécharger"),
    (r"\btelecharges\b", "télécharges"),
    (r"\btelecharger\b", "télécharger"),
    (r"\bTelecharger\b", "Télécharger"),
    (r"\btelechargeable\b", "téléchargeable"),
    (r"\btelechargement\b", "téléchargement"),
    (r"\bTelechargement\b", "Téléchargement"),
    (r"\bapres paiement\b", "après paiement"),
    (r"\bapres validation\b", "après validation"),
    (r"\bapres la\b", "après la"),
    (r"\bapres le\b", "après le"),
    (r"\bApres\b", "Après"),
    (r"\bapres\b", "après"),
    (r"\brecu par\b", "reçu par"),
    (r"\brecu\b", "reçu"),
    (r"\bRecu\b", "Reçu"),
    (r"\bRecupere\b", "Récupère"),
    (r"\brecupere\b", "récupère"),
    (r"\bsecurise\b", "sécurisé"),
    (r"\bSecurise\b", "Sécurisé"),
    (r"\bsecurisee\b", "sécurisée"),
    (r"\bsecurite\b", "sécurité"),
    (r"\bSecurite\b", "Sécurité"),
    (r"\benvoye par\b", "envoyé par"),
    (r"\benvoyes par\b", "envoyés par"),
    (r"\benvoye\b", "envoyé"),
    (r"\benvoyes\b", "envoyés"),
    (r"\ba l'unite\b", "à l'unité"),
    (r"\bqu'a l'unite\b", "qu'à l'unité"),
    (r"\ba l'unité\b", "à l'unité"),
    (r"\bdemarrer\b", "démarrer"),
    (r"\bDemarrer\b", "Démarrer"),
    (r"\bdebutant\b", "débutant"),
    (r"\bDebutant\b", "Débutant"),
    (r"\bintermediaire\b", "intermédiaire"),
    (r"\bIntermediaire\b", "Intermédiaire"),
    (r"\bdelai\b", "délai"),
    (r"\bDelai\b", "Délai"),
    (r"\bdelais\b", "délais"),
    (r"\bpoints cles\b", "points clés"),
    (r"\bcles\b", "clés"),  # prudent : peut trop matcher - on limite plus bas
    (r"\bcafe\b", "café"),
    (r"\bEconomie\b", "Économie"),
    (r"\beconomie\b", "économie"),
    (r"\bmatieres\b", "matières"),
    (r"\bderives\b", "dérivés"),
    (r"\bequipe\b", "équipe"),
    (r"\bEquipe\b", "Équipe"),
    (r"\bavancee\b", "avancée"),
    (r"\bmethodologie\b", "méthodologie"),
    (r"\bIdeal\b", "Idéal"),
    (r"\bideal\b", "idéal"),
    (r"\bsi ca \b", "si ça "),
    (r"\bca te \b", "ça te "),
    (r"\bca va\b", "ça va"),
    (r"\bca charge\b", "ça charge"),
    (r"\bca prend\b", "ça prend"),
    (r"\bCombien de temps ca \b", "Combien de temps ça "),
    (r"\bcoute\b", "coûte"),
    (r"\bdepend\b", "dépend"),
    (r"\bacces\b", "accès"),
    (r"\bprecise\b", "précise"),
    (r"\bPrecis\b", "Précis"),
    (r"\bgouter\b", "goûter"),
    (r"\bGouter\b", "Goûter"),
    (r"\becris\b", "écris"),
    (r"\becrit\b", "écrit"),
    (r"\breelle\b", "réelle"),
    (r"\breel\b", "réel"),
    (r"\bspontane\b", "spontané"),
    (r"\bdetendu\b", "détendu"),
    (r"\bportee\b", "portée"),
    (r"\bfrancais\b", "français"),
    (r"\bFrancais\b", "Français"),
    (r"\bgeneral\b", "général"),
    (r"\bGeneral\b", "Général"),
    (r"\bgenerale\b", "générale"),
    (r"\bevenement\b", "événement"),
    (r"\bevenements\b", "événements"),
    (r"\breference\b", "référence"),
    (r"\breferences\b", "références"),
    (r"\bpresente\b", "présente"),
    (r"\bPresente\b", "Présente"),
    (r"\binteresse\b", "intéresse"),
    (r"\binteressé\b", "intéressé"),
    (r"\binteressée\b", "intéressée"),
    (r"\bqualite\b", "qualité"),
    (r"\bQualite\b", "Qualité"),
    (r"\bactivite\b", "activité"),
    (r"\bactivites\b", "activités"),
    (r"\bnecessaire\b", "nécessaire"),
    (r"\bNecessaire\b", "Nécessaire"),
    (r"\bnumero\b", "numéro"),
    (r"\bNumero\b", "Numéro"),
    (r"\bnumeros\b", "numéros"),
    (r"\bhoraires et numero\b", "horaires et numéro"),
    (r"\bcomplete\b", "complète"),
    (r"\bComplete\b", "Complète"),
    (r"\bcompletement\b", "complètement"),
    (r"\brapide a lancer\b", "rapide à lancer"),
    (r"\bRapide a lancer\b", "Rapide à lancer"),
    (r"\bmoins cher qu'a\b", "moins cher qu'à"),
    (r"\bLivre a \b", "Livre à "),
    (r"\blivres gratuits a \b", "livres gratuits à "),
    (r"\ble reste a prix\b", "le reste à prix"),
    (r"\ba prix d'appel\b", "à prix d'appel"),
    (r"\bTu est \b", "Tu es "),
    (r"\btu est \b", "tu es "),
    (r"\banee 1\b", "année 1"),  # placeholder - better handled separately
]

# Trop dangereux en global : retirer
SKIP_PATTERNS = {
    r"\bcles\b",
    r"\banee 1\b",
    r"\bcomplete\b",  # peut etre "complete" anglais / verbe
    r"\bComplete\b",
    r"\bdepend\b",  # verbe anglais parfois
    r"\bgeneral\b",  # peut etre dans generalPurpose etc - rare en json
    r"\bGeneral\b",
    r"\bpresente\b",
    r"\bPresente\b",
    r"\becris\b",
    r"\becrit\b",
}

SAFE_REPLACEMENTS = [(p, r) for p, r in REPLACEMENTS if p not in SKIP_PATTERNS]

# Dossiers / fichiers cibles
INCLUDE_DIRS = [
    ROOT / "src" / "pages",
    ROOT / "src" / "includes",
    ROOT / "src" / "data",
    ROOT / "api" / "data",
]

INCLUDE_FILES = [
    ROOT / "build.py",
]

EXCLUDE_NAME_PARTS = {
    "package-lock",
    "node_modules",
}

TEXT_EXTS = {".html", ".json", ".md"}


def should_process(path: Path) -> bool:
    """Filtre les fichiers a traiter."""
    if path.suffix.lower() not in TEXT_EXTS and path.name != "build.py":
        return False
    if any(part in path.parts for part in ("node_modules", "dist", ".git")):
        return False
    # Eviter les prompts images trop bruts si besoin - on garde data/
    return True


def fix_text(text: str) -> tuple[str, int]:
    """Applique les remplacements regex.

    @returns: (texte, nombre de remplacements)
    """
    total = 0
    out = text
    for pattern, repl in SAFE_REPLACEMENTS:
        out2, n = re.subn(pattern, repl, out)
        if n:
            out = out2
            total += n
    return out, total


def main() -> None:
    """Parcourt les contenus visibles et corrige l'orthographe courante."""
    files: list[Path] = []
    for base in INCLUDE_DIRS:
        if base.is_dir():
            files.extend(p for p in base.rglob("*") if p.is_file() and should_process(p))
    for path in INCLUDE_FILES:
        if path.is_file():
            files.append(path)

    changed = 0
    total = 0
    for path in sorted(set(files)):
        try:
            original = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        fixed, n = fix_text(original)
        if not n:
            continue
        path.write_text(fixed, encoding="utf-8", newline="\n")
        changed += 1
        total += n
        print(f"{path.relative_to(ROOT).as_posix()}: {n}")

    print(f"files={changed} replacements={total}")


if __name__ == "__main__":
    main()
