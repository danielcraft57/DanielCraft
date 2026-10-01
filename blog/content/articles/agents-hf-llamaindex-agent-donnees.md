---
title: "Agent + tes documents (LlamaIndex)"
date: 2026-10-13
excerpt: "Indexer ta FAQ, laisser l'agent chercher dedans : répondre avec tes textes, pas avec des inventions."
type: tutorial
tags: [agents IA, LlamaIndex, FAQ, formation, débutant]
series: hf-agents-serie
series_order: 11
og_image: agents-hf-llamaindex-agent-donnees-1200x630.jpg
---

# Agent + tes documents (LlamaIndex)

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-llamaindex.svg" alt="Schéma : docs, index, agent, réponse citée" class="schema-inline" width="800" />
  <figcaption>Tes docs → index → l'agent cherche → réponse sourcée.</figcaption>
</figure>

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-llamaindex-illustration.jpg" alt="Illustration agent branché sur la documentation" class="schema-inline" width="800" loading="lazy" />
  <figcaption>Ta FAQ indexée, l'agent qui cherche, la réponse citée.</figcaption>
</figure>

**LlamaIndex**, dans le [cours Agents HF](https://huggingface.co/learn/agents-course), pousse une idée simple :  
beaucoup d'agents utiles commencent par **tes fichiers**, pas par un modèle nu.

## En une phrase

Tu ranges ta doc pour qu'on puisse la chercher. L'agent s'en sert comme d'un outil.

## Pipeline mental

1. Charger FAQ / fiches.  
2. Les découper et les indexer.  
3. Exposer un outil « cherche dans la FAQ ».  
4. L'agent décide quand l'appeler.

## Pour un commerce

20 pages de FAQ propres battent 2 Go de drive bordélique.  
Titres clairs. Infos à jour. Pas les salaires à côté des allergènes.

## Citations

Impose un format : réponse + source.  
Si rien trouvé : le dire.  
Confiance > bluff.

## En résumé

LlamaIndex = rayonnage intelligent de ta doc + agent qui sait chercher.  
Complémentaire de smolagents / LangGraph, pas forcément un remplacement.

Dernier article : multi-agents, vision, navigateur - puissant, à manier avec prudence.

---

## Questions fréquentes (FAQ)

**Seulement du RAG ?**  
C'est sa force. Les agents y sont naturels dès que la réponse dépend du corpus.

**Ça remplace smolagents ?**  
Complémentaire. Choisis selon « je débute » vs « j'ai beaucoup de docs ».

**Pourquoi citer ?**  
Pour que le client (et toi) puissiez vérifier.

---

## Navigation dans la série

- Précédent : [Un parcours en étapes (LangGraph)](/blog/articles/agents-hf-langgraph-premier-graphe.html)
- Suivant : [Plusieurs spécialistes, vision, navigateur](/blog/articles/agents-hf-multi-agents-vision-browser.html)
