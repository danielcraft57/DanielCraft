# Chapitre 2 - pathlib : des chemins sans douleur

En Python, tu touches souvent a des fichiers. Un CSV de notes, un dossier `data`, un fichier de config. Le piege classique, c'est de coller des chemins a la main avec des chaines et des slash... jusqu'au jour ou ca casse sur Windows, ou sur un autre dossier.

`pathlib` est la solution moderne : tu travailles avec des objets `Path`, pas avec des string brutes. Chez DanielCraft, on resume comme ca : un chemin, c'est un objet, pas un texte magique.

## Creer un Path

```python
from pathlib import Path

dossier = Path("data")
fichier = Path("data") / "notes.csv"
```

L'operateur `/` assemble les morceaux. Sur Windows comme sur Linux, Python s'occupe du detail. Tu n'as plus a te demander si c'est `\` ou `/`.

Tu peux aussi partir du dossier du script :

```python
ici = Path(__file__).resolve().parent
notes = ici / "data" / "notes.csv"
```

`__file__` est le chemin du fichier `.py` en cours. `.parent` remonte d'un cran. C'est utile quand tu lances le script depuis un autre repertoire : tu ne depend plus du "dossier courant" mysterieux.

## Existe ? Fichier ? Dossier ?

```python
p = Path("data/notes.csv")
print(p.exists())
print(p.is_file())
print(p.parent.is_dir())
```

Avant d'ouvrir, tu peux verifier. Ce n'est pas obligatoire a chaque ligne, mais c'est rassurant au debut. Si le dossier n'existe pas, tu peux le creer :

```python
Path("data").mkdir(parents=True, exist_ok=True)
```

`parents=True` cree aussi les dossiers parents manquants. `exist_ok=True` evite une erreur si le dossier est deja la.

## Lire et ecrire du texte

Pour un petit fichier texte (ou un JSON en string), `pathlib` a des raccourcis :

```python
chemin = Path("data/bonjour.txt")
chemin.write_text("Salut\n", encoding="utf-8")
contenu = chemin.read_text(encoding="utf-8")
print(contenu)
```

Toujours preciser `encoding="utf-8"` quand tu manipules du francais. Sinon, selon la machine, les accents peuvent devenir bizarres.

Pour du binaire (images, etc.), il existe `read_bytes` / `write_bytes`. On reste sur du texte ici.

## Lister un dossier

```python
dossier = Path("data")
for element in dossier.iterdir():
    print(element.name, element.is_file())
```

Ou filtrer avec un motif :

```python
for csv in Path("data").glob("*.csv"):
    print(csv)
```

`rglob` fait la meme chose en recursif (sous-dossiers inclus). Pratique pour trouver tous les `.csv` d'un projet.

## Chemin absolu vs relatif

Un chemin relatif depend du dossier ou tu lances Python. Un chemin absolu pointe toujours au meme endroit.

```python
p = Path("data/notes.csv")
print(p.resolve())
```

`.resolve()` donne la forme absolue, avec les `..` ranges. Quand tu debogues "fichier introuvable", affiche `resolve()` : souvent tu regardais au mauvais endroit.

## Erreur classique

Melanger `os.path.join` partout et `Path` au milieu, sans coherence. Choisis `pathlib` pour les nouveaux scripts. Autre classique : oublier que le dossier courant n'est pas toujours le dossier du script. Utilise `Path(__file__).parent` quand le fichier doit etre "a cote" du code.

## En vrai

Cree un dossier `data` a cote d'un script. Ecris `bonjour.txt` avec `write_text`. Relis-le. Affiche le chemin absolu. Change de repertoire dans le terminal et relance : si tu as bien ancre le chemin sur `__file__`, ca continue de marcher.

## A toi

Ecris un petit script qui cree `data/notes.csv` vide (ou avec une ligne d'en-tete), en utilisant uniquement `Path`. Pas de `os.path`. Le geste compte : on branchera le vrai CSV au chapitre suivant.
