# Chapitre 13 - Mini-projet : quiz terminal

On assemble ce qu'on sait : variables, conditions, boucles, listes, dictionnaires, un peu de fichiers et de modules. Ce n'est pas un examen piege. C'est une preuve pour toi : tu peux construire un petit outil complet, le lancer, le casser, le reparer. Chez DanielCraft, le mini-projet sert a ca - transformer des chapitres separes en geste fluide.

Lea a adapte ce quiz pour briefer un stagiaire. Max l'a transforme en questions metier (marges, TVA). Sam l'utilise tel quel en classe, puis demande deux questions perso. Trois versions, meme ossature. Tu n'as pas a inventer un reseau social. Tu as a finir un outil petit et net.

## Ce que ce n'est pas

Ce n'est pas "le projet final de ta carriere". Ce n'est pas non plus une excuse pour copier-coller sans comprendre. Ce n'est pas obligatoire d'aller jusqu'a la version objet des le premier jet. Version simple d'abord. Version propre ensuite. Shuffle + JSON si tu as le temps. Une marche apres l'autre. Et ce n'est surtout pas "tout faire d'un coup et ne rien finir". Un quiz de cinq questions qui marche bat un projet "parfait" abandonne a 40 %.

Tu as une liste de fiches `{question, reponse}`. Tu parcours. Tu demandes. Tu compares avec `strip` et `lower`. Tu comptes. Tu affiches. Plus tard, tu melanges l'ordre, tu sauves le record. Le quiz n'est qu'un pretexte : la vraie competence, c'est l'assemblage. Chez DanielCraft, on repete : l'assemblage, c'est le niveau au-dessus de "je connais la syntaxe".

Lea voit un brief stagiaire. Max voit un quiz metier. Sam voit un exercice de classe. Trois pretexts, meme architecture.

## Version simple

```python
score = 0

reponse = input("Capitale de la France ? ")
if reponse.strip().lower() == "paris":
    print("OK")
    score = score + 1
else:
    print("Non, c'etait Paris")

reponse = input("2 + 2 = ? ")
if reponse.strip() == "4":
    print("OK")
    score = score + 1
else:
    print("Non, 4")

reponse = input("Langage de ce livre ? ")
if reponse.strip().lower() == "python":
    print("OK")
    score = score + 1
else:
    print("Python !")

print("Score final :", score, "/ 3")
```

Ca marche. Ca se repete. D'ou la version plus propre. Ne meprise pas cette version : elle prouve que tu pilotes conditions et score. Ensuite seulement, tu ranges.

## Version plus propre

```python
questions = [
    {"q": "Capitale de la France ?", "a": "paris"},
    {"q": "2 + 2 = ?", "a": "4"},
    {"q": "Langage de ce livre ?", "a": "python"},
]

score = 0
for item in questions:
    rep = input(item["q"] + " ").strip().lower()
    if rep == item["a"]:
        print("OK")
        score += 1
    else:
        print("Non, reponse :", item["a"])

print(f"Score : {score} / {len(questions)}")
```

Regarde ce qui a change : les donnees sont separees de la boucle. Ajouter une question devient une ligne, pas un copier-coller de huit lignes. Lea appelle ca "arreter de se mentir sur le temps gagne". Sam appelle ca "enfin un code qu'on peut montrer".

## Version avec shuffle + JSON

```python
import json
import random
from pathlib import Path

questions = [
    {"q": "Capitale de la France ?", "a": "paris"},
    {"q": "2 + 2 = ?", "a": "4"},
    {"q": "Langage de ce livre ?", "a": "python"},
    {"q": "Couleur du ciel (souvent) ?", "a": "bleu"},
]

random.shuffle(questions)
score = 0
for item in questions:
    rep = input(item["q"] + " ").strip().lower()
    if rep == item["a"]:
        print("OK")
        score += 1
    else:
        print("Non :", item["a"])

print(f"Score : {score}/{len(questions)}")

fichier = Path("meilleur_score.json")
meilleur = 0
if fichier.exists():
    meilleur = json.loads(fichier.read_text(encoding="utf-8")).get("score", 0)

if score > meilleur:
    fichier.write_text(json.dumps({"score": score}, indent=2), encoding="utf-8")
    print("Nouveau record !")
else:
    print("Record actuel :", meilleur)
```

## Petite histoire

Sam a fait retaper la version propre sans coller. Les eleves qui collaient bloquaient sur le JSON. Ceux qui tapaient comprenaient `Path.exists`. Max a ajoute un message selon le score (bien / moyen / a revoir) avec un `if`. Lea a melange les questions pour que le stagiaire ne memorise pas l'ordre. Chez DanielCraft, on prefere ces ameliorations concretes aux reecritures cosmiques. Une feature utile, un test, un sourire.

## Erreur classique

Comparer sans `strip`/`lower`. Oublier d'initialiser `score = 0`. Ecraser le record JSON a chaque run sans lire l'ancien. Vouloir tout faire d'un coup et ne rien finir. Criteres minimum : au moins 3 questions (idealement 5), score final, comparaison souple. Autre piege : changer les questions sans relancer deux fois pour verifier le shuffle et le record.

## En vrai

Retape la version propre sans copier-coller. Change les questions. Relance 2 fois. Puis ajoute le melange + sauvegarde du record si tu peux. Note le temps. Tu verras que l'assemblage prend plus que la syntaxe - et c'est normal.

## A toi

Livrable : un fichier `quiz.py` qui pose au moins 5 questions, affiche le score, et (bonus) sauve le record. Ecris aussi en trois lignes ce que tu reutiliserais dans un autre projet (boucle ? dico ? JSON ?). Range le livrable. Les ateliers suivants s'appuieront sur cette base.

## Zoom : donnees vs logique

Dans la version simple, donnees et logique sont meleés. Dans la version propre, les questions sont des donnees, la boucle est de la logique. Cette separation est le debut de l'organisation. Chez DanielCraft, on la celebre autant qu'une nouvelle fonction : demain, tu pourras charger les questions depuis un JSON sans retoucher la boucle.
