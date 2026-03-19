---
title: "AWS : les fondamentaux et grands types de services"
date: 2025-05-06
excerpt: "Comprendre la philosophie d’AWS, les grandes familles de services (compute, stockage, bases de données, réseau, sécurité, observabilité) et comment choisir les bons blocs pour ton application."
type: article
tags: [AWS, cloud, architecture, services managés, DevOps]
series: aws-serie
series_order: 1
og_image: aws-fondamentaux-1200x630.jpg
---

# AWS : les fondamentaux et grands types de services

Quand on découvre AWS pour la première fois, la sensation est souvent la même : **trop de services, trop de noms, trop d’options**.
L’objectif de cet article est de poser une carte lisible du territoire avant d’entrer dans le détail dans les articles suivants de la série.

---

## 1. Philosophie d’AWS en une phrase

AWS fournit des **briques d’infrastructure managées** (serveurs, stockage, bases, réseau, sécurité, observabilité…) que tu peux assembler pour construire :

- des **applications web** (sites, APIs, backends) ;
- des **systèmes temps réel** (IoT, streaming, jeux en ligne) ;
- des **pipelines data / analytics / IA** ;
- des **plateformes internes** (back‑office, SaaS B2B, outils métiers).

L’idée clé : **tu loues les briques dont tu as besoin, à la demande, et tu ne gères plus le matériel physique**.

---

## 2. Les grandes familles de services AWS

Plutôt que mémoriser 200+ noms, il vaut mieux retenir quelques catégories.

### 2.1 Compute (puissance de calcul)

Services principaux :

- **EC2** : machines virtuelles (serveurs) que tu administres comme un VPS classique.
- **ECS / EKS** : exécution de conteneurs (Docker) avec orchestration (ECS propriétaire, EKS = Kubernetes managé).
- **Lambda** : fonctions serverless, facturées à l’exécution (pas de serveur à gérer).

**Pour quels types d’applications ?**

- EC2 : lift & shift, applis existantes, besoins très spécifiques (binaire, OS).
- ECS / EKS : microservices, APIs conteneurisées, architectures modernes.
- Lambda : APIs légères, jobs planifiés, webhooks, traitement événementiel.

Nous détaillerons ces services dans l’article 2 de la série.

### 2.2 Stockage

- **S3** : stockage d’objets (fichiers) durable et peu cher.
- **EBS** : disques attachés aux instances EC2 (comme un SSD local).
- **EFS** : système de fichiers partagé entre plusieurs serveurs.

Usage typique :

- S3 pour les **backups, assets statiques, logs, exports** ;
- EBS pour les **disques d’instances** (OS, données locales) ;
- EFS pour les **applications qui nécessitent un partage de fichiers** entre plusieurs machines.

### 2.3 Bases de données

- **RDS** : bases relationnelles managées (PostgreSQL, MySQL, Aurora, etc.).
- **DynamoDB** : base NoSQL clé/valeur ultra scalable.
- **Amazon Aurora** : base relationnelle optimisée pour le cloud (version compatible MySQL / PostgreSQL).

Tu choisis en fonction :

- du **modèle de données** (relationnel vs clé/valeur) ;
- des **contraintes de scalabilité et de latence** ;
- de l’écosystème existant (ORM, outils).

### 2.4 Réseau et CDN

- **VPC** : réseau virtuel isolé dans lequel vivent tes ressources AWS.
- **Route 53** : DNS managé (et parfois équilibrage global).
- **CloudFront** : CDN pour distribuer ton contenu au plus près des utilisateurs.

Ce bloc te permet de :

- définir des **zones privées / publiques** ;
- contrôler les **flux entrants / sortants** ;
- **accélérer** la livraison de tes assets et APIs partout dans le monde.

### 2.5 Sécurité, identité, conformité

- **IAM** : gestion des identités (utilisateurs, rôles, permissions).
- **KMS** : gestion de clés de chiffrement.
- **Secrets Manager / Systems Manager Parameter Store** : stockage sécurisé de secrets.
- **AWS WAF / Shield** : protection applicative (filtrage, attaques DDoS).

