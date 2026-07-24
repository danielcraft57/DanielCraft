# Chapitre 1 - Salut, c'est quoi l'IA generative ?

L'intelligence artificielle generative, ce n'est pas un robot qui "pense" comme toi. Ce n'est pas non plus de la magie noire cachee dans un nuage. C'est une famille d'outils informatiques capables de produire du texte, des images, du son, du code, parfois de la video, a partir d'une demande que tu formules. En 2026, quand quelqu'un dit "j'ai utilise l'IA", il parle le plus souvent d'un assistant conversationnel : tu ecris, il repond. Derriere, il y a des modeles entraines sur d'enormes quantites de donnees. Pour toi, le geste reste simple : poser une question utile, lire, verifier, garder ce qui sert.

Chez DanielCraft, on aime une image nette. L'IA generative, c'est un stagiaire ultra rapide qui a lu beaucoup de choses, qui n'a pas de jugement moral propre, qui invente parfois avec assurance, et qui travaille mieux quand tu lui donnes un brief clair. Tu restes le responsable. Lui, il accelere. Si tu confonds vitesse et verite, tu te fais avoir. Si tu gardes le pilotage, tu gagnes du temps sans perdre ta credibilite.

## Ce que ce n'est pas

Ce n'est pas une conscience. Ca ne "comprend" pas comme un humain, meme si les phrases sonnent humaines. Ce n'est pas une source de verite automatique. Ce n'est pas un remplacant de ton metier du jour au lendemain. Et ce n'est surtout pas une excuse pour coller un texte non relu a un client, a un eleve, a un juge, ou a un patient.

Ce n'est pas non plus "un seul produit". ChatGPT, Claude, Gemini, Copilot, Mistral, Midjourney, des assistants dans Word, dans ton telephone, dans ton editeur de code : meme famille large, usages differents. On va les demeler sans jargon opaque. Tu n'as pas besoin de devenir chercheur. Tu as besoin de devenir un bon pilote.

## Image mentale

Tu as une tache. Tu as des contraintes : temps, ton, public, regles, budget. L'IA propose des pistes. Toi, tu choisis, tu corriges, tu assumes. Le pont, c'est le prompt : la facon dont tu formules la demande. Sans pont, tu obtiens du flou poli. Avec un pont, tu obtiens quelque chose de reutilisable. Plus loin dans le livre, on ajoutera des notions utiles : tokens, fenetre de contexte, temperature, system prompts, RAG, agents, multimodal, evaluation, couts d'API, securite des donnees. Pas pour te faire peur. Pour que tu saches ce que tu manipules.

Lea, freelance web, utilise l'IA pour ebaucher un mail client et un plan de page. Max, artisan plombier, s'en sert pour reformuler un devis plus clair et une fiche d'entretien. Sam, enseignant, prepare un quiz et une explication plus simple pour ses eleves. Trois metiers, meme logique : gagner du temps sur le brouillon, garder le cerveau pour le jugement.

## Ce que tu vas savoir faire

Dans ce livre, tu vas comprendre l'IA generative en mots simples, un peu d'histoire utile, les grands types d'outils, le fonctionnement pratique des LLM (tokens, contexte, temperature), l'art du prompt et des consignes systeme, les limites et les hallucinations, les usages du quotidien, le multimodal (image, audio, video), l'idee du RAG et des agents, l'ethique et la securite des donnees, l'evaluation des reponses, et l'idee des couts d'API. Puis un mini-projet, un recap, trois ateliers, comment choisir un outil, les bonnes pratiques, un quiz, et un bravo.

Niveau debutant solide. Pas besoin de coder pour comprendre. Pas besoin d'etre "tech". Besoin de curiosite et d'honnetete : l'IA aide ; elle ne remplace pas ta verification.

## Comment lire ce livre

Lis dans l'ordre au debut. Les premiers chapitres posent le sol. Les ateliers font faire. Le quiz verifie. Tu peux revenir ensuite a un chapitre precis (prompts, hallucinations, securite, couts) comme a une fiche. A chaque fin de chapitre, il y a un "A toi". Fais-le. Cinq minutes valent mieux qu'une lecture passive de quarante pages.

