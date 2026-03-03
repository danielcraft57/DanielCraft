---
title: "CI/CD : builder et pousser des images Docker (tags, cache, multi-stage)"
date: 2026-02-06
excerpt: "Comment construire des images Docker en CI sans exploser les temps de build : stratégie de tags, cache, multi-stage builds et registry."
type: article
tags: [CI/CD, Docker, images, registry, DevOps]
series: ci-cd-serie
series_order: 3
og_image: ci-cd-docker-images-1200x630.jpg
---

# CI/CD : builder et pousser des images Docker (tags, cache, multi-stage)

Si tu déploies une API, ton artefact le plus propre est souvent une **image Docker**.

Mais attention : un mauvais build d'image en CI peut devenir :

- lent,
- instable,
- impossible à reproduire.

On va poser une méthode simple.

---

## La règle d'or : une image versionnée

Tu veux pouvoir dire :

"la prod tourne sur l'image `1.2.3`"

Donc on évite de ne publier que `latest`.

Tags utiles :

- `sha-<commit>` (traçabilité parfaite)
- `1.2.3` (version sémantique)
- `prod` / `staging` (alias pratique)

---

## Multi-stage builds (toujours)

On compile d'un côté, on exécute de l'autre.

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
CMD ["node", "dist/main.js"]
```

Résultat :

- image plus petite,
- moins de surface d'attaque,
- plus rapide à déployer.

---

## Cache : gagner du temps sans tricher

Le secret, c'est l'ordre des COPY.

1) Copier les manifests de deps  
2) Installer deps  
3) Copier le reste du code

Comme ça, si tu modifies un fichier métier, Docker ne réinstalle pas toutes les deps.

---

## Registry : où tu pushes

Tu peux pousser :

- sur Docker Hub,
- sur GHCR (`ghcr.io`),
- sur un registry privé.

L'important : que ton cluster (ou ta VM) puisse tirer l'image.

---

## À la fin, l'objectif

Ton pipeline doit sortir une image :

- reproductible,
- versionnée,
- poussée au registry,
- prête à être déployée (sans rebuild).

Dans l'article suivant, on attaque un sujet critique : **les secrets et variables d'environnement** en CI/CD (sans fuite).

