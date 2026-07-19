---
title: "AWS : où ranger tes fichiers"
date: 2025-05-13
excerpt: "S3, EBS, EFS : trois façons de stocker, trois jobs différents."
type: article
tags: [AWS, S3, EBS, EFS, stockage, performance]
series: aws-serie
series_order: 3
og_image: aws-stockage-s3-ebs-efs-1200x630.jpg
---

# [AWS](/blog/articles/aws-fondamentaux-cloud-aws-services.html) : où ranger tes fichiers

Sur AWS, on a souvent envie de "tout mettre sur le disque du serveur". Mauvaise idee. **S3, EBS et EFS** font trois jobs differents. Comme un coffre, un tiroir de bureau, et une etagere partagee.

Apres le [compute](/blog/articles/aws-compute-ec2-lambda-ecs-eks.html), on range les fichiers.

---

## S3 : le grand coffre a objets

**S3**, tu y poses des fichiers (objets) dans des **buckets** (des seaux). Chaque objet a une cle genre `dossier/fichier.ext`. Ce n'est pas un disque monte. C'est un entrepot accessible en HTTP.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/aws-stockage-choix.svg" alt="Schema choix stockage AWS S3 EBS EFS" class="schema-inline" width="640" />
  <figcaption>S3 objet, EBS block, EFS fichier : trois jobs differents.</figcaption>
</figure>

Points forts :

- tres **durable** (AWS annonce beaucoup de 9 apres la virgule),
- classes de prix (Standard, IA, Glacier...) selon la frequence d'acces,
- acces via HTTPS, SDK, CLI.

**Bon pour** : images/CSS/JS, backups, archives, fichiers data (CSV, logs).

**Astuces** : active le versioning, des Lifecycle pour envoyer le vieux vers Glacier, et [CloudFront](/blog/articles/aws-reseaux-vpc-route53-cloudfront.html) devant pour livrer plus vite.

---

## EBS : le disque de ta machine EC2

**EBS**, c'est un **volume bloc** colle a une instance EC2. Le systeme le voit comme un vrai disque. Tu y mets un systeme de fichiers (ext4, xfs...).

**Bon pour** : disque systeme (OS), donnees d'une base que tu geres toi-meme, stockage local d'une appli.

**Astuces** : choisis le type (gp3, io2...) selon IOPS et budget. Fais des **snapshots** reguliers. N'achete pas un disque geant "au cas ou".

---

## EFS : l'etagere partagee

**EFS**, c'est un **systeme de fichiers reseau** manage (NFS). Plusieurs machines (EC2, ECS) montent le meme dossier. Tu paies a l'espace utilise. Ca grandit tout seul.

**Bon pour** : applis qui ont besoin d'un vrai partage de fichiers (uploads, documents).

**A eviter pour** : le stockage chaud d'une base tres exigeante. Prefere EBS ou une base managee ([RDS](/blog/articles/aws-bases-donnees-rds-dynamodb-aurora.html)).

---

## Comment choisir ?

- Disque pour **un** serveur → **EBS**.
- Fichiers durables, accessibles en HTTP, pas cher → **S3**.
- Plusieurs serveurs partagent les **memes dossiers** → **EFS**.

Combos classiques :

- EC2 + EBS pour tourner + S3 pour assets et backups.
- ECS/EKS + EFS si besoin de partage simple + S3 pour le froid.

---

## Secu, couts, vue

- HTTPS pour S3. Roles [IAM](/blog/articles/iam-mfa-principes-zero-trust.html) minimal. Chiffrement au repos (souvent via [KMS](/blog/articles/aws-securite-iam-kms-waf.html)).
- Surveille le volume S3 par classe. Nettoie snapshots EBS orphelins. Evite les transferts geants inutiles entre regions.
- Logs d'acces critiques + metriques dans [CloudWatch](/blog/articles/aws-observabilite-cloudwatch-xray-cloudtrail.html).

---

## Resume

S3 = coffre objet. EBS = disque local. EFS = etagere partagee. Trois boites, trois usages. Ensuite : [quelle base de donnees](/blog/articles/aws-bases-donnees-rds-dynamodb-aurora.html) choisir.
