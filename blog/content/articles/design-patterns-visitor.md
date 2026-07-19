---
title: "Visitor : ajouter une operation sans toucher les classes"
date: 2026-04-23
excerpt: "Une nouvelle action qui visite chaque type d'objet, sans modifier leur code."
type: article
tags: [Design Patterns, GoF, Visitor, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-visitor-1200x630.jpg
series: design-patterns-serie
series_order: 23
---

# Visitor : ajouter une operation sans toucher les classes

Le **Visitor** apporte une nouvelle operation. Les objets acceptent la visite.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-visitor.svg" alt="Schema Visitor" class="schema-inline" width="640" />
  <figcaption>Objets visites par un visiteur.</figcaption>
</figure>

## Analogie

Un **controleur des impots** qui visite chaque type de dossier avec des regles differentes.

## Quand

Beaucoup de types stables, beaucoup d'operations qui changent (export, stats…). Sinon, ca peut etre lourd. Intro : [patterns](/blog/articles/design-patterns-introduction-gang-of-four.html).

