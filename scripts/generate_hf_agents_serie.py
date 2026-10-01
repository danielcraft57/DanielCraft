#!/usr/bin/env python3
"""Genere la serie Agents Hugging Face (cours agents) : articles, schemas, OG.

Usage :
    python scripts/generate_hf_agents_serie.py
"""
from __future__ import annotations

import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = _SCRIPT_DIR.parent
sys.path.insert(0, str(_SCRIPT_DIR))

from _og_cartoon import render_og_card  # noqa: E402

ARTICLES = ROOT / "blog" / "content" / "articles"
COLLECTIONS = ROOT / "blog" / "content" / "collections"
SCHEMAS = ROOT / "assets" / "images" / "blog" / "schemas"
OG_DIR = ROOT / "assets" / "images" / "og"

SERIES = "hf-agents-serie"
HF_AGENTS = "https://huggingface.co/learn/agents-course"

ORDER = [
    "agents-hf-quest-ce-qu-un-agent",
    "agents-hf-outils-et-function-calling",
    "agents-hf-react-pensee-action-observation",
    "agents-hf-smolagents-premier-agent",
    "agents-hf-code-agents-vs-tool-calling",
    "agents-hf-frameworks-llamaindex-langgraph",
    "agents-hf-rag-agentique",
    "agents-hf-observabilite-evaluation",
]


def svg_flow(path: Path, title: str, caption: str, boxes: list[str], accent_last: bool = True) -> None:
    n = len(boxes)
    gap = 12
    box_w = min(150, (760 - gap * (n - 1)) // n)
    total = n * box_w + (n - 1) * gap
    start_x = (800 - total) // 2
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" role="img" aria-labelledby="title desc">',
        f'  <title id="title">{title}</title>',
        f'  <desc id="desc">{caption}</desc>',
        '  <rect width="800" height="420" fill="#f5f7fb"/>',
        f'  <text x="400" y="36" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="18" font-weight="700" fill="#0f172a">{title}</text>',
        '  <defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#0f172a"/></marker></defs>',
    ]
    for i, label in enumerate(boxes):
        x = start_x + i * (box_w + gap)
        y = 160
        stroke = "#dc2626" if accent_last and i == n - 1 else ("#2563eb" if i % 2 == 0 else "#60a5fa")
        lines = label.split("\n")
        parts.append(f'  <rect x="{x}" y="{y}" width="{box_w}" height="70" rx="8" fill="#fff" stroke="{stroke}" stroke-width="2"/>')
        if len(lines) == 1:
            parts.append(
                f'  <text x="{x + box_w/2}" y="{y + 40}" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="12" font-weight="600" fill="#0f172a">{lines[0]}</text>'
            )
        else:
            parts.append(
                f'  <text x="{x + box_w/2}" y="{y + 32}" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="11" font-weight="600" fill="#0f172a">{lines[0]}</text>'
            )
            parts.append(
                f'  <text x="{x + box_w/2}" y="{y + 50}" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="11" font-weight="600" fill="#0f172a">{lines[1]}</text>'
            )
        if i < n - 1:
            x1 = x + box_w
            x2 = x1 + gap - 10
            parts.append(f'  <path d="M{x1} 195 H{x2}" stroke="#0f172a" stroke-width="2" fill="none" marker-end="url(#a)"/>')
    parts.append(
        f'  <text x="400" y="390" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#0f172a">{caption}</text>'
    )
    parts.append("</svg>\n")
    path.write_text("\n".join(parts), encoding="utf-8")


SCHEMAS_SPEC = {
    "agents-hf-quest": (["LLM", "Outils\n(tools)", "Boucle\nagent", "Action\ndans le monde"], "Un agent = LLM + outils + boucle."),
    "agents-hf-tools": (["Besoin", "Schema\noutils", "Appel\nfonction", "Resultat"], "Les tools donnent des mains au modele."),
    "agents-hf-react": (["Thought", "Action", "Observation", "Reponse"], "Cycle ReAct : penser, agir, observer."),
    "agents-hf-smolagents": (["CodeAgent", "Modele", "Tools", "Run"], "smolagents : agent leger Hugging Face."),
    "agents-hf-code-vs-json": (["Code\nagent", "vs", "Tool-calling\nJSON", "Choix"], "Code Python ou blobs JSON : deux styles."),
    "agents-hf-frameworks": (["smolagents", "LlamaIndex", "LangGraph", "Cas\ndusage"], "Trois frameworks, trois philosophies."),
    "agents-hf-rag": (["Question", "Retrieval\nagentique", "Outils\nRAG", "Reponse\ncitee"], "RAG agentique : chercher puis raisonner."),
    "agents-hf-observability": (["Traces", "Metriques", "Eval\nhumaine", "Ameliorer"], "Observer pour fiabiliser les agents."),
}


