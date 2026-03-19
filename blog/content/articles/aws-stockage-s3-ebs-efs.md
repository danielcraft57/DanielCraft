---
title: "Stockage AWS : S3, EBS, EFS – où mettre tes données ?"
date: 2025-05-13
excerpt: "Comparer S3, EBS et EFS : modèles de stockage, performances, coûts et scénarios types (assets web, bases de données, partage de fichiers) pour choisir le bon service AWS."
type: article
tags: [AWS, S3, EBS, EFS, stockage, performance]
series: aws-serie
series_order: 3
og_image: aws-stockage-s3-ebs-efs-1200x630.jpg
---

# Stockage AWS : S3, EBS, EFS – où mettre tes données ?

Sur AWS, on a souvent tendance à “tout mettre sur le disque du serveur”.
En réalité, **S3, EBS et EFS** servent des besoins très différents.

Dans cet article, on clarifie :

- ce que chaque service sait faire ;
- les cas d’usage idéaux ;
- les méthodes d’optimisation (coûts, perf, durabilité).

---

## 1. S3 : le coffre‑fort objet

### 1.1 Modèle

**Amazon S3** est un système de **stockage d’objets** :

- tu stockes des fichiers (objets) dans des buckets ;
- chaque objet a une clé (`dossier/fichier.ext`) ;
- pas de notion de “disque” ou de “système de fichiers monté” par défaut.

Caractéristiques clés :

- Durabilité annoncée de **11 9** (`99.999999999%`) ;
- classes de stockage pour optimiser les coûts (Standard, IA, Glacier…) ;
- accès via HTTP(S), SDKs, CLI.

### 1.2 Cas d’usage

- Assets statiques web (images, CSS/JS minifiés, vidéos).
- Backups, exports, archives.
- Fichiers de données (CSV, Parquet, logs) pour analytics.

### 1.3 Optimisation

- Activer **versioning** pour la sécurité, **Lifecycle** pour envoyer au Glacier ce qui vieillit.
- Utiliser les classes IA/Glacier pour les données peu accédées.
- Combiner avec **CloudFront** pour réduire la latence et les coûts de sortie.

---

## 2. EBS : le disque de ton serveur EC2

### 2.1 Modèle

**EBS (Elastic Block Store)**, c’est un **volume bloc** attaché à une instance EC2.

- Le système le voit comme un **disque** (`/dev/xvdf` par exemple).
- Tu y mets un système de fichiers (ext4, xfs…).
- Il est stocké de façon redondante dans une AZ.

### 2.2 Cas d’usage

- Disque système de l’instance (OS, binaires).
- Données applicatives nécessitant un accès bloc (bases de données auto‑gérées, caches, storage d’app métier).

### 2.3 Optimisation

- Choisir le bon type de volume (gp3, io1/io2, st1, sc1) selon :
  - IOPS nécessaires ;
  - throughput ;
  - budget.
- Mettre en place des **snapshots réguliers** pour la sauvegarde/restauration.
- Éviter les sur‑dimensionnements permanents ; augmenter au besoin.

---

## 3. EFS : le partage de fichiers managé

### 3.1 Modèle

**EFS (Elastic File System)** fournit un **système de fichiers réseau managé** (NFS) :

- plusieurs instances (EC2, ECS) peuvent monter le même système de fichiers ;
- tu payes à l’espace utilisé, la capacité s’ajuste automatiquement.

### 3.2 Cas d’usage

- Applis legacy qui nécessitent un **partage de fichiers** (uploads, documents).
- Environnements où plusieurs serveurs doivent lire/écrire dans les mêmes dossiers.

À éviter pour :

- le stockage “chaud” d’une base de données très exigeante (préférer EBS ou services managés type RDS).

### 3.3 Optimisation

- Choisir le bon mode de performance (General Purpose vs Max I/O).
- Utiliser les **politiques de lifecycle** pour déplacer les fichiers froids vers des classes moins chères.

---

## 4. Comment choisir entre S3, EBS et EFS ?

Une checklist rapide :

- **Tu as besoin d’un disque pour un serveur** → EBS.
- **Tu veux stocker des fichiers accessibles via HTTP, de façon durable et bon marché** → S3.
- **Plusieurs serveurs doivent partager un système de fichiers commun** → EFS.

Combinaisons typiques :

- EC2 avec EBS pour le runtime + S3 pour les assets et backups.
- ECS/EKS avec :
  - EFS pour des besoins de partage simple ;
  - S3 pour les données applicatives plus “froides”.

---

## 5. Gestion et bonnes pratiques

### 5.1 Sécurité

- Toujours utiliser **HTTPS** pour accéder à S3.
- IAM minimal : un rôle applicatif qui ne peut lire/écrire que dans le bucket nécessaire.
- Activer le chiffrement au repos (S3, EBS, EFS proposent des options simples).

### 5.2 Coûts

- Surveiller les coûts S3 par bucket / classe de stockage.
- Nettoyer les snapshots EBS orphelins.
- Éviter les architectures qui transfèrent en permanence des volumes énormes entre AZ/régions.

### 5.3 Observabilité

- Activer **S3 Access Logs** ou CloudTrail pour les accès critiques.
- Surveiller :
  - le volume stocké ;
  - le nombre de requêtes ;
  - la latence sur les usages sensibles.

---

## 6. Résumé

Tu peux voir ces trois briques comme complémentaires :

- S3 pour le **stockage objet durable** (fichiers, backups, data analytics).
- EBS pour le **disque local performant** d’une instance.
- EFS pour le **partage de fichiers** entre serveurs.

Dans les prochains articles de la série, on va appliquer la même logique de comparaison aux **bases de données** (RDS, DynamoDB, Aurora) puis au **réseau** (VPC, Route 53, CloudFront) pour que ton architecture AWS soit cohérente de bout en bout.+
