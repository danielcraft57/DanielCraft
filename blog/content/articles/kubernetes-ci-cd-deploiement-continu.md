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

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/k8s-cicd.svg" alt="Schema CI/CD vers Kubernetes" class="schema-inline" width="640" />
  <figcaption>Commit, build image, manifest, apply ou GitOps, sondes.</figcaption>
</figure>

Tu as les briques Kubernetes (pods, Deployments, Services). Il reste à les brancher à un **pipeline CI/CD** pour que chaque merge sur `main` fasse la même chose, à chaque fois :

- builder l'image Docker,
- la pousser vers un registry,
- mettre à jour le cluster (push depuis la CI, ou pull via GitOps).

L'objectif : arrêter les `kubectl apply` depuis ton laptop le vendredi soir. Si tu découvres encore Deployments et Services, commence par [copies de ton app + adresse stable](/blog/articles/kubernetes-deployments-services.html).

---

## Pourquoi CI/CD + Kubernetes

Sans pipeline, le déploiement dépend de la personne, de la machine, du jour. Avec un pipeline :

- les tests tournent avant la prod,
- l'image est versionnée (SHA ou tag semver),
- le cluster reçoit toujours la même procédure.

Exemple mental : Alice merge un fix. La CI construit `mon-api:a1b2c3`, pousse l'image, met à jour le Deployment, attend que le rollout soit OK. Bob n'a pas besoin d'être là — et Alice non plus après le merge.

Pour le détail des images Docker dans un pipeline : [build d'images Docker en CI/CD](/blog/articles/ci-cd-build-images-docker.html).

---

## Pipeline type (API classique)

Pour une API Node.js (ou PHP, Go…), le flux ressemble souvent à :

1. Lint + tests unitaires (et éventuellement tests d'intégration légers).
2. Build de l'image Docker + push vers le registry (GHCR, ECR, Harbor…).
3. Mise à jour de la référence d'image dans Kubernetes (`image: ...:a1b2c3`).
4. Application : `kubectl` depuis la CI **ou** commit GitOps consommé par Argo CD / Flux.
5. Vérification : `kubectl rollout status` ou health checks côté GitOps.

Les stratégies de déploiement (rolling, blue/green, canary) sont détaillées dans [stratégies de déploiement Kubernetes](/blog/articles/ci-cd-kubernetes-deploiement-strategies.html).

---

## Exemple simple avec GitHub Actions

Workflow ultra simplifié (à adapter : secrets, environnements, approvals) :

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

Ce squelette montre le flux global. Un workflow plus complet (jobs séparés, cache, environnements) : [GitHub Actions de bout en bout](/blog/articles/ci-cd-github-actions-workflow-complet.html).

### Checklist avant de « valider » le job

- [ ] Les tests ont réussi (pas de `continue-on-error` silencieux sur le lint).
- [ ] L'image est taguée de façon unique (évite le tag `latest` en prod).
- [ ] Le Deployment a des sondes `readiness` / `liveness` raisonnables.
- [ ] `rollout status` (ou l'équivalent GitOps) échoue si les pods ne deviennent pas Ready.
- [ ] Tu peux revenir en arrière (undo Deployment ou revert GitOps).

Versioning et rollbacks côté process produit : [versioning, releases et rollbacks](/blog/articles/ci-cd-versioning-releases-rollbacks.html).

---

## GitOps : laisser le cluster tirer les changements

Plutôt que de pousser avec `kubectl` depuis la CI, tu peux adopter le **GitOps** :

- manifests Kubernetes versionnés dans un repo (souvent dédié),
- un opérateur (Argo CD, Flux) observe ce repo,
- un commit fusionné = état souhaité appliqué sur le cluster.

Avantages concrets :

- historique clair de « ce qui devrait tourner »,
- rollback = revert Git,
- séparation nette code appli / config cluster.

La CI peut alors se limiter à : build + push image + commit du nouveau tag dans le repo de manifests. Pour la mise en place : [GitOps avec Argo et Flux](/blog/articles/ci-cd-gitops-argo-flux.html).

---

## Pièges fréquents

- **Kubeconfig en clair dans le repo** : jamais. Secrets CI, idéalement un compte de service à droits limités (RBAC).
- **Tag `latest` partout** : tu ne sais plus quelle version tourne, et le rollback devient flou.
- **Déployer sans attendre le rollout** : le job vert alors que les pods crashent en boucle.
- **Pas de séparation staging / prod** : un merge = prod directe sans filet.
- **Secrets applicatifs dans l'image** : préfère Secrets / ConfigMaps montés au runtime — voir [ConfigMaps et Secrets](/blog/articles/kubernetes-configmaps-secrets.html).

---

## Bonnes pratiques (rappel)

- Secrets CI pour tout ce qui touche le cluster ou le registry.
- Naming cohérent des tags (commit SHA, semver + env).
- Checks de rollout obligatoires.
- Préférer GitOps dès que plusieurs personnes touchent la prod.
- Documenter le chemin de rollback en une commande (ou un revert).

Avec cette chaîne — code → build Docker → push → déploiement Kubernetes — tu as une base DevOps solide, prête à évoluer vers des stratégies plus fines et une vraie observabilité une fois en prod.
