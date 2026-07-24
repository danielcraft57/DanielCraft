# Chapitre 2 - Installer Git

## Windows

1. Va sur git-scm.com
2. Telecharge l'installateur
3. Suis l'assistant (les options par defaut vont bien au debut)
4. Ouvre un terminal et tape :

```bash
git --version
```

Si tu vois un numero, c'est bon.

## Premiere config (obligatoire)

Git a besoin de savoir qui tu es pour signer tes commits :

```bash
git config --global user.name "Ton Prenom"
git config --global user.email "ton@email.com"
```

Verifie :

```bash
git config --global --list
```

Utilise un email que tu assumeras (souvent celui de ton compte GitHub).

## Ou taper les commandes ?

- Terminal Windows (PowerShell)
- Git Bash (installe avec Git)
- Terminal integre de VS Code

Les commandes de ce livre marchent dans ces environnements.
Sur PowerShell, c'est le meme `git ...`.

## Editeur de message

Parfois Git ouvre un editeur pour ecrire un message de commit.
Au debut, reste sur les messages en une ligne avec `-m "..."` .
Plus simple.

## Aide integree

```bash
git help
git help commit
```

Ou :

```bash
git commit -h
```

## A toi

1. `git --version`
2. Configure `user.name` et `user.email`
3. Affiche la config

## Erreur classique

Tu commits sans avoir configure le nom/email.
Git rale. Ou pire : il utilise une fausse identite.
Configure tout de suite.

## En vrai, sur le terrain

Ouvre VS Code. Ouvre le terminal. Tape `git --version`.
Si ca marche la, tu es pret pour la suite.

## Mini defi

Cree un dossier `mes-tests-git` sur ton disque.
C'est ton terrain de jeu pour tout le livre.
