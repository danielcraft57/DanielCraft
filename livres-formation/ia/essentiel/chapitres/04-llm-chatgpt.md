# Chapitre 4 - Les LLM : tokens, contexte, temperature

**LLM** veut dire Large Language Model : grand modele de langage. En francais simple : un systeme entraine a manipuler le langage en predisant la suite probable d'un texte, a une echelle enorme. ChatGPT est un produit construit autour de tels modeles (avec interface, memoire de conversation, regles de securite, options payantes). Claude, Gemini, Copilot, Le Chat, Mistral et d'autres jouent dans la meme cour, avec des differences de style, de limites, et d'integration.

Tu n'as pas besoin de comprendre les maths. Tu as besoin de comprendre le comportement - et trois idees pratiques qui changent tout : les **tokens**, la fenetre de **contexte**, et la **temperature** (ou l'esprit "creatif vs strict").

:::retenir
Tokens + contexte + temperature mentale : trois leviers pour piloter un LLM sans maths.
:::

## Ce que fait vraiment un LLM

Il ne "cherche pas la verite dans une base officielle" par defaut (sauf si on le couple a une recherche ou a tes documents). Il produit une reponse coherente avec ta demande et avec ce qu'il a appris. Coherent n'est pas synonyme de vrai. Fluide n'est pas synonyme de competent.

Imagine un improvisateur genial qui a lu internet, des livres, des forums, du code. Il peut jouer le medecin, l'avocat, le marketeur. Parfois brillant. Parfois il invente une loi, une citation, un prix de piece detachee. D'ou l'importance des **prompts**, puis des hallucinations, puis de l'evaluation.

## Tokens : l'unite de lecture et d'ecriture

Le modele ne lit pas vraiment "mot par mot" comme a l'ecole. Il decoupe le texte en petits morceaux appeles tokens. Un token, ce peut etre un mot court, un bout de mot, une ponctuation. "Bonjour" peut etre un token ; un mot long ou rare peut en prendre plusieurs. Pourquoi tu t'en fiches... jusqu'au jour ou tu colles un roman, ou tu paies une API au token, ou tu te demandes pourquoi le modele "oublie" le debut.

En pratique, plus tu envoies de texte, plus tu consommes de tokens en entree. Plus il repond long, plus tu consommes en sortie. Les interfaces grand public masquent souvent ce compteur. Les API le montrent. Pour un debutant, retiens : sois precis, evite de coller dix PDF inutiles, demande la longueur dont tu as besoin. Tu gagnes en clarte et parfois en argent.

Ordre de grandeur pedagogique (pas une loi exacte) : en francais, compte souvent ~0,7 a 1 token par mot. Un mail de 120 mots ~ 100 a 150 tokens. Un chapitre de 800 mots ~ 600 a 900 tokens. Si l'API facture 0,50 EUR / million de tokens en entree (chiffre invente pour l'exo), coller 10 fois le meme PDF de 50 000 tokens coute vite cher... pour peu de gain.

```python
# Approximation pedagogique (pas un vrai tokenizer)
texte = "Bonjour Max, peux-tu confirmer le devis a 180 euros ?"
mots = texte.split()
tokens_approx = int(len(mots) * 0.9)
print(len(mots), "mots ~", tokens_approx, "tokens")
```

Avec une API, tu envoies souvent une liste de messages (systeme + utilisateur). Idee du format :

```python
messages = [
    {"role": "system", "content": "Tu reponds en francais simple. Signale les incertitudes."},
    {"role": "user", "content": "Reformume ce devis en 5 lignes. Prix exacts uniquement."},
]
# Puis: client.chat.completions.create(model="...", messages=messages, temperature=0.2)
```

Tu n'as pas a coder pour utiliser un chat. Mais voir ce squelette t'aide a comprendre temperature, roles, et cout.

:::astuce
Impose "8 lignes", "pas d'introduction", "commence par la reponse" : tu pilotes tokens et patience d'un coup.
:::

## Fenetre de contexte : ce que le modele "voit" maintenant

La fenetre de contexte, c'est la quantite maximale de conversation + documents que le modele peut prendre en compte a un instant T. Ce n'est pas une memoire humaine infinie. Si tu depasses, le systeme tronque, resume, ou refuse. Si la conversation devient tres longue et confuse, le debut s'estompe ou se noie. Solution pratique : reformuler un brief propre, recommencer un fil, ou n'attacher que l'extrait utile.

Certains produits ajoutent une "memoire" entre conversations (ils retiennent que tu es plombier a Lyon). Pratique. Aussi risque : ils retiennent des infos que tu n'aurais pas du coller. Gere ca comme un carnet partage, pas comme un coffre-fort.

