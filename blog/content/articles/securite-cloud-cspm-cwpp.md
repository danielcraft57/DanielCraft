---
title: "Sécurité cloud : les mauvais réglages qui coûtent cher"
date: 2025-11-27
excerpt: "Le cloud n'est pas magique : erreurs de config, partage des responsabilités, et outils pour vérifier."
type: article
tags: [cloud, CSPM, CWPP, sécurité, DevSecOps]
series: cybersecurite-secops-serie
series_order: 8
og_image: securite-cloud-cspm-cwpp-1200x630.jpg
---

# Sécurité cloud : les mauvais réglages qui coûtent cher

Le cloud ne te rend pas "automatiquement" plus securise. Il te rend plus **rapide**. Et la rapidite, sans garde-fous, ca veut dire plus d'erreurs de config en prod avant meme que quelqu'un ait le temps de les voir.

Bucket public "pour un test". Role trop large "le temps de debugger". Cle API dans un repo "on la retirera apres". Spoiler : apres n'arrive jamais.

La bonne nouvelle, c'est que les controles cloud les plus efficaces sont souvent des controles de **configuration**. Moins glamour qu'un firewall magique. Bien plus rentable.

## Responsabilite partagee : ne pas se tromper de niveau

Le fournisseur ([AWS](/blog/articles/aws-fondamentaux-cloud-aws-services.html), Azure, GCP) securise le datacenter, l'hyperviseur, et une partie des services geres. **Toi**, tu securises les identites, les cles, les secrets, les donnees, la config reseau, les workloads (VM, [conteneurs](/blog/articles/docker-fondamentaux-images-conteneurs.html), fonctions), et les logs.

Confondre les deux, c'est le debut des mauvaises surprises.

"C'est chez AWS, donc c'est securise" est une phrase dangereuse. AWS securise *leur* couche. Ton bucket public, c'est *ton* probleme. Ton role "tout sur tout", aussi. Le modele de responsabilite partagee n'est pas un detail juridique - c'est la carte de ce que tu dois vraiment controler.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cloud-cspm-cwpp.svg" alt="Schéma CSPM vs CWPP : posture de configuration cloud et protection des workloads" class="schema-inline" width="640" />
  <figcaption>CSPM regarde la posture (config, conformité). CWPP protège les charges de travail (VM, conteneurs, runtime).</figcaption>
</figure>

Meme sur un service "manage" (base de donnees gerée, App Service), tu restes responsable des acces, du chiffrement, des backups, et souvent du reseau. Le manage enleve de l'ops, pas de la responsabilite securite.

## CSPM vs CWPP, sans jargon inutile

Le **CSPM** (Cloud Security Posture Management), c'est le radar de config. Il detecte les mauvaises configs et mesure la posture : stockage public, groupe de securite ouvert a tout Internet, **double authentification** absente sur les comptes root, logging desactive, chiffrement non active. En gros : "est-ce que mon cloud est configure comme un pro ou comme un labo etudiant ?"

Le **CWPP** (Cloud Workload Protection Platform), c'est la protection de ce qui **tourne** : VM, conteneurs, parfois serverless. Failles sur les images, malware, comportements suspects a l'execution. En gros : "ce qui tourne est-il sain, et se comporte-t-il normalement ?"

Beaucoup d'outils modernes melangent les deux sous une meme interface. Peu importe le logo. Ce qui compte, c'est de couvrir **config** *et* **runtime**. Un CSPM sans protection workload, tu vois les portes ouvertes mais pas forcement ce qui rentre. Un CWPP sans posture, tu surveilles des machines mal nees.

## Les erreurs cloud qui reviennent tout le temps

- **IAM** trop permissif : admin partout, wildcards, comptes partages (voir [IAM / Zero Trust](/blog/articles/iam-mfa-principes-zero-trust.html))
- **Stockage public** involontaire : [S3](/blog/articles/aws-stockage-s3-ebs-efs.html), blobs Azure, buckets GCS ouverts "pour un POC"
- **Secrets** dans le code ou dans les variables CI en clair
- Sorties reseau non controlees : exfiltration facile une fois a l'interieur
- **Logs** d'audit desactives ou non centralises : pas de preuves le jour J
- Snapshots / images anciennes avec des [vulnerabilites](/blog/articles/gestion-vulnerabilites-cve-patching.html) connues qui tournent encore

Ce n'est pas theorique. Une grosse part des incidents cloud publics des dernieres annees, c'est de la config, pas un zero-day mysterieux. Si tu n'as qu'une heure par mois pour la secu cloud, passe-la sur IAM et stockage - pas sur un dashboard joli.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cloud-shared-responsibility.svg" alt="Schema du modele de responsabilite partagee cloud" class="schema-inline" width="640" />
  <figcaption>Le cloud n'efface pas ta part : identites, config, donnees.</figcaption>
</figure>

Autre classique : le compte "sandbox" qui devient prod sans personne ne le dire. Pas de tags, pas d'alertes budget, pas de politiques d'org. Six mois plus tard, tu decouvres un bucket public dans une region que tu n'utilises "pas". Inventaire et tagging, ce n'est pas de la cosmetique - c'est la base pour savoir ce que tu proteges.

## La posture "80/20" qui tient debout

- Double authentification partout, roles au **minimum**, revues d'acces
- Logs d'audit actives et envoyes quelque part ou tu les vois vraiment
- Chiffrement par defaut au repos et en transit
- Policies qui **bloquent** le stockage public
- Segmentation reseau : pas un reseau plat ou tout le monde voit tout
- Secrets dans un coffre (Secrets Manager, Key Vault…), pas dans Git
- Scan des images et des dependances avant deploy ([DevSecOps](/blog/articles/devsecops-sast-dast-sbom.html))

Tu n'as pas besoin de tout automatiser le jour 1. Commence par les **garde-fous** organisationnels : "personne ne peut creer un bucket public", "personne ne peut desactiver les logs d'audit", "compte root protege". Ensuite tu peaufines compte par compte.

Pour une TPE sur un seul compte cloud : active les logs, double auth, bloque le public storage, range les cles. Pour un SaaS multi-comptes : ajoute organisation multi-comptes, CSPM multi-account, et des alertes sur les derives de config.

## Detection cloud utile (signaux qui comptent)

Cote [SOC](/blog/articles/secops-soc-fonctions-process.html) ou "petit SOC", quelques alertes cloud valent mieux qu'un tsunami :

- Creation de cle d'acces / cle API
- Desactivation ou modification des logs d'audit
- Changement IAM admin / permission large
- Bucket rendu public
- Login "impossible" geographiquement sur la console
- Spike de sortie reseau inhabituel
- Lancement d'instances dans une region que tu n'utilises jamais

Correle avec l'IAM et l'[EDR](/blog/articles/edr-xdr-endpoint-detection-response.html) quand tu peux. Une cle creee a 3h, suivie d'une sortie vers un reseau inconnu, ca n'attend pas le lundi matin. Et si tu externalises la detection, garde quand meme un proprietaire interne qui sait isoler un compte ou une cle.

## Demarrer cette semaine

1. Liste tes comptes cloud et active les **logs d'audit** manquants
2. Cherche les ressources **publiques** (stockage, load balancers, groupes ouverts) - coupe ou justifie
3. Active la **double authentification** sur tous les humains qui touchent la console
4. Si tu as un outil CSPM (meme le gratuit du cloud provider), branche-le et traite d'abord les findings "high" lies a IAM et exposition publique

Dans le cloud, la securite se gagne par des politiques (garde-fous), un IAM solide, et des logs + detection. Le reste vient apres.
