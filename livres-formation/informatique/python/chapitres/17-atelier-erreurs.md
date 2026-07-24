# Chapitre 17 - Atelier : lire les erreurs

Le terminal parle. Apprends a l'ecouter.
Une erreur, c'est un GPS, pas une insulte.

## NameError

Tu utilises un nom inconnu.
Souvent une faute de frappe : `scroe` au lieu de `score`.

## TypeError

Tu melanges mal les types.
Ex : `"3" + 1`

## ValueError

Conversion impossible.
Ex : `int("bonjour")`

## IndexError / KeyError

```python
liste = [1, 2]
print(liste[5])          # IndexError
d = {"a": 1}
print(d["b"])            # KeyError
```

## IndentationError / SyntaxError

Deux points `:` oublie, ou decalage foireux.
Ou parenthese non fermee.

## FileNotFoundError

Mauvais chemin, mauvais dossier, fichier pas encore cree.

## Methode

Lis d'abord la **derniere** ligne de l'erreur (le type). Va au numero de ligne. Corrige le plus petit truc, puis relance. Si besoin, entoure avec `try/except` - mais comprends d'abord.

## Exercice 1

Casse volontairement ton quiz (enleve un `:`).
Lis l'erreur. Repare.

## Exercice 2

Fais un `int(input(...))` et tape `abc`.
Puis protege avec `try/except` comme au chapitre 15.

## Exercice 3

Ouvre un fichier qui n'existe pas.
Attrape `FileNotFoundError`. Affiche un message propre.

## Check final atelier

Tu sais nommer 4 types d'erreurs courants, trouver la ligne fautive, et corriger sans tout reecrire.
