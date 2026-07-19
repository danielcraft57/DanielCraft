---
title: "AWS : où garder tes données"
date: 2025-05-15
excerpt: "RDS, Aurora, DynamoDB : choisir selon comment tu lis et écris vraiment."
type: article
tags: [AWS, RDS, DynamoDB, Aurora, bases de données]
series: aws-serie
series_order: 4
og_image: aws-bases-donnees-rds-dynamodb-aurora-1200x630.jpg
---

# [AWS](/blog/articles/aws-fondamentaux-cloud-aws-services.html) : où garder tes données

Une architecture AWS solide repose sur une **bonne base**. AWS en propose plein. Ici, les trois piliers pour le web et le SaaS : **RDS**, **DynamoDB**, **Aurora**.

Tu as vu le [stockage fichiers](/blog/articles/aws-stockage-s3-ebs-efs.html) ? Les bases, c'est un autre rayon.

---

## RDS : la base relationnelle "on s'occupe du moteur"

**RDS**, c'est une base SQL managee. PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, Aurora...

AWS gere : backups, petites mises a jour, haute dispo [Multi-AZ](/blog/articles/aws-architectures-ha-scalabilite.html) si tu l'actives.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/aws-databases-choix.svg" alt="Schema choix bases de donnees AWS RDS Aurora DynamoDB" class="schema-inline" width="640" />
  <figcaption>Relationnel ou Dynamo : le modele d'acces decide, pas la mode.</figcaption>
</figure>

Tu gardes la main sur : schema, index, requetes, taille de l'instance.

**Bon pour** : API classiques, SaaS, e-commerce, tout ce qui aime le SQL et les jointures.

**Astuces** : Multi-AZ pour le critique. Surveille CPU, IOPS, connexions, lenteur des requetes. Indexe ce que tu filtres vraiment.

---

## DynamoDB : le casier ultra rapide

**DynamoDB**, c'est une base NoSQL cle/valeur (et document). Pas de serveur a soigner. Mode on-demand = tu paies a l'usage. Latences tres basses, meme en gros volume.

Modele : cle de partition (+ cle de tri optionnelle), index secondaires pour d'autres chemins de lecture.

**Bon pour** : fort trafic avec acces simples et previsibles - sessions, paniers, events, IoT.

**Astuces** : dessine le schema **a partir des requetes** (pas "on verra apres"). Evite les hot partitions (une cle trop chaude). Commence en on-demand, passe en provisioned si la charge est stable.

---

## Aurora : le relationnel turbo cloud

**Aurora**, c'est du MySQL/PostgreSQL **reconstruit pour le cloud**. Stockage separe du calcul. Replication auto sur plusieurs AZ. Restauration a un point dans le temps.

**Bon pour** : SaaS a fort trafic qui depasse un RDS classique, besoin de haute dispo et de lectures en parallele.

**Astuces** : replicas en lecture pour le reporting. Aurora Serverless v2 si la charge varie beaucoup.

---

## Comment choisir ?

- Appli web classique, SQL, relations → commence par **RDS (PostgreSQL)**.
- Patterns simples, scale extreme → regarde **DynamoDB**.
- Relationnel qui souffre, besoin d'un cran au-dessus → **Aurora**.

Combos frequents : RDS pour le coeur metier + DynamoDB pour events/cache. Aurora pour le critique + [S3](/blog/articles/aws-stockage-s3-ebs-efs.html) pour l'archive longue.

---

## Secu, backups, facture

- Reseau ferme ([VPC](/blog/articles/aws-reseaux-vpc-route53-cloudfront.html), security groups). Pas d'acces public direct si possible.
- [IAM](/blog/articles/iam-mfa-principes-zero-trust.html) minimal. Chiffrement au repos ([KMS](/blog/articles/aws-securite-iam-kms-waf.html)).
- **Teste** une restauration. Une sauvegarde jamais restauree, c'est une histoire.
- Nettoie les bases de demo. Adapte la taille a l'usage reel.

---

## Resume

Par defaut, pense **relationnel (RDS/Aurora)**. Passe a DynamoDB quand tu as un vrai besoin NoSQL scalable. Le modele d'acces decide - pas la mode. Ensuite : le [reseau](/blog/articles/aws-reseaux-vpc-route53-cloudfront.html) pour brancher tout ca proprement.
