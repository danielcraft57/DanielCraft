# Chapitre 18 - Atelier : juste prix

L'ordinateur choisit un nombre. Tu cherches.

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

Le `else` du `while` s'execute si on ne `break` pas.
Pratique pour le message de defaite.

## Variantes

Demande si on rejoue (`o/n`). Garde le meilleur score (moins d'essais) dans un JSON. Ajoute une difficulte : facile 1-10, normal 1-20, dur 1-50. En version objet, une classe `Partie` avec `secret`, `essais` et `jouer()`.

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

## A toi

Implemente au moins un max d'essais, un message de defaite, et une saisie protegee (`try/except`).

## Mini defi

Ajoute le mode rejouer + sauvegarde du record.
