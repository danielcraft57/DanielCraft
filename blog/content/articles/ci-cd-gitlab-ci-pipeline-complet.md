---
title: "CI/CD : pipeline GitLab CI complet (stages, cache, déploiement)"
date: 2026-02-12
excerpt: "Un pipeline GitLab CI lisible : stages, cache, artefacts, build d'image, push registry et déploiement. Les mêmes idées que GitHub Actions, côté GitLab."
type: article
tags: [CI/CD, GitLab CI, Docker, pipeline, DevOps]
series: ci-cd-serie
series_order: 6
og_image: ci-cd-gitlab-1200x630.jpg
---

# CI/CD : pipeline GitLab CI complet (stages, cache, déploiement)

GitLab CI repose sur une idée très simple :

- un fichier `.gitlab-ci.yml`,
- des **stages**,
- des **jobs** qui s'exécutent dans cet ordre.

Même logique que GitHub Actions, juste une syntaxe différente.

---

## Exemple `.gitlab-ci.yml` (structure propre)

```yaml
stages:
  - test
  - build
  - deploy

variables:
  DOCKER_TLS_CERTDIR: ""

cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/

test:
  stage: test
  image: node:22-alpine
  script:
    - npm ci
    - npm run lint
    - npm run typecheck
    - npm test

build-image:
  stage: build
  image: docker:27
  services:
    - docker:27-dind
  script:
    - docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" "$CI_REGISTRY"
    - docker build -t "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA" .
    - docker push "$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA"
  only:
    - main

deploy-staging:
  stage: deploy
  image: bitnami/kubectl:1.29
  script:
    - echo "$KUBECONFIG_B64" | base64 -d > kubeconfig.yml
    - export KUBECONFIG="$PWD/kubeconfig.yml"
    - kubectl set image deployment/ton-api api="$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA" -n staging
    - kubectl rollout status deployment/ton-api -n staging
  only:
    - main
```

Ce pipeline :

- teste tout,
- build/push l'image sur `main`,
- déploie sur staging.

---

## Bonnes pratiques GitLab CI

- garde tes stages explicites (`test`, `build`, `deploy`),
- utilise cache et artefacts (mais pas n'importe comment),
- sépare staging/prod,
- évite de mettre des scripts énormes en ligne : appelle un `make deploy` ou un script `scripts/ci/deploy.sh`.

Prochaine étape : côté Kubernetes, on regarde les **stratégies de déploiement** (rolling update, blue/green, canary) et comment gérer rollbacks proprement.

