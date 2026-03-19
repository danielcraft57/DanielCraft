---
title: "Observabilité AWS : CloudWatch, X-Ray, CloudTrail – voir ce qui se passe vraiment"
date: 2025-05-27
excerpt: "Mettre en place logs, métriques, traces et audit sur AWS avec CloudWatch, X-Ray et CloudTrail pour diagnostiquer les problèmes et piloter ton architecture."
type: article
tags: [AWS, observabilité, CloudWatch, CloudTrail, X-Ray, monitoring]
series: aws-serie
series_order: 7
og_image: aws-observabilite-cloudwatch-xray-cloudtrail-1200x630.jpg
---

# Observabilité AWS : CloudWatch, X-Ray, CloudTrail – voir ce qui se passe vraiment

Sans observabilité, une architecture cloud est un **boîte noire**.
AWS propose plusieurs briques :

- **CloudWatch** pour les métriques et les logs ;
- **X-Ray** pour les traces de requêtes ;
- **CloudTrail** pour l’audit des appels API.

---

## 1. CloudWatch : métriques, logs, alarmes

### 1.1 Métriques

CloudWatch collecte des métriques natives :

- CPU, RAM, réseau des instances EC2 ;
- métriques RDS (connexions, IOPS, latence) ;
- métriques ELB/ALB (latence, erreurs 4xx/5xx).

Tu peux aussi :

- pousser des **métriques personnalisées** (temps de réponse métier, taille de queue, etc.) ;
- créer des **dashboards** personnalisés.

### 1.2 Logs

- Les logs applicatifs (EC2, ECS, Lambda) peuvent être envoyés dans **CloudWatch Logs**.
- Tu peux y définir :
  - des **filtres de logs** ;
  - des métriques basées sur la fréquence de certains messages (erreurs, exceptions).

### 1.3 Alarmes

Tu peux créer des alarmes sur :

- des métriques de base (CPU > 80 %, mémoire saturée) ;
- des métriques issues des logs (nombre d’erreurs 500/minute).

Réactions possibles :

- notifications (SNS, email, Slack via webhook) ;
- déclenchement de Lambda pour corriger / scaler.

---

## 2. X-Ray : traces distribuées

**AWS X-Ray** permet de tracer une requête à travers plusieurs services :

- front → API Gateway → Lambda/ECS → RDS/DynamoDB → autres APIs.

Tu obtiens :

- un graphe de service (qui appelle qui) ;
- les temps de réponse par segment ;
- les erreurs et timeouts.

Usage recommandé :

- activer X-Ray sur les services critiques (APIs, microservices) ;
- échantillonner raisonnablement pour limiter les coûts ;
- utiliser ces données pour identifier les goulots d’étranglement.

---

## 3. CloudTrail : audit et traçabilité

**CloudTrail** journalise les appels API AWS :

- qui a créé/supprimé telle ressource ;
- quelle IP a modifié tel Security Group ;
- quel rôle a utilisé telle clé KMS.

Indispensable pour :

- les enquêtes de sécurité ;
- la conformité (traçabilité des actions d’admin) ;
- le debugging de certains problèmes d’infra.

Bonnes pratiques :

- activer CloudTrail au niveau de l’organisation ;
- envoyer les logs dans un bucket S3 dédié, éventuellement chiffré ;
- limiter les accès à ce bucket.

---

## 4. Mettre en place une stack d’observabilité minimale

Pour une application web/API sur AWS, une stack de base devrait inclure :

- **CloudWatch Logs** pour :
  - les logs applicatifs ;
  - les logs des lambdas ;
  - les logs des ALB / API Gateway.
- **Métriques CloudWatch** pour :
  - la charge CPU/RAM ;
  - les erreurs 4xx/5xx ;
  - la taille des queues (SQS, Kafka managé si utilisé).
- **Alarmes** pour :
  - erreurs 5xx ;
  - latence supérieure à un seuil ;
  - coût mensuel approchant un budget donné.
- **CloudTrail** activé avec stockage des logs sur S3.

---

## 5. Gouvernance et exploitation

### 5.1 Centralisation

- Regrouper les logs critiques dans quelques groupes CloudWatch bien nommés.
- Structurer les noms de métriques avec des préfixes (`app/`, `infra/`, `business/`).

### 5.2 Coûts

- Mettre en place des **politiques de rétention** : garder le détail quelques jours/semaines, agréger ou archiver au‑delà.
- Exporter les logs les plus anciens vers S3 pour archivage long terme moins cher.

### 5.3 Culture

- Intégrer les dashboards d’observabilité dans les rituels (revues hebdo, post‑mortems).
- Rendre visibles les métriques business (commandes, taux d’erreur…) au même titre que les métriques techniques.

---

## 6. Résumé

Sur AWS, une bonne observabilité repose sur :

- **CloudWatch** pour les métriques et les logs + alarmes ;
- **X-Ray** pour voir le chemin complet des requêtes complexes ;
- **CloudTrail** pour savoir qui a fait quoi sur l’infrastructure.

Cette visibilité est essentielle pour exploiter sereinement les architectures construites avec le reste de la série AWS (compute, stockage, réseau, bases, sécurité).+
