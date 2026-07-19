---
title: "Prototype : copier un modele plutot que tout recreer"
date: 2026-04-18
excerpt: "Cloner un objet existant puis ajuster — plus simple parfois que construire a neuf."
type: article
tags: [Design Patterns, GoF, Prototype, Créationnel, TypeScript, Python, junior]
og_image: design-patterns-prototype-1200x630.jpg
series: design-patterns-serie
series_order: 18
---

# Prototype : copier un modele plutot que tout recreer

Le **Prototype** part d'un modele, le **clone**, puis tu ajustes.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-prototype.svg" alt="Schema Prototype" class="schema-inline" width="640" />
  <figcaption>Modele, clone, ajuste, nouvelle copie.</figcaption>
</figure>

## Analogie

Un **tampon** ou un modele Word : tu dupliques, tu changes 2 champs.

## Quand

Objets couteux a creer, ou beaucoup de variantes proches. Voir aussi [Builder](/blog/articles/design-patterns-builder.html).

