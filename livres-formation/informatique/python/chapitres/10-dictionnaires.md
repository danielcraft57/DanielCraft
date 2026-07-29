# Les dictionnaires

## C'est quoi un dictionnaire ?

Un dictionnaire associe des cles a des valeurs. Comme un vrai dictionnaire : mot -> definition.

```python
personne = {
    "nom": "Lea",
    "age": 28,
    "ville": "Bordeaux"
}
print(personne["nom"])  # Lea
```

## Ajouter et modifier

```python
personne["email"] = "lea@exemple.fr"  # Ajoute
personne["age"] = 29                   # Modifie
del personne["ville"]                  # Supprime
```

## Parcourir un dictionnaire

```python
for cle, valeur in personne.items():
    print(f"{cle}: {valeur}")
```

## Verifier l'existence d'une cle

```python
if "email" in personne:
    print(personne["email"])
```

> **Astuce DanielCraft** - Utilise `.get(cle, defaut)` pour eviter une erreur si la cle n'existe pas.

```python
tel = personne.get("telephone", "Non renseigne")
```

## Methodes utiles

| Methode | Role |
|---------|------|
| `.keys()` | Toutes les cles |
| `.values()` | Toutes les valeurs |
| `.items()` | Paires cle-valeur |
| `.get(k, d)` | Valeur ou defaut |
| `len(d)` | Nombre de paires |

## Petite histoire

Max cree un dictionnaire pour stocker les prix de ses produits. Il parcourt avec `.items()` et calcule le total en 3 lignes.

```python
panier = {"pain": 1.20, "lait": 0.95, "oeufs": 2.50}
total = sum(panier.values())
print(f"Total : {total:.2f} EUR")
```

## A retenir

- Dictionnaire = paires cle-valeur.
- Acces par cle : `dico["cle"]`.
- `.get()` pour eviter les erreurs.
