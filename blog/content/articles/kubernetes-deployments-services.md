---
title: "Déployer une appli sur Kubernetes : Deployments et Services"
date: 2025-01-14
excerpt: "Passer d'un simple pod à un déploiement géré : Deployments, ReplicaSets, Services (ClusterIP, NodePort, LoadBalancer) et stratégie de mise à jour."
type: article
tags: [Kubernetes, Deployments, Services, réseau]
series: kubernetes-serie
series_order: 3
og_image: k8s-deployments-services-1200x630.jpg
---

# Déployer une appli sur Kubernetes : Deployments et Services

Créer un pod à la main, c'est bien pour tester. Pour une vraie appli, tu veux :

- plusieurs réplicas,
- des mises à jour contrôlées,
- un point d'entrée stable pour les clients.

C'est exactement ce que t'apportent les **Deployments** et les **Services**.

---

## Deployment : la façon moderne de gérer tes pods

Un **Deployment** gère :

- le nombre de réplicas,
- la stratégie de mise à jour,
- l'historique des versions de ReplicaSets.

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

Commande :

```bash
kubectl apply -f deployment-api.yaml
kubectl get deployments
kubectl get pods -l app=mon-api
```

---

## Services : exposer tes pods

Les pods peuvent mourir, être recréés, bouger de node. Tu ne veux pas que les clients parlent directement aux IPs des pods.

Tu définis un **Service** qui :

- pointe vers les bons pods via un **selector** de labels,
- leur assigne une IP/port stable dans le cluster.

### ClusterIP (interne)

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

- Les autres pods du cluster peuvent appeler `http://mon-api:80`.
- Rien n'est exposé vers l'extérieur.

### NodePort (exposition simple)

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

- Ouvre le port 30080 sur chaque node.
- Accessible sur `http://<ip-node>:30080`.

Pratique pour du debug ou un petit cluster perso, moins idéal en prod "propre".

### LoadBalancer (cloud)

Sur les clouds managés (GKE, AKS, EKS…), un Service `LoadBalancer` demande au provider :

- de provisionner un load balancer externe,
- de le brancher sur ton Service.

```yaml
spec:
  type: LoadBalancer
  selector:
    app: mon-api
  ports:
    - port: 80
      targetPort: 3000
```

---

## Rolling update et rollback

Avec un Deployment, tu peux faire un **rolling update** :

```bash
kubectl set image deployment/mon-api api=ghcr.io/likedevGit/mon-api:1.1.0
kubectl rollout status deployment/mon-api
```

Si ça se passe mal :

```bash
kubectl rollout undo deployment/mon-api
```

La stratégie par défaut remplace progressivement les pods, sans downtime marqué (sauf bug applicatif).

---

## Bonnes pratiques

- Utilise des **labels cohérents** (`app`, `tier`, `env`) pour faciliter les selectors.  
- Sépare les Services internes (ClusterIP) des frontaux (LoadBalancer/Ingress).  
- Sur du cloud, préfère souvent un **Ingress** + Service ClusterIP plutôt que des dizaines de Services LoadBalancer.

Dans les prochains articles, on ajoutera la **configuration** (ConfigMaps, Secrets) et l'**observabilité** pour suivre tes pods en situation réelle.
