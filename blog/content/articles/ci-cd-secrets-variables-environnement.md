---
title: "CI/CD : cacher les mots de passe (sans les coller dans Git)"
date: 2025-03-13
excerpt: "Ou mettre cles API et mots de passe pour que la chaine fonctionne sans fuite."
type: article
tags: [CI/CD, secrets, sécurité, variables, DevOps]
series: ci-cd-serie
series_order: 4
og_image: ci-cd-secrets-1200x630.jpg
---

# CI/CD : cacher les mots de passe (sans les coller dans Git)

Un **secret**, c'est un truc qu'on ne montre pas : mot de passe, cle API, certificat. Si tu le mets dans Git, considere-le **public**.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-secrets.svg" alt="Schema bons et mauvais usages des secrets" class="schema-inline" width="640" />
  <figcaption>Coffre CI et variables masquees : jamais de secret dans le code.</figcaption>
</figure>

## Les mauvais reflexes

- Fichier `.env` committe "juste pour tester"
- Secret dans un script
- Secret imprime dans les **logs** de la CI

## Les bons reflexes

- Coffre de la CI (GitHub Secrets, variables GitLab masquees…)
- Droits **limites** : chaque job n'a que ce dont il a besoin
- **Rotation** : changer une cle compromise rapidement
- Pas de secret dans l'[image Docker](/blog/articles/docker-production-registry-securite.html)

## Variables vs secrets

Les variables (URL d'API, mode debug) peuvent etre visibles. Les secrets, non. Separe-les clairement. C'est aussi vrai sur [Kubernetes](/blog/articles/kubernetes-configmaps-secrets.html).

