# Chapitre 19 - Bonnes pratiques

Ce chapitre ne rajoute presque pas de syntaxe. Il solidifie des reflexes. Tu peux le relire de temps en temps, comme une checklist amicale.

## Fonctions courtes, noms clairs

`moyenne_eleve` dit ce qu'elle fait. `calc2` non. Une fonction qui lit un CSV, appelle le reseau, formate trois messages et ecrit un fichier... c'est trop. Decoupe. Chez DanielCraft, on prefere trois fonctions ennuyeuses a une fonction heros.

## Un seul role pour le point d'entree

`main` parse, appelle, affiche. La logique metier vit ailleurs. Benefice : tests plus simples, CLI plus mince.

## Echecs previsibles

Fichier absent, JSON inattendu, reseau down : tu les as deja vus. Traite-les tot. Messages en francais simple. Details techniques dans les logs. Code retour non zero (`sys.exit(1)`) quand le script est utilise dans une chaine d'outils.

## UTF-8 et chemins

Toujours `encoding="utf-8"` pour le texte francais. Preferer `pathlib`. Eviter les chemins absolus graves dans le code (`C:\Users\...`) : passe-les en argument ou relative au projet.

## Dependances sous controle

Venv. `requirements.txt`. `python -m pip`. Pas de "j'ai installe globalement, tant pis". Moins de mysteres entre machines.

## Secrets

Variables d'environnement. `.env` ignore par Git. `.env.example` partageable. Jamais de jeton dans un screenshot de cours ni dans un log.

## Peu de magie

Les regex, les one-liners cryptiques, les imports circulaires : souvent impressifs, rarement gentils pour le futur toi. Clairete > densite.

## Documenter le "pourquoi" utile

Un README court. Une docstring sur une fonction non evidente. Pas besoin de commenter `i += 1`. Commente l'intention quand le code seul ne suffit pas : "Open-Meteo renvoie la temp en C sous current_weather".

## Versionne tes donnees d'exemple

Un petit `data/notes.exemple.csv` aide. Evite de casser le CSV "reel" a chaque test. Copie, travaille, compare.

## Petit, mais relancable

Un bon script se relance demain sans que tu te souviennes de tous les details. L'aide `-h`, le README, et des exemples d'appel dans un commentaire en haut du fichier aident enormement. Ecris pour ton futur toi fatigue.

## Eviter la perfection prematuree

Pas besoin de microservices pour un CSV de notes. Pas besoin de dix fichiers pour trente lignes. Organise assez pour rester lisible. Si tu passes plus de temps a "architecturer" qu'a faire marcher le cas nominal, simplifie.

## Petite checklist avant de partager

Est-ce que `-h` est clair ? Est-ce qu'un fichier manquant est explique ? Est-ce que le venv est documente ? Est-ce qu'un secret traine ? Est-ce qu'un test minimal existe pour le coeur du calcul ? Si oui, ton script merite d'etre montre.

## En vrai

Relis ton mini-projet avec cette checklist. Corrige deux choses seulement, mais pour de vrai. Les bonnes pratiques arrivent par couches, pas par sermon.

## A toi

Choisis une habitude (timeout, venv, ou secrets) et applique-la systematiquement a tous tes scripts cette semaine. Une habitude ancree vaut mieux que dix intentions.
