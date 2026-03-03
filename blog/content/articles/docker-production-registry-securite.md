---
title: "Préparer Docker pour la production : registry, tags et sécurité"
date: 2025-12-23
excerpt: "Passer de Docker en local à un usage plus sérieux : registry privé, stratégie de tags, bonnes pratiques de sécurité de base et liens avec Kubernetes."
type: article
tags: [Docker, production, registry, sécurité, DevOps]
series: docker-serie
series_order: 6
og_image: docker-production-1200x630.jpg
---

# Préparer Docker pour la production : registry, tags et sécurité

Dernier volet de la série Docker : on sort du cadre purement local pour parler **prod**.

Objectif : que ce que tu fais sur ta machine soit déjà pensé pour une mise en production propre, que ce soit sur un simple VPS, une stack Swarm, ou un cluster Kubernetes.

---

## Registry privé : où pousser tes images

Pour la prod, tu ne veux pas dépendre uniquement de Docker Hub public.

Options courantes :

- **GitHub Container Registry** (`ghcr.io`)  
  Pratique si ton code est sur GitHub.

- **GitLab Container Registry**  
  Intégré au pipeline CI/CD GitLab.

- **Registry auto‑hébergé** (Harbor, registry Docker, etc.)  
  Utile pour environnements sensibles / clients.

Exemple avec GitHub Container Registry :

```bash
echo $GITHUB_TOKEN | docker login ghcr.io -u likedevGit --password-stdin

docker build -t ghcr.io/likedevGit/mon-api:1.0.0 .
docker push ghcr.io/likedevGit/mon-api:1.0.0
```

---

## Stratégie de tags

Évite le **tout-latest**. Quelques conventions utiles :

- `1.2.3` : version exacte (build reproduisible).
- `1.2` : dernière patch de la 1.2.
- `prod`, `staging`, `test` : dernier build déployé sur tel environnement.

Workflow classique :

1. CI pousse une image versionnée : `1.2.3`.  
2. Après validation, tu mets à jour le tag `prod` → `1.2.3`.  
3. Ta config de déploiement utilise `:prod` (ou directement la version, selon ta préférence).

---

## Sécurité minimale dans les images

Tu ne vas pas devenir expert sécurité en un article, mais tu peux éviter les gros pièges.

### 1. Ne pas tourner en root

Dans ton Dockerfile :

```dockerfile
RUN addgroup -S app && adduser -S app -G app
USER app
```

Ensuite, ton process applicatif tourne avec cet utilisateur plutôt que root.

### 2. Réduire la surface d'attaque

- Utilise des images de base **minimales** (alpine, distroless, slim).  
- N'installe que ce dont tu as besoin.  
- Nettoie les caches de paquets (`rm -rf /var/lib/apt/lists/*`).

### 3. Ne pas embarquer les secrets

Jamais de secrets dans :

- le Dockerfile,
- le code versionné,
- les images.

À la place :

- variables d'env,
- fichiers montés,
- secrets Docker/Kubernetes.

---

## Intégration avec Kubernetes (aperçu)

Quand tu passeras sur Kubernetes, tes images Docker seront consommées par des **Deployments** :

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mon-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: mon-api
  template:
    metadata:
      labels:
        app: mon-api
    spec:
      containers:
        - name: api
          image: ghcr.io/likedevGit/mon-api:1.2.3
          ports:
            - containerPort: 3000
```

Si tes Dockerfile sont propres, tes déploiements Kubernetes seront déjà beaucoup plus simples.

---

## Résumé de la série Docker

On a vu :

1. **Images vs conteneurs** et le cycle de vie de base.  
2. **Installation propre** de Docker (Linux, macOS, Windows/WSL).  
3. **Volumes** et **réseaux** pour les données et la communication entre services.  
4. **docker-compose** pour décrire un environnement complet en YAML.  
5. **Optimisation des Dockerfile** et réduction de la taille des images.  
6. **Préparation de la prod** : registry privé, tags, sécurité, lien avec Kubernetes.

Avec ça, tu as un socle solide pour aborder la suite : **Kubernetes**.

