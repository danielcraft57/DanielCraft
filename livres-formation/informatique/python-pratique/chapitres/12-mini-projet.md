# Chapitre 12 - Mini-projet : CLI resume CSV ou API

On assemble. Objectif : un petit outil en ligne de commande qui, selon le mode, lit un CSV de notes ou appelle une API meteo, puis affiche un resume clair. Avec arguments, gestion d'erreurs, et un log discret.

Tu n'as pas besoin que ce soit parfait. Il faut que les deux chemins marchent, et que l'echec soit humain.

## Parcours

1. Cree un dossier de projet avec un venv et `requests` installe.
2. Place un `data/notes.csv` d'exemple.
3. Ecris `resume.py` avec argparse : `--mode notes|meteo`, et les options utiles.
4. Mode notes : `--fichier` + `--eleve` -> moyenne.
5. Mode meteo : latitude/longitude (ou ville fixe) -> temperature.
6. Erreurs : fichier manquant, eleve inconnu, HTTP rate, timeout.
7. `print` pour l'utilisateur, `logging` pour le detail.

## Squelette argparse

```python
import argparse
import logging

def build_parser():
    p = argparse.ArgumentParser(description="Resume notes CSV ou meteo API")
    p.add_argument("--mode", choices=["notes", "meteo"], required=True)
    p.add_argument("--fichier", help="CSV pour le mode notes")
    p.add_argument("--eleve", help="Nom de l'eleve")
    p.add_argument("--lat", type=float, default=48.85)
    p.add_argument("--lon", type=float, default=2.35)
    return p
```

Tu branches ensuite :

```python
def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
    args = build_parser().parse_args()
    if args.mode == "notes":
        commande_notes(args)
    else:
        commande_meteo(args)

if __name__ == "__main__":
    main()
```

Le `if __name__ == "__main__"` evite d'executer `main` si le fichier est importe. Habitude saine.

## Mode notes (coeur)

Reutilise `pathlib` + `csv.DictReader`. Calcule la moyenne. Si aucune ligne : message clair. Si le fichier n'existe pas : "Fichier introuvable : ..." et un `logging.error`.

## Mode meteo (coeur)

`requests.get` avec timeout, `raise_for_status`, extraction de la temperature. En cas d'echec : "Impossible de recuperer la meteo." + log de l'exception.

## Qualite minimale

Pas de traceback brut comme seul resultat. Pas de secret en dur. Aide `-h` lisible. Noms de fonctions clairs (`commande_notes`, `moyenne_eleve`, `fetch_meteo`). Un resume en une ou deux lignes a l'ecran.

Exemple de sorties attendues :

```text
Moyenne de Alice : 15.0 (4 notes)
Il fait 18.2 C (lat=48.85, lon=2.35)
```

## Organisation minimale du fichier

Meme dans un seul `resume.py`, range dans cet ordre : imports, logging config dans `main`, fonctions metier (`moyenne_eleve`, `fetch_meteo`), fonctions CLI (`commande_notes`, `commande_meteo`), puis `main`. Tu te retrouves plus vite. Plus tard, tu pourras couper en plusieurs fichiers (chapitre organisation).

## Variante

Ajoute `--seuil` en mode notes pour lister les notes au-dessus du seuil. Ou `--json` pour afficher un mini objet JSON au lieu d'une phrase. Bonus, pas obligatoire.

## Criteres "c'est fini"

Tu peux expliquer en trente secondes comment lancer les deux modes. Un ami peut lire `-h` et comprendre. Tu as casse au moins deux choses volontairement (mauvais fichier, mauvais reseau) et les messages tenaient la route. Le code n'a pas de cle en dur.

## A toi

Code les deux modes. Casse volontairement le chemin CSV. Casse l'URL ou coupe le reseau. Verifie les messages. Remets tout. Si les chemins heureux et malheureux sont propres, le mini-projet est reussi. Chez DanielCraft, c'est ce genre de petit outil qu'on garde sous le coude.
