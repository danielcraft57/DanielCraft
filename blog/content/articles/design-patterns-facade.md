---
title: "Facade : une porte simple vers un systeme complexe"
date: 2026-04-08
excerpt: "Cacher 10 appels techniques derriere une methode claire."
type: article
tags: [Design Patterns, GoF, Facade, Structurel, TypeScript, Python, junior]
og_image: design-patterns-facade-1200x630.jpg
series: design-patterns-serie
series_order: 8
---

# Facade : une porte simple vers un systeme complexe

La **Facade** offre une entree simple. Derriere, plein de pieces techniques restent cachees.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-facade.svg" alt="Schema Facade" class="schema-inline" width="640" />
  <figcaption>Une methode claire versus dix appels techniques.</figcaption>
</figure>

## Analogie

La **reception** d'un hotel : tu demandes une chambre, tu ne geres pas le menage, la cle, la facture.

## Gain

Le client (ton code UI) reste simple. Les details restent au service. Cousin : [Mediator](/blog/articles/design-patterns-mediator.html) pour coordonner des egaux.

