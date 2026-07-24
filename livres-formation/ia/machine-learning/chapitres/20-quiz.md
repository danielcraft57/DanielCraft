# Quiz final

1. L'apprentissage supervise necessite surtout :
- A) Aucun exemple
- B) Des exemples avec labels (bonnes reponses)
- C) Uniquement des images de chats

2. Predire un prix, c'est typiquement :
- A) De la classification
- B) De la regression
- C) Du clustering obligatoire

3. Train/test sert a :
- A) Faire joli dans un rapport
- B) Evaluer la generalisation sans se mentir
- C) Doubler la taille memoire

4. L'overfitting, c'est :
- A) Coller trop au train et generaliser mal
- B) Avoir trop peu de parametres toujours
- C) Un antivirus

5. Une bonne feature doit etre :
- A) N'importe quelle colonne du CSV
- B) Disponible a l'instant de prediction et definie clairement
- C) Un ID unique de preference

6. Sur classes desequilibrees, l'accuracy globale :
- A) Suffit toujours
- B) Peut tromper ; regarder precision/rappel/couts
- C) Est interdite par la loi

7. Un pipeline aide surtout a :
- A) Eviter fuites et incoherences de transformation
- B) Remplacer les donnees
- C) Dessiner des logos

8. Les biais dans les donnees :
- A) Disparaissent magiquement dans les maths
- B) Peuvent etre herites et amplifies par le modele
- C) N'existent que dans les LLM

9. Scikit-learn, en idee :
- A) Un reseau social
- B) Une bibliotheque avec une grammaire fit/transform/predict
- C) Un type de GPU

10. Avant un modele complexe, DanielCraft recommande :
- A) Une baseline simple et un protocole honnete
- B) Dix librairies a la mode
- C) D'ignorer la metrique metier

## Corriges

1-B, 2-B, 3-B, 4-A, 5-B, 6-B, 7-A, 8-B, 9-B, 10-A.

9/10 ou plus : solide. Sinon, relis features, train/test, metriques, biais, puis refais apres un atelier.
## Bonus

Explique en cinq lignes a un ami la difference supervise / non supervise, et pourquoi l'accuracy peut mentir. Si tu bloques, relis chapitres 2, 3, 10.

## Developpement : penser comme un artisan des modeles

Le machine learning n'est pas un distributeur de verite. C'est un artisanat de decisions sous incertitude. Tu choisis une question, tu rassembles des exemples, tu acceptes une erreur moyenne, tu te donnes les moyens de la mesurer, tu decides si cette erreur est tolerable pour le cas d'usage. Beaucoup de frustration vient d'attendre la perfection la ou il fallait un score utile avec un humain dans la boucle.

Quand Noe predit un risque de retour, il ne remplace pas le service client. Il priorise. Quand un hopital utilise un score (hors du perimetre de ce livre introductif, et avec des cadres stricts), l'enjeu n'est plus le meme : les couts d'erreur explosent, les biais deviennent critiques, la gouvernance monte. Adapte toujours la profondeur de ta demarche a l'impact. Un modele jouet sur un CSV public n'exige pas la meme revue qu'un score qui bloque un credit.

## Donnees : le personnage principal

Les algorithmes changent. Les principes de donnees restent : definition claire, representativite, fraicheur, droits, documentation, absence de fuite, inspection des cas bizarres. Passe plus de temps sur les donnees que sur le shopping d'algorithmes. C'est le conseil le moins glamour et le plus rentable du livre. Un arbre simple sur des features excellentes bat une usine a gaz sur un tableau sale.

## Mise en production (apercu)

Un notebook n'est pas un produit. En production, tu dois gerer des entrees manquantes nouvelles, des categories inconnues, des delais, des journaux, des versions, des rollback, des alertes si la metrique chute. Tu n'as pas a tout construire aujourd'hui. Tu dois savoir que ca existe, pour ne pas crier victoire trop tot apres un score de validation. Prevour des le jour 1 un chemin "humain si doute".

## Culture et communication

Apprends a dire "non" a un modele inutile. Apprends a dire "pas encore" quand les labels manquent. Apprends a dire "voici les limites" quand tu presentes un score. Cette honnetete te rend plus credible que n'importe quel jargon. Chez DanielCraft, on forme des gens capables de tenir cette conversation avec un metier, un manager, ou un client.

## Pour aller plus loin sans te perdre

Tu n'as pas a tout maitriser d'un coup. Reviens a ce chapitre quand tu butes sur un cas reel. Relis l'erreur classique. Refais le "A toi". Chez DanielCraft, on prefere trois relectures actives a une lecture passive de vingt pages. Si un paragraphe te semble encore flou, reformule-le a voix haute avec ton propre exemple. Des que ca passe a l'oral, c'est que c'est entre. Ensuite seulement, passe au chapitre suivant. Cette discipline lente cree une competence rapide sur la duree - le contraire du binge de tutos oublies le lendemain.
