---
title: "Apres le deploiement : voir si ca va vraiment bien"
date: 2025-04-03
excerpt: "Logs, mesures et alertes utiles pour savoir si la nouvelle version tient la route."
type: article
tags: [CI/CD, observabilité, logs, métriques, alertes]
series: ci-cd-serie
series_order: 10
og_image: ci-cd-observabilite-1200x630.jpg
---

# Apres le deploiement : voir si ca va vraiment bien

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-observabilite.svg" alt="Schema observabilite apres deploiement" class="schema-inline" width="640" />
  <figcaption>Logs, mesures, alertes, dashboards.</figcaption>
</figure>

Déployer, c’est bien. Savoir si le déploiement a réussi *et* si l’app tient vraiment la route, c’est indispensable. Un job CI vert ne dit pas que les utilisateurs sont contents : il dit seulement que les étapes automatisées ont passé. Voici comment structurer l’observabilité autour de la CI/CD.

Complément naturel du [versioning / rollback](/blog/articles/ci-cd-versioning-releases-rollbacks.html) : tu as une version claire — encore faut-il *voir* quand revenir en arrière.

---

## Pourquoi observer après un déploiement

- Détecter tout de suite une régression (erreurs 5xx, latence, crashs).
- Savoir « qui a déployé quoi et quand » (audit).
- Réduire le temps entre un problème et sa correction (rollback ou hotfix).

Sans observabilité, tu apprends le bug via un client ou un message Slack. Avec, tu le vois en minutes — parfois avant que tout le trafic bascule (canary).

---

## Logs de déploiement

La CI/CD doit logger au minimum : version (tag ou commit), environnement, heure UTC, déclencheur (utilisateur ou job).

Centralise ces logs avec les logs applicatifs. En GitOps ([Argo / Flux](/blog/articles/ci-cd-gitops-argo-flux.html)), l’historique Git sert déjà de trace ; un résumé Slack du type « `billing-api` prod → `v2.3.1` — pipeline #889 » suffit pour corréler dashboard et release.

---

## Métriques utiles

- **Taux d’erreur** (4xx/5xx) avant / après déploiement.
- **Latence** (p50, p95, p99) pour voir une dégradation.
- **Débit** (requêtes/s) pour vérifier que le trafic arrive bien sur la nouvelle version.
- **Métriques applicatives** : file d’attente, jobs en échec, connexions DB, saturations.

Idéal : un dashboard « avant / après release » ou une comparaison courte (5 min avant vs 5 min après). Si le p95 double pendant que les 5xx montent, tu as ton signal de rollback — lié à ta [stratégie de versioning](/blog/articles/ci-cd-versioning-releases-rollbacks.html).

### Checklist « 15 minutes après deploy »

- [ ] Taux 5xx stable ou en baisse
- [ ] Latence p95 dans la fourchette habituelle
- [ ] Pas de pic de restart / OOM
- [ ] Health checks verts
- [ ] Pas d’alerte critique ouverte liée au service

---

## Health checks et readiness

- En Kubernetes : probes **readiness** et **liveness** pour que le cluster ne route pas le trafic vers un pod pas prêt ou mort. Détails pratiques dans les [stratégies de déploiement K8s](/blog/articles/ci-cd-kubernetes-deploiement-strategies.html).
- Hors K8s : endpoint `/health` (ou équivalent), surveillé par le load balancer ou un outil de monitoring.
- Après un déploiement, attendre que les health checks soient verts avant de considérer le release réussi — et éventuellement couper l’ancienne version.

Piège : un `/health` qui répond `200` alors que la base est down. Un bon check vérifie les dépendances critiques (DB, cache) sans être trop lent.

---

## Alertes post-déploiement

- Alertes sur erreurs, latence, crashs, avec une fenêtre courte après un déploiement (ex. 10–15 min).
- Lier l’alerte au déploiement (lien vers le job CI, le commit, le tag) pour faciliter le rollback ou l’analyse.
- Éviter le bruit : seuils adaptés, regroupement, silence sur staging si besoin — sinon l’équipe ignore tout.

### Règle simple

Une alerte doit entraîner une action. Si personne ne sait quoi faire, ce n’est pas une alerte : c’est du bruit. Documente l’action dans un runbook d’une page.

---

## Bonnes pratiques

- **Canary / blue-green** : observer une fraction du trafic avant de basculer à 100 %.
- **Runbook** : rollback ? Qui prévenir ? Quelles commandes ?
- **Post-mortem** : améliorer tests ([quality gates](/blog/articles/ci-cd-tests-qualite-gates.html)) et seuils, pas seulement corriger le bug.
- **Corrélation** : une timeline (deploy + métriques + logs) plutôt que trois outils déconnectés.

---

## Pièges fréquents

- Se fier uniquement au « Deploy succeeded » de la CI.
- Alertes trop sensibles → fatigue, puis silence le jour du vrai incident.
- Pas de baseline : impossible de savoir si « 200 ms de p95 » est normal.
- Logs de deploy sans numéro de version.
- Observer seulement la prod (un smoke staging aurait vu le problème).

---

## Mini scénario

Tu déploies `v1.9.0`. Job CI vert. Deux minutes plus tard : 5xx de 0,2 % à 4 %, p95 qui double. L’alerte pointe le tag `v1.9.0`. Rollback vers `v1.8.4`, checklist des 15 minutes, puis post-mortem : un test d’intégration manquait sur le paiement.

Boucle utile : déployer → observer → décider → améliorer les portes qualité.

---

## En résumé

- Logger chaque déploiement (version, env, heure) et centraliser.
- Suivre erreurs, latence et débit avant / après release.
- Health checks + alertes actionnables + runbook + post-mortem.

Fin de la série CI/CD : du commit à la prod — [tests](/blog/articles/ci-cd-tests-qualite-gates.html), [Docker](/blog/articles/ci-cd-build-images-docker.html), [secrets](/blog/articles/ci-cd-secrets-variables-environnement.html), K8s/GitOps, versioning et observabilité.