def write_schemas() -> None:
    SCHEMAS.mkdir(parents=True, exist_ok=True)
    mapping = {
        "agents-hf-quest-ce-qu-un-agent": "agents-hf-quest",
        "agents-hf-outils-et-function-calling": "agents-hf-tools",
        "agents-hf-react-pensee-action-observation": "agents-hf-react",
        "agents-hf-smolagents-premier-agent": "agents-hf-smolagents",
        "agents-hf-code-agents-vs-tool-calling": "agents-hf-code-vs-json",
        "agents-hf-frameworks-llamaindex-langgraph": "agents-hf-frameworks",
        "agents-hf-rag-agentique": "agents-hf-rag",
        "agents-hf-observabilite-evaluation": "agents-hf-observability",
    }
    titles = {
        "agents-hf-quest": "Agent IA = LLM + outils",
        "agents-hf-tools": "Tools et function calling",
        "agents-hf-react": "Cycle ReAct",
        "agents-hf-smolagents": "smolagents",
        "agents-hf-code-vs-json": "Code agent vs tool-calling",
        "agents-hf-frameworks": "Frameworks agents",
        "agents-hf-rag": "RAG agentique",
        "agents-hf-observability": "Observabilite agents",
    }
    for slug, key in mapping.items():
        boxes, cap = SCHEMAS_SPEC[key]
        svg_flow(SCHEMAS / f"{key}.svg", titles[key], cap, boxes)


CONTENT: dict[str, dict] = {}


def _art(
    slug: str,
    *,
    title: str,
    excerpt: str,
    order: int,
    schema: str,
    schema_alt: str,
    figcaption: str,
    body: str,
    faq: list[tuple[str, str]],
    og_title: str,
    og_sub: str,
    scene: str,
) -> None:
    CONTENT[slug] = {
        "title": title,
        "excerpt": excerpt,
        "order": order,
        "schema": schema,
        "schema_alt": schema_alt,
        "figcaption": figcaption,
        "body": body,
        "faq": faq,
        "og_title": og_title,
        "og_sub": og_sub,
        "scene": scene,
    }


_art(
    "agents-hf-quest-ce-qu-un-agent",
    title="Agents IA : c'est quoi, au juste ?",
    excerpt="LLM, outils et boucle : la definition simple d'un agent, sans marketing.",
    order=1,
    schema="agents-hf-quest.svg",
    schema_alt="Schema agent IA : LLM, outils, boucle, action",
    figcaption="Un agent combine un modele, des outils et une boucle de decisions.",
    og_title="Agents IA : c'est quoi ?",
    og_sub="LLM + outils + boucle, sans blabla",
    scene="assistant",
    faq=[
        ("Un chatbot est-il un agent ?", "Pas forcement. S'il ne fait que repondre du texte sans outils ni actions, c'est un LLM conversationnel, pas un agent."),
        ("Il faut un gros modele ?", "Non. Un petit modele bien outille peut battre un geant sans tools sur des taches concretes."),
        ("C'est dangereux ?", "Oui si tu donnes trop de pouvoirs (ecrire des fichiers, payer, envoyer des mails) sans garde-fous. On y revient dans la serie."),
    ],
    body=f"""
Tu entends « agent IA » partout depuis 2025. Souvent, ca veut juste dire « un chat qui appelle une API ». Ici on pose une definition propre, inspiree du [cours Agents Hugging Face]({HF_AGENTS}) (contenu original DanielCraft).

## Definition citable

Un **agent IA** est un systeme qui utilise un modele de langage pour **decider** quelles actions mener, via des **outils** (tools), dans une **boucle** : observer le resultat, puis continuer jusqu'a une reponse ou un arret.

Le LLM reste le cerveau. Les tools sont les mains. La boucle est le rythme : sans elle, tu as juste une generation unique.

## Ce qui change vs un simple LLM

Un LLM seul predit des tokens. Tu lui donnes un prompt, tu recois du texte. Utile. Limite des qu'il faut chercher une info fraiche, calculer, lire un fichier, cliquer quelque part.

Un agent peut :
- appeler une fonction Python (météo, SQL, calendrier) ;
- chercher dans une base documentaire ;
- ecrire du code et l'executer (avec sandbox) ;
- enchaîner plusieurs etapes sans que tu rebricoles le prompt a chaque fois.

## Anatomie en trois blocs

**1. Le modele.** Chat LLM capable de suivre des instructions et, idéalement, d'appeler des tools (function calling).

**2. Les outils.** Des fonctions decrites (nom, parametres, description). Le modele choisit quoi appeler ; ton runtime execute.

**3. La boucle.** Thought → Action → Observation (on detaille ReAct juste apres dans la serie). Tant que la tache n'est pas finie, on continue.

## Exemple mental (boutique Metz)

Client : « Est-ce que vous etes ouvert samedi et quel est le delai pour un devis site ? »

Sans agent : le LLM invente ou te sort une reponse generique.

Avec agent : tool `get_horaires()`, tool `get_delai_devis()`, puis reponse basee sur les observations. Toi tu as branche les vraies donnees.

## Ce que cette serie va couvrir

Tools et function calling. Cycle ReAct. Premier agent avec **smolagents**. Code agents vs tool-calling JSON. Vue d'ensemble LlamaIndex / LangGraph. RAG agentique. Observabilite et eval.

On s'inspire du parcours Hugging Face Agents Course. On n'en copie pas les lecons : on les retraduit en francais, avec du terrain.

## Lien avec la serie LLM

Si tu debutes totalement, la [serie LLM & Transformers](/blog/series/llm-transformers-serie.html) pose les bases (pipeline, Hub, fine-tuning). Ici on suppose que tu sais qu'un LLM predit des tokens - et on lui donne des outils.
""".strip(),
)

