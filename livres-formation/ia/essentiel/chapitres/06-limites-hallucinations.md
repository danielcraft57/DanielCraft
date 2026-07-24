# Chapitre 6 - Limites et hallucinations : l'IA peut inventer

Une hallucination, en langage IA, ce n'est pas quand ton ecran scintille. C'est quand le modele invente des faits, des sources, des chiffres, des citations, des fonctionnalites logicielles - souvent avec un ton tres sur de lui. C'est le piege numero un pour les debutants, parce que la phrase sonne juste. Fluide. Professionnelle. Fausse.

Chez DanielCraft, on le dit cash : un LLM est un generateur de suite plausible, pas un notaire. Tant que tu traites ses reponses comme des hypotheses a verifier, tu es en securite relative. Des que tu signes sans lire, tu prends le risque a ta place.

## Pourquoi ca arrive

Le modele a ete entraine a continuer le texte de facon coherente. Quand tu demandes une reference precise, un prix de piece, une jurisprudence, un numero d'article de loi, il peut "completer" comme un improvisateur. Il n'a pas toujours un mecanisme interne qui dit "je ne sais pas" aussi fort qu'un humain prudent. Les produits ajoutent des garde-fous, de la recherche web, des refus - utiles, pas parfaits.

Les hallucinations augmentent quand tu demandes des details rares, des faits tres recents, des chiffres exacts, des listes de sources, ou quand tu pousses le mode creatif sur un sujet qui devrait etre factuel. Elles diminuent quand tu fournis le materiel, quand tu limites le perimetre, quand tu demandes l'aveu d'incertitude, et quand tu verifies ailleurs.

## Autres limites importantes

Fenetre de contexte : oubli du debut, confusion entre deux sujets. Connaissances coupees a une date (selon l'outil). Biais : stereotypes herites des donnees. Flatterie : le modele veut souvent "aider" et te dire oui. Style generique. Faiblesse sur le raisonnement multi-etapes non verifie. Cout et latence si tu abuses. Et l'illusion de competence : plus c'est bien ecrit, plus tu baisses la garde.

## Comment reduire les inventions

Fournis tes faits. Demande "si tu ne sais pas, ecris INCONNU". Interdis les fausses sources. Demande des hypotheses separees des faits. Pour tout chiffre critique, ouvre une source humaine ou officielle. Pour le code, execute et teste. Pour un mail client, relis les promesses. Pour un contenu medical, juridique, fiscal : expert humain, point.

Lea demande un plan SEO, puis verifie les pretentions "Google adore X en 2026" sur des sources serieuses. Max ne laisse jamais l'IA inventer un prix de piece : il colle son tarif. Sam fait generer un exercice, puis le resout lui-meme avant de le donner aux eleves.

## Evaluer une reponse (idee simple)

Avant d'envoyer, pose quatre questions : Est-ce fidele a mon brief ? Y a-t-il des faits inventes ? Le ton me ressemble-t-il ? Est-ce que je signerais ca demain matin devant un client difficile ? Si une reponse est non, tu iteres ou tu jette. On approfondira l'evaluation plus loin, mais ce mini-filtre sauve deja des galeres.

## Erreur classique

Demander "cite tes sources" et se contenter de liens qui ont l'air vrais. Ou regenerer dix fois jusqu'a ce que ca sonne joli, sans verifier. Ou croire que "le modele premium n'hallucine jamais". Il hallucine moins souvent sur certains taches - pas jamais.

## En vrai

Demande a ton outil une reference bibliographique precise sur un sujet niche que tu connais un peu. Verifie chaque titre. Note le taux de solidite. Puis refais la meme demande en mode : "n'invente aucune reference ; si tu n'en as pas, dis-le et propose comment chercher". Compare.

## A toi

Choisis une tache a risque dans ton metier (prix, delai, conseil sensible). Ecris la regle personnelle : "l'IA peut ebaucher X, jamais signer Y sans verification Z". Garde-la visible.
## Typologie rapide des inventions

Invention de source (article, loi, page web). Invention de chiffre (prix, statistique, date). Invention de fonctionnalite logicielle ("dans Word tu cliques sur..."). Invention de procedure interne ("votre entreprise fait deja..."). Confusion d'homonymes. Melange de deux sujets proches. Extrapolation confiante hors donnees. Chacune a son antidote : fournir le materiel, interdire, verifier, limiter le perimetre.

## Quand le modele refuse

Parfois l'outil refuse une demande sensible. Ce n'est pas toujours absurde. Parfois le refus est trop large, parfois trop etroit. Contourne ethiquement : reformule un usage legitime et precis, sans chercher a "jailbreaker" pour le sport. Si ton usage pro est legitime et bloque, change d'outil ou de canal selon ta politique. Le refus n'est pas une preuve que ta demande etait mauvaise, ni une preuve que tu dois ruser.

## Culture d'equipe anti-hallucination

Interdiction de coller une reponse non lue dans un ticket client. Obligation de sourcer les faits critiques hors modele. Ritual de double lecture sur les contenus a enjeu. C'est moins glamour qu'une demo. Ca evite les crises.

## Scene de terrain (developpee)

Imagine une matinee ordinaire. Tu ouvres l'outil, tu as une tache, tu as dix minutes. Sans methode, tu tapes une phrase vague, tu obtiens un texte poli, tu colles, tu regrettes. Avec methode, tu prends deux minutes pour cadrer : but, public, contraintes, faits, interdits. Tu generes. Tu verifies les faits critiques. Tu corriges le ton. Tu ranges le prompt si ca a marche. Le resultat n'est pas seulement "plus joli". Il est plus sur, plus reutilisable, plus respectueux des gens dont les donnees pourraient trainer dans le fil.

Cette difference se voit peu le premier jour. Elle se voit au bout d'un mois, quand tu as une bibliotheque de huit prompts, une charte donnees, une grille d'evaluation, et zero incident majeur. C'est ca que ce chapitre prepare : pas l'effet wow, l'effet fiable.

## Pieges subtils

Le piege du perfectionnisme : retoucher le prompt une heure pour un mail de huit lignes. Le piege de la paresse : ne jamais retoucher. Le piege de la nouveaute : changer d'outil chaque semaine. Le piege de la peur : ne rien automatiser jamais, meme le bas risque. Le juste milieu se construit en ecrivant tes regles personnelles et en les testant. Ce livre te donne des regles candidates ; toi tu les adaptes a ton metier, ton risque, ton budget.

## Lien avec le reste du livre

Ce que tu lis ici se branche sur les tokens (ne noie pas), le contexte (un fil propre), la temperature (strict ou creatif), le system prompt (cadre durable), les hallucinations (verifier), le multimodal (entree propre), le RAG (documents ranges), les agents (freins), l'evaluation (grille), les couts (ordre de grandeur), la securite (2FA, secrets). Tu n'as pas a tout activer d'un coup. Active une brique, solidifie, ajoute.

## Pour aller plus loin sans te perdre

Tu n'as pas a tout maitriser d'un coup. Reviens a ce chapitre quand tu butes sur un cas reel. Relis l'erreur classique. Refais le "A toi". Chez DanielCraft, on prefere trois relectures actives a une lecture passive de vingt pages. Si un paragraphe te semble encore flou, reformule-le a voix haute avec ton propre exemple. Des que ca passe a l'oral, c'est que c'est entre. Ensuite seulement, passe au chapitre suivant. Cette discipline lente cree une competence rapide sur la duree - le contraire du binge de tutos oublies le lendemain.
