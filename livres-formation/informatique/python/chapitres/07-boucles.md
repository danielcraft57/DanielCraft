# Chapitre 7 - Les boucles

Une boucle = repeter sans tout retaper.

## for + range

```python
for i in range(1, 6):
    print("Tour", i)
```

`range(1, 6)` = 1, 2, 3, 4, 5 (le 6 est exclu).

```python
for i in range(5):      # 0..4
    print(i)

for i in range(0, 10, 2):  # 0,2,4,6,8
    print(i)
```

## while

```python
vies = 3
while vies > 0:
    print("Il reste", vies, "vies")
    vies = vies - 1
```

Si tu oublies de diminuer `vies` : boucle infinie.
Ctrl+C pour arreter.

## Boucler sur une liste

```python
fruits = ["pomme", "banane", "kiwi"]
for fruit in fruits:
    print(fruit)
```

Avec index :

```python
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)
```

## break et continue

```python
for n in range(1, 10):
    if n == 5:
        break      # stop complet
    if n % 2 == 0:
        continue   # saute le reste du tour
    print(n)
```

`break` = je sors.
`continue` = je passe au tour suivant.

## while True (motif utile)

```python
while True:
    cmd = input("Commande (q pour quitter) : ").strip().lower()
    if cmd == "q":
        break
    print("Tu as tape :", cmd)
```

## Exemple : table de multiplication

```python
n = 8
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

## A toi

Affiche la table de 8 (de 8x1 a 8x10) avec `for` et `range`.
Puis une version `while`.

## En vrai, sur le terrain

Fais une boucle qui compte de 10 a 1, puis affiche "Decollage".

## Mini defi

Demande un mot de passe jusqu'a ce que ce soit le bon (max 3 essais).
Utilise `while` + `break`.
