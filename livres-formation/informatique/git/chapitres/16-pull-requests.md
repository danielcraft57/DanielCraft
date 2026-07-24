# Chapitre 16 - Pull requests (PR)

Une pull request = "peux-tu fusionner mon travail dans la branche principale ?"

C'est le coeur de la collab sur GitHub.

## Scenario type

1. `git switch -c feature/login`
2. commits locaux
3. `git push -u origin feature/login`
4. Sur GitHub : **Compare & pull request**
5. Remplis titre + description
6. Quelqu'un review
7. Merge sur GitHub
8. En local : `git switch main` puis `git pull`

## Pourquoi pas merger en silence ?

- Relecture
- Discussion
- CI / tests automatiques
- Historique clair

Meme en solo, une PR t'oblige a resumer ton travail. C'est sain.

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

- **Create a merge commit**
- **Squash and merge** (souvent propre pour petites features)
- **Rebase and merge**

Demande la convention de ton equipe.

## A toi

1. Branche + 1 commit
2. Push
3. Ouvre une PR vers `main`
4. Merge-la toi-meme
5. `git pull` en local

## En vrai, sur le terrain

Lis 2 PR open source.
Tu verras le meme format partout.

## Mini defi

Ecris un modele de description PR dans ton README (section Contributing).
