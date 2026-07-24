# Chapitre 16 - Les classes (objets)

Jusqu'ici : fonctions + donnees separees.
Une classe, c'est coller les deux : "une fiche avec des actions".

Image mentale : un moule a cookies.
La classe = le moule.
Un objet = un cookie.

## Premiere classe

```python
class Joueur:
    def __init__(self, prenom, score=0):
        self.prenom = prenom
        self.score = score

    def gagner(self, points):
        self.score += points

    def presenter(self):
        return f"{self.prenom} : {self.score} pts"


j = Joueur("Sam")
j.gagner(10)
print(j.presenter())
```

`__init__` = constructeur. Appele a la creation.
`self` = "moi-meme", l'objet en cours.

## Pourquoi c'est pratique

```python
equipe = [Joueur("Sam"), Joueur("Lea", 50), Joueur("Noe")]
for j in equipe:
    j.gagner(5)
    print(j.presenter())
```

Chaque joueur a son propre score.
Pas besoin de 3 variables `score_sam`, `score_lea`...

## Methode vs fonction

Une fonction ressemble a `presenter(joueur)`. Une methode ressemble a `joueur.presenter()`. Meme idee, style different. Les methodes vivent avec les donnees.

## __str__ (affichage joli)

```python
class Joueur:
    def __init__(self, prenom, score=0):
        self.prenom = prenom
        self.score = score

    def __str__(self):
        return f"{self.prenom} ({self.score})"


print(Joueur("Sam", 12))
```

## Heritage (apercu)

```python
class Boss(Joueur):
    def gagner(self, points):
        # le boss gagne double
        self.score += points * 2
```

Une classe peut specialiser une autre.
Utile plus tard. Pas obligatoire maintenant.

## Dataclass (tres moderne, apercu)

```python
from dataclasses import dataclass

@dataclass
class Produit:
    nom: str
    prix: float

p = Produit("Stylo", 1.5)
print(p.nom, p.prix)
```

Python ecrit une partie du boilerplate pour toi.
Tu le verras dans du code recent.

## Quand utiliser une classe ?

Quand tu as plusieurs donnees liees et des actions dessus. Ou plusieurs "exemplaires" du meme genre (joueurs, produits, ennemis). Si c'est juste 2 fonctions et 1 variable : une fonction suffit. Pas besoin de classe partout.

## A toi

Cree `Compte` avec `solde`.
Methodes `deposer(montant)` et `retirer(montant)`.
Refuse un retrait trop grand (message ou exception).

## En vrai, sur le terrain

Cree 2 joueurs. Fais-les gagner des points. Affiche le plus fort.

## Mini defi

Classe `Question` avec `texte` et `reponse`.
Methode `poser()` qui fait l'input et renvoie True/False.
Branche ca sur ton quiz.
