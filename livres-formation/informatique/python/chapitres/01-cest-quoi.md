# Chapitre 1 - Salut, c'est quoi Python ?

Python, ce n'est pas un serment de magie ni un club reserve aux ingenieurs. C'est un **langage de programmation** : une facon d'ecrire des instructions que l'ordinateur peut suivre. Tu formules une idee en phrases plus lisibles que dans beaucoup d'autres langages. Python la traduit. La machine execute. En 2026, quand quelqu'un dit "j'ai fait un petit **script**", il parle souvent de Python : renommer des fichiers, calculer un score, lire un CSV, brancher une API, preparer des donnees pour un modele. Le geste reste le meme depuis le debut : ecrire, lancer, lire le resultat, corriger.

Chez DanielCraft, on aime une image nette. Python, c'est un messager clair entre toi et la machine. Tu restes le chef. Si le message est flou, l'ordinateur se plaint avec un **message d'erreur**. Ce n'est pas une humiliation. C'est un dialogue. Lea, freelance web, s'en sert pour automatiser des exports clients et verifier des listes. Max, artisan, l'utilise pour un mini calculateur de devis. Sam, enseignant, prepare des quiz dans le terminal pour ses eleves. Trois metiers, meme logique : gagner du temps sur le repetitif, garder le cerveau pour le jugement.

## Ce que ce n'est pas

Ce n'est pas "la seule facon de coder". Ce n'est pas non plus un outil qui lit dans tes pensees : si tu n'as pas clarifie le probleme, le code sera confus. Ce n'est pas une excuse pour coller un script non relu sur la machine d'un client. Et ce n'est surtout pas un langage "trop simple pour etre serieux". Derriere la syntaxe accueillante, tu peux aller tres loin : data, IA, web, automatisation. Ici, on pose des bases solides. Ensuite on touche exceptions et classes, sans devenir un manuel de 800 pages.

Ce n'est pas non plus "tout comprendre avant d'ecrire". Beaucoup de debutants attendent d'avoir la theorie complete. Ils n'ecrivent jamais la premiere ligne. Python s'apprend en tapant, en cassant, en relisant l'erreur. Tu n'as pas besoin de devenir chercheur. Tu as besoin de devenir quelqu'un qui ose lancer `python mon_fichier.py` et lire ce qui sort.

Tu as une tache. Tu la decoupes. Tu ecris des instructions. Python execute. Si ca plante, le message d'erreur pointe souvent la ligne. Tu corriges. Tu relances. Le pont, c'est le fichier **`.py`** : un texte simple, des mots cles, de l'**indentation**. Sans pont clair, tu obtiens du flou. Avec un pont, tu obtiens quelque chose de reutilisable. Plus loin dans le livre : variables, types, conditions, boucles, fonctions, listes, dictionnaires, fichiers, modules, exceptions, classes. Pas pour te faire peur. Pour que tu saches ce que tu manipules.

Lea ouvre VS Code, ecrit dix lignes, gagne vingt minutes chaque semaine. Max prefere IDLE au debut : moins d'options, moins de panique. Sam projette le terminal devant la classe et montre qu'une erreur n'est pas un drame. Chez DanielCraft, on prefere ce genre d'habitude a la collection de tutos oublies le lendemain.

:::astuce
Dis a voix haute une tache repetee de ton quotidien. Si tu peux la decouper en trois etapes claires, tu as deja un futur script.
:::

## Ce que tu vas savoir faire

Tu vas installer Python et lancer un programme. Tu manipuleras variables, types, conditions et boucles. Tu ecriras des fonctions avec parametres et `return`. Tu joueras avec listes et dictionnaires. Tu liras et ecriras des fichiers (texte et JSON). Tu importeras des modules comme `random` ou `math`. Tu gereras des erreurs avec `try/except`, tu creeras une petite `class`, tu feras un quiz et un jeu dans le terminal. Puis un mini-projet, un recap, trois ateliers, un quiz final, et un bravo.

