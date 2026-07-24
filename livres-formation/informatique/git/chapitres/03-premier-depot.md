# Chapitre 3 - Ton premier depot

Un depot (repository) = un projet suivi par Git.

## Creer le dossier

```bash
mkdir mon-carnet
cd mon-carnet
```

## Initialiser Git

```bash
git init
```

Git cree un dossier cache `.git`.
Ne le touche pas a la main. C'est la memoire de Git.

## Premier fichier

Cree `readme.txt` avec :

```text
Mon carnet de tests Git
```

## Voir l'etat

```bash
git status
```

Git dit souvent quels fichiers sont non suivis (untracked), modifies, ou prets a commit. Lis `status` souvent. C'est ton tableau de bord.

## Zones a retenir

Le **dossier de travail**, ce sont tes fichiers normaux. L'**index / staging**, c'est ce que tu prepares pour la photo. Le **depot**, c'est l'historique des commits. On detaille `add` / `commit` au chapitre suivant.

## git init dans un projet existant

Tu peux lancer `git init` dans un dossier qui a deja des fichiers.
Puis tu choisis quoi ajouter.

## A toi

Fais `git init` dans `mes-tests-git` (ou `mon-carnet`). Cree un fichier texte. Lance `git status` et lis le resultat a voix haute.

## Erreur classique

Tu fais `git init` dans le mauvais dossier (ex : ton dossier utilisateur entier).
Verifie avec `cd` et `pwd` (ou `cd` sous PowerShell) avant.

## En vrai, sur le terrain

Ouvre l'explorateur. Active "elements caches".
Tu dois voir `.git` apparaitre apres `init`.

## Mini defi

Ajoute un second fichier `notes.txt`.
Relance `status`. Compare avec avant.

## Trois zones, encore une fois

Imagine une chaine. Tu ecris dans tes fichiers (zone de travail). Tu choisis quoi photographier (`add` = index). Tu valides la photo (`commit` = historique).

Beaucoup de debutants confondent 2 et 3.
Si `status` dit "Changes to be committed", c'est pret pour la photo.
Si ca dit "Changes not staged", il manque un `add`.
