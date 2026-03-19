---
title: "AWS Compute : EC2, Lambda, ECS, EKS – quel service pour ton application ?"
date: 2025-05-08
excerpt: "Comparer EC2, Lambda, ECS et EKS : modèles de responsabilité, scénarios types, coûts et bonnes pratiques pour choisir la bonne brique compute sur AWS."
type: article
tags: [AWS, EC2, Lambda, ECS, EKS, compute, serveurs]
series: aws-serie
series_order: 2
og_image: aws-compute-ec2-lambda-ecs-eks-1200x630.jpg
---

# AWS Compute : EC2, Lambda, ECS, EKS – quel service pour ton application ?

La première question sur AWS est souvent : **“je déploie mon appli où ?”**.
Tu peux tout mettre sur EC2, mais tu passeras peut‑être à côté des avantages du serverless ou des conteneurs.

Dans cet article, on compare **EC2, Lambda, ECS et EKS** avec une grille simple :

- modèle de responsabilité ;
- cas d’usage idéaux ;
- coûts et optimisation ;
- gestion et opérations.

---

## 1. EC2 : les “vrais” serveurs dans le cloud

### 1.1 Modèle

EC2 te fournit des **instances (VM)** sur lesquelles tu choisis :

- l’OS (Amazon Linux, Ubuntu, Debian, Windows…) ;
- la taille (CPU, RAM, stockage) ;
- les logiciels installés (Nginx, Node, PHP, Docker, etc.).

Tu es responsable de :

- la configuration système ;
- les mises à jour de sécurité ;
- le dimensionnement ;
- les sauvegardes (snapshots EBS, AMI).

### 1.2 Cas d’usage

- Migration d’un **serveur existant** (lift & shift).
- Applications monolithiques difficiles à conteneuriser.
- Besoin de **contrôle fin** sur l’OS, les drivers, etc.

### 1.3 Coûts et optimisation

- Facturation **à l’heure / seconde** en fonction du type d’instance.
- Optimisations :
  - choisir la bonne famille (généraliste, optimisée CPU, RAM, stockage) ;
  - utiliser des **Reserved Instances** ou **Savings Plans** pour les charges stables ;
  - automatiser l’extinction des environnements non‑prod.

---

## 2. Lambda : le serverless à la demande

### 2.1 Modèle

Avec **AWS Lambda**, tu n’achètes plus des serveurs mais des **exécutions de fonctions**.

- Tu fournis du code (Node, Python, etc.).
- AWS s’occupe de **provisionner, scaler, patcher** l’infrastructure.
- Tu paies au **nombre d’invocations + durée d’exécution**.

### 2.2 Cas d’usage

- **APIs légères** (via API Gateway ou Function URLs).
- Automatisations (traitement de fichiers S3, jobs planifiés, webhooks).
- Backends à trafic irrégulier (pics, périodes de calme).

Ce n’est pas idéal pour :

- les traitements de longue durée (au‑delà de quelques minutes) ;
- les workloads nécessitant un contrôle précis sur l’OS ou le réseau.

### 2.3 Optimisation

- Bien calibrer la **mémoire** pour un bon ratio temps/coût.
- Éviter d’initialiser des choses lourdes à chaque appel (connexions DB, SDK…).
- Grouper du code dans des fonctions cohérentes (pas un énorme “god function”, pas mille fonctions minuscules).

---

## 3. ECS : exécuter des conteneurs sans gérer Kubernetes

### 3.1 Modèle

**ECS (Elastic Container Service)** est un orchestrateur de conteneurs géré par AWS.

- Tu définis des **tâches** (containers + ressources) et des **services** (scaling, redémarrage).
- Deux modes principaux :
  - **ECS sur EC2** : tu gères encore des instances (cluster EC2).
  - **ECS Fargate** : serverless pour conteneurs (pas d’instance à gérer).

### 3.2 Cas d’usage

- API REST / GraphQL en microservices.
- Workers asynchrones (queues SQS, Kafka).
- Backends d’applications web modernes.

ECS est un bon compromis si tu veux :

- bénéficier des conteneurs ;
- **éviter la complexité de Kubernetes** ;
- rester dans l’écosystème AWS.

### 3.3 Optimisation

- En mode EC2 : bien dimensionner le cluster (autoscaling, types d’instances).
- En mode Fargate : choisir la bonne taille CPU/RAM par tâche et ajuster l’auto‑scaling sur des métriques métier (latence, queue length).

---

## 4. EKS : Kubernetes managé

### 4.1 Modèle

**EKS (Elastic Kubernetes Service)** te fournit un **control plane Kubernetes managé**.

- Tu déploies des workloads Kubernetes “classiques” (`Deployment`, `Service`, `Ingress`…).
- Tu peux utiliser les mêmes outils qu’on‑prem (kubectl, Helm, ArgoCD, etc.).

Tu restes toutefois responsable de :

- la gestion des **nodes workers** (ou Fargate pour certaines charges) ;
- les mises à jour de versions Kubernetes côté workloads ;
- la configuration de l’observabilité et de la sécurité.

### 4.2 Cas d’usage

- Organisation qui a déjà investi dans **Kubernetes** (compétences, tooling).
- Besoin de **portabilité** entre cloud / on‑prem.
- Plateformes multi‑tenants, architectures microservices complexes.

Si tu n’as pas encore de stack Kubernetes, ECS/Fargate ou Lambda seront souvent plus simples.

---

## 5. Comment choisir entre EC2, Lambda, ECS et EKS ?

Une grille de décision rapide :

- **Tu veux gérer des serveurs** (SSH, OS, paquets)  
  → EC2.

- **Tu veux exécuter un peu de code à la demande, sans serveur**  
  → Lambda.

- **Tu veux des conteneurs mais sans Kubernetes**  
  → ECS (idéalement Fargate).

- **Tu as déjà un écosystème Kubernetes fort**  
  → EKS.

On peut aussi combiner :

- EC2 pour quelques workloads “legacy” ;
- ECS/Fargate pour les nouveaux services ;
- Lambda pour la glue / automatisations ;
- EKS pour des plateformes plus avancées.

---

## 6. Gestion et bonnes pratiques transverses

### 6.1 Infrastructure as Code

Quel que soit le service compute choisi :

- décrire l’infra avec Terraform, CloudFormation ou CDK ;
- versionner les manifestes ;
- automatiser les déploiements (CI/CD).

### 6.2 Observabilité

- Centraliser les logs dans CloudWatch Logs, avec filtres/métriques.
- Instrumenter la latence, les erreurs, le CPU/RAM, la saturation des queues.
- Mettre en place des **dashboards par service** (API, workers, batch).

### 6.3 Sécurité

- IAM minimal : un rôle par type de workload (API, worker, batch).
- Pas de secrets dans les images : utiliser Secrets Manager / SSM Parameter Store.
- Reviewer régulièrement les rôles/permissions.

---

## 7. Résumé

Pour bien exploiter AWS côté compute :

- garde EC2 pour ce qui ressemble à un **serveur classique** ;
- privilégie **Lambda** pour les petits morceaux de logique événementielle ;
- utilise **ECS/Fargate** pour les APIs et services conteneurisés ;
- choisis **EKS** seulement si tu as une vraie stratégie Kubernetes derrière.

Dans le prochain article, on va regarder comment **S3, EBS et EFS** se complètent pour le stockage de tes données (fichiers, disques, partages).+
