---
title: "Optimisation des coûts AWS : Reserved, Savings Plans, Spot et bonnes pratiques"
date: 2025-06-03
excerpt: "Réduire la facture AWS sans casser la prod : comprendre Reserved Instances, Savings Plans, instances Spot et mettre en place une gouvernance coûts efficace."
type: article
tags: [AWS, coûts, optimisation, Reserved Instances, Savings Plans, Spot]
series: aws-serie
series_order: 9
og_image: aws-optimisation-couts-reserved-savings-spot-1200x630.jpg
---

# Optimisation des coûts AWS : Reserved, Savings Plans, Spot et bonnes pratiques

La flexibilité d’AWS a un prix : sans gouvernance, la facture peut exploser.
L’objectif de cet article : donner une **boîte à outils concrète** pour garder le contrôle.

---

## 1. Comprendre la structure de coûts

Postes principaux :

- compute (EC2, Fargate, Lambda) ;
- bases de données (RDS, DynamoDB, Aurora) ;
- stockage (S3, EBS, EFS) ;
- réseau (sortie Internet, inter‑AZ, inter‑région) ;
- services managés (CloudFront, API Gateway, etc.).

Première étape : **savoir où part l’argent** via Cost Explorer et les rapports de coûts (CUR).

---

## 2. Reserved Instances et Savings Plans

### 2.1 Reserved Instances (RI)

- Engagement sur une **famille d’instances** (ex : m6g.large) pour 1 ou 3 ans.
- Réduction importante sur le prix horaire (jusqu’à ~70 %).
- Moins flexibles, plutôt pour des charges stables très prévisibles.

### 2.2 Savings Plans

- Engagement sur un **montant de dépense horaire** (ex : 10 $/h) pour 1 ou 3 ans.
- Plus flexibles que les RI : peuvent s’appliquer à plusieurs types d’instances/services.
- Deux grandes familles :
  - Compute Savings Plans (plus flexibles) ;
  - EC2 Instance Savings Plans (plus ciblés).

Stratégie classique :

- commencer avec des Savings Plans pour couvrir un socle de charge stable ;
- envisager des RI pour des cas spécifiques si besoin.

---

## 3. Instances Spot

Les **instances Spot** te permettent d’utiliser la capacité EC2 inutilisée à prix cassé, avec une contrainte :

- AWS peut **reprendre l’instance à tout moment** avec un préavis court.

Utilisation typique :

- jobs batch ;
- traitements parallélisables et tolérants à l’interruption ;
- environnements éphémères (tests de charge, CI/CD).

On évite les Spot pour :

- les bases de données ;
- les composants critiques en temps réel non tolérants à l’interruption.

---

## 4. Bonnes pratiques générales d’optimisation

### 4.1 Droitsizing

- Mesurer l’utilisation CPU/RAM des instances et réduire les tailles sur‑dimensionnées.
- Utiliser les rapports de recommendation AWS (Compute Optimizer).

### 4.2 Environnements non‑prod

- Éteindre automatiquement les environnements de **dev/test** la nuit et le week‑end.
- Utiliser des gabarits plus petits pour ces environnements.

### 4.3 Nettoyage régulier

- Supprimer :
  - les volumes EBS orphelins ;
  - les snapshots inutiles ;
  - les Elastic IP non utilisées ;
  - les buckets S3 de tests devenus obsolètes.

---

## 5. Gouvernance et outillage

### 5.1 Tagging systématique

- Tagger toutes les ressources avec au moins :
  - `env` (dev, staging, prod) ;
  - `project` (nom d’application) ;
  - `owner` (équipe/référent).

Permet :

- d’identifier qui consomme quoi ;
- de ré‑allouer les coûts aux bons projets/équipes.

### 5.2 Budgets et alertes

- Configurer des **budgets** AWS par compte, par projet ou par environnement.
- Recevoir des alertes email/Slack quand :
  - la dépense mensuelle dépasse un seuil ;
  - le rythme de dépense est anormal (pic soudain).

### 5.3 Rapports réguliers

- Faire une **revue coûts mensuelle** :
  - top des services par coût ;
  - évolution par rapport aux mois précédents ;
  - décisions (droitsizing, arrêt de ressources, engagement Savings Plans).

---

## 6. Résumé

Optimiser les coûts AWS n’est pas un “one shot” mais un **processus continu** :

- mesurer (Cost Explorer, tagging, rapports) ;
- agir (droitsizing, éteindre, nettoyer, engager des Savings Plans / RI) ;
- surveiller (budgets, alertes, revues régulières).

Avec ces réflexes, tu peux profiter de la puissance d’AWS **sans te faire surprendre par la facture**.+
