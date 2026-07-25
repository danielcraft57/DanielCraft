# Chapitre 16 - Atelier : transformer et usage LLM

Objectif : relier architecture et gestes d'usage. Duree visee : environ 35 minutes. Tu sors avec une fiche "du transformer a mon usage" : schema d'attention, protocole RAG manuel, regles de cout et de verification.

Chez DanielCraft, comprendre le moteur sans protocole d'usage, c'est laisser le frein au garage. Cet atelier pose le frein.

:::retenir
Attention expliquee + contexte budgete + RAG manuel + temperature choisie + risques listes = usage adulte d'un LLM.
:::

## Ce que ce n'est pas

Ce n'est pas un fine-tune obligatoire. Ce n'est pas "construire un agent autonome". Ce n'est pas non plus un concours de prompts miracles. C'est relier ce que tu as appris au chapitre 8 et 12 a des gestes que tu peux faire aujourd'hui.

## Image mentale

Tu as un moteur attentionnel avec une fenetre de contexte limitee. Tu decids quoi mettre dans la fenetre, comment chercher des extraits, comment regler l'aleas, comment verifier. Lea fait ca pour ses propositions clients. Ines pour sa doc. Sam pour ses quiz. Max pour ses mails - avec interdiction d'inventer un delai.

## Etapes (dans l'ordre)

1) Explique l'attention avec ton propre exemple de phrase (pronom, reference, consigne metier). Ecris 8 lignes max.

2) Mesure mentalement une limite de contexte : que coupes-tu dans un long PDF ? Ordre de priorite.

3) Concevoir un mini-RAG : 5 documents (memes fictifs), une question, l'extrait a coller, une consigne anti-invention.

4) Deux temperatures mentales sur la meme tache (strict vs creatif) et une petite grille d'evaluation (utile / faux / flou).

5) Decrire un fine-tuning que tu NE feras pas maintenant, et pourquoi prompting / RAG suffisent pour l'instant.

6) Lister 3 risques : donnees sensibles, hallucination, cout tokens (ou temps de verification).

:::idee
Le mini-RAG manuel (copier l'extrait toi-meme) enseigne mieux que trois slides sur les vector stores.
:::

## Petite histoire

Lea a teste le meme brief "strict" puis "creatif" pour un mail artisan. Le creatif a invente une promo. Le strict a demande le prix manquant. Elle a garde le strict pour l'envoi, le creatif pour brainstorm prive. Sam fait le meme exercice avec ses eleves : choisir la temperature, c'est choisir un risque.

## Budget tokens

Estime un cout mensuel grossier : questions / jour x tokens moyens x prix. Ajoute le cout de tes erreurs (temps de verification, risque metier). Decide si un modele plus petit suffit pour 80 % des cas. Ines reserve le modele "lourd" aux cas ambigus ; le reste passe au leger.

## Erreur classique

Coller tout le disque dans le contexte. Ou faire un "RAG" sans verifier que l'extrait repond a la question. Ou annoncer un fine-tune pour impressionner alors qu'un bon brief suffit. Ou ignorer le cout de verification humaine.

:::attention
Un extrait mal choisi dans un RAG produit une reponse fluide et fausse. Le fluide empire le piege.
:::

## En vrai

Fais le mini-RAG sur papier : question, extrait, consigne "n'utilise que l'extrait, dis inconnu sinon". Execute dans ton outil. Compare a la meme question sans extrait.

## Livrable

Fiche "du transformer a mon usage" avec : schema attention, protocole RAG manuel, deux reglages de temperature, budget tokens, 3 risques. Une page recto volait.

## A toi

Coche les 6 etapes. Puis ecris la phrase : "je fine-tune seulement si ..." avec un critere mesurable. Si tu ne trouves pas de critere, tu ne fine-tune pas.

## Variante Max

Remplace le PDF par un devis et une fiche produit. Meme atelier. Interdits : inventer delai, prix, garantie. C'est du deep learning applique a la confiance client.

## Exemple de mini-RAG (modele)

Question : "Quel delai max pour la piece B ?". Document 3 : "Piece B : delai annonce 5 jours ouvres, hors rupture.". Consigne : "Reponds seulement avec l'extrait. Si absent, dis inconnu.". Sans extrait, le modele invente parfois 48 h. Avec extrait, il cite 5 jours. Max garde cet exemple scotche au-dessus de son ecran.

## Grille d'evaluation rapide

Pour chaque reponse : utile / faux / flou / danger donnees. Trois exemples suffisent pour sentir la temperature et le brief. Lea exige cette grille avant d'industrialiser un usage chat en entreprise.
