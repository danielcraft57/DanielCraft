---
title: "Versions et retours arriere : livrer sans paniquer"
date: 2025-04-01
excerpt: "Tags, releases et rollback : savoir exactement ce qui tourne, et revenir vite."
type: article
tags: [CI/CD, versioning, releases, rollback, sémantique]
series: ci-cd-serie
series_order: 9
og_image: ci-cd-versioning-1200x630.jpg
---

# Versions et retours arriere : livrer sans paniquer

Sans **version** claire, "revenir en arriere" devient un jeu de piste. Avec un tag et une release, tu sais **quoi** est en prod.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-versioning.svg" alt="Schema versioning release rollback" class="schema-inline" width="640" />
  <figcaption>Tag, release, deploy, probleme, rollback.</figcaption>
</figure>

## Habitudes utiles

- Versions lisibles (ex. `1.4.2`) ou commit hash
- Une **release** = notes + artefact
- Rollback teste (pas seulement imagine)
- Ne jamais ecraser un tag deja livre

C'est le filet de securite de toute la [serie CI/CD](/blog/series/ci-cd-serie.html).

