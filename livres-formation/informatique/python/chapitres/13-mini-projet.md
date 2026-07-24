# Chapitre 13 - Mini-projet : quiz terminal

On assemble ce qu'on sait : variables, conditions, boucles, listes, dicos.

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

## Ameliorations

Tu peux melanger l'ordre avec `random.shuffle`. Sauvegarde le meilleur score dans un fichier JSON. Ajoute 2 questions perso. Affiche un message selon le score (bien / moyen / a revoir).

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

## Criteres

Vise au moins 3 questions (idealement 5). Affiche le score a la fin. Compare de facon souple avec `strip` et `lower`.

## En vrai, sur le terrain

Retape la version propre sans copier-coller.
Change les questions. Relance 2 fois.

## Mini defi

Ajoute le melange + sauvegarde du record.
