# Chapitre 18 - Organiser un petit projet

Un script unique, c'est bien pour apprendre. Des qu'il y a CSV + API + CLI + tests, un peu d'ordre evite le chaos. Pas besoin d'architecture d'entreprise. Juste un dossier clair.

Chez DanielCraft, on vise : un nouvel arrivant comprend en 30 secondes ou cliquer.

## Arborescence type

```text
mon-outil/
  .venv/
  .gitignore
  .env.example
  requirements.txt
  README.md
  data/
    notes.csv
  src/
    mon_outil/
      __init__.py
      cli.py
      notes.py
      meteo.py
  tests/
    test_notes.py
```

Variante plus simple, tout a plat au debut :

```text
mon-outil/
  .venv/
  requirements.txt
  resume.py
  notes_lib.py
  data/
  tests/
```

L'important : separer donnees, code, tests. Ne pas melanger le CSV de prod et les brouillons sans nom.

## requirements.txt

```text
requests==2.32.3
pytest==8.3.0
```

Les versions exactes (pin) rendent les installs reproductibles. Pour un apprentissage, pinner au moins les paquets critiques.

Installation :

```text
python -m venv .venv
# activer le venv
python -m pip install -r requirements.txt
```

## README court

Quatre blocs suffisent : a quoi sert l'outil, comment installer, comment lancer (2 exemples), ou mettre sa cle si besoin (renvoi a `.env.example`). Ecris pour un humain presse, pas pour un roman.

## .gitignore utile

```text
.venv/
.env
__pycache__/
*.pyc
.pytest_cache/
app.log
```

Tu ignores le virtuel, les secrets, le cache Python, les logs locaux.

## Ou mettre le point d'entree ?

`cli.py` ou `resume.py` parse les arguments et appelle des fonctions. `notes.py` / `meteo.py` portent la logique. Les tests importent la logique, pas le parseur complet (sauf tests d'integration plus tard).

## Erreur classique

Un dossier `Nouveau dossier (3)` avec `script_final_v2_REEL.py`. Ou installer sans `requirements.txt` et ne plus savoir quoi recreer sur une autre machine. Ou committer `.venv` (lourd, inutile, parfois fragile).

## En vrai

Reprends ton mini-projet. Range-le dans une arborescence simple. Ajoute `requirements.txt`, `.env.example`, un README de 15 lignes. Supprime les fichiers morts.

## A toi

Ecris la structure choisie sur papier (ou dans le README) avant de deplacer les fichiers. Dix minutes d'ordre economisent une heure de "ou j'avais mis ca ?".
