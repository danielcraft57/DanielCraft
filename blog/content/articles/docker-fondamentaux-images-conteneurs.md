---
title: "Docker : comprendre les images et les conteneurs"
date: 2024-11-05
excerpt: "Les bases indispensables de Docker : différence entre image et conteneur, registres, cycle de vie et premiers réflexes pour travailler proprement."
type: article
tags: [Docker, conteneurs, images, DevOps, fondamentaux]
series: docker-serie
series_order: 1
og_image: docker-fondamentaux-1200x630.jpg
---

# Docker : comprendre les images et les conteneurs

Docker est partout, mais beaucoup l'utilisent comme une boîte noire. Si tu veux aller plus loin (cluster, Kubernetes, CI/CD), tu dois être à l'aise avec les deux briques de base : **l'image** et le **conteneur**.

L'idée de cette première partie est simple : poser des bases solides, sans jargon inutile.

---

## Image vs conteneur : la métaphore simple

On peut voir Docker comme un système de fabrication et d'exécution de petites machines logicielles.

- **Une image** Docker, c'est le *plan figé* de la machine.  
  - Contient le système de fichiers, les binaires, les dépendances, la config par défaut.  
  - Ne tourne pas, ne consomme rien.  
  - Versionnée et partageable via un registre (Docker Hub, GitHub Container Registry, registry privé).

- **Un conteneur**, c'est *une instance vivante* de cette image.  
  - A son propre PID, sa mémoire, son réseau, son cycle de vie.  
  - Peut avoir un état (logs, fichiers écrits localement, etc.).  
  - On peut en lancer plusieurs à partir d'une même image.

En pratique :

```bash
# Télécharge une image officielle
docker pull nginx:1.27

# Lance un conteneur nommé "web"
docker run --name web -p 8080:80 nginx:1.27
```

Ici, `nginx:1.27` est l'image, `web` est le conteneur en cours d'exécution.

---

## Registres d'images : où vivent tes images

Une image vit dans un **registre** :

- **Docker Hub** (`docker.io`) : public par défaut, pratique pour les images open source.
- **GitHub Container Registry** (`ghcr.io`) : pratique si tu as déjà tout ton code sur GitHub.
- **Registry privé** (Harbor, GitLab, registry maison) : pour les images internes, prod, clients, etc.

Notation classique :

```text
<registry>/<namespace>/<image>:<tag>
```

Exemples :

- `nginx:1.27` → raccourci pour `docker.io/library/nginx:1.27`
- `ghcr.io/likedevgit/dispycluster:latest`
- `registry.interne.local/clients/mon-projet-api:2.3.1`

---

## Cycle de vie d'un conteneur

Quelques commandes suffisent pour couvrir 80 % de ce que tu fais au quotidien.

```bash
# Lister les conteneurs en cours
docker ps

# Lister tous les conteneurs (y compris stoppés)
docker ps -a

# Stopper un conteneur
docker stop web

# Relancer un conteneur stoppé
docker start web

# Supprimer un conteneur
docker rm web
```

Points importants :

- **Le conteneur est jetable** : on doit pouvoir le supprimer et le recréer sans crise de panique.
- **L'état persistant** (données métiers) doit vivre ailleurs : volume Docker, base externe, bucket S3, etc.

---

## Inspection rapide d'une image

Avant de faire confiance aveuglément à une image, regarde ce qu'elle contient.

```bash
docker image ls
docker history nginx:1.27
docker inspect nginx:1.27
```

Tu peux vérifier :

- la **taille** (images énormes = temps de build et de déploiement plus longs),
- l'**OS de base** (Debian, Alpine, Ubuntu, distroless),
- les **ports** exposés,
- la **commande d'entrée** (`CMD`, `ENTRYPOINT`).

---

## Bonnes pratiques de base

- **Toujours taguer tes images**  
  Évite de ne travailler qu'avec `latest`. Utilise des tags clairs : `1.0.0`, `2026-02-21`, `prod`, `staging`.

- **Une image = un rôle clair**  
  Pas de "grosse boîte" qui fait API + worker + cron dans le même conteneur.  
  Tu veux du découpage : 1 service = 1 image = 1 conteneur (ou plusieurs instances).

- **Évite de stocker des secrets dans l'image**  
  Mots de passe, clés API, certificats → passent par les variables d'environnement, fichiers montés, secrets Kubernetes, etc.

---

## Pour la suite de la série

Dans les prochains articles, on va :

1. Installer Docker proprement sur un poste de dev (Linux, macOS, Windows WSL).  
2. Gérer les **volumes** et les **réseaux** pour que tes conteneurs discutent entre eux.  
3. Orchestrer un petit stack avec **docker-compose**.  
4. Optimiser tes **Dockerfile** pour réduire la taille et le temps de build.  
5. Préparer la prod : registry privé, sécurité minimale, stratégie de tags.

L’objectif : que tu sois totalement à l’aise avec Docker en solo avant de passer à Kubernetes.

