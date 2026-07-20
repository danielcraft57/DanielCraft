---
title: "Versions et retours arriere : livrer sans paniquer"
date: 2025-04-01
excerpt: "Tags, releases et rollback : savoir exactement ce qui tourne, et revenir vite."
type: article
tags: [CI/CD, versioning, releases, rollback, sémantique]
series: ci-cd-serie
series_order: 9
og_image: ci-cd-versioning-1200x630.jpg
---

# Versions et retours arriere : livrer sans paniquer

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-versioning.svg" alt="Schema versioning release rollback" class="schema-inline" width="640" />
  <figcaption>Tag, release, deploy, probleme, rollback.</figcaption>
</figure>

Une bonne CI/CD ne suffit pas si tes versions sont floues et tes rollbacks chaotiques. Quand un bug critique arrive en prod un vendredi soir, la question n’est pas « qui a cassé quoi ? » : c’est « quelle version tourne, et comment revenir à une version saine en moins de cinq minutes ? ». Voici comment structurer releases et retours en arrière sans improvisation.

---

## Pourquoi versionner proprement

Sans numéro clair, tu navigues à vue. Avec un versioning sérieux, tu gagnes trois choses concrètes :

- **Traçabilité** : savoir exactement ce qui tourne en prod (tag d’image, commit, changelog).
- **Rollback ciblé** : revenir à `v1.4.2`, pas à « le build d’hier vers 17 h ».
- **Changelog** : communiquer ce qui a changé à l’équipe, au support et parfois aux clients.

C’est le pendant naturel des [stratégies de déploiement Kubernetes](/blog/articles/ci-cd-kubernetes-deploiement-strategies.html) : blue-green ou canary ne servent à rien si tu ne sais pas quelle version est sur quelle couleur.

---

## Versioning sémantique (SemVer)

Format classique : `MAJOR.MINOR.PATCH` (ex. `2.1.3`).

- **MAJOR** : changements incompatibles (breaking) — une API qui casse les clients, une migration irréversible.
- **MINOR** : nouvelles fonctionnalités rétrocompatibles.
- **PATCH** : corrections de bugs, sans changement d’API.

Exemple concret : tu corriges un bug de calcul de TVA → `1.3.1` → `1.3.2`. Tu ajoutes un endpoint `/invoices/export` sans casser l’existant → `1.3.2` → `1.4.0`. Tu renommes un champ JSON obligatoire → `1.4.0` → `2.0.0`.

En CI/CD, le tag Git ou le numéro de build alimente souvent le tag d’image Docker et les manifests (Kubernetes, Helm). Un article utile côté images : [builder des images Docker en CI](/blog/articles/ci-cd-build-images-docker.html).

---

## Tags Git et builds

- Branche `main` : chaque merge peut déclencher un build ; la release, elle, porte un tag stable (`v1.2.3`).
- Les tags Git servent de point de release : **ne pas les déplacer**, les créer depuis la CI après tests verts.
- Évite le mélange « parfois un tag, parfois un hash de commit affiché à la main dans Slack ».

Conseil : un seul endroit qui « décide » du numéro (script, CI, ou outil type `semantic-release`) pour éviter les incohérences entre GitHub Release, image registry et Helm chart.

### Exemple de flux simple

1. Merge sur `main` → build + tests.
2. Tag `v1.5.0` créé automatiquement (ou manuellement après validation staging).
3. Image `registry.example/app:1.5.0` poussée.
4. Staging puis prod pointent vers `1.5.0`, pas vers `latest`.

---

## Changelog et release notes

- Fichier `CHANGELOG.md` (ou équivalent) mis à jour à chaque release.
- En CI : tu peux générer des notes à partir des commits conventionnels (`feat:`, `fix:`, `breaking:`) ou des tickets.
- Les release notes aident pour le rollback (savoir ce qu’on enlève) et pour le support (« depuis la 1.4, le bouton X a bougé »).

Piège fréquent : un changelog vide ou recopié à la va-vite. Mieux vaut trois lignes honnêtes qu’une page de marketing.

---

## Environnements et promotion

Typique : **dev → staging → prod**.

- Chaque environnement pointe vers une version (tag d’image ou commit).
- La « promotion » = mettre à jour la référence (Helm values, repo GitOps) vers un tag déjà validé en staging.
- Éviter de déployer « le dernier build » en prod sans passer par un tag de release.

Avec [GitOps (Argo / Flux)](/blog/articles/ci-cd-gitops-argo-flux.html), la promotion devient un commit : `image: app:1.5.0` → `image: app:1.5.1`. Le rollback, c’est souvent un revert de ce commit.

---

## Stratégie de rollback

1. **Définir** ce qu’est un rollback : revenir à la version N-1 (ou à un tag précis documenté).
2. **Documenter** : quelle commande, quel manifest, quel tag — dans un runbook d’une page.
3. **Automatiser** si possible : bouton « rollback », `kubectl rollout undo`, ou revert GitOps.
4. **Vérifier** après retour : health checks verts, taux d’erreur redevenu normal (voir [l’observabilité des déploiements](/blog/articles/ci-cd-observabilite-deploiements.html)).
5. **Post-mortem** : après un rollback, analyser la cause pour éviter la récidive.

### Checklist avant d’appeler un rollback « prêt »

- [ ] La version précédente est toujours disponible dans le registry (pas purgée).
- [ ] Les migrations de base sont rétrocompatibles (ou un plan de downgrade existe).
- [ ] Quelqu’un sait lancer le rollback sans ouvrir cinq onglets de doc.
- [ ] Les secrets / config de l’ancienne version sont toujours valides.

---

## Pièges fréquents

- Utiliser `latest` en prod : impossible de savoir ce qui tourne vraiment.
- Déplacer un tag Git après coup : tu réécris l’histoire et tu sèmes le chaos.
- Rollback d’app sans penser à la base : la version N-1 plante si le schéma a déjà évolué.
- Numéro de version différent entre image, chart Helm et release notes.

---

## En résumé

- Utilise le versioning sémantique et des tags Git stables.
- Un changelog et des release notes améliorent la traçabilité.
- Promouvoir des versions entre environnements (pas « dernier build » en prod).
- Rollback = processus clair, documenté, idéalement automatisé.

Prochaine étape logique : [observer après le déploiement](/blog/articles/ci-cd-observabilite-deploiements.html) (logs, métriques, alertes) pour décider vite si tu gardes la release… ou si tu reviens en arrière.
