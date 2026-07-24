# Chapitre 5 - Les types (texte, nombre, vrai/faux)

Les types, c'est la nature de ce que tu ranges dans la boite.

## Texte (str)

```python
phrase = "Bonjour"
ville = 'Lyon'  # simples ou doubles, au choix
```

## Nombre entier (int)

```python
vies = 3
```

## Nombre a virgule (float)

```python
prix = 19.99
```

## Booleen (bool)

```python
est_connecte = True
a_fini = False
```

Attention : `True` / `False` avec majuscule.
Pas `true` comme en JS.

## Conversion

`input` donne du texte. Pour calculer, convertis :

```python
age_texte = input("Age ? ")
age = int(age_texte)
print("Dans 10 ans :", age + 10)
```

Versions courtes :

```python
n = int(input("Nombre ? "))
prix = float(input("Prix ? "))
```

Si la personne ecrit "douze", `int(...)` plante.
Normal. Au chapitre exceptions, on apprendra a rattraper ca.

## type()

```python
print(type(3))      # int
print(type("3"))    # str
print(type(3.0))    # float
print(type(True))   # bool
```

Utile pour comprendre ce que tu as vraiment.

## Pieges classiques

```python
print("3" + "1")   # "31" (colle du texte)
print(3 + 1)       # 4
# print("3" + 1)   # TypeError
```

Et :

```python
print(bool(""))     # False (texte vide)
print(bool("0"))    # True (texte non vide)
print(bool(0))      # False
```

## None

```python
valeur = None  # "pas de valeur" volontaire
```

Tu le croiseras avec les fonctions qui ne renvoient rien.

## A toi

Demande deux nombres (via `input` + `int`).
Affiche leur somme, leur difference, leur produit.

## En vrai, sur le terrain

Teste `type()` sur 4 valeurs differentes dans la console interactive.

## Mini defi

Demande un prix en texte, convertis en `float`, ajoute 20% (TVA simple), affiche le TTC.
