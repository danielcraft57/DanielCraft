# Chapitre 1 - Rappel rapide et carte du livre

Tu as deja fait les bases. Variables, conditions, boucles, fonctions, DOM, evenements. Si quelque chose est flou, ce n'est pas grave : on ne va pas tout refaire. Ce livre part du moment ou la page commence a parler avec le monde exterieur.

Chez DanielCraft, on aime bien une image simple. Les bases, c'etait apprendre a faire bouger une piece. La suite, c'est ouvrir la fenetre, envoyer un message, attendre une reponse, et ranger le code pour qu'il reste lisible.

## Ce que tu gardes en tete

Tu sais selectionner un element avec `querySelector`. Tu sais ecouter un clic ou un `submit`. Tu sais changer un texte avec `textContent`. Tu sais ecrire une fonction. C'est assez pour avancer.

On ne revient pas sur `let`, `if`, `for`, ni sur "c'est quoi le DOM". Si tu bloques sur ces mots, relis le premier livre. Ici, on monte d'un cran.

## La carte du livre

Imagine une petite appli meteo, un formulaire de contact, ou une liste de produits. Pour que ca marche vraiment, tu as besoin de plusieurs pieces.

D'abord les formulaires. Tu recuperes ce que la personne a tape, tu verifies, tu affiches une erreur claire si besoin. Ensuite JSON : un format de texte pour transporter des donnees (nom, prix, temperature...). Puis `fetch` : ta page demande des infos a un serveur. Les promesses et `async/await` t'aident a attendre la reponse sans te perdre. Les modules te permettent de decouper le code en fichiers. Et a la fin, tu debogues, tu organises, tu fais de petits ateliers.

## Un fil rouge

On va souvent parler de trois exemples. Une todo un peu plus serieuse. Une meteo qui charge des donnees. Un formulaire de contact qui valide avant d'envoyer. Ces exemples reviennent, pour que tu sentes le progres.

## Comment lire ce livre

Lis dans l'ordre au debut. Formulaires, JSON, fetch, promesses, async : ca s'enchaine. Ensuite modules et organisation. Les ateliers sont la pour faire, pas seulement lire. Le quiz sert a verifier. Le dernier chapitre, c'est juste pour souffler et voir la suite.

Tu n'as pas besoin d'un framework. React, Vue, et les autres viendront plus tard si tu veux. Ici, on reste en JavaScript "nu", clair, dans le navigateur.

## Erreur classique

Croire que "je connais les bases" = "je sais faire une vraie app". Les bases sont le moteur. La suite, c'est la route, le carburant, et la carte. Sans fetch et JSON, ta page reste seule dans sa bulle. Sans modules, ton fichier devient un spaghetti. Sans validation de formulaire, tu envoies n'importe quoi.

## En vrai

Ouvre une page que tu as deja codee (compteur, todo simple...). Note ce qui manque pour en faire quelque chose d'utile : charger une liste depuis ailleurs ? envoyer un message ? decouper le fichier ? Ce livre repond a ca.

## A toi

Ecris en trois phrases ce que tu veux construire a la fin. Pas un reseau social. Quelque chose de petit : "afficher la meteo de ma ville", "valider un formulaire contact", "charger une liste de produits". Garde ce but. On y reviendra.
