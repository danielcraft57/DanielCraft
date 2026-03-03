---
title: "CI/CD : gérer les secrets et variables d'environnement (sans fuite)"
date: 2026-02-08
excerpt: "API keys, mots de passe, kubeconfig, tokens de registry : où les stocker, comment les injecter dans le pipeline, et quoi éviter absolument."
type: article
tags: [CI/CD, secrets, sécurité, variables, DevOps]
series: ci-cd-serie
series_order: 4
og_image: ci-cd-secrets-1200x630.jpg
---

# CI/CD : gérer les secrets et variables d'environnement (sans fuite)

La CI/CD manipule souvent des choses sensibles :

- tokens registry (push/pull d'images),
- clés API (Sentry, Stripe, OpenAI…),
- accès base de données (staging),
- kubeconfig / credentials cloud.

Une fuite de secret, c'est le genre de truc qui te ruine une soirée (et parfois un week-end).

Ici, on met des règles simples et une méthode.

---

## La règle numéro 1

**Aucun secret dans le repo.**

Ni dans :

- le code,
- les manifests Kubernetes versionnés en clair,
- les Dockerfile,
- les fichiers `.env` committés.

Si un secret a fuité, considère qu'il est compromis et **rotate** immédiatement.

---

## Secrets vs variables

### Variables "publiques" (ok dans le repo)

- noms d'environnements,
- flags sans impact (ex: `FEATURE_X=true`),
- URLs non sensibles (ex: URL publique d'un endpoint).

### Secrets (jamais en clair)

- passwords,
- tokens,
- clés privées,
- certificats,
- kubeconfig complet.

---

## Où stocker les secrets ?

Trois niveaux :

1. **Secrets CI** (GitHub Actions Secrets, GitLab CI Variables, etc.)  
   Très bien pour commencer.

2. **Secret manager** (Vault, AWS Secrets Manager, GCP Secret Manager)  
   Plus solide, plus traçable.

3. **Kubernetes Secrets** (ou External Secrets Operator)  
   Pour que l'app récupère les secrets côté cluster.

L'idée : éviter que la CI devienne un coffre‑fort géant non maîtrisé.

---

## Comment injecter un secret dans un job CI

Principe : le secret arrive en variable d'environnement au runtime.

Exemple pseudo :

```bash
echo "$REGISTRY_TOKEN" | docker login ghcr.io -u "$REGISTRY_USER" --password-stdin
```

Ce qui est important :

- ne jamais `echo` le secret dans les logs,
- désactiver le debug si ça affiche l'environnement,
- limiter le scope et la durée de vie des tokens.

---

## Cas concret : kubeconfig

Tu peux stocker un kubeconfig dans un secret CI (base64), puis le reconstruire à l'exécution :

```bash
echo "$KUBECONFIG_B64" | base64 -d > kubeconfig.yml
export KUBECONFIG="$PWD/kubeconfig.yml"
kubectl get nodes
```

Bonnes pratiques :

- kubeconfig dédié **staging** / **prod**,
- comptes séparés,
- droits minimum (RBAC).

---

## Rotations, scopes, environnements

Un setup sain :

- secrets par environnement (staging/prod),
- token staging ne donne jamais accès à prod,
- rotation régulière (automatique si possible),
- audit (qui a accès à quoi).

---

## Et dans Kubernetes ?

La CI/CD ne devrait pas injecter directement des secrets dans les pods via des manifests committés en clair.

Approches propres :

- External Secrets Operator (K8s) + secret manager,
- sealed-secrets (chiffrement dans Git),
- Vault Agent sidecar.

---

Prochain article : un workflow **GitHub Actions** complet (avec build d'image Docker, push registry, déploiement Kubernetes et contrôle de rollout).
