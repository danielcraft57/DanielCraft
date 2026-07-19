---
title: "Chain of Responsibility : passer la demande au bon maillon"
date: 2026-04-20
excerpt: "Chaque etape decide : je traite, ou je passe au suivant."
type: article
tags: [Design Patterns, GoF, Chain of Responsibility, Comportemental, TypeScript, Python, junior]
og_image: design-patterns-chain-of-responsibility-1200x630.jpg
series: design-patterns-serie
series_order: 20
---

# Chain of Responsibility : passer la demande au bon maillon

Une **chaine** : A regarde, sinon B, sinon C… jusqu'a ce que quelqu'un traite.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-chain.svg" alt="Schema Chain of Responsibility" class="schema-inline" width="640" />
  <figcaption>Requete passee de maillon en maillon.</figcaption>
</figure>

## Analogie

Support client : niveau 1, puis 2, puis expert. Ou une file de validateurs.

## Gain

Tu ajoutes un maillon sans toucher les autres. Voir [Command](/blog/articles/design-patterns-command.html) pour emballer la requete.

