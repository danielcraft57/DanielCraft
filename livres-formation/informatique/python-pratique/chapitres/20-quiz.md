# Quiz final

Pas de piege. Relis une fois si besoin. L'idee : verifier que tu peux avancer sans paniquer.

## Questions

1. Pourquoi preferer `pathlib.Path` a une string de chemin colle a la main ?
- A) Parce que Path colorie le terminal
- B) Pour manipuler des chemins proprement (joindre, verifier, lire) sans galerer avec les slash
- C) Parce que CSV l'exige

2. Avec `csv.DictReader`, chaque ligne est surtout :
- A) Un entier
- B) Un dictionnaire dont les cles viennent de l'en-tete
- C) Une image

3. A quoi sert `argparse` ?
- A) A installer des paquets
- B) A definir et lire les arguments d'un script en ligne de commande
- C) A creer des pages web

4. Un environnement virtuel (`venv`), c'est surtout pour :
- A) Isoler les paquets d'un projet
- B) Remplacer Git
- C) Compiler le systeme

5. Quelle commande installe souvent les dependances listees ?
- A) `python -m pip install -r requirements.txt`
- B) `csv install requirements`
- C) `pathlib --install`

6. Dans `requests`, que fait souvent `reponse.json()` ?
- A) Ouvre Excel
- B) Parse le corps JSON en structures Python (dict/list)
- C) Cree un venv

7. Pourquoi mettre un `timeout` sur un GET ?
- A) Pour colorier les logs
- B) Pour eviter d'attendre indefiniment si le reseau/serveur rame
- C) Parce que CSV l'impose

8. `raise_for_status()` sert surtout a :
- A) Ignorer les erreurs
- B) Lever une exception si le code HTTP indique une erreur (4xx/5xx)
- C) Formater une date

9. Ou stocker une cle API plutot que dans le code source ?
- A) Dans une variable d'environnement (idee .env hors Git)
- B) Dans le nom du fichier CSV
- C) Dans un commentaire `print`

10. Le niveau `logging.INFO` par rapport a `DEBUG` :
- A) Affiche en general moins de detail que DEBUG
- B) Remplace argparse
- C) Chiffre les secrets

11. `strftime` sert a :
- A) Installer pytest
- B) Formater une date/heure en chaine selon un motif
- C) Lire un CSV

12. Une bonne raison d'utiliser `re.search` :
- A) Remplacer pathlib pour lister des dossiers
- B) Chercher un motif dans un texte irregulier (ex: email approximatif)
- C) Activer le venv

## Corriges

1-B, 2-B, 3-B, 4-A, 5-A, 6-B, 7-B, 8-B, 9-A, 10-A, 11-B, 12-B.

Si tu as 9/12 ou plus : tu es pret pour de vrais petits outils. Sinon, relis les chapitres lies (chemins, CSV, CLI, reseau, secrets), sans dramatiser.