La règle : on ne met **jamais** de clés d’accès en dur dans le code ou les images, on passe par IAM et des rôles bien calibrés.

### 2.6 Observabilité et gouvernance

- **CloudWatch** : métriques, logs, alarmes.
- **X-Ray** : traçage des requêtes (APM léger).
- **CloudTrail** : audit des appels API AWS (qui a fait quoi, quand).

Ces briques sont indispensables pour :

- comprendre le comportement de ton système ;
- diagnostiquer les problèmes ;
- répondre aux exigences de conformité (qui a créé/supprimé telle ressource).

---

## 3. Comment choisir les bons services ?

Pour éviter la sur‑ingénierie, pars de **l’usage** :

1. **Type d’application**
   - Site vitrine / portfolio.
   - API back‑office / SaaS.
   - Pipeline data / ETL.
   - Application temps réel (chat, IoT…).

2. **Contraintes**
   - Trafic attendu (quelques centaines, milliers, millions de requêtes).
   - Sensibilité aux pannes (tolérance aux interruptions, RPO/RTO).
   - Budget (coût mensuel cible).
   - Compétences de l’équipe (Linux, Docker, Kubernetes, serverless…).

3. **Pattern standard AWS**
   - **Small / MVP** : S3 + CloudFront + Lambda + RDS (ou même S3 + CloudFront + API Gateway + Lambda).
   - **Appli web classique** : ALB + ECS/Fargate ou EC2 + RDS + S3 + CloudFront.
   - **Data / analytics** : S3 + Glue + Athena/Redshift + Lambda/ECS.

Les articles suivants détailleront ces patterns avec des exemples concrets.

---

## 4. Avantages et limites d’AWS

### 4.1 Avantages

- **Écosystème énorme** : pratiquement tout ce dont tu as besoin existe déjà.
- **Pay as you go** : tu démarres petit, tu montes en charge au besoin.
- **Intégrations natives** : IAM, CloudWatch, KMS fonctionnent ensemble.
- **Régions multiples** : possibilité de déployer près des utilisateurs.

### 4.2 Limites / points de vigilance

- **Complexité** : le nombre de services peut faire peur et conduire à de mauvais choix.
- **Coût** : sans suivi ni politiques de gouvernance, la facture peut monter très vite.
- **Verrouillage** : plus tu utilises de services managés spécifiques, plus tu es lié à AWS.

La clé est de **connaître les blocs de base**, puis de limiter les services “exotiques” aux besoins réellement différenciants.

---

## 5. Optimisation et gestion : principes transverses

Avant de zoomer service par service, garde ces réflexes généraux :

- **Taguer toutes les ressources** (`env`, `project`, `owner`) pour suivre les coûts et nettoyer ce qui traîne.
- **Automatiser** : Terraform / CloudFormation / CDK ou au minimum des scripts de provisionnement répétables.
- **Isoler par environnements** : comptes ou VPC séparés pour `dev`, `staging`, `prod`.
- **Mesurer en continu** : CloudWatch + Cost Explorer + budgets/alertes.
- **Sécurité by design** : IAM minimal, pas de secrets en dur, chiffrement activé par défaut.

---

## 6. Pour la suite de la série

Dans les prochains articles, on va :

1. Plonger dans le **compute** (EC2, Lambda, ECS, EKS) et les bons patterns de déploiement en fonction de ton application.  
2. Comparer et positionner les **services de stockage** (S3, EBS, EFS) dans des cas concrets.  
3. Explorer les **bases de données** managées (RDS, DynamoDB, Aurora) et comment les combiner.  
4. Mettre en place un **réseau AWS propre** (VPC, subnets, sécurité, DNS, CDN).  
5. Parler **sécurité, observabilité et optimisation des coûts** avec des checklists actionnables.

L’objectif : que tu sois capable de **lire un diagramme d’architecture AWS, le critiquer et le faire évoluer** en connaissance de cause.+
