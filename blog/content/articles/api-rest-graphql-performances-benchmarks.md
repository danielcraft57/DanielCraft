---
title: "REST vs GraphQL : performances, coûts et benchmarks"
date: 2025-07-10
excerpt: "Comparer REST et GraphQL sur ce qui compte en prod : latence, nombre de requêtes, charge serveur, cache, coûts cloud et complexité opérationnelle."
type: article
tags: [API, REST, GraphQL, performance, benchmark]
series: api-rest-graphql-serie
series_order: 4
og_image: api-rest-graphql-performances-benchmarks-1200x630.jpg
---

# REST vs GraphQL : performances, coûts et benchmarks

Dire « GraphQL est plus rapide que REST » ou l’inverse n’a pas beaucoup de sens hors contexte.  
Ce qui t’intéresse vraiment : **combien de requêtes partent vers le backend / la base de données, quelle est la latence perçue côté utilisateur, et combien ça te coûte en infra et en complexité.**

---

## 1. Scénario 1 : écran simple, peu de données

Exemple : page « profil utilisateur » qui affiche les infos de base.

- **REST** :
  - `GET /users/me` → JSON avec les infos de base.
  - Facile à mettre en cache HTTP/CDN (ETag, `Cache-Control`, etc.).
  - Très simple à observer, logs lisibles.
- **GraphQL** :
  - Query `me { id email name }`.
  - Une requête HTTP vers `/graphql`, puis résolveur unique vers la base.

Dans ce cas, **aucune différence majeure** : bien fait, REST comme GraphQL sont rapides et peu coûteux.  
REST garde un léger avantage sur la **simplicité de cache côté CDN**.

---

## 2. Scénario 2 : écran composite (dashboard)

Exemple : dashboard qui affiche l’utilisateur, ses dernières commandes, des agrégats, etc.

- **REST naïf** :
  - 4–6 requêtes (`/me`, `/orders?limit=5`, `/notifications`, `/stats`…).
  - Risque de **waterfall** côté frontend si on séquence mal.
- **REST optimisé** :
  - Endpoint agrégé dédié `GET /dashboards/home` qui compose côté backend.
  - Performant, mais **spécifique à un écran** → risque de prolifération d’endpoints.
- **GraphQL** :

```graphql
query Dashboard {
  me { id email }
  recentOrders(limit: 5) { id total status }
  unreadNotificationsCount
  kpis { revenue30d newCustomers }
}
```

Ici, GraphQL a un vrai avantage :

- **Une seule requête HTTP**, latence côté client souvent meilleure.
- Composition déclarative de données hétérogènes **sans multiplier les endpoints**.

Le coût côté serveur dépend ensuite de la qualité des résolveurs (batching, cache applicatif, etc.).

---

## 3. Scénario 3 : mobile en réseau dégradé

Sur mobile, tu veux limiter :

- Le **nombre de requêtes**.
- La **taille des payloads**.

GraphQL :

- Permet de **demander exactement les champs nécessaires** pour un écran mobile, souvent plus restreint que sur desktop.
- Réduit le « JSON inutile » transmis sur le réseau.

REST peut s’en sortir aussi en :

- Ajoutant des endpoints dédiés mobile (`/mobile/home`), ou des paramètres `?fields=`.
- Mais on arrive vite à une **matrice complexe** de variantes par plateforme.

Dans ce contexte, GraphQL fournit en général un **meilleur contrôle sur le trade‑off données / latence**, au prix d’un backend plus sophistiqué.

---

## 4. Côté serveur : CPU, base de données et cache

Les performances API ne se jouent pas qu’au transport :

- **REST** :
  - Facile à mettre derrière un **reverse proxy / CDN** avec cache par URL.
  - Observabilité simple (un endpoint = une fonction métier).
- **GraphQL** :
  - Requêtes souvent non cacheables telles quelles côté CDN (une seule URL `/graphql`).
  - Mais tu peux :
    - Mettre en place un **cache applicatif** par résolveur ou par clé métier.
    - Utiliser des systèmes comme Apollo, GraphQL Gateway avec cache segmenté.
  - Exige une vigilance sur :
    - Les **N+1 queries**.
    - Les requêtes trop profondes / coûteuses (analyse de coût, limites).

En pratique, beaucoup d’équipes :

- Gardent leurs **microservices internes en REST**.
- Ajoutent une **couche GraphQL BFF** qui agrège et simplifie pour les clients.

---

## 5. Coûts cloud et complexité opérationnelle

Les coûts dépendent de trois choses :

1. **Volume de requêtes** (clients → API).
2. **Travail par requête** (API → bases / autres services).
3. **Capacité à mettre en cache** ce qui peut l’être.

Quelques constats :

- GraphQL peut **réduire le nombre de requêtes front → backend**, mais augmenter la complexité backend si le schéma est mal pensé.
- REST peut être très économique si :
  - Tu exploites bien le cache HTTP / CDN.
  - Tu évites l’explosion d’endpoints agrégés spécifiques.

**Complexité opérationnelle** :

- REST : plus simple pour des équipes petites ou peu outillées.
- GraphQL : nécessite tooling, gouvernance, monitoring spécifiques, mais peut **simplifier** la vie de gros frontends.

---

## 6. Mini‑benchmark conceptuel

Sans chiffres absolus (ils dépendent de ton infra), on peut comparer :

- **Temps de TTFB perçu par l’utilisateur** :
  - REST naïf (multi‑requêtes) : souvent plus mauvais.
  - REST agrégé / GraphQL : comparables.
- **Volume total de données transférées** :
  - REST : dépend de la granularité des endpoints.
  - GraphQL : généralement meilleur (moins de champs inutiles).
- **Simplicité de scaling horizontal** :
  - REST : très simple (stateless, cache par URL).
  - GraphQL : nécessite de bien maîtriser le serveur, les résolveurs et leur coût.

---

## 7. Synthèse : ce qui compte vraiment

Au final, REST comme GraphQL peuvent être **rapides et peu coûteux** si :

- Tu observes tes APIs (APM, traces, métriques).
- Tu soignes le design (pas de N+1, pas de payloads monstrueux).
- Tu mets en place un **cache intelligent**.

La vraie question n’est pas « lequel est le plus rapide ? » mais :  
**quel modèle donne à ton équipe le plus de contrôle et de lisibilité sur ces performances ?**

L’article de conclusion proposera une **grille de décision concrète** pour choisir REST, GraphQL, ou un mix des deux.

