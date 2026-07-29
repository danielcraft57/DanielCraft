# Atelier : listes et dictionnaires

## Objectif

Manipuler des collections : ajouter, filtrer, trier, transformer.

## Exercice 1 : filtrer les pairs

```python
nombres = [3, 8, 1, 12, 7, 4, 15, 2]
pairs = [n for n in nombres if n % 2 == 0]
print(pairs)  # [8, 12, 4, 2]
```

## Exercice 2 : compteur de mots

```python
phrase = "le chat dort le chat mange le chat joue"
mots = phrase.split()
compteur = {}
for mot in mots:
    compteur[mot] = compteur.get(mot, 0) + 1
print(compteur)
# {'le': 3, 'chat': 3, 'dort': 1, 'mange': 1, 'joue': 1}
```

## Exercice 3 : inverser une liste sans .reverse()

```python
def inverser(lst):
    return lst[::-1]

print(inverser([1, 2, 3, 4]))  # [4, 3, 2, 1]
```

## Exercice 4 : carnet d'adresses

```python
carnet = []

def ajouter_contact(nom, email):
    carnet.append({"nom": nom, "email": email})

def trouver(nom):
    return [c for c in carnet if nom.lower() in c["nom"].lower()]

ajouter_contact("Nora Duval", "nora@exemple.fr")
ajouter_contact("Max Petit", "max@exemple.fr")
print(trouver("nora"))
```

## Defi : top 3 des notes

```python
notes = [8, 14, 19, 11, 17, 6, 15]
top3 = sorted(notes, reverse=True)[:3]
print(f"Top 3 : {top3}")  # [19, 17, 15]
```

> **Astuce DanielCraft** - Les list comprehensions rendent le code compact. Mais si ca devient illisible, utilise une boucle classique.

## A retenir

- `[expr for x in liste if cond]` : list comprehension.
- `.get(cle, defaut)` evite les KeyError.
- `sorted()` cree une nouvelle liste triee.
