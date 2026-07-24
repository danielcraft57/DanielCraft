# Chapitre 7 - RNN : sequences dans le temps (overview)

Les RNN (Recurrent Neural Networks) ont ete concus pour les sequences : texte, audio, series temporelles. Idee : traiter un element a la fois en maintenant un etat memoire qui resume le passe. Chaque nouveau mot met a jour la memoire, puis on predit.

## Limites historiques

Sur les longues sequences, les RNN simples oublient ou deviennent instables (gradients qui disparaissent ou explosent). Des variantes (LSTM, GRU) ont ameliore la memoire. Puis les transformers ont souvent pris le dessus sur le langage a grande echelle, grace a l'attention parallele. Pourquoi en parler encore ? Parce que l'intuition "etat qui voyage dans le temps" reste pedagogique, et parce que certaines series temporelles industrielles utilisent encore des approches recurrentes ou hybrides.

## Ou les situer en 2026

Pour le langage generatif massif : transformers. Pour comprendre l'histoire du NLP et certaines taches sequentielles legeres : utile. Pour l'audio et la parole, des architectures mixtes existent. L'important : savoir que "sequence" demande un traitement du contexte ordonne, pas seulement un sac de mots.

## Erreur classique

Choisir un RNN parce qu'un tutoriel de 2017 le dit, alors qu'un modele preentraine transformer resoudrait mieux ton cas texte. Autre piege : croire qu'une memoire recurrente egale une comprehension humaine du recit.

## A toi

Donne un exemple de sequence dans ton metier (logs, phrases, mesures). Qu'est-ce qui depend du passe recent ?
## Series temporelles

Predire la demande, detecter une anomalie sur un capteur : parfois RNN/LSTM, parfois modeles statistiques, parfois transformers temporels. La lecon transversale : respecter le temps dans le split (pas de futur qui fuit dans le passe), et evaluer sur des periodes realistes.

## Developpement : ce que le deep learning change vraiment

Le deep learning a deplace le curseur : des taches autrefois impossibles sans features handicraftées deviennent abordables si tu as des donnees et du calcul. Images, parole, langue. Mais il n'a pas aboli les fondamentaux : split honnete, metriques alignees, biais, monitoring, abstention. Il les a rendus plus urgents, parce que les systemes sont plus opaques et plus couts.

Quand tu entends "on a mis du deep learning", pose les questions de ce livre : combien de donnees ? preentraine ou from scratch ? quelle validation ? quel GPU / quel budget ? quel comportement hors distribution ? quel plan si le modele se trompe ? Tu passeras pour quelqu'un de serieux. C'est voulu.

## Intuition des representations

Une bonne representation rend le probleme plus simple pour la couche suivante. Au debut du reseau, l'entree est brute (pixels, tokens). Au milieu, des motifs. A la fin, une decision. Transfer learning = reutiliser un milieu deja riche. RAG cote LLM = injecter des faits dans le contexte plutot que de tout stocker dans les poids. Prompting = conditionner la representation de sortie sans maj de poids. Ces leviers sont differents, mais ils parlent le meme langage : influencer ce que le systeme "voit" avant de decider.

## Experimentation sobre

Change une chose a la fois. Logge. Compare a une baseline. Arrete-toi quand la validation stagne. Ne confonds pas agitation et progres. Un entrainement qui fait baisser la loss train sans ameliorer la val n'est pas un succes. Un petit modele qui generalise un peu est parfois preferable a un grand modele qui memorise.

## Ethique et impact

Derriere les perfs : energie, annotation, risques de surveillance, deepfakes, automatisation de decisions sensibles. Ce livre introductif ne tranche pas tous les debats. Il exige que tu les voies. Utiliser un outil puissant sans regarder ses effets collateraux, ce n'est pas de la neutralite technique. C'est une decision. Assume-la.

## Pour aller plus loin sans te perdre

Tu n'as pas a tout maitriser d'un coup. Reviens a ce chapitre quand tu butes sur un cas reel. Relis l'erreur classique. Refais le "A toi". Chez DanielCraft, on prefere trois relectures actives a une lecture passive de vingt pages. Si un paragraphe te semble encore flou, reformule-le a voix haute avec ton propre exemple. Des que ca passe a l'oral, c'est que c'est entre. Ensuite seulement, passe au chapitre suivant. Cette discipline lente cree une competence rapide sur la duree - le contraire du binge de tutos oublies le lendemain.
