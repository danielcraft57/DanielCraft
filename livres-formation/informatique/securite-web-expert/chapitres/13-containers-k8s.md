# Conteneurs et Kubernetes (bases securite)

Docker et K8s apportent de nouvelles surfaces : images, orchestrateur, reseau.

## Docker

- Image **non-root** (`USER 1000`).
- Read-only filesystem si possible.
- Pas de `--privileged` sans raison.

## Kubernetes

- **RBAC** minimal par namespace.
- **NetworkPolicy** : isoler les pods.
- Secrets K8s chiffres at rest (etcd encryption).
- Pas de `cluster-admin` pour les apps.

> **Piege** - Monter le socket Docker dans un conteneur = game over.

## A retenir

- Conteneur != sandbox magique : durcir image + orchestrateur.
- Moindre privilege partout.
