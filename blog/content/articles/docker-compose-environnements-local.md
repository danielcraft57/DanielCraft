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

Tu sais lancer un conteneur. Bien. Maintenant tu veux plusieurs boîtes ensemble : base, API, front, worker… Lancer tout ça à la main avec `docker run`, c’est comme préparer un repas en ouvrant chaque tiroir un par un.

**Docker Compose**, c’est la recette complète. Un fichier. Une commande. Tout démarre.

Si les [volumes et réseaux](/blog/articles/docker-volumes-reseaux.html) te sont encore flous, lis-les d’abord. Compose s’appuie dessus. Pour l’installation et les réflexes de base, vois aussi [Docker : installation et bonnes pratiques](/blog/articles/docker-installation-bonnes-pratiques.html).

---

## Le principe

Tu décris ton garage dans `docker-compose.yml` :

- services (nom, image, ports, volumes, variables),
- réseaux,
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

`up` = allume tout. `down` = éteint les conteneurs (les volumes nommés restent, sauf si tu ajoutes `-v`).

L’intérêt pour une équipe : le même fichier dans le repo = le même environnement pour tout le monde. Moins de « chez moi ça marche ».

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

Avec ça :

- `db` et `api` partagent le réseau `app-net`,
- la base garde ses données dans `db-data`,
- l’API est sur `http://localhost:8080`.

Le nom du service (`db`) sert d’adresse DNS interne. Comme un prénom dans la pièce : l’API parle à `db:5432`, pas à `localhost` (qui, depuis le conteneur `api`, pointerait… vers lui-même).

### Exemple concret du quotidien

Tu clones le repo, tu lances `docker compose up -d`, tu ouvres l’API. Un collègue fait pareil le lendemain. Même Postgres, mêmes ports, même `.env` partagé (sans secrets de prod). Le onboarding passe de « deux heures de config » à « dix minutes ».

Tu peux enrichir la stack sans changer d’outil : un Redis pour le cache, un worker pour les jobs, un mailhog pour tester les e-mails. Chaque service = un bloc dans le même fichier. Compose les relie sur le réseau commun.

---

## Healthcheck : attendre que la base soit vraiment prête

`depends_on: [db]` dit seulement « démarre `db` avant `api` ». Pas « Postgres accepte déjà les connexions ».

Exemple de healthcheck Postgres :

```yaml
db:
  image: postgres:16
  healthcheck:
    test: ["CMD-SHELL", "pg_isready -U postgres"]
    interval: 5s
    timeout: 5s
    retries: 10
  # ...

api:
  depends_on:
    db:
      condition: service_healthy
```

Sans ça, tu as le classique : premier `compose up` qui plante, second qui « marche » — parce que la base a fini de démarrer entre-temps. Frustrant, et trompeur pour les nouveaux.

---

## Commandes de base

```bash
# Mode attaché (tu vois les logs)
docker compose up

# Arrière-plan
docker compose up -d

# Logs en direct
docker compose logs -f
docker compose logs -f api

# Stopper (garde les volumes)
docker compose down

# Tout supprimer (conteneurs + volumes)
docker compose down -v
```

`down -v`, c’est le grand ménage. Sur une base utile, réfléchis deux fois : tu perds les données du volume.

Autres commandes utiles :

```bash
docker compose ps
docker compose exec api sh
docker compose restart api
```

---

## Plusieurs fichiers Compose

Tu peux avoir :

- un `docker-compose.yml` de base,
- un `docker-compose.override.yml` pour le **dev** (montage du code, outils en plus).

Compose fusionne les deux par défaut.

```bash
docker compose -f docker-compose.yml -f docker-compose.override.yml up
```

Exemple d’override :

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

En prod, tu n’ajoutes pas pgAdmin. En local, c’est pratique pour inspecter les tables.

### Pièges fréquents

- **`depends_on` ≠ « la base est prête »** : Postgres peut encore démarrer quand l’API tente de se connecter. Ajoute un healthcheck + `condition: service_healthy`, ou un petit retry côté app.
- **Ports déjà pris** sur la machine hôte (`5432`, `8080`) → change le mapping `"5433:5432"`.
- **Secrets en dur** dans le YAML versionné : préfère un `.env` (non committe pour la prod) ou des fichiers d’exemple `.env.example`.

---

## Variables d’environnement

Compose lit automatiquement un fichier `.env` à côté du YAML. Tu y mets les ports, mots de passe locaux, noms de bases — sans les coller en dur dans le fichier versionné.

Bon réflexe d’équipe :

- committer un `.env.example` (valeurs fictives, commentaires) ;
- ignorer `.env` dans Git (sauf si c’est vraiment du « local only » sans secret) ;
- documenter dans le README : « copie `.env.example` → `.env`, puis `compose up` ».

Quand tu monteras une vraie [pipeline CI/CD](/blog/articles/ci-cd-fondamentaux-pipelines.html), les secrets ne seront plus dans un `.env` local : vault, variables CI, secrets Kubernetes. Compose local reste le bac à sable.

---

## Bons réflexes

- Pas de tag `latest` partout. Tags clairs (`postgres:16`, `redis:7.2`).
- Un service = une responsabilité (pas « tout-en-un » opaque).
- Versionne les fichiers Compose dans le repo : toute l’équipe a le **même** environnement.
- Rebuild ciblé quand tu changes le Dockerfile : `docker compose build api && docker compose up -d api`.
- Pour la vraie prod, Compose peut rester une étape. Un orchestrateur plus gros ([Kubernetes](/blog/articles/kubernetes-concepts-pods-nodes.html)…) prendra souvent le relais. Avant ça, [optimise tes images](/blog/articles/docker-build-optimisation-images.html) et [prépare registry + sécu](/blog/articles/docker-production-registry-securite.html).

### Checklist environnement local

- [ ] Un `docker compose up -d` suffit pour démarrer
- [ ] Un `.env.example` documente les variables
- [ ] Healthcheck sur la base (ou retry côté app)
- [ ] Les volumes de données sont nommés
- [ ] Les tags d’images sont figés
- [ ] Le README explique `up` / `down` / `logs` / `down -v`

---

## En résumé

Compose, c’est la **liste de courses** de ton environnement. Tu écris une fois. Tu lances souvent. Moins d’erreurs, moins de divergences entre machines — et une base saine avant de parler pipeline ou cluster.
