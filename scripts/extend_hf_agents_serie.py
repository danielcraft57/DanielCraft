#!/usr/bin/env python3
"""Etend la serie Agents HF : function-calling FT, LangGraph, LlamaIndex, multi-agents."""
from __future__ import annotations

import json
import sys
from pathlib import Path

_SCRIPT = Path(__file__).resolve().parent
ROOT = _SCRIPT.parent
sys.path.insert(0, str(_SCRIPT))

from _og_cartoon import render_og_card  # noqa: E402

ART = ROOT / "blog" / "content" / "articles"
COL = ROOT / "blog" / "content" / "collections"
SCH = ROOT / "assets" / "images" / "blog" / "schemas"
OG = ROOT / "assets" / "images" / "og"
HF = "https://huggingface.co/learn/agents-course"
SERIES = "hf-agents-serie"

FULL_ORDER = [
    "agents-hf-quest-ce-qu-un-agent",
    "agents-hf-outils-et-function-calling",
    "agents-hf-react-pensee-action-observation",
    "agents-hf-smolagents-premier-agent",
    "agents-hf-code-agents-vs-tool-calling",
    "agents-hf-frameworks-llamaindex-langgraph",
    "agents-hf-rag-agentique",
    "agents-hf-observabilite-evaluation",
    "agents-hf-finetune-function-calling",
    "agents-hf-langgraph-premier-graphe",
    "agents-hf-llamaindex-agent-donnees",
    "agents-hf-multi-agents-vision-browser",
]

TITLES = {
    "agents-hf-quest-ce-qu-un-agent": "Agents IA : c'est quoi, au juste ?",
    "agents-hf-outils-et-function-calling": "Tools et function calling : donner des mains au LLM",
    "agents-hf-react-pensee-action-observation": "ReAct : pensée, action, observation",
    "agents-hf-smolagents-premier-agent": "Premier agent avec smolagents",
    "agents-hf-code-agents-vs-tool-calling": "Code agents vs tool-calling JSON",
    "agents-hf-frameworks-llamaindex-langgraph": "smolagents, LlamaIndex, LangGraph : quoi choisir ?",
    "agents-hf-rag-agentique": "RAG agentique : chercher, puis raisonner",
    "agents-hf-observabilite-evaluation": "Observer et évaluer ses agents IA",
    "agents-hf-finetune-function-calling": "Fine-tuner un LLM pour le function calling",
    "agents-hf-langgraph-premier-graphe": "LangGraph : ton premier graphe d'agent",
    "agents-hf-llamaindex-agent-donnees": "LlamaIndex : agents branchés sur tes données",
    "agents-hf-multi-agents-vision-browser": "Multi-agents, vision et navigateur",
}


def svg(path: Path, title: str, caption: str, boxes: list[str]) -> None:
    n = len(boxes)
    gap, box_w = 12, min(150, (760 - 12 * (n - 1)) // n)
    start = (800 - (n * box_w + (n - 1) * gap)) // 2
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" role="img">',
        f'  <title>{title}</title><desc>{caption}</desc>',
        '  <rect width="800" height="420" fill="#f5f7fb"/>',
        f'  <text x="400" y="36" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="18" font-weight="700" fill="#0f172a">{title}</text>',
        '  <defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#0f172a"/></marker></defs>',
    ]
    for i, label in enumerate(boxes):
        x = start + i * (box_w + gap)
        stroke = "#dc2626" if i == n - 1 else ("#2563eb" if i % 2 == 0 else "#60a5fa")
        lines = label.split("\n")
        parts.append(f'  <rect x="{x}" y="160" width="{box_w}" height="70" rx="8" fill="#fff" stroke="{stroke}" stroke-width="2"/>')
        if len(lines) == 1:
            parts.append(f'  <text x="{x+box_w/2}" y="200" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="12" font-weight="600" fill="#0f172a">{lines[0]}</text>')
        else:
            parts.append(f'  <text x="{x+box_w/2}" y="192" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="11" font-weight="600" fill="#0f172a">{lines[0]}</text>')
            parts.append(f'  <text x="{x+box_w/2}" y="210" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="11" font-weight="600" fill="#0f172a">{lines[1]}</text>')
        if i < n - 1:
            parts.append(f'  <path d="M{x+box_w} 195 H{x+box_w+gap-10}" stroke="#0f172a" stroke-width="2" fill="none" marker-end="url(#a)"/>')
    parts.append(f'  <text x="400" y="390" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif" font-size="12" fill="#0f172a">{caption}</text></svg>\n')
    path.write_text("\n".join(parts), encoding="utf-8")


