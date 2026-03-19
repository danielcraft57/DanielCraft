---
title: "CI/CD : un workflow GitHub Actions complet (Docker + déploiement)"
date: 2025-03-18
excerpt: "Un exemple complet et réaliste de GitHub Actions : quality checks, tests, build d'image Docker, push registry, déploiement et vérification."
type: article
tags: [CI/CD, GitHub Actions, Docker, DevOps, déploiement]
series: ci-cd-serie
series_order: 5
og_image: ci-cd-github-actions-1200x630.jpg
---

# CI/CD : un workflow GitHub Actions complet (Docker + déploiement)

L'objectif ici : te donner un workflow **compréhensible**, pas un truc magique.

On part sur une appli type API (Node/TS ou autre), avec :

- lint + typecheck + tests,
- build image Docker,
- push vers un registry,
- déploiement sur un cluster Kubernetes,
- vérification du rollout.

---

## Structure recommandée

Deux workflows plutôt qu'un seul énorme :

- `ci.yml` : checks (lint/tests/build) sur PR
- `deploy.yml` : build/push/deploy sur `main`

Ça garde les responsabilités propres.

---

## Exemple `deploy.yml` (simplifié mais complet)

```yaml
name: Deploy

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Node
        uses: actions/setup-node@v4
        with:
          node-version: "22"
          cache: "npm"

      - name: Install deps
        run: npm ci

      - name: Lint + typecheck + tests
        run: |
          npm run lint
          npm run typecheck
          npm test

      - name: Login registry
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
          tags: ghcr.io/ton-org/ton-api:${{ github.sha }}

      - name: Setup kubectl
        uses: azure/setup-kubectl@v4
        with:
          version: "v1.29.0"

      - name: Write kubeconfig
        run: echo "${KUBECONFIG_B64}" | base64 -d > kubeconfig.yml
        env:
          KUBECONFIG_B64: ${{ secrets.KUBECONFIG_B64 }}

      - name: Deploy
        env:
          KUBECONFIG: ${{ github.workspace }}/kubeconfig.yml
        run: |
          kubectl set image deployment/ton-api api=ghcr.io/ton-org/ton-api:${{ github.sha }}
          kubectl rollout status deployment/ton-api
```

Notes :

- on tag l'image avec `github.sha` (traçable),
- on update le Deployment via `kubectl set image`,
- on attend `rollout status` pour ne pas valider un déploiement cassé.

---

## À améliorer en prod

Pour aller plus loin :

- tags sémantiques (`1.2.3`) en plus du SHA,
- promotion staging -> prod (pas de déploiement direct prod),
- scan de l'image (Trivy),
- notifications (Slack, email),
- stratégie de rollback automatique si healthcheck KO.

Dans l'article suivant, on fait la même chose côté **GitLab CI** (concepts similaires, syntaxe différente).

