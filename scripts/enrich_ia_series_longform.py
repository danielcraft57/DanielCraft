#!/usr/bin/env python3
"""
Allonge les series Claude + formations en long format pedagogique.

Usage:
    python scripts/enrich_ia_series_longform.py
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "blog" / "content" / "articles"

PREFIXES = ("ia-claude-", "ia-cours-")

EXTRA_BLOCKS = {
    "ia-claude-": """## Prendre Claude en main (sans se perdre)

Claude, c'est pas "ChatGPT en beige". Il est souvent plus a l'aise sur les longs textes, le code, et les consignes precises. Si tu debutes :

1. Ouvre un projet / espace dedie (pas un chat fourre-tout).
2. Donne le contexte en 5 lignes max : qui tu es, pour qui, quel resultat.
3. Demande un plan avant le rendu final.
4. Relis, puis demande une passe "plus naturelle / plus courte".

### Skills et plugins, en vrai

Une Skill, c'est un pack d'instructions reutilisable. Utile quand tu refais souvent la meme tache (audit, mail, resume, brief). Les plugins, eux, branchent Claude a des outils (finance, docs, etc.). Commence simple : 1 skill claire > 10 gadgets.

### Passage depuis ChatGPT

Garde tes meilleurs prompts. Adapte juste le ton : Claude repond souvent mieux si tu precises le format de sortie (liste, tableau, etapes). Et oui, tu peux lui demander de reformuler un vieux prompt ChatGPT pour son style.
""",
    "ia-cours-": """## Construire un vrai parcours (pas juste "regarder des videos")

Se former a l'IA, c'est comme apprendre un outil de travail : ca marche si tu pratiques. Un parcours simple :

1. **Semaine 1** : bases (prompts, limites, verification).
2. **Semaine 2** : un cas perso (mails, resumes, recherche).
3. **Semaine 3** : un cas pro (offre, page, process).
4. **Semaine 4** : automatiser 1 truc repetitif (meme a la main d'abord).

### Comment choisir une formation gratuite

- Est-ce qu'il y a des exercices ?
- Est-ce que ca date de moins d'un an ?
- Est-ce que tu peux reutiliser le contenu dans ton taf cette semaine ?
- Est-ce que le formateur montre des exemples reels (pas que des slides) ?

Si la reponse est non 3 fois, passe a autre chose. Le temps, c'est le vrai cout.
""",
}


def parse_parts(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end < 0:
        return "", text
    return text[: end + 4], text[end + 4 :].lstrip("\n")


def already_enriched(body: str) -> bool:
    return "Prendre Claude en main" in body or "Construire un vrai parcours" in body


def inject_before_faq(body: str, block: str) -> str:
    markers = ("## Mini checklist", "## Questions fréquentes", "## Questions frequentes")
    for m in markers:
        if m in body:
            return body.replace(m, block.strip() + "\n\n---\n\n" + m, 1)
    return body.rstrip() + "\n\n---\n\n" + block.strip() + "\n"


def deepen_steps(body: str) -> str:
    """Ajoute un conseil pratique apres chaque etape/point du deroule."""
    def repl(match: re.Match) -> str:
        heading = match.group(0)
        return (
            heading
            + "\n\n"
            + "> Conseil : fais cette partie une fois sans viser parfait. "
            + "Note ce qui bloque, puis recommence avec une consigne plus precise.\n"
        )

    # Evite de doubler si deja present
    if "> Conseil :" in body:
        return body
    return re.sub(r"(?m)^(### .+)$", repl, body, count=4)


def main() -> None:
    n = 0
    for path in sorted(ARTICLES.glob("ia-*.md")):
        prefix = next((p for p in PREFIXES if path.name.startswith(p)), None)
        if not prefix:
            continue
        text = path.read_text(encoding="utf-8")
        fm, body = parse_parts(text)
        if already_enriched(body):
            print(f"[SKIP] {path.name}")
            continue
        body = deepen_steps(body)
        body = inject_before_faq(body, EXTRA_BLOCKS[prefix])
        # Apostrophes droites
        body = body.replace("'", "'").replace("'", "'").replace("—", "-").replace("–", "-")
        # Accents utiles dans blocs ajoutes
        fixes = {
            "a l'aise": "à l'aise",
            "dedie": "dédié",
            "fourre-tout": "fourre-tout",
            "reutilisable": "réutilisable",
            "meme tache": "même tâche",
            "resume": "résumé",
            "etapes": "étapes",
            "Se former a": "Se former à",
            "ca marche": "ça marche",
            "perso": "perso",
            "automatiser 1 truc repetitif": "automatiser 1 truc répétitif",
            "meme a la main": "même à la main",
            "reutiliser": "réutiliser",
            "reels": "réels",
            "reponse": "réponse",
            "cout": "coût",
            "precise": "précise",
        }
        for a, b in fixes.items():
            body = body.replace(a, b)
        path.write_text(fm + "\n" + body, encoding="utf-8")
        n += 1
        print(f"[OK] {path.name}")
    print(f"\nLong-form enriched: {n}")


if __name__ == "__main__":
    main()
