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

Deployer sans regarder, c'est comme livrer un colis sans confirmer qu'il est arrive. L'**observabilite**, c'est voir ce qui se passe.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-observabilite.svg" alt="Schema observabilite apres deploiement" class="schema-inline" width="640" />
  <figcaption>Logs, mesures, alertes, dashboards.</figcaption>
</figure>

## Le trio de base

- **Logs** : l'histoire ecrite
- **Mesures** : erreurs, latence, CPU
- **Alertes** : seulement ce qui merite un reveil

Apres chaque deploiement : une checklist de 5 minutes. Sur Kubernetes, vois aussi [l'observabilite cluster](/blog/articles/kubernetes-observabilite-logs-metrics.html).

