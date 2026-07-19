---
title: "Docker : garder ses fichiers et connecter les boîtes"
date: 2024-11-12
excerpt: "Volumes pour persister, réseaux pour faire parler les services — sans magie noire."
type: article
tags: [Docker, volumes, réseaux, data, DevOps]
series: docker-serie
series_order: 3
og_image: docker-volumes-reseaux-1200x630.jpg
---

# Docker : garder ses fichiers et connecter les boîtes

Lancer `docker run` avec une image publique, c'est sympa. Mais tres vite tu as besoin de deux choses :

- **garder les donnees** (base, fichiers uploades) meme si tu recrees le conteneur ;
- **faire discuter** plusieurs boites entre elles (API + base, front + API...).

Docker te donne deux outils : les **volumes** et les **reseaux**. Si tu as rate les bases, reviens a [images et conteneurs](/blog/articles/docker-fondamentaux-images-conteneurs.html).

---

## Volumes : le tiroir a souvenirs

Sans volume, tout ce qui vit dans le conteneur disparait quand tu le supprimes. C'est comme jeter une boite avec les photos dedans.

### Deux types utiles

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/docker-volumes-reseaux.svg" alt="Schema Docker volumes et reseaux" class="schema-inline" width="640" />
  <figcaption>Volumes pour persister, reseaux pour composer — pas l'inverse.</figcaption>
</figure>

- **Volume nomme** : Docker garde le tiroir pour toi.
- **Bind mount** : tu ouvres une porte entre un dossier de ton PC et le conteneur.

```bash
# Volume nomme
docker volume create db-data

docker run -d --name db \
  -v db-data:/var/lib/postgresql/data \
  postgres:16

# Bind mount (dev)
docker run -d --name api \
  -v "$PWD/src":/app/src \
  my-api-image:latest
```

Regles simples :

- En **prod** : privilegie les volumes nommes. Docker gere l'emplacement. Plus portable.
- En **dev** : les bind mounts sont parfaits. Tu modifies le code, le conteneur voit le changement.

---

## Inspecter et nettoyer

```bash
docker volume ls
docker volume inspect db-data
docker volume rm db-data
```

Attention : supprimer un volume = **perdre les donnees** dedans. Sur une base de test, ok. Sur la prod... tu vois l'idee.

---

## Reseaux : faire parler les boites

Par defaut, Docker cree un reseau `bridge`. La bonne pratique : creer **ton propre reseau**, comme une piece ou seules tes boites se parlent.

```bash
docker network create mon-app-net

docker run -d --name db --network mon-app-net postgres:16
docker run -d --name api --network mon-app-net my-api-image:latest
```

Dans ce reseau :

- `api` joint la base via `db:5432` (le nom du conteneur = l'adresse).
- Tu n'as pas besoin d'ouvrir le port 5432 vers l'exterieur pour qu'ils se parlent.

---

## Ports vs reseaux

Deux idees differentes :

- **Port vers ta machine** : `-p 8080:80` - tu ouvres la fenetre 8080 sur ton PC.
- **Port dans le reseau** : visible seulement entre conteneurs.

Bonne pratique :

- N'ouvre vers l'exterieur que le strict necessaire (souvent l'API ou le reverse proxy).
- Laisse bases, brokers, workers **caches** derriere le reseau Docker.

---

## Exemple : API + base

```bash
docker network create app-net

docker run -d --name postgres \
  --network app-net \
  -e POSTGRES_PASSWORD=secret \
  -v db-data:/var/lib/postgresql/data \
  postgres:16

docker run -d --name api \
  --network app-net \
  -e DATABASE_URL=postgresql://postgres:secret@postgres:5432/appdb \
  -p 8080:3000 \
  my-api-image:latest
```

- L'exterieur parle a l'API via `localhost:8080`.
- L'API parle a la base via `postgres:5432` dans `app-net`.
- Les donnees vivent dans le volume `db-data`.

---

## Suite : tout ca dans un fichier

Ecrire ces commandes a la main, ca lasse. Avec [Docker Compose](/blog/articles/docker-compose-environnements-local.html), tu decries services, reseaux et volumes dans un YAML. Puis : `docker compose up`. Un seul geste pour tout le garage.
