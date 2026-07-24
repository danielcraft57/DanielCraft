# Chapitre 18 - Atelier : workflow d'equipe (simule)

Meme seul, tu peux simuler deux personnes.

## Idee

Deux dossiers locaux : `alice/carnet` et `bob/carnet`. Tous deux clones du meme depot GitHub.

## Tour de jeu

Alice cree une branche `feature/alice`, commit, push, PR. Bob fait `pull` sur `main` apres le merge. Bob cree `feature/bob` sur une autre zone de fichier, puis sa PR. Alice review (meme si c'est toi sous un autre navigateur).

## Regles d'equipe simples

Pas de commit direct sur `main` : branche + PR. Messages clairs. PR petites. `pull` le matin. Ne jamais forcer (`push --force`) sur `main`.

## force push ?

```bash
git push --force
```

A bannir sur les branches partagees tant que tu ne maitrises pas.
Ca reecrit l'histoire distante. Ca peut effacer le travail des autres.

## Protection de branche

Sur GitHub : Settings -> Branches -> proteger `main`.
Exige une PR. C'est une ceinture de securite.

## A toi

Joue Alice et Bob sur un depot de test.
2 PR mergees. Historique lisible.

## Mini defi

Ecris un fichier `CONTRIBUTING.md` de 10 lignes pour ton futur projet.

## Mini charte (copie-colle)

Personne ne pousse en force sur `main`. Toute feature passe par une PR. On review au moins 1 fois (meme soi-meme en solo). On ne commit pas `.env`. On ecrit des messages qui se lisent.

Colle ca dans `CONTRIBUTING.md`.