NEW = [
    {
        "slug": "agents-hf-finetune-function-calling",
        "order": 9,
        "date": "2026-10-11",
        "title": TITLES["agents-hf-finetune-function-calling"],
        "excerpt": "Quand le prompting ne suffit plus : adapter un modèle à appeler tes outils proprement.",
        "schema": "agents-hf-finetune-fc.svg",
        "boxes": ["Dataset\nappels", "Fine-tune", "Eval\ntools", "Agent\nplus fiable"],
        "caption": "Fine-tuning orienté function calling.",
        "og_title": "Fine-tune function calling",
        "og_sub": "Adapter le modèle à tes outils",
        "scene": "stats",
        "faq": [
            ("Prompting vs fine-tune ?", "Commence par de bons schemas d'outils. Fine-tune si le modèle rate souvent le format ou le bon tool."),
            ("Combien d'exemples ?", "Des centaines de paires propres battent des milliers de lignes bruyantes."),
            ("Ça remplace ReAct ?", "Non : tu améliores le cerveau. La boucle et les garde-fous restent."),
        ],
        "body": f"""
Le bonus du [cours Agents Hugging Face]({HF}) sur le fine-tuning function-calling répond à un vrai problème : parfois le modèle **comprend** la tâche mais **rate** l'appel d'outil (mauvais nom, mauvais JSON, outil inventé).

## Définition citable

Le **fine-tuning pour function calling** consiste à entraîner (ou adapter) un modèle sur des exemples d'appels d'outils corrects, pour qu'il propose plus fiablement le bon tool avec les bons arguments.

## Quand ça vaut le coup

- ton domaine a des tools très spécifiques (CRM maison, devis Metz, stock) ;
- le modèle de base se trompe souvent de signature ;
- tu as déjà une allowlist stable d'outils.

Quand ça ne vaut pas le coup : 3 tools génériques et un bon prompt système. Là, itère d'abord sur les descriptions.

## À quoi ressemble un exemple d'entraînement

```json
{{
  "messages": [
    {{"role": "user", "content": "Vous êtes ouverts samedi ?"}},
    {{
      "role": "assistant",
      "tool_calls": [{{
        "type": "function",
        "function": {{
          "name": "get_horaires_boutique",
          "arguments": "{{\\"jour\\": \\"samedi\\"}}"
        }}
      }}]
    }},
    {{"role": "tool", "name": "get_horaires_boutique", "content": "10h-17h"}},
    {{"role": "assistant", "content": "Oui, samedi on ouvre de 10h à 17h."}}
  ]
}}
```

Varie les formulations utilisateur. Inclus des cas « pas besoin de tool ». Inclus des erreurs tool (API down) pour apprendre à répondre proprement.

## Méthode pragmatique

1. Logge les échecs réels de ton agent (mauvais tool / args).
2. Transforme-les en exemples corrigés.
3. Adapte avec LoRA / PEFT si le budget GPU est limité (voir la [série LLM](/blog/series/llm-transformers-serie.html)).
4. Évalue sur un set gelé de scénarios tool - pas seulement la perplexité.

## Pièges

Dataset qui ne contient que des succès : le modèle n'apprend pas le refus. Arguments en texte libre alors que tu veux un enum. Oublier de versionner le schéma d'outils avec le checkpoint.

## Lien série

Après l'observabilité, le fine-tune est le levier « cerveau ». Ensuite on passe au **contrôle de flux** avec LangGraph.
""".strip(),
    },
    {
        "slug": "agents-hf-langgraph-premier-graphe",
        "order": 10,
        "date": "2026-10-12",
        "title": TITLES["agents-hf-langgraph-premier-graphe"],
        "excerpt": "Nœuds, arêtes, état partagé : construire un agent dont le flux est explicite.",
        "schema": "agents-hf-langgraph.svg",
        "boxes": ["Etat", "Noeuds", "Aretes\ncondition", "Reponse"],
        "caption": "LangGraph : l'agent comme un graphe contrôlé.",
        "og_title": "LangGraph : premier graphe",
        "og_sub": "Contrôler le flux de l'agent",
        "scene": "process",
        "faq": [
            ("LangGraph vs smolagents ?", "smolagents = démarrer vite. LangGraph = contrôler les chemins, retries, humain dans la boucle."),
            ("Obligatoire en prod ?", "Non. Utile dès que le flux métier a des branches et des validations."),
            ("C'est du no-code ?", "Non : tu codes le graphe. L'UI éventuelle ne remplace pas le design d'état."),
        ],
        "body": f"""
Dans le [cours Agents HF]({HF}), **LangGraph** arrive quand tu veux plus qu'une boucle libre : un **flux métier** visible.

## Définition citable

**LangGraph** est un framework qui modélise un agent (ou un workflow LLM) comme un **graphe d'états** : nœuds qui transforment l'état, arêtes (parfois conditionnelles) qui décident la suite.

## Pourquoi un graphe

Un agent « while True + tools » marche en démo. En prod tu veux :
- brancher « si montant > 500 € → validation humaine » ;
- retry un tool sans recommencer tout ;
- tracer quel nœud a planté.

Le graphe rend ça explicite.

## Briques mentales

**State** : ce que tu transportes (messages, flags, résultats tools).
**Node** : une fonction qui lit/écrit le state (appeler le LLM, exécuter un tool, formater).
**Edge** : transition fixe ou conditionnelle (`if needs_review`).

## Mini squelette (esprit)

```python
# Pseudo-code conceptuel LangGraph
from typing import TypedDict

class AgentState(TypedDict):
    messages: list
    needs_human: bool

def call_model(state: AgentState) -> AgentState:
    # LLM + tool calling éventuel
    return state

def maybe_human(state: AgentState) -> str:
    return "human" if state.get("needs_human") else "end"

# builder.add_node("agent", call_model)
# builder.add_conditional_edges("agent", maybe_human, ...)
```

Tu ne copies pas une API figée : tu retiens l'idée **état + nœuds + conditions**.

## Cas boutique

1. Nœud `parse_intent`  
2. Nœud `tools` (horaires / devis)  
3. Condition : si devis personnalisé → nœud `notify_humain`  
4. Nœud `reply`

L'utilisateur voit une réponse. Toi tu vois le chemin dans les traces.

## Erreurs fréquentes

Trop de nœuds trop tôt. État fourre-tout illisible. Conditions cachées dans le prompt au lieu d'arêtes. Commence petit : 3 nœuds, une branche.

## Suite

LlamaIndex pour quand le cœur du problème, c'est **tes documents et index** - pas seulement le graphe.
""".strip(),
    },
    {
        "slug": "agents-hf-llamaindex-agent-donnees",
        "order": 11,
        "date": "2026-10-13",
        "title": TITLES["agents-hf-llamaindex-agent-donnees"],
        "excerpt": "Index, retrievers et agents : répondre avec ta doc, pas avec des inventés.",
        "schema": "agents-hf-llamaindex.svg",
        "boxes": ["Docs", "Index", "Agent\n+ tools", "Reponse\ncitee"],
        "caption": "LlamaIndex : l'agent vit sur tes données.",
        "og_title": "LlamaIndex : agents et données",
        "og_sub": "Indexer puis laisser l'agent chercher",
        "scene": "catalog",
        "faq": [
            ("LlamaIndex = seulement RAG ?", "Non, mais c'est sa force. Les agents y excellent quand la réponse dépend de corpus."),
            ("Remplace smolagents ?", "Complémentaire. Choisis selon data-centric vs code-agent léger."),
            ("Citations ?", "Exige-les dans le design : chunk id, fichier, ancre - sinon tu rejoues l'hallucination."),
        ],
        "body": f"""
**LlamaIndex**, dans le [cours Agents]({HF}), pousse une idée simple : un agent utile sur entreprise commence souvent par **tes fichiers**, pas par un LLM nu.

## Définition citable

**LlamaIndex** fournit des briques pour ingérer, indexer et interroger des données, puis brancher des **agents / workflows** qui utilisent ces index comme outils de retrieval.

## Pipeline mental

1. Charger des docs (PDF devis type, FAQ, CGV).  
2. Chunk + embed → index.  
3. Exposer un tool `retrieve_faq(query)`.  
4. L'agent décide quand l'appeler (RAG agentique, pas retrieve aveugle à chaque fois).

## Mini esprit d'usage

```python
# Esprit LlamaIndex (API simplifiée)
# documents = SimpleDirectoryReader("data/faq").load_data()
# index = VectorStoreIndex.from_documents(documents)
# query_engine = index.as_query_engine()
# agent = ReActAgent.from_tools([query_engine_tool, horaires_tool], llm=llm)
# agent.chat("Quel délai pour un devis vitrine ?")
```

L'intérêt : la retrieval n'est plus un script à part, c'est un **outil** de l'agent.

## Qualité des données > modèle

Mauvais chunks → mauvaises réponses, même avec GPT géant. Soigne titres, métadonnées (ville, type page), fraîcheur. Un commerce du Grand Est gagne plus à indexer une FAQ claire qu'à changer de LLM chaque mois.

## Pièges

Tout mettre dans un seul index fourre-tout. Oublier les mises à jour (doc obsolète = agent confiant et faux). Laisser l'agent répondre sans source quand le retrieve est vide.

## Suite

Dernier bonus de la série : **multi-agents**, vision et navigateur - quand un seul agent ne suffit plus.
""".strip(),
    },
    {
        "slug": "agents-hf-multi-agents-vision-browser",
        "order": 12,
        "date": "2026-10-14",
        "title": TITLES["agents-hf-multi-agents-vision-browser"],
        "excerpt": "Orchestrer plusieurs agents, lire une image, naviguer le web : puissance et risques.",
        "schema": "agents-hf-multi.svg",
        "boxes": ["Manager", "Agent\nrecherche", "Agent\nvision", "Synthese"],
        "caption": "Plusieurs agents spécialisés sous un chef d'orchestre.",
        "og_title": "Multi-agents, vision, browser",
        "og_sub": "Spécialiser sans perdre le contrôle",
        "scene": "gallery",
        "faq": [
            ("Toujours multi-agent ?", "Non. Un agent + 4 tools clairs bat souvent 5 agents mal briefés."),
            ("Browser agent = dangereux ?", "Oui : phishing, fuites, actions irréversibles. Sandbox, allowlist de domaines, humain sur actions sensibles."),
            ("Vision sert à quoi concrètement ?", "Lire un screenshot d'erreur, une étiquette produit, une maquette - pas décorer le pitch."),
        ],
        "body": f"""
Le module smolagents du [cours Agents HF]({HF}) ouvre aussi **multi-agents**, **vision** et **browser**. Puissant. Facile à transformer en chaos.

## Définition citable

Un **système multi-agents** répartit une tâche entre plusieurs agents spécialisés (recherche, code, critique…) coordonnés par un orchestrateur ; les agents **vision** / **browser** ajoutent la perception d'images ou d'pages web.

## Pourquoi plusieurs agents

Séparation des rôles :
- un agent « chercheur » (retrieve + web) ;
- un agent « rédacteur » ;
- un agent « vérifieur » (checklist, citations).

Le manager ne fait pas tout : il délègue et fusionne.

## Quand rester mono-agent

Tâche courte, tools bornés, besoin de latence basse. Exemple : horaires + délai devis. Multi-agent ici = overhead pour rien.

## Vision

Tu passes une image (photo rayon, capture bug). L'agent décrit / extrait, puis peut appeler un tool métier. Garde-fou : ne jamais traiter une image comme vérité absolue (OCR peut se tromper).

## Browser

L'agent navigue, clique, lit le DOM. Cas utile : comparer un concurrent, vérifier une page publique. Cas dangereux : comptes connectés, formulaires de paiement, sites hors allowlist.

Règles minimales :
- domaines autorisés ;
- pas de credentials en clair dans le prompt ;
- confirmation humaine avant action à effet de bord ;
- logs de chaque URL visitée.

## Mini architecture

```text
User
  -> ManagerAgent
       -> ResearchAgent (retrieve / browser allowlist)
       -> VisionAgent (si image jointe)
       -> WriterAgent
  <- réponse + sources + trace
```

## Clôture élargie de la série

Tu as le socle (agent, tools, ReAct, smolagents), les choix de framework, le RAG agentique, l'obs, le fine-tune function calling, LangGraph, LlamaIndex, et les patterns avancés multi-agents / vision / browser.

Le [Agents Course Hugging Face]({HF}) reste la référence pour les labs et le projet type GAIA. Ici tu as la carte en français, orientée terrain.

Prochaine lecture utile si tu reviens aux modèles purs : la [série LLM & Transformers](/blog/series/llm-transformers-serie.html).
""".strip(),
    },
]


