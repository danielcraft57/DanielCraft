---
title: "Kubernetes : qui decide, qui execute"
date: 2025-01-09
excerpt: "Le plan de controle et les nodes : le cerveau et les bras du cluster."
type: article
tags: [Kubernetes, architecture, control plane, etcd, scheduler]
series: kubernetes-serie
series_order: 2
og_image: k8s-architecture-1200x630.jpg
---

# Kubernetes : qui decide, qui execute

Un cluster a un **cerveau** (plan de controle) et des **bras** (nodes).

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/k8s-architecture.svg" alt="Schema architecture cluster Kubernetes" class="schema-inline" width="640" />
  <figcaption>API, etcd, scheduler, puis nodes qui executent.</figcaption>
</figure>

## En image mentale

1. Tu parles a l'**API** (la reception)
2. **etcd** se souvient de l'etat voulu
3. Le **scheduler** choisit sur quelle machine placer un pod
4. Les **nodes** executent

Tu n'as pas besoin de tout reconstruire a la main pour comprendre. Garde cette carte mentale, puis passe aux [Deployments et Services](/blog/articles/kubernetes-deployments-services.html).

