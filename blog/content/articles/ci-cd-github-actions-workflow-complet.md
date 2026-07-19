---
title: "GitHub Actions : une recette automatique pour ton projet"
date: 2025-03-18
excerpt: "Un workflow simple : tester, construire, deployer — explique sans jargon."
type: article
tags: [CI/CD, GitHub Actions, Docker, DevOps, déploiement]
series: ci-cd-serie
series_order: 5
og_image: ci-cd-github-actions-1200x630.jpg
---

# GitHub Actions : une recette automatique pour ton projet

**GitHub Actions**, c'est le robot de GitHub. Tu ecris une recette (YAML). A chaque push, il execute.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-github-actions.svg" alt="Schema d'un workflow GitHub Actions" class="schema-inline" width="640" />
  <figcaption>Declencheur, jobs, artefacts, environnements.</figcaption>
</figure>

## En pratique

1. Un evenement (push sur `main`, pull request)
2. Des **jobs** : test, build, deploy
3. Des secrets ranges dans les reglages du repo
4. Souvent : staging d'abord, prod ensuite

Garde un workflow **lisible**. Si personne ne comprend le fichier, personne ne l'entretient. Pour une alternative, vois [GitLab CI](/blog/articles/ci-cd-gitlab-ci-pipeline-complet.html).

