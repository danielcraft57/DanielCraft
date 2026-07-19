---
title: "State : le comportement change selon l'etat"
date: 2026-04-13
excerpt: "Selon ou tu en es (brouillon, publie…), les actions autorisees changent."
type: article
tags: [Design Patterns, GoF, State, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-state-1200x630.jpg
series: design-patterns-serie
series_order: 13
---

# State : le comportement change selon l'etat

Avec **State**, l'objet se comporte differemment selon son etat actuel.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-state.svg" alt="Schema State" class="schema-inline" width="640" />
  <figcaption>Brouillon, publie, archive.</figcaption>
</figure>

## Analogie

Une **commande en ligne** : panier, paye, expedie. Tu ne peux pas "expedier" depuis le panier.

## Vs Strategy

Strategy : tu choisis l'algo. State : l'etat decide (et peut changer tout seul). Voir [Strategy](/blog/articles/design-patterns-strategy.html).

