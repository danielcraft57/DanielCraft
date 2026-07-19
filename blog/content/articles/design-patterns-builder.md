---
title: "Builder : construire etape par etape"
date: 2026-04-11
excerpt: "Assembler un objet complexe clairement, sans constructeur monstrueux."
type: article
tags: [Design Patterns, GoF, Builder, Créationnel, TypeScript, Python, junior]
og_image: design-patterns-builder-1200x630.jpg
series: design-patterns-serie
series_order: 11
---

# Builder : construire etape par etape

Le **Builder** te laisse ajouter des options une par une, puis `build()`.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-builder.svg" alt="Schema Builder" class="schema-inline" width="640" />
  <figcaption>Base, options, build, objet pret.</figcaption>
</figure>

## Analogie

Commander un sandwich : pain, sauce, garnitures, puis "c'est pret".

## Pourquoi

Evite les constructeurs a 12 parametres. Complement : [Factory Method](/blog/articles/design-patterns-factory-method.html) pour creer, Builder pour configurer.

