# Chapitre 4 - Les variables

Une variable = une boite avec un nom.
Tu ranges une valeur. Tu la reutilises plus tard.

```python
age = 12
prenom = "Leo"
score = 0
```

Pas besoin de dire "c'est un nombre" ou "c'est du texte".
Python regarde la valeur et comprend.

## Changer une valeur

```python
score = 0
score = score + 1
score += 5  # raccourci : score = score + 5
print(score)
```

Le nom reste. Le contenu peut changer.

## Noms clairs

Oui :

```python
nombre_de_vies = 3
message_accueil = "Salut"
```

Non (ou alors on se perd) :

```python
x1 = 3
a = "Salut"
```

En Python, on utilise souvent le `snake_case` : mots separes par `_`.
C'est la convention. Suis-la. Ton futur toi te remerciera.

## Plusieurs infos

```python
a = 3
b = 5
total = a + b
print(total)
```

Tu peux aussi echanger :

```python
x = 1
y = 2
x, y = y, x
print(x, y)  # 2 1
```

## Constantes (habitude)

Python n'a pas de vrai `const` comme certains langages.
Par convention, on ecrit en MAJUSCULES ce qu'on ne veut pas changer :

```python
MAX_ESSAIS = 5
```

Ce n'est pas bloque techniquement. C'est un signal pour les humains.

## Attention

```python
# piege : ecraser sans faire gaffe
score = 10
score = "dix"  # autorise, mais souvent une mauvaise idee
```

Une variable peut changer de type. Ca ne veut pas dire que c'est clair.

## Exemple complet

```python
pseudo = "PixelFox"
niveau = 1
xp = 0

xp += 50
print(f"{pseudo} a {xp} xp")

if xp >= 50:
    niveau += 1
    xp -= 50
    print(f"Niveau up ! Niveau {niveau}")

print(f"Etat : niveau {niveau}, xp {xp}")
```

## A toi

Cree :
- `prenom`
- `points` (commence a 0)
- ajoute 10 points
- affiche le tout avec `print` ou une f-string

## En vrai, sur le terrain

Retape l'exemple joueur.
Change le pseudo et le seuil d'xp. Relance.

## Mini defi

Invente un mini profil (jeu, sport, ecole).
3 variables minimum. Affiche une phrase complete.
