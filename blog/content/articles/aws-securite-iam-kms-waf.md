---
title: "AWS : qui a le droit d'ouvrir quoi"
date: 2025-05-22
excerpt: "IAM, clés, pare-feu applicatif : des couches de protection simples à comprendre."
type: article
tags: [AWS, sécurité, IAM, KMS, WAF, secrets]
series: aws-serie
series_order: 6
og_image: aws-securite-iam-kms-waf-1200x630.jpg
---

# [AWS](/blog/articles/aws-fondamentaux-cloud-aws-services.html) : qui a le droit d'ouvrir quoi

Une architecture AWS puissante mais mal fermee, c'est une **porte ouverte** avec un joli salon. La bonne nouvelle : AWS donne les serrures. Encore faut-il les utiliser.

---

## IAM : qui a les cles ?

**IAM** gere les identites : utilisateurs, groupes, **roles**, politiques (permissions en JSON).

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/aws-secu-couches.svg" alt="Schema couches securite AWS IAM KMS WAF" class="schema-inline" width="640" />
  <figcaption>IAM, KMS, reseau, WAF, detection : des couches, pas un outil unique.</figcaption>
</figure>

Principe central : **least privilege** - ne donner que le necessaire. Comme ne pas donner toutes les cles de la maison a chaque invite.

Bons reflexes :

- Roles pour les workloads ([EC2](/blog/articles/aws-compute-ec2-lambda-ecs-eks.html), ECS, Lambda) - **pas** de cles statiques dans le code.
- Evite le compte racine au quotidien. Active le [MFA](/blog/articles/iam-mfa-principes-zero-trust.html). Prefere le SSO pour les humains.
- Un role par metier : `app-backend`, `app-batch`, `deploy`.

---

## KMS : le trousseau chiffre

**KMS** gere les cles de chiffrement utilisees par [S3](/blog/articles/aws-stockage-s3-ebs-efs.html), EBS, [RDS](/blog/articles/aws-bases-donnees-rds-dynamodb-aurora.html), DynamoDB... et par ton code si besoin.

Objectif : centraliser les cles, savoir qui les utilise.

- Active le chiffrement au repos partout ou c'est simple.
- Restreins l'usage des cles via IAM.
- Surveille les operations sensibles avec [CloudTrail](/blog/articles/aws-observabilite-cloudwatch-xray-cloudtrail.html).

---

## Secrets : hors du code

Mots de passe, cles API, chaines de connexion :

- **Secrets Manager** : rotation auto, integrations fortes.
- **Parameter Store** : config (claire ou chiffree).

Regle d'or : **jamais** de secret en clair dans le code, les [images Docker](/blog/articles/docker-fondamentaux-images-conteneurs.html), ou un fichier Git. Si tu viens de [Docker prod](/blog/articles/docker-production-registry-securite.html), c'est la meme idee.

---

## WAF et Shield : le filtre devant la porte

**WAF** se place devant CloudFront, ALB, API Gateway. Tu bloques certaines IP / pays, tu limites des patterns d'attaque (SQLi, XSS, bots...).

**Shield** aide contre le DDoS (Standard inclus sur certaines ressources).

Le duo marche bien avec un [reseau propre](/blog/articles/aws-reseaux-vpc-route53-cloudfront.html) : CloudFront + WAF + ALB + subnets prives.

---

## Hygiene au quotidien

- Separe **dev / staging / prod** (comptes ou VPC clairement isoles).
- Active CloudTrail. Centralise les logs. Alerte sur creation de cles, changement de roles, ouverture de ports.
- Revois les roles IAM chaque trimestre. Cherche les buckets S3 publics. Mets a jour AMI et deps.

---

## Resume

Trois piliers : **IAM propre**, **chiffrement + secrets bien ranges**, **surface exposee minimale** (WAF, SG, VPC). Ensuite, vois vraiment ce qui se passe avec [l'observabilite](/blog/articles/aws-observabilite-cloudwatch-xray-cloudtrail.html).
