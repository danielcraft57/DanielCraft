---
title: "Kubernetes : des boites (pods) sur des machines (nodes)"
date: 2025-01-07
excerpt: "Le vocabulaire de base pour comprendre un cluster sans se noyer."
type: article
tags: [Kubernetes, pods, nodes, cluster, DevOps]
series: kubernetes-serie
series_order: 1
og_image: k8s-concepts-1200x630.jpg
---

# Kubernetes : des boites (pods) sur des machines (nodes)

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/k8s-pods-nodes.svg" alt="Schema pods et nodes Kubernetes" class="schema-inline" width="640" />
  <figcaption>Node = machine. Pod = plus petite unite qui tourne dessus.</figcaption>
</figure>

Si Docker te permet d'exécuter des conteneurs sur **une** machine, Kubernetes te permet de gérer un **cluster** : plusieurs machines qui travaillent ensemble. L'idée n'est pas de remplacer Docker, mais de décider *où* tourne chaque boîte, *combien* d'exemplaires tu en veux, et *quoi faire* si une machine tombe.

Avant de parler de Deployments, de Services ou d'Ingress, il faut être à l'aise avec quelques mots du quotidien :

- **cluster** : l'ensemble (cerveau + machines),
- **node** : une machine du cluster,
- **pod** : la plus petite unité qui tourne,
- **namespace** : un tiroir logique pour organiser,
- **labels** : des étiquettes pour retrouver les bons pods.

Ce glossaire suffit pour lire la majorité des tutos et des `kubectl get` sans paniquer.

---

## Cluster et nodes : la vue d'ensemble

Un cluster Kubernetes, c'est deux familles de rôles :

1. le **plan de contrôle** (control plane) : il décide (où placer un pod, que faire si un node disparaît, quel état viser) ;
2. les **nodes** : ils exécutent réellement les pods.

En petit labo, tout peut tourner sur une seule machine (Minikube, kind, k3s). En prod, tu sépares souvent le control plane des workers, et tu mets plusieurs nodes pour survivre à une panne.

### Node : une machine qui travaille pour le cluster

Un node est une machine (physique ou virtuelle) qui :

- fait tourner un agent appelé **kubelet** (le bras droit de Kubernetes sur cette machine),
- exécute les conteneurs via un runtime (containerd, CRI-O…),
- met à disposition CPU, RAM, disque et réseau.

Tu verras parfois des rôles ou des **taints** : « cette machine n'accepte que certains pods » (GPU, batch, control-plane…). Pour démarrer, retiens surtout : **node = machine**, **pod = charge de travail dessus**.

Commande utile :

```bash
kubectl get nodes
kubectl describe node mon-node
```

`describe` montre la capacité (CPU/RAM), les pods déjà placés, et les conditions (Ready, MemoryPressure…). C'est souvent le premier endroit où regarder si « rien ne démarre ».

---

## Pod : l'unité de base

Kubernetes ne déploie pas directement des conteneurs : il déploie des **pods**.

- Un pod est le plus petit objet déployable.
- Il contient **un ou plusieurs** conteneurs qui partagent :
  - le même **namespace réseau** (ils se voient en `localhost`),
  - souvent des **volumes** communs.

Dans la vraie vie, 95 % des pods = **1 conteneur applicatif**, parfois + un **sidecar** (proxy, agent de logs, sync de config).

Exemple minimal :

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

Tu peux le créer avec `kubectl apply -f hello-pod.yaml`, puis :

```bash
kubectl get pods
kubectl describe pod hello-pod
kubectl logs hello-pod
kubectl exec -it hello-pod -- sh
```

En pratique, tu crées rarement des pods « à la main » pour une appli. Tu passes par un **Deployment** (il recrée les pods s'ils meurent, gère le rolling update). Les pods restent pourtant la brique que tu observes au quotidien : crash, ImagePullBackOff, Pending… c'est toujours le pod qui parle.

Si tu viens de Docker Compose, le mental model aide :

| Docker Compose | Kubernetes (idée) |
|----------------|-------------------|
| service | Deployment + pods |
| container | conteneur *dans* un pod |
| machine unique | plusieurs nodes |

Pour aller plus loin sur le déploiement, vois [Deployments et Services](/blog/articles/kubernetes-deployments-services.html) quand tu seras prêt.

---

## Namespaces : organiser sans tout mélanger

Les **namespaces** découpent logiquement le cluster. Ce n'est pas un mur de sécurité absolu (il faut aussi NetworkPolicy, RBAC…), mais c'est indispensable pour ne pas confondre `dev` et `prod`.

Exemples courants :

- `default` : namespace par défaut,
- `kube-system` : composants internes (ne touche pas au hasard),
- `prod`, `staging`, `dev` : tes environnements,
- `monitoring` : Prometheus, Grafana, etc.

```bash
kubectl get namespaces
kubectl get pods -n prod
kubectl config set-context --current --namespace=staging
```

Astuce débutant : dès que tu travailles souvent dans un namespace, fixe-le dans le contexte. Tu évites d'appliquer un YAML en `default` alors que tu pensais être en `staging`.

---

## Labels, selectors et ressources

Chaque objet Kubernetes a des **labels** (paires clé/valeur). Ce sont des étiquettes collées sur les pods, services, etc.

```yaml
metadata:
  labels:
    app: mon-api
    tier: backend
    env: staging
```

Un **Service** ou un **Deployment** retrouve les bons pods grâce à un **selector** du type « tous les pods avec `app=mon-api` ». Sans labels cohérents, le service ne pointe nulle part — symptôme classique : « mon Service existe, mais rien ne répond ».

Tu peux aussi demander des **requests/limits** CPU et mémoire sur les conteneurs. En débutant, mets des valeurs raisonnables pour éviter qu'un pod gourmand étouffe le node. Kubernetes utilisera ces infos pour le placement (scheduling).

---

## kubectl : le couteau suisse du quotidien

Quelques commandes que tu vas retaper des centaines de fois :

```bash
kubectl get pods
kubectl get pods -A                 # tous les namespaces
kubectl get pods -o wide            # IP + node
kubectl describe pod hello-pod
kubectl logs hello-pod -f
kubectl exec -it hello-pod -- sh
kubectl delete pod hello-pod        # souvent recréé par le Deployment
```

Méthode de debug simple :

1. `get` → le pod est-il Running ?
2. `describe` → Events en bas (ImagePull, FailedScheduling…).
3. `logs` → l'appli a-t-elle planté au démarrage ?
4. `exec` → si besoin, explorer depuis l'intérieur.

---

## Pour la suite de la série

Dans les prochains articles Kubernetes, on verra :

1. l'**architecture** du control plane (API server, scheduler, etcd…) ;
2. des **Deployments** et **Services** propres ;
3. la **config** avec ConfigMaps et Secrets ;
4. l'**observabilité** (logs, métriques, events) ;
5. le branchement **CI/CD** pour déployer sans stress.

L'objectif : partir de ce que tu connais déjà en [Docker](/blog/articles/docker-fondamentaux-images-conteneurs.html) / Compose, et le projeter sur les objets Kubernetes. Une fois pods, nodes et namespaces clairs, le reste devient beaucoup plus digeste.
