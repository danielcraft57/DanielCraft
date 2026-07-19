---
title: "Docker : la recette et le gâteau (image vs conteneur)"
date: 2024-11-05
excerpt: "Image = plan figé. Conteneur = instance qui tourne. Les bases sans jargon."
type: article
tags: [Docker, conteneurs, images, DevOps, fondamentaux]
series: docker-serie
series_order: 1
og_image: docker-fondamentaux-1200x630.jpg
---

# Docker : la recette et le gâteau (image vs conteneur)

Imagine une **recette** de gateau et le gateau lui-meme. La recette, tu la ranges. Le gateau, tu le manges. Avec Docker, c'est la meme idee.

L'**image**, c'est la recette figee. Le **conteneur**, c'est le gateau en train de tourner. Si tu melanges les deux, tout devient flou. On pose ca clairement ici.

---

## Image vs conteneur : la metaphore simple

Docker, c'est une usine a petites boites. Chaque boite fait tourner un programme (ton site, ton API, ta base).

- Une **image** Docker, c'est le *plan* de la boite.
  - Dedans : fichiers, programmes, reglages de base.
  - Elle ne tourne pas. Elle ne mange pas de memoire.
  - Tu la partages via un **registre** (un grand garage a images).

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/docker-image-vs-conteneur.svg" alt="Schema Docker image versus conteneur" class="schema-inline" width="640" />
  <figcaption>Image = plan. Conteneur = instance. Ne les confonds plus.</figcaption>
</figure>

- Un **conteneur**, c'est une *boite vivante* creee a partir de ce plan.
  - Elle a sa propre memoire, son reseau, sa vie.
  - Tu peux en lancer plusieurs avec la meme image.
  - Tu peux l'arreter, la supprimer, en recreer une autre.

En pratique :

```bash
# Telecharge une image officielle
docker pull nginx:1.27

# Lance un conteneur nomme "web"
docker run --name web -p 8080:80 nginx:1.27
```

Ici, `nginx:1.27` est l'image. `web` est le conteneur qui tourne.

---

## Ou vivent tes images ?

Une image vit dans un **registre** - un entrepot :

- **Docker Hub** : le garage public. Pratique pour commencer.
- **GitHub Container Registry** (`ghcr.io`) : utile si ton code est sur GitHub.
- **Registry prive** : pour tes images internes, la prod, tes clients.

Notation classique :

```text
<registry>/<namespace>/<image>:<tag>
```

Exemples :

- `nginx:1.27` = raccourci pour `docker.io/library/nginx:1.27`
- `ghcr.io/likedevgit/dispycluster:latest`
- `registry.interne.local/clients/mon-projet-api:2.3.1`

Le **tag** (apres le `:`), c'est l'etiquette sur la boite. Evite de ne travailler qu'avec `latest`. C'est comme ecrire "derniere version" sans date.

---

## La vie d'un conteneur

Quelques commandes couvrent 80 % du quotidien :

```bash
# Lister les conteneurs en cours
docker ps

# Lister tous (meme stoppes)
docker ps -a

# Stopper
docker stop web

# Relancer
docker start web

# Supprimer
docker rm web
```

Deux règles d'or :

- Le conteneur est **jetable**. Tu dois pouvoir le jeter et le recreer sans panique.
- Les **donnees importantes** ne vivent pas dans la boite. Elles vont dans un volume, une base externe, un bucket. On detaille ca dans [Docker volumes et reseaux](/blog/articles/docker-volumes-reseaux.html).

---

## Regarder dans une image

Avant de faire confiance a une image, regarde ce qu'elle contient :

```bash
docker image ls
docker history nginx:1.27
docker inspect nginx:1.27
```

Tu verifies :

- la **taille** (grosse image = build et deploiement plus lents),
- l'OS de base (Alpine, Debian, Ubuntu...),
- les **ports** ouverts,
- la commande de demarrage.

---

## Bons reflexes

- **Toujours taguer** : `1.0.0`, `2026-02-21`, `prod`. Pas seulement `latest`.
- **Une image = un role**. Pas de boite magique API + worker + cron. Un service, une image, un conteneur.
- **Pas de secrets dans l'image**. Mots de passe et cles passent par des variables d'environnement ou des fichiers montes.

---

## Pour la suite

Ensuite dans la serie :

1. [Installer Docker proprement](/blog/articles/docker-installation-bonnes-pratiques.html) sur ta machine.
2. Volumes et reseaux pour faire discuter les boites.
3. [Docker Compose](/blog/articles/docker-compose-environnements-local.html) pour tout lancer d'un coup.
4. [Optimiser tes images](/blog/articles/docker-build-optimisation-images.html).
5. [Preparer la prod](/blog/articles/docker-production-registry-securite.html) : registry, tags, securite.

L'objectif : etre a l'aise avec Docker **en solo**, avant de passer a des usines plus grosses.
