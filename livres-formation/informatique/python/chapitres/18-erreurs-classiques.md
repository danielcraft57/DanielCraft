# Erreurs classiques en Python

## Les pieges des debutants

Chaque debutant tombe dans les memes pieges. Les connaitre te fait gagner des heures.

## 1. Indentation incorrecte

```python
if True:
print("Erreur")  # IndentationError
```

Toujours 4 espaces apres `:`.

## 2. Confondre = et ==

```python
if x = 5:   # SyntaxError
if x == 5:  # Correct
```

## 3. Modifier une liste pendant l'iteration

```python
nombres = [1, 2, 3, 4, 5]
for n in nombres:
    if n % 2 == 0:
        nombres.remove(n)  # Comportement imprevisible
```

Solution : creer une nouvelle liste filtree.

## 4. Oublier les deux-points

```python
if x > 5    # SyntaxError : il manque le :
    print(x)
```

## 5. Index hors limites

```python
liste = [1, 2, 3]
print(liste[3])  # IndexError : indices 0, 1, 2 seulement
```

## 6. Variable non initialisee

```python
print(total)  # NameError si total n'existe pas encore
```

## 7. Mutable par defaut dans les fonctions

```python
def ajouter(element, liste=[]):  # Piege !
    liste.append(element)
    return liste
```

La liste par defaut est partagee entre les appels. Utilise `None` :

```python
def ajouter(element, liste=None):
    if liste is None:
        liste = []
    liste.append(element)
    return liste
```

> **Astuce DanielCraft** - Lis toujours le message d'erreur en entier. La derniere ligne donne le type, les lignes au-dessus montrent ou.

## A retenir

- Indentation = structure du code.
- `=` assigne, `==` compare.
- Ne modifie pas une liste pendant que tu la parcours.
- Lis les messages d'erreur : ils sont explicites en Python.
