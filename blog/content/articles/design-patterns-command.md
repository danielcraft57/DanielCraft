---
title: "Command : une action en paquet (qu'on peut annuler)"
date: 2026-04-09
excerpt: "Transformer une action en objet : executer, stocker, annuler, rejouer."
type: article
tags: [Design Patterns, GoF, Command, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-command-1200x630.jpg
series: design-patterns-serie
series_order: 9
---

# Command : une action en paquet (qu'on peut annuler)

Une **Command** = "fais ca" emballe dans un objet. On peut la mettre en file, l'annuler, la rejouer.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-command.svg" alt="Schema Command" class="schema-inline" width="640" />
  <figcaption>Bouton, commande, executer, annuler.</figcaption>
</figure>

## Analogie

Une **telecommande** : chaque bouton envoie une commande. Tu peux meme avoir "annuler".

## Ou c'est top

Undo/redo, files de taches, macros. Voir [Memento](/blog/articles/design-patterns-memento.html) pour restaurer un etat complet.

