---
title: "Kubernetes : copies de ton app + adresse stable"
date: 2025-01-14
excerpt: "Deployment pour gerer les pods, Service pour les joindre facilement."
type: article
tags: [Kubernetes, Deployments, Services, réseau]
series: kubernetes-serie
series_order: 3
og_image: k8s-deployments-services-1200x630.jpg
---

# Kubernetes : copies de ton app + adresse stable

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/k8s-deploy-service.svg" alt="Schema Deployment et Service" class="schema-inline" width="640" />
  <figcaption>Image, Deployment, pods, Service, utilisateurs.</figcaption>
</figure>

Créer un pod à la main, c'est bien pour tester. Pour une vraie appli, tu veux :

- plusieurs copies (réplicas) de ton conteneur,
- des mises à jour contrôlées,
- une adresse stable pour les clients (autres pods ou utilisateurs).

C'est exactement le duo **Deployment** + **Service**. Si les notions de pods et de nœuds ne sont pas encore claires, passe d'abord par [pods et nodes](/blog/articles/kubernetes-concepts-pods-nodes.html) et [l'architecture d'un cluster](/blog/articles/kubernetes-architecture-cluster.html).

---

## Deployment : gérer tes pods sans les micro-gérer

Un **Deployment** décrit l'état souhaité de ton appli. Kubernetes se charge du reste :

- nombre de réplicas,
- stratégie de mise à jour (rolling par défaut),
- historique via des ReplicaSets (utile pour rollback).

Exemple minimal :

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
          image: ghcr.io/likedevGit/mon-api:1.0.0
          ports:
            - containerPort: 3000
```

Commandes utiles :

```bash
kubectl apply -f deployment-api.yaml
kubectl get deployments
kubectl get pods -l app=mon-api
kubectl describe deployment mon-api
```

### Ce qui se passe concrètement

Tu dis « je veux 3 pods avec cette image ». Si un pod meurt, le Deployment (via le ReplicaSet) en recrée un. Tu ne colles plus d'IP de pod dans tes configs : les pods bougent, le **Service** restera stable (voir plus bas).

Astuce débutant : aligne toujours les labels du `selector` et du `template.metadata.labels`. Un décalage = Deployment qui ne « voit » aucun pod.

---

## Services : exposer tes pods sans coller aux IP

Les pods naissent, meurent, changent de nœud. Les clients ne doivent **jamais** parler directement à l'IP d'un pod.

Un **Service** :

- sélectionne les pods via un **selector** de labels,
- offre une IP / un nom DNS stable dans le cluster (`mon-api.default.svc.cluster.local`, souvent raccourci en `mon-api`).

### ClusterIP (interne) — le défaut

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mon-api
spec:
  type: ClusterIP
  selector:
    app: mon-api
  ports:
    - port: 80
      targetPort: 3000
```

- Les autres pods appellent `http://mon-api:80`.
- Rien n'est exposé vers Internet.

Cas typique : front → API, API → base (si la base est aussi dans le cluster), workers → API interne.

### NodePort — exposition simple pour debug

```yaml
spec:
  type: NodePort
  selector:
    app: mon-api
  ports:
    - port: 80
      targetPort: 3000
      nodePort: 30080
```

Accessible sur `http://<ip-node>:30080`. Pratique en labo ou petit cluster perso, rarement l'idéal en prod « propre » (ports élevés, TLS, multi-services…).

### LoadBalancer — côté cloud

Sur GKE, AKS, EKS…, un Service `LoadBalancer` demande au provider un load balancer externe branché sur ton Service :

```yaml
spec:
  type: LoadBalancer
  selector:
    app: mon-api
  ports:
    - port: 80
      targetPort: 3000
```

En prod, on préfère souvent **Ingress** (ou Gateway API) + Services ClusterIP : un seul point d'entrée HTTP(S), routage par host/path, certificats centralisés — plutôt que dix LoadBalancers.

---

## Rolling update et rollback

Mise à jour progressive :

```bash
kubectl set image deployment/mon-api api=ghcr.io/likedevGit/mon-api:1.1.0
kubectl rollout status deployment/mon-api
```

Si ça tourne mal :

```bash
kubectl rollout undo deployment/mon-api
kubectl rollout history deployment/mon-api
```

La stratégie par défaut remplace les pods progressivement. Sans sondes `readiness`, Kubernetes peut envoyer du trafic vers un pod encore en train de démarrer — d'où l'intérêt de les configurer tôt. Pour aller plus loin (canary, blue/green) : [stratégies de déploiement](/blog/articles/ci-cd-kubernetes-deploiement-strategies.html). Pour automatiser tout ça : [CI/CD vers Kubernetes](/blog/articles/kubernetes-ci-cd-deploiement-continu.html).

---

## Checklist de démarrage

- [ ] Deployment avec `replicas` ≥ 2 pour une appli « sérieuse »
- [ ] Labels cohérents (`app`, éventuellement `tier`, `env`)
- [ ] Service ClusterIP aligné sur le même selector
- [ ] `containerPort` / `targetPort` cohérents avec l'appli
- [ ] Image taguée (pas seulement `latest`)
- [ ] `kubectl rollout status` après chaque changement d'image
- [ ] Config et secrets hors de l'image — [ConfigMaps et Secrets](/blog/articles/kubernetes-configmaps-secrets.html)

### Pièges fréquents

- **Selector / labels qui ne matchent pas** : Service sans endpoints (`kubectl get endpoints mon-api` vide).
- **Un seul réplica** : maintenance d'un nœud = downtime immédiat.
- **Port 3000 exposé « partout »** sans savoir si c'est ClusterIP, NodePort ou LB.
- **Oublier le rollback** : pas d'historique clair, tag d'image perdu.
- **Aucun log / métrique** : difficile de comprendre pourquoi le rollout échoue — suite logique : [observabilité](/blog/articles/kubernetes-observabilite-logs-metrics.html).

---

## Bonnes pratiques

- Labels stables et documentés pour tous les selectors.
- ClusterIP pour le trafic interne ; Ingress / un LoadBalancer frontal pour l'extérieur.
- Séparer clairement front, API et jobs (Deployments + Services dédiés).
- Toujours vérifier les endpoints après un `apply`.

Tu as maintenant le duo de base pour faire tourner une appli « comme en vrai ». Ensuite : configurer sans rebuild ([ConfigMaps / Secrets](/blog/articles/kubernetes-configmaps-secrets.html)), observer ([logs et metrics](/blog/articles/kubernetes-observabilite-logs-metrics.html)), puis brancher un [pipeline CI/CD](/blog/articles/kubernetes-ci-cd-deploiement-continu.html).
