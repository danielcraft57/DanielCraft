# Bonnes pratiques

## Ecrire du code lisible

Le code est lu bien plus souvent qu'il n'est ecrit. La lisibilite est prioritaire.

## Nommage

- Variables et fonctions : `snake_case` (ex: `prix_total`, `calculer_moyenne`).
- Constantes : `MAJUSCULES` (ex: `TVA = 0.20`).
- Classes : `PascalCase` (ex: `CompteBancaire`).
- Noms explicites : `age` plutot que `a`, `liste_clients` plutot que `lc`.

## Structure du code

```python
# 1. Imports
import json
from pathlib import Path

# 2. Constantes
FICHIER_CONFIG = Path("config.json")

# 3. Fonctions
def charger_config():
    ...

# 4. Point d'entree
if __name__ == "__main__":
    config = charger_config()
```

## Regles de style (PEP 8)

- 4 espaces pour l'indentation (pas de tabulations).
- Lignes de 79 caracteres max (tolerance a 100).
- Deux lignes vides entre les fonctions de premier niveau.
- Un espace autour des operateurs : `x = 5`, pas `x=5`.

> **Astuce DanielCraft** - Installe un linter (flake8 ou ruff) pour reperer les problemes automatiquement.

## Documenter

```python
def calculer_ttc(prix_ht, tva=0.20):
    """Calcule le prix TTC a partir du HT et du taux de TVA."""
    return prix_ht * (1 + tva)
```

Les docstrings expliquent le "pourquoi", pas le "comment".

## Tester

```python
assert calculer_ttc(100) == 120.0
assert calculer_ttc(100, 0.055) == 105.5
```

Meme des tests simples avec `assert` detectent des regressions.

## A retenir

- Noms explicites en snake_case.
- PEP 8 pour le style.
- Docstrings pour les fonctions importantes.
- Tester meme simplement vaut mieux que ne pas tester.
