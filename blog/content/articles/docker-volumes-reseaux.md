---
title: "Docker : bien utiliser les volumes et les réseaux"
date: 2025-12-11
excerpt: "Connecter tes conteneurs entre eux et gérer les données persistantes avec les volumes et les réseaux Docker, sans te retrouver avec une base de données effacée par erreur."
type: article
tags: [Docker, volumes, réseaux, data, DevOps]
series: docker-serie
series_order: 3
og_image: docker-volumes-reseaux-1200x630.jpg
---

# Docker : bien utiliser les volumes et les réseaux

Lancer `docker run` avec une image publique, c'est sympa. Mais très vite tu as besoin de deux choses :

- **garder les données** (base de données, fichiers d'upload, etc.) même quand tu recrées un conteneur ;
- **faire discuter plusieurs conteneurs entre eux** (API + base, front + API, worker + broker, etc.).

Pour ça, Docker te donne deux outils clés : **les volumes** et **les réseaux**.

---

## Volumes : où vivent tes données

Sans volume, tout ce qui vit dans le système de fichiers du conteneur disparaît dès qu'il est supprimé.

### Types de volumes

En pratique, tu verras surtout :

- **Volumes nommés** : gérés par Docker.
- **Bind mounts** : montage d'un dossier de ta machine hôte dans le conteneur.

```bash
# Volume nommé
docker volume create db-data

docker run -d --name db \
  -v db-data:/var/lib/postgresql/data \
  postgres:16

# Bind mount (développement)
docker run -d --name api \
  -v "$PWD/src":/app/src \
  my-api-image:latest
```

Quelques règles simples :

- Pour la **prod**, privilégie les **volumes nommés** → Docker gère l'emplacement, la portabilité.
- Pour le **dev**, les **bind mounts** sont parfaits pour éditer le code en live.

---

## Inspecter et nettoyer les volumes

```bash
docker volume ls
docker volume inspect db-data
docker volume rm db-data
```

Attention au ménage : supprimer un volume = perdre les données qui sont dedans.  
Sur une base de dev, ce n'est pas grave. Sur une base prod… tu vois l'idée.

---

## Réseaux Docker : faire parler les conteneurs

Par défaut, Docker crée un réseau `bridge`. Tu peux déjà faire :

```bash
docker run -d --name db postgres:16
docker run -d --name api --link db postgres:16
```

Mais la bonne pratique moderne, c'est de créer **ton propre réseau**.

```bash
docker network create mon-app-net

docker run -d --name db --network mon-app-net postgres:16
docker run -d --name api --network mon-app-net my-api-image:latest
```

Dans ce réseau :

- Le conteneur `api` peut joindre la base via `db:5432`.  
- Tu n'as pas besoin d'exposer le port 5432 vers l'extérieur pour qu'ils se parlent.

---

## Ports vs réseaux : ne pas tout exposer

On distingue :

- **Port exposé vers l'hôte** : `-p 8080:80` → tu ouvres 8080 sur ta machine.
- **Port interne au réseau** : `--network mon-app-net` → seulement visible entre conteneurs.

Bonne pratique :

- N'ouvre vers l'extérieur que ce qui est vraiment nécessaire (souvent le reverse proxy ou l'API publique).
- Laisse les bases, brokers, workers **cachés** derrière le réseau Docker.

---

## Exemple concret : API + base de données

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

- L'extérieur parle à l'API via `localhost:8080`.
- L'API parle à la base via `postgres:5432` dans le réseau `app-net`.

---

## Volumes et réseaux avec docker-compose

Dans le prochain article, on utilisera **docker-compose** pour décrire ce genre de stack dans un fichier YAML :

- services (`api`, `db`, `redis`, etc.)  
- réseaux (`frontend`, `backend`)  
- volumes (`db-data`, `uploads`, etc.).

L'idée : pouvoir tout lancer/arrêter avec un simple `docker compose up` / `down`.
