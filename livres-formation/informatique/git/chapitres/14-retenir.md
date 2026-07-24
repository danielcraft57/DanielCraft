# Chapitre 14 - Ce qu'il faut retenir (bases)

## Boucle quotidienne

```text
status -> add -> commit -> (push)
pull souvent si collab
```

## Commandes vitales

- `git init` / `git clone`
- `git status`
- `git add` / `git commit`
- `git log --oneline`
- `git switch` / `git branch`
- `git merge`
- `git pull` / `git push`
- `git remote -v`

## Zones

Travail -> index (`add`) -> historique (`commit`) -> remote (`push`)

## Habitudes

1. `status` avant et apres
2. Messages clairs
3. `.gitignore` tot
4. Petites branches
5. Ne jamais commit un secret

## Erreurs classiques

- Commit sur la mauvaise branche
- Push refuse car remote en avance
- Conflit laisse avec des `<<<<<<<`
- `git add .` sans regarder

## Suite immediate

Deux chapitres un cran au-dessus :
- stash + annuler proprement
- pull requests

Puis ateliers + quiz.

## Mini check

Sans notes : ecris la boucle `add/commit/push` et a quoi sert une branche.
## Aide-memoire express

| Besoin | Commande |
|--------|----------|
| Etat | `git status` |
| Preparer | `git add` |
| Photo | `git commit -m "..."` |
| Histoire | `git log --oneline` |
| Branche | `git switch -c nom` |
| Fusion | `git merge nom` |
| Envoyer | `git push` |
| Recevoir | `git pull` |

Imprime cette page mentalement.
