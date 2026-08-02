# Chapitre 1 - Rappel rapide et carte du livre

Tu as deja parcouru les bases JavaScript. Variables, conditions, boucles, fonctions, DOM, evenements : tout ca, tu l'as deja touche. Ce livre ne repart pas de zero. Il part du moment ou ta page cesse d'etre seule dans son coin et commence a parler avec le monde exterieur. Formulaires qui valident avant d'envoyer, donnees qui voyagent en **JSON**, requetes reseau avec **fetch**, attente propre avec **promesses** et **async/await**, code decoupe en **modules** : voila le terrain de la suite. Tu vas sentir le passage entre "je fais bouger un bouton" et "je livre une petite feature qui charge et envoie pour de vrai".

Chez DanielCraft, on aime une image simple pour situer le niveau. Le premier livre JavaScript, c'etait apprendre a faire bouger une piece sur l'echiquier. Ici, c'est ouvrir la fenetre, envoyer un message, attendre une reponse, ranger le code pour qu'il reste lisible dans six mois, et savoir expliquer a l'utilisateur quand ca charge ou quand ca casse. Tu n'as pas besoin d'un framework pour ca. React, Vue et les autres viendront plus tard si tu veux. Ici, on reste en JavaScript "nu", clair, dans le navigateur. Ce choix est volontaire : quand tu comprendras le flux a nu, un framework ne sera plus de la magie opaque.

## Ce que tu gardes en tete

Tu sais selectionner un element avec querySelector. Tu sais ecouter un clic ou un submit. Tu sais changer un texte avec textContent. Tu sais ecrire une fonction. C'est deja beaucoup. On ne revient pas sur let, if, for, ni sur "c'est quoi le DOM". Si ces mots te bloquent encore, relis le premier livre du parcours. Ici, on monte d'un cran sans te laisser en rade. Tu peux relire un chapitre du tome 1 en vingt minutes si un souvenir flanche : mieux vaut ca que de forcer en restant perdu.

Lea, freelance web, en est la : elle sait animer un menu et compter des clics. Max, artisan plombier qui code un peu son site, sait afficher ses tarifs. Sam, enseignant, fait des petits exercices interactifs pour ses eleves. Tous trois ont le meme besoin maintenant : faire parler leur page avec des donnees reelles. Trois metiers, un meme saut technique. Tu vas les retrouver tout au long du livre comme des compagnons de route, pas comme des mascottes inutiles.

Imagine une petite appli meteo, un formulaire de contact, ou une liste de produits. Pour que ca marche vraiment, tu as besoin de plusieurs briques qui s'enchainent. D'abord les formulaires : recuperer ce que la personne a tape, verifier, afficher une erreur claire si besoin. Ensuite JSON, le format texte standard pour transporter des donnees (nom, prix, temperature). Puis fetch : ta page demande des infos a un serveur. Les promesses et async/await t'aident a attendre la reponse sans te perdre dans des pyramides de then. Les modules te permettent de decouper le code en fichiers. Et a la fin, tu debogues, tu organises, tu fais des ateliers concrets.

On va souvent parler de trois exemples fil rouge. Une todo un peu plus serieuse. Une meteo qui charge des donnees. Un formulaire de contact qui valide avant d'envoyer. Ces exemples reviennent pour que tu sentes le progres chapitre apres chapitre, pas seulement des morceaux isoles. Quand une idee reapparait sous un autre angle, ce n'est pas un oubli : c'est de l'ancrage.

:::astuce
Garde une page perso ouverte pendant toute la lecture (compteur, todo, galerie). Chaque chapitre te dira ce qu'il lui manque encore. Tu transformeras la lecture en checklist vivante.
:::

## Ce que tu vas savoir faire

Dans ce livre, tu vas valider des formulaires proprement, manipuler JSON avec parse et stringify, faire des requetes GET et POST avec fetch, gerer les erreurs reseau et les codes HTTP, ecrire du code async lisible, decouper un projet en modules, deboguer avec methode, comprendre **CORS** sans panique, ralentir une recherche avec debounce, et appliquer quelques reflexes de performance. Puis un mini-projet, un recap, trois ateliers, un quiz, et un bravo.

Niveau debutant solide qui a deja code un peu. Pas besoin d'etre "tech avance". Besoin de curiosite et de patience : le reseau ne repond pas toujours, et c'est normal. Une appli qui explique l'echec vaut mieux qu'une appli qui marche seulement le jour du wifi parfait.

## Comment lire ce livre

Lis dans l'ordre au debut. Formulaires, JSON, fetch, promesses, async : ca s'enchaine logiquement. Ensuite modules et organisation. Les ateliers sont la pour faire, pas seulement lire. Le quiz verifie. Le dernier chapitre, c'est pour souffler et voir la suite. Tu peux revenir ensuite a un chapitre precis (erreurs reseau, CORS, debounce) comme a une fiche. A chaque fin de chapitre, il y a un "A toi". Fais-le. Cinq minutes valent mieux qu'une lecture passive.

