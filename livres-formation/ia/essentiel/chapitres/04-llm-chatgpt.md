# Chapitre 4 - Les LLM et ChatGPT (le coeur du sujet)

LLM veut dire Large Language Model : grand modele de langage. En francais simple : un systeme entraine a manipuler le langage en predissant la suite probable d'un texte, a une echelle enorme. ChatGPT est un produit construit autour de tels modeles (avec interface, memoire de conversation, regles de securite, options payantes, plugins selon les epoques). Claude, Gemini, Copilot, Le Chat, et d'autres, jouent dans la meme cour avec des differences de style, de limites, et d'integration.

Tu n'as pas besoin de comprendre les maths. Tu as besoin de comprendre le comportement.

## Ce que fait vraiment un LLM

Il ne "cherche pas la verite dans une base officielle" par defaut (sauf si on le couple a une recherche ou a tes documents). Il produit une reponse coherente avec ta demande et avec ce qu'il a appris. Coherent n'est pas synonyme de vrai. Fluide n'est pas synonyme de competent.

Imagine un improvisateur genial qui a lu internet, des livres, des forums, du code. Il peut jouer le medecin, l'avocat, le marketeur. Parfois brillant. Parfois il invente une loi, une citation, un prix de piece detachee. D'ou le chapitre suivant sur les prompts, et celui d'apres sur les hallucinations.

## Tokens, contexte, memoire : version poche

Le modele lit et ecrit par petits morceaux (tokens). Il a une fenetre de contexte : une quantite max de conversation + documents qu'il "voit" a un instant T. Si tu colles un roman et que tu demandes un detail page 2, il peut rater. Si la conversation devient tres longue, le debut s'estompe. Solution pratique : reformuler, recommencer un fil propre, ou attacher le bon extrait.

Certains produits ajoutent une "memoire" entre conversations (ils retiennent que tu es plombier a Lyon). Pratique. Aussi risque : ils retiennent des infos que tu n'aurais pas du coller. Gere ca comme un carnet partage, pas comme un coffre-fort.

## ChatGPT et la famille 2026

En pratique, tu ouvriras souvent : un chat web ou app ; un assistant dans Word / Docs / Outlook ; un assistant dans ton editeur de code ; parfois un modele local sur ta machine (plus avance, plus technique). Les noms changent. Les gestes restent : brief, iteration, verification.

Chez DanielCraft, on recommande aux debutants de maitriser un outil principal pendant un mois, plutot que d'ouvrir cinq comptes "parce que c'est gratuit". La competence se transfère. La dispersion moins.

## Forces typiques

Rediger et reformuler. Resumer. Traduire. Brainstormer. Expliquer simplement. Generer des variantes. Structurer un plan. Aider a apprendre (avec prudence). Ebaucher du code ou des formules. Jouer un role pour s'entrainer (entretien, objection client) - toujours en gardant la tete.

Lea lui demande dix accroches d'email, puis en garde deux. Max lui demande de transformer ses notes de chantier en compte-rendu clair. Sam lui demande trois analogies pour expliquer la fraction a des eleves de 6e, puis choisit celle qui colle a sa classe.

## Faiblesses typiques

Faits recents non verifies. Chiffres precis inventes. Sources bidon. Raisonnement juridique / medical / fiscal dangereux si pris au pied de la lettre. Flatterie. Digressions. Style generique ("Dans le monde d'aujourd'hui..."). Difficulté sur ce qui exige une vraie experience terrain que tu n'as pas mise dans le prompt.

## Temperature mentale (sans bouton)

Tu peux demander "sois creatif" ou "sois strict et factuel". Plus tu demandes de creativite, plus tu acceptes de variation - et parfois d'invention. Pour un devis, un reglement, une note aux parents : mode strict. Pour un slogan : mode creatif, puis filtre humain.

## Erreur classique

Traiter le chat comme Google + expert + notaire. Ou a l'inverse, le jeter apres une mauvaise reponse a une question floue. Autre erreur : enchaîner vingt messages confus sans jamais reposer le cadre. Souvent, un nouveau fil avec un bon brief bat une conversation pourrie.

## En vrai

Pose la meme question a ton outil de deux facons. Version floue : "parle-moi du SEO". Version cadre : "Tu es conseiller pour un artisan fleuriste a Toulouse. Explique le SEO local en 8 lignes simples. Donne 3 actions concretes cette semaine. Pas de jargon. Si tu n'es pas sur, dis-le." Compare. Tu viens de toucher le coeur du livre.

## A toi

Choisis ton outil principal pour ce livre. Note son nom. Ecris une phrase d'identite que tu pourras recoler en debut de prompt : qui tu es, pour qui tu ecris, ton ton. Exemple : "Je suis Max, plombier independant. Public : clients particuliers. Ton : clair, calme, sans blabla."
