# Quiz final

Pas de piege. Relis une fois si besoin. L'idee : verifier que tu peux avancer sans paniquer. Chez DanielCraft, on considere qu'un quiz reussi, c'est surtout la preuve que tu peux relancer un script demain sans relire vingt pages. Lea note ses trous. Max refait un atelier. Sam utilise ce QCM en fin de module. Toi, tu coches sans tricher. Ensuite seulement, tu compares.

Une premiere passe honnete vaut mieux qu'un score maquille. Si une question te bloque, marque-la et continue. Tu reviendras. Le but n'est pas la perfection du jour. Le but, c'est la carte des chapitres a rouvrir.

:::retenir
Fais le quiz, note ton score, rejoue dans une semaine. Le vrai progres se voit a la deuxieme passe.
:::

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
- A) Dans une variable d'environnement (`.env` hors Git)
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

Si tu as 9/12 ou plus : tu es pret pour de vrais petits outils. Sinon, relis les chapitres lies (chemins, CSV, CLI, reseau, secrets), sans dramatiser. Un 7/12 honnete avec une carte de reprise bat un 12/12 maquille qu'on oublie demain.

:::attention
Ne triche pas sur le score pour te rassurer. Note les trous. Le vrai progres se voit a la deuxieme passe, pas au premier coches.
:::

## Petite histoire

Lea a rate la question timeout. Elle a rit, puis a ajoute `timeout=10` partout dans ses scripts clients le soir meme. Max a confondu `strftime` et `strptime` : il a rejoue l'atelier dates dix minutes. Sam affiche le score moyen sans nommer personne : "on revoit secrets et venv demain". Trois reactions, meme message : le quiz est une carte, pas un jugement. Chez DanielCraft, on aime ces cartes.

## Questions bonus (auto-eval)

13. Cite trois gestes pour un script reseau robuste. 14. Difference entre `print` et `logging` dans un CLI. 15. Pourquoi `Path(__file__).parent` plutot qu'un chemin relatif au dossier courant. Reponses libres : compare a tes chapitres 2, 7, 9.

## En vrai

Coche tes mauvaises reponses. Ouvre le chapitre lie. Refais un mini geste de cinq minutes : un GET avec timeout, un Path, un assert. Pas besoin de tout relire. Un trou a la fois.

## A toi

Ecris tes trois questions ratees (ou les plus floues). A cote, une phrase "ce que je confonds". Dans sept jours, rejoue seulement ces trois. Le vrai score, c'est la deuxieme passe.

## Pour aller plus loin sans te perdre

Tu n'as pas a tout maitriser d'un coup. Reviens a ce chapitre quand tu butes sur un cas reel. Relis l'erreur classique du chapitre concerne. Refais le "A toi". Chez DanielCraft, on prefere trois relectures actives a une lecture passive de vingt pages. Si un paragraphe te semble encore flou, reformule-le a voix haute avec ton propre exemple. Des que ca passe a l'oral, c'est que c'est entre.

Si tu as rate timeout ou secrets, ne te flagelle pas. Rouvre le chapitre 7 ou 8 dix minutes, refais un geste concret, puis rejoue ces deux questions seules. Lea a fait exactement ca. Max aussi. Le score du jour compte moins que la reprise dans sept jours. Chez DanielCraft, on garde ce quiz comme carte de poche, pas comme jugement.

:::astuce
Trois relectures actives battent une lecture passive de vingt pages. Un trou a la fois, un geste de cinq minutes.
:::
