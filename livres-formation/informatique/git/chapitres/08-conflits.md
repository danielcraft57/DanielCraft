# Chapitre 8 - Les conflits

Un conflit = Git ne sait pas choisir.
Deux versions du meme endroit. Il te demande d'arbitrer.

## Comment ca arrive

1. Sur `main`, tu modifies la ligne 1 de `readme.txt`
2. Sur une branche, tu modifies aussi la ligne 1
3. Tu merges : boum, conflit

## A quoi ca ressemble

Dans le fichier :

```text
<<<<<<< HEAD
version de main
=======
version de la branche
>>>>>>> idee-couleurs
```

Tu gardes ce que tu veux. Tu enleves les marqueurs `<<<<<<<` etc.

## Resolving

1. Ouvre le fichier
2. Corrige a la main
3. `git add fichier_corrige.txt`
4. `git commit` (pour conclure le merge)

Ou, si ton outil propose "accepter actuel / entrant / les deux", OK - mais comprends ce que tu acceptes.

## Annuler un merge en cours

Si tu es perdu :

```bash
git merge --abort
```

Retour avant le merge. Ouf.

## Eviter les conflits (un peu)

- Petits commits
- Se parler en equipe
- Merger / rebaser souvent (pas attendre 3 semaines)
- Eviter que deux personnes editent la meme zone sans coordination

## A toi

Provoque un conflit volontairement sur `readme.txt`.
Resols-le. Termine le merge.

## En vrai, sur le terrain

Un conflit n'est pas un echec.
C'est Git qui dit : "decide humain".

## Mini defi

Note 3 regles perso pour limiter les conflits dans ton prochain projet.
