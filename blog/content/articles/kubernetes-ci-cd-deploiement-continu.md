---
title: "Kubernetes et CI/CD : déploiement continu propre"
date: 2026-01-25
excerpt: "Brancher ton cluster Kubernetes sur ta CI/CD : build d'images, push vers un registry, mise à jour des manifests et stratégies de déploiement."
type: article
tags: [Kubernetes, CI/CD, déploiement continu, DevOps]
series: kubernetes-serie
series_order: 6
og_image: k8s-ci-cd-1200x630.jpg
---

# Kubernetes et CI/CD : déploiement continu propre

Tu as les briques Kubernetes, il reste à les brancher à ton **pipeline CI/CD** pour :

- builder les images Docker,
- les pousser vers un registry,
- mettre à jour le cluster automatiquement (ou presque).

L'objectif : éviter les `kubectl apply` manuels sur ton laptop pour chaque mise en prod.

---

## Pipeline type

Pour une appli classique (API Node.js par exemple), un pipeline peut ressembler à ça :

1. Lint + tests unitaires.  
2. Build de l'image Docker et push vers le registry.  
3. Mise à jour du manifest Kubernetes (`image: ...:1.2.3`).  
4. `kubectl apply` (directement ou via un outil GitOps).

---

## Exemple simple avec GitHub Actions

Un workflow ultra simplifié :

```yaml
name: CI/CD API

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build and push image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ghcr.io/likedevGit/mon-api:${{ github.sha }}

      - name: Set up kubectl
        uses: azure/setup-kubectl@v4
        with:
          version: "v1.29.0"

      - name: Configure kubeconfig
        run: echo "${KUBECONFIG_CONTENT}" > kubeconfig.yml
        env:
          KUBECONFIG_CONTENT: ${{ secrets.KUBECONFIG_CONTENT }}

      - name: Deploy to cluster
        env:
          KUBECONFIG: ${{ github.workspace }}/kubeconfig.yml
        run: |
          kubectl set image deployment/mon-api api=ghcr.io/likedevGit/mon-api:${{ github.sha }}
          kubectl rollout status deployment/mon-api
```

Ce n'est qu'un squelette, mais il illustre le flux global.

---

## GitOps : laisser le cluster "tirer" les changements

Plutôt que de pousser directement avec `kubectl` depuis la CI, tu peux adopter une approche **GitOps** :

- tu versionnes les manifests Kubernetes dans un repo dédié,
- un opérateur (Argo CD, Flux) observe ce repo,
- il applique les changements sur le cluster dès qu'un commit est fusionné.

Avantages :

- historique clair de l'état souhaité du cluster,
- rollbacks simplifiés,
- séparation nette entre code appli et config infra.

---

## Quelques bonnes pratiques

- Évite de stocker le kubeconfig complet en clair dans le repo → utilise des **secrets** CI.  
- Garde un **naming cohérent** pour les tags d'image (commit SHA, version, env).  
- Ajoute des **checks de rollout** (`kubectl rollout status` ou équivalent GitOps) pour éviter de "valider" un déploiement cassé.

Avec cette dernière étape, tu as une chaîne complète :

- code → build Docker → push → déploiement Kubernetes,  
sculptée pour évoluer vers des pratiques DevOps solides.
