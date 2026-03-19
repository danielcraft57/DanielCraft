---
title: "Kubernetes : observabilité, logs et métriques"
date: 2025-01-21
excerpt: "Surveiller un cluster Kubernetes : logs de pods, events, métriques (CPU/RAM), probes de santé et briques d'observabilité à mettre en place."
type: article
tags: [Kubernetes, observabilité, logs, métriques, monitoring]
series: kubernetes-serie
series_order: 5
og_image: k8s-observabilite-1200x630.jpg
---

# Kubernetes : observabilité, logs et métriques

Déployer une appli, c'est bien. Savoir **ce qui se passe** quand elle tourne en prod, c'est vital.

Dans un cluster Kubernetes, tu dois pouvoir répondre rapidement à des questions comme :

- Pourquoi ce pod crash‑loop ?  
- Est‑ce qu'on manque de CPU/RAM ?  
- Quels sont les pods à l'origine d'un pic de latence ?

---

## Logs applicatifs

Premier réflexe :

```bash
kubectl logs mon-pod
kubectl logs mon-pod -c nom-du-container
kubectl logs -f mon-pod
```

Pour plusieurs réplicas derrière un Deployment :

```bash
kubectl get pods -l app=mon-api
kubectl logs mon-api-xxxxx
```

En prod, tu voudras rapidement envoyer ces logs vers une stack centralisée :

- EFK (Elasticsearch + Fluentd + Kibana),
- Loki + Promtail + Grafana,
- Stack cloud (CloudWatch, GCP Logging, etc.).

Mais même sans ça, `kubectl logs` reste ton couteau suisse pour du debug rapide.

---

## Events Kubernetes

Les **events** te racontent ce que le cluster fait :

```bash
kubectl get events --sort-by=.metadata.creationTimestamp
```

Tu peux les filtrer par namespace ou par ressource :

```bash
kubectl describe pod mon-api-xxxxx
```

Les events typiques :

- pod qui ne trouve pas son image,
- problème de scheduling (pas assez de ressources),
- erreur de readiness/liveness probe.

---

## Probes de santé (liveness / readiness / startup)

Tes deployments devraient définir des probes pour que Kubernetes sache :

- si le conteneur est vivant (**liveness**),
- s'il est prêt à recevoir du trafic (**readiness**),
- si l'initialisation est terminée (**startup**).

Exemple :

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 3000
  initialDelaySeconds: 10
  periodSeconds: 15

readinessProbe:
  httpGet:
    path: /ready
    port: 3000
  initialDelaySeconds: 5
  periodSeconds: 10
```

Avec ça :

- Kubernetes ne route du trafic vers ton pod que s'il est `Ready`.
- Si le pod bloque ou ne répond plus, la liveness probe peut déclencher un redémarrage.

---

## Métriques (CPU, RAM, HPA)

Tu peux installer un **metrics-server** pour avoir des métriques de base :

```bash
kubectl top nodes
kubectl top pods
```

Ensuite, tu peux configurer un **HorizontalPodAutoscaler (HPA)** :

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: mon-api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: mon-api
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

Kubernetes ajuste alors le nombre de pods en fonction de la charge CPU.

---

## Stack d'observabilité complète

À plus long terme, vise quelque chose comme :

- **Logs** : Loki ou Elasticsearch,
- **Métriques** : Prometheus + Grafana,
- **Traces** : OpenTelemetry,
- **Dashboards** : Grafana (santé du cluster, services clés, latence).

L'idée n'est pas de tout mettre en place dès le jour 1, mais de prévoir des hooks (export de métriques, endpoints `/metrics`, etc.) dès la conception de tes services.

Dans le dernier article de la série Kubernetes, on parlera **CI/CD et déploiement continu** : comment brancher ton cluster à ton pipeline pour que les déploiements soient reproductibles et fiables.
