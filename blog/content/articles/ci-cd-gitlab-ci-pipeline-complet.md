---
title: "GitLab CI : des etapes claires jusqu'au deploiement"
date: 2025-03-20
excerpt: "Stages, cache et deploiement : une pipeline GitLab simple a suivre."
type: article
tags: [CI/CD, GitLab CI, Docker, pipeline, DevOps]
series: ci-cd-serie
series_order: 6
og_image: ci-cd-gitlab-1200x630.jpg
---

# GitLab CI : des etapes claires jusqu'au deploiement

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-gitlab-ci.svg" alt="Schema des stages GitLab CI" class="schema-inline" width="640" />
  <figcaption>build, test, package, deploy : une chaine lisible.</figcaption>
</figure>

GitLab CI repose sur une idée très simple : un fichier `.gitlab-ci.yml` à la racine du dépôt, des **stages** qui s'enchaînent, et des **jobs** qui s'exécutent dans chaque stage. Même logique que GitHub Actions, syntaxe différente. L'avantage : tout est intégré si tu héberges déjà ton code sur GitLab.

## Anatomie d'une pipeline GitLab

Chaque pipeline est déclenchée par un push, une merge request ou un tag. Les jobs d'un même stage s'exécutent en parallèle ; les stages s'enchaînent séquentiellement. Un job qui échoue bloque les stages suivants (sauf si tu configures `allow_failure`).

Structure type pour une API conteneurisée :

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

Ce pipeline teste le code, build et push l'image Docker sur `main`, puis déploie sur staging. Le tag `$CI_COMMIT_SHA` garantit la traçabilité : tu sais exactement quel commit tourne en staging.

## Stages, jobs et règles de déclenchement

Garde tes stages explicites et peu nombreux : `test`, `build`, `deploy`. Ajouter un stage `security` pour les scans SAST ou des images Docker, c'est une bonne pratique en production.

Utilise `rules` ou `only/except` pour contrôler quand un job s'exécute :

- Tests sur toutes les merge requests
- Build d'image uniquement sur `main` ou sur les tags
- Déploiement prod manuel (`when: manual`) pour éviter les mises en prod accidentelles

Les **variables CI/CD** (Settings → CI/CD → Variables) stockent les secrets : token registry, kubeconfig encodé, clés API. Coche « Masked » et « Protected » pour les variables sensibles.

## Cache et artefacts : accélérer sans fausser

Le cache GitLab réutilise des dossiers entre pipelines (`node_modules/`, `.npm/`). La clé `${CI_COMMIT_REF_SLUG}` isole le cache par branche. Attention : un cache corrompu peut provoquer des builds intermittents. En cas de doute, vide-le depuis l'interface GitLab.

Les **artefacts** passent des fichiers d'un job à un autre (rapport de tests, binaire compilé). Exemple : le job `test` produit un rapport JUnit, le job `deploy` consomme le binaire buildé. Les artefacts expirent : définis une durée de rétention adaptée.

## Docker-in-Docker et registry intégré

GitLab propose un Container Registry intégré (`$CI_REGISTRY_IMAGE`). Pas besoin de Docker Hub si tu es déjà sur GitLab. Le service `docker:dind` (Docker-in-Docker) permet de builder des images dans un runner Docker.

Points de vigilance :

- `DOCKER_TLS_CERTDIR: ""` simplifie la config sur les runners partagés
- Utilise des images de base légères (`alpine`) pour accélérer les pulls
- Scanne tes images avec Trivy ou GitLab Container Scanning avant la prod

## Séparer staging et production

Ne déploie jamais directement en prod depuis une branche feature. Pattern recommandé :

1. Merge sur `main` → déploiement staging automatique
2. Validation manuelle ou tests E2E sur staging
3. Job `deploy-prod` déclenché manuellement ou via tag sémantique (`v1.2.3`)

Externalise les scripts longs dans `scripts/ci/deploy.sh` plutôt que des blocs YAML de 50 lignes. Ça facilite le debug local et la relecture en code review.

## Runners : shared vs self-hosted

Les runners GitLab.com (shared) conviennent pour démarrer. En production, un runner self-hosted te donne plus de contrôle (accès réseau interne, cache persistant, conformité). Installe-le sur une VM ou un pod Kubernetes selon ton infra.

## Conclusion

Une pipeline GitLab CI lisible repose sur des stages clairs, un cache maîtrisé et une séparation staging/prod. Tag tes images avec le SHA du commit, externalise les scripts de déploiement et protège tes secrets via les variables CI/CD. Pour comparer avec l'écosystème GitHub, consulte le guide sur [GitHub Actions et les workflows complets](/blog/articles/ci-cd-github-actions-workflow-complet.html).
