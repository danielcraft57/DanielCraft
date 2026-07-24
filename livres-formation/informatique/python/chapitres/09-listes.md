# Chapitre 9 - Les listes

Une liste range plusieurs valeurs, une apres l'autre.

```python
courses = ["pain", "lait", "oeufs"]
print(courses[0])  # pain
print(courses[-1]) # oeufs (dernier)
```

L'index commence a **0**.
`-1` = dernier element. Pratique.

## Modifier / longueur

```python
courses[1] = "lait d'avoine"
print(len(courses))
```

## Ajouter / retirer

```python
courses.append("beurre")
courses.insert(0, "eau")
dernier = courses.pop()
courses.remove("pain")  # enleve la premiere occurrence
```

## Parcourir

```python
for item in courses:
    print("-", item)
```

## in

```python
if "pain" in courses:
    print("On a du pain")
```

## Tranches (slices)

```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])   # 1,2,3
print(nums[:3])    # 0,1,2
print(nums[3:])    # 3,4,5
print(nums[::-1])  # inverse
```

## Trier

```python
notes = [12, 8, 15, 10]
print(sorted(notes))       # nouvelle liste
notes.sort()               # modifie sur place
notes.sort(reverse=True)
```

## List comprehension (avance soft)

```python
carres = [n * n for n in range(1, 6)]
print(carres)  # [1, 4, 9, 16, 25]

pairs = [n for n in range(10) if n % 2 == 0]
```

C'est une boucle `for` en une ligne.
Lisible si c'est court. Sinon, garde une boucle classique.

## Tuple (cousin fige)

```python
point = (10, 20)
# point[0] = 11  # erreur : tuple non modifiable
```

Utile pour des paires fixes (coordonnees, resultat double...).

## Ensemble set (apercu)

```python
tags = {"python", "debutant", "python"}
print(tags)  # les doublons sautent
```

## A toi

Liste de 4 jeux.
Ajoute-en un avec `append`.
Affiche tout avec une boucle.
Affiche aussi le dernier avec `[-1]`.

## En vrai, sur le terrain

Fais une liste de notes. Calcule la moyenne avec une boucle.

## Mini defi

A partir de `[1,2,3,4,5,6]`, cree la liste des pairs avec une comprehension.
