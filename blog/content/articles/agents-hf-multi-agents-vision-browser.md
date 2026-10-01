---
title: "Plusieurs spécialistes, vision, navigateur"
date: 2026-10-14
excerpt: "Un chef d'orchestre et des rôles : utile parfois. Vision et navigateur : puissants, risqués. On garde les pieds sur terre."
type: tutorial
tags: [agents IA, multi-agents, vision, formation, débutant]
series: hf-agents-serie
series_order: 12
og_image: agents-hf-multi-agents-vision-browser-1200x630.jpg
---

# Plusieurs spécialistes, vision, navigateur

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-multi.svg" alt="Schéma : chef, recherche, vision, synthèse" class="schema-inline" width="800" />
  <figcaption>Un chef d'orchestre, des rôles clairs, une synthèse finale.</figcaption>
</figure>

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/agents-hf-multi-illustration.jpg" alt="Illustration multi-agents avec rôles spécialisés" class="schema-inline" width="800" loading="lazy" />
  <figcaption>Plusieurs spécialistes sous un chef - seulement si vraiment besoin.</figcaption>
</figure>

Dernier épisode de la série.  
Le [cours Agents HF](https://huggingface.co/learn/agents-course) ouvre aussi multi-agents, vision et navigateur.  
On reste prudents : c'est là que beaucoup de démos deviennent du chaos.

## Multi-agents : l'idée

Au lieu d'un seul agent qui fait tout :

- un **chercheur** (FAQ / web limité) ;  
- un **vision** (lit une image) ;  
- un **rédacteur** ;  
- un **chef** qui répartit et fusionne.

## Quand rester simple (cas le plus fréquent)

Horaires + délai devis + FAQ : **un** agent, 3 outils, ça suffit.  
Plusieurs agents = overhead. Ne le fais que si tu as une vraie douleur.

## Vision

Utile pour : capture d'erreur, étiquette, maquette.  
Pas magique : l'OCR se trompe. Valide les champs critiques.

## Navigateur (browser)

Utile pour : lire une page publique autorisée.  
Dangereux pour : comptes connectés, paiements, tout le web ouvert.

Règles mini :

- domaines autorisés ;  
- pas de secrets dans le prompt ;  
- humain avant action irréversible ;  
- log de chaque URL.

## Clôture de la série

Tu as maintenant la carte :

1. c'est quoi un agent ;  
2. outils ;  
3. boucle ;  
4. premier agent ;  
5. code vs outil contrôlé ;  
6. choix de framework ;  
7. chercher dans ta doc ;  
8. voir / mesurer ;  
9. fine-tune outils ;  
10. parcours LangGraph ;  
11. docs LlamaIndex ;  
12. multi / vision / navigateur.

Le cours officiel reste top pour les labs.  
Ici, tu as la version **lisible**, en français, avec les garde-fous.

Pour le socle modèles : [série LLM](/blog/series/llm-transformers-serie.html).

Phrase à garder : **un agent sans limite, c'est un stagiaire avec les clés du camion**.

---

## Questions fréquentes (FAQ)

**Toujours multi-agent ?**  
Non. Un agent bien outillé bat cinq agents mal briefés.

**Browser = danger ?**  
Oui s'il est ouvert sans règles.

**Par quoi commencer demain ?**  
Un agent, 2 outils, traces allumées, 20 vraies questions clients.

---

## Navigation dans la série

- Précédent : [Agent + tes documents (LlamaIndex)](/blog/articles/agents-hf-llamaindex-agent-donnees.html)
- Fin de la série - [Agents Course Hugging Face](https://huggingface.co/learn/agents-course) · [série LLM](/blog/series/llm-transformers-serie.html)
