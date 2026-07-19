---
title: "Abstract Factory : des familles d'objets qui vont ensemble"
date: 2026-04-15
excerpt: "Creer des lots coherents (theme clair / sombre) sans melanger les pieces."
type: article
tags: [Design Patterns, GoF, Abstract Factory, Créationnel, TypeScript, Python, junior]
og_image: design-patterns-abstract-factory-1200x630.jpg
series: design-patterns-serie
series_order: 15
---

# Abstract Factory : des familles d'objets qui vont ensemble

L'**Abstract Factory** cree des **familles** assorties : bouton + champ + fenetre du meme style.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-abstract-factory.svg" alt="Schema Abstract Factory" class="schema-inline" width="640" />
  <figcaption>Familles assorties, ne pas melanger.</figcaption>
</figure>

## Analogie

Un **pack salon** : canape + fauteuil + table du meme style. Pas un canape baroque avec une table IKEA au hasard.

## Lien

Plus "macro" que [Factory Method](/blog/articles/design-patterns-factory-method.html). Utile UI multi-themes, multi-plateformes.