Si un chapitre te semble deja connu, lis-le quand meme en diagonale : le ton et les pieges cites servent de filet de securite pour la suite. Les ateliers, eux, ne se "lisent" pas : ils se livrent.

## Petite histoire

Lea avait un compteur de clics sur son portfolio. Ca marchait. Le client lui a demande : "Et si on affichait mes produits depuis ma boutique en ligne ?" Lea a ouvert son fichier de 200 lignes, a cherche ou mettre un fetch, et s'est sentie perdue. Ce livre repond exactement a ce moment : tu sais deja bouger la piece, maintenant tu apprends la route.

Max voulait un formulaire de devis sur son site. Sans validation, il recevait des mails vides. Sam voulait charger une liste de mots pour un quiz. Meme schema mental pour tous : lire, verifier, envoyer ou afficher, gerer l'echec. Trois debuts differents, un meme besoin de methode.

## Erreur classique

Croire que "je connais les bases" egal "je sais faire une vraie app". Les bases sont le moteur. La suite, c'est la route, le carburant, et la carte. Sans fetch et JSON, ta page reste seule dans sa bulle. Sans modules, ton fichier devient un spaghetti illisible. Sans validation de formulaire, tu envoies n'importe quoi au serveur ou tu frustres l'utilisateur avec des messages cryptiques.

Autre piege : vouloir tout faire d'un coup. Un formulaire qui POST, charge une liste, debounce une recherche et gere CORS le premier jour, c'est trop. Avance chapitre par chapitre. Chaque brique se pose sur la precedente.

:::attention
Ne saute pas les "A toi" pour "gagner du temps". Sans micro-action, le cerveau classe le chapitre comme "lu", pas comme "su". Cinq minutes actives battent quarante pages passives.
:::

## En vrai

Ouvre une page que tu as deja codee (compteur, todo simple, galerie basique). Note ce qui manque pour en faire quelque chose d'utile : charger une liste depuis ailleurs ? envoyer un message ? decouper le fichier en plusieurs morceaux ? Ce livre repond a ces questions une par une. Garde cette page ouverte en reference pendant la lecture. Si tu n'as aucune page sous la main, note trois idees de mini-apps et choisis-en une avant le chapitre 2.

## A toi

Ecris en trois phrases ce que tu veux construire a la fin de ce livre. Pas un reseau social. Quelque chose de petit et concret : "afficher la meteo de ma ville", "valider un formulaire contact avant envoi", "charger une liste de produits depuis un fichier JSON". Garde ce but sur papier. On y reviendra au mini-projet et dans les ateliers.

## Zoom DanielCraft : le fil rouge technique

Sur la duree du livre, tu vas assembler exactement ce type de flux : evenement utilisateur (clic, submit) -> validation locale -> fetch avec await -> verification response.ok -> JSON.parse implicite via .json() -> affichage DOM -> message d'erreur humain si echec. Ce schema revient partout. Apprends-le comme une recette de cuisine. Les ingredients changent (meteo, produits, citations), la recette reste. Quand tu seras bloque plus tard, reviens a cette recette avant de tout reecrire.

## Ce que ce livre n'est pas

Ce n'est pas un cours Node.js backend complet. Ce n'est pas un guide React. Ce n'est pas un manuel de securite avancee. Tu n'as pas besoin d'installer Webpack pour suivre. Tu as besoin d'un editeur, d'un navigateur, et d'un mini serveur local pour fetch et modules (Live Server ou python -m http.server suffisent). Si tu bloques la, relis le README du dossier livre ou demande de l'aide : ce setup revient dans tous les projets front modernes.

## Tableau rapide des chapitres

Chapitres 2 a 8 : parler au reseau (formulaires, JSON, fetch, async, erreurs, POST). Chapitres 9 a 11 : ranger et deboguer. Chapitre 12 : mini-projet assemble. Chapitre 13 : recap. Chapitres 14 a 16 : ateliers mains dans le code. Chapitres 17 a 19 : CORS, debounce, perf legere. Chapitres 20 a 21 : quiz et bravo. Tu peux sauter temporairement 17-19 si tu es presse, mais reviens-y avant un vrai deploiement : CORS te rattrapera toujours.

## Petite scene DanielCraft

Lea ouvre le chapitre 4 en sachant deja valider un formulaire. Max ouvre le chapitre 2 parce que son site envoie encore des champs vides. Sam fait le parcours complet avec ses eleves en douze seances. Trois rythmes, un meme livre. Choisis le tien, mais ne saute pas les "A toi" : c'est la que le livre devient competence.

:::retenir
Bases = moteur. Suite = route + JSON + fetch + async + modules - avance brique par brique, livre les "A toi".
:::
