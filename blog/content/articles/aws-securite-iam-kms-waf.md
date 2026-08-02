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

# AWS : qui a le droit d'ouvrir quoi

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/aws-secu-couches.svg" alt="Schema couches securite AWS IAM KMS WAF" class="schema-inline" width="640" />
  <figcaption>IAM, KMS, reseau, WAF, detection : des couches, pas un outil unique.</figcaption>
</figure>

Une architecture AWS puissante mais mal sécurisée est une **bombe à retardement**. Tu n’as pas besoin d’être expert cybersécurité pour poser des bases saines. Pense en **couches** : qui peut faire quoi (IAM), chiffrement (KMS), secrets, surface exposée (WAF, security groups), journalisation (CloudTrail).

Si une couche rate, une autre limite les dégâts. Un outil unique « qui sécurise tout » n’existe pas.

---

## 1. IAM : qui peut faire quoi ?

### 1.1 Principes de base

**IAM (Identity and Access Management)** gère :

- les **utilisateurs** et **groupes** (humains) ;
- les **rôles** (attachés aux services : EC2, Lambda, ECS…) ;
- les **politiques** (JSON) qui listent les actions autorisées ou refusées.

Le principe central : **least privilege** — ne donner que le minimum nécessaire. « AdminAccess partout, on verra plus tard » est la phrase la plus chère du cloud.

Exemple mental : une Lambda qui lit un bucket S3 n’a pas besoin de créer des utilisateurs IAM ni de supprimer des VPC. Elle a besoin de `s3:GetObject` sur *ce* bucket, point.

### 1.2 Bonnes pratiques concrètes

- Utiliser des **rôles IAM** pour les workloads (EC2, ECS, Lambda…), **pas** de clés d’accès statiques dans le code, les `.env` commités ou les images Docker.
- Éviter le compte **root** au quotidien ; activer le **MFA** ; préférer SSO (IAM Identity Center) plutôt que 40 utilisateurs IAM humains.
- Nommer des rôles clairs : `app-backend-role`, `app-batch-role`, `deploy-role`.
- Séparer les droits **deploy** (CI/CD) des droits **runtime** (l’appli en prod).

Piège classique : coller `AdministratorAccess` sur un rôle EC2 « pour que ça marche ». Ça marche — et offre tout le compte à quiconque compromet la machine.

Pour le compute, voir [EC2 / Lambda / ECS](/blog/articles/aws-compute-ec2-lambda-ecs-eks.html).

---

## 2. KMS : gérer les clés de chiffrement

**AWS KMS (Key Management Service)** centralise les clés utilisées par :

- S3, EBS, RDS, EFS, DynamoDB, etc. ;
- tes applications (via l’API KMS Encrypt/Decrypt).

Objectifs simples :

- savoir **qui** peut utiliser **quelle** clé ;
- tracer les usages sensibles (via CloudTrail) ;
- pouvoir **désactiver** une clé en cas d’incident (effet de levier fort).

Bonnes pratiques débutant :

1. Activer le **chiffrement au repos** sur S3, EBS, RDS — c’est souvent une case à cocher.
2. Restreindre l’usage des clés via les politiques KMS **et** IAM (double verrou).
3. Éviter de partager une clé « fourre‑tout » pour toute l’entreprise : une clé par domaine (prod DB, backups, app secrets) facilite l’audit.

Le chiffrement n’empêche pas une mauvaise policy IAM : si un rôle peut déchiffrer, un attaquant avec ce rôle aussi. KMS complète IAM, il ne le remplace pas.

---

## 3. Secrets Manager et Parameter Store

À stocker hors du code : mots de passe, clés API, chaînes de connexion, tokens.

| Service | Usage typique |
|---------|----------------|
| **Secrets Manager** | secrets sensibles, rotation auto (ex. mot de passe RDS) |
| **SSM Parameter Store** | config + paramètres SecureString chiffrés |

Règle d’or : **jamais** de secrets en clair dans Git, une image Docker ou Slack. L’appli les récupère au démarrage via son rôle IAM. En local : `.env` non versionné ; en cloud : Secrets Manager / Parameter Store.

---

## 4. AWS WAF et Shield : filtrer devant la porte

**AWS WAF** (Web Application Firewall) se place devant :

- CloudFront ;
- ALB ;
- API Gateway.

Tu y définis des règles pour :

- bloquer des IP / pays ;
- limiter le rate (anti‑bruteforce) ;
- filtrer des patterns connus (SQLi, XSS) via des managed rules AWS ou partenaires.

**AWS Shield Standard** (inclus) aide contre certains DDoS sur les services éligibles. Shield Advanced est un autre budget, pour les cas très exposés.

WAF n’excuse pas une appli pleine de failles : c’est un **filet**. Combine‑le avec des security groups serrés (voir [réseaux VPC](/blog/articles/aws-reseaux-vpc-route53-cloudfront.html)) : la base n’écoute jamais sur Internet, seulement depuis l’ALB / le VPC applicatif.

---

## 5. Gouvernance et hygiène de sécurité

### 5.1 Comptes et environnements

- Séparer **dev / staging / prod** (idéalement par comptes AWS, sinon au minimum VPC + IAM très stricts).
- Dans une Organisation AWS, les **SCP** (Service Control Policies) empêchent même les admins d’un compte de faire certaines actions (ex. désactiver CloudTrail).

Un incident en staging ne doit pas pouvoir toucher la prod « parce que même compte, mêmes clés ».

### 5.2 Journalisation et audit

- Activer **CloudTrail** (historique des appels API) et le garder longtemps.
- Centraliser les logs dans un compte / bucket dédié, avec accès restreint.
- Alerter (CloudWatch / EventBridge) sur : création de clés d’accès, modification de rôles admin, security group `0.0.0.0/0` sur SSH/RDP, désactivation de MFA…

Sans logs, tu ne sauras pas *quand* ni *comment* quelqu’un a ouvert la porte.

### 5.3 Revue régulière (le vrai métier)

Une checklist trimestrielle simple :

- rôles IAM trop permissifs ;
- buckets S3 publics involontaires ;
- clés d’accès humaines non utilisées ;
- AMI / images / dépendances à jour ;
- secrets qui n’ont jamais tourné.

La sécurité AWS, ce n’est pas un projet d’un week‑end : c’est une **habitude**.

---

## 6. Résumé

Une bonne sécurité AWS repose sur trois piliers :

1. **IAM propre** — rôles, least privilege, pas de clés dans le code ;
2. **Chiffrement et secrets** — KMS, Secrets Manager / Parameter Store ;
3. **Surface exposée minimale** — WAF, security groups, VPC, pas de base publique.

Dans le reste de la série, on combine ces briques avec le compute, le stockage, les bases et l’[observabilité](/blog/articles/aws-observabilite-cloudwatch-xray-cloudtrail.html). Une plateforme performante mais non sécurisée n’est pas « presque prête » — elle est dangereuse.
