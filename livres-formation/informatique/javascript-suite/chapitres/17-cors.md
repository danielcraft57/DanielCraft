# Chapitre 17 - CORS, en une page claire

Tu appelles une API depuis ta page. La console crie quelque chose avec "CORS" ou "blocked by CORS policy". Tu te dis que JavaScript est casse, que fetch est nul, que tu as fait une faute de frappe. Souvent, non : c'est le navigateur qui applique une regle de securite. Comprendre CORS en deux minutes te evite des heures de panique et de mauvaises "solutions" trouvees sur des forums.

Chez DanielCraft, on voit des juniors perdre une journee entiere sur CORS sans savoir ce que c'est. Ce chapitre te donne l'essentiel : pas un cours complet de securite web, mais assez pour savoir quoi faire quand le message apparait.

Une page hebergee sur http://localhost:3000 qui demande des donnees a https://autre-site.com fait une requete "inter-origine". Origine = protocole + domaine + port. Le navigateur demande au serveur distant : "Est-ce que tu autorises cette origine a lire ta reponse ?" Si le serveur ne repond pas oui avec les bons en-tetes CORS (Access-Control-Allow-Origin, etc.), le navigateur bloque la reponse cote page. Ton code fetch echoue. Ce n'est pas toujours toi qui "codes mal". C'est une regle : un site malveillant ne doit pas lire facilement les donnees privees d'un autre site a ta place sans que le serveur distant l'accepte.

## Ce que tu peux faire en apprenant

Utilise des API qui autorisent explicitement le navigateur (demos publiques, APIs avec CORS ouvert pour les tests). Ou passe par ton propre serveur (backend) qui, lui, appelle l'API cote serveur : le navigateur ne voit que ton domaine. Ou travaille avec des fichiers JSON locaux servis par le meme origine pendant les exercices de ce livre. Lea developpe souvent le front contre un petit backend maison ou des JSON locaux avant de brancher l'API cliente.

## Ce qu'il ne faut pas croire

"Desactiver CORS" dans le navigateur via une extension ou un flag n'est pas une solution pro. Ca peut aider cinq minutes pour un test solo, ca ne regle rien pour tes utilisateurs finaux. Ne ship jamais une appli qui depend de ca. Autre mythe : "CORS c'est only en dev". Non, c'est partout dans le navigateur.

## Petite histoire

Max voulait afficher des donnees d'une API meteo gratuite sur son site. Ca marchait quand il ouvrait l'URL directement dans le navigateur. Ca plantait en fetch depuis sa page. Meme URL, contexte different : barre d'adresse vs JavaScript. Lea lui a montre une API alternative avec CORS autorise, puis un fichier JSON local pour l'exercice. Probleme compris, pas contourne en hack.

Sam explique a ses eleves : lire une URL dans la barre, ce n'est pas la meme chose qu'une requete fetch depuis une page. Le navigateur applique des regles differentes.

## Lire le message d'erreur

Quand tu verras CORS, lis le message : quelle origine est bloquee ? quelle URL distante ? quelle methode ? Puis demande-toi : est-ce que je suis cense appeler cette API directement depuis le navigateur, ou depuis un serveur intermediaire ? Cette question evite des heures de tentatives inutiles. Parfois la reponse est "utilise leur SDK" ou "inscris-toi pour une cle avec domaine autorise".

## Erreur classique

Conclure que fetch est casse et tout reecrire en XMLHttpRequest (meme probleme CORS). Ou copier une extension "Allow CORS" et croire que le projet est fini. Ou blamer le JSON alors que c'est l'origine.

## En vrai

Note en une phrase ta definition personnelle de CORS. Si tu peux l'expliquer a un ami sans jargon ("le navigateur verifie si le site distant accepte que MA page lise sa reponse"), c'est gagne. Garde une liste de deux APIs que tu sais utiliser depuis le front sans surprise, et une strategie backend si tu depasses.

## A toi

Ecris ta definition CORS en trois lignes max. Puis liste deux options quand une API bloque : API alternative avec CORS OK, ou backend intermediaire. Pas besoin d'implementer le backend ici : comprendre la strategie suffit pour ce livre.

## Preflight : une precision utile

Pour certaines requetes (POST avec headers custom, methodes exotiques), le navigateur envoie d'abord une requete OPTIONS "preflight" pour demander la permission. Si le serveur ne repond pas correctement, fetch echoue avant meme ton POST. En exercice avec JSON simple et APIs de demo, tu touches parfois ce cas. Symptome : erreur CORS alors que GET marchait. Solution : lire la doc API ou passer par ton backend.

## Same-origin en pratique

Meme domaine, meme port, meme protocole : pas de CORS. Fichier servi depuis http://localhost:5500 qui fetch http://localhost:5500/data.json : OK. Page file:// qui fetch n'importe quoi : souvent KO. Page localhost qui fetch api externe : depend des en-tetes du serveur distant. Lea teste toujours en conditions proches de la prod (serveur local, pas file).

## En resume DanielCraft

CORS n'est pas un bug de ton code JavaScript. C'est le navigateur qui protege l'utilisateur. Ton job front : utiliser des sources compatibles navigateur, ou deleguer au backend. Ne perds pas une journee a "desactiver CORS". Perds trente minutes a comprendre l'origine du blocage et choisir la bonne strategie.
