---
title: "Factory Method : laisser creer sans se prendre la tete"
date: 2026-04-03
excerpt: "Demander un objet a une fabrique au lieu de tout construire a la main."
type: article
tags: [Design Patterns, GoF, Factory Method, Créationnel, TypeScript, Python, junior]
og_image: design-patterns-factory-method-1200x630.jpg
series: design-patterns-serie
series_order: 3
---

# Factory Method : laisser creer sans se prendre la tete

La **fabrique** cree l'objet pour toi. Toi, tu demandes juste "un paiement" ou "un bouton".

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-factory-method.svg" alt="Schema Factory Method" class="schema-inline" width="640" />
  <figcaption>Demande, fabrique, produit adapte.</figcaption>
</figure>

## Analogie

Tu commandes un cafe. Le barista choisit la machine et la recette. Tu ne rentres pas en cuisine.

## Pourquoi c'est cool

Tu peux changer le type cree **sans** casser le code qui utilise le produit. Voir aussi [Abstract Factory](/blog/articles/design-patterns-abstract-factory.html) et [Builder](/blog/articles/design-patterns-builder.html).

