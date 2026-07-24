# Chapitre 7 - Erreurs HTTP : status, timeout, try/except

Appeler le reseau, c'est accepter que ca casse. Pas de wifi. Serveur en panne. URL fausse. Reponse trop lente. JSON inattendu. Un script "pratique" gere ca sans afficher une page de traceback a l'utilisateur.

Chez DanielCraft, regle d'or : echec possible = message clair + details techniques a part (log ou console).

## status_code et raise_for_status

```python
import requests

reponse = requests.get(url, timeout=10)
print(reponse.status_code)

if reponse.status_code != 200:
    print("Echec HTTP :", reponse.status_code)
else:
    data = reponse.json()
```

Plus court, style requests :

```python
reponse = requests.get(url, timeout=10)
reponse.raise_for_status()  # leve une erreur si 4xx ou 5xx
data = reponse.json()
```

`raise_for_status()` transforme un 404 ou 500 en exception. Tu peux la capturer dans un `try/except`.

## Timeout

```python
try:
    reponse = requests.get(url, timeout=5)
    reponse.raise_for_status()
    data = reponse.json()
except requests.Timeout:
    print("Le serveur met trop de temps a repondre.")
except requests.HTTPError as e:
    print("Erreur HTTP :", e.response.status_code)
except requests.RequestException:
    print("Impossible de contacter le serveur.")
```

`RequestException` est la famille large (reseau, HTTP, etc.). Commencer large est OK pour un petit script. Affiner ensuite.

Tu peux aussi ecrire `timeout=(3, 10)` : 3 secondes pour connecter, 10 pour lire. Pour debuter, un seul nombre suffit.

## JSON pourri

Parfois le status est 200, mais le corps n'est pas du JSON, ou il manque une cle.

```python
try:
    data = reponse.json()
    temp = data["current_weather"]["temperature"]
except ValueError:
    print("La reponse n'est pas du JSON valide.")
except KeyError:
    print("JSON inattendu : cle manquante.")
```

Ne suppose pas que l'API est parfaite. Verifie ce dont tu as besoin.

## Pattern solide pour un mini outil

```python
def fetch_json(url, params=None):
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        return r.json()
    except requests.Timeout:
        raise RuntimeError("Delai depasse") from None
    except requests.RequestException as e:
        raise RuntimeError(f"Echec reseau : {e}") from None
```

Tu centralises. Le reste du programme appelle `fetch_json` et gere un message utilisateur. Moins de copier-coller.

## Erreur classique

Avaler toutes les exceptions avec `except:` vide (ou `except Exception: pass`). Tu caches le probleme au lieu de le comprendre. Autre classique : afficher le traceback brut a un utilisateur non technicien. Garde le detail pour toi (`print` debug ou logging au chapitre 9).

## En vrai

Appelle une URL volontairement fausse. Puis une URL lente avec un timeout tres court. Observe les exceptions. Branche des messages humains. Casse, puis reparer : c'est comme ca qu'on apprend le reseau.

## A toi

Reprends `temperature_paris()` (ou equivalent). Ajoute timeout, `raise_for_status`, et des messages clairs pour timeout / HTTP / JSON. Si les trois chemins d'echec sont propres, ce chapitre est reussi.
