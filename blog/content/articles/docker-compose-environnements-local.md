---
title: "Docker Compose : un environnement complet en une commande"
date: 2024-11-14
excerpt: "Assembler plusieurs services Docker (API, base, front, worker) dans un fichier docker-compose pour lancer un environnement complet de dev en une seule commande."
type: article
tags: [Docker, docker-compose, environnement, dev]
series: docker-serie
series_order: 4
og_image: docker-compose-1200x630.jpg
---

# Docker Compose : un environnement complet en une commande

Une fois que tu maîtrises les conteneurs seuls, tu veux vite **enchaîner plusieurs services** :

- base de données,
- API,
- front,
- worker de fond,
- parfois un outil type pgAdmin, RedisInsight, etc.

Lancer tout ça à la main avec `docker run`, c'est pénible. C'est là que **docker-compose** devient ton meilleur ami.

---

## Le principe

Tu décris ton environnement dans un fichier `docker-compose.yml` :

- services (nom, image, ports, volumes, variables d'env),
- réseaux,
- volumes.

Puis tu fais simplement :

```bash
docker compose up
docker compose down
```

---

## Exemple : API + Postgres

Un exemple minimal mais déjà utile :

```yaml
version: "3.9"

services:
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: appdb
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - app-net

  api:
    build: ./api
    environment:
      DATABASE_URL: postgresql://postgres:secret@db:5432/appdb
    ports:
      - "8080:3000"
    depends_on:
      - db
    networks:
      - app-net

volumes:
  db-data:

networks:
  app-net:
```

Avec ça :

- `db` et `api` partagent le réseau `app-net`,
- la base garde ses données dans `db-data`,
- l'API est accessible sur `http://localhost:8080`.

---

## Commandes de base

```bash
# Lancer en mode attaché
docker compose up

# Lancer en arrière-plan
docker compose up -d

# Voir les logs
docker compose logs -f

# Stopper et supprimer les conteneurs (mais pas les volumes)
docker compose down

# Tout supprimer (conteneurs + volumes nommés)
docker compose down -v
```

---

## Gérer plusieurs fichiers de compose

Tu peux avoir :

- un `docker-compose.yml` générique,
- un `docker-compose.override.yml` pour le dev (montage de code, outils en plus).

Docker compose fusionne les deux par défaut.

```bash
docker compose -f docker-compose.yml -f docker-compose.override.yml up
```

Exemple de `docker-compose.override.yml` :

```yaml
services:
  api:
    volumes:
      - ./api:/app
    environment:
      DEBUG: "1"

  pgadmin:
    image: dpage/pgadmin4
    ports:
      - "8081:80"
    environment:
      PGADMIN_DEFAULT_EMAIL: "dev@example.com"
      PGADMIN_DEFAULT_PASSWORD: "secret"
    depends_on:
      - db
    networks:
      - app-net
```

---

## Bonnes pratiques avec docker-compose

- N'utilise pas `latest` partout : garde des tags d'images explicites.
- Regroupe les variables communes dans un `.env` que compose peut charger.
- Versionne les fichiers compose dans le repo → tout le monde a le même environnement.
- Pour la prod, compose peut être une étape, mais **Kubernetes** ou un autre orchestrateur prendra souvent le relais.

---

## Transition vers Kubernetes

Le gros avantage de bien structurer tes fichiers docker-compose, c'est que :

- les **services** correspondent assez naturellement aux **Deployments**,
- les **networks** à des **Services** ou simplement au réseau du cluster,
- les **volumes** à des **PersistentVolumeClaims**.

Dans la série Kubernetes, on repartira de ce type de stack pour la migrer proprement vers un cluster.
