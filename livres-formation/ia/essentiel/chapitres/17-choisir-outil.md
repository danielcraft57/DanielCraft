# Chapitre 17 - Choisir un outil et comprendre les couts

Choisir un outil IA, ce n'est pas epouser une marque. C'est matcher un besoin, des contraintes de donnees, un budget, et une habitude de travail. Les noms changent. Tes criteres peuvent rester stables.

## Criteres utiles

Qualite sur TES prompts (pas sur une demo marketing). Respect de tes contraintes de donnees (training, retention, options pro). Integration (mail, docs, IDE, mobile). Limites de contexte. Multimodal si besoin. Possibilite d'instructions persistantes. Prix clair. Support / statut (compte pro, SSO, facture). Pour un artisan solo, un bon chat suffit souvent. Pour une equipe, les questions admin et RGPD montent.

## L'idee des couts API

En interface grand public, tu paies souvent un abonnement mensuel : un forfait d'usage. En API (quand un developpeur branche le modele dans une appli), on facture souvent a l'usage : tokens en entree, tokens en sortie, parfois le type de modele, parfois des outils (vision, recherche). Plus tu envoies de contexte, plus tu paies. Plus tu demandes des reponses longues, plus tu paies. Un agent qui boucle vingt fois peut couter cher sans que tu t'en rendes compte.

Meme si tu ne codes pas, comprendre ca t'aide : sois concis, attache l'extrait utile, evite les regenerations inutiles, choisis le modele "assez bon" pour la tache (pas toujours le plus gros pour reformuler un SMS). Lea a appris a couper ses PDF avant de les coller. Max a appris a ne pas demander un roman pour un mail. Sam a appris a limiter les variantes a un nombre utile.

## Protocole de choix en une heure

1) Ecris 5 prompts types de ton metier. 2) Teste-les sur 1 a 2 outils max. 3) Note avec ta grille d'evaluation. 4) Verifie options donnees / prix. 5) Choisis pour un mois. 6) Reevalue. Pas besoin de cinq abonnements le jour 1.

## Quand payer

Paye quand le free te freine vraiment (limites, confidentialite, qualite, integration), pas par peur de manquer. Un abonnement inutile est un cout. Un outil qui te fait gagner deux heures semaine a un prix raisonnable est un investissement. Fais le calcul simple : heures gagnees x ta valeur temps vs prix.

## Erreur classique

Suivre chaque hype la semaine de sa sortie. Ou choisir uniquement sur "c'est gratuit". Gratuit peut etre cher en donnees et en temps. Autre piege : rester sur un outil mediocre par habitude sans jamais retester tes 5 prompts ailleurs.

## En vrai

Fais le protocole sur une heure cette semaine, meme avec un seul concurrent. Ecris la decision et la date de reevaluation (dans 30 jours).

## A toi

Tableau simple : outil, prix, point fort, point faible, verdict 30 jours. Une page.
## Lire une grille tarifaire API sans paniquer

Tu verras souvent un prix pour 1 million de tokens entree, un autre pour la sortie, parfois un modele "mini" moins cher, un modele "large" plus cher, des options vision. Fais un calcul d'ordre de grandeur : un prompt de 1 000 tokens + reponse de 500 tokens, combien de fois par jour, fois 30. Compare a un forfait chat. Ajoute ton temps. Choisis. Recalcule dans trente jours avec du reel, pas de la science-fiction.

## Scene de terrain (developpee)

Imagine une matinee ordinaire. Tu ouvres l'outil, tu as une tache, tu as dix minutes. Sans methode, tu tapes une phrase vague, tu obtiens un texte poli, tu colles, tu regrettes. Avec methode, tu prends deux minutes pour cadrer : but, public, contraintes, faits, interdits. Tu generes. Tu verifies les faits critiques. Tu corriges le ton. Tu ranges le prompt si ca a marche. Le resultat n'est pas seulement "plus joli". Il est plus sur, plus reutilisable, plus respectueux des gens dont les donnees pourraient trainer dans le fil.

Cette difference se voit peu le premier jour. Elle se voit au bout d'un mois, quand tu as une bibliotheque de huit prompts, une charte donnees, une grille d'evaluation, et zero incident majeur. C'est ca que ce chapitre prepare : pas l'effet wow, l'effet fiable.

## Pieges subtils

Le piege du perfectionnisme : retoucher le prompt une heure pour un mail de huit lignes. Le piege de la paresse : ne jamais retoucher. Le piege de la nouveaute : changer d'outil chaque semaine. Le piege de la peur : ne rien automatiser jamais, meme le bas risque. Le juste milieu se construit en ecrivant tes regles personnelles et en les testant. Ce livre te donne des regles candidates ; toi tu les adaptes a ton metier, ton risque, ton budget.

## Lien avec le reste du livre

Ce que tu lis ici se branche sur les tokens (ne noie pas), le contexte (un fil propre), la temperature (strict ou creatif), le system prompt (cadre durable), les hallucinations (verifier), le multimodal (entree propre), le RAG (documents ranges), les agents (freins), l'evaluation (grille), les couts (ordre de grandeur), la securite (2FA, secrets). Tu n'as pas a tout activer d'un coup. Active une brique, solidifie, ajoute.

## Pour aller plus loin sans te perdre

Tu n'as pas a tout maitriser d'un coup. Reviens a ce chapitre quand tu butes sur un cas reel. Relis l'erreur classique. Refais le "A toi". Chez DanielCraft, on prefere trois relectures actives a une lecture passive de vingt pages. Si un paragraphe te semble encore flou, reformule-le a voix haute avec ton propre exemple. Des que ca passe a l'oral, c'est que c'est entre. Ensuite seulement, passe au chapitre suivant. Cette discipline lente cree une competence rapide sur la duree - le contraire du binge de tutos oublies le lendemain.
