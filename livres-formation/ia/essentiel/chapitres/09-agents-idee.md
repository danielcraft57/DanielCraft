# Chapitre 9 - Les agents : l'idee, sans science-fiction

Un agent, en version simple, c'est une IA a qui tu donnes un but, et qui enchaine plusieurs actions avec des outils pour s'en approcher : chercher une info, lire un fichier, ecrire un brouillon, classer, parfois cliquer dans une interface. Ce n'est plus seulement "reponds a ma question". C'est "avance sur cette mission".

En 2026, les agents grand public existent sous des formes variees : mode "ordinateur" ou navigateur dans certains chats, automatisations Zapier/Make branchees a de l'IA, assistants dans les IDE, workflows d'entreprise. Parfois spectaculaire. Parfois fragile. Souvent couteux en attention si mal cadre.

Chez DanielCraft, on enseigne l'idee avant la demence automatisee.

## Agent vs chatbot vs script

Chatbot : une reponse (ou une conversation) dans une boite. Script classique : regles fixes "si ceci alors cela". Agent : boucle but -> action -> observation -> prochaine action, avec un modele qui decide un peu.

Exemple chatbot : "ecris un mail de relance". Exemple script : "chaque lundi a 9h, envoie ce modele". Exemple agent : "regarde mes mails non lus sur les devis, resume ceux qui attendent une reponse, prepare 3 brouillons, ne rien envoyer". La derniere phrase compte : ne rien envoyer.

## Ou ca aide vraiment

Taches repetitives multi-etapes a bas risque : collecter, resumer, classer, preparer. Recherche bornee avec sources a verifier. Assistance developpeur (lire erreur, proposer patch, lancer tests - avec revue). Prep de dossier : "a partir de ces PDF, fais une grille comparative".

Lea peut laisser un agent preparer un dossier concurrent (sites publics) avant un RDV. Max peut imaginer plus tard un flux "photo + dictée -> fiche chantier" - encore mieux avec validation. Sam peut generer des variantes d'exercices a partir d'un modele, puis selectionner.

## Ou ca casse

Acces e-mail / agenda / paiements sans garde-fous. Instructions ambigues ("occupe-toi des clients mecontents"). Sites qui changent. Captchas. Jugement social. Hallucination + action = erreur executee. Boucles infinies qui consomment du temps et de l'argent.

Un agent sans perimetre, c'est un stagiaire avec les cles du camion.

## Cadre de securite mental

Principe du moindre privilege : acces lecture avant ecriture, brouillon avant envoi, sandbox avant production. Demande des checkpoints : "apres chaque etape, montre-moi et attends mon OK". Log ce qui a ete fait. Budget : limite de temps, d'actions, de cout.

Interdits de debutant : envoyer des mails seuls, poster seuls, modifier la compta, toucher aux notes d'eleves, acheter quoi que ce soit.

## Comment demarrer sans te bruler

1. Choisis une mission de 15 minutes, bas risque.
2. Ecris le but, les outils autorises, les interdits, le format du rapport final.
3. Lance avec supervision (tu regardes).
4. Note ou ca a derape.
5. Seulement ensuite, automatise un bout.

Si tu n'as pas d'outil "agent" sous la main, simule : fais-toi ecrire la checklist d'actions, execute-les toi-meme, garde l'habitude du brief. L'idee d'agent commence par un bon cahier des charges.

## Niveau 0, 1, 2 (pour ne pas bruler les etapes)

Niveau 0 : tu es l'agent. L'IA ecrit la checklist ; tu executes. Niveau 1 : l'IA propose des actions dans un perimetre lecture seule (resumes, tris, brouillons). Tu valides chaque envoi. Niveau 2 : quelques actions ecriture bornees (creer une note, une tache), toujours avec log et plafond. Beaucoup de debutants veulent le niveau 2 lundi. Reste au 0-1 jusqu'a ce que tes prompts et ta verif soient stables.

Lea au niveau 1 : "prepare un dossier a partir de pages publiques, ne contacte personne". Max au niveau 0 : checklist pieces detachees generee, commande humaine. Sam au niveau 1 : "genere 3 variantes d'exercice a partir de mon modele, n'envoie rien aux eleves".

## Erreur classique

Confondre demo Twitter et fiabilite metier. Ou "autonomiser" avant d'avoir des prompts et des verifications solides. Les agents amplifient tes bonnes pratiques - et tes mauvaises. Autre piege : juger l'idee entiere apres une seule demo ratee sur un site capricieux. Cadre mieux, reduis le but, reteste.

## En vrai

Ecris le brief d'un mini-agent utile a ton metier, meme fictif. Exemple Max : "A partir de notes collees, produire fiche chantier + liste pieces + questions au client. Ne jamais inventer une reference constructeur. Sortie en 3 blocs." Tu n'as pas besoin de le brancher demain. Tu as besoin de savoir le commander.

## A toi

Complete : But / Outils autorises / Interdits / Preuve de fin / Validation humaine a quelle etape. Une demi-page. C'est ton permis de conduire agent - version papier.
