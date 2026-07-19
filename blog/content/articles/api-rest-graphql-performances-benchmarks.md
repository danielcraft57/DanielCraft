---
title: "REST ou GraphQL : lequel va plus vite (et pour qui)"
date: 2025-07-10
excerpt: "Écran simple, dashboard chargé, mobile, cache : où chacun gagne vraiment."
type: article
tags: [API, REST, GraphQL, performance, benchmark]
series: api-rest-graphql-serie
series_order: 4
og_image: api-rest-graphql-performances-benchmarks-1200x630.jpg
---

# REST ou GraphQL : lequel va plus vite (et pour qui)

"GraphQL est plus rapide que REST." Non. Ou plutot : ca depend tellement du contexte que la phrase ne veut **rien** dire.

Ce qui compte en prod, c'est autre chose. Combien de **requetes** partent du client. Combien de travail ca genere cote base. Quelle **latence** l'utilisateur ressent. Combien tu paies en infra. Et a quel point ton equipe comprend ce qui se passe quand ca rame un vendredi.

Pour le decor, vois [REST vs GraphQL](/blog/articles/api-rest-graphql-fondamentaux-comparaison.html). Pour soigner chaque style : [REST](/blog/articles/api-rest-bonnes-pratiques-conception.html) et [GraphQL](/blog/articles/graphql-fondamentaux-schema-queries.html).

## Ecran simple : match nul (presque)

Page profil. Infos de base. Avec REST : un `GET /users/me`, JSON propre, **cache** HTTP/CDN facile. Avec GraphQL : une query `me { id email name }`, un resolveur, meme histoire.

Bien fait, les deux sont rapides et peu chers. REST garde un leger avantage sur la simplicite de cache CDN : une URL stable, les proxies savent quoi en faire. GraphQL passe souvent tout par `/graphql` - le cache "gratuit" n'est plus aussi gratuit.

Si ton produit, c'est surtout ca - des ressources stables, peu de composition - te battre sur GraphQL pour gagner 5 ms, c'est du theatre. Personne ne le sentira.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/api-perf-benchmark.svg" alt="Schéma comparatif des performances REST et GraphQL" class="schema-inline" width="640" />
  <figcaption>Latence perçue, volume de données, charge serveur : trois axes, pas un seul gagnant.</figcaption>
</figure>

## Dashboard composite : la, ca change

Imagine un **dashboard** : user, cinq dernieres commandes, compteur de notifs, quelques chiffres. REST naif : quatre a six appels. Si le front les enchaine mal, tu as une cascade. L'utilisateur attend. Tu te demandes pourquoi "l'API est lente" alors que c'est surtout le pattern d'appels.

REST optimise : un endpoint dedie `GET /dashboards/home`. Performant, oui. Specifique a un ecran, aussi. Multiplie par dix ecrans : collection de Frankenstein.

GraphQL : une query qui demande exactement ces tranches. Une requete HTTP. Cote client, la latence ressentie est souvent meilleure. Cote serveur, tout depend des resolveurs : batching, DataLoader, cache. Si tu resols n'importe comment, tu as juste deplace le cout du reseau vers la base - et parfois multiplie.

## Mobile, reseau pourri

Sur **mobile**, chaque octet et chaque requete comptent. GraphQL brille ici : tu peux demander un sous-ensemble vraiment mince pour le telephone, different du desktop. Moins de JSON mort.

REST s'en sort avec des endpoints mobile dedies ou des `?fields=` - jusqu'au jour ou tu as une matrice de variantes et personne ne sait laquelle est encore vivante.

En clair : GraphQL te donne un meilleur controle sur le trade-off donnees / latence, au prix d'un backend plus exigeant. REST te donne de la simplicite, au prix parfois de payloads trop gros ou de trop d'appels. Ni l'un ni l'autre n'est "plus rapide" en soi.

## Serveur, CPU, cache : le vrai terrain

Les perfs ne se jouent pas qu'au transport. REST derriere un reverse proxy ou un CDN avec cache par URL : pain beni. Un endpoint = une intention = des logs lisibles.

GraphQL : le cache CDN "par URL" marche mal. Tu compenses avec du cache applicatif par resolveur, des cles metier, eventuellement une gateway. Tu surveilles aussi la **profondeur** des queries et le cout : un client peut te demander un graphe monstrueux si tu ne limites rien.

Beaucoup d'equipes font un choix hybride qui marche bien : microservices internes en REST (ou gRPC), couche GraphQL BFF devant pour les fronts. Cache et clarte en interne. Composition pour les clients. Souvent le meilleur des deux mondes - si le BFF ne devient pas un monolithe opaque.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/api-cache-layers.svg" alt="Schema des couches de cache cote API" class="schema-inline" width="640" />
  <figcaption>Le perf game se joue souvent dans les caches, pas dans le framework.</figcaption>
</figure>

## Couts cloud et complexite humaine

Trois leviers : volume de requetes clients, travail par requete, capacite a **cacher** ce qui peut l'etre. GraphQL peut reduire les appels front → API tout en augmentant le travail serveur si le schema est mal pense. REST peut etre tres economique si tu exploites le cache HTTP et que tu evites l'explosion d'endpoints agreges.

Et puis il y a le **cout humain**. REST, petites equipes, outillage classique : plus simple a operer. GraphQL : tooling, gouvernance, monitoring des resolveurs. En echange, les gros fronts gagnent en autonomie. Si tu n'as pas le budget mental pour soigner le serveur GraphQL, tu vas payer plus cher en incidents qu'en instances.

Sans chiffres absolus (ils dependent de ton infra), le mini-benchmark mental : REST naif multi-requetes perd souvent sur la latence ressentie. REST agrege et GraphQL bien faits sont comparables. Sur le volume de donnees, GraphQL gagne souvent. Sur le scaling "bete et mechant", REST reste plus simple.

## Ce qui compte vraiment

Au final, les deux peuvent etre rapides et peu couteux si tu observes, si tu evites les N+1, si tu caches intelligemment. **Mesure** avant de trancher. Une intuition de cafe ne remplace pas une trace.

La question utile n'est pas "lequel est le plus rapide ?" C'est : quel modele donne a ton equipe le plus de controle et de lisibilite ? La [grille de decision](/blog/articles/choisir-rest-graphql-quand-et-comment.html) arrive juste apres - y compris le mix des deux. Oui, tu n'es pas oblige de choisir une religion.
