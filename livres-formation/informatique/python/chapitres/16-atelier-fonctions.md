# Atelier : fonctions

## Objectif

Pratiquer la creation et l'utilisation de fonctions. Chaque exercice te fait ecrire une fonction avec un role precis.

## Exercice 1 : salutation personnalisee

```python
def saluer(nom, heure):
    if heure < 12:
        moment = "Bonjour"
    elif heure < 18:
        moment = "Bon apres-midi"
    else:
        moment = "Bonsoir"
    return f"{moment} {nom} !"

print(saluer("Lea", 9))   # Bonjour Lea !
print(saluer("Max", 20))  # Bonsoir Max !
```

## Exercice 2 : calculer une moyenne

```python
def moyenne(notes):
    if not notes:
        return 0
    return sum(notes) / len(notes)

print(moyenne([14, 16, 11, 18]))  # 14.75
```

## Exercice 3 : mot de passe valide ?

Ecris une fonction qui verifie qu'un mot de passe fait au moins 8 caracteres et contient un chiffre.

```python
def mdp_valide(mdp):
    if len(mdp) < 8:
        return False
    return any(c.isdigit() for c in mdp)

print(mdp_valide("abc"))       # False
print(mdp_valide("Python3!"))  # True
```

## Exercice 4 : factorielle recursive

```python
def factorielle(n):
    if n <= 1:
        return 1
    return n * factorielle(n - 1)

print(factorielle(5))  # 120
```

> **Astuce DanielCraft** - Teste tes fonctions avec plusieurs cas : cas normal, cas limite (0, vide), cas erreur.

## A retenir

- Une fonction = un nom + des parametres + un `return`.
- Teste chaque fonction isolement avant de l'integrer.
- La recursion est puissante mais attention a la profondeur.
