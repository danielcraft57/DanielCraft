# Chapitre 2 - pathlib : des chemins sans douleur

En Python, tu touches souvent a des fichiers. Un CSV de notes, un dossier `data`, un fichier de config. Le piege classique, c'est de coller des chemins a la main avec des chaines et des slash... jusqu'au jour ou ca casse sur Windows, ou sur un autre dossier, ou quand tu lances le script depuis un endroit different. Tu perds une heure a chercher un fichier qui "existait hier".

`pathlib` est la solution moderne : tu travailles avec des objets **Path**, pas avec des string brutes. Un chemin, c'est une adresse. Avec `pathlib`, tu manipules l'adresse comme un objet : tu l'assembles, tu verifies si elle existe, tu lis ou tu ecris. L'operateur `/` remplace le collage manuel de slash. Python s'occupe du detail selon le systeme. Tu n'as plus a te demander si c'est `\` ou `/`. Tu penses "dossier puis fichier", pas "string fragile".

Chez DanielCraft, on resume comme ca : un chemin, c'est un objet, pas un texte magique. Lea ancre ses scripts sur `Path(__file__).parent` pour que les exports clients marchent quel que soit le dossier courant. Max range ses CSV de factures dans `data/` sans se battre avec les backslash Windows. Sam garde ses notes dans un dossier a cote du script, pas "quelque part sur le bureau".

:::astuce
Des que ton fichier doit vivre "a cote" du script, ancre avec `Path(__file__).resolve().parent`. Tu evites la moitie des "fichier introuvable".
:::

## Creer un Path

```python
from pathlib import Path

dossier = Path("data")
fichier = Path("data") / "notes.csv"
```

L'operateur `/` assemble les morceaux. Sur Windows comme sur Linux, ca marche. Tu peux aussi partir du dossier du script :

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

Toujours preciser `encoding="utf-8"` quand tu manipules du francais. Sinon, selon la machine, les accents peuvent devenir bizarres. Pour du binaire (images, etc.), il existe `read_bytes` / `write_bytes`. On reste sur du texte ici.

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

Un chemin **relatif** depend du dossier ou tu lances Python. Un chemin **absolu** pointe toujours au meme endroit.

```python
p = Path("data/notes.csv")
print(p.resolve())
```

`.resolve()` donne la forme absolue, avec les `..` ranges. Quand tu debogues "fichier introuvable", affiche `resolve()` : souvent tu regardais au mauvais endroit.

## Petite histoire

Max avait un script qui lisait `notes.csv` en dur. Ca marchait quand il lancait depuis son dossier projet. Un matin, il l'a lance depuis `C:\Users\Max` et Python a dit "fichier introuvable". Il a cru que Python etait casse. En realite, le chemin relatif pointait ailleurs. Avec `Path(__file__).parent / "data" / "notes.csv"`, le script retrouve toujours son fichier, peu importe d'ou tu l'appelles.

Lea a le meme reflexe sur tous ses outils clients. Sam le montre en cours : "change de dossier, relance, ca marche encore". Le geste rentre mieux qu'une page de theory.

## Erreur classique

Melanger `os.path.join` partout et `Path` au milieu, sans coherence. Choisis `pathlib` pour les nouveaux scripts. Autre classique : oublier que le dossier courant n'est pas toujours le dossier du script. Utilise `Path(__file__).parent` quand le fichier doit etre "a cote" du code. Autre piege : oublier `encoding="utf-8"` et voir des caracteres bizarres dans un CSV francais.

:::attention
Un chemin relatif "qui marche chez toi" peut planter demain si tu lances depuis un autre dossier. Ancre, ou passe le chemin en argument.
:::

## En vrai

Cree un dossier `data` a cote d'un script. Ecris `bonjour.txt` avec `write_text`. Relis-le. Affiche le chemin absolu avec `resolve()`. Change de repertoire dans le terminal et relance : si tu as bien ancre le chemin sur `__file__`, ca continue de marcher.

## A toi

Ecris un petit script qui cree `data/notes.csv` vide (ou avec une ligne d'en-tete `eleve,matiere,note`), en utilisant uniquement `Path`. Pas de `os.path`. Le geste compte : on branchera le vrai CSV au chapitre suivant. Bonus : affiche `resolve()` du fichier cree pour verifier ou il vit vraiment sur le disque.

:::retenir
Un chemin, c'est un objet Path. Assemble avec `/`, ancre avec `__file__` quand le fichier vit a cote du script.
:::
