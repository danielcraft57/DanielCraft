---
title: "AWS : publier du code automatiquement"
date: 2025-06-05
excerpt: "Du commit au déploiement avec des contrôles qualité — pas juste un bouton magique."
type: article
tags: [AWS, DevOps, CI/CD, CodePipeline, CodeBuild, CodeDeploy]
series: aws-serie
series_order: 10
og_image: aws-devops-ci-cd-codepipeline-codebuild-1200x630.jpg
---

# [AWS](/blog/articles/aws-fondamentaux-cloud-aws-services.html) : publier du code automatiquement

Après avoir vu les briques compute, stockage, réseau et sécurité, il reste un point clé :
**comment livrer ton application proprement et régulièrement**.

AWS propose une chaîne DevOps complète :

- **CodeCommit** : dépôt Git managé ;
- **CodeBuild** : builds et tests ;
- **CodeDeploy** : déploiement sur [EC2](/blog/articles/aws-compute-ec2-lambda-ecs-eks.html)/ECS/Lambda ;
- **CodePipeline** : orchestration de bout en bout.

---

## 1. Vue d’ensemble d’une pipeline AWS

Un pipeline typique :

1. Push sur la branche `main` du dépôt (CodeCommit ou GitHub).
2. CodePipeline déclenche un **build CodeBuild** :
   - installation des dépendances ;
   - tests ;
   - build des artefacts ([image Docker](/blog/articles/docker-fondamentaux-images-conteneurs.html), bundle frontend…).
3. Les artefacts sont stockés ([S3](/blog/articles/aws-stockage-s3-ebs-efs.html), ECR).
4. CodeDeploy (ou un job custom) déploie :
   - sur ECS/EKS (rolling, blue/green) ;
   - ou sur EC2 / Lambda.



<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/aws-cicd-pipeline.svg" alt="Schema pipeline CI/CD AWS CodePipeline CodeBuild" class="schema-inline" width="640" />
  <figcaption>CodePipeline + CodeBuild : du commit au deploy avec des gates.</figcaption>
</figure>

---

## 2. CodeCommit

**CodeCommit** est un service Git managé.

Tu peux l’utiliser quand :

- tu veux rester 100 % dans AWS ;
- tu as déjà une organisation centrée sur AWS.

Sinon, tu peux tout à fait garder **GitHub / GitLab** et connecter CodePipeline dessus.

---

## 3. CodeBuild

**CodeBuild** exécute des builds dans des environnements conteneurisés.

- Tu définis un fichier `buildspec.yml` dans ton repo :

```yaml
version: 0.2
phases:
  install:
    commands:
      - npm ci
  build:
    commands:
      - npm test
      - npm run build
artifacts:
  files:
    - dist/**/*
```

- CodeBuild installe, teste et construit tes artefacts.

Bonnes pratiques :

- rendre le build **idempotent** (reproductible) ;
- utiliser des **images de build custom** si nécessaire (outils spécifiques).

---

## 4. CodeDeploy

**CodeDeploy** gère les déploiements vers plusieurs cibles :

- EC2/On‑Prem (agent CodeDeploy) ;
- ECS (rolling ou blue/green) ;
- Lambda (versions, alias).

Tu définis une stratégie :

- pourcentage de trafic basculé ;
- durées de monitoring ;
- actions en cas d’échec (rollback).

---

## 5. CodePipeline

**CodePipeline** est l’orchestreur :

- il définit les **stages** (Source, Build, Test, Deploy) ;
- il relie les services (CodeCommit/GitHub → CodeBuild → CodeDeploy → notifications).

Avantages :

- visualisation graphique du pipeline ;
- possibilités d’intégrer des étapes manuelles (approbations) ;
- intégrations avec d’autres services (CloudFormation, Lambda pour étapes custom).

---

## 6. Bonnes pratiques CI/CD sur AWS

- **Travailler par environnement** : `dev`, `staging`, `prod` avec des pipelines dédiés ou des stages séparés.
- **Automatiser les tests** (unitaires, intégration, end‑to‑end) avant déploiement.
- **Figer les artefacts** (images Docker, archives) dans S3/ECR pour pouvoir rollback.
- Tracer les déploiements (tags Git, changelog, dashboards de monitoring).

---

## 7. Résumé

La suite DevOps AWS permet de construire une CI/CD complète **sans quitter le cloud** :

- dépôt Git (CodeCommit ou GitHub) ;
- build/test (CodeBuild) ;
- déploiement (CodeDeploy) ;
- orchestration (CodePipeline).

Tu peux aussi combiner ces services avec des solutions externes (GitHub Actions, GitLab CI)
pour garder la flexibilité et choisir l’outil le plus adapté à ton équipe.+
