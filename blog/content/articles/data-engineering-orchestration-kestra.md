---
title: "Orchestration : planifier et surveiller les jobs"
date: 2026-10-03
excerpt: "Enchaîner les étapes, retenter si ça casse, être alerté - l'esprit Kestra / Airflow sans usine obscure."
type: tutorial
tags: ["orchestration", "Kestra", "Airflow", "DAG", "data engineering", "formation"]
series: data-engineering-serie
series_order: 3
og_image: data-engineering-orchestration-kestra-1200x630.jpg
---

# Orchestration : planifier et surveiller les jobs

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/data-eng-orchestration.svg" alt="Schéma orchestration" class="schema-inline" width="800" />
  <figcaption>DAG, schedule, retries, alertes.</figcaption>
</figure>

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/data-eng-orchestration-illustration.jpg" alt="Planifier, retenter, alerter." class="schema-inline" width="800" loading="lazy" />
  <figcaption>Le chef d'orchestre des jobs data.</figcaption>
</figure>

Un script lancé à la main, ça va… jusqu'au jour où tu oublies. Ou jusqu'au jour où l'API de la caisse tousse à 3 h du matin et personne ne le sait. L'orchestration enchaîne les étapes, retente si besoin, et te dit quand ça rate.

Cette série s'inspire du [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp). Ici, on parle de l'esprit Kestra / Airflow sans se noyer dans l'usine. L'outil précis compte moins que le réflexe : **planifier, ordonner, surveiller**.

## L'idée en une phrase

**Planifier → enchaîner → retenter → alerter.**

## Pourquoi orchestrer (exemple boutique)

Imagine une boutique près de Metz. Chaque matin, le gérant veut trois chiffres : commandes de la veille, panier moyen, stock bas. Sans orchestrateur, quelqu'un lance trois scripts « quand il pense à le faire ». Un jour de foire à Nancy, personne ne lance rien. Le dashboard reste sur l'ancienne semaine. Mauvaise décision, bonne foi.

Avec un orchestrateur :

1. à 5 h, on extrait les commandes ;
2. seulement si ça a marché, on transforme ;
3. seulement ensuite, on charge le tableau métier ;
4. si l'extract plante, on retente deux fois, puis on envoie un mail / un message.

Le métier se réveille avec un chiffre frais - ou une alerte claire. Pas un silence gênant.

## Ce que tu gagnes, concrètement

- un **calendrier** (chaque nuit, chaque heure, chaque lundi) ;
- un **ordre** clair (extract avant transform, transform avant mart) ;
- des **retries** si l'API tousse cinq minutes ;
- une **alerte** au lieu d'un « tiens, le graphique est bizarre depuis mardi » ;
- un **historique** des runs : qui a tourné, combien de temps, combien de lignes.

L'orchestrateur ne remplace pas tes scripts. Il les rend **fiables dans le temps**. Comme un chef de cuisine qui ne cuisine pas chaque plat, mais qui s'assure que les postes s'enchaînent.

## DAG, en français simple

Tu verras souvent le mot **DAG**. En vrai, c'est juste le **plan des étapes et de leurs dépendances**. Qui doit finir avant qui. Pas besoin du jargon pour retenir l'idée.

Exemple pour une boutique lorraine :

1. `extract_commandes`  
2. `extract_promo` (peut tourner en parallèle de 1)  
3. `join_et_nettoie` (attend 1 et 2)  
4. `charge_mart_ventes` (attend 3)

Si 1 échoue, 3 et 4 ne partent pas. C'est du bon sens. L'orchestrateur force ce bon sens, même à 4 h du matin.

## Schedule, retries, alertes (les trois leviers)

**Schedule**  
« Tous les jours à 5 h » ou « toutes les heures ». Choisis selon le besoin métier. Une boutique qui regarde les ventes une fois le matin n'a pas besoin d'un run toutes les minutes.

**Retries**  
L'API externe peut planter. Tu retentes avec un délai (ex. 2 minutes). Attention : le job doit être **safe à relancer** (on en parle dans l'article ingestion). Sinon tu doubles les commandes.

**Alertes**  
Mail, Slack, SMS… Peu importe. L'idée : quelqu'un de vivant est prévenu. Un pipeline silencieux qui échoue, c'est pire qu'un pipeline qui n'existe pas - parce que le métier croit encore au chiffre.

## Kestra, Airflow… même esprit

Dans le Zoomcamp et ailleurs, tu croiseras Airflow, Kestra, Prefect, etc. L'esprit reste le même :

- tu décris des flux ;
- tu les planifies ;
- tu regardes l'état des runs ;
- tu retentes / alertes.

Choisis selon ton équipe, ton hébergement, et ce que tu arrives à maintenir. Pour apprendre, un outil en local (souvent via Docker, article précédent) suffit. Une boutique à Épinal n'a pas besoin d'un cluster d'orchestration le premier mois. Elle a besoin que le job du matin soit honnête.

## Erreurs classiques

1. **Tout en un seul script monstre**  
   Difficile à retenter. Découpe : extract / transform / load.

2. **Retry sur un job qui double les lignes**  
   Relancer doit être sûr. Sinon le retry empire le problème.

3. **Alerter tout le monde pour tout**  
   Trop d'alertes = plus personne ne lit. Alerte sur l'échec critique. Logue le reste.

4. **Oublier le fuseau**  
   « 5 h » à Metz, c'est quelle heure côté serveur cloud ? Vérifie. Les ventes « du jour » aiment les fuseaux mal réglés.

## Comment ça se branche sur la suite

L'orchestration appelle des jobs d'**ingestion** (prochain article), puis charge un **entrepôt**, puis lance des transforms **dbt**. L'orchestrateur est le chef d'orchestre. Les musiciens, ce sont tes scripts et tes modèles SQL.

## En résumé

L'orchestrateur ne remplace pas tes scripts. Il les rend fiables dans le temps.  
Planifier, enchaîner, retenter, alerter - c'est ça le réflexe. L'outil suit.

Prochaine étape : charger les données sans tout rejouer depuis 2019 chaque nuit.

---

## Questions fréquentes (FAQ)

**Kestra ou Airflow ?**  
L'esprit est le même. Choisis selon ton équipe / ton hébergement. Pour apprendre, prends celui que tu arrives à faire tourner en local sans te battre trois jours.

**Cron Linux, ça compte ?**  
Oui pour un seul job simple. Dès que tu as des dépendances, des retries et des alertes, un vrai orchestrateur te simplifie la vie.

**Faut-il orchestrer dès le premier CSV ?**  
Pas forcément. Dès que tu dépends du résultat chaque matin, oui. Le jour où « j'oublie de lancer » devient un risque métier, tu orchestrés.

**Et si le job dure 2 heures ?**  
Découpe, mesure, regarde où ça rame. L'orchestrateur te montre la durée. Ensuite tu optimises l'ingestion ou le SQL - pas le calendrier au feeling.

**Ça sert à une petite boutique ?**  
Oui : un run nocturne fiable bat trois exports manuels « entre midi ».

---

## Navigation dans la série

- Précédent : [Docker Terraform](/blog/articles/data-engineering-docker-terraform-infra.html)
- Suivant : [Ingestion](/blog/articles/data-engineering-ingestion-api-incremental.html)
