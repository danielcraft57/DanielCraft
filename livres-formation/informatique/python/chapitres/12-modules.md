# Chapitre 12 - Les modules (import)

Un module, c'est une boite a outils deja prete. Au lieu de reinventer la racine carree, tu `import math`. Au lieu de bricoler un tireage au sort douteux, tu `import random`. Au lieu de parser des dates a la main, tu regardes `datetime`. Python standard est riche. Apprends a chercher dedans avant d'installer le monde entier avec `pip`. En 2026, la tentation du "installe ce paquet" est partout. Resiste un peu. Souvent, la bibliotheque standard suffit pour un debut solide.

Chez DanielCraft, on adore ce reflexe : module standard d'abord, bibliotheque tierce ensuite. Lea a perdu du temps a installer des paquets pour des choses que `pathlib` faisait deja. Max a decouvert `random.randint` et a fait un de en trois lignes. Sam fait tirer des conseils au hasard pour montrer qu'`import` n'est pas intimidant. Trois chemins, meme lecon : tu n'es pas seul face a la machine. Des outils existent. Apprends a les appeler.

```python
import math
print(math.sqrt(16))
print(math.pi)
```

## Ce que ce n'est pas

Un module, ce n'est pas un virus mysterieux. Ce n'est pas non plus "du code que tu ne peux pas comprendre". Souvent, tu peux ouvrir la doc ou meme le fichier source plus tard. Ce n'est pas obligatoire d'utiliser `from math import *` (mauvaise idee : tu pollues ton espace de noms). Et ce n'est surtout pas la meme chose qu'une fonction : le module contient des fonctions, des constantes, parfois des classes.

Ce n'est pas non plus "pip install pour tout". `pip` est utile. Il n'est pas le premier geste. D'abord `import` ce qui est deja la. Ensuite seulement, une dependance claire, isolee plus tard dans un venv (livre pratique).

Tu as ton atelier. Sur l'etagere, des boites etiquetees `math`, `random`, `json`, `datetime`. `import math` pose la boite sur la table. Tu appelles `math.sqrt`. `from math import sqrt` sort juste l'outil `sqrt` et le pose devant toi. Quand ton projet grandit, tu crees ta propre boite `outils.py` et tu l'importes. C'est le meme geste. Tu passes de consommateur a auteur de module. Chez DanielCraft, ce passage est un rite de passage doux : tu ranges ton propre code comme Python range le sien.

Lea importe `json` pour ses configs. Max importe `random` pour ses jeux. Sam importe `datetime` pour dater un quiz. Puis chacun cree un petit module perso. Le geste devient naturel.

## random, datetime, from import

```python
import random

print(random.randint(1, 6))  # de 1 a 6 inclus
print(random.choice(["rouge", "vert", "bleu"]))
print(random.random())       # flottant entre 0 et 1

cartes = [1, 2, 3, 4, 5]
random.shuffle(cartes)
print(cartes)
```

```python
from datetime import datetime
maintenant = datetime.now()
print(maintenant.strftime("%Y-%m-%d %H:%M"))
```

Utile pour dater un log ou un score. Lea date ses journaux. Max horodate un devis exporte. Sam affiche l'heure au debut d'un quiz.

```python
from math import pi, sqrt
print(pi, sqrt(9))
```

Utile quand tu utilises deux-trois symboles souvent. Evite l'etoile `*`. Prefere la liste explicite. Ton futur toi te remerciera.

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

Pratique quand le projet grandit. Mets les deux fichiers dans le meme dossier pour debuter. Plus tard tu apprendras les packages. Ici, le geste compte : decouper. Si `import outils` echoue, regarde d'abord le dossier courant du terminal. Neuf fois sur dix, c'est ca.

## pip (apercu)

Pour installer une bibliotheque tierce :

```bash
pip install requests
```

Puis tu pourras `import requests`. On ne l'utilise pas dans ce livre. Mais tu dois connaitre le reflexe : module standard d'abord, `pip` ensuite, environnement virtuel encore apres. Chez DanielCraft, on refuse le "installe tout ce que le tuto cite" sans comprendre pourquoi. Une dependance, c'est une dette. Prends-la volontairement.

## Petite histoire

Max a simule un de a 6 faces cinq fois, additionne, affiche. Sensation de jeu immediate. Lea a melange une liste de prenoms avec `shuffle` pour un ordre de passage en reunion. Sam a code un "oracle" : cinq conseils, un tire au hasard. Les eleves ont rit, puis ont demande "et si je cree mon module ?". Reponse : cree `conseils.py` avec une liste et une fonction `tire()`. C'est exactement l'esprit du chapitre. Amusement d'abord, organisation ensuite, autonomie apres.

## Erreur classique

Importer sans etre dans le bon dossier (ton module perso introuvable). Confondre le nom du fichier et le nom importe (`outils.py` -> `import outils`). Faire `from random import random` puis s'etonner que `random.randint` ne marche plus pareil. Autre piege : reinstaller des paquets globalement en desordre - plus tard, le venv t'aidera. Pour l'instant, reste sur la bibliotheque standard. Lea a aussi nomme un fichier `random.py` et a casse l'import du vrai module. Evite les noms qui existent deja.

## En vrai

Melange une liste de 5 prenoms avec `shuffle`, affiche le premier "tire au sort". Puis petit "oracle" : tire une phrase au hasard dans une liste de 5 conseils. Relance plusieurs fois. Observe que le hasard change. C'est voulu.

## A toi

Simule un de a 6 faces 5 fois avec une boucle. Affiche aussi la somme des jets. Bonus : cree `outils.py` avec une fonction `moyenne(liste)` et utilise-la depuis un autre fichier. Si l'import echoue, note le dossier du terminal et corrige. Ce diagnostic te servira toute ta vie de scripteur.

## Zoom : import math vs from math import sqrt

Les deux marchent. Le premier garde le "nom de famille" (`math.sqrt`). Le second pose l'outil nu sur la table (`sqrt`). Prefere le premier quand tu debutes : tu vois d'ou vient la fonction. Prefere le second quand tu utilises deux-trois symboles souvent et que le fichier reste lisible. Chez DanielCraft, on evite `import *` : trop de surprise, trop peu de clarte.
