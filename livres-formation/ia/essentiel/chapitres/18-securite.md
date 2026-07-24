# Chapitre 18 - Securite : comptes, secrets, pouvoirs

La securite IA debutant n'est pas de la paranoia. C'est de l'hygiene. Tu manipules des textes qui peuvent contenir des secrets, des acces, des pouvoirs d'action. Un bon brief ne suffit pas si ton compte est partage ou si un agent peut envoyer seul.

## Comptes et acces

Mot de passe unique et long. Double authentification. Pas de compte "equipe" avec le meme login pour six personnes si tu peux eviter. Separe perso / pro quand c'est possible. Revoke les sessions perdues. Si tu quittes un outil, exporte ce qui compte, puis ferme proprement.

## Secrets

Ne colle jamais de cles API, mots de passe, tokens d'acces, seeds crypto, ou extraits de bases clients dans le chat "pour debugger". Si tu developpes, utilise des variables d'environnement et des coffres. Si tu n'es pas tech : ne mets pas ces chaines dans un prompt, point. Un modele peut echo ce que tu as colle dans des logs ou des historiques.

## Donnees sensibles

Pieces d'identite, dossiers sante, donnees scolaires nominatives, secrets d'affaires, conversations privees de tiers : regarde le chapitre ethique, puis ajoute la couche technique. Outil adapte, options de retention, desactivation de l'usage pour entrainement si disponible et necessaire, chiffrement et bonnes pratiques du poste (verrouillage ecran, pas de captures partagees a la legere).

## Pouvoirs limites pour les agents

Lecture seule d'abord. Brouillons ensuite. Envoi / publication / paiement seulement avec validation humaine explicite. Journalise. Fixe un budget. Interdis des domaines d'action. Un agent sans perimetre est une faille autonome.

## Ingenierie sociale et arnaques

L'IA ecrit de beaux mails de phishing. Mele a la voix clonee ou a un faux site, ca devient persuasif. Verifie les demandes d'argent et les changements d'IBAN par un second canal. Ne fais pas confiance a un style "parfaitement professionnel". Les attaquants aiment le parfait.

## Erreur classique

Partager son ecran en visio avec un chat ouvert plein de secrets. Ou laisser Copilot / assistant actif sur un depot qui contient des .env. Ou croire que "c'est interne donc safe" sans regarder qui a acces a l'espace workspace.

## En vrai

Passe 15 minutes : active 2FA partout ou c'est possible, nettoie les sessions, cherche une donnee sensible dans tes historiques, supprime ou anonymise. Petite session, gros soulagement.

## A toi

Checklist securite perso a 8 cases, cochee aujourd'hui. Date la prochaine revue (dans 90 jours).
## Incident : que faire

Tu as colle un secret par erreur. Revoque la cle / change le mot de passe. Purge l'historique si l'outil le permet. Previen qui de droit selon ta politique. Note l'incident et le correctif (checklist). La honte retarde ; la revocation protege. Mieux vaut un signalement interne rapide qu'une fuite longue.

## Scene de terrain (developpee)

Imagine une matinee ordinaire. Tu ouvres l'outil, tu as une tache, tu as dix minutes. Sans methode, tu tapes une phrase vague, tu obtiens un texte poli, tu colles, tu regrettes. Avec methode, tu prends deux minutes pour cadrer : but, public, contraintes, faits, interdits. Tu generes. Tu verifies les faits critiques. Tu corriges le ton. Tu ranges le prompt si ca a marche. Le resultat n'est pas seulement "plus joli". Il est plus sur, plus reutilisable, plus respectueux des gens dont les donnees pourraient trainer dans le fil.

Cette difference se voit peu le premier jour. Elle se voit au bout d'un mois, quand tu as une bibliotheque de huit prompts, une charte donnees, une grille d'evaluation, et zero incident majeur. C'est ca que ce chapitre prepare : pas l'effet wow, l'effet fiable.

## Pieges subtils

Le piege du perfectionnisme : retoucher le prompt une heure pour un mail de huit lignes. Le piege de la paresse : ne jamais retoucher. Le piege de la nouveaute : changer d'outil chaque semaine. Le piege de la peur : ne rien automatiser jamais, meme le bas risque. Le juste milieu se construit en ecrivant tes regles personnelles et en les testant. Ce livre te donne des regles candidates ; toi tu les adaptes a ton metier, ton risque, ton budget.

## Lien avec le reste du livre

Ce que tu lis ici se branche sur les tokens (ne noie pas), le contexte (un fil propre), la temperature (strict ou creatif), le system prompt (cadre durable), les hallucinations (verifier), le multimodal (entree propre), le RAG (documents ranges), les agents (freins), l'evaluation (grille), les couts (ordre de grandeur), la securite (2FA, secrets). Tu n'as pas a tout activer d'un coup. Active une brique, solidifie, ajoute.

## Pour aller plus loin sans te perdre

Tu n'as pas a tout maitriser d'un coup. Reviens a ce chapitre quand tu butes sur un cas reel. Relis l'erreur classique. Refais le "A toi". Chez DanielCraft, on prefere trois relectures actives a une lecture passive de vingt pages. Si un paragraphe te semble encore flou, reformule-le a voix haute avec ton propre exemple. Des que ca passe a l'oral, c'est que c'est entre. Ensuite seulement, passe au chapitre suivant. Cette discipline lente cree une competence rapide sur la duree - le contraire du binge de tutos oublies le lendemain.
