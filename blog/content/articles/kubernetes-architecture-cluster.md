---
title: "Kubernetes : architecture d'un cluster (API server, etcd, scheduler)"
date: 2025-01-09
excerpt: "Plonger sous le capot de Kubernetes : rôle de l'API server, d'etcd, du scheduler et des contrôleurs. Comprendre comment le control plane prend ses décisions."
type: article
tags: [Kubernetes, architecture, control plane, etcd, scheduler]
series: kubernetes-serie
series_order: 2
og_image: k8s-architecture-1200x630.jpg
---

# Kubernetes : architecture d'un cluster (API server, etcd, scheduler)

Tu as vu les **pods** et les **nodes**. Reste une question : *qui décide quoi lancer, où et quand ?*

C'est le boulot du **control plane** : un ensemble de composants qui orchestrent l'état du cluster.

---

## Vue globale

On peut résumer Kubernetes ainsi :

- **Tu déclares un état désiré** (manifeste YAML : "je veux 3 pods de mon API").  
- **Le control plane observe l'état réel**.  
- **Il applique des boucles de contrôle** pour rapprocher le réel du désiré.

Les principaux composants côté control plane :

- `kube-apiserver`
- `etcd`
- `kube-scheduler`
- `kube-controller-manager`

Sur chaque node, on retrouve :

- `kubelet`
- le runtime de conteneurs (containerd, CRI-O…)

---

## kube-apiserver : porte d'entrée unique

L'**API server** est le point d'entrée central :

- toutes les commandes `kubectl` passent par lui,
- les opérateurs et controllers discutent avec lui,
- il gère l'authentification/autorisation, la validation des objets, etc.

Quand tu fais :

```bash
kubectl apply -f deployment-api.yaml
```

`kubectl` :

1. appelle l'API server,
2. lui envoie le YAML,
3. l'API server valide, puis enregistre l'objet dans etcd.

---

## etcd : la source de vérité

Kubernetes stocke tout son état dans **etcd**, une base clé/valeur distribuée.

- Chaque ressource (Pod, Deployment, Service, ConfigMap, etc.) est un objet stocké dans etcd.
- Le control plane lit/écrit en permanence dans etcd.

En production, etcd est critique :

- on le met souvent sur des nodes dédiés (ou au moins protégés),
- on surveille sa latence et son espace disque,
- on planifie des backups réguliers.

---

## kube-scheduler : qui va où ?

Le **scheduler** décide *sur quel node* placer chaque pod.

Il se base sur :

- les ressources disponibles (CPU/RAM),
- les contraintes (`nodeSelector`, `nodeAffinity`, `taints/tolerations`),
- d'éventuels plug-ins de scheduling.

Cycle basique :

1. L'API server voit qu'un nouveau pod doit être créé (par ex. suite à un Deployment).  
2. Il marque ce pod comme "non schedulé".  
3. Le scheduler choisit un node adapté et met à jour le pod avec cette info.  
4. Le `kubelet` du node choisi se charge ensuite de créer les conteneurs.

---

## kube-controller-manager : les boucles de contrôle

Le **controller manager** fait tourner plein de "contrôleurs" :

- **ReplicationController / Deployment controller** : s'assure qu'il y a le bon nombre de pods.  
- **Node controller** : surveille la santé des nodes.  
- **Endpoint / Service controller** : met à jour les endpoints des Services.  
- etc.

Chaque controller suit le même pattern :

1. Observe un type de ressource (Deployment, Node, etc.).  
2. Compare l'état désiré à l'état réel.  
3. Effectue les actions nécessaires (créer/supprimer des pods, marquer un node comme `NotReady`, etc.).

---

## kubelet et runtime de conteneurs

Sur chaque node :

- **kubelet** parle avec l'API server, reçoit les ordres (pods à créer/supprimer).  
- Il demande ensuite au **runtime** (containerd, CRI-O) de lancer/stopper les conteneurs.  
- Il remonte aussi l'état (health, logs, etc.) vers le control plane.

---

## Pourquoi cette architecture t'intéresse en tant que dev

Même si tu n'administres pas directement le cluster, comprendre cette architecture te permet de :

- mieux lire les messages d'erreur (`kubectl describe`, events),
- savoir où regarder quand quelque chose ne va pas (pods en `Pending`, nodes en `NotReady`),
- discuter plus efficacement avec l'équipe infra/DevOps.

Dans les prochains articles, on va utiliser ces briques pour déployer réellement des applis.
