# Chapitre 6 - Les branches

Une branche = une piste parallele.
Tu experimentes sans casser la version stable.

## Voir les branches

```bash
git branch
```

Souvent tu as `main` (ou `master` sur de vieux depots).

## Creer et changer de branche

```bash
git branch idee-couleurs
git switch idee-couleurs
```

Ou en une commande :

```bash
git switch -c idee-couleurs
```

(`git checkout -b ...` existe encore. `switch` est plus clair.)

## Travailler sur la branche

Modifie un fichier. Commit.

```bash
git log --oneline
```

Ces commits sont sur `idee-couleurs`.
`main` n'a pas encore ces changements.

## Revenir sur main

```bash
git switch main
```

Tes fichiers "reviennent" a l'etat de `main`.
Magique la premiere fois. Normal ensuite.

## A quoi ca sert vraiment ?

- Feature en cours
- Correction urgente sur `main` pendant que tu experimentes ailleurs
- Essai risqué (tu peux jeter la branche)

## Renommer / supprimer

```bash
git branch -m ancien-nom nouveau-nom
git branch -d idee-couleurs
```

`-d` refuse s'il reste des commits non fusionnes.
`-D` force (prudent).

## A toi

1. Cree une branche `essai`
2. Ajoute un fichier `essai.txt` + commit
3. Reviens sur `main`
4. Verifie que `essai.txt` n'est plus la (normal)

## En vrai, sur le terrain

Avant chaque experience : nouvelle branche.
Reflexe pro, meme en solo.

## Mini defi

Deux branches : `page-a` et `page-b`.
Un commit different sur chacune. Note ce que `log` montre sur chaque.
