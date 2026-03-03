---
title: "Kubernetes : comprendre les pods, les nodes et les ressources de base"
date: 2026-01-05
excerpt: "Avant de déployer quoi que ce soit sur Kubernetes, il faut comprendre les briques de base : cluster, node, pod, container, namespace et ressources. Cette intro pose un vocabulaire clair."
type: article
tags: [Kubernetes, pods, nodes, cluster, DevOps]
series: kubernetes-serie
series_order: 1
og_image: k8s-concepts-1200x630.jpg
---

# Kubernetes : comprendre les pods, les nodes et les ressources de base

Si Docker te permet d'exécuter des conteneurs sur une machine, Kubernetes te permet de gérer **un cluster complet** de machines et de conteneurs.

Avant de parler de déploiements, de services ou d'ingress, il faut être à l'aise avec quelques notions :

- **cluster**,
- **node**,
- **pod**,
- **namespace**,
- et la manière dont Kubernetes gère les ressources.

---

## Cluster et nodes : la vue d'ensemble

Un cluster Kubernetes, c'est :

- un **plan de contrôle** (control plane) qui prend les décisions,
- un ensemble de **nodes** qui exécutent réellement les pods.

### Node

Un node est une machine (physique ou virtuelle) qui :

- fait tourner un agent (`kubelet`),
- exécute les conteneurs via un runtime (containerd, CRI-O…),
- expose CPU/RAM/disque/réseau au cluster.

Il peut y avoir des roles (worker, control-plane, taints pour des workloads spécifiques, etc.).

---

## Pod : l'unité de base

Kubernetes ne déploie pas directement des conteneurs, mais des **pods**.

- Un pod est le plus petit objet déployable dans Kubernetes.
- Il peut contenir **un ou plusieurs conteneurs** qui partagent :
  - le même **namespace réseau** (localhost commun),
  - le même **système de fichiers** pour certains volumes.

Dans la majorité des cas :

- 1 pod = 1 conteneur applicatif (et éventuellement un **sidecar**).

Exemple de pod très simple :

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hello-pod
spec:
  containers:
    - name: hello
      image: nginx:1.27
      ports:
        - containerPort: 80
```

En pratique, tu ne vas pas créer beaucoup de pods "à la main". Tu passeras plutôt par des **Deployments** (on y viendra dans un autre article).

---

## Namespaces : organiser le cluster

Les **namespaces** permettent de découper logiquement ton cluster :

- `default` : namespace par défaut,
- `kube-system` : composants internes de Kubernetes,
- `prod`, `staging`, `dev`, etc. : pour isoler les environnements.

Tu peux lister les namespaces :

```bash
kubectl get namespaces
```

Et cibler un namespace particulier :

```bash
kubectl get pods -n prod
kubectl config set-context --current --namespace=staging
```

Travailler correctement avec les namespaces évite de mélanger les ressources et de faire des bêtises en prod.

---

## Ressources, labels et selectors

Chaque objet Kubernetes a :

- des **labels** (paires clé/valeur),
- éventuellement des **annotations**,
- et parfois des **selectors** qui s'appuient sur ces labels.

Exemple :

```yaml
metadata:
  labels:
    app: mon-api
    tier: backend
```

Ces labels permettent à d'autres ressources (Service, Deployment, HPA…) de cibler les bons pods.

---

## kubectl : ton couteau suisse

Quelques commandes que tu vas utiliser tout le temps :

```bash
kubectl get pods
kubectl get pods -A          # tous les namespaces
kubectl describe pod hello-pod
kubectl logs hello-pod
kubectl exec -it hello-pod -- sh
```

---

## Pour la suite de la série

Dans les prochains articles Kubernetes, on va voir :

1. **L'architecture du cluster** : API server, scheduler, etcd, controller manager.
2. Comment créer des **Deployments** et des **Services** propres.
3. Comment gérer la **configuration** avec ConfigMaps et Secrets.
4. Comment surveiller l'état du cluster (logs, métriques, events).
5. Comment brancher **CI/CD** pour déployer proprement.

L'idée est de partir de ce que tu connais déjà en Docker Compose et de le projeter sur les objets Kubernetes.

