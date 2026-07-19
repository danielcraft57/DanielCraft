---
title: "GitLab CI : des etapes claires jusqu'au deploiement"
date: 2025-03-20
excerpt: "Stages, cache et deploiement : une pipeline GitLab simple a suivre."
type: article
tags: [CI/CD, GitLab CI, Docker, pipeline, DevOps]
series: ci-cd-serie
series_order: 6
og_image: ci-cd-gitlab-1200x630.jpg
---

# GitLab CI : des etapes claires jusqu'au deploiement

Avec **GitLab CI**, tu decris des **stages** (etapes) : build, test, package, deploy. Chaque job appartient a une etape.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-gitlab-ci.svg" alt="Schema des stages GitLab CI" class="schema-inline" width="640" />
  <figcaption>build, test, package, deploy : une chaine lisible.</figcaption>
</figure>

## Conseils simples

- Nomme les jobs pour un humain
- Mets du **cache** sur les dependances (sans casser les builds)
- Separe staging et prod
- Range les [secrets](/blog/articles/ci-cd-secrets-variables-environnement.html) correctement

Le but : la meme histoire a chaque merge. Ensuite, tu peux viser [Kubernetes](/blog/articles/ci-cd-kubernetes-deploiement-strategies.html) ou le [GitOps](/blog/articles/ci-cd-gitops-argo-flux.html).

