# Chapitre 12 - Les modules (import)

Un module = une boite a outils deja prete.

```python
import math
print(math.sqrt(16))
print(math.pi)
```

## random

```python
import random

print(random.randint(1, 6))  # de 1 a 6 inclus
print(random.choice(["rouge", "vert", "bleu"]))
print(random.random())       # flottant entre 0 et 1
```

```python
cartes = [1, 2, 3, 4, 5]
random.shuffle(cartes)
print(cartes)
```

## datetime (apercu)

```python
from datetime import datetime
maintenant = datetime.now()
print(maintenant.strftime("%Y-%m-%d %H:%M"))
```

Utile pour dater un log ou un score.

## from ... import

```python
from math import pi, sqrt
print(pi, sqrt(9))
```

## Creer ton module

Fichier `outils.py` :

```python
def double(n):
    return n * 2
```

Autre fichier :

```python
import outils
print(outils.double(5))
```

Pratique quand le projet grandit.

## pip (apercu)

Pour installer une bibliotheque tierce :

```bash
pip install requests
```

Puis :

```python
# import requests  # apres install
```

On ne l'utilise pas dans ce livre.
Mais tu dois connaitre le reflexe : module standard d'abord, `pip` ensuite.

## A toi

Simule un de a 6 faces 5 fois avec une boucle.
Affiche aussi la somme des jets.

## En vrai, sur le terrain

Melange une liste de 5 prenoms avec `shuffle`, affiche le premier "tire au sort".

## Mini defi

Petit "oracle" : tire une phrase au hasard dans une liste de 5 conseils.
