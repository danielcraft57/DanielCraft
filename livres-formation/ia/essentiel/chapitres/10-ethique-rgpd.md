# Chapitre 10 - Ethique, RGPD et securite des donnees

L'IA mange du **contexte**. Plus tu lui donnes d'infos, plus la reponse peut etre "perso". Plus tu lui donnes d'infos, plus tu exposes des personnes. Ethique et **RGPD** ne sont pas des chapitres ennuyeux reserves aux juristes. Ce sont des reflexes de respect : **minimiser**, anonymiser, informer, securiser, assumer.

Chez DanielCraft, on pose une regle simple : si tu n'aimerais pas voir cette donnee affichee sur un ecran de metro, ne la colle pas dans un outil grand public. Et si la donnee concerne quelqu'un d'autre, la barre monte encore.

:::retenir
Si tu n'aimerais pas voir cette donnee sur un ecran de metro, ne la colle pas dans un outil grand public.
:::

## Minimiser

Tu n'as pas besoin du numero de securite sociale pour reformuler un mail. Tu n'as pas besoin de la date de naissance pour un plan de site. Tu n'as pas besoin du nom complet d'un eleve pour generer un exercice. Enleve ce qui ne sert pas. Remplace "Mme Dupont, 12 rue..." par "une cliente particuliere a Lyon". Souvent, la qualite du brief reste bonne.

## Anonymiser et pseudonymiser

**Anonymiser** vraiment est plus dur qu'on croit (un petit village + un metier rare = reidentifiability). Fais de ton mieux : enleve noms, adresses exactes, telephones, numeros de dossier. Pour un usage interne serieux, choisis des outils et des contrats adaptes - pas seulement "c'est dans le cloud donc OK".

## Bases RGPD (idee debutant)

Le RGPD encadre le traitement des donnees personnelles en Europe. Idees cles : finalite claire, minimisation, securite, droits des personnes, responsabilite. L'IA n'efface pas ca. Elle l'accentue, parce que coller un fichier dans un chat est devenu trop facile. Si tu es pro, parle a quelqu'un de competent pour ton cas. Ce livre n'est pas un conseil juridique personnalise ; c'est une boussole de prudence.

:::attention
Dire "c'est anonyme" des qu'on enleve le prenom ne suffit pas - surtout en petit village ou metier rare.
:::

## Ethique au-dela de la loi

Meme "legal", un usage peut etre moche : generer un faux avis client, cloner une voix sans accord, truquer une photo de resultat avant/apres, laisser un eleve croire qu'un devoir IA non assume est OK sans discussion. Ethique = ce que tu assumes le matin devant un miroir et devant les gens concernes. Transparence quand c'est utile. Respect quand c'est obligatoire.

## Securite des donnees (ponte vers le chapitre securite)

Mots de passe uniques, double authentification, pas de compte partage "equipe" avec le meme login, pas de collages de cles API dans le chat, choix d'outils avec options pro / retention / training opt-out quand c'est critique. On detaille plus loin. Ici, retiens le lien : ethique sans **securite** technique, c'est un voeu pieux.

## Erreur classique

Dire "c'est anonyme" des qu'on enleve le prenom. Ou "tout le monde fait ca". Ou "l'outil a une jolie page confiance donc je suis couvert". Autre piege : utiliser un compte perso gratuit pour des donnees pro sensibles parce que "c'est plus simple".

## En vrai

Ouvre ton historique de chat recent. Identifie une donnee que tu n'aurais pas du coller (meme mineure). Note la lecon. Mets en place une regle d'anonymisation pour la semaine.

## A toi

Ecris ta charte perso en 6 lignes : ce que je colle, ce que je n'y colle jamais, outils autorises, qui est informe, ou je stocke les prompts, qui valide les contenus sensibles.

## Scenarios a refuser

Coller la liste complete d'eleves pour "personnaliser". Generer un faux avis 5 etoiles. Cloner la voix du dirigeant pour un message interne "drole". Utiliser des photos de clients sans base legale pour entrainer un truc. Laisser un stagiaire brancher un agent sur la boite mail partagee sans charte. Si un scenario te met mal a l'aise avant meme l'avis juridique, c'est deja un signal.

## Transparence utile

Tu n'as pas a mettre un bandeau "IA" sur chaque virgule. Tu as a etre honnete quand ca compte : devoir evalue, contenu journalistique sensible, decision qui affecte quelqu'un, engagement contractuel. La transparence n'est pas un gadget ; c'est une maintenance de confiance.

:::astuce
Ecris ta charte perso en 6 lignes et colle-la la ou tu ouvres ton outil - avant le prochain collage.
:::

## Scene de terrain (developpee)

Imagine une matinee ordinaire. Tu ouvres l'outil, tu as une tache, tu as dix minutes. Sans methode, tu tapes une phrase vague, tu obtiens un texte poli, tu colles, tu regrettes. Avec methode, tu prends deux minutes pour cadrer : but, public, contraintes, faits, interdits. Tu generes. Tu verifies les faits critiques. Tu corriges le ton. Tu ranges le prompt si ca a marche. Le resultat n'est pas seulement "plus joli". Il est plus sur, plus reutilisable, plus respectueux des gens dont les donnees pourraient trainer dans le fil.

Cette difference se voit peu le premier jour. Elle se voit au bout d'un mois, quand tu as une bibliotheque de huit prompts, une charte donnees, une grille d'evaluation, et zero incident majeur. C'est ca que ce chapitre prepare : pas l'effet wow, l'effet fiable.

## Pieges subtils

Le piege du perfectionnisme : retoucher le prompt une heure pour un mail de huit lignes. Le piege de la paresse : ne jamais retoucher. Le piege de la nouveaute : changer d'outil chaque semaine. Le piege de la peur : ne rien automatiser jamais, meme le bas risque. Le juste milieu se construit en ecrivant tes regles personnelles et en les testant. Ce livre te donne des regles candidates ; toi tu les adaptes a ton metier, ton risque, ton budget.

## Lien avec le reste du livre

Ce que tu lis ici se branche sur les tokens (ne noie pas), le contexte (un fil propre), la temperature (strict ou creatif), le system prompt (cadre durable), les hallucinations (verifier), le multimodal (entree propre), le RAG (documents ranges), les agents (freins), l'evaluation (grille), les couts (ordre de grandeur), la securite (2FA, secrets). Tu n'as pas a tout activer d'un coup. Active une brique, solidifie, ajoute.

## Pour aller plus loin sans te perdre

Tu n'as pas a tout maitriser d'un coup. Reviens a ce chapitre quand tu butes sur un cas reel. Relis l'erreur classique. Refais le "A toi". Chez DanielCraft, on prefere trois relectures actives a une lecture passive de vingt pages. Si un paragraphe te semble encore flou, reformule-le a voix haute avec ton propre exemple. Des que ca passe a l'oral, c'est que c'est entre. Ensuite seulement, passe au chapitre suivant. Cette discipline lente cree une competence rapide sur la duree - le contraire du binge de tutos oublies le lendemain.
