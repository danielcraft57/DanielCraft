---
title: "Interpreter : comprendre un petit langage"
date: 2026-04-24
excerpt: "Lire une expression simple (regles, formules) et l'evaluer."
type: article
tags: [Design Patterns, GoF, Interpreter, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-interpreter-1200x630.jpg
series: design-patterns-serie
series_order: 24
---

# Interpreter : comprendre un petit langage

L'**Interpreter** lit une petite grammaire (regles, filtres) et calcule un resultat.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-interpreter.svg" alt="Schema Interpreter" class="schema-inline" width="640" />
  <figcaption>Texte, parse, arbre, evaluer, resultat.</figcaption>
</figure>

## Analogie

Une **calculatrice** ou un filtre "prix > 10 ET stock".

## Attention

Pour un vrai langage complexe, utilise un vrai parseur. Ici : regles metier simples. Retour a l'[intro](/blog/articles/design-patterns-introduction-gang-of-four.html).

