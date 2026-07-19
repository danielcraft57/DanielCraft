---
title: "Composite : traiter un arbre comme une seule piece"
date: 2026-04-16
excerpt: "Dossiers et fichiers : meme API pour une feuille ou une branche."
type: article
tags: [Design Patterns, GoF, Composite, Structurel, TypeScript, Python, junior]
og_image: design-patterns-composite-1200x630.jpg
series: design-patterns-serie
series_order: 16
---

# Composite : traiter un arbre comme une seule piece

Le **Composite** permet de manipuler un element **seul** ou un **groupe** de la meme facon.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-composite.svg" alt="Schema Composite" class="schema-inline" width="640" />
  <figcaption>Dossier, fichier, meme API.</figcaption>
</figure>

## Analogie

Un **dossier** : `taille totale` marche pour un fichier et pour un dossier entier.

## Ou

Menus, arbres de scene, org charts. Souvent avec [Iterator](/blog/articles/design-patterns-iterator.html) pour parcourir.

