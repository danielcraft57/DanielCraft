# Chapitre 17 - Tests simples

Quand une fonction calcule une moyenne ou parse une date, tu veux pouvoir verifier sans relancer tout le CLI a la main. Les **tests**, c'est ca : des mini-verifications automatiques. Pas un luxe de grande entreprise. Un filet pour ton futur toi fatigue, qui modifiera une ligne et cassera un cas limite sans le voir.

On reste simple. D'abord `assert`. Ensuite l'idee de `pytest`. Pas besoin d'une usine. Separe le coeur (fonctions pures : entree -> sortie) du CLI (argparse, print, fichiers). Teste le coeur avec des donnees fictives en memoire. Le CLI, tu le testes manuellement ou plus tard avec des tests d'integration. Commence petit : trois asserts sur une fonction, c'est deja enorme.

Lea teste `moyenne_eleve` avec des dicts en memoire avant de brancher le CSV. Max verifie son extracteur JSON meteo avec un faux dict. Sam montre que trois asserts valent mieux qu'un relancement manuel a chaque modification. Chez DanielCraft, on dit : teste le coeur, pas le theatre du terminal.

## Ce que ce n'est pas

Tester, ce n'est pas ecrire plus de code que le programme lui-meme. Ce n'est pas non plus "couvrir 100% des lignes" des le jour un. Ce n'est pas une religion. Trois asserts utiles battent cinquante tests vides. Et ce n'est surtout pas une excuse pour ne plus jamais lancer le script a la main : les tests etent le coeur, tes doigts verifient le CLI.

:::retenir
Fonction pure + asserts = filet. CLI a part. Reseau fictif d'abord, vrai reseau ensuite.
:::

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

Si un `assert` echoue, Python leve `AssertionError` et s'arrete. Si tout passe, tu vois "Tests OK". Pour de petites fonctions pures (entree -> sortie, sans reseau), c'est deja enorme. Max a commence comme ca, sans installer quoi que ce soit. Sam aussi, en classe, sans wifi.

## Separer le coeur du CLI

Le piege : tout coller dans `main` avec argparse. Difficile a tester. Mieux :

```python
def moyenne_eleve(lignes, nom):
    notes = [float(l["note"]) for l in lignes if l["eleve"] == nom]
    if not notes:
        return None
    return sum(notes) / len(notes)
```

Tu testes `moyenne_eleve` avec une liste de dicts en memoire. Pas besoin de fichier. Le CLI, lui, lit le CSV puis appelle la fonction. Lea a decouvert ce decoupage en voulant tester sans toucher au vrai CSV client. Depuis, elle ne revient plus en arriere.

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

Tu n'es pas oblige d'installer pytest aujourd'hui. Comprends surtout : fonctions testables + verifications automatiques. L'outil suit l'habitude, pas l'inverse.

## Quoi tester en priorite ?

Les calculs. Les parsers (date, validation regex legere). Les branches "vide / absent". Moins urgent au debut : tout le reseau (ca demande des mocks). Pour l'API, tu peux tester une fonction qui extrait la temperature d'un dict JSON fictif.

```python
def temperature_depuis(data):
    return float(data["current_weather"]["temperature"])

assert temperature_depuis({"current_weather": {"temperature": 18.2}}) == 18.2
```

:::astuce
Fais echouer un assert volontairement une fois. Lis le message. Puis reparer. Tu retiendras mieux qu'avec une lecture passive.
:::

## Petite histoire

Sam a modifie son calcul de moyenne et a casse le cas "eleve absent" sans s'en rendre compte. Lea lui a fait ecrire trois asserts en cinq minutes. Desormais, Sam lance `checks.py` avant chaque session de notes. Un assert rouge vaut dix relancements manuels.

Max a casse son extracteur meteo en "simplifiant" une cle JSON. Son assert a crie. Il a sourit : mieux vaut un assert rouge qu'un mail client avec `KeyError`. Chez DanielCraft, on collectionne ces petites peurs evitees.

## Erreur classique

Tester uniquement le chemin heureux. Ajoute le cas vide, le cas absent, une note non numerique si tu la geres. Autre classique : asserts sur le texte exact d'un message utilisateur qui change souvent - prefere tester la valeur de retour. Autre piege : tester le reseau directement (lent, fragile) au lieu de tester l'extraction sur un dict fictif.

## Fichier checks.py minimal

Tu peux regrouper tes verifications dans un fichier lancable :

```python
# checks.py
from notes_lib import moyenne_eleve

lignes = [{"eleve": "Alice", "note": "10"}, {"eleve": "Alice", "note": "20"}]
assert moyenne_eleve(lignes, "Alice") == 15
assert moyenne_eleve(lignes, "Bob") is None
print("Tous les checks OK")
```

Lance avec `python checks.py`. Zero dependance extra. Quand le projet grandit, migre vers pytest. L'important : le reflexe "je modifie une fonction, je relance les checks" avant de toucher au CLI ou au reseau.

## En vrai

Extrais une fonction pure de ton atelier CSV. Ecris 3 asserts. Fais-en echouer un volontairement pour voir le message, puis reparer. Note le temps : souvent moins de dix minutes. Ces dix minutes te sauveront des soirees.

## A toi

Si tu es a l'aise, installe pytest et deplace tes asserts dans `test_*.py`. Sinon, garde un fichier `checks.py` lanceable. L'habitude compte plus que l'outil. Bonus : ajoute le cas "note non numerique" si tu le geres dans ta fonction. Lea lance ses checks avant chaque livraison client. Max aussi, depuis un devis faux. Sam exige `checks.py` sur les projets eleves partages.

:::attention
Ne teste pas seulement le chemin heureux. Ajoute le cas vide, le cas absent, et un cas limite. C'est la que ca casse demain.
:::
