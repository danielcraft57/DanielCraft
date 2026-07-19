---
title: "CI/CD : du commit a la mise en ligne, automatiquement"
date: 2025-03-04
excerpt: "Une chaine qui teste et publie ton code a ta place — pour livrer plus souvent, sans trembler."
type: article
tags: [CI/CD, DevOps, pipeline, Git, déploiement]
series: ci-cd-serie
series_order: 1
og_image: ci-cd-fondamentaux-1200x630.jpg
---

# CI/CD : du commit a la mise en ligne, automatiquement

Imagine une **chaine de montage**. Tu poses une piece (ton code). Des machines verifient, emballent, puis envoient le produit. La **CI/CD**, c'est ca pour un site ou une appli.

Tu n'as plus besoin de "deployer a la main le vendredi soir en croisant les doigts".

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/cicd-pipeline-simple.svg" alt="Schema d'un pipeline CI/CD simple" class="schema-inline" width="640" />
  <figcaption>Commit, tests, build, controle, deploiement : une recette repetable.</figcaption>
</figure>

## CI et CD, en mots simples

La **CI** (integration continue) : a chaque changement, on verifie automatiquement que ca tient debout (tests, qualite, compilation).

La **CD** :
- **Delivery** : on prepare un paquet pret a installer (souvent une [image Docker](/blog/articles/docker-fondamentaux-images-conteneurs.html)).
- **Deployment** : on l'installe vraiment (parfois apres un clic "OK").

Beaucoup disent "CD" pour les deux. L'important : **automatiser** ce qui se repete.

## Pourquoi tu en as besoin (meme tout petit)

Sans CI/CD, tu as souvent :
- "Ca marche sur mon PC" mais pas ailleurs
- un oubli de fichier a la mise en ligne
- la peur de toucher a la prod

Avec une petite chaine, tu gagnes : **meme recettes**, **preuves** (tests verts), et un historique clair.

## Les etapes typiques

1. Declenchement (push, merge)
2. Installation des dependances
3. **Tests** et controles
4. **Build** (image, bundle)
5. Publication de l'artefact
6. Deploiement (staging puis prod)

Garde ca **simple** au debut. Une usine a gaz de 40 jobs pour 2 devs, ca fatigue tout le monde.

## Ce qu'il faut retenir

La CI/CD n'est pas un badge DevOps. C'est une **habitude** : chaque changement passe par le meme chemin. Dans la suite : tests qui bloquent, secrets bien ranges, Docker en CI, GitHub/GitLab, strategies de deploiement, et comment voir si ca s'est bien passe.

