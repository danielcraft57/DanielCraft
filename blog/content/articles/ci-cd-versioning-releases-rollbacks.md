---
title: "Versioning, releases et rollbacks : livrer sans casser"
date: 2025-04-01
excerpt: "Tags, sémantique, changelog, environnements et rollbacks : une stratégie de release cohérente pour la CI/CD et la traçabilité."
type: article
tags: [CI/CD, versioning, releases, rollback, sémantique]
series: ci-cd-serie
series_order: 9
og_image: ci-cd-versioning-1200x630.jpg
---

# Versioning, releases et rollbacks : livrer sans casser

Une bonne CI/CD ne suffit pas si tes versions sont floues et tes rollbacks chaotiques. Voici comment structurer releases et retours en arrière.

---

## Pourquoi versionner proprement

- **Traçabilité** : savoir exactement ce qui tourne en prod.
- **Rollback ciblé** : revenir à une version connue, pas à "hier".
- **Changelog** : communiquer ce qui a changé (équipe, clients, support).

---

## Versioning sémantique (SemVer)

Format classique : `MAJOR.MINOR.PATCH` (ex. `2.1.3`).

- **MAJOR** : changements incompatibles (breaking).
- **MINOR** : nouvelles fonctionnalités rétrocompatibles.
- **PATCH** : corrections de bugs, pas de changement d’API.

En CI/CD : le tag Git ou le numéro de build alimente souvent le tag d’image Docker et les manifests (Kubernetes, Helm).

---

## Tags Git et builds

- Branche `main` / `master` : chaque merge peut déclencher un build et un tag (ex. `v1.2.3` ou `1.2.3-build.123`).
- Les tags Git (`v1.0.0`) servent de point de release : ne pas les déplacer, les créer depuis la CI après tests verts.

Conseil : un seul endroit qui "décide" du numéro (script, CI, ou outil type `semantic-release`) pour éviter les incohérences.

---

## Changelog et release notes

- Fichier `CHANGELOG.md` (ou équivalent) mis à jour à chaque release.
- En CI : tu peux générer des notes à partir des commits (conventionnel commits) ou des tickets.
- Les release notes aident pour le rollback (savoir ce qu’on enlève) et pour la communication.

---

## Environnements et promotion

Typique : **dev → staging → prod**.

- Chaque environnement pointe vers une version (tag d’image ou commit).
- La "promotion" = mettre à jour la référence (ex. Helm values, GitOps repo) vers un tag validé en staging.
- Éviter de déployer "le dernier build" en prod sans passer par un tag de release.

---

## Stratégie de rollback

1. **Définir** ce qu’est un rollback : revenir à la version N-1 (ou à un tag précis).
2. **Documenter** : quelle commande, quel manifest, quel tag.
3. **Automatiser** si possible : bouton "rollback" qui repointe vers la version précédente (GitOps revert, `kubectl rollout undo`, etc.).
4. **Post-mortem** : après un rollback, analyser la cause pour éviter la récidive.

---

## En résumé

- Utilise le versioning sémantique et des tags Git stables.
- Un changelog et des release notes améliorent la traçabilité.
- Promouvoir des versions entre environnements (pas "dernier build" en prod).
- Rollback = processus clair, documenté, idéalement automatisé.

Prochain article : observabilité des déploiements (logs, métriques, alertes) pour voir ce qui se passe après un release.
