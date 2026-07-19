---
title: "Docker en prod : ranger et protéger ses boîtes"
date: 2024-11-21
excerpt: "Registry privé, scan, non-root, secrets hors image : les bases sérieuses."
type: article
tags: [Docker, production, registry, sécurité, DevOps]
series: docker-serie
series_order: 6
og_image: docker-production-1200x630.jpg
---

# Docker en prod : ranger et protéger ses boîtes

Dernier volet de la serie Docker : on sort du garage local pour parler **prod**.

Objectif : ce que tu fais sur ta machine doit deja ressembler a une mise en ligne propre. VPS, Swarm ou Kubernetes - les memes reflexes. Tu as [optimise tes images](/blog/articles/docker-build-optimisation-images.html) ? Bien. Maintenant on range, on etiquette, on ferme a cle.

---

## Registry prive : l'entrepot serieux

En prod, tu ne veux pas dependre uniquement de Docker Hub public. Tu as besoin d'un **entrepot a toi**.

Options courantes :

- **GitHub Container Registry** (`ghcr.io`) - pratique si ton code est sur GitHub.
- **GitLab Container Registry** - integre au pipeline GitLab.
- **Registry auto-heberge** (Harbor, registry Docker) - pour environnements sensibles.

Exemple avec ghcr.io :

```bash
echo $GITHUB_TOKEN | docker login ghcr.io -u likedevGit --password-stdin

docker build -t ghcr.io/likedevGit/mon-api:1.0.0 .
docker push ghcr.io/likedevGit/mon-api:1.0.0
```

Tu pousses une version claire. Pas "la derniere qu'on a trouvee".

---

## Strategie de tags

Evite le **tout-latest**. C'est comme etiqueter toutes les boites "actuel". Personne ne sait ce qu'il y a dedans.

Conventions utiles :

- `1.2.3` : version exacte (reproductible).
- `1.2` : derniere patch de la 1.2.
- `prod`, `staging` : dernier build depeye sur cet environnement.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/docker-prod-secu.svg" alt="Schema securite Docker en production et registry" class="schema-inline" width="640" />
  <figcaption>En prod : registry prive, scan, non-root, secrets hors image.</figcaption>
</figure>

Workflow classique :

1. La CI pousse une image versionnee : `1.2.3`.
2. Apres validation, tu mets a jour le tag `prod` vers `1.2.3`.
3. Le deploiement utilise `:prod` ou directement la version.

---

## Securite minimale dans les images

Tu ne seras pas expert secu en un article. Mais tu peux eviter les gros pieges.

### 1. Ne pas tourner en root

```dockerfile
RUN addgroup -S app && adduser -S app -G app
USER app
```

Ton programme tourne avec un utilisateur simple. Pas le patron de la machine.

### 2. Reduire la surface

- Images de base **minimales** (alpine, distroless, slim) - cf. [optimisation des images](/blog/articles/docker-build-optimisation-images.html).
- N'installe que ce dont tu as besoin.
- Nettoie les caches (`rm -rf /var/lib/apt/lists/*`).

### 3. Pas de secrets dans l'image

Jamais de mots de passe dans :

- le Dockerfile,
- le code versionne,
- l'image poussee.

A la place : variables d'environnement, fichiers montes, secrets Docker/Kubernetes.

---

## Lien avec Kubernetes (apercu)

Quand tu passeras sur Kubernetes, tes images seront mangees par des **Deployments** :

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

Si tes Dockerfile sont propres, le deploiement est deja plus simple. Les [bases Docker](/blog/articles/docker-fondamentaux-images-conteneurs.html) et [Compose](/blog/articles/docker-compose-environnements-local.html) t'ont prepare le terrain.

---

## Resume de la serie

1. Images vs conteneurs.
2. [Installation propre](/blog/articles/docker-installation-bonnes-pratiques.html).
3. [Volumes et reseaux](/blog/articles/docker-volumes-reseaux.html).
4. Compose pour un environnement complet.
5. Optimisation des Dockerfile.
6. Prod : registry, tags, securite.

Avec ca, tu as un **socle solide**. Les boites sont legeres, etiquetees, et pretes a voyager hors de ton PC.
