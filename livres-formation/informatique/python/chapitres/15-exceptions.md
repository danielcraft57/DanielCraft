# Chapitre 15 - Les exceptions (try / except)

Parfois le programme plante.
Pas grave. On peut rattraper.

Exemple classique : l'utilisateur tape une lettre au lieu d'un nombre.

```python
texte = input("Nombre ? ")
try:
    n = int(texte)
    print("Tu as choisi", n)
except ValueError:
    print("Ce n'est pas un nombre.")
```

`try` = j'essaie.
`except` = si ca casse de cette facon, je fais autre chose.

## Plusieurs erreurs

```python
try:
    a = int(input("a ? "))
    b = int(input("b ? "))
    print(a / b)
except ValueError:
    print("Il faut des nombres.")
except ZeroDivisionError:
    print("Division par zero interdite.")
```

## else et finally

```python
try:
    n = int(input("Nombre ? "))
except ValueError:
    print("Nope")
else:
    print("OK, n =", n)   # seulement si pas d'erreur
finally:
    print("Toujours execute")
```

`finally` sert souvent a "nettoyer" (fermer un truc), meme en cas d'erreur.

## raise (lever une erreur)

```python
def age_valide(age):
    if age < 0:
        raise ValueError("Age negatif impossible")
    return age

print(age_valide(12))
# print(age_valide(-1))  # plante volontairement
```

Utile dans tes fonctions : signaler un probleme clair.

## Ne pas tout avaler

Mauvais reflexe :

```python
try:
    faire_un_truc()
except:
    pass  # silence total = tu ne vois plus rien
```

Mieux : attraper l'erreur precise, ou au moins afficher un message.

## Fichier manquant

```python
from pathlib import Path

p = Path("secret.txt")
try:
    print(p.read_text(encoding="utf-8"))
except FileNotFoundError:
    print("Fichier introuvable. On continue.")
```

## Exemple utile : saisie solide

```python
def demander_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Un entier, s'il te plait.")

age = demander_int("Age ? ")
print("Age =", age)
```

Tu peux reutiliser ca partout.

## A toi

Reprends le juste prix (ou un `int(input(...))`).
Entoure la conversion avec `try/except`.
Si erreur : message + redemande.

## En vrai, sur le terrain

Fais planter volontairement `int("bonjour")` sans try.
Lis l'erreur. Puis protege.

## Mini defi

Fonction `diviser(a, b)` qui renvoie le resultat ou `None` si division par zero,
avec un message clair.
