---
title: "Kubernetes : voir ce qui se passe dans le cluster"
date: 2025-01-21
excerpt: "Logs, mesures et alertes pour ne pas piloter a l'aveugle."
type: article
tags: [Kubernetes, observabilité, logs, métriques, monitoring]
series: kubernetes-serie
series_order: 5
og_image: k8s-observabilite-1200x630.jpg
---

# Kubernetes : voir ce qui se passe dans le cluster

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/k8s-observabilite.svg" alt="Schema observabilite Kubernetes" class="schema-inline" width="640" />
  <figcaption>Pods, logs, mesures, alertes, action.</figcaption>
</figure>

Déployer une appli, c’est bien. Savoir **ce qui se passe** quand elle tourne en prod, c’est vital.

Dans un cluster Kubernetes, tu dois pouvoir répondre vite à des questions concrètes :

- Pourquoi ce pod est en `CrashLoopBackOff` ?
- Est-ce qu’on manque de CPU ou de RAM ?
- Quel service provoque ce pic de latence ?

Sans logs, métriques et alertes, tu pilotes à l’aveugle. Si les bases pods / nodes te manquent encore, relis d’abord les [concepts Kubernetes](/blog/articles/kubernetes-concepts-pods-nodes.html) et l’[architecture du cluster](/blog/articles/kubernetes-architecture-cluster.html).

---

## Logs applicatifs

Premier réflexe en debug :

```bash
kubectl logs mon-pod
kubectl logs mon-pod -c nom-du-container
kubectl logs -f mon-pod
```

Avec plusieurs réplicas derrière un [Deployment](/blog/articles/kubernetes-deployments-services.html) :

```bash
kubectl get pods -l app=mon-api
kubectl logs mon-api-xxxxx --tail=100
```

Astuce débutant : ajoute `--previous` si le conteneur a redémarré — tu vois les logs du crash d’avant, pas seulement le nouveau process vide.

En prod, tu enverras vite ces logs vers une stack centralisée :

- EFK (Elasticsearch + Fluentd + Kibana),
- Loki + Promtail + Grafana,
- stack cloud (CloudWatch, GCP Logging…).

Même sans ça, `kubectl logs` reste ton couteau suisse pour un incident « maintenant ».

### Checklist logs

- [ ] L’app écrit sur stdout/stderr (pas seulement dans un fichier perdu dans le conteneur)
- [ ] Les messages ont un niveau clair (`INFO`, `WARN`, `ERROR`)
- [ ] Tu peux retrouver une requête par un `request_id` ou un user id

---

## Events Kubernetes

Les **events** racontent ce que le cluster fait (scheduling, pull d’image, probes…) :

```bash
kubectl get events --sort-by=.metadata.creationTimestamp
kubectl describe pod mon-api-xxxxx
```

Events typiques :

- image introuvable (`ImagePullBackOff`),
- pas assez de ressources pour placer le pod,
- readiness / liveness qui échouent.

Quand un pod « ne démarre pas », `describe` + events te donnent souvent la réponse en 30 secondes — avant de fouiller dans Grafana.

---

## Probes de santé (liveness / readiness / startup)

Tes Deployments devraient définir des probes pour que Kubernetes sache :

- si le conteneur est vivant (**liveness**),
- s’il est prêt à recevoir du trafic (**readiness**),
- si l’init est terminée (**startup** — utile pour les apps lentes au boot).

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

Avec ça : pas de trafic vers un pod pas `Ready` ; redémarrage si la liveness échoue trop longtemps.

### Pièges fréquents

- **Même endpoint pour liveness et readiness** : un problème de dépendance (base lente) peut tuer le pod en boucle au lieu de juste le retirer du trafic.
- **Délais trop courts** : l’app n’a pas le temps de démarrer → crash loop.
- **Probe qui dépend d’un service externe** sur la liveness : tu redémarres alors que le vrai problème est ailleurs.

---

## Métriques (CPU, RAM, HPA)

Installe un **metrics-server** pour les bases :

```bash
kubectl top nodes
kubectl top pods
```

Puis un **HorizontalPodAutoscaler (HPA)** pour ajuster le nombre de pods :

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

Exemple concret : un pic de trafic à 14 h. Le HPA passe de 2 à 6 pods. Le pic retombe, le HPA redescend. Sans métriques, tu aurais surdimensionné « au feeling » — et payé pour rien la nuit.

Pense aussi aux **requests / limits** de ressources : sans requests, le scheduler et le HPA manquent de repères. Les [ConfigMaps et Secrets](/blog/articles/kubernetes-configmaps-secrets.html) ne remplacent pas une bonne config CPU/RAM.

---

## Stack d’observabilité complète

À moyen terme, vise :

- **Logs** : Loki ou Elasticsearch,
- **Métriques** : Prometheus + Grafana,
- **Traces** : OpenTelemetry,
- **Dashboards** : santé cluster, latence p95, taux d’erreur 5xx.

Tu n’as pas besoin de tout le jour 1. Prévois dès la conception : endpoint `/metrics`, logs structurés, healthchecks honnêtes. Pour la suite de la série, on branche le cluster à un pipeline propre : [CI/CD et déploiement continu sur Kubernetes](/blog/articles/kubernetes-ci-cd-deploiement-continu.html).

### Checklist « je ne vole pas à l’aveugle »

- [ ] Je sais lire les logs d’un pod en 1 commande
- [ ] Les probes sont distinctes et testées
- [ ] `kubectl top` (ou équivalent) est disponible
- [ ] Au moins une alerte critique existe (pods down, erreur 5xx)
- [ ] Un dashboard minimal montre CPU, RAM et latence du service clé

---

## En résumé

L’observabilité Kubernetes, ce n’est pas « encore un outil ». C’est pouvoir **voir, comprendre, agir** : logs pour le détail, events pour le cluster, probes pour la santé, métriques pour la charge, alertes pour ne pas découvrir le problème via un client.