_art(
    "agents-hf-outils-et-function-calling",
    title="Tools et function calling : donner des mains au LLM",
    excerpt="Decrire une fonction, laisser le modele l'appeler, executer le resultat : le coeur des agents.",
    order=2,
    schema="agents-hf-tools.svg",
    schema_alt="Schema tools et function calling",
    figcaption="Du besoin au resultat via un schema d'outil.",
    og_title="Tools et function calling",
    og_sub="Des mains pour le modele",
    scene="code",
    faq=[
        ("Function calling = agent ?", "C'est une brique. L'agent ajoute la boucle et la strategie d'enchainement."),
        ("Combien d'outils max ?", "Commence avec 3-5 bien decrits. Trop d'outils = le modele se perd."),
        ("JSON Schema obligatoire ?", "En pratique oui pour les APIs modernes : nom, types, required, description claire."),
    ],
    body=f"""
Sans outils, un LLM raconte. Avec des outils, il **agit** (dans les limites que tu poses). Cette idee est centrale dans le [cours Agents HF]({HF_AGENTS}).

## Definition citable

Le **function calling** (ou tool calling) est le mecanisme par lequel un modele propose d'appeler une fonction externe avec des arguments structures ; ton application execute la fonction et renvoie le resultat au modele.

## A quoi ressemble un tool

```python
def get_horaires_boutique(jour: str) -> str:
    \"\"\"Retourne les horaires d'ouverture pour un jour (ex: samedi).\"\"\"
    data = {{
        "lundi": "ferme",
        "mardi": "9h-18h",
        "mercredi": "9h-18h",
        "jeudi": "9h-18h",
        "vendredi": "9h-18h",
        "samedi": "10h-17h",
        "dimanche": "ferme",
    }}
    return data.get(jour.lower(), "jour inconnu")
```

Cote modele, tu exposes un schema : nom `get_horaires_boutique`, parametre `jour` (string), description utile. Le modele ne « voit » pas ton code Python - il voit le contrat.

## Le flux en quatre temps

1. L'utilisateur pose une question.
2. Le modele decide : repondre direct ou appeler un tool.
3. Ton runtime execute le tool (vrai code, vraie API).
4. Tu renvoies l'observation au modele, qui formule la reponse finale (ou un nouvel appel).

## Bien ecrire les descriptions

Le modele lit les docstrings / descriptions comme un manuel. Vague = mauvais choix d'outil.

Mauvais : « recupere des infos ».
Bon : « Retourne les horaires d'ouverture de la boutique pour un jour de la semaine en francais. »

Pareil pour les parametres : enums si possible, formats de date explicites, unites.

## Pieges classiques

Laisser un tool « envoyer_email » sans confirmation humaine. Donner un tool SQL libre sur la prod. Oublier les erreurs : si l'API tombe, l'observation doit le dire clairement pour que le modele s'adapte (ou s'arrete).

## Mini squelette d'orchestration

```python
# Pseudo-code d'une boucle tool-calling
messages = [{{"role": "user", "content": question}}]
while True:
    out = llm.chat(messages, tools=TOOL_SCHEMAS)
    if out.tool_calls:
        for call in out.tool_calls:
            result = run_tool(call.name, call.args)
            messages.append(tool_result_message(call, result))
        continue
    return out.content
```

La boucle, c'est deja l'embryon d'agent. ReAct formalise comment le modele « pense » entre les appels.
""".strip(),
)

_art(
    "agents-hf-react-pensee-action-observation",
    title="ReAct : pensee, action, observation",
    excerpt="Le cycle Thought-Action-Observation qui structure la plupart des agents modernes.",
    order=3,
    schema="agents-hf-react.svg",
    schema_alt="Schema cycle ReAct Thought Action Observation",
    figcaption="Penser, agir, observer - puis recommencer si besoin.",
    og_title="ReAct : pensee, action, observation",
    og_sub="Le rythme des agents modernes",
    scene="process",
    faq=[
        ("ReAct = une lib ?", "Non : c'est un pattern de raisonnement. Les libs l'implementent."),
        ("Toujours afficher le Thought ?", "En debug oui. En prod face client, souvent tu caches le raisonnement brut."),
        ("Ca evite les hallucinations ?", "Ca les reduit si les tools sont fiables. Ca ne remplace pas la validation."),
    ],
    body=f"""
**ReAct** (Reason + Act) est le schema mental le plus utile pour comprendre un agent. Le [cours Agents Hugging Face]({HF_AGENTS}) insiste dessus des l'unite 1 - pour une bonne raison.

## Definition citable

**ReAct** est une approche ou le modele alterne raisonnement interne (**Thought**), appel d'outil (**Action**), et prise en compte du retour (**Observation**), jusqu'a une reponse finale.

## Les trois temps

**Thought.** Le modele explique (parfois en interne) ce qu'il va faire : « Il me faut les horaires de samedi. »

**Action.** Il choisit un tool + des arguments : `get_horaires_boutique(jour="samedi")`.

**Observation.** Ton systeme renvoie `"10h-17h"`. Le modele integre ca.

Si c'est suffisant → reponse. Sinon → nouveau Thought.

## Pourquoi ca marche mieux qu'un mega-prompt

Un prompt unique « fais tout » pousse le modele a inventer. ReAct force des checkpoints avec le monde reel (tes tools). Chaque observation ancre la suite.

## Mini trace lisible

```text
Thought: Je dois verifier le stock du produit X.
Action: check_stock(sku="X-42")
Observation: stock=3
Thought: Stock bas mais disponible. Je peux confirmer la commande.
Action: final_answer("Oui, 3 pieces encore en stock.")
```

En vrai, selon le framework, le « Thought » peut etre un champ cache, un message systeme, ou du code.

## Limites a connaitre

Boucles infinies (l'agent rappelle le meme tool). Actions couteuses sans budget. Observations trop bruyantes (HTML de 200 Ko). Tu poses des plafonds : max steps, timeout, allowlist d'outils.

## Lien pratique

smolagents et d'autres frameworks implementent cette boucle pour toi. Comprendre ReAct te permet de debugger quand « l'agent tourne en rond » - souvent un tool mal decrit ou une observation inutile.
""".strip(),
)

