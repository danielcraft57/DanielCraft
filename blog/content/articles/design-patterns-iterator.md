---
title: "Iterator : parcourir sans tout reveler"
date: 2026-04-12
excerpt: "Avancer element par element sans exposer la structure interne."
type: article
tags: [Design Patterns, GoF, Iterator, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-iterator-1200x630.jpg
series: design-patterns-serie
series_order: 12
---

# Iterator : parcourir sans tout reveler

L'**Iterator** dit : "suivant ?" jusqu'a la fin. Toi, tu ne vois pas si c'est une liste, un arbre, un fichier.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-iterator.svg" alt="Schema Iterator" class="schema-inline" width="640" />
  <figcaption>Collection, iterator, next, next, fin.</figcaption>
</figure>

## Analogie

Une **playlist** : tu passes a la suivante sans ouvrir le tiroir des fichiers.

## Bonus

Tu peux avoir plusieurs parcours (avant, arriere) sans casser la collection. Souvent couple a [Composite](/blog/articles/design-patterns-composite.html).

