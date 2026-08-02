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

Après avoir vu les briques compute, stockage, réseau et sécurité, il reste un point clé : **comment livrer ton application proprement et régulièrement**.

Sur AWS, tu n’as pas besoin d’inventer toute la chaîne toi-même. Une suite de services couvre le chemin du commit jusqu’à la prod :

- **CodeCommit** : dépôt Git managé ;
- **CodeBuild** : builds et tests ;
- **CodeDeploy** : déploiement sur [EC2](/blog/articles/aws-compute-ec2-lambda-ecs-eks.html), ECS ou Lambda ;
- **CodePipeline** : orchestration de bout en bout.

L’idée n’est pas « un bouton magique », mais une **recette répétable** : mêmes étapes, mêmes contrôles, même artefact, à chaque livraison. Si tu découvres encore la logique générale des pipelines, les [fondamentaux CI/CD](/blog/articles/ci-cd-fondamentaux-pipelines.html) donnent le cadre avant de zoomer sur AWS.

---

## 1. Vue d’ensemble d’une pipeline AWS

Un pipeline typique ressemble à ceci :

1. Push sur la branche `main` (CodeCommit ou GitHub).
2. CodePipeline déclenche un **build CodeBuild** : dépendances, tests, build d’artefacts ([image Docker](/blog/articles/docker-fondamentaux-images-conteneurs.html), bundle frontend…).
3. Les artefacts partent vers [S3](/blog/articles/aws-stockage-s3-ebs-efs.html) ou ECR.
4. CodeDeploy (ou un job custom) déploie : ECS/EKS (rolling, blue/green), EC2, ou Lambda.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/aws-cicd-pipeline.svg" alt="Schema pipeline CI/CD AWS CodePipeline CodeBuild" class="schema-inline" width="640" />
  <figcaption>CodePipeline + CodeBuild : du commit au deploy avec des gates.</figcaption>
</figure>

Exemple concret : tu merges une PR sur une API Node. CodeBuild lance `npm ci`, `npm test`, puis build l’image. L’image taguée `api:1.4.2` arrive dans ECR. CodeDeploy bascule le service ECS vers cette version. Si le healthcheck échoue, tu reviens à l’ancienne image sans reconstruire.

---

## 2. CodeCommit (ou GitHub / GitLab)

**CodeCommit** est un Git managé dans AWS. Il a du sens si tu veux rester 100 % dans le cloud AWS, ou si ton organisation est déjà centrée sur IAM et les VPC.

Sinon, **garde GitHub ou GitLab** et connecte CodePipeline dessus. C’est courant, et souvent plus simple pour les équipes déjà sur ces forges. L’important : une seule source de vérité Git, des branches claires (`main`, `staging`), et des protections de branche (reviews, checks verts).

### Checklist dépôt

- [ ] Branche `main` protégée (pas de push direct)
- [ ] Tags de release cohérents (`v1.4.2`)
- [ ] Lien pipeline ↔ repo documenté dans le README

---

## 3. CodeBuild et le `buildspec.yml`

**CodeBuild** exécute tes builds dans des environnements conteneurisés. Tu décris les étapes dans un `buildspec.yml` à la racine du repo :

```yaml
version: 0.2
phases:
  install:
    commands:
      - npm ci
  pre_build:
    commands:
      - npm test
  build:
    commands:
      - npm run build
artifacts:
  files:
    - dist/**/*
```

Bonnes pratiques :

- rendre le build **idempotent** (même commit → même résultat) ;
- figer les versions d’outils (Node 20, Python 3.12…) ;
- utiliser une **image de build custom** seulement si tu as vraiment besoin d’outils spécifiques.

### Pièges fréquents

- Installer des dépendances « à la main » dans la console au lieu de les déclarer dans le `buildspec`.
- Oublier le cache des deps : le pipeline devient lent, l’équipe le contourne.
- Tester uniquement en local : le build AWS révèle souvent des chemins ou des secrets manquants.

Pour aller plus loin sur la qualité avant déploiement, vois les [portes qualité CI/CD](/blog/articles/ci-cd-tests-qualite-gates.html).

---

## 4. CodeDeploy : comment tu bascules

**CodeDeploy** déploie vers plusieurs cibles :

- EC2 / on-prem (agent CodeDeploy) ;
- ECS (rolling ou blue/green) ;
- Lambda (versions + alias).

Tu définis une stratégie : pourcentage de trafic basculé, durée de monitoring, action en cas d’échec (rollback). Exemple : blue/green sur ECS — la nouvelle tâche démarre à côté, tu bascules 10 % du trafic, tu regardes les erreurs, puis 100 %. Si ça casse, tu reviens en un clic.

Sans stratégie claire, tu fais un « big bang » : tout le monde bascule d’un coup. Ça marche… jusqu’au jour où ça ne marche plus.

---

## 5. CodePipeline : l’orchestreur

**CodePipeline** enchaîne les stages : Source → Build → Test → Deploy. Il relie les services, affiche l’état graphique, et permet des **approbations manuelles** (utile avant la prod).

Tu peux aussi brancher CloudFormation pour provisionner l’infra, ou une Lambda pour une étape custom (notifier Slack, valider un changelog…). Pour suivre ce qui se passe après le deploy, couple la chaîne avec [CloudWatch / X-Ray](/blog/articles/aws-observabilite-cloudwatch-xray-cloudtrail.html).

---

## 6. Bonnes pratiques CI/CD sur AWS

- **Environnements séparés** : `dev`, `staging`, `prod` (pipelines dédiés ou stages clairs).
- **Tests automatiques** avant tout déploiement prod.
- **Artefacts figés** dans S3/ECR : on déploie un tag précis, on ne rebuild pas « depuis main » en urgence.
- **Secrets hors du repo** : Parameter Store / Secrets Manager, jamais en clair dans le `buildspec` versionné. Voir aussi la gestion des [secrets dans une pipeline](/blog/articles/ci-cd-secrets-variables-environnement.html).
- **Observabilité du deploy** : tags Git, changelog, alarmes CPU/erreur 5xx.

### Checklist avant de « passer en auto »

- [ ] Staging reçoit le même artefact que la future prod
- [ ] Rollback testé au moins une fois
- [ ] Alarmes et healthchecks en place
- [ ] Qui peut approuver la prod est documenté

---

## 7. Résumé

La suite DevOps AWS permet une CI/CD complète **sans quitter le cloud** : dépôt (CodeCommit ou GitHub), build/test (CodeBuild), déploiement (CodeDeploy), orchestration (CodePipeline).

Tu peux aussi combiner AWS avec [GitHub Actions](/blog/articles/ci-cd-github-actions-workflow-complet.html) ou GitLab CI : build ailleurs, déploiement sur AWS. Choisis l’outil que ton équipe comprend — la discipline (tests, artefacts figés, rollback) compte plus que le logo du service.
