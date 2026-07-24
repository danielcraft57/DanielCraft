# Chapitre 6 - requests GET : appeler une API JSON

Jusqu'ici, tes donnees vivaient dans des fichiers. Maintenant, ton script peut demander des infos ailleurs : une API meteo, un service public, un endpoint de demo.

`requests` est une bibliotheque tres utilisee pour ca. En mode GET, tu dis : "donne-moi cette ressource". Chez DanielCraft, on resume : demander, lire, utiliser.

## Installer (rappel)

Dans ton venv :

```text
python -m pip install requests
```

## Premier appel

```python
import requests

url = "https://httpbin.org/json"
reponse = requests.get(url, timeout=10)
print(reponse.status_code)
data = reponse.json()
print(data)
```

Que se passe-t-il ? `requests.get` part chercher l'URL. Tu recois un objet reponse. `status_code` est le code HTTP (200 = OK en general). `.json()` parse le corps si c'est du JSON, et te donne un dict ou une liste Python.

Le `timeout=10` evite d'attendre eternellelement si le reseau rame. On en reparlera au chapitre erreurs. Prends l'habitude de le mettre des maintenant.

## Meteo : exemple mental

Beaucoup d'API meteo renvoient un JSON du genre :

```text
{ "ville": "Paris", "temp": 18.2, "ciel": "nuageux" }
```

Ton script fait un GET sur une URL avec la ville en parametre, lit le JSON, puis affiche une phrase. Memes etapes partout. Seules les cles changent.

Avec Open-Meteo (API publique, sans cle pour un usage simple), l'idee ressemble a :

```python
import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 48.85,
    "longitude": 2.35,
    "current_weather": "true",
}
reponse = requests.get(url, params=params, timeout=10)
data = reponse.json()
meteo = data["current_weather"]
print("Temperature :", meteo["temperature"])
```

`params` ajoute les parametres a l'URL proprement (encodage inclus). Tu n'as pas a coller `?latitude=...` a la main.

## Afficher un resume

```python
temp = meteo["temperature"]
vent = meteo["windspeed"]
print(f"Il fait {temp} C, vent {vent}")
```

Tu vois le pattern de beaucoup d'outils CLI : appeler, extraire deux-trois champs, afficher clairement. Pas besoin d'une interface graphique pour etre utile.

## Headers (idee rapide)

Parfois une API demande un en-tete (type de contenu, jeton...). Avec requests :

```python
headers = {"Accept": "application/json"}
reponse = requests.get(url, headers=headers, timeout=10)
```

On gardera les secrets (jetons) pour le chapitre variables d'environnement. Ne colle jamais une cle API en dur dans un fichier que tu partages.

## Erreur classique

Oublier `.json()` et manipuler `reponse.text` en croyant que c'est deja un dict. Ou appeler sans timeout. Ou croire que "pas d'exception" signifie "tout va bien" : un 404 ne leve pas toujours une exception avec requests (selon comment tu codes). Le prochain chapitre traite ca.

## En vrai

Dans ton venv, appelle une URL JSON publique (httpbin, open-meteo, ou autre dispo chez toi). Affiche le `status_code` et deux cles du JSON. Le but : voir de vraies donnees arriver dans ton terminal.

## A toi

Ecris une fonction `temperature_paris()` qui retourne la temperature actuelle (float), ou leve une erreur claire si le JSON n'a pas la forme attendue. On solidifiera les erreurs juste apres.
