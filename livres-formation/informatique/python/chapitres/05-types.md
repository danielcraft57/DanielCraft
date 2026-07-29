# Les types de donnees

## Les types de base

Python a plusieurs types principaux :

| Type | Exemple | Usage |
|------|---------|-------|
| `int` | `42` | Nombres entiers |
| `float` | `3.14` | Nombres decimaux |
| `str` | `"Bonjour"` | Texte |
| `bool` | `True` / `False` | Vrai ou faux |

## Verifier un type

```python
age = 25
print(type(age))  # <class 'int'>
```

La fonction `type()` te dit quel type a une valeur.

## Conversion de types

```python
texte = "42"
nombre = int(texte)  # Convertit la chaine en entier
print(nombre + 8)    # 50
```

> **Astuce DanielCraft** - `input()` retourne toujours une chaine. Convertis avec `int()` ou `float()` si tu veux un nombre.

## Operations sur les nombres

```python
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3 (division entiere)
print(a % b)   # 1 (reste)
print(a ** b)  # 1000 (puissance)
```

## Operations sur les chaines

```python
nom = "Lea"
print(nom.upper())    # LEA
print(nom.lower())    # lea
print(len(nom))       # 3
print("a" in nom)     # False (sensible casse: 'a' pas dans 'Lea')
```

## Petite histoire

Nora demande l'age de l'utilisateur avec `input()`. Elle oublie de convertir et fait `age + 1`. Python concatene au lieu d'additionner. Elle ajoute `int()` et tout fonctionne.

## A retenir

- `int`, `float`, `str`, `bool` sont les types de base.
- `type()` pour verifier, `int()` / `str()` pour convertir.
- `input()` retourne toujours une chaine.
