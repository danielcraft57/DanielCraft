---
title: "GitOps : le cluster suit Git (pas l'inverse)"
date: 2025-03-27
excerpt: "Argo CD ou Flux : deployer en declarant l'etat souhaite dans un depot Git."
type: article
tags: [CI/CD, GitOps, Kubernetes, Argo CD, Flux]
series: ci-cd-serie
series_order: 8
og_image: ci-cd-gitops-1200x630.jpg
---

# GitOps : le cluster suit Git (pas l'inverse)

Le **GitOps**, c'est une idee simple : Git decrit **ce qui doit tourner**. Un outil (Argo CD, Flux) regarde Git et aligne le cluster.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-gitops.svg" alt="Schema GitOps avec Argo ou Flux" class="schema-inline" width="640" />
  <figcaption>Git, build, manifest, synchronisation cluster.</figcaption>
</figure>

## Pourquoi c'est rassurant

- Historique clair (qui a change quoi)
- Moins de `kubectl` a la main a 23h
- Un ecart ? On le voit

Ca demande de la discipline : les manifests (fichiers de description) doivent etre **propres** et versionnes. Branche avec la [CI/CD Kubernetes](/blog/articles/ci-cd-kubernetes-deploiement-strategies.html).

