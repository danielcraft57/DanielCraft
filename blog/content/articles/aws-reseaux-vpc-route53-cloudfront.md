---
title: "AWS : routes, adresses et accélération web"
date: 2025-05-20
excerpt: "VPC, Route 53, CloudFront : du chemin réseau clair, du DNS au serveur."
type: article
tags: [AWS, VPC, Route 53, CloudFront, réseau, sécurité]
series: aws-serie
series_order: 5
og_image: aws-reseaux-vpc-route53-cloudfront-1200x630.jpg
---

# AWS : routes, adresses et accélération web

Beaucoup de la fiabilite et de la secu de ton appli AWS depend du **reseau**. C'est comme le plan de ta maison : portes, pieces privees, boite aux lettres.

On pose quatre briques : **VPC**, **Security Groups**, **Route 53**, **CloudFront**. Les [fondamentaux](/blog/articles/aws-fondamentaux-cloud-aws-services.html) aident a situer le rayon.

---

## VPC : ton quartier prive

Un **VPC**, c'est un reseau logique isole. Tu choisis une plage IP (ex. `10.0.0.0/16`). Tu crees des **subnets** (sous-quartiers) publics / prives. Tu definis ou vont les routes (Internet, autre VPC...).

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/aws-vpc-edge.svg" alt="Schema reseau AWS VPC Route53 CloudFront" class="schema-inline" width="640" />
  <figcaption>Du DNS a la subnet privee : un chemin reseau lisible.</figcaption>
</figure>

Organisation classique :

- Subnets **publics** : load balancers (ALB). Acces Internet via Internet Gateway.
- Subnets **prives** : applis ([EC2/ECS/EKS](/blog/articles/aws-compute-ec2-lambda-ecs-eks.html)) et [bases](/blog/articles/aws-bases-donnees-rds-dynamodb-aurora.html). Sortie Internet via NAT (ou pas du tout).

Objectif : **aucune base critique directement ouverte sur Internet**.

---

## Security Groups : les portes

Les **Security Groups**, c'est un pare-feu colle a chaque ressource. Tu dis qui entre / sort (ports, IP, autres SG).

Bons reflexes :

- un SG par role (ALB, API, base...),
- autorise le SG de l'API vers le SG de la base - pas une IP en dur.

Les **NACLs** (au niveau subnet) existent aussi. Dans beaucoup de projets, on les laisse simples et on concentre la logique dans les Security Groups.

---

## Route 53 : le carnet d'adresses

**Route 53**, c'est le DNS manage. Tu geres la zone de ton domaine. Tu crees des enregistrements (`A`, `CNAME`, `TXT`...). Tu peux pointer en **alias** vers CloudFront, ALB, S3...

Exemples : `www.` vers CloudFront, `api.` vers l'ALB.

---

## CloudFront : le camion de livraison proche

**CloudFront**, c'est le CDN. Il met en cache ton contenu dans des points proches des utilisateurs. Il sert aussi de reverse proxy devant S3, ALB, API Gateway.

Avantages : latence plus basse, pics mieux absorbes, duo possible avec [WAF](/blog/articles/aws-securite-iam-kms-waf.html).

---

## Exemple d'appli web

1. Utilisateur → `https://app.ton-domaine.fr` (Route 53).
2. Route 53 pointe vers **CloudFront**.
3. CloudFront : assets depuis [S3](/blog/articles/aws-stockage-s3-ebs-efs.html), dynamique vers un **ALB**.
4. ALB dans des subnets **publics**.
5. [Conteneurs](/blog/articles/docker-fondamentaux-images-conteneurs.html) / instances dans des subnets **prives**.
6. RDS/Aurora dans des subnets prives dedies, sans Internet direct.

Tu n'exposes que le strict necessaire. Les couches restent claires : edge, web, data.

---

## Gestion et secu

- Decris VPC, subnets, SG en code (Terraform...). Evite le bricolage console.
- Assets statiques via CloudFront. Force HTTPS (certificats ACM).
- Bloque les ports inutiles. Pas de base ouverte au monde.

Pour tenir la charge et les pannes : [haute dispo et scalabilite](/blog/articles/aws-architectures-ha-scalabilite.html).

---

## Resume

VPC = quartier. Security Groups = portes. Route 53 = carnet d'adresses. CloudFront = livraison proche. Avec ca, compute, stock et bases s'emboitent sans chaos.
