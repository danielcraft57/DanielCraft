# Chapitre 4 - add et commit (la photo)

Le duo du quotidien :

1. `git add` : je prepare
2. `git commit` : je prends la photo

## Ajouter un fichier

```bash
git add readme.txt
git status
```

Le fichier passe en "staged" (index).
Pret pour le commit.

## Ajouter plusieurs fichiers

```bash
git add .
```

Le point = "tout ce qui a change ici".
Pratique. Mais regarde `status` avant : tu ne veux pas ajouter un secret par accident.

## Commit

```bash
git commit -m "Premier commit : readme de base"
```

`-m` = message en une ligne.
Le message doit dire **pourquoi** / **quoi** de utile. Pas juste "update".

## Voir que ca a marche

```bash
git status
git log --oneline
```

`status` devrait dire que rien ne reste a commit.
`log` montre ta photo.

## Modifier encore

Change `readme.txt`, puis :

```bash
git status
git add readme.txt
git commit -m "Clarifier le titre du carnet"
```

Chaque commit = une etape claire.

## Schema mental

```text
modifier fichiers
    -> git add
    -> git commit
    -> historique +1
```

## Amend (apercu, avec prudence)

Tu viens de commit et tu as oublie un fichier ?

```bash
git add fichier_oublie.txt
git commit --amend --no-edit
```

Ca refait le dernier commit.
**Ne l'utilise pas** sur un commit deja pousse si tu travailles en equipe (sauf si tu sais pourquoi).

## A toi

Fais 2 commits :
1. creation du readme
2. ajout d'une ligne

## En vrai, sur le terrain

Apres chaque commit, `git log --oneline`.
Tu dois voir tes messages s'empiler.

## Mini defi

Cree `todo.txt` avec 3 taches.
Commit. Coche une tache. Commit encore.
