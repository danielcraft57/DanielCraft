# Chapitre 8 - Les conflits

Un conflit = Git ne sait pas choisir.
Deux versions du meme endroit. Il te demande d'arbitrer.

## Comment ca arrive

Sur `main`, tu modifies la ligne 1 de `readme.txt`. Sur une branche, tu modifies aussi la ligne 1. Tu merges : boum, conflit.

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

Ouvre le fichier. Corrige a la main. Fais `git add fichier_corrige.txt`, puis `git commit` pour conclure le merge. Ou, si ton outil propose "accepter actuel / entrant / les deux", OK - mais comprends ce que tu acceptes.

## Annuler un merge en cours

Si tu es perdu :

```bash
git merge --abort
```

Retour avant le merge. Ouf.

## Eviter les conflits (un peu)

Fais des petits commits. Parle-toi en equipe. Merge / rebase souvent (pas attendre 3 semaines). Evite que deux personnes editent la meme zone sans coordination.

## A toi

Provoque un conflit volontairement sur `readme.txt`.
Resols-le. Termine le merge.

## En vrai, sur le terrain

Un conflit n'est pas un echec.
C'est Git qui dit : "decide humain".

## Mini defi

Note 3 regles perso pour limiter les conflits dans ton prochain projet.
