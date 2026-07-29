# Les boucles

## Repeter sans copier

Une boucle execute un bloc plusieurs fois. Deux types : `for` (nombre de fois connu) et `while` (condition).

## La boucle for

```python
for i in range(5):
    print(i)
# Affiche 0, 1, 2, 3, 4
```

`range(5)` genere les nombres de 0 a 4. Le bloc indente se repete 5 fois.

## Parcourir une liste

```python
fruits = ["pomme", "banane", "cerise"]
for fruit in fruits:
    print(fruit)
```

## La boucle while

```python
compteur = 0
while compteur < 3:
    print(compteur)
    compteur += 1
```

> **Piege** - Si tu oublies `compteur += 1`, la boucle tourne a l'infini. Ctrl+C pour arreter.

## break et continue

```python
for i in range(10):
    if i == 5:
        break  # Sort de la boucle
    if i % 2 == 0:
        continue  # Passe au tour suivant
    print(i)  # Affiche 1, 3
```

> **Astuce DanielCraft** - Prefere `for` quand tu connais le nombre de tours. `while` quand tu attends une condition.

## Petite histoire

Sam doit afficher les tables de multiplication de 1 a 10. Deux boucles imbriquees et c'est fait en 4 lignes.

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
```

## A retenir

- `for` pour un nombre connu d'iterations.
- `while` pour une condition.
- `break` sort, `continue` passe au suivant.
