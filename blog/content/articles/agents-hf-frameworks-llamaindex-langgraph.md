---
title: "Trois boîtes à outils : laquelle choisir ?"
date: 2026-10-08
excerpt: "smolagents, LlamaIndex, LangGraph : trois approches, trois moments. Une carte simple pour ne pas se perdre."
type: tutorial
tags: [agents IA, smolagents, LlamaIndex, LangGraph, formation, débutant]
series: hf-agents-serie
series_order: 6
og_image: agents-hf-frameworks-llamaindex-langgraph-1200x630.jpg
---

# Trois boîtes à outils : laquelle choisir ?

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-frameworks.svg" alt="Schéma smolagents, LlamaIndex, LangGraph" class="schema-inline" width="800" />
  <figcaption>Trois options : démarrer vite, documents, parcours contrôlé.</figcaption>
</figure>

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-frameworks-illustration.jpg" alt="Illustration trois boîtes à outils agents" class="schema-inline" width="800" loading="lazy" />
  <figcaption>smolagents, LlamaIndex, LangGraph - choisis selon ton besoin.</figcaption>
</figure>

Le [cours Agents Hugging Face](https://huggingface.co/learn/agents-course) présente plusieurs frameworks.  
Voici la version « dis voir clairement » - sans guerre de religion.

## Les 3 en une ligne chacun

**smolagents**  
Pour démarrer vite, comprendre la boucle, faire une démo.

**LlamaIndex**  
Quand la réponse dépend surtout de **tes documents** (FAQ, PDF, fiches).

**LangGraph**  
Quand tu veux un **parcours** clair : étape A, puis B, ou branche humaine.

## Analogie magasin

- smolagents = caisse d'apprentissage ;  
- LlamaIndex = rayonnage + inventaire de ta doc ;  
- LangGraph = plan de salle avec flèches (si client devis → validation).

## Comment choisir (règle courte)

1. Tu apprends ? → **smolagents**  
2. Tu as beaucoup de textes internes ? → **LlamaIndex**  
3. Tu as un process métier avec des « si / sinon » ? → **LangGraph**

Tu n'as pas besoin des trois demain matin.

## Ce qui compte plus que le logo

- outils bien décrits ;
- boucle limitée ;
- traces lisibles ;
- droits serrés.

Un mauvais design d'outils avec le « meilleur » framework reste mauvais.

## En résumé

Choisis selon le besoin, pas selon le hype.  
Ensuite on regarde le cas « chercher dans ta doc » (RAG agentique) - encore en français simple.

---

## Questions fréquentes (FAQ)

**Je dois tout apprendre ?**  
Non. Un d'abord. Sache lire les deux autres.

**LangChain dans l'histoire ?**  
LangGraph est la brique « parcours » de cet écosystème. Retiens surtout l'idée de graphe.

**Pour un POC commerce ?**  
Souvent : outils contrôlés + smolagents ou un appel d'outil simple. LlamaIndex si tu as une vraie FAQ à indexer.

---

## Navigation dans la série

- Précédent : [Code libre ou outil contrôlé : comment choisir ?](/blog/articles/agents-hf-code-agents-vs-tool-calling.html)
- Suivant : [Chercher dans ta doc, puis répondre](/blog/articles/agents-hf-rag-agentique.html)
