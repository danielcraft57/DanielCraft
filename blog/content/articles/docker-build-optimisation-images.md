---
title: "Docker : des images plus légères et plus rapides"
date: 2024-11-19
excerpt: "Ordre du Dockerfile, cache, multi-stage : construire mieux sans se compliquer."
type: article
tags: [Docker, Dockerfile, optimisation, images]
series: docker-serie
series_order: 5
og_image: docker-build-optimisation-1200x630.jpg
---

# [Docker](/blog/articles/docker-fondamentaux-images-conteneurs.html) : des images plus légères et plus rapides

Une image Docker trop grosse, c'est un **camion surcharge**. Ca met du temps a demarrer, a voyager, a se deplier. Et il y a plus de place pour les surprises de secu.

Bonne nouvelle : avec quelques reflexes, tu alleges deja beaucoup. Tu as vu [Compose](/blog/articles/docker-compose-environnements-local.html) ? Maintenant on soigne la **recette** (le Dockerfile).

---

## Choisir une bonne image de base

Premier levier : le `FROM`. C'est le fond de ta boite.

```dockerfile
FROM node:22-alpine
```

Compare a un `node:22` classique (Debian), Alpine est bien plus leger. Mais attention :

- Alpine utilise `musl` (pas `glibc`) - certaines libs natives ralent.
- Pour des applis complexes, une image `-slim` (Debian allégée) peut etre plus simple.

Regle :

- tente d'abord `*-alpine` ou `*-slim`,
- si ca bloque, reviens a une base plus complete.

---

## Multistage : cuisiner d'un cote, servir de l'autre

Idee : une cuisine salee pour **construire**, une assiette propre pour **servir**.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/docker-build-layers.svg" alt="Schema optimisation build Docker layers cache" class="schema-inline" width="640" />
  <figcaption>Deps avant le code, multi-stage a la fin : images plus petites et plus rapides.</figcaption>
</figure>

```dockerfile
FROM node:22-alpine AS build
WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM node:22-alpine AS runtime
WORKDIR /app

COPY --from=build /app/dist ./dist
COPY package*.json ./
RUN npm ci --omit=dev

CMD ["node", "dist/main.js"]
```

- La phase `build` a tous les outils (devDependencies, compilateurs...).
- La phase `runtime` ne recoit que le code pret + les deps utiles pour tourner.

Resultat : image plus petite. Souvent plus sure aussi.

---

## Ne pas mettre le desordre dans la boite

- Ajoute un `.dockerignore` :

```text
node_modules
.git
.cache
dist
Dockerfile*
docker-compose*.yml
```

Sans ca, tu copies ton `.git` et tes caches dans l'image. Inutile. Lourd.

- Nettoie les caches de paquets :

```dockerfile
RUN apk add --no-cache build-base python3
```

Sur Debian/Ubuntu :

```dockerfile
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential python3 \
 && rm -rf /var/lib/apt/lists/*
```

---

## Moins de couches inutiles

Chaque `RUN`, `COPY`, `ADD` cree une **couche** (un etage dans le camion). Ce n'est pas grave, mais regroupe ce qui va ensemble :

```dockerfile
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential python3 \
 && rm -rf /var/lib/apt/lists/*
```

Plutot que trois `RUN` separes. Et copie d'abord `package*.json` : Docker reutilise le cache des deps si ton code change.

---

## Verifier la taille

```bash
docker image ls | sort -k 7 -h
docker history mon-image:1.0.0
docker inspect mon-image:1.0.0
```

Pour ouvrir la boite et regarder :

```bash
docker run -it --rm mon-image:1.0.0 sh
```

---

## Exemple API Node optimisee

```dockerfile
FROM node:22-alpine AS build
WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM node:22-alpine AS runtime
WORKDIR /app

ENV NODE_ENV=production

COPY --from=build /app/dist ./dist
COPY package*.json ./
RUN npm ci --omit=dev

EXPOSE 3000
CMD ["node", "dist/main.js"]
```

Ce Dockerfile convient deja a beaucoup de projets internes.

---

## Suite

Dernier volet Docker : [registry, tags et securite pour la prod](/blog/articles/docker-production-registry-securite.html). Des images legeres, c'est bien. Des images **propres et partagees** proprement, c'est mieux.
