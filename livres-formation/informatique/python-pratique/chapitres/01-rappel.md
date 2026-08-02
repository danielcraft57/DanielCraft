# Chapitre 1 - Rappel rapide et carte du livre

Tu as deja fait les bases. Variables, conditions, boucles, fonctions, listes, dictionnaires, fichiers texte, JSON, modules, exceptions, et meme un peu de classes. Si un detail est flou, ce n'est pas grave : on ne va pas tout refaire. Ce livre part du moment ou Python devient un outil du quotidien, pas un exercice de cours. Tu n'ecris plus pour "passer le TD". Tu ecris pour gagner du temps, chaque semaine, sur des taches reelles.

Chez DanielCraft, on aime bien une image simple. Les bases, c'etait apprendre a conduire sur un parking. La **pratique**, c'est prendre la route : ouvrir un fichier **CSV** de notes, lancer un script avec des arguments, appeler une **API** meteo, isoler tes paquets dans un **venv**, et laisser des traces utiles quand ca casse. Lea, freelance web, veut automatiser ses exports clients. Max, artisan, veut resumer ses factures sans Excel a minuit. Sam, enseignant, veut traiter les notes de ses eleves en une commande. Trois metiers, meme logique : Python comme outil, pas comme devoir.

Trois fils rouges reviennent tout le livre. Un fichier CSV de notes (eleve, matiere, note) que Sam utilise en classe. Une API meteo qui renvoie du JSON que Max consulte avant un chantier exterieur. Un script **CLI** que Lea lance depuis le terminal avec des options, sans retoucher le code a chaque client. Ces exemples ne sont pas decoratifs. Ils te montrent le meme geste sous plusieurs angles : lire des donnees, les resumer, gerer l'echec, rendre le script utilisable par quelqu'un d'autre - toi demain matin compte.

## Ce que ce n'est pas

Ce n'est pas un cours complet depuis zero. On ne revient pas sur `print`, `if`, `for`, ni sur "c'est quoi un dictionnaire". Si tu bloques sur ces mots, relis le premier livre Python du parcours. Ce n'est pas non plus un livre web : pas de Django, Flask, FastAPI ici. On reste en Python "outil", clair, dans le terminal et les fichiers. Ce n'est pas un manuel de data science non plus. Pas de pandas obligatoire. Juste la bibliotheque standard plus `requests` et eventuellement `pytest`.

Ce n'est pas non plus "devenir expert en une semaine". Un script qui lit un tableau et affiche une moyenne, c'est deja du temps gagne. Un script qui affiche la meteo du matin, c'est deja un outil perso. Un CLI avec `-h` lisible, c'est deja "pro" pour un petit projet. On monte cran par cran, sans te noyer.

:::retenir
Note des maintenant tes trois fils rouges perso : un tableau a lire, une info a recuperer dehors, une commande que tu voudrais taper sans ouvrir l'editeur.
:::

## Ce que tu gardes en tete

Tu sais ecrire une fonction. Tu sais boucler sur une liste. Tu sais ouvrir un fichier texte et lire du JSON. Tu as vu `try/except`. C'est assez pour avancer. On monte d'un cran avec des outils standards : `pathlib` pour les chemins, `csv` pour les tableaux, `argparse` pour la ligne de commande, `venv` et `pip` pour les paquets, `requests` pour le HTTP, `logging` pour les traces, `datetime` pour les dates, `re` pour quelques motifs texte.

## La carte du livre

Les premiers chapitres posent les briques une par une. Chemins, CSV, CLI, environnement virtuel, appels API, erreurs reseau, secrets, logs, dates, regex. Puis un mini-projet qui assemble tout ca. Trois ateliers concrets (CSV, CLI, API). Ensuite tests simples, organisation de projet, bonnes pratiques. Le quiz verifie. Le dernier chapitre, c'est pour souffler et regarder la route parcourue.

Tu n'as pas besoin d'un framework web pour etre utile des demain. Ce livre te donne la boite a outils du quotidien : fichiers, terminal, reseau, hygiene. Le reste (web, bases de donnees, packaging) vient apres, sur ce socle.

## Ce dont tu as besoin

Python 3 installe. Un editeur (VS Code, Cursor, ou autre). Un terminal. Pour la partie API : une connexion internet et un venv. Rien de plus pour suivre. Les paquets hors standard seront installes au fur et a mesure (`requests`, plus tard eventuellement `pytest`).

## Comment lire ce livre

Lis dans l'ordre au debut. Les chapitres s'enchainent logiquement. Les ateliers sont la pour faire, pas seulement lire. A chaque fin de chapitre, il y a un "A toi". Fais-le. Cinq minutes valent mieux qu'une lecture passive. Tu peux revenir ensuite a un chapitre precis (CSV, argparse, requests) comme a une fiche quand un cas reel te bloque.

## Petite histoire

Sam avait un tableur de notes ouvert depuis septembre. Chaque fin de trimestre, meme galere : copier-coller, moyennes a la main, une formule cassee. Lea lui a montre un script de quarante lignes qui lit un CSV et sort les moyennes. Sam n'est pas devenu developpeur. Il a juste gagne deux heures par session. Max, lui, checkait la meteo sur son telephone avant chaque toiture. Il a ecrit un petit script terminal avec sa ville en argument. Moins de clics, meme info, plus rapide le matin dehors.

Lea, le meme mois, a transforme trois exports clients "a la main" en une commande. Elle a gagne une soiree. Pas de magie. Juste Python pratique, le genre d'outil qu'on garde sous le coude chez DanielCraft.

## Erreur classique

Croire que "je connais les bases" egal "je sais automatiser mon quotidien". Les bases sont le moteur. La pratique, c'est la boite a outils : CSV, CLI, HTTP, logs. Sans ca, tu reecris tout a la main a chaque fois. Autre piege : vouloir tout apprendre d'un coup sans faire les ateliers. Ce livre se gagne en tapant du code, pas en lisant passivement.

:::attention
Si tu sautes les "A toi", tu vas "comprendre" et ne plus savoir faire dans trois semaines. Cinq minutes actives battent quarante pages passives.
:::

## En vrai

Ouvre un vieux script Python que tu as deja ecrit. Note ce qui manque pour le rendre utile : lire un tableau ? accepter un argument ? appeler une URL ? isoler les paquets ? Ce livre repond a ca, chapitre par chapitre.

## A toi

Ecris en trois phrases ce que tu veux construire a la fin. Pas un reseau social. Quelque chose de petit : "resumer mes notes depuis un CSV", "afficher la meteo de ma ville", "un script CLI qui dit bonjour avec mon nom". Garde ce but. On y reviendra au mini-projet. Si tu hesites entre trois idees, choisis celle que tu utiliserais vraiment la semaine prochaine. Chez DanielCraft, un usage reel bat une intention ambitieuse.

:::astuce
Les bases, c'est le moteur. Ce livre, c'est la boite a outils du quotidien : fichiers, CLI, HTTP, hygiene. Garde cette phrase sous le coude.
:::
