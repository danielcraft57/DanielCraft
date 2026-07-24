# Chapitre 14 - Atelier : CSV des notes

Objectif : un petit pipeline local. Tu crees un CSV, tu calcules des moyennes par eleve, tu ecris un second CSV resume. Pas d'API ici. Que des fichiers et du Python clair.

## Etapes

1. Cree le dossier `atelier-csv` avec un sous-dossier `data`.
2. Ecris `data/notes.csv` avec l'en-tete `eleve,matiere,note` et au moins 6 lignes (2 eleves, 3 matieres).
3. Ecris `resume_notes.py` qui utilise `pathlib` et `csv`.
4. Lis toutes les notes. Accumule somme et compte par eleve (dictionnaire de dictionnaires, ou deux dicos).
5. Affiche dans le terminal chaque eleve et sa moyenne arrondie a 1 decimale.
6. Ecris `data/moyennes.csv` avec les colonnes `eleve,moyenne,nb_notes`.
7. Gere le cas fichier manquant avec un message clair (pas seulement le traceback).

## Criteres de reussite

- Relancer le script deux fois de suite recree `moyennes.csv` sans planter.
- Les moyennes sont correctes (verifie a la main sur un eleve).
- Le code utilise `DictReader` / `DictWriter`, pas un `.split(",")` maison.
- Encoding UTF-8 partout.

## Idee de structure interne

```python
def lire_notes(chemin):
    ...

def moyennes_par_eleve(lignes):
    ...

def ecrire_moyennes(chemin, moyennes):
    ...
```

Tu testes mentalement chaque morceau. Au chapitre tests, tu pourras poser des `assert` sur `moyennes_par_eleve` sans toucher aux fichiers.

## Bonus

Ajoute argparse : `--fichier` pour le CSV source, `--sortie` pour le CSV moyennes. Valeurs par defaut vers `data/notes.csv` et `data/moyennes.csv`.

## Piege

Les notes en string. Convertis avec `float` (ou `int` si tu es sur des entiers). Si une ligne a une note invalide, decide : ignorer avec un warning, ou arreter avec une erreur claire. Les deux sont defensables ; l'important est d'avoir choisi. Autre piege : oublier `writeheader` et te retrouver avec un CSV sans colonnes nommees.

## A toi

Quand `moyennes.csv` est correct, ouvre-le dans un tableur si tu veux. Le pont Python <-> tableur, c'est souvent ca le vrai gain.
