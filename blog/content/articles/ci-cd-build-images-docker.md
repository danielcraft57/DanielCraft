---
title: "CI/CD : fabriquer et envoyer une image Docker"
date: 2025-03-11
excerpt: "Construire la meme boite a chaque fois, la taguer, la pousser dans un registry."
type: article
tags: [CI/CD, Docker, images, registry, DevOps]
series: ci-cd-serie
series_order: 3
og_image: ci-cd-docker-images-1200x630.jpg
---

# CI/CD : fabriquer et envoyer une image Docker

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-docker-build.svg" alt="Schema build et push d'image Docker en CI" class="schema-inline" width="640" />
  <figcaption>Code, Dockerfile, build, tag, registry.</figcaption>
</figure>

Si tu déploies une API ou un service web, ton artefact le plus propre est souvent une **image Docker**. Elle encapsule le code, les dépendances et la configuration runtime dans un format reproductible. Mais un build mal configuré en CI devient vite lent, instable et impossible à auditer. Voici une méthode simple pour builder, taguer et pousser proprement.

## La règle d'or : une image versionnée et traçable

Tu dois pouvoir répondre à la question : « Quelle version tourne en prod ? » Si ta seule réponse est `latest`, tu as un problème.

Tags utiles à combiner :

- **`sha-<commit>`** ou directement le SHA Git : traçabilité parfaite, lien direct commit → image
- **`1.2.3`** : version sémantique pour les releases officielles
- **`staging`** / **`prod`** : alias pratiques, mais jamais seuls (ils écrasent l'historique)

En CI, tag systématiquement avec le SHA du commit. En release, ajoute le tag sémantique. Le cluster référence un tag immuable, pas un alias mouvant.

## Multi-stage builds : images légères et sécurisées

Un Dockerfile mono-stage inclut souvent les outils de compilation, les sources et les devDependencies. Résultat : une image de 800 Mo alors que ton binaire fait 20 Mo.

Le multi-stage compile d'un côté, exécute de l'autre :

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
USER node
CMD ["node", "dist/main.js"]
```

Bénéfices :

- Image finale plus petite → pull plus rapide en déploiement
- Moins de packages installés → surface d'attaque réduite
- Séparation claire build / runtime

Adapte le pattern à ton stack : Go, Rust, Python, Java — le principe reste identique.

## Cache Docker : gagner du temps sans tricher

L'ordre des instructions Dockerfile impacte directement le cache. Règle simple :

1. Copier d'abord les fichiers de dépendances (`package.json`, `go.mod`, `requirements.txt`)
2. Installer les dépendances
3. Copier le reste du code source

Ainsi, un changement dans un fichier métier ne relance pas l'installation de toutes les dépendances. En CI, active aussi le cache de layers (GitHub Actions `cache-to`/`cache-from`, GitLab `--cache-from`).

Évite `COPY . .` en première instruction : chaque commit invalide tout le cache.

## Registry : où pousser et comment sécuriser

Choix courants :

- **Docker Hub** : simple, limites sur le plan gratuit
- **GHCR** (`ghcr.io`) : intégré à GitHub, pratique avec Actions
- **GitLab Container Registry** : intégré à GitLab CI
- **Registry privé** (Harbor, ECR, ACR, GCR) : contrôle total, conformité entreprise

L'important : que ton cluster ou ta VM de prod puisse **pull** l'image. Configure un `imagePullSecret` Kubernetes si le registry est privé. Authentifie la CI avec un token à portée limitée (push uniquement, pas admin).

## Pipeline CI type : build, scan, push

Étapes recommandées :

1. **Build** l'image avec le tag SHA
2. **Scan** avec Trivy ou Grype (vulnérabilités CVE)
3. **Push** vers le registry si le scan passe (ou avec seuil de sévérité configurable)
4. **Référencer** le tag dans le manifest de déploiement (GitOps ou kubectl)

Ne rebuild pas en prod. L'image qui tourne est exactement celle testée en CI. C'est le principe « build once, deploy everywhere ».

## Bonnes pratiques complémentaires

- Utilise des images de base officielles et mises à jour (`alpine`, `distroless`)
- Exécute le conteneur avec un utilisateur non-root (`USER node`, `USER 1000`)
- Ajoute un `.dockerignore` pour exclure `node_modules`, `.git`, fichiers de test
- Pinned les versions de base (`node:22.4-alpine`, pas `node:latest`)

## Conclusion

Ton pipeline doit produire une image reproductible, versionnée, scannée et poussée au registry — prête à être déployée sans rebuild. Tag avec le SHA, multi-stage pour la légèreté, cache intelligent pour la vitesse. Pour gérer les credentials de registry et les variables sensibles en CI, voir le guide sur les [secrets et variables d'environnement en CI/CD](/blog/articles/ci-cd-secrets-variables-environnement.html).
