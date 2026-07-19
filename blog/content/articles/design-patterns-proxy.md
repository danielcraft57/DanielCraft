---
title: "Proxy : un intermediaire qui controle l'acces"
date: 2026-04-14
excerpt: "Un objet devant un autre : cache, securite, ou chargement lazy."
type: article
tags: [Design Patterns, GoF, Proxy, Structurel, TypeScript, Python, junior]
og_image: design-patterns-proxy-1200x630.jpg
series: design-patterns-serie
series_order: 14
---

# Proxy : un intermediaire qui controle l'acces

Le **Proxy** se place devant le vrai objet. Le client parle au proxy.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-proxy.svg" alt="Schema Proxy" class="schema-inline" width="640" />
  <figcaption>Client, proxy, vrai objet.</figcaption>
</figure>

## Analogie

Un **gardien** a l'entree : il verifie, puis te laisse entrer (ou non).

## Usages

Lazy loading, cache, droits d'acces, logs. Differe du [Decorator](/blog/articles/design-patterns-decorator.html) (ajoute une feature) et de la [Facade](/blog/articles/design-patterns-facade.html) (simplifie un sous-systeme).