def write_article(item: dict) -> None:
    slug = item["slug"]
    order = item["order"]
    idx = FULL_ORDER.index(slug)
    faq = ["\n---\n\n## Questions fréquentes (FAQ)\n"]
    for q, a in item["faq"]:
        faq.append(f"**{q}** {a}\n")
    nav = ["\n---\n\n## Navigation dans la série\n"]
    if idx > 0:
        prev = FULL_ORDER[idx - 1]
        nav.append(f"- Précédent : [{TITLES[prev]}](/blog/articles/{prev}.html)")
    if idx < len(FULL_ORDER) - 1:
        nxt = FULL_ORDER[idx + 1]
        nav.append(f"- Suivant : [{TITLES[nxt]}](/blog/articles/{nxt}.html)")
    else:
        nav.append(
            "- Fin de la série Agents (parcours élargi) - retour au [Agents Course HF](https://huggingface.co/learn/agents-course) ou à la [série LLM](/blog/series/llm-transformers-serie.html)."
        )
    schema_file = item["schema"]
    md = f"""---
title: "{item['title']}"
date: {item['date']}
excerpt: "{item['excerpt']}"
type: tutorial
tags: [agents IA, Hugging Face, smolagents, LangGraph, LlamaIndex, formation]
series: {SERIES}
series_order: {order}
og_image: {slug}-1200x630.jpg
---

# {item['title']}

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/{schema_file}" alt="Schéma {item['title']}" class="schema-inline" width="640" />
  <figcaption>{item['caption']}</figcaption>
</figure>

{item['body']}
{''.join(faq)}
{chr(10).join(nav)}
"""
    # Unescape JSON braces from doubled braces in f-string bodies
    md = md.replace("{{", "{").replace("}}", "}")
    (ART / f"{slug}.md").write_text(md, encoding="utf-8")
    print(f"  article {slug}")


