---
title: "Decorator : ajouter des options comme des couches"
date: 2026-04-06
excerpt: "Enrichir un objet sans modifier sa classe de base."
type: article
tags: [Design Patterns, GoF, Decorator, Structurel, TypeScript, Python, junior]
og_image: design-patterns-decorator-1200x630.jpg
series: design-patterns-serie
series_order: 6
---

# Decorator : ajouter des options comme des couches

Le **Decorator** enveloppe un objet et ajoute un comportement. On peut empiler les couches.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-decorator.svg" alt="Schema Decorator" class="schema-inline" width="640" />
  <figcaption>Base puis options empilees.</figcaption>
</figure>

## Analogie

Cafe + lait + chantilly. Chaque option enveloppe la precedente.

## Différence avec heritage

Heritage fixe. Decorator compose a la volee. Voir aussi [Proxy](/blog/articles/design-patterns-proxy.html) (controle d'acces) et [Adapter](/blog/articles/design-patterns-adapter.html) (compatibilite).

