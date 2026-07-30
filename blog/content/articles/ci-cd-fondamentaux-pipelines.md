---
title: "CI/CD : du commit a la mise en ligne, automatiquement"
date: 2025-03-04
excerpt: "Une chaine qui teste et publie ton code a ta place — pour livrer plus souvent, sans trembler."
type: article
tags: [CI/CD, DevOps, pipeline, Git, déploiement]
series: ci-cd-serie
series_order: 1
og_image: ci-cd-fondamentaux-1200x630.jpg
---

# CI/CD : du commit a la mise en ligne, automatiquement

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-pipeline-simple.svg" alt="Schema d'un pipeline CI/CD simple" class="schema-inline" width="640" />
  <figcaption>Commit, tests, build, controle, deploiement : une recette repetable.</figcaption>
</figure>

La CI/CD, ce n’est pas « un truc de DevOps ». C’est une manière propre de livrer du code :

- **plus vite**,
- **plus souvent**,
- **sans trembler** à chaque déploiement.

Dans cette série, on construit une vision claire et réutilisable. Pas un guide qui finit en copier-coller magique, mais une méthode. Exemple concret : tu pushes une correction de bug un vendredi à 16 h. Le pipeline teste, build, déploie en staging. Tu valides. Tu déploies en prod le lundi — avec le **même** artefact, pas un rebuild « à la main » le jour J.

---

## CI, CD : définition simple

- **CI (Continuous Integration)** : à chaque push / merge, on vérifie automatiquement que le code tient debout (tests, lint, build).
- **CD (Continuous Delivery / Deployment)** :
  - **Delivery** : on prépare un artefact déployable (image Docker, package, bundle), prêt à être lancé.
  - **Deployment** : on déclenche le déploiement automatiquement (souvent après validation).

Dans le langage courant, beaucoup disent « CD » pour tout. L’essentiel : automatiser la vérification, puis automatiser (autant que possible) la mise en ligne.

---

## Pourquoi tu en as besoin (même sur un petit projet)

Sans CI/CD, tu finis avec :

- des builds différents selon la machine,
- des déploiements « à la main » qui oublient un fichier,
- des hotfix en prod impossibles à reproduire.

Avec CI/CD, tu gagnes :

- de la **reproductibilité** (le pipeline fait toujours la même chose),
- un **filet de sécurité** (tests, lint, checks),
- une **traçabilité** (qui a déployé quoi, quand).

Même un site vitrine ou une petite API gagne à avoir : lint + tests + publish. Pas besoin d’un cluster le jour 1.

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

Tu n’es pas obligé de tout faire dès le jour 1. L’important : l’ordre et la logique — les contrôles légers d’abord, le coûteux ensuite. Le détail des portes qui bloquent un mauvais deploy est dans [tests et quality gates](/blog/articles/ci-cd-tests-qualite-gates.html).

---

## Ce qu’on déploie exactement ?

Trois cas fréquents :

- **Site statique** : build + upload (S3, Nginx, GitHub Pages).
- **API / back** : image Docker versionnée + déploiement (Kubernetes, VM, PaaS).
- **Monorepo** : plusieurs builds + plusieurs déploiements.

L’artefact doit être :

- **versionné**,
- **reproductible**,
- **déployable sans rebuild** en prod.

Pour le packaging conteneur, vois [build d’images Docker en CI](/blog/articles/ci-cd-build-images-docker.html). Sur un cluster, les [stratégies de déploiement Kubernetes](/blog/articles/ci-cd-kubernetes-deploiement-strategies.html) complètent le tableau.

### Checklist artefact

- [ ] Tag clair (`1.4.2` ou commit SHA), pas seulement `latest`
- [ ] Même binaire / image testé en staging et promu en prod
- [ ] Rollback possible vers le tag précédent

---

## Éviter les pièges classiques

### 1. Pipeline trop lent

Si ton pipeline met 20 minutes, l’équipe va le contourner.

Réflexes :

- cache des dépendances,
- parallélisation (tests en shards),
- tests ciblés (unitaires rapides → intégration plus tard).

### 2. Pipeline trop « magique »

Un pipeline incompréhensible, c’est une bombe à retardement.

Réflexes :

- étapes nommées clairement,
- scripts simples (Makefile, npm scripts),
- logs lisibles.

### 3. Secrets mal gérés

Pas de mots de passe en dur dans le repo. Jamais. Les détails sont dans [secrets et variables d’environnement](/blog/articles/ci-cd-secrets-variables-environnement.html).

### 4. Déployer sans filet

Pas de staging, pas de smoke test, pas de rollback planifié. Tu découvres le bug… via un client. Prépare au moins un healthcheck et une procédure de retour arrière ([versioning, releases, rollbacks](/blog/articles/ci-cd-versioning-releases-rollbacks.html)).

---

## Comment démarrer en pratique (jour 1)

1. Branche `main` protégée + PR obligatoire.
2. Un workflow minimal : install → lint → tests.
3. Ajoute le build d’artefact.
4. Déploie d’abord **staging** automatiquement.
5. Prod : approbation manuelle, puis auto quand tu es à l’aise.

Tu peux commencer avec [GitHub Actions](/blog/articles/ci-cd-github-actions-workflow-complet.html) ou [GitLab CI](/blog/articles/ci-cd-gitlab-ci-pipeline-complet.html) — l’outil compte moins que la discipline.

### Checklist « pipeline utile »

- [ ] Rouge = on ne merge / ne déploie pas
- [ ] Logs compréhensibles en moins de 2 minutes
- [ ] Staging proche de la prod
- [ ] Au moins une alerte post-deploy ([observabilité des déploiements](/blog/articles/ci-cd-observabilite-deploiements.html))

---

## Comment cette série est organisée

1. **Fondamentaux** (ce que tu lis ici)
2. **Tests + quality gates**
3. **Build d’images Docker**
4. **Secrets / config**
5. **Exemple GitHub Actions**
6. **Exemple GitLab CI**
7. **Déploiement Kubernetes**
8. **GitOps** (Argo CD / Flux)
9. **Versioning + releases**
10. **Observabilité des déploiements**

Objectif final : une chaîne propre du commit jusqu’à la prod, applicable à tes projets Docker / Kubernetes — sans magie, avec des contrôles que ton équipe comprend.
