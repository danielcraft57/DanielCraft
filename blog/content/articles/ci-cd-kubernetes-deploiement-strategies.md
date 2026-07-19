---
title: "CI/CD sur Kubernetes : changer de version sans tout casser"
date: 2025-03-25
excerpt: "Rolling, blue/green, canary : comment remplacer une version en douceur."
type: article
tags: [CI/CD, Kubernetes, déploiement, canary, rollback]
series: ci-cd-serie
series_order: 7
og_image: ci-cd-k8s-deploiement-1200x630.jpg
---

# CI/CD sur Kubernetes : changer de version sans tout casser

Sur [Kubernetes](/blog/articles/kubernetes-concepts-pods-nodes.html), tu ne "copies" pas un fichier sur un serveur. Tu remplaces des **pods** (petites boites) pendant que le service continue.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-k8s-strategies.svg" alt="Schema strategies de deploiement Kubernetes" class="schema-inline" width="640" />
  <figcaption>Rolling, blue/green, canary et rollback.</figcaption>
</figure>

## Trois strategies en francais

- **Rolling** : on remplace peu a peu. Simple et courant.
- **Blue/Green** : deux versions cote a cote, on bascule le trafic d'un coup.
- **Canary** : on envoie un petit pourcentage d'utilisateurs sur la nouveaute.

Toujours prevoir un **rollback** (revenir en arriere) et des **sondes** (est-ce que l'app repond ?). Voir aussi [Deployments et Services](/blog/articles/kubernetes-deployments-services.html).

