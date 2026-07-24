# Chapitre 1 - Rappel rapide et carte du livre

Tu as deja fait les bases. Variables, conditions, boucles, fonctions, listes, dictionnaires, fichiers texte, JSON, modules, exceptions, et meme un peu de classes. Si un detail est flou, ce n'est pas grave : on ne va pas tout refaire. Ce livre part du moment ou Python devient un outil du quotidien.

Chez DanielCraft, on aime bien une image simple. Les bases, c'etait apprendre a conduire sur un parking. La pratique, c'est prendre la route : ouvrir un fichier CSV, lancer un script avec des arguments, appeler une API, isoler ses paquets, et laisser des traces utiles quand ca casse.

## Ce que tu gardes en tete

Tu sais ecrire une fonction. Tu sais boucler sur une liste. Tu sais ouvrir un fichier texte et lire du JSON. Tu as vu `try/except`. C'est assez pour avancer.

On ne revient pas sur `print`, `if`, `for`, ni sur "c'est quoi un dictionnaire". Si tu bloques sur ces mots, relis le premier livre Python. Ici, on monte d'un cran : des outils standards pour de vrais petits scripts.

## La carte du livre

Imagine que tu veux un script qui lit des notes dans un tableau, ou qui demande la meteo a une API, ou qui se lance depuis le terminal avec des options. Pour que ca marche vraiment, tu as besoin de plusieurs pieces.

D'abord `pathlib` : des chemins de fichiers sans te battre avec les slash. Ensuite le module `csv` : lire et ecrire des tableaux. Puis `argparse` : transformer ton fichier en vrai petit programme en ligne de commande. Un environnement virtuel (`venv`) et `pip` pour installer des paquets sans polluer le reste. `requests` pour appeler une API JSON. Les erreurs HTTP, les variables d'environnement, le `logging`, les dates avec `datetime`, et un peu de regex pour chercher des motifs dans du texte.

Plus tard : un mini-projet qui assemble tout ca, des ateliers concrets, des tests simples, une facon d'organiser un dossier, et des bonnes habitudes. Le quiz verifie. Le dernier chapitre, c'est pour souffler.

## Un fil rouge

On va souvent parler de trois exemples. Un fichier de notes (eleve, matiere, note) en CSV. Une meteo qui arrive en JSON depuis une API. Un script CLI que tu lances dans le terminal avec des arguments. Ces exemples reviennent, pour que tu sentes le progres.

Tu verras le meme geste sous plusieurs angles : lire des donnees, les resumer, gerer l'echec, rendre le script utilisable par quelqu'un d'autre (toi demain matin compte).

## Ce dont tu as besoin

Python 3 installe. Un editeur (VS Code, Cursor, ou autre). Un terminal. Pour la partie API : une connexion internet et un venv. Rien de plus pour suivre. Les paquets hors standard seront installes au fur et a mesure (`requests`, plus tard eventuellement `pytest`).

## Comment lire ce livre

Lis dans l'ordre au debut. Chemins, CSV, CLI, venv, requests : ca s'enchaine. Ensuite erreurs, secrets, logs, dates, regex. Le mini-projet colle les briques. Les ateliers sont la pour faire, pas seulement lire.

Tu n'as pas besoin d'un framework web. Django, Flask, FastAPI viendront plus tard si tu veux. Ici, on reste en Python "outil", clair, dans le terminal et les fichiers.

## Erreur classique

Croire que "je connais les bases" = "je sais automatiser mon quotidien". Les bases sont le moteur. La pratique, c'est la boite a outils : CSV, CLI, HTTP, logs. Sans ca, tu reecris tout a la main a chaque fois. Avec ca, tu gagnes du temps chaque semaine.

## En vrai

Ouvre un vieux script Python que tu as deja ecrit. Note ce qui manque pour le rendre utile : lire un tableau ? accepter un argument ? appeler une URL ? isoler les paquets ? Ce livre repond a ca.

## A toi

Ecris en trois phrases ce que tu veux construire a la fin. Pas un reseau social. Quelque chose de petit : "resumer mes notes depuis un CSV", "afficher la meteo de ma ville", "un script CLI qui dit bonjour avec mon nom". Garde ce but. On y reviendra.
