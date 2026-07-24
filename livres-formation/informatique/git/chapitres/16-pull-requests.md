# Chapitre 16 - Pull requests (PR)

Une pull request = "peux-tu fusionner mon travail dans la branche principale ?"

C'est le coeur de la collab sur GitHub.

## Scenario type

Tu crees une branche avec `git switch -c feature/login`, tu fais tes commits locaux, puis `git push -u origin feature/login`. Sur GitHub, tu cliques **Compare & pull request**. Tu remplis titre + description. Quelqu'un review. On merge sur GitHub. En local, tu reviens avec `git switch main` puis `git pull`.

## Pourquoi pas merger en silence ?

Ca permet la relecture, la discussion, les tests automatiques (CI), et un historique plus clair. Meme en solo, une PR t'oblige a resumer ton travail. C'est sain.

## Bonne description

```text
## But
Ajouter un formulaire de contact.

## Changes
- page contact.html
- validation email basique

## Test
Ouvrir /contact et envoyer un faux message.
```

## Draft PR

Tu peux ouvrir une PR en brouillon.
Utile pour montrer l'avancement sans demander le merge tout de suite.

## Review

En review, on commente des lignes.
Tu pousses des commits sur la meme branche : la PR se met a jour.

## Merge buttons

Tu verras souvent **Create a merge commit**, **Squash and merge** (souvent propre pour petites features), et **Rebase and merge**. Demande la convention de ton equipe.

## A toi

Cree une branche avec 1 commit. Push. Ouvre une PR vers `main`. Merge-la toi-meme. Puis `git pull` en local.

## En vrai, sur le terrain

Lis 2 PR open source.
Tu verras le meme format partout.

## Mini defi

Ecris un modele de description PR dans ton README (section Contributing).