_art(
    "agents-hf-smolagents-premier-agent",
    title="Premier agent avec smolagents",
    excerpt="Lancer un CodeAgent Hugging Face, brancher un tool, obtenir une premiere run propre.",
    order=4,
    schema="agents-hf-smolagents.svg",
    schema_alt="Schema smolagents CodeAgent modele tools run",
    figcaption="smolagents orchestre modele, tools et execution.",
    og_title="Premier agent avec smolagents",
    og_sub="Le framework leger Hugging Face",
    scene="code",
    faq=[
        ("smolagents c'est quoi ?", "Une lib Hugging Face pour construire des agents legers, surtout CodeAgent."),
        ("Il faut un GPU ?", "Pour un petit modele API / Hub, non. Pour un gros modele local, oui."),
        ("Prod-ready out of the box ?", "Excellent pour apprendre et prototyper. En prod : sandbox, quotas, logs."),
    ],
    body=f"""
**smolagents** est la lib mise en avant dans le [cours Agents HF]({HF_AGENTS}) pour passer de la theorie a une demo qui tourne. Idee : rester simple, Python-first.

## Definition citable

**smolagents** est un framework leger Hugging Face pour creer des agents qui raisonnent et agissent, notamment via l'execution de code (**CodeAgent**) ou d'appels d'outils structures.

## Install minimal

```bash
pip install smolagents
```

Tu auras aussi besoin d'un modele accessible (API HF, local, ou autre backend compatible selon ta config).

## Un premier CodeAgent (esprit)

```python
from smolagents import CodeAgent, HfApiModel

def average(nums: list[float]) -> float:
    \"\"\"Calcule la moyenne d'une liste de nombres.\"\"\"
    return sum(nums) / max(len(nums), 1)

model = HfApiModel()  # adapte selon ta config / token
agent = CodeAgent(tools=[average], model=model)

result = agent.run("Quelle est la moyenne de 10, 12 et 17 ?")
print(result)
```

L'agent peut ecrire un petit bout de Python qui appelle `average`, l'executer, lire le resultat, repondre. C'est ReAct sous le capot, avec du code comme langage d'action.

## Ce que tu verifies au premier run

- Le tool est bien selectionne (pas d'invention de fonction).
- L'execution est dans un perimetre safe (pas d'acces disque sauvage en lab).
- Le nombre de steps reste raisonnable.
- La reponse finale est ancree sur l'observation, pas sur une hallucination.

## Bonnes pratiques des le jour 1

Nomme clairement les tools. Limite les imports dangereux. Log chaque Action/Observation. Commence avec une tache bete (calcul, horaires) avant le « agent qui gere ma boite mail ».

## Suite

Dans l'article suivant : **CodeAgent** vs **ToolCallingAgent** (JSON) - quand choisir quoi.
""".strip(),
)

_art(
    "agents-hf-code-agents-vs-tool-calling",
    title="Code agents vs tool-calling JSON",
    excerpt="Deux facons d'agir : generer du Python executable, ou proposer des appels JSON parses.",
    order=5,
    schema="agents-hf-code-vs-json.svg",
    schema_alt="Schema comparaison code agent et tool-calling JSON",
    figcaption="Deux styles d'action, un meme objectif : agir via des outils.",
    og_title="Code agents vs tool-calling",
    og_sub="Python executable ou JSON structure",
    scene="gear",
    faq=[
        ("Lequel est « mieux » ?", "Ni l'un ni l'autre. Code = flexible. JSON = plus controle et souvent plus safe."),
        ("Code agent = executer n'importe quoi ?", "Non si tu sandboxes. Oui si tu fais confiance aveugle - mauvaise idee."),
        ("Les APIs chat classiques ?", "La plupart exposent du tool-calling JSON natif."),
    ],
    body=f"""
Dans smolagents (et le [cours Agents]({HF_AGENTS})), tu croises deux familles. Comprendre la difference evite de te tromper de design.

## Code agent

Le modele **ecrit du code** (souvent Python) qui utilise tes tools / libs. Tu executes ce code dans un environnement controle. Avantage : composition libre (boucles, calculs intermediaires). Risque : surface d'attaque plus large si la sandbox est perméable.

## Tool-calling JSON

Le modele renvoie un **blob structure** : `{{"name": "get_horaires", "arguments": {{"jour": "samedi"}}}}`. Ton runtime parse, valide, execute **uniquement** cette fonction. Avantage : allowlist stricte. Limite : moins de flexibilité pour des enchaînements complexes dans un seul step.

## Definition citable

Un **CodeAgent** exprime ses actions en code executable ; un **ToolCallingAgent** exprime ses actions en appels d'outils structures (souvent JSON) interpretes par le runtime.

## Quand choisir quoi

| Besoin | Piste |
|--------|--------|
| Calculs / ETL leger / scripts | Code agent |
| Actions metier bornees (CRM, horaires) | Tool-calling JSON |
| Conformite / audit strict | JSON + validation schema |
| Exploration data science | Code agent sandboxe |

## Erreur frequente

Mettre un CodeAgent en prod avec `os.system` accessible parce que « ca marche en local ». Sandbox, pas de reseau par defaut, timeout, memoire limitee - ou reste sur du JSON tool-calling.

## En pratique DanielCraft

Pour un commerce : tool-calling sur horaires, devis, stock. Pour un lab data / analyse : CodeAgent derriere une sandbox. Les deux patterns coexistent dans une stack serieuse.
""".strip(),
)

