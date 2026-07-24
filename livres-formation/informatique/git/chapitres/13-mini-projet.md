# Chapitre 13 - Mini-projet : carnet versionne

On enchaine le vrai workflow du quotidien.

## But

Un petit projet `carnet-git` avec :
- `README.md`
- `notes.md`
- historique propre
- branche de feature
- push GitHub

## Etapes

### 1. Local

```bash
mkdir carnet-git
cd carnet-git
git init
```

Ecris un README (but + auteur).
Commit : `Initialiser le carnet`

### 2. Notes

Ajoute `notes.md` avec 3 puces.
Commit : `Ajouter les premieres notes`

### 3. Branche

```bash
git switch -c feature/note-git
```

Ajoute une note sur Git.
Commit.
Reviens sur `main` et merge.

### 4. Ignore

Ajoute `.gitignore` avec `.env` et un faux secret local.
Commit.

### 5. GitHub

Cree le depot distant.
`remote add` + `push -u origin main`

### 6. Preuve

Copie l'URL GitHub dans ton `README.md`.
Commit + push.

## Criteres de reussite

- Au moins 4 commits lisibles
- Une branche fusionnee
- Un `.gitignore`
- Projet visible sur GitHub (prive OK)

## Variante avancee

- Ouvre une issue "Ameliorer le README"
- Cree une branche depuis cette idee
- Ouvre une pull request (chapitre 16)

## En vrai, sur le terrain

Chronometre-toi. Vise moins de 20 minutes une fois a l'aise.

## Mini defi

Invite un ami en lecture seule sur le depot (s'il a un compte).
