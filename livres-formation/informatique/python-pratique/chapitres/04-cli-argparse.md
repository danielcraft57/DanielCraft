# Chapitre 4 - argparse : un script avec des arguments

Tu lances Python avec `python mon_script.py`. C'est bien. Encore mieux : `python mon_script.py --fichier data/notes.csv --eleve Alice`. Le script lit des options. Tu n'as plus a modifier le code pour changer le fichier ou le nom.

`argparse` fait partie de la bibliotheque standard. Il parse la ligne de commande, affiche une aide (`-h`), et refuse les options invalides. Chez DanielCraft, on aime les scripts qui s'expliquent tout seuls.

## L'idee en une image

Ton programme declare : "j'accepte un fichier, et optionnellement un eleve". L'utilisateur passe ces infos. Toi, tu recois un objet propre avec des attributs. Plus besoin de fouiller `sys.argv` a la main (sauf cas tres simples).

## Premier exemple

```python
import argparse

parser = argparse.ArgumentParser(description="Resume des notes CSV")
parser.add_argument("--fichier", required=True, help="Chemin vers le CSV")
parser.add_argument("--eleve", default=None, help="Filtrer sur un eleve")
args = parser.parse_args()

print("Fichier :", args.fichier)
print("Eleve :", args.eleve)
```

Lance :

```text
python resume.py --fichier data/notes.csv --eleve Alice
```

Ou demande l'aide :

```text
python resume.py -h
```

Tu verras la description et les options. C'est deja "pro" pour un petit outil.

## Types et drapeaux

Tu peux demander un entier, un flottant, un booleen style drapeau :

```python
parser.add_argument("--seuil", type=float, default=10.0)
parser.add_argument("--verbose", action="store_true", help="Plus de details")
```

Avec `--verbose`, `args.verbose` vaut `True`. Sans, `False`. Avec `--seuil 12`, tu recois `12.0`. Si quelqu'un met du texte a la place d'un nombre, argparse proteste clairement.

## Relier au CSV

```python
import argparse
import csv
from pathlib import Path

parser = argparse.ArgumentParser(description="Moyenne d'un eleve")
parser.add_argument("--fichier", required=True)
parser.add_argument("--eleve", required=True)
args = parser.parse_args()

chemin = Path(args.fichier)
total = 0.0
compte = 0
with chemin.open(encoding="utf-8", newline="") as f:
    for ligne in csv.DictReader(f):
        if ligne["eleve"] == args.eleve:
            total += float(ligne["note"])
            compte += 1

if compte == 0:
    print("Aucune note pour", args.eleve)
else:
    print(f"Moyenne de {args.eleve} : {total / compte:.1f}")
```

Tu sens le pattern : parser les arguments, puis faire le travail. Le CLI n'est pas le coeur metier. C'est la poignee de la porte.

## Arguments positionnels

Parfois tu veux `python outil.py notes.csv` sans `--fichier` :

```python
parser.add_argument("fichier", help="Chemin CSV")
```

Pas de tirets. L'ordre compte. Melange positionnels et options selon ce qui est le plus naturel a taper.

## Erreur classique

Tout mettre en dur dans le code (`fichier = "notes.csv"`) et dupliquer le script pour chaque cas. Ou parser `sys.argv[1]` sans aide ni verification. Autre classique : oublier `required=True` puis planter plus loin avec un `None` mysterieux. Mieux vaut une erreur argparse des le debut.

## En vrai

Reprends ton lecteur de notes. Ajoute argparse. Lance-le trois fois avec des eleves differents, sans toucher au code. Affiche `-h` et lis ce que ca dit. Si l'aide est claire, ton futur toi (ou un collegue) te remerciera.

## A toi

Ajoute une option `--seuil` : n'affiche que les notes au-dessus du seuil, ou un message "aucune note au-dessus". Petit, utile, concrete. C'est exactement le genre d'outil qu'on garde.
