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

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-k8s-strategies.svg" alt="Schema strategies de deploiement Kubernetes" class="schema-inline" width="640" />
  <figcaption>Rolling, blue/green, canary et rollback.</figcaption>
</figure>

Kubernetes gère nativement le remplacement progressif des pods via le Deployment. Mais selon ton trafic, ton niveau de risque et tes exigences de disponibilité, tu ne déploies pas toujours de la même manière. Rolling update, blue/green ou canary : chaque stratégie a son contexte.

## Rolling update : le comportement par défaut

C'est ce que fait un Deployment Kubernetes out of the box : les anciens pods sont remplacés progressivement par les nouveaux, sans coupure totale du service.

Paramètres clés dans le Deployment :

```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1        # pods supplémentaires temporaires
      maxUnavailable: 0  # aucun pod indisponible pendant le rollout
```

Conditions de succès :

- Pods **stateless** (pas d'état local critique)
- **Readiness probes** fiables (le pod n reçoit du trafic que quand il est prêt)
- **Migrations base de données** compatibles (backward compatible ou exécutées avant le rollout)

Commandes indispensables :

```bash
kubectl rollout status deployment/mon-api
kubectl rollout undo deployment/mon-api
kubectl rollout history deployment/mon-api
```

Le rolling update convient à la majorité des applications web classiques. Simple, intégré, suffisant pour un trafic modéré.

## Blue/Green : basculer d'un coup

Deux environnements coexistent :

- **Blue** : version actuelle en production
- **Green** : nouvelle version déployée en parallèle

Tu déploies green, tu testes (tests fonctionnels, smoke tests, validation QA), puis tu bascules le trafic d'un coup en modifiant le Service ou l'Ingress.

Avantages :

- Rollback instantané (reswitch vers blue)
- Tests réalistes sur green avant bascule
- Pas de mélange de versions côté utilisateur

Inconvénients :

- Double consommation de ressources pendant la transition
- Migrations DB plus délicates (deux versions doivent cohabiter ou migration avant bascule)

Implémentation courante : deux Deployments (`mon-api-blue`, `mon-api-green`) et un Service dont le selector pointe sur l'un ou l'autre. Certains Ingress controllers (NGINX, Traefik) permettent de switcher le backend sans modifier le Service.

## Canary : progresser par paliers

Tu envoies progressivement du trafic vers la nouvelle version :

- 5 % des requêtes → nouvelle version
- Observation des métriques (erreurs, latence)
- Montée à 20 %, 50 %, 100 % si tout va bien
- Rollback automatique si les métriques dégradent

Avantages :

- Impact limité en cas de bug
- Validation en conditions réelles avec du vrai trafic
- Décision data-driven

Inconvénients :

- Complexité accrue (routing, observabilité, logique de promotion)
- Deux versions en production simultanément (compatibilité API/DB requise)

Outils fréquents :

- **Argo Rollouts** : CRD Kubernetes avec steps de canary configurables
- **Flagger** : canary automatisé avec Linkerd/Istio/NGINX
- **Service mesh** (Istio, Linkerd) : contrôle fin du trafic par pourcentage

Un canary sans métriques fiables, c'est un déploiement aléatoire déguisé.

## Le socle commun : probes et observabilité

Quelle que soit la stratégie, trois prérequis :

### Readiness probe

Vérifie que le pod est prêt à recevoir du trafic. Sans elle, Kubernetes route vers des pods encore en démarrage → erreurs 502.

### Liveness probe

Redémarre un pod bloqué. Distincte de la readiness : un pod live mais pas ready ne reçoit pas de trafic.

### Métriques et alerting

Taux d'erreur HTTP 5xx, latence p95/p99, saturation CPU/mémoire. Connecte Prometheus/Grafana ou ton APM. Configure des alertes avant le déploiement, pas après l'incident.

## Comment choisir sa stratégie

| Contexte | Stratégie recommandée |
|----------|----------------------|
| Projet simple, faible trafic | Rolling update |
| Besoin de switch instant + rollback facile | Blue/green |
| Gros trafic, risque élevé, SRE mature | Canary |
| Migration majeure incompatible | Blue/green + maintenance |

Commence par le rolling update. Passe au blue/green quand tu as besoin de validation avant bascule. Adopte le canary quand tu as l'observabilité pour piloter la montée en charge.

## Conclusion

Kubernetes offre le rolling update natif, mais blue/green et canary répondent à des exigences de disponibilité plus strictes. Probes fiables et métriques en temps réel sont le socle de toute stratégie. Pour aller plus loin en équipe, combine ces approches avec le [GitOps (Argo CD / Flux)](/blog/articles/ci-cd-gitops-argo-flux.html) : le cluster suit Git, et tu choisis la stratégie de rollout adaptée à chaque application.