_art(
    "agents-hf-frameworks-llamaindex-langgraph",
    title="smolagents, LlamaIndex, LangGraph : quoi choisir ?",
    excerpt="Trois frameworks du cours Agents HF : legerete, data-centric, graphes de controle.",
    order=6,
    schema="agents-hf-frameworks.svg",
    schema_alt="Schema frameworks smolagents LlamaIndex LangGraph",
    figcaption="Meme probleme agent, trois philosophies d'implementation.",
    og_title="smolagents, LlamaIndex, LangGraph",
    og_sub="Choisir le bon framework agent",
    scene="catalog",
    faq=[
        ("Je dois tous les apprendre ?", "Non. Comprends les trade-offs, maitrise-en un, sache lire les deux autres."),
        ("LangChain dans le lot ?", "LangGraph est la brique graphe moderne de l'ecosysteme LangChain."),
        ("Pour un POC rapide ?", "smolagents ou un tool-calling natif API. Monte en framework quand le graphe se complexifie."),
    ],
    body=f"""
Le [cours Agents Hugging Face]({HF_AGENTS}) ne s'arrete pas a smolagents : **LlamaIndex** et **LangGraph** font partie du parcours. Voici la carte mentale, sans guerre de religion.

## smolagents

Leger, pedagogique, tres HF. Ideal pour comprendre CodeAgent / tools vite. Moins « enterprise workflow » out of the box.

## LlamaIndex

Historiquement centre sur l'indexation et la retrieval sur **tes donnees**. Les agents y sont naturels des que la question est « repondre avec ma doc / mes bases ». Pense composants, Hub d'integrations, workflows agentiques.

## LangGraph

Tu modelises l'agent comme un **graphe** : noeuds, aretes, etat partage, branches. Excellent quand tu veux un controle fin (humain dans la boucle, retries, chemins conditionnels, prod).

## Definition citable

**LlamaIndex** privilégie agents et workflows autour de donnees indexees ; **LangGraph** privilégie le controle explicite du flux agent via un graphe d'etats.

## Tableau rapide

| Critere | smolagents | LlamaIndex | LangGraph |
|---------|------------|------------|-----------|
| Courbe | douce | moyenne | plus raide |
| Force | simplicite HF | data / RAG | controle prod |
| Style | code-first | composants data | graphe d'etat |

## Conseil de choix

POC atelier / formation → smolagents.
Assistant sur corpus entreprise → LlamaIndex (ou RAG + tools).
Process metier avec etats et validations → LangGraph.

L'important n'est pas le logo : c'est tools clairs, ReAct maitrise, et observabilite (prochain articles : RAG agentique puis eval).
""".strip(),
)

_art(
    "agents-hf-rag-agentique",
    title="RAG agentique : chercher, puis raisonner",
    excerpt="Au-dela du RAG lineaire : l'agent decide quand retriever, quoi relancer, quels outils combiner.",
    order=7,
    schema="agents-hf-rag.svg",
    schema_alt="Schema RAG agentique question retrieval outils reponse",
    figcaption="L'agent pilote la retrieval au lieu d'un pipeline fixe.",
    og_title="RAG agentique",
    og_sub="Chercher et raisonner en boucle",
    scene="report",
    faq=[
        ("RAG classique vs agentique ?", "Classique = retrieve puis generate une fois. Agentique = l'agent peut retriever plusieurs fois, changer de requete, appeler d'autres tools."),
        ("Toujours meilleur ?", "Non. Plus cher, plus lent. Utile quand la question est multi-etapes."),
        ("Citations obligatoires ?", "Fortement recommande pour la confiance et le GEO / E-E-A-T."),
    ],
    body=f"""
Le **RAG** classique : embed la question → top-k chunks → prompt → reponse. Ca marche. Ca casse sur les questions qui demandent plusieurs allers-retours. Le [cours Agents HF]({HF_AGENTS}) pousse le **RAG agentique**.

## Definition citable

Le **RAG agentique** laisse un agent decider dynamiquement quand et comment recuperer de l'information (requetes, sources, outils), puis integrer les observations avant de repondre.

## Exemple

Question : « Compare le delai de devis annonce sur le site et ce qu'on a livre au client Dupont en mars. »

RAG lineaire : un seul retrieve risque de rater soit la page site, soit le ticket CRM.

Agentique :
1. Tool web/doc interne → delai annonce.
2. Tool CRM → dossier Dupont mars.
3. Thought : ecart detecte.
4. Reponse comparee + sources.

## Outils typiques

- retriever vectoriel (collection « faq-site ») ;
- recherche bm25 / keyword ;
- API metier ;
- calculatrice / formatter.

L'agent n'est pas magique : si l'index est pourri, il retrievera du pourri avec plus de style.

## Garde-fous

Max retrieval steps. Obligation de citer. Refus si rien de pertinent (« je n'ai pas trouve dans la base »). Logs des chunks utilises.

## Mini pseudo-flux

```text
Thought: Il me faut la politique de delai.
Action: retrieve(query="delai devis site", k=4)
Observation: [chunk A, chunk B]
Thought: Maintenant le dossier client.
Action: crm_get(client="Dupont", mois="2026-03")
Observation: {{"livre_en_jours": 9}}
Action: final_answer(...)
```

## Suite

Un agent sans mesure, c'est du theatre. Dernier article : **observabilite et evaluation**.
""".strip(),
)

