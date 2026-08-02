# Chapitre 3 - CSV : lire et ecrire un tableau

Un fichier **CSV**, c'est un tableau en texte. Chaque ligne est une ligne du tableau. Les colonnes sont separees par une virgule (parfois un point-virgule en France). Excel et les tableurs adorent ce format. Les scripts aussi. C'est le pont le plus simple entre Python et le monde "metier" : notes d'eleves, listes clients, exports comptables. Tu n'as pas besoin d'un tableur ouvert a minuit pour calculer une moyenne.

Tu pourrais decouper a la main avec `.split(",")`. Ca marche jusqu'au jour ou une cellule contient une virgule, ou des guillemets. Le module `csv` de la bibliotheque standard gere ca proprement. Un CSV, c'est un tableur aplati. La premiere ligne dit "voici les noms de colonnes". Chaque ligne suivante est une ligne de donnees. Python lit ligne par ligne et te donne des dictionnaires avec des cles nommees. Tu penses en colonnes (`eleve`, `matiere`, `note`), pas en indices `0`, `1`, `2`. C'est plus lisible, et plus solide quand l'ordre des colonnes change.

Chez DanielCraft, on dit : pour un tableau, utilise l'outil tableau. Sam lit les notes de ses eleves avec **DictReader**. Lea exporte des moyennes vers un second CSV pour ses clients. Max recoit des factures fournisseurs en CSV et les resume sans ouvrir Excel. Sam a six lignes : Alice et Bob, maths et francais. DictReader lui donne `ligne["eleve"]`, `ligne["note"]`. Il calcule, il exporte. Zero copier-coller.

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

Chaque `ligne` est un dictionnaire. Les cles viennent de l'en-tete. Le `newline=""` est une recommandation officielle sous Windows pour le module `csv`. Garde-le. L'`encoding="utf-8"` protege les accents.

Attention : les valeurs restent des **chaines**. `"14"` n'est pas encore le nombre `14`. Convertis quand tu calcules :

```python
note = float(ligne["note"])
```

:::astuce
Des le premier calcul, force le `float`. Tu evites le classique `"14" + "16"` qui donne `"1416"` au lieu de `30`.
:::

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

:::attention
Tout est string jusqu'a conversion. `"14" + "16"` donne `"1416"`, pas `30`. Passe par `float` avant de calculer.
:::

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

## Petite histoire

Sam exportait les notes depuis son logiciel scolaire en CSV. Il ouvrait Excel, faisait des moyennes, imprimait. Un soir, une formule s'etait cassee et personne ne l'avait vu. Avec un script Python de trente lignes, il relance la meme commande chaque trimestre. Les moyennes sont identiques a la main, mais verifiables. Lea fait pareil pour ses rapports clients : un CSV entree, un CSV sortie, zero copier-coller.

Max a adapte le meme pattern a ses factures fournisseurs. Colonnes differentes, meme geste. C'est ca la force du CSV : un format bete, un pont solide.

## Erreur classique

Ouvrir en mode texte sans `newline=""`. Ou oublier que tout est string et calculer `"14" + "16"` au lieu de `14 + 16`. Ou ecrire sans `writeheader` puis s'etonner que `DictReader` ne trouve pas les cles. Autre piege : confondre le nom du fichier et son contenu - un mauvais chemin donne un fichier vide ou une erreur, pas un "CSV casse".

## En vrai

Cree `notes.csv` a la main (bloc-notes) avec 4-5 lignes. Lis-le avec `DictReader`. Affiche la moyenne d'un eleve. Puis reecris un nouveau fichier `moyennes.csv` avec deux colonnes `eleve,moyenne`.

## A toi

Ecris une fonction `moyenne_eleve(chemin, nom)` qui retourne la moyenne, ou `None` si l'eleve est absent. Teste-la avec ton fichier. On reutilisera ce genre de fonction dans le mini-projet et les ateliers. Bonus : affiche aussi le nombre de notes prises en compte. Sam verifie toujours a la main sur un eleve avant de faire confiance au script.

:::retenir
CSV = tableau texte. DictReader / DictWriter, UTF-8, newline="", et float avant de calculer.
:::
