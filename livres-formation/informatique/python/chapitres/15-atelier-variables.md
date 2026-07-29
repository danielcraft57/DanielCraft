# Atelier : variables et types

## Objectif

Mettre en pratique les variables, les types et les conversions vus aux chapitres 4 et 5.

## Exercice 1 : carte d'identite

Cree un programme qui stocke ton prenom, ton age et ta ville dans des variables, puis affiche une phrase complete avec une f-string.

```python
prenom = "Sam"
age = 22
ville = "Nantes"
print(f"Je suis {prenom}, {age} ans, je vis a {ville}.")
```

## Exercice 2 : convertisseur EUR -> USD

Demande un montant en euros, convertis en dollars (taux 1.08) et affiche le resultat arrondi a 2 decimales.

```python
euros = float(input("Montant en EUR : "))
dollars = euros * 1.08
print(f"{euros} EUR = {dollars:.2f} USD")
```

## Exercice 3 : swap de variables

Echange les valeurs de deux variables sans utiliser de troisieme variable.

```python
a = 5
b = 9
a, b = b, a
print(a, b)  # 9 5
```

## Defi bonus

Demande le rayon d'un cercle et affiche son perimetre et son aire.

```python
import math
rayon = float(input("Rayon : "))
print(f"Perimetre : {2 * math.pi * rayon:.2f}")
print(f"Aire : {math.pi * rayon**2:.2f}")
```

> **Astuce DanielCraft** - Teste avec des valeurs extremes : 0, negatif, tres grand.

## A retenir

- Les f-strings facilitent l'affichage formate.
- `float()` pour convertir une saisie en nombre decimal.
- Python permet le swap elegant : `a, b = b, a`.
