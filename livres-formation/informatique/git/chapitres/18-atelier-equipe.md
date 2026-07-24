# Chapitre 18 - Atelier : workflow d'equipe (simule)

Meme seul, tu peux simuler deux personnes.

## Idee

Deux dossiers locaux :
- `alice/carnet`
- `bob/carnet`

Tous deux clones du meme depot GitHub.

## Tour de jeu

1. Alice cree une branche `feature/alice`, commit, push, PR
2. Bob `pull` sur `main` apres le merge
3. Bob cree `feature/bob` sur une autre zone de fichier
4. PR de Bob
5. Alice review (meme si c'est toi sous un autre navigateur)

## Regles d'equipe simples

- Pas de commit direct sur `main` (branche + PR)
- Messages clairs
- PR petites
- `pull` le matin
- Ne jamais forcer (`push --force`) sur `main`

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

1. Personne ne pousse en force sur `main`
2. Toute feature passe par une PR
3. On review au moins 1 fois (meme soi-meme en solo)
4. On ne commit pas `.env`
5. On ecrit des messages qui se lisent

Colle ca dans `CONTRIBUTING.md`.
