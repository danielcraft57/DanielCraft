# Chapitre 12 - Mini-projet : un usage IA utile et verifie

Assez de theorie. On construit un usage complet, petit, reel, verifiable. Objectif : partir d'une tache fatigante, produire un livrable avec l'IA, appliquer les gardes (brief, limites, donnees, relecture), et pouvoir le reutiliser la semaine prochaine.

## Etape 1 - Choisir la tache

Reprends ta note du chapitre 1. Choisis une tache basse risque : mail type, page de presentation, fiche produit, plan de seance, checklist d'entretien, resume de process. Evite pour ce mini-projet : conseil medical, juridique, fiscal critique, envoi automatique a des clients, generation de fausse preuve.

## Etape 2 - Preparer le brief

Ecris ton prompt signature + le brief de tache : role, public, contraintes, format, faits fournis, interdits. Anonymise les donnees. Decide du mode : strict ou creatif. Decide du critere de succes ("je peux envoyer apres 10 minutes de relecture").

## Etape 3 - Produire

Lance le prompt. Si l'outil le permet, colle aussi tes instructions persistantes (system). Itere au plus trois fois avec des demandes precises. Si ca part en vrille, nouveau fil + brief reconstitue.

## Etape 4 - Evaluer

Checklist : fidelite au brief, faits verifies, ton OK, pas de promesse inventee, pas de donnee sensible residuelle, longueur adaptee, tu signerais. Note les hallucinations eventuelles. Corrige a la main. Le livrable final est le tien, pas "celui de l'IA".

## Etape 5 - Industrialiser legerement

Range le prompt, le livrable modele, et trois lecons dans un dossier. Donne un nom clair. Si c'est un mail type, laisse des zones [NOM], [DATE], [PRIX]. Demain, tu gagnes dix minutes. Dans un mois, des heures.

## Variante avancee (optionnelle)

Si tu as des documents internes non sensibles, simule un mini-RAG : extrait utile colle dans le prompt, consigne "reponds uniquement a partir de cet extrait". Compare avec une reponse sans extrait. Tu verras souvent la difference de solidite.

## Erreur classique

Choisir un projet trop large ("refondre tout mon business"). Ou s'arreter au premier jet "parce que c'est fluide". Ou ne pas ranger le prompt : tu recommenceras de zero a chaque fois.

## En vrai

Fais le mini-projet aujourd'hui, meme imparfait. Un usage fini bat dix intentions.

## A toi

Livre attendu : (1) prompt final, (2) livrable relu, (3) 5 lignes de retrospective : ce qui a marche, ce qui a trompe, ce que tu changes la prochaine fois.
## Criteres de reussite du mini-projet

Le livrable a ete utilise (envoye, publie en interne, enseigne) ou est pret a l'etre. Le prompt est range et reutilisable. Aucune donnee sensible n'a fuité dans un outil inadapte. Tu peux expliquer en deux minutes ce que l'IA a fait et ce que tu as corrige. Tu as une lecon ecrite. Si ces cinq points sont verts, le mini-projet est reussi - meme si le texte n'est pas litteraire.

## Scene de terrain (developpee)

Imagine une matinee ordinaire. Tu ouvres l'outil, tu as une tache, tu as dix minutes. Sans methode, tu tapes une phrase vague, tu obtiens un texte poli, tu colles, tu regrettes. Avec methode, tu prends deux minutes pour cadrer : but, public, contraintes, faits, interdits. Tu generes. Tu verifies les faits critiques. Tu corriges le ton. Tu ranges le prompt si ca a marche. Le resultat n'est pas seulement "plus joli". Il est plus sur, plus reutilisable, plus respectueux des gens dont les donnees pourraient trainer dans le fil.

Cette difference se voit peu le premier jour. Elle se voit au bout d'un mois, quand tu as une bibliotheque de huit prompts, une charte donnees, une grille d'evaluation, et zero incident majeur. C'est ca que ce chapitre prepare : pas l'effet wow, l'effet fiable.

## Pieges subtils

Le piege du perfectionnisme : retoucher le prompt une heure pour un mail de huit lignes. Le piege de la paresse : ne jamais retoucher. Le piege de la nouveaute : changer d'outil chaque semaine. Le piege de la peur : ne rien automatiser jamais, meme le bas risque. Le juste milieu se construit en ecrivant tes regles personnelles et en les testant. Ce livre te donne des regles candidates ; toi tu les adaptes a ton metier, ton risque, ton budget.

## Lien avec le reste du livre

Ce que tu lis ici se branche sur les tokens (ne noie pas), le contexte (un fil propre), la temperature (strict ou creatif), le system prompt (cadre durable), les hallucinations (verifier), le multimodal (entree propre), le RAG (documents ranges), les agents (freins), l'evaluation (grille), les couts (ordre de grandeur), la securite (2FA, secrets). Tu n'as pas a tout activer d'un coup. Active une brique, solidifie, ajoute.

## Pour aller plus loin sans te perdre

Tu n'as pas a tout maitriser d'un coup. Reviens a ce chapitre quand tu butes sur un cas reel. Relis l'erreur classique. Refais le "A toi". Chez DanielCraft, on prefere trois relectures actives a une lecture passive de vingt pages. Si un paragraphe te semble encore flou, reformule-le a voix haute avec ton propre exemple. Des que ca passe a l'oral, c'est que c'est entre. Ensuite seulement, passe au chapitre suivant. Cette discipline lente cree une competence rapide sur la duree - le contraire du binge de tutos oublies le lendemain.
