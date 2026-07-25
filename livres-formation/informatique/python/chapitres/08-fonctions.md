# Chapitre 8 - Les fonctions

Une **fonction**, c'est une recette reutilisable. Tu la definis une fois. Tu l'appelles quand tu veux. Sans fonctions, tu copies le meme bloc partout, tu corriges six fois la meme faute, tu te perds. Avec des fonctions, tu nommes une intention : `dire_salut_a`, `moyenne`, `note_sur_20`. Lea range ses validations dans des fonctions. Max met son calcul de marge dans une fonction. Sam demande une fonction par exercice "propre".

Chez DanielCraft, on separe tot deux gestes : `print` affiche, **return** renvoie une valeur au code appelant. Ce n'est pas la meme chose. Beaucoup de debutants mettent des `print` partout dans la fonction et s'etonnent de ne pas pouvoir reutiliser le resultat. Apprends `return` tot. Ton code grandit mieux. Une fonction qui ne sait que "montrer" est une demo. Une fonction qui "renvoie" est une brique.

```python
def dire_salut():
    print("Salut !")

dire_salut()
dire_salut()
```

## Ce que ce n'est pas

Une fonction, ce n'est pas "du code avance obligatoire des la ligne 1". Ce n'est pas non plus une classe (ca vient plus tard). Ce n'est pas une excuse pour faire des fonctions de 200 lignes qui font dix metiers. Une bonne fonction fait une chose claire. Et ce n'est surtout pas interchangeable avec un commentaire : le nom de la fonction doit deja raconter l'intention. Si tu as besoin d'un roman pour expliquer `f2`, renomme.

Tu ecris une fiche recette `def gateau_chocolat(nb_parts):`. Plus tard, tu appelles la recette avec 6 parts ou 8 parts. Les ingredients changent via les **parametres**. Le resultat peut etre renvoye (`return`) pour etre utilise ailleurs : stocke dans une variable, affiche, compare. Si la fonction ne renvoie rien d'explicite, tu obtiens `None`. Ce n'est pas un bug mysterieux. C'est le silence par defaut.

:::retenir
`print` montre a l'humain. `return` donne une valeur au code. Ce n'est pas interchangeable.
:::

## Parametres, return, defauts

```python
def dire_salut_a(prenom):
    print(f"Salut {prenom}")

dire_salut_a("Nora")
dire_salut_a("Sam")
```

```python
def double(n):
    return n * 2

resultat = double(4)
print(resultat)  # 8
```

Valeur par **defaut** :

```python
def saluer(prenom="ami"):
    print(f"Salut {prenom}")

saluer()
saluer("Lea")
```

Plusieurs parametres :

```python
def moyenne(a, b):
    return (a + b) / 2

print(moyenne(12, 16))
```

Petite doc utile :

```python
def carre(n):
    # Renvoie n au carre
    return n * n
```

Plus tard tu verras les "docstrings" (texte entre triples guillemets). Meme idee : expliquer le role. Lea ecrit une phrase. Max ecrit le "pourquoi" du coefficient. Sam exige au moins le role quand la fonction n'est pas evidente.

## *args (apercu avance)

Parfois tu veux un nombre variable d'arguments :

```python
def somme(*nombres):
    total = 0
    for n in nombres:
        total += n
    return total

print(somme(1, 2, 3, 4))  # 10
```

Tu n'es pas oblige de l'utiliser tout de suite. Mais tu le croiseras dans du vrai code. Lea l'a vu dans une librairie et a compris grace a cet apercu. Mieux vaut l'avoir croise une fois que de paniquer devant l'etoile.

:::astuce
Ecris d'abord une petite fonction qui renvoie True/False (`est_pair`). Teste-la seule. Puis branche-la dans un programme plus grand.
:::

## Pourquoi c'est bien

Tu copies moins. Le code devient plus clair. C'est plus facile a corriger, parce que tu testes une brique a la fois. Sam fait ecrire `est_pair(n)` avant d'ecrire un programme complet : True/False, tests avec 2, 3, 10. Si la brique est solide, le mur tient. Lea decoupe ses scripts clients des qu'elle se surprend a copier-coller un bloc. Max a appris apres un devis faux : une formule a trois endroits, un oubli, un client mecontent.

## Exemple complet

```python
def note_sur_20(points, total):
    if total == 0:
        return 0
    return round(points / total * 20, 1)

print(note_sur_20(15, 20))
print(note_sur_20(7, 10))
```

Regarde le garde-fou `total == 0`. Une fonction propre anticipe les cas betes. Chez DanielCraft, on aime ces petites protections plus que les discours sur "le clean code". Une ligne qui evite une division par zero, c'est du soin concret.

## Petite histoire

Max calculait sa marge en recopiant la formule a trois endroits. Il a change un coefficient, oublie un endroit, envoye un devis faux. Depuis, une seule fonction `marge(prix_vente, cout)`. Il l'appelle partout. Lea fait pareil pour formater un prix TTC. Sam note autant la clarte du nom que le resultat. Trois pratiques, une lecon : une idee, un endroit.

Autre scene DanielCraft : Lea ouvre un vieux script. Elle voit `calc`, `calc2`, `calc_final`. Elle renomme, extrait, respire. Le client n'a rien vu. Elle, si : elle peut enfin modifier sans peur.

## Erreur classique

Oublier `return` et croire que `print` "renvoie". Confondre parametre et variable globale. Mettre trop de logique dans une seule fonction. Autre piege : appeler la fonction sans parentheses dans un contexte ou tu voulais le resultat (`print(double)` affiche la fonction, pas `8`). Tu veux `print(double(4))`. Et encore : une fonction "fourre-tout" qui lit un fichier, calcule, et envoie un mail. Decoupe. Tu respireras.

## En vrai

Ecris `est_pair(n)` qui renvoie True/False. Teste avec 2, 3, 10. Puis `presenter(prenom, age)` qui retourne une phrase (pas print) : tu printes le resultat a l'exterieur. Sens la difference : la fonction donne, le programme montre. C'est le geste qui change tout pour la suite (tests, reutilisation, classes).

## A toi

Ecris `moyenne(a, b)` qui renvoie la moyenne. Puis `moyenne3(a, b, c)`. Teste. Bonus : gere le cas ou tu recois des textes convertibles en `float` a l'interieur de la fonction. Super bonus : ajoute un garde-fou si la conversion echoue (message clair, ou `None`).

## Zoom : nommer, c'est deja concevoir

Avant d'ecrire le corps, dis le nom a voix haute. `calculer_ttc`, `est_majeur`, `charger_notes`. Si tu galeres a nommer, c'est souvent que la fonction fait trop de choses. Chez DanielCraft, on prefere trois noms ennuyeux a un nom heroique flou. Lea renomme souvent avant de refactorer. Max a appris que `f` n'aide personne a 23h. Sam barre au tableau les noms d'une lettre hors boucles courtes. Le nom est le premier test de clarte.
