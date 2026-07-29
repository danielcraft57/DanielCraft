# Les fonctions

## Pourquoi des fonctions ?

Une fonction regroupe du code reutilisable sous un nom. Au lieu de copier-coller, tu appelles la fonction.

```python
def saluer(prenom):
    print(f"Bonjour {prenom} !")

saluer("Nora")
saluer("Max")
```

## Parametres et retour

```python
def additionner(a, b):
    return a + b

resultat = additionner(3, 7)
print(resultat)  # 10
```

`return` renvoie une valeur. Sans `return`, la fonction retourne `None`.

## Parametres par defaut

```python
def presenter(nom, langue="francais"):
    print(f"{nom} parle {langue}")

presenter("Lea")             # Lea parle francais
presenter("Tom", "anglais")  # Tom parle anglais
```

> **Astuce DanielCraft** - Une fonction doit faire une seule chose. Si elle fait trop, decoupe-la.

## Fonctions integrees utiles

| Fonction | Role |
|----------|------|
| `len()` | Longueur |
| `max()` / `min()` | Plus grand / petit |
| `abs()` | Valeur absolue |
| `round()` | Arrondir |
| `input()` | Lire une saisie |
| `type()` | Type d'une valeur |

## Petite histoire

Max ecrit 3 fois le meme calcul de TVA. Sam lui montre comment creer `calculer_ttc(prix_ht)` et l'appeler partout. Le code passe de 15 lignes a 6.

## Erreur classique

```python
def dire_bonjour():
    print("Bonjour")

resultat = dire_bonjour()
print(resultat)  # None ! La fonction n'a pas de return.
```

## A retenir

- `def nom(params):` pour definir.
- `return` pour renvoyer une valeur.
- Une fonction = une responsabilite.
