# Chapitre 13 - A retenir (carte mentale)

Si tu ne devais garder qu'une page, ce serait celle-ci. Python pratique, ce n'est pas "savoir coder des exercices". C'est savoir lire un **tableau**, lancer un script avec des **options**, appeler une **API**, et ranger un petit projet sans paniquer. Tu pilotes. Python execute. Tu verifies. Tu assumes. Chez DanielCraft, on colle cette carte au-dessus de l'ecran quand un script devient flou. Relis-la avant les ateliers. Relis-la apres. Elle sert de boussole.

Tu n'as pas besoin de tout memoriser. Tu as besoin de reconnaitre les gestes et de savoir ou les retrouver. Lea resume en une phrase : "fichier ou API, message clair, secret dehors". Max dit : "venv, timeout, `-h`". Sam dit : "je peux relancer demain sans me souvenir de tout". Les trois ont raison. Choisis ta phrase. Garde-la.

Trois fils rouges sur une meme table. Un CSV de notes (Sam). Une meteo JSON (Max). Un script CLI avec `-h` (Lea). Autour : pathlib, logging, secrets, dates, regex avec moderation. Le mini-projet assemble. Les ateliers forcent le livrable. Les tests protegent le coeur. L'organisation evite le dossier "Nouveau dossier (3)". Tout le livre tient dans ces gestes.

## Ce que ce n'est pas

Ce chapitre n'est pas un glossaire de soixante mots. Ce n'est pas non plus un examen surprise. Ce n'est pas "la fin de Python". Et ce n'est surtout pas le moment de paniquer parce qu'un parametre argparse t'echappe. Les gestes comptent plus que le catalogue. Si tu peux ouvrir un CSV, lancer un CLI, faire un GET avec timeout, et isoler un venv, tu as le socle.

:::retenir
"Fichier ou API, message clair, secret dehors, venv isole." Cette phrase resume le livre mieux qu'un glossaire.
:::

## Les idees solides

`pathlib` : chemins en objets, `/` pour assembler, `read_text` / `write_text`, ancrer avec `Path(__file__).parent`. `csv` : `DictReader` / `DictWriter`, `newline=""`, `encoding="utf-8"`, tout est string jusqu'a conversion. `argparse` : options CLI, aide `-h`, `required=True` des le debut. `venv` + `pip` : un projet, un venv, `python -m pip install -r requirements.txt`. `requests` : GET, `.json()`, `params`, `timeout`, `raise_for_status`. Secrets : `os.environ`, `.env` hors Git, `.env.example` partageable. `logging` : niveaux, print pour l'utilisateur, log pour le detail. `datetime` : `strftime`, `strptime`, `timedelta`, comparer des objets pas des chaines. `re` : `search`, `fullmatch`, `findall` avec moderation.

Ce n'est pas une checklist a cocher en courant. C'est un paysage. Si un mot est flou, rouvre le chapitre concerne dix minutes. Une relecture active bat une lecture passive de quarante pages.

## La boucle DanielCraft

1) Lire ou appeler. 2) Verifier (fichier existe, HTTP ok, JSON attendu). 3) Traiter (calcul, filtre, resume). 4) Afficher clair (`print`). 5) Tracer le detail (`logging`). 6) Echouer proprement (message humain, pas traceback brut). 7) Ranger (venv, requirements, README).

C'est la meme boucle pour Lea sur un export client, pour Max sur la meteo du chantier, pour Sam sur les notes du trimestre. Les donnees changent. Le geste reste.

## Ce que tu peux oublier

La syntaxe exacte de chaque parametre argparse. Le nom de chaque exception requests. La peur du terminal. Garde les gestes. Change de paquet si besoin. Les gestes restent. Tu n'es pas un dictionnaire ambulant. Tu es un pilote qui sait ou chercher.

## Petite checklist de poche

Venv actif ? Timeout sur le reseau ? Secrets hors du code ? CSV avec `newline=""` ? Chemins ancrees si besoin ? `-h` lisible ? Un test minimal sur le coeur du calcul ? Si oui partout, tu es pret pour les ateliers.

:::astuce
Sans regarder tes notes, ecris de memoire : ouvrir un CSV avec DictReader, et un requests.get avec timeout + raise_for_status. Les trous montrent ce qu'il faut relire.
:::

## Petite histoire

Sam avait lu tous les chapitres. Le lundi des notes, il a bloque sur "par quel bout commencer". Lea lui a dit : "Relis la carte. Fais le CSV. Puis le CLI. Puis l'API." En deux soirees, le mini-projet etait la. Max a saute la carte, a melange secrets et chemins absolus, a perdu une heure. Il est revenu a cette page. Chez DanielCraft, on voit souvent cette scene : la carte poche vaut mieux que la memoire heroique.

## Erreur classique

Croire que "je connais les bases" egal "je sais automatiser mon quotidien". Les bases sont le moteur. La pratique, c'est la boite a outils. Autre piege : empiler pandas, Flask et Docker avant d'avoir un script CSV + CLI + timeout qui tient la route. Autre piege : lire cette carte sans refaire un "A toi" a voix haute.

:::attention
Sans livrable apres la carte, tu "comprends" et tu oublies. Ecris. Lance. Casse. Repare.
:::

## En vrai

Sans regarder le livre, ecris sur papier en dix lignes : pathlib, csv, argparse, venv, requests, secrets, logging. Compare ensuite. Les trous montrent ce qu'il faut relire avant les ateliers. Pas de honte. De la carte.

## A toi

Recopie cette carte sur papier en 10 lignes max, avec TES mots. Si tu peux l'expliquer a un ami sans regarder, c'est bon signe. Prends le temps. Un atelier fait a fond vaut mieux que trois ateliers survoles. Si tu es presse, fais la moitie aujourd'hui et l'autre demain - mais ecris le livrable. Sans livrable, le cerveau classe ca comme "lu", pas comme "su". DanielCraft forme des gens qui livrent, meme petit.
