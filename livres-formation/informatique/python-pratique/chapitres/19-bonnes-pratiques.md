# Chapitre 19 - Bonnes pratiques

Ce chapitre ne rajoute presque pas de syntaxe. Il solidifie des reflexes. Tu peux le relire de temps en temps, comme une checklist amicale. Chez DanielCraft, on prefere trois habitudes ancres a dix intentions oubliees. Ce n'est pas un sermon. C'est une boite a outils mentale pour le jour ou tu livres, partages, ou reprends un script a froid.

Lea relit cette liste avant de livrer un script client. Max l'a collee en commentaire en haut de ses outils perso. Sam en parle en fin de trimestre : ce ne sont pas des regles scolaires, ce sont des gestes qui evitent la galere. Toi, tu en choisis deux cette semaine. Pas vingt. Deux.

:::retenir
Noms clairs, echecs previsibles, secrets dehors, venv isole. Quatre piliers. Le reste suit.
:::

## Fonctions courtes, noms clairs

`moyenne_eleve` dit ce qu'elle fait. `calc2` non. Une fonction qui lit un CSV, appelle le reseau, formate trois messages et ecrit un fichier... c'est trop. Decoupe. Chez DanielCraft, on prefere trois fonctions ennuyeuses a une fonction heros. Lea renomme avant de refactorer. Max a appris apres un devis faux. Sam barre les noms flous au tableau.

## Un seul role pour le point d'entree

`main` parse, appelle, affiche. La logique metier vit ailleurs. Benefice : tests plus simples, CLI plus mince. Tu as vu ca au chapitre tests. Ici, tu l'ancres comme habitude, pas comme theorie.

## Echecs previsibles

Fichier absent, JSON inattendu, reseau down : tu les as deja vus. Traite-les tot. Messages en francais simple. Details techniques dans les logs. Code retour non zero (`sys.exit(1)`) quand le script est utilise dans une chaine d'outils. L'humain lit une phrase. La machine lit un code. Les deux comptent.

## UTF-8 et chemins

Toujours `encoding="utf-8"` pour le texte francais. Preferer `pathlib`. Eviter les chemins absolus graves dans le code (`C:\Users\...`) : passe-les en argument ou relative au projet. Lea a deja livre un script qui marchait chez elle et cassait chez le client a cause d'un chemin absolu. Depuis, argument ou relatif. Point.

## Dependances sous controle

Venv. `requirements.txt`. `python -m pip`. Pas de "j'ai installe globalement, tant pis". Moins de mysteres entre machines. Sam refuse de deboguer un projet eleve sans venv active. Max aussi, depuis qu'il a casse un autre outil en mettant a jour un paquet global.

## Secrets

Variables d'environnement. `.env` ignore par Git. `.env.example` partageable. Jamais de jeton dans un screenshot de cours ni dans un log. Chez DanielCraft, c'est non negociable. Une cle fuitee, c'est une soiree gachee et parfois une facture.

## Peu de magie

Les regex, les one-liners cryptiques, les imports circulaires : souvent impressifs, rarement gentils pour le futur toi. Clairete > densite. Si tu as besoin d'un commentaire pour expliquer une ligne, demande-toi si tu peux ecrire trois lignes plus claires a la place.

## Documenter le "pourquoi" utile

Un README court. Une docstring sur une fonction non evidente. Pas besoin de commenter `i += 1`. Commente l'intention quand le code seul ne suffit pas : "Open-Meteo renvoie la temp en C sous current_weather". Lea ecrit le pourquoi. Max ecrit l'exemple d'appel. Sam exige les deux sur les projets partages.

## Versionne tes donnees d'exemple

Un petit `data/notes.exemple.csv` aide. Evite de casser le CSV "reel" a chaque test. Copie, travaille, compare. Sam le fait systematiquement. Lea aussi, apres avoir ecrase un export client une fois. Une fois suffit.

## Petit, mais relancable

Un bon script se relance demain sans que tu te souviennes de tous les details. L'aide `-h`, le README, et des exemples d'appel dans un commentaire en haut du fichier aident enormement. Ecris pour ton futur toi fatigue. C'est la vraie audience.

## Eviter la perfection prematuree

Pas besoin de microservices pour un CSV de notes. Pas besoin de dix fichiers pour trente lignes. Organise assez pour rester lisible. Si tu passes plus de temps a "architecturer" qu'a faire marcher le cas nominal, simplifie. Chez DanielCraft, on coupe les chateaux avant les fondations.

## Code retour et scripts en chaine

Quand ton script est appele par un autre outil (cron, tache planifiee, Makefile), le code retour compte. `sys.exit(0)` si tout va bien, `sys.exit(1)` si echec. L'appelant peut reagir sans lire le texte affiche. Max a decouvert ca quand son script meteo "marchait" mais envoyait quand meme un mail d'alerte parce qu'il retournait 1 par erreur. Une ligne, un gros bug en moins.

## Petite checklist avant de partager

Est-ce que `-h` est clair ? Est-ce qu'un fichier manquant est explique ? Est-ce que le venv est documente ? Est-ce qu'un secret traine ? Est-ce qu'un test minimal existe pour le coeur du calcul ? Si oui, ton script merite d'etre montre. Sinon, corrige deux cases, puis montre. Pas besoin d'attendre la perfection.

## Petite histoire

Lea a livre un script sans README ni requirements. Le client a mis trois jours a le faire tourner. Lea a ajoute quinze lignes de doc et un requirements.txt. Le client a relance en dix minutes. La lecon : un script pratique, c'est aussi un script qu'on peut reprendre sans toi.

Max a partage un outil avec une cle en dur "juste pour la demo". La demo a fuite dans un salon. Il a tourne la cle, appris la lecon, colle `.env.example` partout depuis. Sam raconte cette histoire (anonymisee) chaque annee. Elle marche mieux qu'un slide "securite".

## Erreur classique

Vouloir appliquer les vingt points d'un coup et ne rien ancrer. Ou traiter ce chapitre comme de la litterature : lu, admire, oublie. Autre piege : perfectionner l'architecture pendant que le cas nominal ne marche pas encore. Fais marcher. Puis solidifie. Dans cet ordre.

:::attention
Une cle dans le code "juste pour la demo", c'est deja une fuite en puissance. `.env`, toujours.
:::

## En vrai

Relis ton mini-projet avec cette checklist. Corrige deux choses seulement, mais pour de vrai. Les bonnes pratiques arrivent par couches, pas par sermon. Demain, deux autres. Dans une semaine, ton script aura change de visage sans drame.

## A toi

Choisis une habitude (timeout, venv, ou secrets) et applique-la systematiquement a tous tes scripts cette semaine. Une habitude ancree vaut mieux que dix intentions. Ecris l'habitude sur un post-it. Coches chaque script traite. Simple, visible, efficace. Si tu rates un jour, ne recommence pas a zero : reprends le script suivant. Chez DanielCraft, la constance bat la perfection.

:::astuce
Deux habitudes cette semaine, pas vingt. Une ancree bat dix intentions sur un post-it oublie.
:::