_art(
    "agents-hf-observabilite-evaluation",
    title="Observer et evaluer ses agents IA",
    excerpt="Traces, metriques, eval humaine : fiabiliser la boucle Thought-Action-Observation.",
    order=8,
    schema="agents-hf-observability.svg",
    schema_alt="Schema observabilite agents : traces, metriques, eval",
    figcaption="Sans traces, tu ne sais pas pourquoi l'agent a deraille.",
    og_title="Observabilite et eval agents",
    og_sub="Traces, metriques, revue humaine",
    scene="stats",
    faq=[
        ("Quoi logger en priorite ?", "Chaque tool call (nom, args, latence, succes) + la reponse finale + le nombre de steps."),
        ("Eval automatique suffisante ?", "Non seule. Combine checks automatiques et revue humaine sur un echantillon."),
        ("Lien avec le cours HF ?", "Le bonus observability du cours Agents insiste sur monitoring + evaluation - on garde le meme esprit."),
    ],
    body=f"""
Tu as un agent qui « marche en demo ». Bravo. En vrai, il va : boucler, couter cher, inventer un tool, se tromper de client. Le bonus observability du [cours Agents HF]({HF_AGENTS}) insiste la-dessus - on le traduit en checklist terrain.

## Definition citable

L'**observabilite d'un agent** consiste a enregistrer traces (pensees/actions/observations), metriques (latence, cout, succes tools) et evaluations (auto + humaine) pour comprendre et ameliorer son comportement.

## Ce que tu traces

- prompt utilisateur ;
- chaque Thought (si dispo) ;
- chaque Action (tool + args) ;
- chaque Observation (tronquee si enorme) ;
- reponse finale ;
- tokens / cout / duree ;
- raison d'arret (success, max steps, erreur).

Sans ca, « ca a hallucine » reste une legende de Slack.

## Metriques simples qui comptent

Taux de succes tool. Steps moyens. Cout moyen par requete. Taux de fallback (« je ne sais pas »). Satisfaction humaine sur 20 tickets / semaine.

## Eval : trois couches

1. **Unitaires tools** : chaque fonction isolee, tests classiques.
2. **Scenarios agent** : jeux de questions avec reponse attendue / contraintes.
3. **Revue humaine** : echantillon, grille (exactitude, tone, respect des limites).

## Ameliorer sans tout casser

Regarde les traces des echecs. Souvent : description d'outil floue, observation illisible, trop d'outils, max steps trop haut. Corrige le contrat avant de changer de modele.

## Cloture de la serie

Tu sais ce qu'est un agent, comment brancher des tools, suivre ReAct, demarrer avec smolagents, choisir un style d'action et un framework, faire du RAG agentique, et mesurer.

Pour aller plus loin : le [Agents Course Hugging Face]({HF_AGENTS}) (exercices, frameworks, projet final type GAIA). Cote DanielCraft : croise avec la [serie LLM](/blog/series/llm-transformers-serie.html) si tu veux solidifier le socle modeles.

Et rappelle-toi : un agent sans garde-fous, c'est un stagiaire avec les cles du camion. Tu valides, tu limites, tu logs.
""".strip(),
)


def write_collection() -> None:
    COLLECTIONS.mkdir(parents=True, exist_ok=True)
    text = """{
  "id": "hf-agents-serie",
  "title": "Serie Agents Hugging Face : du tool au RAG agentique",
  "description": "Parcours pratique inspire du Agents Course Hugging Face : definition d'agent, tools, ReAct, smolagents, frameworks, RAG agentique et observabilite. Contenu original en francais.",
  "slug": "hf-agents-serie",
  "cover_image": "og/agents-hf-quest-ce-qu-un-agent-1200x630.jpg",
  "articles": [
    "agents-hf-quest-ce-qu-un-agent",
    "agents-hf-outils-et-function-calling",
    "agents-hf-react-pensee-action-observation",
    "agents-hf-smolagents-premier-agent",
    "agents-hf-code-agents-vs-tool-calling",
    "agents-hf-frameworks-llamaindex-langgraph",
    "agents-hf-rag-agentique",
    "agents-hf-observabilite-evaluation"
  ]
}
"""
    # Accents in JSON description
    text = text.replace("Serie Agents", "Série Agents")
    text = text.replace("inspire du", "inspiré du")
    text = text.replace("definition d'agent", "définition d'agent")
    text = text.replace("observabilite", "observabilité")
    text = text.replace("francais", "français")
    (COLLECTIONS / "hf-agents-serie.json").write_text(text, encoding="utf-8")