def patch_observability_nav() -> None:
    path = ART / "agents-hf-observabilite-evaluation.md"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    text = text.replace("Clôture de la serie", "Clôture de la vague 1")
    old_nav = """## Navigation dans la série

- Précédent : [RAG agentique : chercher, puis raisonner](/blog/articles/agents-hf-rag-agentique.html)
- Fin de la série Agents - croise avec la [série LLM](/blog/series/llm-transformers-serie.html) ou le [Agents Course HF](https://huggingface.co/learn/agents-course).
"""
    new_nav = f"""## Navigation dans la série

- Précédent : [{TITLES['agents-hf-rag-agentique']}](/blog/articles/agents-hf-rag-agentique.html)
- Suivant : [{TITLES['agents-hf-finetune-function-calling']}](/blog/articles/agents-hf-finetune-function-calling.html)
"""
    if "agents-hf-finetune-function-calling" not in text:
        if old_nav in text:
            text = text.replace(old_nav, new_nav)
        else:
            text = text.replace(
                "- Fin de la série Agents - croise avec la [série LLM](/blog/series/llm-transformers-serie.html) ou le [Agents Course HF](https://huggingface.co/learn/agents-course).",
                f"- Suivant : [{TITLES['agents-hf-finetune-function-calling']}](/blog/articles/agents-hf-finetune-function-calling.html)",
            )
        path.write_text(text, encoding="utf-8")
        print("  patched observabilite nav")


