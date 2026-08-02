# Chapitre 16 - Les classes (objets)

Jusqu'ici : fonctions + donnees souvent separees. Une classe, c'est coller les deux : "une fiche avec des actions". Tu ne ranges plus `prenom` et `score` d'un cote, `gagner` de l'autre, comme des pieces perdues. Tu dis : un `Joueur` sait son prenom, son score, et comment gagner des points. Ce n'est pas obligatoire partout. C'est puissant quand tu as plusieurs exemplaires du meme genre.

Chez DanielCraft, on utilise l'image du moule a cookies. La classe = le moule. Un objet = un cookie. Lea cree des `Produit`. Max cree un `Compte`. Sam cree des `Question`. Trois moules, meme idee : donnees + comportements ensemble. Tu modelises un bout du monde au lieu de jongler avec dix variables orphelines.

## Ce que ce n'est pas

Une classe, ce n'est pas "le niveau expert interdit aux debutants". Ce n'est pas non plus obligatoire pour trois lignes de script. Ce n'est pas une religion. Si deux fonctions et une variable suffisent, reste simple. Ce n'est pas non plus de l'heritage obligatoire des le jour un : l'apercu suffit. Et ce n'est surtout pas du jargon pour impressionner. `self`, c'est "moi-meme, l'objet en cours". Point. Pas de mystique.

Tu fabriques un moule `Joueur`. Quand tu ecris `Joueur("Sam")`, tu sors un cookie Sam avec score 0. `j.gagner(10)` demande a ce cookie d'ajouter des points. `j.presenter()` demande une phrase. Chaque objet a sa propre memoire. Sam et Lea ne partagent pas le meme score, meme s'ils viennent du meme moule. Si tu penses "exemplaires", tu as compris l'essentiel. Le reste, c'est de la syntaxe qui rentre en retapant.

:::astuce
Commence par une classe avec deux donnees et une methode. Pas dix methodes le premier jour.
:::

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

`__init__` = constructeur. Appele a la creation. `self` = l'objet en cours. Oui, c'est un peu bizarre au debut. Retape. Ca rentre. Sam fait retaper trois fois avant d'expliquer. Lea a mis deux jours a "sentir" `self`. Puis ca a clique. Normal.

## Pourquoi c'est pratique

```python
equipe = [Joueur("Sam"), Joueur("Lea", 50), Joueur("Noe")]
for j in equipe:
    j.gagner(5)
    print(j.presenter())
```

Chaque joueur a son propre score. Pas besoin de `score_sam`, `score_lea`... Une fonction ressemble a `presenter(joueur)`. Une methode ressemble a `joueur.presenter()`. Meme idee, style different. Les methodes vivent avec les donnees. Quand tu as une liste d'objets, ton code devient une petite histoire lisible.

## __str__, heritage, dataclass (apercus)

```python
class Joueur:
    def __init__(self, prenom, score=0):
        self.prenom = prenom
        self.score = score

    def __str__(self):
        return f"{self.prenom} ({self.score})"


print(Joueur("Sam", 12))
```

```python
class Boss(Joueur):
    def gagner(self, points):
        # le boss gagne double
        self.score += points * 2
```

Une classe peut specialiser une autre. Utile plus tard. Pas obligatoire maintenant. Comprends juste : parfois un moule herite d'un autre moule et change une regle.

```python
from dataclasses import dataclass

@dataclass
class Produit:
    nom: str
    prix: float

p = Produit("Stylo", 1.5)
print(p.nom, p.prix)
```

Python ecrit une partie du boilerplate pour toi. Tu le verras dans du code recent. Lea adore pour des structures simples. Sam montre les deux styles pour eviter le choc culturel plus tard. Max dit : "si c'est juste des cases a remplir, dataclass. Si j'ai des regles (retrait, depot), vraie classe."

## Quand utiliser une classe ?

Quand tu as plusieurs donnees liees et des actions dessus. Ou plusieurs "exemplaires" du meme genre (joueurs, produits, ennemis, comptes). Si c'est juste 2 fonctions et 1 variable : une fonction suffit. Pas besoin de classe partout. Chez DanielCraft, la classe est un outil, pas un trophee. La question utile : "est-ce que je modelise plusieurs exemplaires avec des regles ?" Si oui, classe. Sinon, fonctions.

## Petite histoire

Max a cree `Compte` avec `deposer` et `retirer`. Il a refuse un retrait trop grand. Sensation concrete : l'objet protege ses regles. Lea a branche une classe `Question` sur son quiz : `poser()` renvoie True/False. Sam a fait comparer deux joueurs et afficher le plus fort. Trois exercices, une meme montee en puissance : tu modelises un bout du monde.

Autre scene : Lea a voulu "tout mettre en classes" apres avoir lu un article. Son script de quinze lignes est devenu illisible. Elle a recule. Deux classes utiles, le reste en fonctions. Chez DanielCraft, on applaudit ce recul. La simplicite n'est pas un echec.

## Erreur classique

Oublier `self` dans les methodes. Appeler `Joueur.gagner(10)` au lieu de `j.gagner(10)`. Mettre toute la logique du programme dans `__init__`. Creer une classe pour une seule valeur sans comportement. Autre piege : croire que la classe "remplace" les fonctions - non, elles cohabitent. Les fonctions organisent. Les classes modelisent quand c'est utile.

:::attention
Oublier `self` casse presque toujours au debut. Relis la traceback. Ajoute `self`. Relance. C'est le rite de passage.
:::

## En vrai

Cree 2 joueurs. Fais-les gagner des points. Affiche le plus fort. Puis classe `Question` avec `texte`, `reponse`, methode `poser()` : branche ca sur ton quiz. Sens la difference entre "deux variables" et "un objet qui sait repondre". Si ca te semble lourd pour rien, reviens aux fonctions. Si ca te semble propre, continue.

## A toi

Cree `Compte` avec `solde`. Methodes `deposer(montant)` et `retirer(montant)`. Refuse un retrait trop grand (message ou exception). Bonus : `__str__` pour afficher le solde proprement. Super bonus : une liste de comptes et un total general calcule en boucle.

## Zoom : objets et vie reelle

Un devis, c'est souvent un objet : lignes, total, TVA, statut. Un joueur de jeu, pareil. Une question de QCM, pareil. Tu n'as pas besoin d'UML. Tu as besoin de nommer la chose et ses gestes. Lea dessine parfois trois cases sur papier avant de coder. Max parle a voix haute : "le compte refuse si solde insuffisant". Sam demande aux eleves d'ecrire d'abord les methodes en francais. Puis le code suit. Chez DanielCraft, la classe commence dans la tete, pas dans le jargon.
