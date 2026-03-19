---
title: "CI/CD : comprendre les pipelines (vraiment) - du commit au déploiement"
date: 2025-03-04
excerpt: "La CI/CD expliquée clairement : pourquoi on l'utilise, comment penser un pipeline, quelles étapes mettre, et comment éviter les usines à gaz."
type: article
tags: [CI/CD, DevOps, pipeline, Git, déploiement]
series: ci-cd-serie
series_order: 1
og_image: ci-cd-fondamentaux-1200x630.jpg
---

# CI/CD : comprendre les pipelines (vraiment) - du commit au déploiement

La CI/CD, ce n'est pas "un truc de DevOps". C'est juste une manière propre de livrer du code :

- **plus vite**,
- **plus souvent**,
- **sans trembler** à chaque déploiement.

Dans cette série, on va construire une vision claire et réutilisable. Pas un guide qui finit en copier-coller magique, mais une méthode.

---

## CI, CD : définition simple

- **CI (Continuous Integration)** : à chaque push/merge, on vérifie automatiquement que le code tient debout (tests, lint, build).
- **CD (Continuous Delivery/Deployment)** :
  - **Delivery** : on prépare un artefact déployable automatiquement (image Docker, package, bundle), prêt à être lancé.
  - **Deployment** : on déclenche le déploiement automatiquement (souvent après validation).

Dans les faits, beaucoup disent CD pour tout.

---

## Pourquoi tu en as besoin (même sur un petit projet)

Sans CI/CD, tu finis avec :

- des builds différents selon la machine,
- des déploiements "à la main" qui oublient un fichier,
- des hotfix en prod impossibles à reproduire.

Avec CI/CD, tu gagnes :

- de la **reproductibilité** (le pipeline fait toujours la même chose),
- un **filet de sécurité** (tests, lint, checks),
- une **traçabilité** (qui a déployé quoi, quand).

---

## Le pipeline type (la base saine)

Un pipeline bien pensé suit souvent cette logique :

1. **Checkout + install deps**
2. **Qualité** (lint, format, typecheck)
3. **Tests** (unitaires, intégration)
4. **Build** (artefact)
5. **Package** (image Docker)
6. **Scan** (dépendances / image)
7. **Déploiement** (staging, puis prod)
8. **Vérifications post-déploiement** (healthchecks, smoke tests)

Tu n'es pas obligé de tout faire dès le jour 1. L'important : l'ordre et la logique.

---

## Ce qu'on déploie exactement ?

Trois cas fréquents :

- **Site statique** : build + upload (S3, Nginx, GitHub Pages).
- **API/Back** : image Docker versionnée + déploiement (Kubernetes, VM, PaaS).
- **Monorepo** : plusieurs builds + plusieurs déploiements.

L'artefact doit être :

- **versionné**,
- **reproductible**,
- **déployable sans rebuild** en prod.

---

## Éviter les pièges classiques

### 1. Pipeline trop lent

Si ton pipeline met 20 minutes, l'équipe va le contourner.

Réflexes :

- cache des dépendances,
- parallélisation (tests en shards),
- tests ciblés (unitaires rapides -> intégration plus tard).

### 2. Pipeline trop "magique"

Un pipeline incompréhensible, c'est une bombe à retardement.

Réflexes :

- étapes nommées clairement,
- scripts simples (Makefile, npm scripts),
- logs lisibles.

### 3. Secrets mal gérés

Pas de mots de passe en dur dans le repo. Jamais.

On verra ça en détail dans un article dédié : secrets, variables, vault, etc.

---

## Comment cette série est organisée

On va avancer dans cet ordre :

1. **Fondamentaux** (ce que tu lis ici)
2. **Tests + quality gates** (quand tu bloques un déploiement)
3. **Build d'images Docker** (tags, cache, multi-stage)
4. **Secrets / config** (sans fuite)
5. **Exemple GitHub Actions** complet
6. **Exemple GitLab CI** complet
7. **Déploiement Kubernetes** (strategies, rollout, rollback)
8. **GitOps** (Argo CD / Flux)
9. **Versioning + releases**
10. **Observabilité des déploiements**

Objectif final : une chaîne propre du commit jusqu'à la prod, que tu peux appliquer à tes projets (Docker/Kubernetes).

