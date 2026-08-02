# Chapitre 5 - Classification : predire une classe

**Classifier**, c'est attribuer une categorie. Spam ou non. Client a risque ou non. Produit defaillant ou non. Langue detectee. Type de ticket support. La sortie n'est pas un prix ; c'est une case (parfois un score de probabilite avant la case).

:::retenir
Classification = predire une classe. Le seuil et le cout des erreurs comptent plus qu'un score "joli".
:::

## Frontiere de decision

Imagine des points de deux couleurs sur un plan. Un classifieur trace une frontiere. D'un cote, classe A ; de l'autre, classe B. Lineaire : une droite. Plus souple : des courbes, des rectangles (arbres), des combines. Sur des textes ou des images, l'espace est vaste, mais l'idee reste : separer des regions.

## Scores et seuils

Beaucoup de modeles sortent un score ("probabilite" de spam). Tu choisis un **seuil** : au-dessus, tu filtres. Baisser le seuil attrape plus de spam mais risque de bloquer des mails legimes. Monter le seuil l'inverse. Le "meilleur" seuil depend du cout des erreurs - pas d'une beaute mathematique.

Exemple jouet (spam = 1) :

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

# feature jouet : longueur du mail (caracteres)
X = np.array([[40], [60], [200], [220], [80], [300]])
y = np.array([0, 0, 1, 1, 0, 1])  # 0 = ok, 1 = spam

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.33, random_state=0)
clf = LogisticRegression().fit(Xtr, ytr)
probas = clf.predict_proba(Xte)[:, 1]
seuil = 0.5
preds = (probas >= seuil).astype(int)
print("probas", np.round(probas, 2))
print("preds ", preds, "vrai", yte)
```

Change `seuil` a 0.3 puis 0.7. Tu verras le trade-off rappel / precision... meme sur 6 lignes.

:::astuce
Ecris d'abord le cout d'un **faux positif** et d'un **faux negatif**. Le seuil se deduit souvent de ca, pas d'une courbe seule.
:::

## Classes desequilibrees

Si 1 % des commandes sont frauduleuses, un modele naif qui dit toujours "pas fraude" a 99 % de exactitude globale... et zero interet. Il faut des **metriques** adaptees (precision, rappel, F1, cout metier) et parfois des strategies d'echantillonnage. Noe avec 8 % de retours doit regarder la detection des retours, pas seulement le taux global de bonnes reponses.

:::attention
Sur classes desequilibrees, l'**accuracy** globale peut etre excellente et le modele inutile. Regarde precision, rappel, et la matrice de confusion.
:::

## Multclasse

Parfois plus de deux cases : type A/B/C/D. Les idees restent proches, les metriques et matrices de confusion s'etendent. Clarifie si les classes sont ordonnees (faible/moyen/fort) ou non : ca change les options.

## Erreur classique

Optimiser l'accuracy aveugle sur un jeu desequilibre. Ou deployer un classifieur sans definir le cout d'un faux positif vs faux negatif (bloquer un client sain vs laisser passer une fraude).

## A toi

Pour une classification de ton monde, ecris : cout d'un faux positif, cout d'un faux negatif. Lequel est pire ? Ca guidera ton seuil.

## Probabilites calibrees (idee)

Un score de 0,8 devrait vouloir dire "environ 80 % de chances" si tu veux l'utiliser comme probabilite. Ce n'est pas toujours vrai hors boite. Pour debuter, traite les scores comme des ordres utiles pour ranger, choisis un seuil metier, et mefie-toi des interpretations trop litterales tant que tu n'as pas verifie la calibration.

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
