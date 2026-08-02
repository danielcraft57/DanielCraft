# Chapitre 14 - Atelier : CSV des notes

Objectif : un petit pipeline local. Tu crees un **CSV**, tu calcules des **moyennes** par eleve, tu ecris un second CSV resume. Pas d'API ici. Que des fichiers et du Python clair. Duree : 30 a 45 minutes. Materiel : Python 3, un editeur, un terminal.

Sam veut remplacer son Excel de notes par un script reutilisable. Lea lui a donne cet atelier comme premier pas concret. Max fait la variante avec ses factures fournisseurs (meme logique, autres colonnes). Chez DanielCraft, on considere qu'un atelier sans livrable, c'est une lecture deguisee. Tu vas sortir avec un dossier `atelier-csv/` que tu peux rouvrir dans six mois sans paniquer.

Entree : `notes.csv` avec des lignes eleve / matiere / note. Sortie : `moyennes.csv` avec eleve / moyenne / nb_notes. Au milieu : `DictReader`, conversion `float`, accumulation, `DictWriter`. Si le fichier manque, message clair. Si une note est pourrie, tu decides : ignorer ou arreter. Le script se relance deux fois de suite sans planter. C'est ca, un outil, pas un exercice jetable.

:::retenir
Avant de coder, ecris a la main une moyenne d'un eleve sur ton CSV. Tu auras une verite a comparer apres le script.
:::

## Exercice 1 - Preparer les donnees (10 min)

Cree le dossier `atelier-csv` avec un sous-dossier `data`. Ecris `data/notes.csv` avec l'en-tete `eleve,matiere,note` et au moins 6 lignes (2 eleves, 3 matieres). Utilise `pathlib` pour verifier que le dossier existe. Encoding UTF-8. Evite les accents dans les chemins si ton terminal est capricieux ; dans les donnees, UTF-8 doit tenir.

## Exercice 2 - Lire et calculer (15 min)

Ecris `resume_notes.py` qui utilise `pathlib` et `csv`. Lis toutes les notes avec `DictReader`. Accumule somme et compte par eleve (dictionnaire de dictionnaires, ou deux dicos). Affiche dans le terminal chaque eleve et sa moyenne arrondie a 1 decimale. Convertis les notes avec `float`. Souviens-toi : tout est string jusqu'a conversion.

## Exercice 3 - Ecrire le resume (10 min)

Ecris `data/moyennes.csv` avec les colonnes `eleve,moyenne,nb_notes`. Utilise `DictWriter` avec `writeheader()`. Relance le script deux fois de suite : le fichier doit etre recree sans planter. C'est le test "outil du quotidien" : Sam le relancera chaque trimestre.

## Exercice 4 - Gerer l'echec (5 min)

Gere le cas fichier manquant avec un message clair (pas seulement le traceback). Si une note est invalide, decide : ignorer avec un warning, ou arreter avec une erreur claire. Documente ton choix en commentaire. Lea prefere arreter tot sur un export client. Max prefere ignorer une ligne foireuse et logger. Choisis, mais choisis.

## Idee de structure interne

```python
def lire_notes(chemin):
    ...

def moyennes_par_eleve(lignes):
    ...

def ecrire_moyennes(chemin, moyennes):
    ...
```

Tu testes mentalement chaque morceau. Au chapitre tests, tu pourras poser des `assert` sur `moyennes_par_eleve` sans toucher aux fichiers. Separe le coeur du CLI des maintenant : demain tu te remercieras.

## Petite histoire

Sam a calcule les moyennes a la main sur Alice pendant que Lea ecrivait le script. Quand le script a dit 14.5 et le papier 14.5, Sam a sourit. Max a copie le meme schema pour ses factures : fournisseur, montant, total. Meme pipeline, autre metier. Chez DanielCraft, on aime ces ponts : un atelier notes qui devient un outil perso en une soiree.

Le premier echec de Sam ? Notes laissees en string. `"10" + "12"` ne fait pas 22. La conversion `float` a tout debloque. Tu vas peut-etre vivre la meme scene. Tant mieux : tu ne l'oublieras plus.

## Livrable

Un dossier `atelier-csv/` avec `data/notes.csv`, `data/moyennes.csv`, et `resume_notes.py`. Les moyennes verifiees a la main sur au moins un eleve.

## Criteres de reussite

Relancer le script deux fois de suite recree `moyennes.csv` sans planter. Les moyennes sont correctes (verifie a la main sur un eleve). Le code utilise `DictReader` / `DictWriter`, pas un `.split(",")` maison. Encoding UTF-8 partout.

## Bonus

Ajoute argparse : `--fichier` pour le CSV source, `--sortie` pour le CSV moyennes. Valeurs par defaut vers `data/notes.csv` et `data/moyennes.csv`. Si tu fais le bonus, tu anticipes l'atelier CLI.

## Erreur classique

Les notes en string oubliees. Oublier `writeheader` et te retrouver avec un CSV sans colonnes nommees. Utiliser `.split(",")` sur un CSV qui contient des virgules dans une cellule. Autre piege : travailler dans le mauvais dossier et croire que le fichier "n'existe pas".

:::attention
Tout est string jusqu'a `float`. Oublier la conversion, c'est le piege numero un de cet atelier.
:::

## En vrai

Ouvre `moyennes.csv` dans un tableur. Verifie une ligne a la main. Si ca matche, tu as un pont Python <-> tableur. C'est souvent ca le vrai gain pour Sam, Lea et Max.

## A toi

Quand `moyennes.csv` est correct, ecris trois lignes : ce qui t'a pris le plus de temps, ce que tu referais differemment, ce que tu gardes tel quel. Garde ce papier. L'atelier suivant partira de ce reflexe "outil avec options". Si tu as ignore une note invalide, ecris aussi pourquoi : demain tu sauras ce que tu as choisi.

:::astuce
Un atelier fait a fond bat trois ateliers survoles. Ecris le livrable aujourd'hui, meme si tu finis demain.
:::
