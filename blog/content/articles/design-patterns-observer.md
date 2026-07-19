---
title: "Observer : prevenir plein de gens d'un coup"
date: 2026-04-04
excerpt: "Quand quelque chose change, tous les abonnes sont prevenus automatiquement."
type: article
tags: [Design Patterns, GoF, Observer, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-observer-1200x630.jpg
series: design-patterns-serie
series_order: 4
---

# Observer : prevenir plein de gens d'un coup

Le **sujet** change. Les **abonnes** (observers) sont prevenus. Personne n'a besoin de tout hardcoder.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-observer.svg" alt="Schema Observer" class="schema-inline" width="640" />
  <figcaption>Un sujet notifie A, B et C.</figcaption>
</figure>

## Analogie

Tu t'abonnes a une chaine : quand une video sort, tu es notifie. La chaine ne te connait pas personnellement.

## Ou on le voit

UI qui se met a jour, notifications, events. Cousin utile : [Mediator](/blog/articles/design-patterns-mediator.html) si trop d'abonnes se parlent entre eux.

