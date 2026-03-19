---
title: "Observabilité des déploiements : logs, métriques, alertes"
date: 2025-04-03
excerpt: "Après un déploiement, savoir si tout va bien : logs de release, métriques, health checks, alertes et bonnes pratiques pour réagir vite."
type: article
tags: [CI/CD, observabilité, logs, métriques, alertes]
series: ci-cd-serie
series_order: 10
og_image: ci-cd-observabilite-1200x630.jpg
---

# Observabilité des déploiements : logs, métriques, alertes

Déployer, c’est bien. Savoir si le déploiement a réussi et si l’app tourne correctement, c’est indispensable. Voici comment structurer l’observabilité autour de la CI/CD.

---

## Pourquoi observer après un déploiement

- Détecter tout de suite une régression (erreurs 5xx, latence, crashs).
- Savoir "qui a déployé quoi et quand" (audit).
- Réduire le temps entre un problème et sa correction (rollback ou fix).

---

## Logs de déploiement

- La CI/CD doit logger : version déployée, environnement, heure, utilisateur ou job.
- Centraliser ces logs (même endroit que les logs applicatifs) pour retrouver facilement le contexte d’un incident.
- En GitOps : les commits et l’historique Git servent déjà de trace ; tu peux en plus envoyer un résumé vers un outil (Slack, email, outil de monitoring).

---

## Métriques utiles

- **Taux d’erreur** (4xx/5xx) avant / après déploiement.
- **Latence** (p50, p95, p99) pour voir une dégradation.
- **Débit** (requêtes/s) pour vérifier que le trafic arrive bien sur la nouvelle version.
- **Métriques applicatives** : file d’attente, jobs, connexions DB, etc.

Idéal : des dashboards "avant / après release" ou des comparaisons courtes (ex. 5 min avant vs 5 min après).

---

## Health checks et readiness

- En Kubernetes : **readiness** et **liveness** probes pour que le cluster ne route pas le trafic vers un pod pas prêt ou mort.
- En dehors de K8s : endpoint `/health` ou équivalent, surveillé par un load balancer ou un outil de monitoring.
- Après un déploiement, attendre que les health checks soient verts avant de considérer le release réussi (et éventuellement couper l’ancienne version).

---

## Alertes post-déploiement

- Alertes sur erreurs, latence, crashs, avec une fenêtre courte après un déploiement (ex. 10–15 min).
- Lier l’alerte au déploiement (lien vers le job CI, le commit, le tag) pour faciliter le rollback ou l’analyse.
- Éviter le bruit : seuils adaptés, regroupement des alertes, pour ne pas noyer l’équipe.

---

## Bonnes pratiques

- **Canary / blue-green** : observer la nouvelle version avant de basculer tout le trafic.
- **Runbook** : documenter ce qu’il faut faire en cas d’alerte (rollback, qui prévenir, quelles commandes).
- **Post-mortem** : après un incident lié à un déploiement, faire un retour pour améliorer tests, seuils ou processus.

---

## En résumé

- Logger chaque déploiement (version, env, heure) et centraliser.
- Suivre métriques (erreurs, latence, débit) avant et après release.
- S’appuyer sur health checks (readiness/liveness) pour la stabilité.
- Alertes ciblées + runbook + post-mortem pour réagir vite et améliorer.

Fin de la série CI/CD : tu as maintenant une vue complète du commit à la production, avec pipelines, tests, build, secrets, déploiement (K8s, GitOps), versioning, rollbacks et observabilité.
