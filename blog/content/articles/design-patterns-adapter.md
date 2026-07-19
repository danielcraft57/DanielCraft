---
title: "Adapter : faire marcher deux pieces incompatibles"
date: 2026-04-07
excerpt: "Traduire une interface pour brancher l'ancien sur le nouveau."
type: article
tags: [Design Patterns, GoF, Adapter, Structurel, TypeScript, Python, junior]
og_image: design-patterns-adapter-1200x630.jpg
series: design-patterns-serie
series_order: 7
---

# Adapter : faire marcher deux pieces incompatibles

L'**Adapter** traduit. D'un cote un format, de l'autre un autre. Au milieu : l'adaptateur.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-adapter.svg" alt="Schema Adapter" class="schema-inline" width="640" />
  <figcaption>Ancien format, adaptateur, nouveau format.</figcaption>
</figure>

## Analogie

Un **prise / chargeur universel** : la prise murale et ton appareil ne sont pas les memes.

## Quand

API legacy, lib tierce, formats differents. Ne confonds pas avec [Facade](/blog/articles/design-patterns-facade.html) (simplifie) ni [Bridge](/blog/articles/design-patterns-bridge.html) (separe deux axes).

