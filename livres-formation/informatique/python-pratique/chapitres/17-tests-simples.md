# Chapitre 17 - Tests simples

Quand une fonction calcule une moyenne ou parse une date, tu veux pouvoir verifier sans relancer tout le CLI a la main. Les tests, c'est ca : des mini-verifications automatiques.

On reste simple. D'abord `assert`. Ensuite l'idee de `pytest`. Pas besoin d'une usine.

## assert : la base

```python
def moyenne(valeurs):
    if not valeurs:
        return None
    return sum(valeurs) / len(valeurs)

assert moyenne([10, 20]) == 15
assert moyenne([]) is None
print("Tests OK")
```

Si un `assert` echoue, Python leve `AssertionError` et s'arrete. Si tout passe, tu vois "Tests OK". Pour de petites fonctions pures (entree -> sortie, sans reseau), c'est deja enorme.

## Separer le coeur du CLI

Le piege : tout coller dans `main` avec argparse. Difficile a tester. Mieux :

```python
def moyenne_eleve(lignes, nom):
    notes = [float(l["note"]) for l in lignes if l["eleve"] == nom]
    if not notes:
        return None
    return sum(notes) / len(notes)
```

Tu testes `moyenne_eleve` avec une liste de dicts en memoire. Pas besoin de fichier. Le CLI, lui, lit le CSV puis appelle la fonction.

## L'idee pytest

`pytest` est un outil populaire. Tu installes dans le venv : `pip install pytest`. Tu ecris un fichier `test_moyenne.py` :

```python
from resume import moyenne_eleve

def test_moyenne_simple():
    lignes = [
        {"eleve": "Alice", "note": "10"},
        {"eleve": "Alice", "note": "20"},
    ]
    assert moyenne_eleve(lignes, "Alice") == 15

def test_eleve_absent():
    assert moyenne_eleve([], "Bob") is None
```

Puis tu lances :

```text
pytest
```

pytest trouve les fonctions `test_...`, les execute, et resume les succes/echec. Plus confortable que des assert disperses quand le projet grandit.

Tu n'es pas oblige d'installer pytest aujourd'hui. Comprends surtout : fonctions testables + verifications automatiques.

## Quoi tester en priorite ?

Les calculs. Les parsers (date, validation regex legere). Les branches "vide / absent". Moins urgent au debut : tout le reseau (ca demande des mocks). Pour l'API, tu peux tester une fonction qui extrait la temperature d'un dict JSON fictif.

```python
def temperature_depuis(data):
    return float(data["current_weather"]["temperature"])

assert temperature_depuis({"current_weather": {"temperature": 18.2}}) == 18.2
```

## Erreur classique

Tester uniquement le chemin heureux. Ajoute le cas vide, le cas absent, une note non numerique si tu la geres. Autre classique : asserts sur le texte exact d'un message utilisateur qui change souvent - prefere tester la valeur de retour.

## En vrai

Extrais une fonction pure de ton atelier CSV. Ecris 3 asserts. Fais-en echouer un volontairement pour voir le message, puis reparer.

## A toi

Si tu es a l'aise, installe pytest et deplace tes asserts dans `test_*.py`. Sinon, garde un fichier `checks.py` lanceable. L'habitude compte plus que l'outil.
