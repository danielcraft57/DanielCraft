# Les listes

## C'est quoi une liste ?

Une liste stocke plusieurs valeurs dans un seul conteneur, dans un ordre precis.

```python
notes = [14, 17, 11, 19, 8]
print(notes[0])   # 14 (premier element)
print(notes[-1])  # 8 (dernier element)
```

## Ajouter et supprimer

```python
fruits = ["pomme", "banane"]
fruits.append("cerise")      # Ajoute a la fin
fruits.insert(0, "kiwi")     # Insere au debut
fruits.remove("banane")      # Supprime par valeur
del fruits[0]                # Supprime par index
```

## Parcourir une liste

```python
for fruit in fruits:
    print(fruit)
```

Avec l'index :

```python
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

## Tranches (slicing)

```python
nombres = [0, 1, 2, 3, 4, 5]
print(nombres[1:4])   # [1, 2, 3]
print(nombres[:3])    # [0, 1, 2]
print(nombres[3:])    # [3, 4, 5]
```

> **Astuce DanielCraft** - Les indices commencent a 0. `liste[0]` est le premier element.

## Methodes utiles

| Methode | Role |
|---------|------|
| `.append(x)` | Ajoute x a la fin |
| `.pop()` | Retire et retourne le dernier |
| `.sort()` | Trie sur place |
| `.reverse()` | Inverse l'ordre |
| `len(liste)` | Nombre d'elements |

## Petite histoire

Nora stocke les prenoms de sa classe dans une liste. Elle utilise `.sort()` pour les afficher par ordre alphabetique et `len()` pour compter les eleves.

## A retenir

- Liste = collection ordonnee, modifiable.
- Index a partir de 0, negatifs depuis la fin.
- `.append()`, `.remove()`, `.sort()` pour manipuler.
