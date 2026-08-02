# Chapitre 12 - Lien avec les LLM : du neurone au chat

Un **LLM** est un reseau de deep learning - souvent un **transformer** decodeur - entraine a predire le prochain **token** sur d'enormes corpus, puis souvent aligne pour mieux suivre des instructions et respecter des politiques. Quand tu chats, tu ne "parles pas a une conscience". Tu conditionnes une machine a suites de tokens.

Chez DanielCraft, ce chapitre ferme la boucle : tout ce que tu as vu (neurone, couches, activation, backprop, attention, GPU, transfer) se reconnait dans l'outil du quotidien. Tu gagnes un vocabulaire anti-fantasme.

:::retenir
LLM = deep learning langage (souvent transformer) + alignement + usage (prompt / RAG / agents). Tu pilotes ; tu ne dialogues pas avec une ame.
:::

## Ce que ce n'est pas

Ce n'est pas sans lien avec le deep learning - au contraire. Ce n'est pas une base de connaissances fiable par defaut (**hallucinations**). Ce n'est pas un remplacant automatique du ML classique sur un CSV metier. Et ce n'est pas "uploader un PDF une fois pour qu'il sache tout pour toujours" : sans RAG ni fine-tune evalue, le fichier du jour n'est pas grave dans les poids.

## Ce que tu reconnais maintenant

**Tokens** et **contexte** : la fenetre limite ce que l'attention peut croiser d'un coup. **Temperature** : reglage sur l'aleas des choix de tokens. Poids et couches : milliards de parametres ajustes par descente de gradient a l'echelle industrielle. Hallucinations : prediction plausible hors verite. Multimodal : on branche vision / audio sur des representations communes ou des modules couples. **RAG** : on injecte des extraits dans le contexte plutot que de tout memoriser dans les poids. **Agents** : on boucle le LLM avec des outils.

:::astuce
Dessine 8 fleches : donnees -> transformer -> tokens -> prompt -> reponse -> verification. Place RAG et temperature sur le schema.
:::

## Entrainer vs utiliser

Entrainer un LLM fondation : hors de portee de la plupart des individus (donnees, GPU, argent, energie). Utiliser : API, produit grand public, modele open poids local selon machine. Fine-tuning leger : parfois accessible. Prompting et RAG : levier numero un. Comprendre le deep learning te protege des fantasies et t'oriente vers les bons leviers. Lea le dit a ses clients : "on n'entraine pas ChatGPT ; on l'utilise proprement".

## Alignement (idee)

Apres l'entrainement "predire le prochain token", beaucoup de LLM passent par des etapes pour mieux suivre les instructions et reduire certains comportements dangereux. Ca n'efface pas les hallucinations. Ca change le temperament du produit que tu utilises. D'ou des differences de style entre outils. Sam compare : meme famille de moteurs, permis de conduire differents.

## Petite histoire

Ines utilise un assistant pour rediger la doc utilisateur de son appli vision. Elle fournit des faits vrais (classes, limites, seuils), interdit l'invention de chiffres, verifie. Le LLM accelere le brouillon. Le CNN, lui, classe les pieces. Deux deep learning, deux roles, une meme posture de pilote. Max demande un mail client : meme posture. Chez DanielCraft, on aime cette coexistence assumee.

## Ethique et cout

Derriere le chat fluide : calcul, energie selon les infrastructures, travail d'annotation et de moderation, risques de biais. Le chapitre n'est pas un proces. C'est une invitation a utiliser avec mesure, surtout en entreprise : donnees sensibles, verification, abstention. L'argent des tokens n'est qu'une partie du cout : le cout d'une erreur confiante peut etre bien plus haut.

## Erreur classique

Croire qu'un LLM rend inutile le ML classique sur un CSV. Autre piege : confondre "fine-tune" marketing et vrai changement de poids evalue proprement. Troisieme : coller des secrets dans le fil "parce que ce sera plus perso".

:::attention
Fluide n'est pas competent. Verification et limites restent ton job.
:::

## En vrai

Ouvre l'assistant auquel tu as acces. Pose une question de ton metier avec faits fournis, puis la meme sans faits. Compare inventions et utilite. Note trois differences.

## A toi

Relie en schema : donnees, transformer, tokens, prompt, reponse, verification, RAG, temperature. Une fleche manquante = un trou a relire.

## Pont vers les ateliers

Tu vas solidifier l'intuition neurone/couches, ecrire un plan CNN, puis relier transformer et usage LLM. Tu as maintenant le pont conceptuel. La suite fait faire. C'est le coeur pedagogique DanielCraft : comprendre, puis agir petit, puis evaluer.

## Temperature mentale

Basse : plus deterministe, utile pour faits et procedures. Haute : plus varie, utile pour idees, risquee pour chiffres. Ines garde basse pour la doc technique. Lea monte un peu pour brainstorm, puis redescend pour l'envoi client. Le reglage n'est pas magique ; il change le profil de risque. Couple-le toujours a une verification.

## Agents : boucler avec freins

Un agent enchaine LLM + outils. Puissant, fragile. Sans freins (validation, plafonds, logs), tu automatises aussi les erreurs. Ce livre introductif dit : comprends le moteur avant d'ouvrir l'autoroute. Le chapitre bonnes pratiques et limites te rappellent le frein. Chez DanielCraft, l'agent vient apres le protocole, pas avant.