## Petite histoire

Lea devait ecrire une proposition pour un fleuriste. Avant, elle passait deux heures a regarder le curseur clignoter. Maintenant, elle demande a l'IA un plan en cinq parties, un ton simple, et trois questions a poser au client. Elle relit. Elle coupe le blabla. Elle ajoute son prix et ses limites. Quarante minutes, proposition nette. L'IA n'a pas "fait le devis". Elle a debloque le debut.

Max, lui, avait honte de ses mails. Trop courts, trop secs. Il demande une version plus claire, garde sa voix, envoie. Le client repond plus vite. Ce n'est pas de la triche. C'est de l'aide a la redaction, comme un correcteur en plus fort - a condition de ne jamais coller des donnees clients sensibles sans reflechir. On y revient longuement.

## Erreur classique

Croire que "l'IA a dit" egal "c'est vrai". Ou croire que "je ne sais pas formuler" egal "l'IA ne marche pas pour moi". Souvent, le probleme n'est pas le modele. C'est la demande floue : "ecris-moi quelque chose sur mon business". Quel business ? Pour qui ? Quel ton ? Quelle longueur ? Quelle action attendue ?

Autre piege : tout automatiser trop tot. Commence par une tache repetee et basse risque (mail, plan, reformulation). Monte ensuite vers les sujets plus techniques du livre. Tu seras pret.

## En vrai

Ouvre l'outil auquel tu as deja acces. Sans te former plus, pose une vraie question de ton quotidien : "aide-moi a expliquer mon offre en cinq lignes a un client presse". Lis. Note ce qui est juste, ce qui est vague, ce qui est faux. Ce livre sert a transformer ce premier essai en habitude propre.

## A toi

Ecris en trois phrases : (1) une tache que tu fais souvent et qui te fatigue, (2) ce que tu accepterais qu'une IA ebauche, (3) ce que tu ne lui confieras jamais sans controle humain. Garde ce papier. On y reviendra au mini-projet.
## Zoom : generative vs predictive

Beaucoup de gens melangent deux familles. L'IA predictive repond souvent a une question etroite : ce client va-t-il resilier ? Ce pixel appartient-il a un panneau ? L'IA generative produit un contenu nouveau : un paragraphe, une image, une piste audio. Les deux peuvent cohabiter dans le meme produit (un assistant qui resume puis propose un mail). Pour piloter, tu dois savoir laquelle tu actives. Si tu demandes une generation quand tu as besoin d'une classification fiable, tu obtiens du blabla la ou il fallait un score. Si tu demandes un score la ou tu as besoin d'idees, tu obtiens une case trop seche.

Dans la pratique 2026, le grand public touche surtout la generation via le chat. Les entreprises, elles, ont encore des modeles predictifs partout dans leurs logiciels metier, parfois sans le mot "IA" sur le bouton. Ton avantage, apres ce livre, c'est de ne plus etre impressionne par le label. Tu regardes le geste : generer, predire, enchaîner des actions, ou chercher dans des documents.

## Petite scene DanielCraft

Lea ouvre son assistant pour "ecrire une proposition". Elle a deja perdu vingt minutes a reformuler la meme phrase. Elle colle son brief signature, ajoute trois faits clients anonymises, demande un plan puis un texte. Elle coupe deux adjectifs marketing, remet son prix, envoie. Max, le meme matin, dicte une note de chantier dans le metro, demande une version claire, verifie qu'aucun delai n'a ete invente, envoie au client. Sam prepare un quiz : l'IA propose dix questions, il en jette six parce qu'elles sont ambigues, il garde quatre, il assume. Trois usages, une meme posture de pilote.

## Ce que "50 pages" doivent changer chez toi

A la fin, tu ne seras pas chercheur. Tu seras quelqu'un qui sait briefer, qui connait tokens et contexte assez pour ne pas noyer le modele, qui gere temperature mentale, system prompts, hallucinations, multimodal, RAG, agents, evaluation, couts, et securite des donnees. C'est deja beaucoup. C'est surtout actionnable demain matin.
