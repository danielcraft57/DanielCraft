# Chapitre 8 - Les fonctions

Une fonction = une recette reutilisable.
Tu la definis une fois. Tu l'appelles quand tu veux.

```python
def dire_salut():
    print("Salut !")

dire_salut()
dire_salut()
```

## Avec parametre

```python
def dire_salut_a(prenom):
    print(f"Salut {prenom}")

dire_salut_a("Nora")
dire_salut_a("Sam")
```

## return

```python
def double(n):
    return n * 2

resultat = double(4)
print(resultat)  # 8
```

Sans `return`, la fonction renvoie `None`.
`print` affiche. `return` renvoie une valeur au code appelant.
Ce n'est pas la meme chose.

## Valeur par defaut

```python
def saluer(prenom="ami"):
    print(f"Salut {prenom}")

saluer()
saluer("Lea")
```

## Plusieurs parametres

```python
def moyenne(a, b):
    return (a + b) / 2

print(moyenne(12, 16))
```

## Petite doc

Au-dessus du corps, tu peux laisser un commentaire clair :

```python
def carre(n):
    # Renvoie n au carre
    return n * n
```

Plus tard tu verras aussi les "docstrings" (texte entre triples guillemets).
Meme idee : expliquer le role de la fonction.

## *args (apercu avance)

Parfois tu veux un nombre variable d'arguments :

```python
def somme(*nombres):
    total = 0
    for n in nombres:
        total += n
    return total

print(somme(1, 2, 3, 4))  # 10
```

Tu n'es pas oblige de l'utiliser tout de suite.
Mais tu le croiseras dans du vrai code.

## Pourquoi c'est bien

- Moins de copie
- Code plus clair
- Plus facile a corriger
- Tu testes une brique a la fois

## Exemple complet

```python
def note_sur_20(points, total):
    if total == 0:
        return 0
    return round(points / total * 20, 1)

print(note_sur_20(15, 20))
print(note_sur_20(7, 10))
```

## A toi

Ecris `moyenne(a, b)` qui renvoie la moyenne.
Puis `moyenne3(a, b, c)`.
Teste.

## En vrai, sur le terrain

Ecris une fonction `est_pair(n)` qui renvoie True/False.
Teste avec 2, 3, 10.

## Mini defi

Fonction `presenter(prenom, age)` qui retourne une phrase (pas print).
Tu printes le resultat a l'exterieur.
