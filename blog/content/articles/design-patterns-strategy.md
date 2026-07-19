---
title: "Strategy : changer de methode sans tout casser"
date: 2026-04-05
excerpt: "Plusieurs facons de faire la meme chose, interchangeables."
type: article
tags: [Design Patterns, GoF, Strategy, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-strategy-1200x630.jpg
series: design-patterns-serie
series_order: 5
---

# Strategy : changer de methode sans tout casser

Une **strategie** = une maniere de faire. Tu peux en changer sans reecrire tout le programme.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-strategy.svg" alt="Schema Strategy" class="schema-inline" width="640" />
  <figcaption>If/else geants versus strategies interchangeables.</figcaption>
</figure>

## Analogie

Meme trajet, GPS different (voiture, velo, pied). La voiture reste la voiture.

## Exemple

Trier, payer, calculer frais de port… plusieurs algos, meme interface. Complement : [State](/blog/articles/design-patterns-state.html) (le comportement depend d'un etat).

