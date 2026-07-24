# Chapitre 3 - CSV : lire et ecrire un tableau

Un fichier CSV, c'est un tableau en texte. Chaque ligne est une ligne du tableau. Les colonnes sont separees par une virgule (parfois un point-virgule en France). Excel et les tableurs adorent ce format. Les scripts aussi.

Tu pourrais decouper a la main avec `.split(",")`. Ca marche jusqu'au jour ou une cellule contient une virgule, ou des guillemets. Le module `csv` de la bibliotheque standard gere ca proprement. Chez DanielCraft, on dit : pour un tableau, utilise l'outil tableau.

## Un exemple concret : notes

Imagine `data/notes.csv` :

```text
eleve,matiere,note
Alice,maths,14
Bob,maths,11
Alice,francais,16
Bob,francais,13
```

Premiere ligne : les noms de colonnes (en-tete). Ensuite les donnees. Simple, lisible, partageable.

## Lire avec csv.DictReader

```python
import csv
from pathlib import Path

chemin = Path("data/notes.csv")

with chemin.open(encoding="utf-8", newline="") as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        print(ligne["eleve"], ligne["matiere"], ligne["note"])
```

Chaque `ligne` est un dictionnaire. Les cles viennent de l'en-tete. C'est confortable : tu penses en colonnes nommees, pas en indices `0`, `1`, `2`.

Le `newline=""` est une recommandation officielle sous Windows pour le module `csv`. Garde-le. L'`encoding="utf-8"` protege les accents.

Attention : les valeurs restent des chaines. `"14"` n'est pas encore le nombre `14`. Convertis quand tu calcules :

```python
note = float(ligne["note"])
```

## Ecrire avec csv.DictWriter

```python
import csv
from pathlib import Path

chemin = Path("data/notes.csv")
lignes = [
    {"eleve": "Alice", "matiere": "maths", "note": "14"},
    {"eleve": "Bob", "matiere": "maths", "note": "11"},
]

with chemin.open("w", encoding="utf-8", newline="") as f:
    champs = ["eleve", "matiere", "note"]
    ecriture = csv.DictWriter(f, fieldnames=champs)
    ecriture.writeheader()
    ecriture.writerows(lignes)
```

`writeheader()` ecrit la premiere ligne. `writerows` ecrit le reste. Tu peux aussi faire `writerow` une ligne a la fois dans une boucle.

## Separateur point-virgule

En France, Excel exporte parfois avec `;`. Dis-le au lecteur :

```python
lecteur = csv.DictReader(f, delimiter=";")
```

Et a l'ecriture :

```python
ecriture = csv.DictWriter(f, fieldnames=champs, delimiter=";")
```

Si tu ouvres un CSV et que "tout est dans une seule colonne", regarde le separateur.

## Calculer une moyenne

Tu lis, tu accumules, tu divises. Rien de magique :

```python
total = 0.0
compte = 0
with chemin.open(encoding="utf-8", newline="") as f:
    for ligne in csv.DictReader(f):
        if ligne["eleve"] == "Alice":
            total += float(ligne["note"])
            compte += 1
moyenne = total / compte if compte else 0
print("Moyenne Alice :", moyenne)
```

C'est le coeur de beaucoup de petits scripts "metier" : lire un tableau, filtrer, resumer.

## Erreur classique

Ouvrir en mode texte sans `newline=""`. Ou oublier que tout est string. Ou ecrire sans `writeheader` puis s'etonner que `DictReader` ne trouve pas les cles. Autre piege : confondre le nom du fichier et son contenu - un mauvais chemin donne un fichier vide ou une erreur, pas un "CSV casse".

## En vrai

Cree `notes.csv` a la main (bloc-notes) avec 4-5 lignes. Lis-le avec `DictReader`. Affiche la moyenne d'un eleve. Puis reecris un nouveau fichier `moyennes.csv` avec deux colonnes `eleve,moyenne`.

## A toi

Ecris une fonction `moyenne_eleve(chemin, nom)` qui retourne la moyenne, ou `None` si l'eleve est absent. Teste-la avec ton fichier. On reutilisera ce genre de fonction dans le mini-projet et les ateliers.
