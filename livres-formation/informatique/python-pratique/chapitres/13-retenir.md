# Chapitre 13 - Ce qu'il faut retenir

Tu as grimpe d'un cran. Voici la carte en version poche.

## En une minute

`pathlib` : chemins en objets, `/` pour assembler, `read_text` / `write_text`. `csv` : `DictReader` / `DictWriter` pour les tableaux. `argparse` : options CLI et aide `-h`. `venv` + `pip` : isoler les paquets, `requirements.txt`. `requests` : GET, `.json()`, `params`, `timeout`. Erreurs HTTP : `status_code`, `raise_for_status`, `try/except`. Secrets : `os.environ`, idee `.env`, jamais en clair dans le code. `logging` : niveaux et traces. `datetime` : formater, parser, `timedelta`. `re` : `search`, `fullmatch`, `findall` avec moderation.

## Habitudes solides

1. Un venv par projet
2. Toujours un timeout sur le reseau
3. Messages humains a l'ecran, details en log
4. Secrets hors du code source
5. CSV avec `newline=""` et `encoding="utf-8"`
6. Chemins ancrees avec `Path(__file__).parent` quand besoin
7. Un role clair par fonction

## Erreurs classiques

Installer un paquet dans le mauvais Python. Oublier que les cellules CSV sont des strings. Croire qu'un GET sans exception signifie succes. Coller une cle API dans le fichier. Ecrire une regex la ou un `Path.suffix` suffisait. Tout mettre dans un seul `main` de 200 lignes.

## Suite dans ce livre

Ateliers concrets (CSV, CLI, API), puis tests simples, organisation de projet, bonnes pratiques, quiz, bravo. Tu n'as pas besoin d'etre parfait. Tu as besoin d'etre capable de lire un tableau, lancer un script avec des options, et appeler une API sans paniquer.

## Mini defi

Sans regarder tes notes, ecris de memoire : ouvrir un CSV avec `DictReader`, et un `requests.get` avec timeout + `raise_for_status`. Compare ensuite. Les trous montrent ce qu'il faut relire.
