---
title: "CI/CD : les portes qui bloquent un mauvais deploiement"
date: 2025-03-06
excerpt: "Tests, qualite et controles automatiques : ce qui doit etre vert avant d'aller en prod."
type: article
tags: [CI/CD, tests, qualité, DevOps, automatisation]
series: ci-cd-serie
series_order: 2
og_image: ci-cd-tests-1200x630.jpg
---

# CI/CD : les portes qui bloquent un mauvais deploiement

Une chaine CI/CD sans **portes** (gates), c'est un tapis roulant qui envoie n'importe quoi en prod. Les portes disent : "si ce n'est pas OK, on s'arrete".

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-quality-gates.svg" alt="Schema des portes qualite CI/CD" class="schema-inline" width="640" />
  <figcaption>Lint, tests, secu : si une porte est fermee, on ne livre pas.</figcaption>
</figure>

## Quoi bloquer (le minimum utile)

- **Style / lint** : code trop sale ou dangereux
- **Tests unitaires** : les petites regles metier
- **Tests d'integration** : les pieces qui doivent s'assembler
- Controles **securite** basiques (dependances connues, secrets detectes)

Tu n'as pas besoin de tout le catalogue. Tu as besoin de portes qui **veulent dire quelque chose**.

## Trop de portes = personne ne les ecoute

Si tout est "bloquant", l'equipe contourne. Mieux vaut :
- **bloquer** le critique (tests metier, build casse, secret detecte)
- **avertir** le reste (couverture un peu basse, lint mineur)

## Une regle simple

Avant la prod : "est-ce qu'on oserait deployer ca un vendredi a 17h ?" Si non, la porte doit etre rouge. Ensuite, regarde l'article sur les [secrets](/blog/articles/ci-cd-secrets-variables-environnement.html) et le [build Docker](/blog/articles/ci-cd-build-images-docker.html).

