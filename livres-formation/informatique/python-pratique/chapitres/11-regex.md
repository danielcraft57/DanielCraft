# Chapitre 11 - Regex leger avec re

Une expression reguliere (regex), c'est un motif pour chercher ou valider du texte. Exemple : "est-ce que ca ressemble a un email ?", "trouve tous les numeros", "extraire un code postal".

Attention : les regex peuvent devenir un sport extreme. Ici, on reste leger. Quelques cas utiles avec le module `re`. Chez DanielCraft, consigne : si un `.startswith` ou un `in` suffit, n'utilise pas de regex.

## search : y a-t-il un motif ?

```python
import re

texte = "Contacte-moi : ada@exemple.fr merci"
m = re.search(r"[\w.+-]+@[\w.-]+\.\w+", texte)
if m:
    print("Email trouve :", m.group())
else:
    print("Pas d'email")
```

Le `r"..."` est une raw string : les backslash restent plus lisibles. `search` trouve la premiere occurrence. `m.group()` donne le texte matche.

Ce motif email est simplifie (pas une validation legale absolue). Pour un exercice ou un filtre grossier, ca va. Pour de la vraie validation metier, les regles sont plus riches.

## match vs search vs fullmatch

`search` : quelque part dans la chaine. `match` : au debut. `fullmatch` : la chaine entiere doit correspondre.

```python
print(re.fullmatch(r"\d{5}", "75001"))  # code postal FR simplifie
print(re.fullmatch(r"\d{5}", "7500"))   # None
```

Pour valider une saisie complete, `fullmatch` est souvent le bon reflexe.

## Groupes

Tu veux extraire des morceaux :

```python
m = re.search(r"note\s*[:=]\s*(\d+(?:\.\d+)?)", "note: 14.5")
if m:
    print(float(m.group(1)))
```

Les parentheses capturent. `group(1)` est le premier groupe. Utile pour parser des logs ou des lignes un peu libres.

## findall

```python
texte = "Alice 14, Bob 11, Chloé 16"
notes = re.findall(r"\d+", texte)
print(notes)  # ['14', '11', '16']
```

Tu recuperes une liste de chaines. Convertis ensuite en nombres si besoin.

## Cas utiles du quotidien

Verifier qu'un identifiant ne contient que lettres, chiffres, tirets : `r"^[a-zA-Z0-9_-]+$"`. Chercher une URL grossiere : `r"https?://\S+"`. Remplacer des espaces multiples : `re.sub(r"\s+", " ", texte).strip()`.

```python
propre = re.sub(r"\s+", " ", "  trop   d'espaces  ").strip()
print(propre)
```

## Quand ne pas regex

Compter des lignes CSV : module `csv`. Parser du JSON : `json`. Verifier une extension de fichier : `Path(p).suffix == ".csv"`. Les regex brillent sur du texte irregulier. Sur des formats structures, utilise l'outil du format.

## Erreur classique

Ecrire une regex illegible de trois lignes pour un probleme soluble en deux `split`. Ou oublier `r"..."` et se battre avec les `\` escapes. Ou croire qu'une regex email "parfaite" existe en dix caracteres.

## En vrai

Prends un paragraphe avec un email et un numero a 5 chiffres. Extraie les deux avec `search` / `findall`. Puis valide une saisie code postal avec `fullmatch`.

## A toi

Ecris `extraire_emails(texte)` qui retourne une liste (peut-etre vide). Teste avec 0, 1, 2 emails dans la chaine. Simple, utile, et tu as touche le coeur de `re` sans te noyer.
