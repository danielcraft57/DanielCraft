---
title: "API : deux façons de faire parler un site et un serveur"
date: 2025-07-01
excerpt: "REST et GraphQL, c'est quoi ? Deux styles pour demander des infos à un serveur — on pose le décor."
type: article
tags: [API, REST, GraphQL, backend, architecture]
series: api-rest-graphql-serie
series_order: 1
og_image: api-rest-graphql-fondamentaux-comparaison-1200x630.jpg
---

# API : deux façons de faire parler un site et un serveur

Imagine deux restaurants. Dans le premier, tu commandes des **plats fixes** sur un menu. Dans le second, tu dis exactement ce que tu veux dans ton assiette. Une **API**, c'est un peu ca : un moyen pour ton site (ou ton app) de demander des infos a un serveur.

Souvent, quelqu'un dit trop vite : "On fait du GraphQL !" Ou l'inverse : "REST, point final." Trop tot. Avant de choisir, il faut comprendre ce que chaque style promet - et ce qu'il te demande en echange.

## Une bonne API, c'est d'abord un contrat clair

Oublie un instant les noms REST et GraphQL. Une bonne API, c'est un **contrat**. Tu sais comment appeler. Tu sais ce qui revient. Tu sais quoi faire si ca casse.

Les **erreurs** doivent etre lisibles. La **doc** doit servir, pas dormir dans un PDF de 2019. Et surtout : tu ne veux pas casser dix clients parce qu'un champ a change de nom un mardi.

Pense aussi a la **stabilité**. Et a pouvoir expliquer pourquoi une requete a mis 800 ms un vendredi. Logs, mesures, traces - sans ca, tu cherches une aiguille dans le noir.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/rest-vs-graphql.svg" alt="Schéma comparatif REST vs GraphQL" class="schema-inline" width="640" />
  <figcaption>Deux styles, même objectif : un contrat clair entre clients et serveur.</figcaption>
</figure>

La **vitesse** compte aussi. Une API "elegante" qui fait exploser la facture cloud, ce n'est pas une bonne API. Enfin, elle doit parler le langage du metier : commandes, utilisateurs, abonnements - pas un catalogue de routes inventees au fil des tickets.

Ces criteres, c'est ta grille. REST et GraphQL ne sont que deux reponses differentes a la meme question.

## REST : des ressources et des verbes

**REST**, ce n'est pas une librairie a installer. C'est une facon d'organiser les echanges sur le web, avec **HTTP**.

Les choses ont des adresses (des **URLs**) : `/users`, `/orders/123`. Les **verbes** disent l'action : lire (`GET`), creer (`POST`), modifier (`PATCH`), supprimer (`DELETE`). Les **codes** racontent la suite : `200` ok, `404` introuvable, `500` probleme serveur.

Chaque requete est independante. On dit "sans etat" : le serveur ne garde pas ta conversation precedente dans sa tete.

Dans la vraie vie, presque personne ne fait du REST "parfait de these". On fait du REST **pratique**. On garde les idees utiles. On adapte le reste. Et c'est bien.

L'avantage enorme : le monde connait deja HTTP. Caches, CDN, `curl`, Postman, OpenAPI - tout le monde s'y retrouve. Pour une API publique ou des partenaires, REST reste souvent le chemin le plus simple. Tu veux aller plus loin ? Lis les [bonnes pratiques REST](/blog/articles/api-rest-bonnes-pratiques-conception.html).

Le piege : avec le temps, tu accumules des endpoints. Le front fait trois, quatre, cinq appels pour peindre une page. Ou tu renvoies trop de champs inutiles. Ou tu crees des routes speciales `/screen-home` pour coller a l'ecran. Ca marche... jusqu'au jour ou tu ne sais plus lequel de tes 120 endpoints sert encore.

## GraphQL : tu demandes exactement ce dont tu as besoin

**GraphQL**, c'est un langage de requete. Ne chez Facebook. Tu decries un **schema** (une carte des types et des liens). Le client dit : "donne-moi ca, ca et ca". Souvent, tout passe par **une seule** adresse : `/graphql`.

L'idee centrale : eviter de recevoir trop peu... ou trop. Sur un ecran riche (app, dashboard), tu veux l'email, trois commandes recentes, le compteur de notifs - point. Pas un pavé JSON de 40 champs.

Ca sonne magique. Ce n'est **pas** magique. Il y a une courbe d'apprentissage. Le cache CDN est moins "gratuit" qu'avec des URLs REST propres. Et une mauvaise requete peut etre monstrueuse si tu ne limites rien.

Pour comprendre le schema et les requetes, vois l'article [GraphQL : schema et queries](/blog/articles/graphql-fondamentaux-schema-queries.html).

## Ou chacun brille (et ou ca coince)

REST brille quand tu as des ressources stables : catalogue, commandes, paiement, SMS. Integrations B2B. CRUD clair. Tu veux du standard, du cache simple, du debug lisible : REST est souvent le bon **defaut**.

GraphQL brille quand tes fronts [compose](/blog/articles/[docker](/blog/articles/docker-fondamentaux-images-conteneurs.html)-compose-environnements-local.html)nt beaucoup. Web, iOS, Android - pas les memes tranches de donnees. Un **BFF** (une couche devant qui assemble pour l'ecran) qui cache des microservices. Un metier plein de liens. La, les requetes declaratives changent vraiment la vie du front - si le back tient le schema.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/rest-graphql-ou-briller.svg" alt="Schema ou REST et GraphQL excellent chacun" class="schema-inline" width="640" />
  <figcaption>REST et GraphQL ne se battent pas sur le meme terrain : pattern d'acces d'abord.</figcaption>
</figure>

Les faiblesses se mirent. REST : trop d'endpoints, trop d'aller-retours, payloads trop gros. GraphQL : plus complexe a operer, cache plus subtil, risque de requetes couteuses. Ni l'un ni l'autre n'efface un SQL lent ou une auth foireuse. Ils **deplacent** le probleme.

## Comment lire la suite

La question "REST ou GraphQL ?" n'a pas de gagnant universel. Elle a des **contextes**.

Ensuite dans la serie : design REST, schema GraphQL, [performances et couts](/blog/articles/api-rest-graphql-performances-benchmarks.html), puis une [grille pour choisir (ou mixer)](/blog/articles/choisir-rest-graphql-quand-et-comment.html).

Pour l'instant, retiens ca : ce n'est pas une guerre de religion. C'est un choix d'architecture. Si tu poses le decor correctement, tu evites deja la moitie des regrets.
