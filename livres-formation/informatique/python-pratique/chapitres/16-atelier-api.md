# Chapitre 16 - Atelier : appel API meteo

Objectif : un script qui recupere la meteo actuelle via une **API** JSON publique, affiche un resume, et gere proprement les echecs reseau. Travaille dans un **venv** avec `requests`. Duree : 30 a 45 minutes.

Max check la meteo chaque matin avant les chantiers exterieurs. Lea veut un outil reutilisable, pas un copier-coller d'URL. Sam montre a ses eleves comment le reseau entre dans Python. Chez DanielCraft, un script API sans **timeout** ni gestion d'erreur, c'est un demo, pas un outil. Tu vas sentir la difference entre "ca a marche une fois" et "ca explique quand ca casse".

Tu lances `python meteo.py --lat 48.85 --lon 2.35`. Le script fait un GET avec params et timeout, verifie le statut, extrait la temperature, affiche une phrase claire. Si le reseau rale, message humain + log. Si une cle JSON manque, tu ne pretend pas que tout va bien. Meme schema que le CSV : lire, verifier, traiter, afficher, echouer proprement. Toi, tu actives le venv pour de vrai avant de lancer.

:::retenir
Teste un timeout tres court (0.001) des l'exercice 4. Si le message est propre, tu as gagne le reflexe "echec reseau".
:::

## Exercice 1 - Environnement (5 min)

Cree un dossier `atelier-api` et un venv. Installe `requests`. Ecris un `requirements.txt`. Active le venv avant chaque session. Si tu installes globalement "pour aller plus vite", tu te prepares une galere sur une autre machine.

## Exercice 2 - Appel de base (10 min)

Choisis une API simple (Open-Meteo convient : pas de cle pour un usage de base). Ecris `meteo.py` avec argparse : `--lat`, `--lon` (defauts Paris ok), eventuellement `--timeout`. Fais un GET avec `params` et `timeout`. Pas d'URL monstrueuse colle en dur sans params : les parametres se lisent mieux separes.

## Exercice 3 - Extraction et affichage (10 min)

Verifie le succes (`raise_for_status` ou test du status). Extrais temperature (et vent si dispo). Affiche une phrase claire du type "Temperature : 18 C, vent 12 km/h". `print` pour l'humain. `logging` pour le detail si tu veux pousser.

## Exercice 4 - Echecs propres (10 min)

Attrape timeout et erreurs reseau : message utilisateur + log. Un timeout tres court (ex: 0.001) doit produire un message propre, pas seulement un mur de traceback. Aucune cle en dur dans le fichier (meme si l'API n'en demande pas : prends le reflexe). Lea teste toujours le chemin malheureux avant de montrer un outil a un client.

## Exercice 5 - Variable d'environnement (5 min)

Ajoute une variable d'environnement optionnelle `METEO_TIMEOUT` pour surcharger le timeout si presente. Documente-la dans un `.env.example`. Meme sans vrai secret ici, tu ancrages l'habitude "config dehors".

## Squelette d'extraction

```python
data = reponse.json()
meteo = data["current_weather"]
temp = meteo["temperature"]
print(f"Temperature : {temp} C")
```

Adapte les cles si tu changes d'API. L'important est le parcours, pas la marque du service. Protege les `KeyError` : un 200 ne garantit pas la forme que tu aimes.

## Petite histoire

Max a lance son script sur le parking avant une toiture. Timeout court, message clair, il a regarde le ciel et decide. Lea a ajoute `--brut` pour debug quand Open-Meteo a change une cle. Sam a fait planter le timeout volontairement en classe : les eleves ont vu qu'un echec propre fait partie du metier. Chez DanielCraft, on repete : le chemin malheureux compte autant que le chemin heureux.

## Livrable

Un dossier `atelier-api/` avec `meteo.py`, `requirements.txt`, `.env.example`, et une note de trois tests (appel normal, timeout court, lat/lon differentes).

## Criteres de reussite

`python meteo.py -h` est lisible. Un appel normal affiche temperature (et unite). Un timeout tres court produit un message propre. Aucune cle en dur.

## Bonus

Mode `--brut` qui affiche le JSON indente (`json.dumps(data, indent=2)`) pour debug. Ou ecriture d'une ligne dans `data/historique.csv` avec date + temperature (`datetime` + `csv`). Tu relies alors trois chapitres en un geste.

## Erreur classique

Oublier que la structure JSON peut changer. Protege les `KeyError`. Ne suppose pas que "200" implique les cles que tu aimes. Oublier le timeout. Installer `requests` hors venv et ne plus savoir recreer l'environnement. Autre piege : coller une cle API "temporaire" dans le fichier alors que tu n'en as meme pas besoin ici.

:::attention
Status 200 ne garantit pas les cles que tu attends. Protege les `KeyError`. Et mets toujours un timeout.
:::

## En vrai

Lance le script pour deux paires lat/lon differentes. Compare. Puis force un timeout absurde. Si les trois comportements sont clairs, tu as un outil, pas un brouillon.

## A toi

Si tu sens que c'est devenu un outil (et plus un exercice), ecris en trois lignes : comment tu l'appelles le matin, ce que tu fais si ca rate, ou vit le timeout. Garde ce papier a cote du mini-projet. Relance le script demain sans rouvrir le chapitre : si tu retrouves l'appel et le message d'echec, l'atelier a tenu.

Quand tu bloques sur une cle JSON, affiche d'abord `list(data.keys())` (ou le mode `--brut`) avant de chercher au hasard. Lea fait ca systematiquement. Max aussi, depuis qu'il a passe vingt minutes a chercher `temp` au lieu de `temperature`. Sam montre ce geste en classe : "interroge le JSON avant de l'inventer". Chez DanielCraft, ce reflexe evite plus de paniques que n'importe quel tutoriel d'API.

:::astuce
GET, timeout, raise_for_status, message humain, secrets dehors. Un atelier API propre, c'est ca.
:::