## Temperature : creatif ou strict

La temperature, dans beaucoup d'API, est un reglage qui influence le caractere aleatoire des choix du modele. Temperature basse : reponses plus stables, plus "serrees", parfois repetitives. Temperature haute : plus de variete, plus de surprise, parfois plus d'invention. Dans les chats grand public, tu n'as pas toujours un bouton "temperature". Tu as l'equivalent mental : "sois creatif, propose 10 variantes" versus "sois strict, factuel, dis inconnu si tu ne sais pas".

Pour un devis, un reglement, une note aux parents : mode strict. Pour un slogan, un brainstorm, une metaphore pedagogique : mode creatif, puis filtre humain. Lea demande dix accroches (creatif) puis en garde deux (filtre). Max demande une reformulation fidele de ses notes (strict). Sam demande trois analogies (creatif) puis choisit celle qui colle a sa classe.

:::attention
Un long contexte mal organise noie le signal. Un court contexte bien choisi bat souvent un dump geant.
:::

## ChatGPT et la famille 2026

En pratique, tu ouvriras souvent : un chat web ou app ; un assistant dans Word / Docs / Outlook ; un assistant dans ton editeur de code ; parfois un modele local sur ta machine (plus avance). Les noms changent. Les gestes restent : brief, iteration, verification. Chez DanielCraft, on recommande aux debutants de maitriser un outil principal pendant un mois, plutot que d'ouvrir cinq comptes. La competence se transfère. La dispersion moins.

## Forces et faiblesses typiques

Forces : rediger, reformuler, resumer, traduire, brainstormer, expliquer simplement, generer des variantes, structurer un plan, ebaucher du code, jouer un role pour s'entrainer. Faiblesses : faits recents non verifies, chiffres inventes, sources bidon, raisonnement juridique / medical / fiscal dangereux si pris au pied de la lettre, flatterie, style generique, difficultes sur ce qui exige une vraie experience terrain absente du prompt.

## Erreur classique

Traiter le chat comme Google + expert + notaire. Ou jeter l'outil apres une mauvaise reponse a une question floue. Autre erreur : enchaîner vingt messages confus sans jamais reposer le cadre. Souvent, un nouveau fil avec un bon brief bat une conversation pourrie. Et coller tout ton historique "au cas ou" : tu saturres le contexte et tu melanges les sujets.

## En vrai

Pose la meme question de deux facons. Version floue : "parle-moi du SEO". Version cadre : "Tu es conseiller pour un artisan fleuriste a Toulouse. Explique le SEO local en 8 lignes simples. Donne 3 actions concretes cette semaine. Pas de jargon. Si tu n'es pas sur, dis-le." Compare. Tu viens de toucher tokens (longueur), contexte (cadre), et temperature mentale (strict).

## A toi

Choisis ton outil principal pour ce livre. Note son nom. Ecris une phrase d'identite a recoler en debut de prompt : qui tu es, pour qui tu ecris, ton ton. Exemple : "Je suis Max, plombier independant. Public : clients particuliers. Ton : clair, calme, sans blabla."

## Tokens : exemples concrets

Une phrase courte consomme peu. Un collage de cinquante pages de PDF consomme beaucoup, parfois au-dela de ce que le modele peut vraiment "exploiter" utilement meme si ca rentre. Une reponse qui demarre par trois pages de preambule "Dans un monde en constante evolution" consomme ta patience et tes tokens de sortie pour rien. D'ou les consignes : "8 lignes", "pas d'introduction", "commence par la reponse". Tu ne micro-management pas par plaisir. Tu pilotes la ressource.

Certains outils affichent un compteur. D'autres non. En API, tu le verras sur la facture. Meme en forfait, un usage gaspille te rapproche des limites. Habitude saine : chaque piece jointe doit justifier sa presence en une phrase dans ton brief ("j'attache la page tarifs seulement").

## Contexte long : pas une memoire magique

Les fenetres de contexte ont grandi. Ca n'a pas aboli le besoin de structure. Un long contexte mal organise noie le signal. Un court contexte bien choisi bat souvent un dump. Pareil pour la memoire produit : utile pour "je suis plombier", dangereuse pour "voici mon IBAN". Configure, nettoie, revois.

## Temperature et alternatives

Meme sans bouton, tu influences l'aleas : "donne 1 reponse stricte" versus "donne 12 pistes tres differentes". Tu peux aussi demander "deux options : sage et audacieuse". Tu exterriorises ainsi le reglage. Pour les contenus critiques, baisse l'aleas et augmente la verification humaine. Pour la creativite, monte l'aleas et garde un filtre de gout.
