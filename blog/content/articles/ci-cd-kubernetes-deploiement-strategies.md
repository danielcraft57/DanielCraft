---
title: "CI/CD sur Kubernetes : stratégies de déploiement (rolling, blue/green, canary)"
date: 2026-02-14
excerpt: "Déployer sur Kubernetes sans stress : rolling updates, blue/green, canary, readiness probes, rollbacks et comment choisir la bonne stratégie."
type: article
tags: [CI/CD, Kubernetes, déploiement, canary, rollback]
series: ci-cd-serie
series_order: 7
og_image: ci-cd-k8s-deploiement-1200x630.jpg
---

# CI/CD sur Kubernetes : stratégies de déploiement (rolling, blue/green, canary)

Kubernetes t'apporte déjà un gros avantage : le **rollout** est géré par le Deployment.

Mais selon ton trafic, ton niveau de risque et tes contraintes, tu ne déploies pas toujours de la même manière.

---

## 1) Rolling update (par défaut)

Le classique :

- tu remplaces progressivement les pods,
- tu gardes du trafic pendant la mise à jour,
- tu peux rollback.

Ça marche très bien si :

- tes pods sont stateless,
- tu as des readiness probes propres,
- tes migrations DB sont gérées correctement.

Commandes utiles :

```bash
kubectl rollout status deployment/mon-api
kubectl rollout undo deployment/mon-api
kubectl rollout history deployment/mon-api
```

---

## 2) Blue/Green

Tu as deux versions :

- **blue** (actuelle),
- **green** (nouvelle).

Tu déploies green, tu testes, puis tu switches le trafic d'un coup.

Avantages :

- rollback ultra simple (tu reswitch),
- tests réalistes avant bascule.

Inconvénients :

- double consommation de ressources pendant la transition.

Souvent géré via :

- deux Deployments,
- un Service qui pointe sur l'un ou l'autre,
- ou un Ingress controller avec switch de backend.

---

## 3) Canary

Tu envoies progressivement du trafic vers la nouvelle version :

- 5 %,
- 20 %,
- 50 %,
- 100 %.

Avantages :

- tu limites l'impact d'un bug,
- tu observes les métriques en temps réel.

Inconvénients :

- plus complexe (routing, métriques, décisions).

Outils fréquents :

- Argo Rollouts,
- Flagger,
- service mesh (Istio/Linkerd).

---

## Le vrai secret : readiness + métriques

Quel que soit le style, tu dois avoir :

- readiness probe (évite de router vers un pod pas prêt),
- métriques (taux d'erreur, latence),
- alerting (si ça dérive).

Un canary sans métriques, c'est juste un déploiement aléatoire.

---

## Comment choisir ?

- Projet simple, faible trafic : rolling update
- Besoin de switch instant + rollback facile : blue/green
- Gros trafic / gros risque : canary

Prochain article : on passe à une approche encore plus propre en équipe : **GitOps** (Argo CD / Flux).

