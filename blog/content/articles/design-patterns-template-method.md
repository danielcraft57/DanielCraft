---
title: "Template Method : meme plan, details au choix"
date: 2026-04-10
excerpt: "Une recette fixe avec quelques etapes a personnaliser."
type: article
tags: [Design Patterns, GoF, Template Method, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-template-method-1200x630.jpg
series: design-patterns-serie
series_order: 10
---

# Template Method : meme plan, details au choix

Le **Template Method** fixe l'ordre des etapes. Les sous-classes remplissent les trous.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-template-method.svg" alt="Schema Template Method" class="schema-inline" width="640" />
  <figcaption>Etapes fixes et etape a personnaliser.</figcaption>
</figure>

## Analogie

Recette de gateau : melanger, cuire, decorer. La decoration change ; le plan reste.

## Astuce

Garde le squelette dans la classe mere, mets le variable ailleurs. Proche de [Strategy](/blog/articles/design-patterns-strategy.html), mais ici l'ordre est impose.

