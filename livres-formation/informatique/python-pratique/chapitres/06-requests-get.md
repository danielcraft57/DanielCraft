# Chapitre 6 - requests GET : appeler une API JSON

Jusqu'ici, tes donnees vivaient dans des fichiers. Maintenant, ton script peut demander des infos ailleurs : une **API** meteo, un service public, un endpoint de demo. Le reseau entre dans ton quotidien Python. C'est un cran de plus : plus seulement "lire un CSV", mais "demander a un serveur et utiliser la reponse".

`requests` est une bibliotheque tres utilisee pour ca. En mode **GET**, tu dis : "donne-moi cette ressource". Une API, c'est un serveur qui repond a des questions via HTTP. Tu envoies une URL (avec parfois des parametres). Tu recois un code status (200 = OK en general) et un corps (souvent du JSON). Ton script extrait ce dont il a besoin et affiche un resume. Pas besoin d'interface graphique pour etre utile. Une phrase dans le terminal, le matin, ca suffit.

Chez DanielCraft, on resume : demander, lire, utiliser. Max check la meteo avant un chantier exterieur. Lea recupere des donnees publiques pour un dashboard client. Sam montre a ses eleves comment une URL renvoie du **JSON** lisible par Python.

:::retenir
Garde le pattern en tete : GET -> status -> `.json()` -> extraire deux-trois champs -> afficher clair.
:::

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

Le `timeout=10` evite d'attendre indefiniment si le reseau rame. On en reparlera au chapitre erreurs. Prends l'habitude de le mettre des maintenant.

## Meteo : exemple concret

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

Tu vois le pattern de beaucoup d'outils CLI : appeler, extraire deux-trois champs, afficher clairement.

## Headers (rapide)

Parfois une API demande un en-tete (type de contenu, jeton...). Avec requests :

```python
headers = {"Accept": "application/json"}
reponse = requests.get(url, headers=headers, timeout=10)
```

On gardera les secrets (jetons) pour le chapitre variables d'environnement. Ne colle jamais une cle API en dur dans un fichier que tu partages.

:::attention
Pas de timeout = script qui peut attendre indefiniment. Mets `timeout=` des le premier GET. Toujours.
:::

## Petite histoire

Max ouvrait trois onglets meteo chaque matin avant de partir en toiture. Lea lui a montre un script de quinze lignes avec Open-Meteo. Un lancement, une phrase : "Il fait 12 C, vent 25". Max l'utilise encore. Ce n'est pas revolutionnaire. C'est juste un outil qui reste sous le coude parce qu'il sert vraiment.

Sam a fait la demo en cours : URL, JSON, temperature. Les eleves ont vu "le reseau" devenir quelque chose de concret, pas un nuage abstrait. Chez DanielCraft, c'est le genre de demo qui ancre.

## Erreur classique

Oublier `.json()` et manipuler `reponse.text` en croyant que c'est deja un dict. Ou appeler sans timeout. Ou croire que "pas d'exception" signifie "tout va bien" : un 404 ne leve pas toujours une exception avec requests (selon comment tu codes). Le prochain chapitre traite ca.

## En vrai

Dans ton venv, appelle une URL JSON publique (httpbin, open-meteo, ou autre dispo chez toi). Affiche le `status_code` et deux cles du JSON. Le but : voir de vraies donnees arriver dans ton terminal. Si ca rame, baisse le timeout et observe. Si ca marche, souris : ton script parle au monde.

## A toi

Ecris une fonction `temperature_paris()` qui retourne la temperature actuelle (float), ou leve une erreur claire si le JSON n'a pas la forme attendue. On solidifiera les erreurs juste apres. Bonus : affiche aussi le vent dans une phrase complete, style Max le matin. Garde le timeout des maintenant, meme si le chapitre erreurs vient juste apres : le reflexe se construit tot.

## Zoom : API = contrat

Une API, c'est un contrat. Tu demandes une forme. Tu recois une forme. Si la forme change, ton script casse. Lea lit toujours un exemple de JSON avant de coder. Sam projette le JSON au tableau. Max regarde deux cles seulement et ignore le reste. Chez DanielCraft, on extrait peu, clairement, plutot que de tout imprimer "pour voir" en production.

:::astuce
GET + timeout + `.json()` + extraire clairement. Le reseau devient un outil, pas un mystere.
:::
