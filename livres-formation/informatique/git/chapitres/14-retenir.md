# Chapitre 14 - Ce qu'il faut retenir (bases)

## Boucle quotidienne

```text
status -> add -> commit -> (push)
pull souvent si collab
```

## Commandes vitales

Tu demarres avec `git init` ou `git clone`. Tu regardes l'etat avec `git status`. Tu prepares avec `git add`, puis tu photographies avec `git commit`. Pour l'histoire : `git log --oneline`. Pour les pistes paralleles : `git switch` et `git branch`, puis `git merge`. Avec le distant : `git pull`, `git push`, et `git remote -v` pour verifier le lien.

## Zones

Travail -> index (`add`) -> historique (`commit`) -> remote (`push`)

## Habitudes

Fais `status` avant et apres. Ecris des messages clairs. Mets un `.gitignore` tot. Prefere les petites branches. Ne commit jamais un secret.

## Erreurs classiques

On commit parfois sur la mauvaise branche. Un push peut etre refuse si le remote est en avance. Un conflit laisse des `<<<<<<<` si tu oublies de nettoyer. Et `git add .` sans regarder, c'est le classique des secrets qui passent.

## Suite immediate

Deux chapitres un cran au-dessus : stash + annuler proprement, puis les pull requests. Puis ateliers + quiz.

## Mini check

Sans notes : ecris la boucle `add/commit/push` et a quoi sert une branche.

## Aide-memoire express

Pour l'etat : `git status`. Pour preparer : `git add`. Pour la photo : `git commit -m "..."`. Pour l'histoire : `git log --oneline`. Pour une branche : `git switch -c nom`. Pour fusionner : `git merge nom`. Pour envoyer : `git push`. Pour recevoir : `git pull`.

Imprime cette page mentalement.
