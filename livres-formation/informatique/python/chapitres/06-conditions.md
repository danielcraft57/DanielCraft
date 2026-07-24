# Chapitre 6 - Les conditions (if)

Les conditions, c'est "si ... alors ... sinon ...".

```python
age = 15

if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

L'indentation (decalage) est obligatoire en Python.
En general : 4 espaces.
Sans ca, Python refuse. Ce n'est pas du decoratif.

## elif

```python
note = 14

if note >= 16:
    print("Excellent")
elif note >= 10:
    print("Valide")
else:
    print("On revise")
```

`elif` = "sinon si".
Tu peux en chainer plusieurs.

## Comparaisons

- `==` egal (valeur)
- `!=` different
- `>`, `<`, `>=`, `<=`

Attention : `=` assigne. `==` compare.

## and / or / not

```python
ticket = True
vip = False

if ticket or vip:
    print("Entre")

if ticket and vip:
    print("Acces premium")

if not vip:
    print("Pas VIP")
```

## Conditions avec texte

```python
mdp = input("Mot de passe ? ").strip()
if mdp == "python123":
    print("OK")
else:
    print("Refuse")
```

Souvent on compare en minuscules :

```python
if mdp.lower() == "python123":
    print("OK")
```

## Operateur ternaire (apercu)

```python
age = 20
statut = "majeur" if age >= 18 else "mineur"
print(statut)
```

Pratique pour une petite decision. Pas obligatoire.

## Exemple complet

```python
score = int(input("Score ? "))
vies = int(input("Vies ? "))

if score >= 100 and vies > 0:
    print("Niveau suivant")
elif vies == 0:
    print("Game over")
else:
    print("Continue")
```

## A toi

Demande un mot de passe.
Si c'est `"python123"`, affiche "OK".
Sinon "Refuse".
Bonus : accepte aussi avec majuscules mixees via `.lower()`.

## En vrai, sur le terrain

Change les seuils de l'exemple note. Relance avec 9, 10, 16.

## Mini defi

Programme "meteo" : si temperature < 0 -> "froid", < 20 -> "doux", sinon "chaud".
