#!/usr/bin/env python3
"""Simplifie serie IA Agents."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from add_series3_extra_schemas import (  # noqa: E402
    SCHEMAS,
    compare2,
    esc,
    flow_row,
    grid3,
    stack_layers,
    svg_wrap,
)

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "blog" / "content" / "articles"
COLLECTIONS = ROOT / "blog" / "content" / "collections"


def write_svg(fname: str, title: str, desc: str, body: str) -> None:
    SCHEMAS.mkdir(parents=True, exist_ok=True)
    (SCHEMAS / fname).write_text(svg_wrap(title, desc, body), encoding="utf-8")


def fig(fname: str, alt: str, caption: str) -> str:
    return f'''<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/{fname}" alt="{esc(alt)}" class="schema-inline" width="640" />
  <figcaption>{esc(caption)}</figcaption>
</figure>'''


def patch_fm(raw: str, title: str, excerpt: str) -> str:
    end = raw.find("\n---", 3)
    fm = raw[: end + 4]
    fm = re.sub(r'^title:\s*".*?"', f'title: "{title}"', fm, count=1, flags=re.M)
    esc_ex = excerpt.replace('"', '\\"')
    fm = re.sub(r'^excerpt:\s*".*?"', f'excerpt: "{esc_ex}"', fm, count=1, flags=re.M)
    return fm


def article(slug: str, title: str, excerpt: str, body: str) -> None:
    path = ARTICLES / f"{slug}.md"
    raw = path.read_text(encoding="utf-8")
    fm = patch_fm(raw, title, excerpt)
    path.write_text(fm + "\n\n" + body.lstrip() + "\n", encoding="utf-8")
    print(f"[OK] {slug}")


SVGS = [
    ("ia-agents-base.svg", "Creer un agent", "Objectif et outils",
     flow_row(["But", "Outils", "Regles", "Test", "Corriger"],
              "Un agent sans but clair devient un gadget")),
    ("ia-agents-danger.svg", "Dangers agents", "Cadre et limites",
     compare2("Sans cadre", ["Actions surprises", "Fuites de donnees"],
              "Avec cadre", ["Perimetre", "Revue humaine"],
              "Puissance = responsabilite")),
    ("ia-agents-compare.svg", "Choisir un agent", "Tester 2 options",
     flow_row(["Besoin", "Outil A", "Outil B", "Critere", "Choix"],
              "Compare sur UNE tache concrete")),
    ("ia-agents-slides.svg", "Agent presentations", "Plan puis slides",
     stack_layers([
         ("Plan", "Structure claire"),
         ("Contenu", "Points cles"),
         ("Design", "Simple et lisible"),
         ("Revue", "Humain final"),
     ], "L'IA propose, toi tu valides")),
    ("ia-agents-research.svg", "Deep research", "Sources et doute",
     flow_row(["Question", "Recherche", "Sources", "Synthese", "Verif"],
              "Toujours croiser les sources importantes")),
]
for item in SVGS:
    write_svg(*item)

article(
    "ia-agents-creer-un-agent-ia-gratuit-avec-claude-et-les-mcp-le-model",
    "Agent gratuit avec Claude + MCP : l'idee simple",
    "Connecter Claude a des outils (MCP) pour qu'il agisse — avec un perimetre clair.",
    f"""# Agent gratuit avec Claude + MCP : l'idee simple

**MCP** = brancher des outils. L'agent peut lire / agir dans ce cadre.

{fig("ia-agents-base.svg", "Schema agent Claude MCP", "But, outils, regles, test.")}

Commence par 1 outil utile. Verifie chaque action. Skills Claude : [explication](/blog/articles/ia-claude-si-vous-utilisez-claude-utilisez-ca-une-skill-c-est-un-ensemble-d-i.html).
""",
)

article(
    "ia-agents-formation-gratuite-pour-creer-et-vendre-des-agents-ia-parfait-si-vou",
    "Formation agents IA : apprendre puis vendre (si tu as un vrai offre)",
    "Suivre un parcours gratuit, construire un agent utile, ensuite eventuellement le moneter.",
    f"""# Formation agents IA : apprendre puis vendre (si tu as un vrai offre)

D'abord un agent qui **rend service**. La vente vient apres.

{fig("ia-agents-base.svg", "Schema apprendre agents", "Former, construire, tester.")}

Fais un cas client fictif. Documente le process. Tutoriel : [en quelques minutes](/blog/articles/ia-agents-tutoriel-debutant-comment-creer-un-agent-ia-en-quelques-minutes.html).
""",
)

article(
    "ia-agents-nouvel-agent-ia-gratuit-scout-new-il-est-aussi-bon-que-genspark-et",
    "Nouvel agent gratuit : comment le juger vite",
    "Ne compare pas les marques : compare le resultat sur ta tache en 20 minutes.",
    f"""# Nouvel agent gratuit : comment le juger vite

Chaque semaine un "meilleur agent". Ta methode reste.

{fig("ia-agents-compare.svg", "Schema comparer agents", "Besoin, A, B, critere, choix.")}

Liste 3 criteres (vitesse, qualite, fiabilite). Teste. Garde le gagnant.
""",
)

article(
    "ia-agents-tutoriel-debutant-comment-creer-un-agent-ia-en-quelques-minutes",
    "Creer un agent IA en quelques minutes (debutant)",
    "But clair, consignes courtes, un outil, un test — puis on ameliore.",
    f"""# Creer un agent IA en quelques minutes (debutant)

1. Ecris le **but** en une phrase  
2. Donne 3 regles  
3. Branche 1 outil max  
4. Teste

