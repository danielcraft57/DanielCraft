# Chapitre 11 - Pipeline : enchainer proprement les etapes

Un **pipeline**, c'est une chaine : preparation des **features**, modele, prediction. L'interet n'est pas cosmétique. C'est d'eviter la triche et le chaos : les memes transformations au train et au test, dans le bon ordre, sans fuite, reproductibles.

:::retenir
Pipeline = meme chaine train et prod, fit sur le train seulement. Moins de fuite, plus de clarte.
:::

## Etapes typiques

1) Lecture des donnees. 2) Split. 3) Traitement des manquants (ajuste sur train). 4) Encodage des categories. 5) Scaling si besoin. 6) Modele. 7) Evaluation. 8) Export du modele + des transformateurs. En production, tu rejoues la meme chaine sur une nouvelle ligne.

## Pourquoi scikit-learn aime ca

Dans l'esprit **scikit-learn** (chapitre suivant), on branche des etapes qui exposent **fit** / **transform** / predict. Tu fais fit sur le train, transform sur le test, predict. Si tu ajoutes une etape, tu l'inseres dans la chaine, tu ne recopies pas six scripts divergents. Moins d'erreurs humaines. Plus de clarte.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X = [[1.0], [1.2], [3.5], [3.7], [1.1], [4.0]]
y = [0, 0, 1, 1, 0, 1]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.33, random_state=0)

pipe = Pipeline([
    ("scale", StandardScaler()),
    ("clf", LogisticRegression()),
])
pipe.fit(Xtr, ytr)           # scale + modele : fit sur train seulement
print(pipe.predict(Xte))     # memes etapes sur le test
print("score", pipe.score(Xte, yte))
```

Le scaler n'a jamais "vu" le test pendant fit : moins de fuite.

:::astuce
Dessine le pipeline en boites avant de coder. Marque clairement ou se fait le fit et ou se fait le transform.
:::

## Reproductibilite

Fixe les graines aleatoires quand c'est pertinent. Versionne le code et note la version des donnees. Documente les definitions de features. Un modele non reproductible est un souvenir, pas un actif.

## Monitoring apres deploiement

Les donnees derivent : nouveaux produits, nouvelle saison, nouveau comportement. Surveille les distributions de features et les **metriques** dans le temps. Prevois un reentrainement. Un pipeline sans monitoring est une fusee sans tableau de bord.

:::attention
Un notebook de recherche different du script de prod, c'est le piege classique. Unifie tot, sinon le score labo ne veut plus rien dire.
:::

## Erreur classique

Preprocessing "a la main" different entre le notebook de recherche et le script de prod. Le score labo ne veut plus rien dire. Unifie tot.

## A toi

Dessine ton pipeline en 6 boites. Marque ou se fait le fit, ou se fait le transform, ou se calcule la metrique.

## Tests du pipeline

Meme sans framework lourd : une ligne typique traverse la chaine ; une ligne avec manquants ; une categorie inconnue ; une date future. Si ca casse en silence, tu le sauras trop tard. Automatise ces cas des que tu peux.

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
