---
title: "Flyweight : partager pour economiser la memoire"
date: 2026-04-19
excerpt: "Factoriser ce qui est commun, garder a part ce qui est unique."
type: article
tags: [Design Patterns, GoF, Flyweight, Structurel, TypeScript, Python, junior]
og_image: design-patterns-flyweight-1200x630.jpg
series: design-patterns-serie
series_order: 19
---

# Flyweight : partager pour economiser la memoire

Le **Flyweight** partage les donnees **communes** entre plein d'objets semblables.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-flyweight.svg" alt="Schema Flyweight" class="schema-inline" width="640" />
  <figcaption>Tout duplique versus partage du commun.</figcaption>
</figure>

## Analogie

Dans un livre, la **police** est partagee. Chaque lettre n'emporte pas sa propre copie de la police.

## Attention

Utile si tu as **beaucoup** d'instances. Sinon, complexite inutile. Cousin memoire : parfois [Proxy](/blog/articles/design-patterns-proxy.html) pour le lazy.

