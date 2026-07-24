# Chapitre 17 - CORS, en une page claire

Tu appelles une API. La console crie quelque chose avec "CORS". Tu te dis que JavaScript est casse. Souvent, non : c'est le navigateur qui protege.

## L'idee simple

Une page hebergee sur `http://localhost:3000` qui demande des donnees a `https://autre-site.com` fait une requete "inter-origine". Le navigateur demande au serveur distant s'il accepte. Si le serveur ne dit pas oui (en-tetes CORS), le navigateur bloque la reponse cote page.

Ce n'est pas toi qui "codes mal" a chaque fois. C'est une regle de securite : un site malveillant ne doit pas lire facilement les donnees privees d'un autre site a ta place.

## Ce que tu peux faire en apprenant

- Utilise des API qui autorisent le navigateur (demos publiques).
- Ou passe par ton propre serveur (backend) qui, lui, appelle l'API.
- Ou travaille avec des fichiers JSON locaux pendant les exercices.

## Ce qu'il ne faut pas croire

"Desactiver CORS" dans le navigateur n'est pas une solution pro. Ca peut aider cinq minutes pour un test, ca ne regle rien pour tes utilisateurs.

## En vrai

Quand tu verras CORS, lis le message : origine bloquee, methode, en-tetes. Puis demande : est-ce que je suis cense appeler cette API depuis le navigateur, ou depuis un serveur ? Cette question evite des heures de panique.

## A toi

Note en une phrase ta definition personnelle de CORS. Si tu peux l'expliquer a un ami sans jargon, c'est gagne.
