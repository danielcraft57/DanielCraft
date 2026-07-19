---
title: "Memento : sauvegarder pour pouvoir revenir en arriere"
date: 2026-04-22
excerpt: "Prendre une photo de l'etat, la ranger, la restaurer plus tard (Ctrl+Z)."
type: article
tags: [Design Patterns, GoF, Memento, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-memento-1200x630.jpg
series: design-patterns-serie
series_order: 22
---

# Memento : sauvegarder pour pouvoir revenir en arriere

Le **Memento** garde une **photo** de l'etat. Plus tard, on restaure.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-memento.svg" alt="Schema Memento" class="schema-inline" width="640" />
  <figcaption>Etat, save, changer, restore.</figcaption>
</figure>

## Analogie

**Ctrl+Z** ou une sauvegarde de jeu.

## Tip

Ne laisse pas tout le monde fouiller dans la sauvegarde : un gardien (caretaker) la range. Couple bien avec [Command](/blog/articles/design-patterns-command.html) pour l'historique.

