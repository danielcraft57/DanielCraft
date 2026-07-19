---
title: "AWS : le cloud Amazon expliqué simplement"
date: 2025-05-06
excerpt: "Qui fait quoi (toi vs Amazon), et les familles de services sans te noyer dans le catalogue."
type: article
tags: [AWS, cloud, architecture, services managés, DevOps]
series: aws-serie
series_order: 1
og_image: aws-fondamentaux-1200x630.jpg
---

# AWS : le cloud Amazon expliqué simplement

Quand tu ouvres AWS la premiere fois, c'est comme entrer dans un **magasin geant**. Trop de rayons. Trop de noms. Trop d'options.

Cet article pose une **carte simple**. Pas besoin de tout memoriser. Besoin de savoir ou chercher.

---

## AWS en une phrase

AWS te loue des **briques toutes pretes** : serveurs, disques, bases, reseau, secu, surveillance. Tu les assembles. Tu ne geres plus le materiel physique dans une cave.

Tu peux construire :

- un site ou une API,
- un systeme temps reel,
- un pipeline data,
- une plateforme interne.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/aws-shared-responsibility.svg" alt="Schema responsabilite partagee AWS" class="schema-inline" width="640" />
  <figcaption>AWS gere l'infra de base. Toi : identites, config, donnees, apps.</figcaption>
</figure>

Idee cle : tu paies ce que tu utilises. Tu grandis quand tu en as besoin.

---

## Les grandes familles (les rayons du magasin)

### Compute (la force de calcul)

- **EC2** : une machine virtuelle. Comme un serveur classique que tu administres.
- **ECS / EKS** : faire tourner des **[conteneurs](/blog/articles/docker-fondamentaux-images-conteneurs.html)** Docker (ECS = orchestrateur AWS, EKS = Kubernetes manage).
- **Lambda** : un petit bout de code qui s'execute a la demande. Pas de serveur a soigner.

Detail dans [EC2, Lambda, ECS, EKS](/blog/articles/aws-compute-ec2-lambda-ecs-eks.html).

### Stockage

- **S3** : un grand coffre a fichiers (objets). Pas cher. Tres durable.
- **EBS** : le disque colle a une machine EC2.
- **EFS** : un dossier partage entre plusieurs serveurs.

Voir [S3, EBS, EFS](/blog/articles/aws-stockage-s3-ebs-efs.html).

### Bases de donnees

- **RDS** : base relationnelle managee (PostgreSQL, MySQL...).
- **DynamoDB** : base NoSQL cle/valeur, tres scalable.
- **Aurora** : relationnel turbo, pense pour le cloud.

Voir [RDS, DynamoDB, Aurora](/blog/articles/aws-bases-donnees-rds-dynamodb-aurora.html).

### Reseau et CDN

- **VPC** : ton quartier prive dans AWS.
- **Route 53** : le carnet d'adresses DNS.
- **CloudFront** : livre ton contenu proche des utilisateurs (CDN).

Voir [VPC, Route 53, CloudFront](/blog/articles/aws-reseaux-vpc-route53-cloudfront.html).

### Securite

- **[IAM](/blog/articles/iam-mfa-principes-zero-trust.html)** : qui a le droit de faire quoi.
- **KMS** : les cles pour chiffrer.
- **WAF / Shield** : filtre devant tes apps.

Voir [IAM, KMS, WAF](/blog/articles/aws-securite-iam-kms-waf.html).

### Observabilite

- **CloudWatch** : metriques, logs, alarmes.
- **X-Ray** : suivre une requete de bout en bout.
- **CloudTrail** : qui a touche a quoi dans le compte.

Voir [CloudWatch, X-Ray, CloudTrail](/blog/articles/aws-observabilite-cloudwatch-xray-cloudtrail.html).

---

## Comment choisir sans se perdre ?

Pars de l'**usage**, pas de la mode.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/aws-families-services.svg" alt="Schema des familles de services AWS" class="schema-inline" width="640" />
  <figcaption>Pense par familles de services : compute, data, reseau, secu, ops.</figcaption>
</figure>

1. **Type d'appli** : site vitrine, SaaS, data, temps reel ?
2. **Contraintes** : trafic, panne acceptable, budget, competences de l'equipe.
3. **Patterns simples** :
   - MVP : S3 + CloudFront + Lambda + RDS.
   - Appli web classique : ALB + ECS/Fargate ou EC2 + RDS + S3.
   - Data : S3 + outils analytics.

Ensuite tu peaufines [haute dispo](/blog/articles/aws-architectures-ha-scalabilite.html), [couts](/blog/articles/aws-optimisation-couts-reserved-savings-spot.html) et [CI/CD](/blog/articles/aws-devops-ci-cd-codepipeline-codebuild.html).

---

## Avantages et pieges

**Avantages** : enorme catalogue, paiement a l'usage, pieces qui s'emboitent, regions proches des users.

**Pieges** : trop de choix (mauvais choix), facture qui grimpe sans suivi, verrouillage si tu t'accroches trop a des services tres "AWS-only".

La cle : connaitre les **blocs de base**. Limiter les trucs exotiques au vrai besoin.

---

## Reflexes transverses

- **Taguer** chaque ressource (`env`, `project`, `owner`).
- **Automatiser** (Terraform, CloudFormation, CDK...).
- **Separe** dev / staging / prod.
- **Mesurer** (CloudWatch + Cost Explorer).
- **Securite by design** : IAM minimal, pas de secrets en dur, chiffrement active.

---

## Pour la suite

On zoome rayon par rayon. A la fin, tu dois pouvoir **lire un schema AWS**, le critiquer, et le faire evoluer sans panique.
