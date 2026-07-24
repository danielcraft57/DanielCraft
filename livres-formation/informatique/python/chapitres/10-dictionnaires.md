# Chapitre 10 - Les dictionnaires

Un dictionnaire = une fiche avec des cles (pas seulement des numeros).

```python
joueur = {
    "prenom": "Sam",
    "score": 120,
    "actif": True,
}

print(joueur["prenom"])
joueur["score"] = joueur["score"] + 10
joueur["niveau"] = 2  # nouvelle cle
```

## Cle absente

```python
print(joueur.get("niveau", 1))
```

Si "niveau" n'existe pas, tu obtiens 1.
Avec `joueur["niveau"]` direct : erreur si absent.

## Parcourir

```python
for cle, valeur in joueur.items():
    print(cle, "->", valeur)

print(joueur.keys())
print(joueur.values())
```

## Liste de dictionnaires

```python
equipe = [
    {"prenom": "Sam", "score": 120},
    {"prenom": "Lea", "score": 95},
]
print(equipe[0]["prenom"])

for j in equipe:
    print(f"{j['prenom']} : {j['score']}")
```

## Compter avec un dico

```python
votes = ["chat", "chien", "chat", "oiseau", "chat"]
compteur = {}
for mot in mots:
    compteur[mot] = compteur.get(mot, 0) + 1
print(compteur)
```

Pattern tres courant.

## JSON dans la tete

Un dictionnaire Python ressemble beaucoup a du JSON.
Tu t'en serviras pour sauvegarder des configs, des scores, des API...

## A toi

Cree un dico `livre` avec titre, pages, lu (True/False).
Affiche une phrase complete.
Ajoute une cle `auteur`.

## En vrai, sur le terrain

Fais une petite "fiche eleve" (nom, moyenne, classe).
Modifie la moyenne. Reaffiche.

## Mini defi

Liste de 3 produits `{nom, prix}`.
Affiche le total des prix avec une boucle.
