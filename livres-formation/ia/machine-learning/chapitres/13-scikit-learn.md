# Chapitre 13 - Scikit-learn : l'idee sans jargon opaque

**Scikit-learn** est une bibliotheque Python tres utilisee pour le **machine learning** "classique". Tu n'es pas oblige de coder aujourd'hui pour comprendre son esprit. L'idee : une grammaire commune pour splitter, transformer, entrainer, predire, evaluer. Les noms d'algorithmes changent ; le verbe reste : **fit**, **transform**, **predict**, score.

:::retenir
Scikit-learn = grammaire fit / transform / predict. La discipline compte plus que le nom de l'algo.
:::

## La grammaire mentale

Tu as un tableau X (lignes = exemples, colonnes = **features**) et souvent un vecteur y. Tu crees un objet modele. Tu appelles fit(X_train, y_train) : il apprend. Tu appelles predict(X_test) : il propose. Tu calcules une **metrique** entre y_test et les predictions. Pour les transformateurs (imputation, scaling, encodage), fit apprend les parametres sur le train, transform applique.

Script minimal "bout en bout" :

```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

X, y = load_diabetes(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)

modele = LinearRegression().fit(Xtr, ytr)
pred = modele.predict(Xte)
print("MAE test", round(mean_absolute_error(yte, pred), 2))
```

Remplace ensuite LinearRegression par un arbre, compare MAE, et garde le plus simple qui bat ta baseline.

## Pipeline dans scikit-learn

Tu enchaines transformateurs + modele dans un **Pipeline**. Un seul fit sur le train. Un seul predict sur le nouveau. Moins de fuite. Plus propre. C'est exactement le chapitre pipeline mis en code. Meme si tu utilises un autre outil plus tard, cette discipline reste.

:::astuce
Sans ecrire de code, decris mentalement : colonnes de X, colonne y, premier modele simple, metrique. Si tu codes, commence par battre une baseline.
:::

## Ce que scikit-learn fait bien

Modeles solides pour tableaux (regression, classification, clustering). Outils de validation croisee, recherche de reglages, metriques. Excellent pour apprendre. Limites : ce n'est pas le coeur du deep learning a grande echelle (autres librairies), ni le traitement du langage type LLM. Pour Noe sur un CSV de commandes, c'est souvent le bon terrain.

:::attention
Ne scale pas sur tout le dataset avant le split. Fit des transformateurs sur le train uniquement - meme piege, meme regle.
:::

## Mini parcours d'apprentissage code (optionnel)

1) Charger un CSV. 2) Separer train/test. 3) Pipeline simple (encodage + modele lineaire ou arbre). 4) Score. 5) Matrice de confusion ou erreurs. 6) Inspecter. Tu peux suivre n'importe quel tutoriel officiel en gardant les idees de ce livre comme boussole anti-pieges.

## Erreur classique

Copier un notebook qui scale sur tout le dataset avant split. Ou choisir un modele complexe parce que le nom impressionne. Ou oublier de fixer le traitement des categories inconnues en production.

## A toi

Sans ecrire de code, decris l'appel mental : quelles colonnes dans X, quelle colonne y, quel modele simple en premier, quelle metrique. Si tu codes deja, implemente la baseline cette semaine.

## Ecosysteme voisin

Pandas pour les tableaux, matplotlib/seaborn pour voir, jupyter pour explorer, puis un script propre pour produire. Scikit-learn se place au milieu : modeles et metriques. Plus tard, d'autres outils viendront ; la discipline fit/transform restera.

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
