---
title: "REST : bien organiser ses portes et ses règles"
date: 2025-07-03
excerpt: "Ressources, verbes HTTP, pagination, sécurité : les bases pour une API claire et durable."
type: article
tags: [API, REST, HTTP, backend, bonnes pratiques]
series: api-rest-graphql-serie
series_order: 2
og_image: api-rest-bonnes-pratiques-conception-1200x630.jpg
---

# REST : bien organiser ses portes et ses règles

Tu as deja vu des APIs ou chaque route a l'air inventee le mardi soir. Des codes qui ne veulent rien dire. Des reponses qui changent de forme selon l'humeur du serveur. Ce n'est **pas** du REST. C'est du HTTP bricole.

La bonne nouvelle : un REST **clair** et coherent, ca se pose vite. Avec quelques regles. Et en sachant ou ca commence a grincer.

Si tu debutes la serie, repose d'abord le decor dans [REST vs GraphQL](/blog/articles/api-rest-graphql-fondamentaux-comparaison.html).

## Penser objets metier, pas boutons

Le premier mauvais reflexe : coller des verbes dans l'adresse. `/createUser`. `/doPayment`. Ca marche deux semaines. Puis tu as un catalogue d'actions impossibles a documenter.

**REST** te pousse a penser en **ressources** : utilisateurs, commandes, factures. Une collection `/orders`. Un element `/orders/123`. L'intention, elle, vient du **verbe HTTP**.

Creer : `POST /orders`. Lire : `GET /orders/123`. Modifier un peu : `PATCH /orders/123`. Supprimer : `DELETE /orders/123`. Tu vois le motif ?

Le front, Postman, un partenaire - tout le monde lit la carte sans te demander un Slack a chaque fois. Pour une action bizarre (annuler, republier), reste propre : `POST /orders/123/cancellation` plutot que `/cancelOrderNowPlease`.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/rest-resource-verbs.svg" alt="Schéma REST : ressources, verbes HTTP et codes de statut" class="schema-inline" width="640" />
  <figcaption>Ressources + verbes HTTP : l'intention vit dans la méthode, pas dans l'URL.</figcaption>
</figure>

Petite regle d'or : noms au **pluriel** pour les collections. Identifiant **stable** pour l'element. Pas `/order/abc` un jour et `/orders/abc` le lendemain. La **coherence**, c'est 80 % d'une bonne API.

## HTTP, ce n'est pas juste GET et POST

Beaucoup d'APIs "REST" utilisent GET pour tout lire et POST pour tout le reste. Pratique. Aussi un gachis.

Un `GET` ne doit **rien** changer. Un `PUT` remplace. Un `PATCH` modifie en partie. Si tu melanges tout, ton cache, tes retries et ton monitoring deviennent des cauchemars.

Un `201 Created` avec un `Location` vers la ressource neuve : le client ne joue plus aux devinettes. Un `404` clair. Un `409` en conflit. Un `422` si la validation echoue. Les `5xx` disent "c'est chez nous" - et tu les surveilles comme le lait sur le feu.

Les **en-tetes** aident aussi. `ETag` pour eviter de renvoyer la meme chose. Un `X-Request-Id` pour retrouver une requete dans les logs quand un client dit "ca a plante hier a 16h".

Petit exemple d'erreur coherente - souvent plus important qu'un nouvel endpoint :

```json
{
  "error": "validation_error",
  "message": "Certains champs sont invalides",
  "details": [
    { "field": "email", "message": "Format invalide" },
    { "field": "password", "message": "Doit contenir au moins 12 caracteres" }
  ]
}
```

Si tous tes endpoints parlent la **meme langue** d'erreur, le front te remercie. Sinon tu paies ca pendant des annees.

## Listes : pages, filtres, tri

Sans **pagination**, `GET /orders` finit par renvoyer la moitie de ta base un vendredi. La version simple (`page` + `page_size`) suffit longtemps. Quand ca grossit vraiment, un **curseur** (`cursor`, `limit`) evite les surprises du `OFFSET` SQL qui devient lent.

Filtres et tri : reste explicite. `?status=paid&sort=-created_at`. Pas de mini-langage maison que personne n'ose toucher.

Renvoie aussi des **metadonnees** utiles : `total`, `has_next`, `next_cursor`. Le client ne doit pas inventer sa logique de "y a-t-il encore des pages ?".

## Securite et versions sans panique

Authentification classique (JWT, OAuth2, cles API selon le cas). Droits au niveau ressource. Validation des entrees. Limite de debit. Rien de revolutionnaire. C'est le minimum pour dormir.

Valider **cote serveur** n'est pas optionnel. Le client peut etre une app, un script, un attaquant. Pareil pour les logs de secu : tu veux savoir qui a tape quoi.

Le **versioning**, on le comprend souvent mal. Tu n'as pas besoin d'un `/v2` tous les six mois. Ajoute des champs. Deprecie avant de supprimer. Documente. Une rupture franche, parfois - avec une periode de cohabitation. Les partenaires ne lisent pas ton changelog Discord.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/rest-versioning-secu.svg" alt="Schema des couches securite et versioning d'une API REST" class="schema-inline" width="640" />
  <figcaption>Securite et versioning : des couches stables autour du contrat HTTP.</figcaption>
</figure>

## La ou REST commence a te fatiguer

Meme bien fait, REST a des **limites**. Un dashboard qui veut l'utilisateur, cinq commandes, des notifs et trois chiffres : soit une cascade d'appels, soit un endpoint Frankenstein `/dashboards/home`. Multiplie par mobile et partenaires : explosion de routes "speciales".

Les relations profondes font le meme effet. Trop d'appels... ou trop de payload. Sur un mobile en mauvais reseau, chaque octet se paie cash.

Ce n'est pas une raison de jeter REST. C'est une raison de savoir quand il faut autre chose. La suite de la serie parle de [GraphQL](/blog/articles/graphql-fondamentaux-schema-queries.html), des [perfs](/blog/articles/api-rest-graphql-performances-benchmarks.html) et du [choix concret](/blog/articles/choisir-rest-graphql-quand-et-comment.html).

Pour l'instant : un REST clair, qui exploite vraiment HTTP, reste un excellent **defaut**. Le reste, c'est de la dette que tu choisis - ou que tu subis sans le savoir.
