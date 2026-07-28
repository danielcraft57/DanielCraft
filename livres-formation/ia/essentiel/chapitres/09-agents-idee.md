# Chapitre 9 - RAG et agents : documents et actions

Deux idees changent le niveau au-dessus du simple chat : le **RAG** et les **agents**. Tu n'as pas besoin de les implementer demain. Tu as besoin de comprendre ce qu'elles promettent, et ce qu'elles cassent si on les lache sans cadre.

:::retenir
RAG = repondre avec tes documents recherches. Agent = enchaîner des actions, toujours avec freins humains.
:::

## RAG : brancher le modele sur tes documents

RAG veut dire Retrieval Augmented Generation. En francais simple : avant de repondre, le systeme cherche des morceaux pertinents dans une base (tes PDF, ton wiki, ta FAQ), puis demande au **LLM** de repondre en s'appuyant sur ces extraits. L'idee : moins d'invention sur ton catalogue, tes procedures, tes tarifs - parce que la reponse est "augmentee" par du contenu que tu controles.

Ca ne rend pas le modele infaillible. Si la recherche ramene le mauvais paragraphe, la reponse sera belle et fausse. Si tes documents sont pourris ou obsoletes, le RAG amplifie le pourri. Si tu ne cites pas les extraits, tu ne peux pas verifier. Un bon usage RAG montre ses sources internes : "d'apres la fiche tarif 2026, page 2...".

Lea reve d'un assistant qui connait ses modeles de proposition. Max voudrait un outil qui lit sa bibliotheque de fiches d'entretien. Sam voudrait interroger son cours sans halluciner le programme. Dans les trois cas, le travail invisible est le meme : ranger des documents propres, a jour, avec des droits d'acces clairs.

:::astuce
Sans outil special, simule un RAG : copie l'extrait utile, demande "reponds uniquement a partir de cet extrait, cite les phrases".
:::

## Agents : enchaîner des actions vers un but

Un agent, en idee simple, c'est un systeme qui ne se contente pas de repondre : il planifie, appelle des outils (recherche, calendrier, email, navigateur, base de donnees), observe le resultat, continue. Exemple : "prepare un dossier de veille sur X, resume 5 articles, propose un mail". Puissant. Aussi dangereux : un agent mal cadre peut envoyer un mail, modifier un fichier, acheter, publier.

Chez DanielCraft, la regle debutant est dure : pas d'agent avec pouvoir d'envoi autonome tant que tu n'as pas de validations humaines sur les etapes critiques. L'agent propose ; toi tu valides ; ensuite seulement l'action part. Les demos marketing sautent souvent cette etape. La vraie vie ne devrait pas.

## Comment cadrer un agent (checklist mentale)

But clair. Perimetre etroit. Outils autorises / interdits. Budget (temps, argent, **tokens**). Criteres de succes. Points de **validation humaine**. Journal de ce qu'il a fait. Plan de secours si ca part en vrille. Sans ca, tu as un stagiaire avec les cles de la boite et zero briefing.

:::attention
Un "GPT custom" sans documents a jour n'est pas un RAG solide. Et un agent "utile" sans liste d'interdits devient une faille.
:::

## RAG + agents : la combo

Beaucoup de produits melangent les deux : l'agent cherche dans tes docs (RAG), redige, puis propose une action. C'est souvent l'avenir des assistants metier. Ce n'est pas une raison de brancher ton CRM entier le premier jour. Commence lecture seule. Puis proposition. Puis action sur bac a sable. Puis production avec garde-fous.

## Erreur classique

Confondre "j'ai un GPT custom" avec "j'ai un RAG solide". Un custom sans documents a jour reste un LLM generaliste deguise. Autre erreur : laisser un agent "etre utile" sans liste d'interdits. L'utilite sans frein devient une faille.

## En vrai

Sans outil special, simule un RAG humain : ouvre un de tes PDF, copie l'extrait utile dans le chat, demande une reponse "uniquement a partir de cet extrait, cite les phrases". Tu viens de comprendre l'esprit du RAG. Puis ecris les 5 regles que tu imposerais a un agent avant de lui donner acces a ta boite mail.

## A toi

Decris un usage RAG utile chez toi (quels documents ?) et un usage agent que tu refuses encore (quelle action ?). Une page max.

## Conception d'un agent en une page

But : "preparer une veille hebdo sur X". Outils : recherche web + doc interne lecture seule. Interdits : envoi email, publication, achat. Budget : 20 appels outils max. Validation : humain lit le brouillon avant diffusion. Journal : conserver les sources. Critere de succes : 5 liens verifies + resume fidele. Avec cette page, tu peux discuter avec un prestataire sans te faire vendre une boite noire.

## RAG : hygiene documentaire

Documents dates, titres clairs, versions, droits d'acces, purge des doublons, separation du brouillon et de la procedure officielle. Le RAG n'est pas un sortilege sur un Drive bordelique. C'est une lampe torche : elle eclaire ce qui est la. Si ce qui est la est faux, tu eclaireras du faux.

## Scene de terrain (developpee)

Imagine une matinee ordinaire. Tu ouvres l'outil, tu as une tache, tu as dix minutes. Sans methode, tu tapes une phrase vague, tu obtiens un texte poli, tu colles, tu regrettes. Avec methode, tu prends deux minutes pour cadrer : but, public, contraintes, faits, interdits. Tu generes. Tu verifies les faits critiques. Tu corriges le ton. Tu ranges le prompt si ca a marche. Le resultat n'est pas seulement "plus joli". Il est plus sur, plus reutilisable, plus respectueux des gens dont les donnees pourraient trainer dans le fil.

Cette difference se voit peu le premier jour. Elle se voit au bout d'un mois, quand tu as une bibliotheque de huit prompts, une charte donnees, une grille d'evaluation, et zero incident majeur. C'est ca que ce chapitre prepare : pas l'effet wow, l'effet fiable.

## Pieges subtils

Le piege du perfectionnisme : retoucher le prompt une heure pour un mail de huit lignes. Le piege de la paresse : ne jamais retoucher. Le piege de la nouveaute : changer d'outil chaque semaine. Le piege de la peur : ne rien automatiser jamais, meme le bas risque. Le juste milieu se construit en ecrivant tes regles personnelles et en les testant. Ce livre te donne des regles candidates ; toi tu les adaptes a ton metier, ton risque, ton budget.

## Lien avec le reste du livre

Ce que tu lis ici se branche sur les tokens (ne noie pas), le contexte (un fil propre), la temperature (strict ou creatif), le system prompt (cadre durable), les hallucinations (verifier), le multimodal (entree propre), le RAG (documents ranges), les agents (freins), l'evaluation (grille), les couts (ordre de grandeur), la securite (2FA, secrets). Tu n'as pas a tout activer d'un coup. Active une brique, solidifie, ajoute.

## Pour aller plus loin sans te perdre

Tu n'as pas a tout maitriser d'un coup. Reviens a ce chapitre quand tu butes sur un cas reel. Relis l'erreur classique. Refais le "A toi". Chez DanielCraft, on prefere trois relectures actives a une lecture passive de vingt pages. Si un paragraphe te semble encore flou, reformule-le a voix haute avec ton propre exemple. Des que ca passe a l'oral, c'est que c'est entre. Ensuite seulement, passe au chapitre suivant. Cette discipline lente cree une competence rapide sur la duree - le contraire du binge de tutos oublies le lendemain.
