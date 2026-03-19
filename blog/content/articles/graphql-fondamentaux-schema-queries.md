---
title: "GraphQL : schéma, requêtes et bonnes pratiques"
date: 2025-07-08
excerpt: "Comprendre le modèle mental de GraphQL : schéma typé, requêtes déclaratives, résolveurs, pagination, erreurs et évolutions sans casser les clients."
type: article
tags: [API, GraphQL, backend, schema, BFF]
series: api-rest-graphql-serie
series_order: 3
og_image: graphql-fondamentaux-schema-queries-1200x630.jpg
---

# GraphQL : schéma, requêtes et bonnes pratiques

GraphQL est souvent présenté comme « plus moderne que REST », ce qui ne veut pas dire grand‑chose.  
Ce qui le rend intéressant, c’est surtout son **modèle déclaratif** : le client décrit les données dont il a besoin, et le serveur s’occupe de les composer.

---

## 1. Le schéma : contrat unique entre backend et frontend

En GraphQL, tout part du **schéma** :

```graphql
type User {
  id: ID!
  email: String!
  name: String
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
  body: String!
  publishedAt: String
}

type Query {
  me: User
  post(id: ID!): Post
  searchPosts(query: String!, limit: Int = 10): [Post!]!
}
```

- Types forts (`String`, `Int`, `Boolean`, `ID`, `DateTime` custom, etc.).
- Champs obligatoires (`!`) vs optionnels.
- Entrées (`input`) pour structurer les payloads complexes.

Ce schéma devient **la source de vérité** : docs, types TypeScript, mocks de tests peuvent être générés à partir de lui.

---

## 2. Requêtes, mutations et subscriptions

- **Queries** : lecture de données.
- **Mutations** : écriture / effets de bord (création, mise à jour, suppression, actions métier).
- **Subscriptions** : flux temps réel (WebSocket, SSE).

Exemple de requête côté client :

```graphql
query MeWithPosts {
  me {
    id
    email
    posts {
      id
      title
      publishedAt
    }
  }
}
```

Le serveur renvoie **exactement** la forme demandée, ni plus ni moins.

---

## 3. Résolveurs : coller le schéma à ton backend

Chaque champ du schéma est implémenté par un **résolveur** :

- Découpe claire entre **contrat GraphQL** et **sources de données** (base SQL/NoSQL, REST interne, microservices, files, etc.).
- Idéal pour faire un **BFF (Backend For Frontend)** qui agrège plusieurs microservices existants.

Les principaux pièges :

- **N+1 queries** : un résolveur qui tape la base dans une boucle (solution : DataLoader, batching).
- Résolveurs trop gras qui mélangent logique métier, I/O et mapping GraphQL.

---

## 4. Pagination, filtres et erreurs

Deux patterns courants pour la pagination :

- **Offset/limit** simple (suffisant pour beaucoup de cas).
- **Connections / edges / cursors** (pattern Relay) pour du scroll infini robuste.

Pour les erreurs :

- GraphQL renvoie un **bloc `errors`** en plus des `data`.
- Tu peux exposer des **codes d’erreur métier** (ex. `UNAUTHENTICATED`, `FORBIDDEN`, `VALIDATION_ERROR`) utilisables côté client.

Bon réflexe : garder un **format d’erreur cohérent** avec ton monde REST existant, même si le transport est différent.

---

## 5. Évolution du schéma sans tout casser

GraphQL est très adapté aux **évolutions incrémentales** :

- Ajouter des champs est non‑breaking (les clients existants ne les demandent pas).
- Tu peux **déprécier un champ** (`@deprecated(reason: "Use foo instead")`) avant de le supprimer.
- Les clients choisissent quand consommer les nouveautés.

Mais attention :

- Un schéma mal pensé devient vite **un gros monolithe** difficile à faire évoluer.
- Il faut une vraie **gouvernance de schéma** (reviews, conventions de nommage, ownership des domaines, etc.).

---

## 6. Bonnes pratiques côté client et côté serveur

**Côté serveur** :

- Sécuriser (`auth`, `authz`) au niveau des **résolveurs**.
- Limiter la **profondeur** et la **complexité** des requêtes (query cost analysis).
- Observer : logs détaillés, temps passé dans chaque résolveur, traces distribuées.

**Côté client** :

- Générer les **types TypeScript** à partir du schéma pour éviter les erreurs de champs.
- Centraliser les requêtes plutôt que d’avoir 50 fragments copiés/collés.
- Sur mobile, penser à la **taille des payloads** et aux stratégies de cache côté client.

---

## 7. Ce que GraphQL change (ou pas) dans ton équipe

GraphQL :

- **Rapproche les équipes frontend et backend** autour d’un schéma partagé.
- Demande une montée en compétence tooling (serveur, clients, observabilité).
- N’efface pas les problématiques classiques : dettes métiers, performance SQL, sécurité, etc.

L’article suivant plongera dans les **performances, coûts et benchmarks** REST vs GraphQL sur des cas concrets.

