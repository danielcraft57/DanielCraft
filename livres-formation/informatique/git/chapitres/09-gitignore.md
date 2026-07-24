# Chapitre 9 - .gitignore

Certains fichiers ne doivent **jamais** aller dans Git.
Secrets, caches, gros binaires, dossiers de dependances...

## Creer le fichier

A la racine du projet, cree `.gitignore` :

```text
# secrets
.env
*.key

# python
__pycache__/
.venv/

# node
node_modules/

# OS / editeur
.DS_Store
Thumbs.db
.idea/
.vscode/
```

Adapte a ton projet. Ce n'est pas une liste magique universelle.

## Verifier

```bash
git status
```

Les fichiers ignores ne doivent plus apparaitre comme "a ajouter".

## Deja suivi par erreur ?

Si tu as deja `add` un fichier sensible :

```bash
git rm --cached fichier.env
```

Ca l'enleve de l'index, pas de ton disque.
Puis commit. Et ajoute-le au `.gitignore`.

Si le secret est deja sur GitHub : **change le secret** (mot de passe, cle).
L'enlever de l'historique est un autre niveau.

## Templates

GitHub propose des `.gitignore` tout faits (Python, Node...).
Tu peux t'en inspirer.

## A toi

Ajoute un `.gitignore` a ton carnet de tests.
Cree un faux `.env` avec `SECRET=demo`.
Verifie que Git l'ignore.

## En vrai, sur le terrain

Avant le premier push public : relis `git status`.
Cherche mots de passe, cles, dumps, photos perso.

## Mini defi

Ecris un `.gitignore` pour un mini site (HTML/CSS/JS) avec un dossier `dist/` a ignorer.
## Patterns utiles

```text
*.log
tmp/
build/
dist/
*.pdf
!docs/manuel.pdf
```

`!` peut re-inclure une exception.
Commence simple. Complexifie seulement si besoin.
