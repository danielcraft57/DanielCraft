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

Un cluster sans **observabilite**, c'est un immeuble sans fenetres. Tu entends du bruit, tu ne vois rien.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/k8s-observabilite.svg" alt="Schema observabilite Kubernetes" class="schema-inline" width="640" />
  <figcaption>Pods, logs, mesures, alertes, action.</figcaption>
</figure>

## Le minimum

- Logs des pods
- Mesures (CPU, memoire, erreurs)
- Alertes rares mais utiles
- Une idee de "normal" vs "casse"

Ca complete l'[observabilite des deploiements](/blog/articles/ci-cd-observabilite-deploiements.html).

