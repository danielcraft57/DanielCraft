# Chapitre 18 - Atelier : juste prix

L'ordinateur choisit un nombre. Tu cherches. Derriere le jeu, tu revises : `random`, boucle `while`, conditions, saisie protegee, message de defaite, parfois une classe. Chez DanielCraft, on aime ces projets "jouets serieux" : tu t'amuses, tu solidifies. Lea l'a offert a un neveu, puis a ajoute un record JSON. Max a change les bornes pour faire un "juste prix devis" (trop haut / trop bas sur une estimation). Sam chronometre les essais en classe. Trois usages, meme coeur.

Objectif : implementer un juste prix solide. Duree : 35 a 50 minutes. Materiel : Python, un terminal, un fichier vide. Pas de framework. Pas d'API. Juste toi, une boucle, et un secret.

## Ce que ce n'est pas

Ce n'est pas un AAA. Ce n'est pas non plus "juste un truc enfantin". Un jeu terminal bien tenu montre que tu pilotes les boucles et les erreurs. Ce n'est pas obligatoire de tout faire en objets des le premier jet. Base d'abord. Variantes ensuite. Et ce n'est surtout pas "gagner en lisant le secret dans le code" : joue contre toi, comme si tu ne voyais pas la ligne. Sam sourit quand un eleve triche une fois, puis exige la version honnete.

Tu es face a une boite fermee. Dedans, un nombre. Chaque essai, tu frappes a la porte. "Plus grand", "plus petit", ou "bravo". Tu as un budget d'essais. Si tu depasses, la boite s'ouvre et te montre le secret - avec un message de defaite clair. Lea visualise un quiz. Max visualise une estimation de devis. Sam visualise un exercice de patience. Trois images, meme protocole : secret, boucle, feedback, sortie.

## Version de base (avec try)

```python
import random

secret = random.randint(1, 20)
essais = 0
MAX = 6

while essais < MAX:
    essais += 1
    try:
        proposition = int(input(f"Essai {essais}/{MAX} - Nombre 1..20 ? "))
    except ValueError:
        print("Un nombre, merci.")
        continue

    if proposition < secret:
        print("Plus grand")
    elif proposition > secret:
        print("Plus petit")
    else:
        print(f"Bravo ! Trouve en {essais} essais")
        break
else:
    print(f"Perdu. C'etait {secret}")
```

Le `else` du `while` s'execute si on ne `break` pas. Pratique pour le message de defaite. Beaucoup de debutants l'ignorent. Toi, tu l'as vu. Chez DanielCraft, on souligne ce detail parce qu'il evite un `if` supplementaire maladroit apres la boucle.

## Variantes utiles

Demande si on rejoue (`o/n`). Garde le meilleur score (moins d'essais) dans un JSON. Ajoute une difficulte : facile 1-10, normal 1-20, dur 1-50. En version objet, une classe `Partie` avec `secret`, `essais` et `jouer()`. Une variante a la fois. Teste. Puis la suivante. Si tu ajoutes tout d'un coup, tu ne sauras plus ce qui casse.

## Version objet (bonus)

```python
import random

class Partie:
    def __init__(self, maximum=20, max_essais=6):
        self.secret = random.randint(1, maximum)
        self.maximum = maximum
        self.max_essais = max_essais
        self.essais = 0

    def jouer(self):
        while self.essais < self.max_essais:
            self.essais += 1
            try:
                n = int(input(f"1..{self.maximum} ? "))
            except ValueError:
                print("Nombre invalide")
                continue
            if n == self.secret:
                print("Gagne")
                return True
            print("Plus grand" if n < self.secret else "Plus petit")
        print("Perdu :", self.secret)
        return False


if __name__ == "__main__":
    Partie().jouer()
```

Tu n'es pas oblige de commencer par la classe. La version simple suffit pour valider l'atelier. La classe montre que tu peux ranger le meme jeu dans un objet. Utile pour la suite, pas obligatoire pour "reussir".

## Petite histoire

Sam a vu un eleve "gagner" en lisant le secret dans le code. Il a sourit, puis a dit : "maintenant cache-le vraiment et joue contre toi". Lea a ajoute le mode rejouer et a compris `while` autour du jeu entier. Max a sauve le record et a compare avec son neveu. Chez DanielCraft, le livrable compte plus que la perfection esthetique du terminal. Un jeu qui gere `abc` sans planter bat un jeu "joli" qui explose au premier typo.

## Erreur a eviter

Oublier d'incrementer `essais`. Oublier le message de defaite. Laisser `int(input)` planter sur `abc`. Changer trop de variantes a la fois. Une variante, un test. Autre piege : mettre le secret trop visible dans les messages de debug et oublier de retirer les `print` avant de "jouer pour de vrai".

## Livrable

Un `juste_prix.py` avec au minimum : max d'essais, message de defaite, saisie protegee. Bonus : rejouer + record JSON. Bonus 2 : classe `Partie`. Ecris aussi trois lignes : ce que tu reutiliserais ailleurs (saisie solide ? boucle avec `else` ? classe ?).

## En vrai

Joue cinq parties. Note ce qui te frustre dans l'UX (messages, bornes, essais). Ameliore une seule chose. C'est comme ca qu'un jouet devient un outil. Lea a change le message "Plus grand" en "C'est plus grand" et a trouve ca plus humain. Detail. Detail qui compte.

## A toi

Implemente la base ce soir. Ajoute une variante demain. Ecris en trois lignes ce que tu reutiliserais ailleurs. Range le fichier dans ton dossier de projets. Si tu connais Git, commit. Sinon, le livre Git du parcours t'attend plus tard.
