---
title: "Sécurité AWS : IAM, KMS, WAF – bâtir des fondations solides"
date: 2025-05-22
excerpt: "Comprendre les briques de sécurité AWS (IAM, KMS, WAF, Secrets Manager) et mettre en place des bonnes pratiques concrètes pour protéger tes applications et données."
type: article
tags: [AWS, sécurité, IAM, KMS, WAF, secrets]
series: aws-serie
series_order: 6
og_image: aws-securite-iam-kms-waf-1200x630.jpg
---

# Sécurité AWS : IAM, KMS, WAF – bâtir des fondations solides

Une architecture AWS puissante mais mal sécurisée est une **bombe à retardement**.
La bonne nouvelle : AWS fournit de nombreuses briques pour mettre en place une sécurité saine,
à condition de les utiliser correctement.

---

## 1. IAM : qui peut faire quoi ?

### 1.1 Principes de base

**IAM (Identity and Access Management)** gère :

- les **utilisateurs** et **groupes** ;
- les **rôles** (attachés aux services, aux workloads) ;
- les **politiques** (JSON) qui définissent les permissions.

Le principe central : **least privilege** – ne donner que les droits nécessaires.

### 1.2 Bonnes pratiques

- Utiliser des **rôles IAM** pour les workloads (EC2, ECS, Lambda…), pas de clés statiques dans le code.
- Éviter le compte racine, activer le MFA, limiter les utilisateurs IAM humains (préférer SSO).
- Grouper les permissions par rôle (ex : `app-backend-role`, `app-batch-role`, `deploy-role`).

---

## 2. KMS : gérer les clés de chiffrement

**AWS KMS (Key Management Service)** gère les clés de chiffrement utilisées par :

- S3, EBS, RDS, EFS, DynamoDB, etc. ;
- tes propres applications (via l’API KMS).

Objectif :

- centraliser le contrôle des clés ;
- tracer qui utilise quelles clés, quand.

Bonnes pratiques :

- activer le chiffrement au repos sur les services qui le supportent ;
- restreindre l’usage des clés KMS (IAM sur les clés elles‑mêmes) ;
- surveiller les logs CloudTrail pour les opérations KMS sensibles.

---

## 3. Secrets Manager et Parameter Store

Pour stocker :

- mots de passe ;
- clés API ;
- chaînes de connexion.

Deux options principales :

- **AWS Secrets Manager** : rotation automatique, intégration poussée.
- **SSM Parameter Store** : paramètres (plain / chiffrés) pour la config applicative.

Règle d’or : **jamais de secrets en clair dans le code, les images Docker ou les fichiers de config versionnés**.

---

## 4. AWS WAF et Shield : filtrer les attaques

**AWS WAF** (Web Application Firewall) protège :

- CloudFront ;
- ALB ;
- API Gateway.

Tu peux y définir des règles pour :

- bloquer certaines IP / pays ;
- limiter certains patterns de requêtes (SQLi, XSS, bots…).

**AWS Shield** fournit une protection DDoS gérée sur certaines ressources (inclus en version Standard).

---

## 5. Gouvernance et hygiène de sécurité

### 5.1 Comptes et environnements

- Séparer **dev/staging/prod** (par comptes AWS ou au minimum par VPC clairement isolés).
- Appliquer des **politiques de Service Control Policy (SCP)** dans les organisations complexes.

### 5.2 Journalisation et audit

- Activer **CloudTrail** pour tracer les appels API AWS.
- Centraliser les logs dans un compte dédié ou un bucket S3 sécurisé.
- Mettre en place des alertes (CloudWatch) sur les événements critiques (création de clés, modification des rôles, ouverture de ports, etc.).

### 5.3 Revue régulière

- Revoir les rôles IAM au moins une fois par trimestre.
- Auditer les buckets S3 publics, les ressources exposées sur Internet.
- Mettre à jour les dépendances applicatives et les AMI régulièrement.

---

## 6. Résumé

Une bonne sécurité AWS repose sur trois piliers :

- **IAM propre** (rôles, least privilege, pas de clés dans le code) ;
- **Chiffrement systématique** (KMS, secrets bien gérés) ;
- **Surface exposée minimale** (WAF, security groups, VPC).

Dans les autres articles de la série, on combine ces briques avec le compute, le stockage, les bases de données et l’observabilité pour construire des plateformes complètes, performantes **et** sécurisées.+
