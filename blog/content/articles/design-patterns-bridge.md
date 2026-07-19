---
title: "Bridge : deux axes independants (sans explosion de classes)"
date: 2026-04-17
excerpt: "Separer forme et rendu (ou appareil et protocole) pour les combiner librement."
type: article
tags: [Design Patterns, GoF, Bridge, Structurel, TypeScript, Python, junior]
og_image: design-patterns-bridge-1200x630.jpg
series: design-patterns-serie
series_order: 17
---

# Bridge : deux axes independants (sans explosion de classes)

Le **Bridge** separe deux dimensions qui évoluent chacune de leur cote.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/dp-bridge.svg" alt="Schema Bridge" class="schema-inline" width="640" />
  <figcaption>Axe forme et axe rendu combines.</figcaption>
</figure>

## Analogie

**Forme** (cercle / carre) × **rendu** (ecran / imprimante). Sans Bridge, tu exploses en CercleEcran, CarreImprimante…

## Vs Adapter

Adapter repare un mauvais fit. Bridge est prevu des le debut pour evoluer. Voir [Adapter](/blog/articles/design-patterns-adapter.html).

