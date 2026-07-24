# Chapitre 7 - Fusionner (merge)

Tu as travaille sur une branche. Tu veux ramener le travail dans `main`.

## Scenario

```bash
git switch main
git merge idee-couleurs
```

Git essaie de combiner les historiques.

## Si tout va bien

Git cree souvent un "merge commit" (ou avance juste le pointeur : fast-forward).
Tu vois le resultat dans les fichiers + dans `log`.

## Fast-forward, c'est quoi ?

Si `main` n'a pas bouge pendant ton travail, Git peut juste avancer.
Pas de conflit. Simple.

## Merge avec message

Parfois Git ouvre un editeur.
Tu peux aussi :

```bash
git merge idee-couleurs -m "Fusion idee couleurs"
```

## Apres le merge

```bash
git log --oneline --graph
git branch -d idee-couleurs
```

Tu peux supprimer la branche locale une fois fusionnee.

## Quand ne pas merger directement ?

Sur GitHub, on passe souvent par une **pull request** (chapitre 16).
En local / solo, `merge` suffit pour apprendre.

## A toi

Cree une branche `ajout-note`. Commit un fichier. Merge dans `main`. Regarde `log --graph --oneline`.

## En vrai, sur le terrain

Fais un dessin : `main` et `feature` qui se rejoignent.
Le merge, c'est le point de jonction.

## Mini defi

Deux branches avec chacune un fichier different.
Merge les deux dans `main`. Les deux fichiers doivent etre presents.
## Merge vs rebase (apercu)

`merge` : garde l'historique tel quel, ajoute souvent un commit de jonction.
`rebase` : rejoue tes commits "par-dessus" une autre branche. Historique plus lineaire, mais plus piegeux.

Pour ce livre : maitrise `merge` d'abord.
Le rebase, tu le croiseras plus tard (avec prudence, surtout sur branches partagees).
