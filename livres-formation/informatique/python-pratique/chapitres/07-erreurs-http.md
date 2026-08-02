# Chapitre 7 - Erreurs HTTP : status, timeout, try/except

Appeler le reseau, c'est accepter que ca casse. Pas de wifi. Serveur en panne. URL fausse. Reponse trop lente. JSON inattendu. Un script "pratique" gere ca sans afficher une page de traceback a l'utilisateur. C'est la difference entre un demo et un **outil**.

Chaque appel reseau a trois sorties possibles : succes (200 + JSON ok), echec **HTTP** (404, 500...), echec reseau (**timeout**, pas de connexion). Ton script doit traiter les trois sans paniquer. L'utilisateur voit une phrase humaine. Toi, tu as le detail pour deboguer. Deux canaux, une meme honnetete.

Chez DanielCraft, regle d'or : echec possible = message clair + details techniques a part (log ou console). Lea affiche "Impossible de charger les donnees" a son client et garde le detail HTTP dans un log. Max voit "Serveur trop lent" au lieu d'un mur d'erreur. Sam montre a ses eleves que le reseau, ca casse, et que Python sait le gerer proprement.

:::attention
N'avale jamais toutes les exceptions avec `except: pass`. Tu caches le probleme. Message clair + detail a part, pas le silence.
:::

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

:::astuce
Centralise le fetch dans une fonction. Le CLI n'a qu'a afficher "Impossible de..." et logger le detail. Moins de doublons, plus de clarte.
:::

## Petite histoire

Lea a deploye un script meteo chez un client sans gestion d'erreur. Un jour, l'API a renvoye un 503 pendant dix minutes. Le client a recu une page de traceback Python par email. Lea a ajoute timeout, `raise_for_status`, et des messages clairs le soir meme. Depuis, les echecs reseau sont visibles mais propres. C'est ca la maturite d'un script pratique.

Max a teste avec un timeout de 0.001 seconde juste pour voir. Message propre. Sam le fait faire en classe : "casse, puis reparer". Le reflexe rentre.

## Erreur classique

Avaler toutes les exceptions avec `except:` vide (ou `except Exception: pass`). Tu caches le probleme au lieu de le comprendre. Autre classique : afficher le traceback brut a un utilisateur non technicien. Garde le detail pour toi (`print` debug ou logging au chapitre 9). Autre piege : oublier le timeout et bloquer un script automatise pendant des heures.

## En vrai

Appelle une URL volontairement fausse. Puis une URL lente avec un timeout tres court. Observe les exceptions. Branche des messages humains. Casse, puis reparer : c'est comme ca qu'on apprend le reseau. Note sur papier les trois messages que tu affiches. S'ils sont clairs pour Max non technicien, tu as gagne.

## A toi

Reprends `temperature_paris()` (ou equivalent). Ajoute timeout, `raise_for_status`, et des messages clairs pour timeout / HTTP / JSON. Si les trois chemins d'echec sont propres, ce chapitre est reussi. Bonus : centralise dans `fetch_json` et reutilise. Max teste souvent avec `timeout=0.001` juste pour voir le message. Toi aussi : casse volontairement avant de dire "c'est solide".

## Zoom : deux canaux

L'utilisateur lit une phrase. Toi, tu lis un log. Si tu melanges les deux, tu noies le client ou tu te prives de details. Lea affiche "Impossible de charger les donnees" et loggue le status. Sam oblige les eleves a ecrire les deux phrases avant de coder. Chez DanielCraft, c'est la signature d'un outil adulte.

:::retenir
Succes, echec HTTP, echec reseau : trois sorties, messages humains, details a part.
:::
