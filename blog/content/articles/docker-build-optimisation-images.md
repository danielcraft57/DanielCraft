---
title: "Optimiser tes Dockerfile et la taille de tes images"
date: 2024-11-19
excerpt: "Réduire la taille de tes images Docker, accélérer les builds et éviter les mauvaises surprises en prod grâce à quelques patterns simples."
type: article
tags: [Docker, Dockerfile, optimisation, images]
series: docker-serie
series_order: 5
og_image: docker-build-optimisation-1200x630.jpg
---

# Optimiser tes Dockerfile et la taille de tes images

Une image Docker trop grosse, c'est :

- des builds lents,
- des déploiements lents,
- des temps de démarrage parfois pénibles,
- plus de surface d'attaque côté sécurité.

Bonne nouvelle : avec quelques réflexes, tu peux déjà faire beaucoup mieux que les Dockerfile générés à l'arrache.

---

## Choisir une bonne image de base

Premier levier : le **FROM**.

```dockerfile
FROM node:22-alpine
```

Comparé à un `node:22` classique (basé sur Debian), l'image Alpine est beaucoup plus légère.  
Mais attention :

- Alpine utilise `musl` et non `glibc` → certaines libs natives peuvent être plus chiantes à compiler,
- pour des applis très complexes, tu peux préférer une `-slim` (Debian allégée).

Règle simple :

- tente d'abord `*-alpine` ou `*-slim`,
- si tu bloques sur des dépendances natives, reviens sur une image de base plus complète.

---

## Multistage builds : builder d'un côté, runner de l'autre

Patron classique :

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

Idée :

- la phase `build` contient tout ce qu'il faut pour compiler (devDependencies, outils, etc.),
- la phase `runtime` ne reçoit que le code compilé + les deps nécessaires à l'exécution.

Résultat : image plus petite, et en général plus sécurisée.

---

## Éviter les caches et fichiers inutiles

Quelques réflexes :

- Ajoute un `.dockerignore` :

```text
node_modules
.git
.cache
dist
Dockerfile*
docker-compose*.yml
```

- Nettoie les caches des gestionnaires de paquets si tu dois installer des dépendances :

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

## Minimiser le nombre de layers

Chaque `RUN`, `COPY`, `ADD` crée un layer. Ce n'est pas dramatique en soi, mais tu peux regrouper des commandes qui vont ensemble :

```dockerfile
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential python3 \
 && rm -rf /var/lib/apt/lists/*
```

Plutôt que :

```dockerfile
RUN apt-get update
RUN apt-get install -y build-essential python3
RUN rm -rf /var/lib/apt/lists/*
```

---

## Vérifier la taille et le contenu

Commande simple pour voir la taille de tes images :

```bash
docker image ls | sort -k 7 -h
```

Pour inspecter une image :

```bash
docker history mon-image:1.0.0
docker inspect mon-image:1.0.0
```

Tu peux aussi lancer une image en shell et regarder ce qu'il y a dedans :

```bash
docker run -it --rm mon-image:1.0.0 sh
```

---

## Exemple : API Node.js optimisée

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

Ce Dockerfile est déjà correct pour beaucoup de projets internes.

---

## Ce qui reste à voir

Dans le dernier article de la série Docker, on parlera de :

- registry privé,
- stratégie de tags (prod/staging/feature),
- sécurité minimale (utilisateur non root, secrets),
- comment préparer sereinement le terrain pour un futur déploiement sur Kubernetes.
