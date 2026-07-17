#!/usr/bin/env python3
"""Allonge ChatGPT + Gemini + Agents (meme logique que Claude/formations)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "blog" / "content" / "articles"

BLOCKS = {
    "ia-chatgpt-": """## Utiliser ChatGPT sans tourner en rond

ChatGPT brille quand tu lui donnes un cadre. Un mini template qui marche souvent :

1. **Role** : qui doit-il incarner ?
2. **Contexte** : pour qui, quelle contrainte ?
3. **Objectif** : le resultat attendu en 1 phrase.
4. **Format** : liste, tableau, mail, plan...
5. **Critere de qualite** : court, clair, actionnable, etc.

### Astuce memoire / projets

Si tu refais souvent la meme chose, range-la dans un Project ou un GPT dedie. Evite le chat interminable ou tout se melange.
""",
    "ia-gemini-": """## Gemini et l'ecosysteme Google

Gemini est fort quand tu restes dans Google : Docs, Drive, NotebookLM, AI Studio. Le reflexe utile :

1. Mets tes sources au propre (PDF, notes, liens).
2. Demande un plan, puis un rendu.
3. Verifie les citations / extraits avant de publier.

NotebookLM est top pour transformer un dossier en resume, FAQ ou podcast. Gemini "chat" suffit pour les questions rapides.
""",
    "ia-agents-": """## Agents IA : rester concret

Un agent, c'est surtout une boucle : objectif -> actions -> verification -> suite. Avant de "vendre des agents", assure-toi de savoir :

1. Quelle tache est repetitive ?
2. Quelles donnees sont necessaires ?
3. Ou ca peut planter (et qui valide) ?
4. Comment mesurer que c'est reussi ?

Commence par un agent tout bete (1 outil, 1 resultat). Ensuite seulement tu ajoutes MCP, n8n, ou un Agent Builder.
""",
}


def parse_parts(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    end = text.find("\n---", 3)
    if end < 0:
        return "", text
    return text[: end + 4], text[end + 4 :].lstrip("\n")


def inject_before_faq(body: str, block: str) -> str:
    for m in ("## Mini checklist", "## Questions fréquentes", "## Questions frequentes"):
        if m in body:
            return body.replace(m, block.strip() + "\n\n---\n\n" + m, 1)
    return body.rstrip() + "\n\n---\n\n" + block.strip() + "\n"


def main() -> None:
    n = 0
    for path in sorted(ARTICLES.glob("ia-*.md")):
        prefix = next((p for p in BLOCKS if path.name.startswith(p)), None)
        if not prefix:
            continue
        text = path.read_text(encoding="utf-8")
        fm, body = parse_parts(text)
        marker = BLOCKS[prefix].split("\n", 1)[0]
        if marker in body:
            print(f"[SKIP] {path.name}")
            continue
        body = inject_before_faq(body, BLOCKS[prefix])
        body = body.replace("'", "'").replace("'", "'").replace("—", "-")
        for a, b in {
            "Role": "Rôle",
            "resultat": "résultat",
            "Critere": "Critère",
            "qualite": "qualité",
            "meme chose": "même chose",
            "dedie": "dédié",
            "Evite": "Évite",
            "melange": "mélange",
            "ecosysteme": "écosystème",
            "reflexe": "réflexe",
            "resume": "résumé",
            "repetitive": "répétitive",
            "necessaires": "nécessaires",
            "Ou ca": "Où ça",
            "reussi": "réussi",
        }.items():
            body = body.replace(a, b)
        path.write_text(fm + "\n" + body, encoding="utf-8")
        n += 1
        print(f"[OK] {path.name}")
    print(f"\nExtra series enriched: {n}")


if __name__ == "__main__":
    main()
