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

Lancer `docker run` avec une image publique, c’est sympa. Mais très vite tu as besoin de deux choses :

- **garder les données** (base, fichiers uploadés) même si tu recrées le conteneur ;
- **faire discuter** plusieurs boîtes entre elles (API + base, front + API…).

Docker te donne deux outils : les **volumes** et les **réseaux**. Si tu as raté les bases, reviens à [images et conteneurs](/blog/articles/docker-fondamentaux-images-conteneurs.html). Ici, on reste concret : commandes, règles simples, un mini scénario API + Postgres.

---

## Volumes : le tiroir à souvenirs

Sans volume, tout ce qui vit dans le système de fichiers du conteneur disparaît quand tu le supprimes. C’est comme jeter une boîte avec les photos dedans : la boîte neuve est vide.

### Deux types utiles

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/docker-volumes-reseaux.svg" alt="Schema Docker volumes et reseaux" class="schema-inline" width="640" />
  <figcaption>Volumes pour persister, reseaux pour composer — pas l'inverse.</figcaption>
</figure>

- **Volume nommé** : Docker garde le tiroir pour toi (emplacement géré par Docker).
- **Bind mount** : tu ouvres une porte entre un dossier de ton PC et un chemin dans le conteneur.

```bash
# Volume nommé
docker volume create db-data

docker run -d --name db \
  -v db-data:/var/lib/postgresql/data \
  postgres:16

# Bind mount (dev)
docker run -d --name api \
  -v "$PWD/src":/app/src \
  my-api-image:latest
```

Règles simples :

- En **prod** : privilégie les volumes nommés. Plus portables, moins liés au chemin de ta machine.
- En **dev** : les bind mounts sont parfaits. Tu modifies le code, le conteneur voit le changement (souvent avec un hot‑reload).

Attention au piège Windows / chemins : en PowerShell, `$PWD` marche souvent ; selon le contexte, tu peux aussi écrire le chemin absolu. L’idée reste la même : « dossier hôte → dossier conteneur ».

### Que mettre (ou pas) dans un volume ?

Bon candidats : données Postgres/MySQL, uploads utilisateurs, fichiers générés, caches lourds que tu veux garder.

Mauvais candidats : le code de prod (préfère une image rebuildée), les secrets en clair (passe par des variables d’env / un secret manager), et tout ce qui doit être **identique** à chaque déploiement (ça appartient à l’image).

---

## Inspecter et nettoyer

```bash
docker volume ls
docker volume inspect db-data
docker volume rm db-data
```

`inspect` montre où Docker stocke réellement les données sur la machine. Utile pour comprendre ; en prod, tu ne manipules rarement ce chemin à la main.

Attention : supprimer un volume = **perdre les données** dedans. Sur une base de test, ok. Sur la prod… tu vois l’idée. Avant un `rm`, un backup (dump SQL, snapshot) évite la sueur froide.

Les volumes « orphelins » s’accumulent aussi. De temps en temps :

```bash
docker volume prune
```

…uniquement si tu es sûr de ne plus en avoir besoin.

---

## Réseaux : faire parler les boîtes

Par défaut, Docker crée un réseau `bridge`. La bonne pratique : créer **ton propre réseau**, comme une pièce où seules tes boîtes se parlent.

```bash
docker network create mon-app-net

docker run -d --name db --network mon-app-net postgres:16
docker run -d --name api --network mon-app-net my-api-image:latest
```

Dans ce réseau :

- `api` joint la base via `db:5432` (le **nom du conteneur** sert de nom DNS) ;
- tu n’as **pas** besoin d’ouvrir le port 5432 vers l’extérieur pour qu’ils se parlent.

C’est le cœur du modèle : isolation + découverte par nom. Plus besoin d’IP magiques qui changent à chaque `docker run`.

Tu peux lister et inspecter :

```bash
docker network ls
docker network inspect mon-app-net
```

`inspect` montre quels conteneurs sont branchés — pratique quand « l’API ne trouve pas la base » (souvent : pas le même réseau, ou mauvais hostname).

---

## Ports vs réseaux

Deux idées différentes :

| Concept | Exemple | À quoi ça sert |
|---------|---------|----------------|
| Publier un port | `-p 8080:80` | Ta machine (ou Internet) atteint le conteneur |
| Port dans le réseau | `db:5432` | Conteneurs entre eux, sans exposition hôte |

Bonne pratique :

- N’ouvre vers l’extérieur que le strict nécessaire (souvent l’API ou un reverse proxy type Nginx/Caddy).
- Laisse bases, brokers, workers **cachés** derrière le réseau Docker.

Exemple de mauvaise habitude : `-p 5432:5432` sur Postgres en local « pour que ça marche », puis oubli en préprod. Résultat : base exposée. Préfère un client SQL via `docker exec` ou un outil branché sur le réseau Docker.

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

Ce qui se passe :

- l’extérieur parle à l’API via `localhost:8080` ;
- l’API parle à la base via `postgres:5432` dans `app-net` ;
- les données vivent dans le volume `db-data` — tu peux supprimer/recréer le conteneur `postgres` sans tout perdre (tant que le volume reste).

Si l’API refuse de démarrer : vérifie le hostname (`postgres`, pas `localhost` — `localhost` dans l’API = l’API elle‑même), le réseau commun, et les logs (`docker logs api`, `docker logs postgres`).

---

## Suite : tout ça dans un fichier

Écrire ces commandes à la main, ça lasse. Avec [Docker Compose](/blog/articles/docker-compose-environnements-local.html), tu décris services, réseaux et volumes dans un YAML. Puis : `docker compose up`. Un seul geste pour tout le garage.

En résumé : **volumes = mémoire**, **réseaux = conversation**, **ports publiés = fenêtre vers l’extérieur**. Une fois ces trois idées claires, Docker Compose et même Kubernetes (pods, Services, PersistentVolumes) deviennent beaucoup moins abstraits.