def write_collection() -> None:
    data = {
        "id": "hf-agents-serie",
        "title": "Série Agents Hugging Face : du tool au multi-agents",
        "description": (
            "Parcours pratique inspiré du Agents Course Hugging Face : définition d'agent, tools, "
            "ReAct, smolagents, frameworks, RAG agentique, observabilité, fine-tune function calling, "
            "LangGraph, LlamaIndex, multi-agents et vision. Contenu original en français."
        ),
        "slug": "hf-agents-serie",
        "cover_image": "og/agents-hf-quest-ce-qu-un-agent-1200x630.jpg",
        "articles": FULL_ORDER,
    }
    (COL / "hf-agents-serie.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("  collection updated")


def main() -> int:
    SCH.mkdir(parents=True, exist_ok=True)
    OG.mkdir(parents=True, exist_ok=True)
    print("== bonus articles ==")
    for item in NEW:
        svg(SCH / item["schema"], item["og_title"][:40], item["caption"], item["boxes"])
        write_article(item)
        img = render_og_card(
            title=item["og_title"][:70],
            subtitle=item["og_sub"][:80],
            badge="Agents",
            chips=["HF", "bonus"],
            scene=item["scene"] if item["scene"] in {"stats", "process", "catalog", "gallery", "code", "browser"} else "browser",
            cta="Lire l'article →",
            color="#4da9d6",
        )
        out = OG / f"{item['slug']}-1200x630.jpg"
        img.save(out, "JPEG", quality=88, optimize=True)
        print(f"  og {out.name}")
    patch_observability_nav()
    write_collection()
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