def fix_accents(s: str) -> str:
    reps = [
        ("Definition citable", "Définition citable"),
        ("definition", "définition"),
        ("systeme", "système"),
        ("decider", "décider"),
        ("modele", "modèle"),
        ("idéalement", "idéalement"),
        ("idealement", "idéalement"),
        ("parametres", "paramètres"),
        ("reponse", "réponse"),
        ("repondre", "répondre"),
        ("etape", "étape"),
        ("etapes", "étapes"),
        ("deja", "déjà"),
        ("coeur", "cœur"),
        ("etre", "être"),
        ("meme", "même"),
        ("Meme", "Même"),
        ("grace", "grâce"),
        ("ca ", "ça "),
        ("Ca ", "Ça "),
        ("ca.", "ça."),
        ("ca,", "ça,"),
        ("ca?", "ça?"),
        ("tâche", "tâche"),
        ("tache ", "tâche "),
        ("taches", "tâches"),
        ("controle", "contrôle"),
        ("controlee", "contrôlée"),
        ("écrire", "écrire"),
        ("ecrire", "écrire"),
        ("executer", "exécuter"),
        ("execution", "exécution"),
        ("executable", "exécutable"),
        ("echantillon", "échantillon"),
        ("ecart", "écart"),
        ("chaine", "chaîne"),
        ("enchainement", "enchaînement"),
        ("enchainements", "enchaînements"),
        ("enchaînements", "enchaînements"),
        ("prefer", "préfér"),
        ("privilegie", "privilégie"),
        ("legere", "légère"),
        ("leger", "léger"),
        ("Leger", "Léger"),
        ("pedagogique", "pédagogique"),
        ("donnee", "donnée"),
        ("donnees", "données"),
        ("metier", "métier"),
        ("metriques", "métriques"),
        ("evaluat", "évaluat"),
        ("Eval ", "Éval "),
        ("evaluation", "évaluation"),
        ("evaluations", "évaluations"),
        ("amelior", "amélior"),
        ("Ameliorer", "Améliorer"),
        ("observabilite", "observabilité"),
        ("Observabilite", "Observabilité"),
        ("deraille", "déraille"),
        ("cout", "coût"),
        ("Cout", "Coût"),
        ("duree", "durée"),
        ("succes", "succès"),
        ("evenement", "événement"),
        ("generique", "générique"),
        ("generer", "générer"),
        ("Generation", "Génération"),
        ("interesse", "intéresse"),
        ("a la ", "à la "),
        ("a le ", "à le "),
        ("a un ", "à un "),
        ("a une ", "à une "),
        ("a des ", "à des "),
        ("a chaque", "à chaque"),
        ("a comprendre", "à comprendre"),
        ("a smolagents", "à smolagents"),
        ("a condition", "à condition"),
        ("inspiree", "inspirée"),
        ("inspire ", "inspiré "),
        ("francais", "français"),
        ("meteo", "météo"),
        ("delai", "délai"),
        ("ouverts", "ouverts"),
        ("Pieges", "Pièges"),
        ("pieges", "pièges"),
        ("perméable", "perméable"),
        ("permeable", "perméable"),
        ("flexibilité", "flexibilité"),
        ("flexibilite", "flexibilité"),
        ("Schema ", "Schéma "),
        ("schema ", "schéma "),
        ("etre ", "être "),
        ("plutot", "plutôt"),
        ("Plutot", "Plutôt"),
        ("maitrise", "maîtrise"),
        ("maitriser", "maîtriser"),
        ("ecosysteme", "écosystème"),
        ("enterprise", "enterprise"),
        ("œ", "œ"),
        ("cloture", "clôture"),
        ("Cloture", "Clôture"),
        ("theatre", "théâtre"),
        ("la-dessus", "là-dessus"),
        ("la dessus", "là-dessus"),
        ("des le ", "dès le "),
        ("Des le ", "Dès le "),
        ("arrete", "arrête"),
        ("arret", "arrêt"),
        ("numero", "numéro"),
        ("etoile", "étoile"),
        ("géant", "géant"),
        ("geant", "géant"),
        ("geants", "géants"),
        ("pouvoirs", "pouvoirs"),
        ("necessaire", "nécessaire"),
        ("especes", "espèces"),
        ("referer", "référer"),
        ("role", "rôle"),
        ("Role", "Rôle"),
        ("eleve", "élevé"),
        ("securité", "sécurité"),
        ("securite", "sécurité"),
        ("perimetre", "périmètre"),
        ("acces", "accès"),
        ("Acces", "Accès"),
        ("memoire", "mémoire"),
        ("defaut", "défaut"),
        ("par defaut", "par défaut"),
        ("reseau", "réseau"),
        ("derriere", "derrière"),
        ("s'arrete", "s'arrête"),
        ("n'en copie", "n'en copie"),
        ("aidé", "aidé"),
        ("traversee", "traversée"),
        ("qualite", "qualité"),
        ("fidelite", "fidélité"),
        ("integrer", "intégrer"),
        ("integre", "intègre"),
        ("recuperer", "récupérer"),
        ("Recuperer", "Récupérer"),
        ("multi-etapes", "multi-étapes"),
        ("annonce", "annoncé") if False else ("", ""),
    ]
    for a, b in reps:
        if a and a != b:
            s = s.replace(a, b)
    # Fix over-replacements in code/URLs carefully - undo common damage
    s = s.replace("modèle = HfApiModèle()", "model = HfApiModel()")
    s = s.replace("modèle=modèle", "model=model")
    s = s.replace("HfApiModèle", "HfApiModel")
    s = s.replace("CodeAgent(tools=[average], modèle=model)", "CodeAgent(tools=[average], model=model)")
    s = s.replace("pip install smolagents", "pip install smolagents")
    s = s.replace("définition citable", "Définition citable")
    s = s.replace("## Définition citable", "## Définition citable")
    s = s.replace("à le ", "au ")  # rough
    s = s.replace("à le\n", "au\n")
    return s


