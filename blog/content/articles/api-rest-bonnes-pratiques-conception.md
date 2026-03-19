---
title: "APIs REST : principes, bonnes pratiques et limites"
date: 2025-07-03
excerpt: "Revenir aux bases de REST, poser un design propre (URLs, verbes HTTP, erreurs, pagination, sécurité) et comprendre où ça commence à coincer."
type: article
tags: [API, REST, HTTP, backend, bonnes pratiques]
series: api-rest-graphql-serie
series_order: 2
og_image: api-rest-bonnes-pratiques-conception-1200x630.jpg
---

# APIs REST : principes, bonnes pratiques et limites

REST reste la norme de facto pour exposer des APIs.  
Dans cet article, on se concentre sur **un REST pragmatique bien fait** : ce qui apporte de la clarté et de la robustesse, et ce qui finit par générer de la dette si on ne le gère pas.

---

## 1. Modéliser des ressources claires

- Penser en **ressources métier** : `users`, `orders`, `products`, pas en actions techniques (`/doStuff`).
- Utiliser des **noms au pluriel** pour les collections (`/users`) et un **identifiant stable** pour un élément (`/users/{id}`).
- Éviter les verbes dans les URLs : l’intention vient du **verbe HTTP** (`POST /orders` pour créer, `PATCH /orders/{id}` pour mettre à jour).

Quelques exemples cohérents :

```text
GET    /orders            # liste (filtrable/paginée)
GET    /orders/123        # détail
POST   /orders            # création
PATCH  /orders/123        # mise à jour partielle
DELETE /orders/123        # suppression
```

---

## 2. Bien utiliser HTTP (verbes, codes, headers)

- **Verbes** : `GET` idempotent, `POST` pour créer ou déclencher une action non idempotente, `PUT` pour remplacer, `PATCH` pour modifier partiellement.
- **Codes HTTP** lisibles :
  - `2xx` : succès (`200`, `201`, `204`).
  - `4xx` : erreur côté client (`400`, `401`, `403`, `404`, `409`, `422`…).
  - `5xx` : erreur serveur (`500`, `503`).
- **Headers** :
  - `Location` pour indiquer la ressource créée (`201 Created`).
  - `ETag` + `If-None-Match` pour la mise en cache conditionnelle.
  - `X-Request-Id` pour tracer les requêtes.

Une API REST bien faite exploite vraiment HTTP, pas seulement `GET` et `POST`.

---

## 3. Contrats et format de réponse

Deux points clés :

- **Format de base** : JSON structuré, cohérent d’un endpoint à l’autre.
- **Structure d’erreurs uniforme** :

```json
{
  "error": "validation_error",
  "message": "Certains champs sont invalides",
  "details": [
    { "field": "email", "message": "Format invalide" },
    { "field": "password", "message": "Doit contenir au moins 12 caractères" }
  ]
}
```

Documenter ce contrat d’erreur est souvent plus utile que d’ajouter 30 endpoints.

---

## 4. Pagination, filtrage, tri

Sans pagination, les endpoints « liste » deviennent vite ingérables.

- **Pagination** :
  - Stratégie simple : `page` + `page_size`.
  - Stratégie scalable : **cursor‑based** (`cursor`, `limit`) pour éviter les problèmes de `OFFSET`.
- **Filtrage & tri** :
  - Paramètres query explicites (`?status=paid&sort=-created_at`).
  - Éviter les DSL maison trop complexes (préférer plusieurs filtres simples bien documentés).

Expose toujours la **métadonnée de pagination** dans la réponse (`total`, `has_next`, `next_cursor`…).

---

## 5. Sécurité et versioning

- **Sécurité** :
  - Authentification (JWT, OAuth2, API keys) standardisée.
  - Autorisation au niveau ressource / champ si besoin.
  - Rate limiting, validation forte des inputs, logs de sécurité.

- **Versioning** :
  - Éviter un `v1`, `v2`, `v3` tous les 6 mois.
  - Préférer les **évolutions compatibles** : ajouter des champs, déprécier au lieu de supprimer.
  - Quand une rupture est inévitable, **préparer une migration** (double écriture, double lecture, période de cohabitation).

---

## 6. Là où REST commence à montrer ses limites

Même bien fait, REST peut devenir douloureux quand :

- Le frontend doit agréger **beaucoup de ressources différentes** pour un seul écran.
- On a des **relations très profondes** (ex. graphes sociaux, permissions complexes).
- On doit **optimiser chaque octet** (mobile en réseau dégradé).

Les symptômes classiques :

- Prolifération de endpoints « sur mesure » : `GET /screen-home`, `GET /screen-dashboard`, etc.
- Beaucoup de **round‑trips** côté frontend.
- Des réponses très volumineuses alors qu’on n’affiche que quelques champs.

Ce sont précisément ces problèmes que GraphQL promet d’adresser… mais avec d’autres compromis.  
On les détaillera dans le prochain article.

