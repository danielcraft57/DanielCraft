---
title: "Kubernetes : reglages et secrets hors de l'image"
date: 2025-01-16
excerpt: "ConfigMaps pour la config visible, Secrets pour ce qui doit rester cache."
type: article
tags: [Kubernetes, ConfigMap, Secret, configuration]
series: kubernetes-serie
series_order: 4
og_image: k8s-configmaps-secrets-1200x630.jpg
---

# Kubernetes : reglages et secrets hors de l'image

Ne colle pas tes mots de passe dans l'**image**. Mets la config a part.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/k8s-config-secrets.svg" alt="Schema ConfigMaps et Secrets" class="schema-inline" width="640" />
  <figcaption>Config non secrete vs secrets proteges.</figcaption>
</figure>

## Deux tiroirs

- **ConfigMap** : reglages (URL, options)
- **Secret** : cles, mots de passe (acces limite)

Meme regle qu'en [CI/CD](/blog/articles/ci-cd-secrets-variables-environnement.html) : ce qui est dans Git en clair n'est plus secret.

