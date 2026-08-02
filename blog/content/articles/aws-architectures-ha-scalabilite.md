---
title: "AWS : rester en ligne même si une machine tombe"
date: 2025-05-29
excerpt: "Multi-AZ, autoscaling et tests de panne : la haute dispo sans slide marketing."
type: article
tags: [AWS, architecture, haute disponibilité, scalabilité, résilience]
series: aws-serie
series_order: 8
og_image: aws-architectures-ha-scalabilite-1200x630.jpg
---

# [AWS](/blog/articles/aws-fondamentaux-cloud-aws-services.html) : rester en ligne même si une machine tombe

AWS brille quand il s’agit de **tenir la charge** et de **survivre aux pannes matérielles**. Encore faut‑il structurer ton architecture : une seule instance EC2 dans une seule AZ, ce n’est pas « le cloud », c’est un serveur qui a changé d’adresse.

Trois idées suffisent pour démarrer : **répartir** (multi‑AZ), **équilibrer** (load balancer), **ajuster** (autoscaling). Le reste, c’est de la discipline (backups, tests de panne, coûts).

---

## 1. Les briques de la haute disponibilité

### 1.1 Multi‑AZ : ne pas mettre tous les œufs dans la même salle

Une **Availability Zone** (AZ) est un centre de données isolé dans une région. Beaucoup de services AWS se déploient en **Multi‑AZ** :

- [RDS](/blog/articles/aws-bases-donnees-rds-dynamodb-aurora.html) / Aurora (réplica standby dans une autre AZ) ;
- ALB (load balancers multi‑AZ par défaut) ;
- Auto Scaling Groups d’[EC2](/blog/articles/aws-compute-ec2-lambda-ecs-eks.html) ;
- ECS / EKS (nodes répartis sur plusieurs AZ).

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/aws-ha-multi-az.svg" alt="Schema architecture haute disponibilite AWS multi-AZ" class="schema-inline" width="640" />
  <figcaption>Haute dispo = multi-AZ, autoscaling, et des pannes qu'on a deja testees.</figcaption>
</figure>

L’idée concrète : si une AZ perd le réseau ou l’électricité, une autre continue. Ce n’est pas magique : tes **données** doivent aussi être répliquées (RDS Multi‑AZ, DynamoDB global tables plus tard, snapshots S3…). Une appli Multi‑AZ avec une base mono‑AZ reste fragile.

### 1.2 Load balancing : une porte d’entrée, plusieurs travailleurs

- **ALB** (Application Load Balancer) distribue le trafic HTTP/HTTPS vers plusieurs instances ou containers.
- Tu peux router par **path** (`/api/`, `/admin/`) ou par **host** (`api.`, `admin.`).
- Les **health checks** retirent automatiquement une cible malade du pool.

Sans LB, chaque client « colle » à une machine. Avec un ALB + plusieurs cibles saines, la panne d’une instance devient un non‑événement pour l’utilisateur (quelques requêtes en erreur, puis bascule).

---

## 2. Patterns d’architecture web courants

### 2.1 Appli web classique robuste

Schéma type PME / SaaS :

1. [Route 53](/blog/articles/aws-reseaux-vpc-route53-cloudfront.html) (DNS) + CloudFront optionnel (cache CDN) ;
2. ALB en Multi‑AZ ;
3. Auto Scaling Group d’EC2 **ou** ECS/Fargate derrière l’ALB ;
4. RDS/Aurora en Multi‑AZ ;
5. fichiers statiques / uploads sur [S3](/blog/articles/aws-stockage-s3-ebs-efs.html).

Caractéristiques :

- plusieurs instances applicatives (pas de « serveur unique ») ;
- base répliquée ;
- tolérance à la perte d’une AZ pour le compute **et** la BDD.

Astuce : mets la session hors machine (JWT, Redis, DynamoDB). Sinon un scaling out « perd » les sessions mal gérées.

### 2.2 Architecture serverless

Pattern adapté aux pics irréguliers : Route 53 + CloudFront → API Gateway → Lambdas → DynamoDB / Aurora Serverless / S3.

Avantages : peu de serveurs à patcher, scalabilité quasi auto, facturation à l’usage. Contreparties : cold starts, timeouts, debug différent (CloudWatch, X‑Ray). Ce n’est pas « mieux » que EC2 — c’est **différent**.

---

## 3. Autoscaling : adapter la capacité à la charge

### 3.1 Auto Scaling Groups (EC2)

Tu définis un **min / desired / max** :

- min = plancher de disponibilité (ex. 2 pour survivre à 1 panne) ;
- max = plafond budget / capacité ;
- desired = cible actuelle (ajustée par les politiques).

Les politiques réagissent souvent à :

- CPU moyen du groupe ;
- taille d’une file (SQS) ;
- latence ou taux d’erreur (métriques custom / ALB).

Exemple mental : Black Friday → CPU monte → ASG passe de 2 à 8 instances → le lundi → redescend. Sans autoscaling, tu paies 8 machines toute l’année « au cas où ».

### 3.2 ECS, EKS, Lambda

- **ECS / EKS** : tu scales le nombre de tâches ou de pods (CPU, mémoire, backlog de queue).
- **Lambda** : AWS scale pour toi ; tu contrôles surtout la **concurrency** (et les quotas du compte).

Dans tous les cas, scale **horizontalement** (plus d’exemplaires) plutôt que de tout miser sur une grosse machine. Une grosse machine qui tombe = 100 % down.

---

## 4. Tolérance aux pannes : savoir ce que tu couvres

### 4.1 Trois niveaux de panne

| Niveau | Exemple | Couverture typique |
|--------|---------|--------------------|
| Instance | EC2 crash | ASG + health checks |
| AZ | salle indisponible | Multi‑AZ (LB, BDD, nodes) |
| Région | région entière | multi‑région (plus complexe) |

La plupart des projets gagnent énormément en passant de « 1 instance » à « Multi‑AZ + ASG ». Le multi‑région coûte cher en complexité : ne le lance que si le métier l’exige.

### 4.2 Bonnes pratiques concrètes

- Ne jamais dépendre d’**une seule** instance critique.
- Avoir des **backups testés** (restore réel, pas seulement « le snapshot existe »).
- Documenter une procédure de restauration courte.
- Tester des pannes : stopper une instance, health check KO, failover RDS. Un « game day » d’une heure vaut dix slides.

---

## 5. Gouvernance et coûts : la HA a un prix

Plus tu ajoutes de redondance, plus la facture grimpe. Il faut donc :

- choisir le **niveau de disponibilité** selon la criticité (outil interne vs paiement en ligne) ;
- ne pas sur‑dimensionner staging / preprod (souvent 1 AZ suffit hors prod) ;
- utiliser [Savings Plans / Reserved Instances](/blog/articles/aws-optimisation-couts-reserved-savings-spot.html) pour les charges stables (le min de l’ASG, par exemple).

Règle simple : paie la redondance **là où une panne fait mal**. Ailleurs, simplifie.

---

## 6. Résumé

Construire une architecture AWS haute dispo et scalable, c’est :

1. répartir sur **plusieurs AZ** ;
2. passer par un **load balancer** + health checks ;
3. **autoscaler** le compute ;
4. choisir des services managés adaptés (RDS/Aurora, ECS/EKS, Lambda, S3) ;
5. tester les pannes et surveiller (voir les articles observabilité / coûts de la série).

Tu n’as pas besoin de tout faire le jour 1. Commence par : ALB + 2 instances en Multi‑AZ + RDS Multi‑AZ. C’est déjà un bond énorme par rapport à « une VM unique ». Ensuite, affine scaling, cache et observabilité.
