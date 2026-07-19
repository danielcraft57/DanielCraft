---
title: "Singleton : une seule copie, pas plus"
date: 2026-04-02
excerpt: "Garantir une seule instance partagee — utile parfois, dangereux si abuse."
type: article
tags: [Design Patterns, GoF, Singleton, Créationnel, TypeScript, Python, junior]
og_image: design-patterns-singleton-1200x630.jpg
series: design-patterns-serie
series_order: 2
---

# Singleton : une seule copie, pas plus

Le **Singleton** dit : il n'existe qu'**une** copie de cet objet pour tout le programme.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-singleton.svg" alt="Schema Singleton" class="schema-inline" width="640" />
  <figcaption>Une seule copie partagee versus plusieurs copies qui divergent.</figcaption>
</figure>

## Analogie

Comme le **maire** d'une ville : un seul poste. Tout le monde passe par la meme personne.

## Quand c'est utile

Config globale, un cache partage, un logger. **Rarement** plus.

## Attention

Trop de Singletons = code difficile a tester (tout est lie). Prefere parfois un simple module ou l'[injection](/blog/articles/design-patterns-factory-method.html). Suite de la serie : [Observer](/blog/articles/design-patterns-observer.html).

