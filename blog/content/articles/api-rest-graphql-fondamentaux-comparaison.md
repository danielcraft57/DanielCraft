---
title: "APIs web : REST vs GraphQL, poser le décor"
date: 2025-07-01
excerpt: "Comprendre clairement ce que sont REST et GraphQL, leurs philosophies, et dans quels contextes ils brillent (ou pas) avant de rentrer dans les détails techniques."
type: article
tags: [API, REST, GraphQL, backend, architecture]
series: api-rest-graphql-serie
series_order: 1
og_image: api-rest-graphql-fondamentaux-comparaison-1200x630.jpg
---

# APIs web : REST vs GraphQL, poser le décor

Quand tu dois exposer une API, la question « REST ou GraphQL ? » arrive très vite.  
Plutôt que de partir sur une solution « à la mode », l’idée de cet article est de **poser les bases** : ce que chaque approche promet, ce qu’elle implique pour ton backend, ton frontend et tes équipes.

---

## 1. Rappels : ce qu’on attend d’une bonne API

Avant même de parler REST ou GraphQL, une API doit :

- **Être simple à consommer** : contrat clair, erreurs explicites, docs exploitables.
- **Être stable dans le temps** : compatibilité, versioning, gestion des breaking changes.
- **Être observable** : logs, métriques, traces pour comprendre ce qui se passe.
- **Être performante et prévisible** : latence, charge serveur, coûts infra.
- **Refléter ton domaine métier** : pas juste des endpoints techniques mais un langage métier partagé.

Garder ces critères en tête aidera à comparer REST et GraphQL de manière pragmatique.

---

## 2. REST en deux minutes

REST n’est pas une librairie mais un **style d’architecture** basé sur HTTP :

- Ressources identifiées par des **URLs** (`/users`, `/orders/123`).
- Utilisation des **verbes HTTP** (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).
- Sémantique des **codes HTTP** (`200`, `201`, `400`, `404`, `500`, etc.).
- Notion de **représentations** (JSON, XML, …) et de **stateless** (pas d’état serveur entre deux requêtes).

Dans la pratique, beaucoup d’APIs dites « REST » sont en réalité du **REST pragmatique** : on applique 80 % des principes, on adapte le reste en fonction du besoin et de l’outillage.

---

## 3. GraphQL en deux minutes

GraphQL est un **langage de requête pour API** inventé chez Facebook :

- On définit un **schéma typé** (types, champs, relations) côté serveur.
- Le client envoie une **requête déclarative** : il précise exactement les champs dont il a besoin.
- Une seule **endpoint HTTP** (souvent `/graphql`) reçoit toutes les requêtes.
- Le serveur exécute la requête sur les résolveurs, puis renvoie **exactement** le shape demandé.

L’objectif principal est d’**éviter la sous- et sur‑récupération de données** (under/over‑fetching), surtout dans des frontends riches (SPA, mobile) qui composent des écrans complexes.

---

## 4. Forces et faiblesses (vue très haute)

### REST – points forts

- **S’appuie sur HTTP** : caches, proxies, CDN sont faciles à exploiter.
- **Standard de fait** : outillage massif, facile à exposer à des partenaires.
- **Simple à débugger** : un `curl` ou Postman suffit, les URLs sont explicites.
- Convient très bien aux **APIs orientées ressources** (CRUD, microservices simples).

### REST – points de vigilance

- Risque d’**explosion du nombre d’endpoints** au fil du temps.
- **Sur‑récupération** fréquente (tu récupères plus de données que nécessaire).
- Peut nécessiter beaucoup de **round‑trips** côté frontend pour construire un écran complexe.

### GraphQL – points forts

- **Un seul endpoint** et une requête qui décrit précisément les données voulues.
- **Évolution du schéma** souvent plus fluide (dépréciation champ par champ).
- Excellent pour des **frontends riches/mobiles** qui composent des écrans complexes.

### GraphQL – points de vigilance

- **Courbe d’apprentissage** : schéma, résolveurs, tooling dédié.
- Plus complexe à **mettre en cache** côté CDN (on y reviendra).
- Risque de **requêtes très coûteuses** si le schéma n’est pas bien pensé (N+1, profondeur, etc.).

---

## 5. Cas d’usage typiques

- **REST** brille pour :
  - APIs publiques simples (paiement, SMS, notifications, etc.).
  - Microservices orientés ressources (catalogue produits, commandes, etc.).
  - Intégrations B2B où les partenaires attendent du REST/HTTP classique.

- **GraphQL** brille pour :
  - Applications **front riches** (web/mobile) avec beaucoup d’écrans composés.
  - **Backend For Frontend (BFF)** : adapter des microservices internes à des besoins UI.
  - Exposer un **graphe métier** complexe (relations nombreuses, filtrages variés).

---

## 6. Ce que la série va couvrir

Dans les prochains articles, on va :

1. Entrer dans le détail des **APIs REST modernes** : design, versioning, pagination, erreurs, sécurité.
2. Explorer **GraphQL côté serveur et côté client** : schéma, résolveurs, tooling, anti‑patterns.
3. Comparer **performances, coûts et complexité opérationnelle** dans différents scénarios.
4. Proposer un **guide de choix concret** : quand REST est un no‑brainer, quand GraphQL fait réellement la différence, et comment mixer les deux intelligemment.

L’objectif n’est pas de désigner un « gagnant », mais de te donner une **grille de lecture claire** pour ton contexte.