Niveau debutant solide, avec un cran intermediaire a la fin. Pas besoin d'avoir deja code. Besoin de curiosite et d'honnetete : tu tapes, tu observes, tu corriges.

## Comment lire ce livre

Lis dans l'ordre au debut. Les premiers chapitres posent le sol. Les ateliers font faire. Le quiz verifie. Retape les exemples a la main. Change une valeur, puis relance. Si tu copies-colles sans reflechir, ca rentre moins. Si tu tapes, ca rentre. A chaque fin de chapitre, il y a un "A toi". Fais-le. Cinq minutes valent mieux qu'une lecture passive de quarante pages.

## Petite histoire

Lea devait renommer cinquante captures d'ecran pour un client. Avant, elle le faisait a la main, une par une, en pestant. Maintenant, elle ecrit un petit script : lire le dossier, construire un nouveau nom, renommer. Elle teste sur trois fichiers. Elle lance sur le reste. Dix minutes, travail net. Python n'a pas "pense le projet". Il a execute une recette claire.

Max, lui, calculait toujours sa marge sur un coin de papier. Il a demande a Sam une version simple en Python : prix fournitures, temps, marge. Il tape trois nombres, lit le resultat. Ce n'est pas de la triche. C'est de l'aide au calcul - a condition de verifier que la formule est la sienne, pas une invention. On y revient dans tout le livre : toi tu pilotes, le code accelere.

## Erreur classique

Croire que "je dois tout comprendre avant d'ecrire". Ou croire que "le message d'erreur veut dire que je suis nul". Souvent, le probleme n'est pas toi. C'est une guillemet oubliee, une indentation, un mauvais dossier dans le terminal. Lis la derniere ligne de l'erreur. Elle parle souvent clairement.

Autre piege : vouloir construire "l'app complete" des le jour un. Commence par afficher "Salut". Puis une variable. Puis une condition. Monte ensuite. Tu seras pret.

## En vrai

Ouvre un terminal. Si Python est deja la, tape `python --version` ou `py --version`. Note le numero. Si rien ne repond, pas de panique : le chapitre suivant installe. Dis a voix haute une tache simple que tu aimerais automatiser. Ce livre sert a transformer cette envie en habitude propre.

## A toi

Ecris en trois phrases : (1) une tache repetee qui te fatigue, (2) ce que tu accepterais qu'un script fasse a ta place, (3) ce que tu ne laisserais jamais tourner sans controle humain. Garde ce papier. On y reviendra au mini-projet.

## Zoom : langage vs outil

Beaucoup de gens melangent Python et "l'IA", ou Python et "un site web". Python est le langage. Les outils (editeur, bibliotheques, frameworks) s'appuient dessus. Tu peux ecrire du Python sans IA. Tu peux utiliser une IA pour t'aider a ecrire du Python. Ce n'est pas la meme chose. Ici, on apprend le langage. Si tu utilises un assistant pour debloquer une syntaxe, relis toujours ce qu'il propose avant de le coller. Chez DanielCraft, le pilote, c'est toi.

## Petite scene DanielCraft

Lea ouvre son dossier `mes-tests-python`, cree `salut.py`, lance, sourit. Max regarde par-dessus l'epaule, demande "et pour mon devis ?". Sam repond : "d'abord print, ensuite les calculs". Trois usages, une meme posture : avancer par petites victoires visibles.

:::retenir
Python = un messager clair. Tu ecris la recette, la machine execute, tu restes responsable.
:::

## Ce que ce livre doit changer chez toi

A la fin, tu ne seras pas architecte logiciel. Tu seras quelqu'un qui lit une erreur sans paniquer, qui decoupe un probleme, qui range une idee dans une fonction, qui sait ouvrir un fichier et qui ose une petite classe. C'est deja beaucoup. C'est surtout actionnable demain matin.
