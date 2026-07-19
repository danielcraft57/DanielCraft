---
title: "Kubernetes et CI/CD : publier sans stress"
date: 2025-01-23
excerpt: "Du commit a l'image, puis au cluster, avec les memes etapes a chaque fois."
type: article
tags: [Kubernetes, CI/CD, déploiement continu, DevOps]
series: kubernetes-serie
series_order: 6
og_image: k8s-ci-cd-1200x630.jpg
---

# Kubernetes et CI/CD : publier sans stress

La bonne chaine : **commit → tests → image → description (YAML) → cluster**. Toujours pareil.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/k8s-cicd.svg" alt="Schema CI/CD vers Kubernetes" class="schema-inline" width="640" />
  <figcaption>Commit, build image, manifest, apply ou GitOps, sondes.</figcaption>
</figure>

## Deux styles

- La CI applique les manifests
- Ou le [GitOps](/blog/articles/ci-cd-gitops-argo-flux.html) synchronise depuis Git

Ajoute des sondes et un plan de [rollback](/blog/articles/ci-cd-versioning-releases-rollbacks.html). C'est ca, un deploiement "propre".

