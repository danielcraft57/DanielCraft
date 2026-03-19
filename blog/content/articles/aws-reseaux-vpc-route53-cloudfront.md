---
title: "Réseau AWS : VPC, Route 53, CloudFront – bâtir des fondations propres"
date: 2025-05-20
excerpt: "Construire un réseau AWS propre avec VPC, subnets, security groups, Route 53 et CloudFront : patterns d’architecture, sécurité et performance pour exposer tes applications."
type: article
tags: [AWS, VPC, Route 53, CloudFront, réseau, sécurité]
series: aws-serie
series_order: 5
og_image: aws-reseaux-vpc-route53-cloudfront-1200x630.jpg
---

# Réseau AWS : VPC, Route 53, CloudFront – bâtir des fondations propres

Une bonne partie de la fiabilité et de la sécurité de ton application AWS dépend de **ta couche réseau**.
Dans cet article, on structure les briques :

- **VPC** (réseau virtuel, subnets, routage) ;
- **Security Groups / NACLs** ;
- **Route 53** (DNS) ;
- **CloudFront** (CDN).

---

## 1. VPC : ton “datacenter virtuel”

### 1.1 Modèle

Un **VPC (Virtual Private Cloud)** est un réseau logique isolé dans AWS :

- tu choisis une plage IP (ex : `10.0.0.0/16`) ;
- tu crées des **subnets** (sous‑réseaux) publics/privés ;
- tu définis des **tables de routage** (vers Internet, vers d’autres VPC, vers on‑prem…).

### 1.2 Organisation classique

- Subnets **publics** :
  - contiennent les load balancers (ALB/NLB) ;
  - accès Internet direct via une Internet Gateway.

- Subnets **privés** :
  - contiennent les instances applicatives (EC2/ECS/EKS) et bases de données ;
  - l’accès Internet sortant se fait via un NAT Gateway (ou pas du tout).

Objectif : **aucune base de données ou backend critique n’est directement exposé à Internet**.

---

## 2. Security Groups et NACLs : les garde‑fous

### 2.1 Security Groups

Les **Security Groups** sont des **pare‑feu stateful** appliqués aux ressources (EC2, RDS, ALB, etc.) :

- ils définissent des règles entrantes et sortantes (ports, IP, autres SG) ;
- le trafic autorisé en entrée est automatiquement autorisé en sortie.

Pratiques recommandées :

- un SG par rôle (ALB, backend API, base de données…) ;
- utiliser des **références de SG** plutôt que des IP (ex : le SG du RDS autorise le SG de l’API).

### 2.2 NACLs

Les **Network ACLs** sont des listes de contrôle au niveau subnet, **stateless**.
Dans beaucoup de projets, on les laisse proches de la configuration par défaut (allow all) et on concentre la logique dans les Security Groups.

---

## 3. Route 53 : DNS managé

**Route 53** est le service DNS d’AWS.

- tu y gères la **zone DNS** de ton domaine (`ton-domaine.fr`) ;
- tu crées des enregistrements (`A`, `AAAA`, `CNAME`, `TXT`, etc.) ;
- tu peux utiliser des **alias** vers des ressources AWS (ALB, CloudFront, S3 static website).

Cas d’usage typiques :

- `www.ton-domaine.fr` qui pointe vers un **CloudFront** ou un ALB ;
- sous‑domaines pour des services spécifiques (`api.`, `admin.`, `static.`).

---

## 4. CloudFront : CDN et couche de protection

**CloudFront** est le CDN d’AWS :

- il met en cache ton contenu dans des **edge locations** proches des utilisateurs ;
- il agit comme **reverse proxy** devant S3, ALB, API Gateway, etc.

Avantages :

- latence réduite ;
- capacité à absorber les pics de trafic ;
- intégration avec WAF pour filtrer certaines attaques.

---

## 5. Exemple d’architecture réseau pour une appli web

Un pattern courant pour une application web :

1. **Utilisateur** → `https://app.ton-domaine.fr` (Route 53).
2. Route 53 pointe vers une **distribution CloudFront**.
3. CloudFront renvoie :
   - les **assets statiques** depuis S3 ;
   - le trafic dynamique vers un **ALB** en back‑origin.
4. L’ALB se trouve dans des **subnets publics** du VPC.
5. Les **instances ECS/EC2/EKS** sont dans des **subnets privés**, derrière l’ALB.
6. Les **bases de données RDS/Aurora** sont dans des subnets privés dédiés, sans accès Internet direct.

Cette architecture permet :

- d’exposer uniquement le strict nécessaire ;
- de séparer clairement les couches (edge, web, data).

---

## 6. Gestion, optimisation et sécurité

### 6.1 Gestion

- Documenter ton adressage IP, la séparation des subnets et les routes.
- Utiliser Terraform/CloudFormation/CDK pour décrire VPC, subnets, SG, Route 53.
- Éviter d’empiler les ressources “à la main” dans la console.

### 6.2 Performance

- Toujours passer les assets statiques par CloudFront.
- Activer la compression (Gzip/Brotli) au niveau serveur web.
- Éviter les allers‑retours inter‑régions (garder l’architecture dans une région sauf besoin spécifique).

### 6.3 Sécurité

- Bloquer tous les ports non nécessaires (seulement 80/443 sur l’ALB, 22 uniquement via bastion/VPN si indispensable).
- Forcer HTTPS partout (certificats ACM sur CloudFront/ALB).
- Désactiver toute exposition publique inutile des bases de données ou services internes.

---

## 7. Résumé

Construire un réseau AWS propre, c’est :

- **penser VPC** (subnets publics/privés bien séparés) ;
- utiliser des **Security Groups bien nommés** pour contrôler finement les flux ;
- confier le DNS à **Route 53** et le CDN à **CloudFront** pour la performance globale.

Avec ces fondations en place, les autres briques (compute, bases, file storage) s’imbriquent proprement et restent gérables à long terme.+