def write_articles() -> None:
    ARTICLES.mkdir(parents=True, exist_ok=True)
    for i, slug in enumerate(ORDER):
        meta = CONTENT[slug]
        # Accents on visible French - apply carefully to body only after building
        title = meta["title"]
        excerpt = meta["excerpt"]
        # Minimal accent fixes on title/excerpt
        for old, new in [
            ("definition", "définition"),
            ("Decrire", "Décrire"),
            ("coeur", "cœur"),
            ("pensee", "pensée"),
            ("facons", "façons"),
            ("generer", "générer"),
            ("executable", "exécutable"),
            ("legerete", "légèreté"),
            ("Au-dela", "Au-delà"),
            ("metriques", "métriques"),
            ("fiabiliser", "fiabiliser"),
        ]:
            title = title.replace(old, new)
            excerpt = excerpt.replace(old, new)

        body = fix_accents(meta["body"])
        # Repair code identifiers broken by accent pass
        repairs = [
            ("modèle = HfApiModel()", "model = HfApiModel()"),
            ("CodeAgent(tools=[average], modèle=model)", "CodeAgent(tools=[average], model=model)"),
            ("llm.chat(messages, tools=TOOL_SCHEMAS)", "llm.chat(messages, tools=TOOL_SCHEMAS)"),
            ("out.modèle", "out.model") if False else ("", ""),
            ("{{", "{"),
            ("}}", "}"),
        ]
        # Wait - body uses doubled braces for format - we used f-strings with {{ already resolved
        # Actually CONTENT body was built with f-strings so {{ became {. Good.
        for a, b in repairs:
            if a:
                body = body.replace(a, b)

        faq_lines = ["\n---\n\n## Questions fréquentes (FAQ)\n"]
        for q, a in meta["faq"]:
            faq_lines.append(f"**{fix_accents(q)}** {fix_accents(a)}\n")

        nav = ["\n---\n\n## Navigation dans la série\n"]
        if i > 0:
            prev = ORDER[i - 1]
            nav.append(f"- Précédent : [{CONTENT[prev]['title']}](/blog/articles/{prev}.html)")
        if i < len(ORDER) - 1:
            nxt = ORDER[i + 1]
            nav.append(f"- Suivant : [{CONTENT[nxt]['title']}](/blog/articles/{nxt}.html)")
        else:
            nav.append(
                "- Fin de la série Agents - croise avec la [série LLM](/blog/series/llm-transformers-serie.html) ou le [Agents Course HF](https://huggingface.co/learn/agents-course)."
            )

        date = f"2026-10-{3 + i:02d}"
        md = f"""---
title: "{title}"
date: {date}
excerpt: "{excerpt}"
type: tutorial
tags: [agents IA, Hugging Face, smolagents, ReAct, formation, LLM]
series: {SERIES}
series_order: {meta['order']}
og_image: {slug}-1200x630.jpg
---

# {title}

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/{meta['schema']}" alt="{fix_accents(meta['schema_alt'])}" class="schema-inline" width="640" />
  <figcaption>{fix_accents(meta['figcaption'])}</figcaption>
</figure>

{body}
{''.join(faq_lines)}
{chr(10).join(nav)}
"""
        # Fix common over-accent issues in FAQ/titles after write prep
        md = md.replace("à le runtime", "au runtime")
        md = md.replace("à le monde", "au monde")
        md = md.replace("Schéma d'outil", "schéma d'outil")
        (ARTICLES / f"{slug}.md").write_text(md, encoding="utf-8")
        print(f"  article {slug}")


def write_ogs() -> None:
    OG_DIR.mkdir(parents=True, exist_ok=True)
    scenes_ok = {"assistant", "code", "process", "gear", "catalog", "report", "stats", "browser"}
    for slug in ORDER:
        meta = CONTENT[slug]
        scene = meta["scene"] if meta["scene"] in scenes_ok else "browser"
        img = render_og_card(
            title=meta["og_title"][:70],
            subtitle=meta["og_sub"][:80],
            badge="Agents",
            chips=["HF", "smolagents"],
            scene=scene,
            cta="Lire l'article →",
            color="#4da9d6",
        )
        out = OG_DIR / f"{slug}-1200x630.jpg"
        img.save(out, "JPEG", quality=88, optimize=True)
        print(f"  og {out.name}")


def link_from_llm_series() -> None:
    """Ajoute un pont depuis le dernier article LLM vers la serie Agents."""
    path = ARTICLES / "llm-finetuning-avance-lora-reasoning.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    tip = (
        "\n\nPour la suite cote agents (tools, ReAct, smolagents), enchaine avec la "
        "[série Agents Hugging Face](/blog/series/hf-agents-serie.html) - le pendant pratique "
        "du [Agents Course](https://huggingface.co/learn/agents-course).\n"
    )
    tip = tip.replace("cote", "côté").replace("enchaine", "enchaîne")
    if "hf-agents-serie" not in text:
        if "## Navigation dans la série" in text:
            text = text.replace("## Navigation dans la série", tip + "\n## Navigation dans la série")
        else:
            text = text.rstrip() + tip
        path.write_text(text, encoding="utf-8")
        print("  link LLM -> Agents")


def main() -> int:
    print("== schemas ==")
    write_schemas()
    print("== collection ==")
    write_collection()
    print("== articles ==")
    write_articles()
    print("== og ==")
    write_ogs()
    print("== cross-link ==")
    link_from_llm_series()
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