{fig("ia-agents-base.svg", "Schema agent debutant", "But, outils, regles, test, corriger.")}

Ensuite seulement : complexifie. Dangers : [jour 2](/blog/articles/ia-agents-jour-2-pour-comprendre-les-agents-ia-les-dangers.html).
""",
)

article(
    "ia-agents-agent-ia-neo-by-flowith-le-premier-agent-ia-infini-il-peut-trava",
    "Agents longs / infinis : utiles, a surveiller",
    "Un agent qui travaille longtemps peut deriver : checkpoints et limites obligatoires.",
    f"""# Agents longs / infinis : utiles, a surveiller

Long = plus de risques d'erreur en chaine.

{fig("ia-agents-danger.svg", "Schema agent long", "Cadre et revue.")}

Impose des pauses / validations. Ne laisse pas tourner sur des donnees sensibles sans controle.
""",
)

article(
    "ia-agents-manus-ai-l-agent-ia-le-plus-complet-parfait-pour-les-personnes-non",
    "Agent tout-en-un : pour qui c'est vraiment utile",
    "Complet ne veut pas dire magique : regarde si ca simplifie TON flux de travail.",
    f"""# Agent tout-en-un : pour qui c'est vraiment utile

Si tu debutes, un outil simple + bonne methode bat souvent le tout-en-un.

{fig("ia-agents-compare.svg", "Schema choisir agent complet", "Tester sur ton besoin.")}

Essaye sur une tache reelle. Si ca freine, reviens au [tutoriel debutant](/blog/articles/ia-agents-tutoriel-debutant-comment-creer-un-agent-ia-en-quelques-minutes.html).
""",
)

article(
    "ia-agents-3-alternatives-a-deep-research-l-agent-d-intelligence-artificielle-d",
    "3 alternatives a Deep Research (recherche longue)",
    "Comparer des agents de recherche : sources, profondeur, prix — et toujours verifier.",
    f"""# 3 alternatives a Deep Research (recherche longue)

La recherche IA aide a **cartographier**. Elle n'est pas une bibliotheque magique.

{fig("ia-agents-research.svg", "Schema recherche IA", "Question, sources, synthese, verif.")}

Teste 2 outils sur la meme question. Garde les sources. Voir aussi [examen Deep Research](/blog/articles/ia-agents-le-dernier-examen-de-l-humanite-deep-research-d-openai-atteint-un-s.html).
""",
)

article(
    "ia-agents-astuce-et-bon-plan-comment-avoir-perplexity-pro-gratuitement-pendan",
    "Perplexity Pro : bons plans (et ce qu'il faut verifier)",
    "Promos et essais existent parfois — lis les conditions, ne partage pas ton compte.",
    f"""# Perplexity Pro : bons plans (et ce qu'il faut verifier)

Les "gratuits" ont souvent une **duree** ou des conditions.

{fig("ia-agents-compare.svg", "Schema offre Pro", "Lire les conditions avant.")}

Verifie la date de fin, les moyens de paiement, l'annulation. L'outil sert surtout a chercher avec sources.
""",
)

article(
    "ia-agents-agent-ia-pour-creer-des-presentations-style-powerpoint-en-utilisant-d",
    "Agent presentations : du plan aux slides",
    "Faire generer une trame claire, puis peaufiner le design et le message toi-meme.",
    f"""# Agent presentations : du plan aux slides

L'IA ecrit vite. Toi tu gardes le **fil rouge**.

{fig("ia-agents-slides.svg", "Schema agent slides", "Plan, contenu, design, revue.")}

Demande un plan 8 slides max, puis le contenu. Simplifie. Alternative : [Gamma](/blog/articles/ia-nocode-gamma-ai-meilleure-ia-gratuite-pour-creer-des-presentations-powerpo.html).
""",
)

article(
    "ia-agents-jour-2-pour-comprendre-les-agents-ia-les-dangers",
    "Agents IA : les dangers a connaitre (jour 2)",
    "Actions non voulues, donnees exposees, hallucinations en chaine — comment se proteger.",
    f"""# Agents IA : les dangers a connaitre (jour 2)

Un agent puissant sans cadre, c'est un apprentice sorcier.

{fig("ia-agents-danger.svg", "Schema dangers agents", "Sans cadre versus avec cadre.")}

Limite les droits. Demande confirmation avant actions irreversibles. Relis les sorties. Debut : [tutoriel](/blog/articles/ia-agents-tutoriel-debutant-comment-creer-un-agent-ia-en-quelques-minutes.html).
""",
)

article(
    "ia-agents-le-dernier-examen-de-l-humanite-deep-research-d-openai-atteint-un-s",
    "Deep Research et examens : ce que ca prouve (ou pas)",
    "Un score eleve sur un benchmark n'egal pas une verite absolue dans ton metier.",
    f"""# Deep Research et examens : ce que ca prouve (ou pas)

Les classements impressionnent. Ton usage decide.

{fig("ia-agents-research.svg", "Schema benchmarks recherche", "Score utile, verification indispensable.")}

Utilise l'outil pour explorer. Valide les faits critiques autrement. Alternatives : [3 options](/blog/articles/ia-agents-3-alternatives-a-deep-research-l-agent-d-intelligence-artificielle-d.html).
""",
)

path = COLLECTIONS / "ia-agents-serie.json"
col = json.loads(path.read_text(encoding="utf-8"))
col["title"] = "Serie IA — Agents (agir avec cadre)"
col["description"] = (
    "Creer, comparer et securiser des agents IA : tutoriels debutants, recherche, dangers."
)
path.write_text(json.dumps(col, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("[OK] ia-agents-serie.json")
print("done")
