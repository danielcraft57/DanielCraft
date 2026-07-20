---
title: "GitOps : le cluster suit Git (pas l'inverse)"
date: 2025-03-27
excerpt: "Argo CD ou Flux : deployer en declarant l'etat souhaite dans un depot Git."
type: article
tags: [CI/CD, GitOps, Kubernetes, Argo CD, Flux]
series: ci-cd-serie
series_order: 8
og_image: ci-cd-gitops-1200x630.jpg
---

# GitOps : le cluster suit Git (pas l'inverse)

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-gitops.svg" alt="Schema GitOps avec Argo ou Flux" class="schema-inline" width="640" />
  <figcaption>Git, build, manifest, synchronisation cluster.</figcaption>
</figure>

Le déploiement « classique » pose un problème : la CI exécute `kubectl apply`, l'état réel du cluster diverge du dépôt, et les rollbacks se font au feeling en relançant d'anciens jobs. GitOps inverse la logique : **Git décrit l'état désiré**, et un contrôleur dans le cluster s'assure que la réalité suit.

## Le principe GitOps en quatre étapes

1. Tu versionnes tes manifests Kubernetes (YAML brut, Helm charts ou overlays Kustomize) dans un dépôt Git dédié — souvent appelé « repo GitOps ».
2. La CI build l'image applicative, la push au registry, puis met à jour le tag d'image dans le repo GitOps (commit direct ou pull request).
3. Argo CD ou Flux surveille ce repo en continu.
4. Dès qu'un changement est fusionné, l'outil synchronise le cluster pour correspondre au Git.

Résultat concret :

- **Audit trail** : chaque déploiement = un commit identifiable
- **Diff visible** : tu vois exactement ce qui va changer avant de synchroniser
- **Rollback trivial** : `git revert` sur le commit fautif, resync automatique
- **Séparation des responsabilités** : la CI n'a plus besoin d'un accès direct au cluster (selon le setup)

## Argo CD vs Flux : lequel choisir

Les deux outils sont matures et largement adoptés. La différence se joue surtout sur l'expérience équipe :

### Argo CD

- Interface web riche : visualisation des applications, arborescence des ressources, diffs inline
- Sync manuelle ou automatique, avec options de self-heal (corrige les dérives)
- Écosystème Argo (Rollouts pour le canary, Workflows pour les pipelines data)
- Idéal si ton équipe apprécie une UI pour piloter les déploiements

### Flux (FluxCD)

- Approche plus « Git-native », orientée CLI et reconciliation continue
- Intégration native avec Helm et Kustomize via des CRD (`HelmRelease`, `Kustomization`)
- Footprint léger, souvent préféré dans les setups multi-cluster
- Pas d'UI par défaut (des dashboards tiers existent)

En pratique : choisis selon ton équipe, ton besoin d'UI et ta stack de templating. Les deux gèrent le multi-environnement (dev/staging/prod) via des branches ou des dossiers séparés.

## Comment la CI s'intègre dans GitOps

Avec GitOps, la CI ne fait plus `kubectl apply`. Elle se limite à :

1. Builder et tester l'application
2. Pusher l'image vers le registry (tag = SHA ou version sémantique)
3. Mettre à jour le manifest GitOps (nouveau tag d'image)
4. Optionnellement ouvrir une PR pour revue avant merge

Exemple de mise à jour automatisée :

```yaml
# Dans le repo GitOps : apps/api/deployment.yaml
image: ghcr.io/mon-org/mon-api:abc123def
```

Un bot ou un job CI remplace `abc123def` par le SHA du commit fraîchement buildé. Argo CD détecte le changement et déploie.

Avantage sécurité : même si la CI est compromise, l'attaquant ne peut modifier que le tag d'image dans Git — pas exécuter n'importe quelle commande kubectl arbitraire.

## Structure d'un repo GitOps

Organisation courante :

```
gitops-repo/
├── apps/
│   ├── staging/
│   │   └── api/
│   └── production/
│       └── api/
├── infrastructure/
│   ├── ingress/
│   └── monitoring/
└── clusters/
    ├── staging/
    └── production/
```

Chaque dossier contient des manifests ou des références Helm/Kustomize. Les secrets ne vont jamais en clair : utilise Sealed Secrets, SOPS ou un opérateur externe (Vault, External Secrets).

## Rollback et gestion des dérives

Rollback GitOps = revert du commit problématique dans le repo. Argo CD ou Flux resynchronise, le cluster revient à l'état précédent. Propre, traçable, reproductible.

Le **self-heal** corrige les modifications manuelles (`kubectl edit` en urgence) en revenant à l'état Git. Pratique en théorie, mais documente les interventions d'urgence pour ne pas les perdre au prochain sync.

## Conclusion

GitOps transforme le déploiement Kubernetes en problème de gestion de configuration versionnée. Git devient la source de vérité, Argo CD ou Flux le garant du cluster. Combine cette approche avec des [stratégies de déploiement Kubernetes](/blog/articles/ci-cd-kubernetes-deploiement-strategies.html) (rolling, blue/green, canary) pour livrer en confiance.
