# Chapitre 8 - Multimodal : image, audio, video

Multimodal, en mots simples, veut dire : l'outil accepte ou produit plusieurs formes de media, pas seulement du texte. Tu colles une photo et tu demandes ce qu'elle montre. Tu dictes un message. Tu generes une image a partir d'une description. Tu transcris une reunion. Tu resumes une video. En 2026, beaucoup d'assistants melangent deja ces gestes dans le meme fil. C'est pratique. Ce n'est pas magique.

Chez DanielCraft, on traite le multimodal comme un accelerateur de comprehension et de brouillon visuel ou oral - jamais comme une preuve legale automatique, jamais comme un remplacement d'une photo reelle quand la realite compte.

## Image en entree : decrire, extraire, expliquer

Tu photographies un tableau blanc, une etiquette, un schema. Tu demandes une transcription, un resume, une checklist. Utile pour Max qui capture une note de chantier, pour Lea qui photographie un wireframe papier, pour Sam qui scanne un exercice. Limites : mauvaise photo, ecriture illisible, chiffres mal lus, confusion entre produits proches. Verifie toujours les nombres et les noms propres.

Ne colle pas une piece d'identite, un dossier medical complet, ou une fiche paie complete dans un outil grand public "pour voir". Anonymise. Recadre. Demande-toi si un humain non autorise pourrait nuire avec cette image.

## Image en sortie : generer un visuel

Tu decris une ambiance, un style, un sujet. Le modele propose une image. Utile pour moodboards, illustrations de blog non critiques, idees de mise en page, variantes de logo tres en amont. Dangereux ou fragile pour : fausse photo de produit vendu, deepfake, imitation d'un artiste vivant sans cadre clair, visuel "temoignage" invente. Lea peut generer une direction artistique ; elle ne publie pas une fausse photo de boutique comme si c'etait la sienne.

## Audio : dicter, transcrire, resumer

La dictée accelere la prise de notes. La transcription transforme une reunion en texte. Le resume tire des actions. Cadre : qui a consenti a l'enregistrement ? Ou vont les fichiers ? Combien de temps sont-ils gardes ? Pour une reunion d'equipe interne avec accord, souvent OK avec outil adapte. Pour un client qui n'a pas ete informe, pause. Sam peut transcrire un oral d'entrainement ; il ne diffuse pas la voix d'un eleve sans cadre.

## Video : encore plus lourd

Generer ou editer de la video coute cher en calcul, en temps, en risques de fake. Pour un debutant, l'usage sain est souvent : resumer une video existante dont tu as le droit, extraire des idees, preparer un script - pas fabriquer une fausse interview. Les outils evoluent vite ; la prudence humaine doit rester stable.

## Brief multimodal utile

Comme pour le texte : sois precis. "Decris cette image pour un devis plomberie : liste les elements visibles, signale ce qui est illisible, n'invente aucune dimension." Ou : "Transcris cet audio, marque [inaudible] si besoin, puis donne 5 actions." Le meme squelette role / tache / contraintes / format s'applique.

## Erreur classique

Croire que "l'IA a vu la photo donc c'est exact". Ou publier un visuel genere comme preuve sociale. Ou dicter des secrets clients dans le metro via un assistant cloud. Autre piege : juger un outil multimodal sur une image parfaite de demo, puis l'utiliser sur des photos floues reelles sans controle.

## En vrai

Prends une image non sensible de ton travail (schema, capture d'ecran anonyme, objet). Demande une description stricte. Corrige les erreurs a la main. Note ce que le modele rate systematiquement chez toi.

## A toi

Ecris ta regle multimodal : ce que tu acceptes (dictee, moodboard, transcription interne...) et ce que tu refuses (piece ID, fausse photo produit, voix d'autrui sans accord).
## Qualite d'entree = qualite de sortie

Photo floue, contre-jour, document plie : la description souffrira. Audio avec tele et micro loin : la transcription souffrira. Avant d'accuser le modele, ameliore la capture. Puis demande explicitement de signaler les zones incertains. Un "je vois 12, peut-etre 18" est plus utile qu'un "18" invente.

## Droits et deepfakes

Generer l'image d'une personne reelle, cloner une voix, fabriquer une video d'un evenement invente : zone legale et ethique sensible. Par defaut, ne le fais pas sans cadre clair et consentements. Pour une marque, prefere des visuels clairement illustres / fictifs quand ce n'est pas une photo reelle, et dis-le si besoin. La confiance se construit lentement et se perd vite.

## Scene de terrain (developpee)

Imagine une matinee ordinaire. Tu ouvres l'outil, tu as une tache, tu as dix minutes. Sans methode, tu tapes une phrase vague, tu obtiens un texte poli, tu colles, tu regrettes. Avec methode, tu prends deux minutes pour cadrer : but, public, contraintes, faits, interdits. Tu generes. Tu verifies les faits critiques. Tu corriges le ton. Tu ranges le prompt si ca a marche. Le resultat n'est pas seulement "plus joli". Il est plus sur, plus reutilisable, plus respectueux des gens dont les donnees pourraient trainer dans le fil.

Cette difference se voit peu le premier jour. Elle se voit au bout d'un mois, quand tu as une bibliotheque de huit prompts, une charte donnees, une grille d'evaluation, et zero incident majeur. C'est ca que ce chapitre prepare : pas l'effet wow, l'effet fiable.

## Pieges subtils

Le piege du perfectionnisme : retoucher le prompt une heure pour un mail de huit lignes. Le piege de la paresse : ne jamais retoucher. Le piege de la nouveaute : changer d'outil chaque semaine. Le piege de la peur : ne rien automatiser jamais, meme le bas risque. Le juste milieu se construit en ecrivant tes regles personnelles et en les testant. Ce livre te donne des regles candidates ; toi tu les adaptes a ton metier, ton risque, ton budget.

## Lien avec le reste du livre

Ce que tu lis ici se branche sur les tokens (ne noie pas), le contexte (un fil propre), la temperature (strict ou creatif), le system prompt (cadre durable), les hallucinations (verifier), le multimodal (entree propre), le RAG (documents ranges), les agents (freins), l'evaluation (grille), les couts (ordre de grandeur), la securite (2FA, secrets). Tu n'as pas a tout activer d'un coup. Active une brique, solidifie, ajoute.

## Pour aller plus loin sans te perdre

Tu n'as pas a tout maitriser d'un coup. Reviens a ce chapitre quand tu butes sur un cas reel. Relis l'erreur classique. Refais le "A toi". Chez DanielCraft, on prefere trois relectures actives a une lecture passive de vingt pages. Si un paragraphe te semble encore flou, reformule-le a voix haute avec ton propre exemple. Des que ca passe a l'oral, c'est que c'est entre. Ensuite seulement, passe au chapitre suivant. Cette discipline lente cree une competence rapide sur la duree - le contraire du binge de tutos oublies le lendemain.
