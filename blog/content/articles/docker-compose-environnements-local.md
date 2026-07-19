---
title: "Docker Compose : plusieurs boîtes qui travaillent ensemble"
date: 2024-11-14
excerpt: "Un fichier pour lancer site, base et cache comme une petite équipe locale."
type: article
tags: [Docker, docker-compose, environnement, dev]
series: docker-serie
series_order: 4
og_image: docker-compose-1200x630.jpg
---

# [Docker](/blog/articles/docker-fondamentaux-images-conteneurs.html) Compose : plusieurs boîtes qui travaillent ensemble

Tu sais lancer un conteneur. Bien. Maintenant tu veux plusieurs boites ensemble : base, API, front, worker... Lancer tout ca a la main avec `docker run`, c'est comme preparer un repas en ouvrant chaque tiroir un par un.

**Docker Compose**, c'est la recette complete. Un fichier. Une commande. Tout demarre.

Si les [volumes et reseaux](/blog/articles/docker-volumes-reseaux.html) te sont encore flous, lis-les d'abord. Compose s'appuie dessus.

---

## Le principe

Tu decries ton garage dans `docker-compose.yml` :

- services (nom, image, ports, volumes, variables),
- reseaux,
- volumes.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/docker-compose-stack.svg" alt="Schema d'une stack Docker Compose" class="schema-inline" width="640" />
  <figcaption>Compose aligne services, reseaux et volumes sur un seul fichier.</figcaption>
</figure>

Puis :

```bash
docker compose up
docker compose down
```

`up` = allume tout. `down` = eteint les conteneurs (les volumes nommes restent, sauf si tu ajoutes `-v`).

---

## Exemple : API + Postgres

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

Avec ca :

- `db` et `api` partagent le reseau `app-net`,
- la base garde ses donnees dans `db-data`,
- l'API est sur `http://localhost:8080`.

Le nom du service (`db`) sert d'adresse. Comme un prenom dans la piece.

---

## Commandes de base

```bash
# Mode attache (tu vois les logs)
docker compose up

# Arriere-plan
docker compose up -d

# Logs en direct
docker compose logs -f

# Stopper (garde les volumes)
docker compose down

# Tout supprimer (conteneurs + volumes)
docker compose down -v
```

`down -v`, c'est le grand menage. Sur une base de prod, reflechis deux fois.

---

## Plusieurs fichiers Compose

Tu peux avoir :

- un `docker-compose.yml` de base,
- un `docker-compose.override.yml` pour le **dev** (montage du code, outils en plus).

Compose fusionne les deux par defaut.

```bash
docker compose -f docker-compose.yml -f docker-compose.override.yml up
```

Exemple d'override :

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

En prod, tu n'ajoutes pas pgAdmin. En local, c'est pratique.

---

## Bons reflexes

- Pas de `latest` partout. Tags clairs.
- Variables communes dans un `.env` que Compose charge.
- Versionne les fichiers compose dans le repo. Toute l'equipe a le **meme** environnement.
- Pour la vraie prod, Compose peut rester une etape. Un orchestrateur plus gros (Kubernetes...) prendra souvent le relais. Avant ca, [optimise tes images](/blog/articles/docker-build-optimisation-images.html) et [prepare registry + secu](/blog/articles/docker-production-registry-securite.html).

---

## En resume

Compose, c'est la **liste de courses** de ton environnement. Tu ecris une fois. Tu lances souvent. Moins d'erreurs, moins de "chez moi ca marche".
