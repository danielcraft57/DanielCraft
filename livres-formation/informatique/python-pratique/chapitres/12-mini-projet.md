# Chapitre 12 - Mini-projet : CLI resume CSV ou API

On assemble. Objectif : un petit outil en ligne de commande qui, selon le mode, lit un **CSV** de notes ou appelle une **API** meteo, puis affiche un resume clair. Avec arguments, gestion d'erreurs, et un log discret. C'est le moment ou la theorie devient un outil sous le coude.

Tu n'as pas besoin que ce soit parfait. Il faut que les deux chemins marchent, et que l'echec soit humain. Un seul script, deux modes. Mode notes : tu passes un fichier CSV et un nom d'eleve, tu obtiens une moyenne. Mode meteo : tu passes des coordonnees (ou des defauts Paris), tu obtiens une temperature. Les deux modes partagent la meme structure : argparse, fonctions metier, print pour l'utilisateur, logging pour le detail.

C'est le moment ou Lea, Max et Sam retrouvent leurs trois fils rouges : notes CSV, meteo API, script **CLI**. Chez DanielCraft, c'est ce genre de petit outil qu'on garde parce qu'il sert vraiment.

:::retenir
Range ton fichier dans cet ordre : imports, fonctions metier, fonctions CLI, puis `main`. Tu te retrouves plus vite quand ca casse.
:::

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

Reutilise `pathlib` + `csv.DictReader`. Calcule la moyenne. Si aucune ligne : message clair. Si le fichier n'existe pas : "Fichier introuvable : ..." et un `logging.error`. Tu as deja ecrit ces gestes dans les chapitres CSV et CLI. Ici, tu les branches derriere `--mode notes`. Sam reconnait son atelier. Lea reconnait son export client. Max reconnait ses factures sous d'autres colonnes.

Idee de coeur (a adapter) :

```python
def moyenne_eleve(chemin, eleve):
    total = 0.0
    compte = 0
    with Path(chemin).open(encoding="utf-8", newline="") as f:
        for ligne in csv.DictReader(f):
            if ligne["eleve"] == eleve:
                total += float(ligne["note"])
                compte += 1
    if compte == 0:
        return None
    return total / compte
```

## Mode meteo (coeur)

`requests.get` avec timeout, `raise_for_status`, extraction de la temperature. En cas d'echec : "Impossible de recuperer la meteo." + log de l'exception. Meme discipline que l'atelier API : params separes, timeout explicite, message humain. Max lance ce mode le matin. Lea ajoute parfois `--brut` pour debug. Toi, tu verifies d'abord le chemin malheureux (timeout court) avant de dire "c'est fini".
## Qualite minimale

Pas de traceback brut comme seul resultat. Pas de secret en dur. Aide `-h` lisible. Noms de fonctions clairs (`commande_notes`, `moyenne_eleve`, `fetch_meteo`). Un resume en une ou deux lignes a l'ecran.

Exemple de sorties attendues :

```text
Moyenne de Alice : 15.0 (4 notes)
Il fait 18.2 C (lat=48.85, lon=2.35)
```

## Organisation minimale du fichier

Meme dans un seul `resume.py`, range dans cet ordre : imports, logging config dans `main`, fonctions metier (`moyenne_eleve`, `fetch_meteo`), fonctions CLI (`commande_notes`, `commande_meteo`), puis `main`. Tu te retrouves plus vite. Plus tard, tu pourras couper en plusieurs fichiers (chapitre organisation).

## Petite histoire

Sam avait lu tous les chapitres mais n'avait rien assemble. Lea lui a dit : "Fais le mini-projet ce week-end, meme moche." Sam l'a fait en deux heures. Lundi, il calculait les moyennes du trimestre en une commande. Max a ajoute le mode meteo pour son usage perso. Deux modes, un script, zero copier-coller.

Lea a garde ce squelette comme modele pour ses outils clients. Chez DanielCraft, on dit souvent : un mini-projet fini bat dix chapitres survoles.

## Variante

Ajoute `--seuil` en mode notes pour lister les notes au-dessus du seuil. Ou `--json` pour afficher un mini objet JSON au lieu d'une phrase. Bonus, pas obligatoire.

## Criteres "c'est fini"

Tu peux expliquer en trente secondes comment lancer les deux modes. Un ami peut lire `-h` et comprendre. Tu as casse au moins deux choses volontairement (mauvais fichier, mauvais reseau) et les messages tenaient la route. Le code n'a pas de cle en dur.

:::attention
Casse volontairement le CSV et le reseau avant de dire "c'est fini". Les chemins malheureux comptent autant que le chemin heureux.
:::

## A toi

Code les deux modes. Casse volontairement le chemin CSV. Casse l'URL ou coupe le reseau. Verifie les messages. Remets tout. Si les chemins heureux et malheureux sont propres, le mini-projet est reussi.

:::astuce
Deux modes, un CLI, messages humains, secrets dehors. Assemble, casse, reparer : c'est le vrai test.
:::
