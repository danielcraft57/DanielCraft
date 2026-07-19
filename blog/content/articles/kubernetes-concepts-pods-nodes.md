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

[Docker](/blog/articles/docker-fondamentaux-images-conteneurs.html) fait tourner une boite sur **une** machine. **Kubernetes** gere plein de boites sur **plein** de machines.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/k8s-pods-nodes.svg" alt="Schema pods et nodes Kubernetes" class="schema-inline" width="640" />
  <figcaption>Node = machine. Pod = plus petite unite qui tourne dessus.</figcaption>
</figure>

## Les mots a connaitre

- **Cluster** : l'ensemble (cerveau + machines)
- **Node** : une machine du cluster
- **Pod** : la plus petite unite (souvent 1 conteneur)
- **Namespace** : un tiroir pour ranger (prod, staging…)

Tu demandes un etat ("je veux 3 copies de mon site"). Kubernetes se debrouille pour y arriver. Ensuite : [architecture](/blog/articles/kubernetes-architecture-cluster.html) et [Deployments](/blog/articles/kubernetes-deployments-services.html).

