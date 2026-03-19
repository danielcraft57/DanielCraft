---
title: "GitOps : déployer avec Argo CD ou Flux (et arrêter les kubectl à la main)"
date: 2025-03-27
excerpt: "Le Git devient la source de vérité de ton cluster Kubernetes : manifests versionnés, synchronisation automatique, audit et rollbacks propres avec Argo CD ou Flux."
type: article
tags: [CI/CD, GitOps, Kubernetes, Argo CD, Flux]
series: ci-cd-serie
series_order: 8
og_image: ci-cd-gitops-1200x630.jpg
---

# GitOps : déployer avec Argo CD ou Flux (et arrêter les kubectl à la main)

Le problème du déploiement "classique" (CI qui fait `kubectl apply`) :

- tu ne sais pas toujours quel est l'état exact souhaité,
- l'historique est dispersé dans les logs de CI,
- les rollbacks sont moins naturels.

Le GitOps règle ça avec une idée simple :

**Le Git décrit l'état désiré du cluster.**  
Et un contrôleur dans le cluster s'assure que la réalité suit cet état.

---

## Le principe GitOps

1. Tu versionnes tes manifests (ou Helm/Kustomize) dans un repo.
2. Argo CD / Flux surveille le repo.
3. Dès qu'un commit est fusionné, l'outil synchronise le cluster.

Résultat :

- audit clair,
- diff visible,
- rollbacks via Git (revert commit),
- séparation nette entre code applicatif et config de déploiement.

---

## Argo CD vs Flux (en bref)

- **Argo CD** : UI très pratique, visualisation des apps, diffs, sync manuelle/auto.
- **Flux** : plus "Git‑native", très bien intégré pour Helm/Kustomize, souvent plus léger.

Les deux sont solides. Choisis surtout selon :

- ton équipe,
- ton besoin d'UI,
- ton stack (Helm/Kustomize).

---

## Comment la CI s'intègre

Avec GitOps, la CI ne déploie pas directement. Elle :

- build l'image,
- push l'image,
- met à jour le repo GitOps (tag d'image),
- crée une PR (ou commit sur une branche).

Ensuite Argo/Flux fait la synchro.

Ça évite qu'une CI compromise ait accès direct au cluster (selon les setups).

---

## Rollback GitOps

Rollback = revert commit.

Tu reviens à un manifest précédent, Argo/Flux resynchronise, c'est propre.

---

Prochain article : versioning, releases, rollbacks et comment garder une stratégie de livraison cohérente (tags, changelog, environments).

