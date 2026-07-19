---
title: "Kubernetes : copies de ton app + adresse stable"
date: 2025-01-14
excerpt: "Deployment pour gerer les pods, Service pour les joindre facilement."
type: article
tags: [Kubernetes, Deployments, Services, réseau]
series: kubernetes-serie
series_order: 3
og_image: k8s-deployments-services-1200x630.jpg
---

# Kubernetes : copies de ton app + adresse stable

Un **Deployment** dit : "garde N copies de mon appli a jour". Un **Service** donne une **adresse stable**, meme si les pods changent.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/k8s-deploy-service.svg" alt="Schema Deployment et Service" class="schema-inline" width="640" />
  <figcaption>Image, Deployment, pods, Service, utilisateurs.</figcaption>
</figure>

## Pourquoi c'est pratique

- Une copie tombe ? Kubernetes en relance une
- Tu mets a jour ? Rolling update
- Les utilisateurs passent par le Service, pas par l'IP d'un pod

Ensuite : [config et secrets](/blog/articles/kubernetes-configmaps-secrets.html), puis [CI/CD](/blog/articles/kubernetes-ci-cd-deploiement-continu.html).

