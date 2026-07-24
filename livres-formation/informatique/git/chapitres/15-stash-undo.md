# Chapitre 15 - Stash et annuler (avec prudence)

Parfois tu dois changer de branche alors que tu as des modifs pas pretes.

## stash

```bash
git stash
git switch autre-branche
# ...
git switch -
git stash pop
```

`stash` = met de cote.
`stash pop` = recupere (et enleve de la pile).

Voir la pile :

```bash
git stash list
```

## restore (annuler des modifs locales)

```bash
git restore fichier.txt
```

Revient a la derniere version commit (pour ce fichier).
**Les changements non commits sont perdus.**

## restore --staged

```bash
git restore --staged fichier.txt
```

Retire du staging, garde les modifs dans le dossier.

## reset --soft / --mixed (apercu)

```bash
git reset --soft HEAD~1
```

Annule le dernier commit, garde les changements stages.

```bash
git reset HEAD~1
```

Annule le commit, garde les changements non stages.

## reset --hard (danger)

```bash
git reset --hard HEAD~1
```

Revient en arriere et jette les modifs.
Puissant. Dangereux. Pas sur un commit deja partage sans discussion.

## revert (plus sur en equipe)

```bash
git revert HEAD
```

Cree un **nouveau** commit qui annule le precedent.
L'historique reste honest. Prefere ca sur `main` partage.

## Regle d'or

En local, pas pousse : reset possible. Deja pousse / equipe : revert (ou discussion).

## A toi

Modifie un fichier. Fais `stash`. Verifie que `status` est propre. Puis `stash pop`.

## En vrai, sur le terrain

Avant un `--hard`, respire.
Copie le dossier ailleurs si tu as un doute.

## Mini defi

Fais un commit "oops".
Annule-le avec `revert`. Regarde le `log`.
