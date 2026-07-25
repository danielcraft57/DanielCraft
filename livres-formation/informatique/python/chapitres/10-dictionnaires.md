# Chapitre 10 - Les dictionnaires

Un **dictionnaire**, ce n'est pas une liste numerotee. C'est une fiche avec des **cles** : `"prenom"`, `"score"`, `"actif"`. Tu ranges des paires cle -> valeur. Tu retrouves une info par son nom, pas seulement par sa position. En vrai projet, tu croises ca partout : configs, joueurs, produits, reponses d'API, fichiers JSON. Des que les donnees ont des "etiquettes", le dictionnaire devient ton ami.

Chez DanielCraft, on presente le dictionnaire juste apres la liste parce que les deux se combinent : une liste de dictionnaires, c'est deja une mini base de donnees en memoire. Lea stocke des clients (anonymises). Max stocke des produits `{nom, prix}`. Sam stocke des eleves. Meme structure, metiers differents. Tu vas reconnaitre ce motif dans le reste du livre, puis dans le livre Python pratique.

```python
joueur = {
    "prenom": "Sam",
    "score": 120,
    "actif": True,
}

print(joueur["prenom"])
joueur["score"] = joueur["score"] + 10
joueur["niveau"] = 2  # nouvelle cle
```

## Ce que ce n'est pas

Un dictionnaire, ce n'est pas un fichier Word. Ce n'est pas non plus "obligatoirement du JSON" : **JSON** est un format texte ; le dictionnaire Python est une structure en memoire. Ils se ressemblent, ils se parlent via `json.load` / `json.dump`, mais ce n'est pas identique. Ce n'est pas une excuse pour des cles magiques eparpillees (`"n"`, `"x2"`, `"data"`). Et ce n'est surtout pas safe d'acceder avec `dico[cle]` si la cle peut manquer : prefere parfois `.get`.

Ce n'est pas non plus un remplacement de la liste. Si l'ordre et la position comptent plus que le nom, reste sur une liste. Si tu cherches "par etiquette", prends un dico. Lea dit : "si je dois expliquer la donnee a un client, j'utilise des cles lisibles".

Une fiche cartonnee avec des etiquettes. Tu cherches "score", tu lis 120. Tu changes le score. Tu ajoutes "niveau". Tu parcours toutes les etiquettes avec `.items()`. Si une etiquette n'existe pas, `.get("niveau", 1)` te donne une valeur par defaut au lieu d'exploser. La liste, elle, serait "premiere case, deuxieme case". Ici, tu nommes. Chez DanielCraft, on aime les structures qui se lisent a voix haute sans jargon.

Lea visualise une fiche client. Max visualise une fiche produit. Sam visualise une fiche eleve. Trois fiches, meme geste : ouvrir, lire une cle, modifier, sauvegarder plus tard.

:::astuce
Prefere `.get("cle", defaut)` quand une cle peut manquer. Tu evites une KeyError pour une info optionnelle.
:::

## Cle absente, parcours, liste de dicos

```python
print(joueur.get("niveau", 1))
```

Si "niveau" n'existe pas, tu obtiens 1. Avec `joueur["niveau"]` direct : erreur si absent. Cette difference parait petite. Elle evite des plantages sur des donnees incompletes.

```python
for cle, valeur in joueur.items():
    print(cle, "->", valeur)

print(joueur.keys())
print(joueur.values())
```

```python
equipe = [
    {"prenom": "Sam", "score": 120},
    {"prenom": "Lea", "score": 95},
]
print(equipe[0]["prenom"])

for j in equipe:
    print(f"{j['prenom']} : {j['score']}")
```

Cette forme **liste de dictionnaires** est partout. Apprends a la lire a voix haute : "pour chaque joueur j dans equipe, affiche prenom et score". Sam fait repeter cette phrase. Max l'a reutilisee pour ses produits. Lea pour ses projets.

## Compter avec un dico

```python
mots = ["chat", "chien", "chat", "oiseau", "chat"]
compteur = {}
for mot in mots:
    compteur[mot] = compteur.get(mot, 0) + 1
print(compteur)
```

Pattern tres courant. Sam le montre pour compter des reponses. Lea l'utilise pour des tags. Max pour des categories de depense. Une fois vu, tu le reconnaitras dans beaucoup de tutos. Tu n'as pas besoin d'une bibliotheque speciale pour ce geste debutant.

## JSON dans la tete

Un dictionnaire Python ressemble beaucoup a du JSON. Tu t'en serviras pour sauvegarder des configs, des scores, des echanges avec des services. Au chapitre fichiers, tu ecriras vraiment `joueur.json`. Ici, retiens l'idee : cles nommees, valeurs typees, structure imbriquee possible. Chez DanielCraft, on prepare le terrain avant d'ouvrir le fichier : d'abord penser la structure, ensuite ecrire.

:::retenir
Liste = position. Dictionnaire = etiquette. Liste de dicos = plusieurs fiches.
:::

## Petite histoire

Lea recevait des infos "en vrac" dans quatre variables. Elle les a rangees dans un dico `projet`. Le script est devenu plus court, les affichages plus clairs, la sauvegarde JSON evidente. Max a fait une liste de 3 produits et calcule le total des prix avec une boucle. Sam a cree une fiche eleve, modifie la moyenne, reaffiche. Chez DanielCraft, on celebre ce moment : tu ne manipules plus "des variables perdues", tu manipules une structure. C'est le passage du bricolage a l'outil.

## Erreur classique

Typer une cle (`"Prenom"` vs `"prenom"`). Oublier les guillemets autour de la cle. Croire que l'ordre des cles "doit" toujours etre alphabetique pour que ca marche (ce n'est pas ta priorite debutant). Acceder sans `.get` a une cle optionnelle. Autre piege : modifier un dico en le parcourant de facon hasardeuse - construis plutot une nouvelle structure si tu filtres. Lea a deja perdu une soiree sur une KeyError "inexplicable" : la cle etait la, mais avec une majuscule en trop.

## En vrai

Fais une petite "fiche eleve" (nom, moyenne, classe). Modifie la moyenne. Reaffiche. Puis une liste de 3 produits `{nom, prix}` et le total des prix. Verifie a la main le total une fois. L'habitude de verifier bat la confiance aveugle.

## A toi

Cree un dico `livre` avec titre, pages, lu (True/False). Affiche une phrase complete. Ajoute une cle `auteur`. Bonus : mets deux livres dans une liste et affiche ceux avec `lu == True`. Garde ce fichier. Au chapitre suivant, tu pourras le sauver en JSON.

## Zoom : dico vs liste, comment choisir

Si tu dis "le troisieme element", pense liste. Si tu dis "le score du joueur", pense dictionnaire. Si tu dis "tous les joueurs, et pour chacun un score", pense liste de dictionnaires. Cette phrase simple evite des heures de confusion. Chez DanielCraft, on la recolle mentalement avant chaque structure. Tu n'as pas besoin d'etre architecte. Tu as besoin d'un choix conscient.
