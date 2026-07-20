---
title: "CI/CD : cacher les mots de passe (sans les coller dans Git)"
date: 2025-03-13
excerpt: "Ou mettre cles API et mots de passe pour que la chaine fonctionne sans fuite."
type: article
tags: [CI/CD, secrets, sécurité, variables, DevOps]
series: ci-cd-serie
series_order: 4
og_image: ci-cd-secrets-1200x630.jpg
---

# CI/CD : cacher les mots de passe (sans les coller dans Git)

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-secrets.svg" alt="Schema bons et mauvais usages des secrets" class="schema-inline" width="640" />
  <figcaption>Coffre CI et variables masquees : jamais de secret dans le code.</figcaption>
</figure>

La CI/CD manipule souvent des choses sensibles : tokens registry (push/pull d’images), clés API (Sentry, Stripe…), accès base de données de staging, kubeconfig ou credentials cloud. Une fuite de secret, c’est le genre de truc qui te ruine une soirée — et parfois un compte bancaire ou un cluster entier.

Ici, on pose des règles simples, des exemples concrets et une checklist pour dormir un peu mieux. Si tu construis encore ton pipeline, commence par les [fondamentaux CI/CD](/blog/articles/ci-cd-fondamentaux-pipelines.html), puis reviens ici pour verrouiller les accès.

---

## La règle numéro 1

**Aucun secret dans le repo.**

Ni dans :

- le code source,
- les manifests Kubernetes versionnés en clair,
- les Dockerfile (`ENV PASSWORD=...` est une mauvaise idée),
- les fichiers `.env` committés.

Si un secret a fuité (commit poussé, screenshot Slack, log CI), considère qu’il est compromis et **rotate** immédiatement : révoque l’ancien, crée le nouveau, mets à jour les coffres.

### Piège classique

Tu ajoutes un `.env` dans `.gitignore`… après l’avoir déjà commité. Git ignore le futur, pas le passé. Il faut retirer le fichier de l’historique (ou au minimum le supprimer du tracking) **et** rotator toutes les valeurs exposées.

---

## Secrets vs variables

### Variables « publiques » (ok dans le repo)

- noms d’environnements (`APP_ENV=staging`),
- flags sans impact sécurité (`FEATURE_X=true`),
- URLs publiques (`API_PUBLIC_URL=https://api.exemple.fr`).

### Secrets (jamais en clair)

- mots de passe,
- tokens et clés API,
- clés privées SSH / TLS,
- certificats,
- kubeconfig complet,
- chaînes de connexion avec credentials.

Astuce : tout ce qui permet d’agir « au nom de » quelque chose (écrire en base, déployer, payer) est un secret.

---

## Où stocker les secrets ?

Trois niveaux, du plus simple au plus mature :

1. **Secrets CI** (GitHub Actions Secrets, GitLab CI Variables masquées, etc.)  
   Très bien pour démarrer un [workflow GitHub Actions](/blog/articles/ci-cd-github-actions-workflow-complet.html) ou un [pipeline GitLab CI](/blog/articles/ci-cd-gitlab-ci-pipeline-complet.html).

2. **Secret manager** (Vault, AWS Secrets Manager, GCP Secret Manager)  
   Plus solide : rotation, audit, policies d’accès.

3. **Kubernetes Secrets** (idéalement via External Secrets Operator)  
   Pour que l’app récupère les secrets côté cluster, sans les coller dans Git.

L’idée : éviter que la CI devienne un coffre-fort géant non maîtrisé. La CI *injecte* ou *récupère* ; elle n’est pas forcément la source de vérité à long terme.

---

## Comment injecter un secret dans un job CI

Principe : le secret arrive en variable d’environnement au runtime, jamais écrit dans le dépôt.

Exemple :

```bash
echo "$REGISTRY_TOKEN" | docker login ghcr.io -u "$REGISTRY_USER" --password-stdin
```

Ce qui compte vraiment :

- ne jamais `echo` le secret dans les logs,
- désactiver le mode debug qui dump l’environnement,
- limiter le scope et la durée de vie des tokens (lecture seule staging ≠ admin prod),
- préférer `--password-stdin` aux arguments en ligne de commande (visibles dans `ps`).

---

## Cas concret : kubeconfig

Tu peux stocker un kubeconfig dans un secret CI (base64), puis le reconstruire à l’exécution :

```bash
echo "$KUBECONFIG_B64" | base64 -d > kubeconfig.yml
export KUBECONFIG="$PWD/kubeconfig.yml"
kubectl get nodes
```

Bonnes pratiques :

- kubeconfig dédié **staging** / **prod**,
- comptes séparés,
- droits minimum (RBAC) : un job de déploiement n’a pas besoin de supprimer le cluster,
- supprimer le fichier en fin de job si possible.

Pour le déploiement lui-même, vois aussi les [stratégies Kubernetes](/blog/articles/ci-cd-kubernetes-deploiement-strategies.html).

---

## Rotations, scopes, environnements

Un setup sain ressemble à ça :

- secrets **par environnement** (staging ≠ prod),
- le token staging ne donne **jamais** accès à prod,
- rotation régulière (automatique si possible),
- audit : qui a accès à quels secrets dans GitHub / GitLab / le cloud.

### Checklist express

- [ ] Aucun secret dans Git (recherche `password`, `api_key`, `AKIA…`).
- [ ] Secrets CI masqués / protégés par environnement.
- [ ] Tokens à durée limitée ou révocables facilement.
- [ ] Accès prod restreint (protected branches / environments).
- [ ] Plan de rotation documenté (même une demi-page).

---

## Et dans Kubernetes ?

La CI/CD ne devrait pas injecter des secrets dans les pods via des manifests committés en clair (`stringData: password: SuperSecret123`).

Approches propres :

- External Secrets Operator + secret manager,
- sealed-secrets (chiffrement dans Git, déchiffrement dans le cluster),
- Vault Agent sidecar.

Avec [GitOps](/blog/articles/ci-cd-gitops-argo-flux.html), tu versionnes la *référence* au secret, pas le secret lui-même.

---

## Pièges fréquents

- Copier un secret dans un ticket Jira ou un message Slack « juste pour tester ».
- Réutiliser le même token pour CI, laptop du stagiaire et script local.
- Laisser `CI_DEBUG_TRACE=true` (GitLab) ou un équivalent qui affiche les variables.
- Oublier les secrets dans les artefacts de build (logs Docker, fichiers temporaires uploadés).

---

## En résumé

- Zéro secret dans le repo ; en cas de fuite, rotate tout de suite.
- Distinguer variables publiques et secrets.
- Commencer par les secrets CI, monter en maturité avec un secret manager.
- Injecter au runtime, logger avec précaution, séparer staging et prod.

Prochain article de la série côté pratique : un [workflow GitHub Actions complet](/blog/articles/ci-cd-github-actions-workflow-complet.html) (build Docker, push registry, déploiement Kubernetes).
