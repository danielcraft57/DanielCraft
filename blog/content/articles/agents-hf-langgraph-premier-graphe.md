---
title: "Un parcours en étapes (LangGraph)"
date: 2026-10-12
excerpt: "Comme un plan de salle : étape A, puis B, ou branche humaine. L'idée de LangGraph sans se noyer."
type: tutorial
tags: [agents IA, LangGraph, formation, débutant]
series: hf-agents-serie
series_order: 10
og_image: agents-hf-langgraph-premier-graphe-1200x630.jpg
---

# Un parcours en étapes (LangGraph)

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-langgraph.svg" alt="Schéma : état, étapes, choix, fin" class="schema-inline" width="800" />
  <figcaption>État → étapes → choix → fin (réponse ou humain).</figcaption>
</figure>

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-langgraph-illustration.jpg" alt="Illustration parcours en étapes type plan de salle" class="schema-inline" width="800" loading="lazy" />
  <figcaption>Comme un plan : entrée, branche, validation, réponse.</figcaption>
</figure>

Une boucle libre, c'est bien pour apprendre.  
Un process métier, souvent, veut des **flèches** : si devis custom → validation humaine, sinon réponse auto.

**LangGraph** (vu dans le [cours Agents HF](https://huggingface.co/learn/agents-course)) pense l'agent comme un **parcours** : cases et flèches.

## En une phrase

Tu dessines les étapes. L'agent suit le plan. Tu sais où ça a planté.

## Analogie

C'est un plan de salle au magasin :

1. entrée (comprendre la demande) ;  
2. rayonnage FAQ **ou** comptoir devis ;  
3. si devis → chef de rayon valide ;  
4. sortie (réponse client).

## Les mots utiles (sans jargon lourd)

- **État** : ce qu'on sait déjà (messages, flags).  
- **Étape** : une action (appeler le modèle, un outil, prévenir un humain).  
- **Choix** : si / sinon.

## Mini parcours boutique

1. Comprendre l'intention.  
2. Si horaires → outil horaires → répondre.  
3. Si devis → collecter infos → brouillon → **humain valide** → envoyer.  
4. Sinon → « je passe la main ».

## Quand tu n'en as pas besoin

Question simple + 2 outils + boucle courte : smolagents suffit.  
LangGraph brille quand les branches métier existent vraiment.

## En résumé

Dessine d'abord sur papier.  
Code ensuite.  
Garde peu d'étapes au début.

Suite : **LlamaIndex** - quand le cœur du problème, c'est ta documentation.

---

## Questions fréquentes (FAQ)

**Obligatoire en prod ?**  
Non. Utile dès qu'il y a des branches et des validations.

**C'est du no-code ?**  
Non. Tu définis le parcours en code (parfois avec UI autour).

**smolagents ou LangGraph ?**  
Apprendre / démo → smolagents. Process contrôlé → LangGraph.

---

## Navigation dans la série

- Précédent : [Mieux appeler les outils (fine-tune)](/blog/articles/agents-hf-finetune-function-calling.html)
- Suivant : [Agent + tes documents (LlamaIndex)](/blog/articles/agents-hf-llamaindex-agent-donnees.html)
