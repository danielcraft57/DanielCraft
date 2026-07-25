# Chapitre 15 - Les exceptions (try / except)

Parfois le programme plante. Pas grave. On peut rattraper. L'exemple classique : l'utilisateur tape une lettre au lieu d'un nombre. Sans `try/except`, ton script meurt avec une trace rouge. Avec `try/except`, tu affiches un message clair et tu continues - ou tu redemandes. Ce n'est pas "cacher la poussiere". C'est piloter l'imprevu.

Chez DanielCraft, on refuse deux extremes : tout laisser planter "pour apprendre", et tout avaler avec un `except:` silencieux. Lea protege les saisies clients. Max protege ses divisions. Sam force les eleves a lire d'abord l'erreur nue, puis a proteger. Comprendre avant d'envelopper. Si tu enveloppes trop tot, tu n'apprends rien. Si tu n'enveloppes jamais, ton outil est fragile des qu'un humain tape de travers.

```python
texte = input("Nombre ? ")
try:
    n = int(texte)
    print("Tu as choisi", n)
except ValueError:
    print("Ce n'est pas un nombre.")
```

`try` = j'essaie. `except` = si ca casse de cette facon, je fais autre chose. Tu choisis le type d'erreur. Tu choisis le message. Tu restes responsable du comportement.

:::retenir
Lis l'erreur nue une fois. Puis protege l'endroit qui glisse vraiment - pas tout le programme.
:::

## Ce que ce n'est pas

`try/except`, ce n'est pas un permis de coder sale. Ce n'est pas non plus obligatoire autour de chaque ligne. Ce n'est pas interchangeable avec un `if` : parfois tu verifies avant (`if b != 0`), parfois tu attrapes apres (`ZeroDivisionError`). Et ce n'est surtout pas `except:` + `pass` partout. Le silence total t'empeche d'apprendre et te cache des bugs. Un filet trop large, c'est une piece sans fenetre : tu ne vois plus ou ca fuit.

Tu marches sur une planche. `try` : tu avances. Si la planche casse d'une facon prevue (`ValueError`, `FileNotFoundError`...), `except` te donne une autre marche. `else` : "si rien n'a casse, fais ca". `finally` : "quoi qu'il arrive, nettoie". `raise` : "je signale moi-meme un probleme clair". Tu ne construis pas un bunker. Tu poses des filets aux endroits ou ca glisse souvent. Lea met un filet sur la saisie. Max met un filet sur la division. Sam met un filet sur l'ouverture de fichier. Trois filets, meme idee.

## Plusieurs erreurs, else, finally, raise

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

```python
def age_valide(age):
    if age < 0:
        raise ValueError("Age negatif impossible")
    return age

print(age_valide(12))
# print(age_valide(-1))  # plante volontairement
```

Utile dans tes fonctions : signaler un probleme clair. Lea leve des erreurs explicites plutot que de renvoyer des valeurs magiques illegibles. Max preferait renvoyer `-1` "pour dire erreur". Puis il a meange son propre `-1` comme un vrai age. Depuis, il leve. Sam applaudit.

## Ne pas tout avaler + fichier manquant

Mauvais reflexe :

```python
try:
    faire_un_truc()
except:
    pass  # silence total = tu ne vois plus rien
```

Mieux : attraper l'erreur precise, ou au moins afficher un message.

```python
from pathlib import Path

p = Path("secret.txt")
try:
    print(p.read_text(encoding="utf-8"))
except FileNotFoundError:
    print("Fichier introuvable. On continue.")
```

Le message dit quoi faire a l'humain. Le type d'exception dit quoi comprendre au programmeur. Les deux comptent.

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

Tu peux reutiliser ca partout. Max l'a copie dans son devis. Sam l'exige dans le juste prix. Chez DanielCraft, une petite fonction robuste vaut mieux qu'un discours sur "la qualite". Une fois cette brique posee, tes programmes deviennent moins dramatiques : l'utilisateur se trompe, tu redemandes, la vie continue.

## Petite histoire

Lea a livre un script qui plantait si le client mettait une virgule francaise dans un nombre. Elle a ajoute un message, puis une normalisation simple. Le client a arrete d'appeler. Max a fait planter `int("bonjour")` volontairement, a lu `ValueError`, a compris mieux qu'avec un schema. Sam dit : "si tu ne sais pas lire l'erreur, le `try` ne te sauvera pas - il te rendra juste aveugle plus tard".

Autre scene : Sam projette une traceback complete au tableau. Personne ne parle. Puis il souligne la derniere ligne. "Ca, c'est le GPS." Ensuite seulement, il enveloppe. Les eleves retiennent le geste, pas le jargon.

## Erreur classique

Attraper trop large. Ignorer le type d'exception. Mettre trop de logique dans le `try` (tu ne sauras plus quelle ligne a casse). Croire que `except` "repare" automatiquement - non, tu choisis quoi faire. Autre piege : masquer une vraie bug de logique derriere un filet trop large. Si ton calcul est faux, un `try` ne le rendra pas juste. Il le cachera peut-etre.

:::attention
`except:` + `pass`, c'est le silence total. Tu ne debogues plus. Tu subis.
:::

## En vrai

Fais planter volontairement `int("bonjour")` sans try. Lis l'erreur jusqu'a la derniere ligne. Note le nom de l'exception. Puis protege. Ecris `diviser(a, b)` qui renvoie le resultat ou `None` si division par zero, avec un message clair. Teste avec `10, 2` puis `10, 0`. Regarde la difference de comportement. C'est ca, piloter.

## A toi

Reprends le juste prix (ou un `int(input(...))`). Entoure la conversion avec `try/except`. Si erreur : message + redemande. Bonus : utilise `demander_int` partout ou tu convertis. Super bonus : ajoute un compteur de mauvaises saisies et un message different apres trois echecs.

## Zoom : try serre, logique claire

Garde le `try` court. Convertis. Calcule le minimum. Sors. Le message et la suite vivent dehors. Lea a longtemps mis dix lignes dans un seul `try`. Quand ca cassait, elle ne savait plus laquelle. Depuis, elle coupe. Chez DanielCraft, on dit : filet petit, idee grande. Tu verras la meme logique plus tard avec le reseau (`requests`) : timeout, status, JSON - trois filets precis, pas un mur opaque.
