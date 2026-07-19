---
title: "Mediator : un chef d'orchestre entre les objets"
date: 2026-04-21
excerpt: "Les objets ne se parlent plus tous entre eux : ils passent par un centre."
type: article
tags: [Design Patterns, GoF, Mediator, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-mediator-1200x630.jpg
series: design-patterns-serie
series_order: 21
---

# Mediator : un chef d'orchestre entre les objets

Le **Mediator** centralise les echanges. Fini le spaghetti "tout le monde appelle tout le monde".

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-mediator.svg" alt="Schema Mediator" class="schema-inline" width="640" />
  <figcaption>Spaghetti versus centre de coordination.</figcaption>
</figure>

## Analogie

La **tour de controle** d'un aeroport : les avions ne negocient pas entre eux.

## Vs Observer

Observer diffuse un evenement. Mediator **coordonne** des interactions precises. Voir [Observer](/blog/articles/design-patterns-observer.html).

