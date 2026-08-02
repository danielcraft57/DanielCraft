# Chapitre 10 - Metriques : mesurer sans se raconter d'histoires

Une **metrique** traduit une erreur en nombre. Mauvaise metrique, mauvaise decision. La "bonne" metrique depend du cout metier, pas de la mode GitHub.

:::retenir
Choisis la metrique pour le cout metier, pas pour impressionner. Traduis toujours le score en decision.
:::

## Regression

**MAE** (erreur absolue moyenne) : lisible en unites de y. RMSE : penalise plus les grosses erreurs. MAPE : en pourcentage, attention aux y proches de zero. R2 : part de variance expliquee, utile mais pas sacre. Regarde aussi des graphiques residus : les nombres seuls mentent parfois.

## Classification

**Accuracy** : part de bons labels - trompeuse si classes desequilibrees. **Precision** : parmi les alertes, combien sont justes. **Rappel** (recall) : parmi les vrais positifs, combien tu as attrapes. F1 : compromis. Matrice de confusion : le tableau qui montre ou tu te trompes. Courbes et AUC : utiles, a condition de comprendre le seuil ensuite.

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, confusion_matrix
)

y_vrai = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
y_pred = [0, 0, 0, 1, 0, 1, 1, 0, 1, 1]  # 1 = "alerte fraude"

print("accuracy ", accuracy_score(y_vrai, y_pred))
print("precision", precision_score(y_vrai, y_pred))
print("rappel   ", recall_score(y_vrai, y_pred))
print("matrice\n", confusion_matrix(y_vrai, y_pred))
```

Lis la matrice : lignes = vrai, colonnes = predit. Un seul chiffre "accuracy" ne raconte pas ou tu te trompes.

:::attention
Sur classes desequilibrees, l'accuracy peut mentir. Pair precision/rappel (ou couts) avant de celebrer.
:::

## Cout metier > score unique

Si manquer une fraude coute 1000 et deranger un client sain coute 10, tu n'optimises pas comme si les erreurs etaient egales. Ecris une petite matrice de couts. Choisis seuil et modele en consequence. Noe prefere parfois plus de fausses alertes de retour que rater des retours massifs sur une gamme - ou l'inverse, selon sa logistique.

:::astuce
Une metrique principale + une metrique de garde-fou. La premiere decide, la seconde empeche les derives.
:::

## Baseline toujours

Compare a "toujours predire la moyenne" ou "toujours la classe majoritaire". Un modele complique qui bat a peine le **baseline** n'est pas un succes. Un modele simple qui le bat nettement, si.

## Erreur classique

Chasser le 0.01 d'accuracy en ignorant que le label a change de definition. Ou presenter un score sans intervalle, sans taille d'echantillon, sans contexte de deploiement.

## A toi

Choisis UNE metrique principale et UNE metrique de garde-fou pour ton projet. Justifie en trois phrases metier.

## Raconter un score a un non-tech

Evite "notre F1 est 0,73". Prefere : "sur 100 vrais retours, on en attrape 80, et sur 100 alertes, 40 sont des fausses peurs ; voici ce que ca coute". Traduis. Si tu ne peux pas traduire, tu ne choisis peut-etre pas la bonne metrique.

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
