# Chapitre 16 - Atelier : appel API meteo

Objectif : un script qui recupere la meteo actuelle via une API JSON publique, affiche un resume, et gere proprement les echecs reseau. Travaille dans un venv avec `requests`.

## Etapes

1. Cree un dossier `atelier-api` et un venv. Installe `requests`. Ecris un `requirements.txt`.
2. Choisis une API simple (Open-Meteo convient : pas de cle pour un usage de base).
3. Ecris `meteo.py` avec argparse : `--lat`, `--lon` (defauts Paris ok), eventuellement `--timeout`.
4. Fais un GET avec `params` et `timeout`.
5. Verifie le succes (`raise_for_status` ou test du status).
6. Extrais temperature (et vent si dispo). Affiche une phrase claire.
7. Attrape timeout et erreurs reseau : message utilisateur + log.
8. Ajoute une variable d'environnement optionnelle `METEO_TIMEOUT` pour surcharger le timeout si presente.

## Criteres de reussite

- `python meteo.py -h` est lisible.
- Un appel normal affiche temperature (et unite).
- Un timeout tres court (ex: 0.001) produit un message propre, pas seulement un mur de traceback.
- Aucune cle en dur dans le fichier (meme si l'API n'en demande pas : prends le reflexe).

## Squelette d'extraction

```python
data = reponse.json()
meteo = data["current_weather"]
temp = meteo["temperature"]
print(f"Temperature : {temp} C")
```

Adapte les cles si tu changes d'API. L'important est le parcours, pas la marque du service.

## Bonus

Mode `--brut` qui affiche le JSON indenté (`json.dumps(data, indent=2)`) pour debug. Ou ecriture d'une ligne dans `data/historique.csv` avec date + temperature (`datetime` + `csv`).

## Piege

Oublier que la structure JSON peut changer. Protege les `KeyError`. Ne suppose pas que "200" implique les cles que tu aimes.

## A toi

Lance le script pour deux paires lat/lon differentes. Compare. Si tu sens que c'est devenu un outil (et plus un brouillon), l'atelier est bon.
