# Chapitre 5 - Lire l'historique

L'interet de Git, c'est de pouvoir regarder en arriere sans paniquer.

## log simple

```bash
git log
```

Tu vois hash, auteur, date, message.
Quitte avec `q` si c'est une vue longue.

## log compact

```bash
git log --oneline
```

Une ligne par commit. Ideal au debut.

## Voir un fichier a travers le temps

```bash
git log --oneline -- readme.txt
```

## diff : qu'est-ce qui a change ?

Avant de commit :

```bash
git diff
```

Ca montre les modifications non stagees.

Entre staging et dernier commit :

```bash
git diff --staged
```

Entre deux commits :

```bash
git diff HEAD~1 HEAD
```

`HEAD` = ou tu es maintenant.
`HEAD~1` = le commit d'avant.

## show

```bash
git show HEAD
```

Detail du dernier commit.

## Checkout d'un fichier (apercu)

Pour jeter les modifs non commit d'un fichier :

```bash
git restore readme.txt
```

(Anciennement `git checkout -- readme.txt`.)
Attention : tu perds les changements non sauves dans un commit.

## A toi

1. Fais un petit changement
2. `git diff`
3. `add` + `commit`
4. `git log --oneline`

## En vrai, sur le terrain

Ouvre `git log --oneline --graph --all` une fois.
Meme sur un petit projet, tu vois la forme de l'histoire.

## Mini defi

Cree 3 commits avec des messages tres clairs.
Demande a quelqu'un de lire ton `log --oneline` : est-ce comprehensible ?
