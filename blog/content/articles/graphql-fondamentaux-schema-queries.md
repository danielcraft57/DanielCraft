---
title: "GraphQL : demander exactement ce qu'il te faut"
date: 2025-07-08
excerpt: "Un schéma, des questions précises, et ce qui change vraiment pour l'équipe derrière."
type: article
tags: [API, GraphQL, backend, schema, BFF]
series: api-rest-graphql-serie
series_order: 3
og_image: graphql-fondamentaux-schema-queries-1200x630.jpg
---

# GraphQL : demander exactement ce qu'il te faut

On entend souvent : "GraphQL, c'est plus moderne que REST." OK. Et apres ? Modernite ne construit pas une page.

Ce qui rend **GraphQL** interessant, c'est un autre modele mental. Le client dit ce dont il a besoin. Le serveur [compose](/blog/articles/[docker](/blog/articles/docker-fondamentaux-images-conteneurs.html)-compose-environnements-local.html) la reponse. Pas magique. Juste **declaratif**. Et ca change vraiment la vie... si tu as compris le schema, les resolveurs, et les pieges.

Pour le contexte general, vois d'abord [REST vs GraphQL](/blog/articles/api-rest-graphql-fondamentaux-comparaison.html). Pour le design REST classique, vois les [bonnes pratiques REST](/blog/articles/api-rest-bonnes-pratiques-conception.html).

## Le schema, c'est le contrat

En GraphQL, tout part du **schema**. Types, champs, relations. Ce qui est obligatoire. Ce qui est optionnel. C'est la source de verite partagee entre front et back.

Tu peux generer de la doc, des types TypeScript, des mocks - a partir de ca. Si ton schema est flou, tout le reste sera flou. Contrairement a une pile d'endpoints eparpilles, ici tu as **un seul** endroit pour comprendre le graphe metier.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/graphql-schema-resolvers.svg" alt="Schéma GraphQL : types, requêtes et résolveurs" class="schema-inline" width="640" />
  <figcaption>Du schéma aux résolveurs : le contrat d'un côté, les sources de données de l'autre.</figcaption>
</figure>

Petit extrait pour se mettre d'accord :

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

Tu vois l'idee : le graphe est explicite. `User` a des `posts`. Une query `me` existe. Pas besoin de cinq endpoints pour raconter la meme histoire.

En revanche, soigne ce schema. Sans conventions, sans reviews, ca devient un tas de dettes en six mois. Inputs types, enums pour les statuts, scalars custom seulement si besoin - et reste lisible pour un humain qui debarque.

## Queries, mutations, et le reste

Les **queries**, c'est la lecture. Les **mutations**, c'est l'ecriture et les effets de bord. Les **subscriptions**, c'est le temps reel - si tu en as vraiment besoin. Pas "parce que ca fait cool". Le temps reel a un cout. Beaucoup d'equipes s'en passent tres bien avec un petit polling au debut.

Cote client, une query ressemble a ca :

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

Le serveur renvoie **exactement** cette forme. Ni le pave d'un `/users/me` gonfle, ni trois appels en cascade. Pour un mobile qui n'affiche que trois champs, tu demandes trois champs. Pour un dashboard, tu demandes plus. Meme schema, tranches differentes. C'est ca, le vrai pitch.

## Resolveurs : la ou ca devient reel

Le schema, c'est le contrat. Les **resolveurs**, c'est le collage vers tes sources : SQL, NoSQL, services REST, files... C'est pour ca que GraphQL marche bien en **BFF** : tu caches la complexite interne derriere un graphe oriente produit. Le front n'a pas a savoir que les commandes viennent d'un service et les notifs d'un autre.

Le piege classique, c'est le **N+1**. Tu resols une liste d'utilisateurs. Puis pour chacun, tu vas chercher ses posts un par un. En local avec dix users, ca passe. En prod avec mille, tu pleures. Batching, DataLoader, cache - ce n'est pas du luxe. C'est la survie.

Autre piege : des resolveurs qui melangent mapping GraphQL, logique metier et I/O dans le meme blob. Garde le resolveur mince. Le metier vit ailleurs. Sinon, le jour ou tu veux reutiliser une regle hors GraphQL, tu es coince.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/graphql-n1-resolvers.svg" alt="Schema du probleme N+1 GraphQL et du batching DataLoader" class="schema-inline" width="640" />
  <figcaption>Sans batching, chaque champ peut devenir une requete : le piege N+1.</figcaption>
</figure>

## Pagination, erreurs, evolution

Pour paginer : offset/limit (simple) ou curseurs type Relay (plus robuste pour le scroll infini). Choisis selon ton cas. Documente. Reste coherent d'un type a l'autre.

Pour les **erreurs**, GraphQL renvoie un bloc `errors` a cote de `data`. Garde des codes metier stables : `UNAUTHENTICATED`, `FORBIDDEN`, `VALIDATION_ERROR`. Le client branche sans parser de la prose.

Cote evolution : ajouter un champ ne casse pas les clients (ils ne le demandent pas). Tu peux deprecier avec `@deprecated` avant de supprimer. Mais "evolutif" ne veut pas dire "sans gouvernance". Qui ajoute quoi ? Qui review ? Qui possede Commandes vs Users ? Sans ca, ton schema devient un terrain vague.

## Ce que ca change dans l'equipe

GraphQL rapproche front et back autour d'un contrat unique. Ca demande aussi du **tooling** : serveur, clients, observabilite des resolveurs, limites de profondeur, cout des queries. Securite au niveau des champs. Logs qui disent quel resolveur a pris 400 ms.

Cote client : genère tes types depuis le schema. Centralise tes queries. Pense a la taille des payloads sur mobile. GraphQL n'efface pas un SQL lent ni une auth bancale. Il deplace le probleme vers le graphe.

Prochain episode : [performances, couts, benchmarks](/blog/articles/api-rest-graphql-performances-benchmarks.html) - la ou les slides marketing rencontrent la facture cloud. Puis la [grille de choix](/blog/articles/choisir-rest-graphql-quand-et-comment.html).
