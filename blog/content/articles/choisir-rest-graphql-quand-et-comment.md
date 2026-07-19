---
title: "REST ou GraphQL : comment choisir (ou combiner)"
date: 2025-07-15
excerpt: "Une grille simple selon ton contexte — et comment mixer les deux sans se perdre."
type: article
tags: [API, REST, GraphQL, architecture, décision]
series: api-rest-graphql-serie
series_order: 5
og_image: choisir-rest-graphql-quand-et-comment-1200x630.jpg
---

# REST ou GraphQL : comment choisir (ou combiner)

On a vu les bases, le design, les perfs. Il reste la question qui te reveille a 3h avant un kick-off : qu'est-ce que je choisis pour **ce** projet ? Et est-ce que je vais le regretter dans deux ans ?

Spoiler : ce n'est pas une guerre de religion. C'est un choix de **friction** - entre ton metier, tes clients, ton equipe et ton infra.

Relis vite le [decor](/blog/articles/api-rest-graphql-fondamentaux-comparaison.html), le [design REST](/blog/articles/api-rest-bonnes-pratiques-conception.html), [GraphQL](/blog/articles/graphql-fondamentaux-schema-queries.html) et les [perfs](/blog/articles/api-rest-graphql-performances-benchmarks.html) si besoin.

## Pose le contexte avant l'outil

Deux devs full-stack qui sortent un MVP, ce n'est pas la meme histoire qu'une boite avec trois squads front et un paysage de microservices.

Le type de **clients** compte : SPA riche, apps mobiles, partenaires B2B qui veulent du REST documente OpenAPI, API publique consommee par des inconnus. La stabilite du domaine aussi : si ton modele bouge tous les sprints, un schema GraphQL trop figé trop tot peut faire mal - ou au contraire t'aider si tu ajoutes des champs sans casser.

Et les contraintes non fonctionnelles : SLA, couts, conformite, exposition publique ou non.

Si tu sautes cette etape et que tu choisis "parce que c'est moderne", tu as deja perdu. Le kick-off le plus productif, c'est celui ou quelqu'un demande : "qui consomme quoi, et a quelle frequence ca change ?" **avant** de parler techno.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/choisir-rest-graphql.svg" alt="Schéma de décision REST vs GraphQL" class="schema-inline" width="640" />
  <figcaption>REST, GraphQL ou mix : le contexte décide, pas la hype.</figcaption>
</figure>

## Quand REST est un no-brainer

**REST** gagne souvent quand tu exposes des ressources claires, un CRUD propre, des integrations partenaires qui s'attendent a du HTTP classique. Petite equipe. Peu d'envie d'investir tout de suite dans le tooling GraphQL. Frontend qui n'a pas besoin de [compose](/blog/articles/[docker](/blog/articles/docker-fondamentaux-images-conteneurs.html)-compose-environnements-local.html)r dix sources pour peindre un ecran.

Dans ce monde-la, une API REST bien concue, une doc OpenAPI correcte, un contrat d'erreurs stable, un versioning calme - tu peux vivre longtemps et bien.

Les gens sous-estiment a quel point "REST bien fait" suffit. Ils comparent GraphQL a du REST pourri. Mauvaise comparaison. Compare GraphQL a un REST coherent, et tu verras que beaucoup de projets n'ont simplement **pas** le probleme que GraphQL resout. Inutile de soigner une maladie que tu n'as pas.

## Quand GraphQL change vraiment la donne

La ou **GraphQL** brille : plusieurs clients (web, iOS, Android) qui ne veulent pas les memes tranches de donnees. Ecrans tres composites, widgets, agregats. Equipes front qui ont besoin d'autonomie sur la forme des reponses sans ouvrir un ticket backend pour chaque champ. Ou un **BFF** qui cache un labyrinthe de microservices REST deja en place.

Dans ces cas, tu reduis la proliferation d'endpoints "ecran". Le schema devient le lieu de collaboration. Attention : ca marche si le back est pret a tenir le schema, a limiter les queries couteuses, a observer les resolveurs. Sinon tu as juste deplace la dette - et parfois empire, parce que maintenant tout le monde peut inventer une query monstrueuse.

## Le mix : REST en interne, GraphQL en facade

Strategie tres repandue, et souvent la plus sage. Tu gardes tes services internes en REST (voire gRPC). Tu ajoutes une couche GraphQL orientee experience pour les fronts. Tu n'as pas jete l'existant. Tu introduis GraphQL progressivement sur les parcours qui souffrent vraiment - dashboard, profil riche - et tu laisses REST pour le reste.

Le risque : transformer le serveur GraphQL en monolithe de glue code sans **gouvernance**. Qui change le schema ? Qui review ? Qui possede quel domaine ? Sans reponses, le mix devient une usine a gaz avec deux styles au lieu d'un.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/rest-graphql-mix.svg" alt="Schema d'architecture mixte REST interne et GraphQL facade" class="schema-inline" width="640" />
  <figcaption>Le mix gagnant : REST en interne, GraphQL en facade quand les ecrans le demandent.</figcaption>
</figure>

## Transition dans les deux sens

Tu as deja du REST en prod ? Cartographie les endpoints vraiment utilises. Identifie les ecrans qui souffrent (trop d'appels, trop de complexite, trop de temps de dev). Introduis GraphQL sur un perimetre limite. Garde REST ailleurs. Pas de big bang. Un **pilote** sur un parcours douloureux vaut mieux qu'une migration "tout GraphQL d'ici la fin du trimestre".

Tu as commence par GraphQL et tu regrettes pour certains usages ? Tu peux geler le schema, exposer des endpoints REST pour des partenaires ou des integrations simples, et vivre avec les deux. Tu n'es pas marie a vie a un seul style. Les architectures qui durent acceptent souvent ce genre de pragmatisme.

## Grille rapide (sans slide PowerPoint)

Front simple, peu de composition → **REST**. Integrations B2B ou API publique → REST, eventuellement avec quelques agregats. Front riche SPA/mobile avec beaucoup d'ecrans composites → GraphQL ou BFF GraphQL. Microservices REST deja la → REST interne + GraphQL d'agregation. Equipe reduite, peu de temps pour le tooling → REST d'abord, GraphQL plus tard si un vrai besoin apparait.

Ce n'est pas une formule magique. C'est un **filtre** pour eviter de discuter deux heures autour d'une preference personnelle. Si apres ce filtre tu hesites encore, commence simple (REST), mesure la douleur, et ajoute GraphQL la ou les tickets "endpoint pour cet ecran" s'accumulent.

## Fin de serie, pas fin de debat

REST reste un excellent standard pour les ressources, l'integration, la simplicite operationnelle. GraphQL brille quand tu as besoin de flexibilite cote client et de composition complexe. Le bon choix, c'est celui qui reduit la friction - pas celui qui gagne sur Twitter.

Si cette serie t'a aide a poser le decor, a soigner le design, a regarder les perfs sans dogme, et a choisir (ou mixer) sans panique, tu as deja gagne plus que la plupart des kick-off ou quelqu'un dit "on fait du GraphQL" avant d'avoir pose le besoin.
