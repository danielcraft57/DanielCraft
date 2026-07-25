# Chapitre 8 - Transformers : l'attention (overview)

Le **transformer** est l'architecture dominante du NLP moderne et le coeur de beaucoup de **LLM**. Idee centrale : l'**attention**. Chaque position (chaque **token**) peut regarder les autres positions et ponderer celles qui comptent pour construire une nouvelle representation. Contrairement aux RNN classiques, on peut paralleliser beaucoup mieux sur **GPU**.

Chez DanielCraft, on veut une image nette, pas un papier de recherche. Si tu retiens "attention + profondeur + donnees + calcul", tu as le moteur. Le reste du produit (alignement, interface, garde-fous) vient autour.

:::retenir
Transformer = attention entre positions / tokens, empilee en profondeur. Coeur de beaucoup de LLM.
:::

## Ce que ce n'est pas

Ce n'est pas une garantie de qualite : "on a mis un transformer" n'egal pas "c'est bon". Ce n'est pas l'attention humaine consciente. Ce n'est pas magique hors donnees et evaluation. Et ce n'est pas gratuit : l'attention "tous sur tous" coute cher quand la sequence s'allonge - d'ou les limites de **contexte** et le prix des tokens.

Quand tu lis "le chat sur le tapis, il dort", le mot "il" doit se relier a "chat". L'attention apprend des liens utiles selon la tache. **Multi-tetes** : plusieurs types de liens en parallele. Empilement de blocs : representations de plus en plus riches. On ajoute des encodings de position, parce que sinon l'ordre serait moins clair. Ines explique ca a Lea avec un surligneur mental : chaque mot eclaire les autres selon le besoin.

:::astuce
Pour sentir l'attention, prends une phrase avec un pronom. Demande : a quoi doit se coller ce pronom ? C'est le geste.
:::

## Encodeurs, decodeurs, seq2seq

Selon les modeles : encodeur seul (classification, embeddings), decodeur seul (generation de texte style GPT), encodeur-decodeur (traduction...). Tu n'as pas a tout memoriser. Retiens : attention + profondeur + plein de donnees + plein de calcul = capacites emergentes de langage. Sam resume pour sa classe : "certains lisent et classent, d'autres ecrivent la suite, d'autres traduisent".

## Contexte et complexite

L'attention tous-sur-tous coute cher avec la longueur. D'ou les fenetres de contexte limitees, les resumes, les decoupes, le **RAG** (chercher des morceaux puis les coller dans le contexte), ou le prix plus eleve des longues fenetres. Comprendre ca, c'est comprendre pourquoi un PDF de 200 pages ne "rentre" pas tel quel dans la tete du modele, meme si le chat a l'air confiant.

## Petite histoire

Max a colle un devis de 40 pages dans un chat et a demande "resume les risques". Le modele a invente un delai. Lea lui a montre : fenetre limitee, attention diluee, hallucination possible. Ils ont coupe en sections, pose des questions ciblees, verifie les chiffres. Meme architecture. Meilleur usage. Chez DanielCraft, l'architecture sans protocole reste un moteur sans frein.

## Lien pratique

**Fine-tuning**, RAG, **prompting** : facons d'utiliser ces geants sans tout reentrainer. Comprendre le transformer te permet de comprendre pourquoi le contexte a une taille limite, pourquoi les tokens coutent, pourquoi un long document doit parfois etre coupe ou cherche par morceaux. Ines, cote vision, note le parallele : representations riches reutilisees, tete adaptee - meme esprit que le transfer learning.

## Erreur classique

Dire "on a mis un transformer" comme garantie. Autre piege : confondre attention technique et attention humaine. Troisieme : noyer le modele sous un contexte inutile puis accuser "l'IA" d'etre bete.

:::attention
Le contexte est un budget. Remplis-le avec ce qui sert a la decision, pas avec tout le disque dur.
:::

## En vrai

Explique l'attention a un ami avec l'exemple du pronom "il". Ajoute une phrase : pourquoi un GPU aide a entrainer ca (parallelisme des calculs de matrices / attention).

## A toi

Ecris ton explication "attention + pronom" en 8 lignes. Puis note une limite de contexte pour un document de ton metier : que coupes-tu en premier ?

## Du moteur au produit

Un LLM de chat, c'est souvent un transformer decodeur entraine a predire le prochain token, puis aligne pour mieux suivre des instructions. Le chapitre "lien LLM" detaille ce pont. Ici, tu as le coeur mecanique. Garde-le : il demystifie la suite.

## Multi-tetes : plusieurs regards

Une tete d'attention peut se specialiser vers la syntaxe, une autre vers des liens de long distance, une autre vers des motifs locaux - en pratique, tu n'inspectes pas chaque tete jour 1. L'idee utile : plusieurs types de liens en parallele enrichissent la representation avant la couche suivante. Sam compare a plusieurs eleves qui annotent la meme phrase avec des couleurs differentes, puis fusionnent.

## Pourquoi le GPU aime ca

Les calculs d'attention et de matrices se pretent au parallelisme. D'ou l'alliance historique transformers + accelerateurs. Comprendre ce lien t'evite de croire qu'un CPU portable entrainera un geant "parce que Python". Pour l'usage via API, le GPU est chez le fournisseur ; tu paies l'inference autrement. Ines distingue clairement les deux budgets.
