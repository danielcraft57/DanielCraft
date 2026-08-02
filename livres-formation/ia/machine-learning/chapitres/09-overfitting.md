# Chapitre 9 - Overfitting : trop coller a l'entrainement

L'**overfitting**, c'est quand le modele apprend par coeur les particularites du train (y compris le bruit) et generalise mal sur des cas nouveaux. Image : un etudiant qui recite le corrige des exercices deja vus et se plante a l'examen. Score train splendide. Score test decevant. En production, encore pire.

:::retenir
Overfitting = coller au train, rater le futur. Un 100 % train est souvent un aveu, pas un trophee.
:::

## Sous-apprentissage aussi

A l'inverse, l'**underfitting**, c'est un modele trop simple qui rate meme les motifs reels. Score train mediocre, test mediocre. Tu veux la zone ou le modele capture le signal sans epouser le bruit.

## Signes qui doivent t'alerter

Ecart **train/test** large. Arbre tres profond. Trop de **features** par rapport aux exemples. Performances magiques peu believable. Importance d'IDs ou de timestamps suspects. Forte sensibilite a une petite perturbation des donnees.

Mini demo (arbre trop profond vs profondeur limitee) :

```python
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(80, 1))
y = (3 * X[:, 0] + rng.normal(scale=0.8, size=80))

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=0)
profond = DecisionTreeRegressor(max_depth=None).fit(Xtr, ytr)
simple = DecisionTreeRegressor(max_depth=2).fit(Xtr, ytr)

def mae(m):
    return (
        mean_absolute_error(ytr, m.predict(Xtr)),
        mean_absolute_error(yte, m.predict(Xte)),
    )

print("profond train/test MAE", tuple(round(v, 3) for v in mae(profond)))
print("simple  train/test MAE", tuple(round(v, 3) for v in mae(simple)))
```

Souvent le profond a un train excellent et un test mediocre : overfitting visible.

:::attention
Si le score train est excellent et le test mediocre, arrete d'ajouter de la complexite. Simplifie, regularise, ou revois les donnees.
:::

## Remedes pratiques

Plus de donnees utiles (pas seulement plus de lignes dupliquees). **Regularisation** / profondeur limitee. Moins de features pourries. Ensembles d'arbres bien regles. Early stopping dans certains apprentissages. Surtout : protocole train/test honnete et inspection des erreurs. Parfois le vrai remede est de simplifier la question metier.

:::astuce
Compare toujours train et test cote a cote. L'ecart raconte plus qu'un seul chiffre isole.
:::

## Lien avec l'IA generative

Les LLM aussi peuvent "surapprendre" des styles ou des faits memorises, mais le vocabulaire et les outils different. Ici, reste sur l'image examen : ce qui compte, c'est la performance hors des exemples vus, dans des conditions proches du futur.

## Erreur classique

Ajouter de la complexite des qu'un score train n'est pas 100 %. Le 100 % train est souvent un aveu, pas un trophee.

## A toi

Imagine un modele qui predit parfaitement ton historique. Donne 3 raisons pour lesquelles il pourrait echouer la semaine prochaine.

## Regularisation en mots simples

Freiner la complexite : penaliser les poids trop grands, limiter la profondeur, exiger plus d'exemples par feuille d'arbre, arreter l'apprentissage tot. Ce n'est pas "rendre le modele bete". C'est l'empecher d'apprendre le bruit.

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
