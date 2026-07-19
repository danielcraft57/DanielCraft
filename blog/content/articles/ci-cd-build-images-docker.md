---
title: "CI/CD : fabriquer et envoyer une image Docker"
date: 2025-03-11
excerpt: "Construire la meme boite a chaque fois, la taguer, la pousser dans un registry."
type: article
tags: [CI/CD, Docker, images, registry, DevOps]
series: ci-cd-serie
series_order: 3
og_image: ci-cd-docker-images-1200x630.jpg
---

# CI/CD : fabriquer et envoyer une image Docker

La CI fabrique souvent une **image** : une boite prete a demarrer partout pareil. Ensuite elle l'envoie dans un **registry** (etagere d'images).

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-docker-build.svg" alt="Schema build et push d'image Docker en CI" class="schema-inline" width="640" />
  <figcaption>Code, Dockerfile, build, tag, registry.</figcaption>
</figure>

## Les idees cles

- **Tag** clair : `1.4.2` ou le hash du commit — pas seulement `latest`
- **Cache** de build pour aller plus vite
- Image **legere** (voir [optimisation Docker](/blog/articles/docker-build-optimisation-images.html))
- Scan simple des failles avant prod

## Pourquoi c'est bien

Tu testes **la meme boite** que tu mets en prod. Moins de "mais ca marchait en local". Enchaine avec [GitHub Actions](/blog/articles/ci-cd-github-actions-workflow-complet.html) ou [GitLab CI](/blog/articles/ci-cd-gitlab-ci-pipeline-complet.html).

