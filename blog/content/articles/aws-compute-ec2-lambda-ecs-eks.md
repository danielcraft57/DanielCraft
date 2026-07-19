---
title: "AWS : où faire tourner ton programme"
date: 2025-05-08
excerpt: "EC2, Lambda, ECS, EKS : choisir selon ta charge et ton équipe, pas la mode."
type: article
tags: [AWS, EC2, Lambda, ECS, EKS, compute, serveurs]
series: aws-serie
series_order: 2
og_image: aws-compute-ec2-lambda-ecs-eks-1200x630.jpg
---

# AWS : où faire tourner ton programme

Premiere question sur AWS : **ou je fais tourner mon appli ?**

Tu peux tout mettre sur EC2. Mais parfois une autre boite est plus simple. Si les [fondamentaux AWS](/blog/articles/aws-fondamentaux-cloud-aws-services.html) sont flous, commence la.

Ici, quatre options. Comme quatre vehicules : voiture, scooter, camion, train.

---

## EC2 : la voiture que tu conduis

**EC2**, c'est une machine virtuelle. Tu choisis l'OS, la taille (CPU, RAM), les logiciels.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/aws-compute-choix.svg" alt="Schema de choix compute AWS EC2 Lambda ECS EKS" class="schema-inline" width="640" />
  <figcaption>EC2, Lambda, ECS, EKS : le bon choix suit la charge et l'equipe.</figcaption>
</figure>

Tu es responsable de :

- la config systeme,
- les mises a jour de secu,
- le dimensionnement,
- les sauvegardes (snapshots EBS, AMI).

**Bon pour** : migrer un serveur existant, une appli difficile a mettre en conteneur, un besoin de controle fin sur l'OS.

**Cout** : a l'heure / seconde selon la taille. Pour une charge stable, regarde [Reserved / Savings Plans](/blog/articles/aws-optimisation-couts-reserved-savings-spot.html). Eteins les machines de test la nuit.

---

## Lambda : le scooter a la demande

Avec **Lambda**, tu n'achetes plus de serveur. Tu donnes un bout de code. AWS l'execute quand un evenement arrive. Tu paies au nombre d'appels + a la duree.

**Bon pour** : API legeres, webhooks, jobs planifies, traitement d'un fichier pose sur S3, trafic en dents de scie.

**Moins bon pour** : traitements tres longs, besoin de controler l'OS ou le reseau en detail.

Astuces : calibre bien la **memoire**, evite de recharger tout a chaque appel, ne fais pas une "fonction monstre" ni mille micro-fonctions inutiles.

---

## ECS : des conteneurs sans Kubernetes

**ECS** orchestre des conteneurs Docker pour toi.

- Tu definis des **taches** (conteneurs + ressources) et des **services** (redemarrage, scaling).
- Mode **EC2** : tu geres encore un cluster de machines.
- Mode **Fargate** : pas de machine a soigner. Serverless pour conteneurs.

**Bon pour** : API, microservices, workers derriere une file. Tu veux des conteneurs sans la complexite de Kubernetes.

Pense a [Docker](/blog/articles/docker-fondamentaux-images-conteneurs.html) avant : une image propre facilite beaucoup ECS.

---

## EKS : le train Kubernetes

**EKS** te donne un **plan de controle Kubernetes** manage. Tu deploies comme d'habitude (`Deployment`, `Service`...).

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/aws-compute-ops.svg" alt="Schema operations autour du compute AWS" class="schema-inline" width="640" />
  <figcaption>Le runtime choisi deplace le curseur entre ops et flexibilite.</figcaption>
</figure>

Tu restes responsable des **nodes** (ou Fargate), des versions cote workloads, de la secu et de l'obs.

**Bon pour** : equipe deja forte en Kubernetes, besoin de portabilite cloud / on-prem, plateformes complexes.

Si tu n'as pas encore de stack K8s : ECS/Fargate ou Lambda seront souvent plus simples.

---

## Grille de choix rapide

- Tu veux SSH, OS, paquets → **EC2**.
- Un peu de code a la demande, sans serveur → **Lambda**.
- Conteneurs sans Kubernetes → **ECS** (idealement Fargate).
- Ecosystème Kubernetes deja la → **EKS**.

Tu peux **combiner** : EC2 pour du legacy, ECS pour les nouveaux services, Lambda pour la colle, EKS pour la plateforme avancee.

---

## Reflexes transverses

- Decrire l'infra en code (Terraform / CloudFormation / CDK).
- Logs et metriques dans [CloudWatch](/blog/articles/aws-observabilite-cloudwatch-xray-cloudtrail.html).
- Roles [IAM](/blog/articles/iam-mfa-principes-zero-trust.html) minimal, secrets hors images ([IAM / KMS](/blog/articles/aws-securite-iam-kms-waf.html)).

---

## Resume

EC2 = serveur classique. Lambda = petit moteur a evenements. ECS = conteneurs sans K8s. EKS = K8s manage. Choisis selon la **charge** et l'**equipe**, pas selon la mode.

Ensuite : [ou mettre tes fichiers](/blog/articles/aws-stockage-s3-ebs-efs.html) avec S3, EBS et EFS.
