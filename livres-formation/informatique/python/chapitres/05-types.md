# Chapitre 5 - Les types (texte, nombre, vrai/faux)

Les **types**, c'est la nature de ce que tu ranges dans la boite. Texte, nombre entier, nombre a virgule, vrai/faux : ce n'est pas du jargon pour faire joli. C'est la raison pour laquelle `"3" + "1"` donne `"31"` et `3 + 1` donne `4`. Si tu ignores le type, tu te bats contre des fantomes. Si tu le regardes, les erreurs deviennent lisibles.

Chez DanielCraft, on enseigne les types tot parce que `input` renvoie toujours du texte. Lea a deja envoye un script client qui collait des chiffres au lieu de les additionner. Max a cru que son devis "additionnait" alors qu'il concatenait. Sam commence chaque atelier par `type(...)` au tableau. Une habitude, pas un detail. Tu gagnes des heures en posant cette question tot : "qu'est-ce que j'ai vraiment dans la boite ?"

## Ce que ce n'est pas

Connaitre les types, ce n'est pas memoriser un catalogue academique. Ce n'est pas non plus "annoter tous tes programmes comme en Java" des le jour un. Ce n'est pas une excuse pour avoir peur de convertir. Et ce n'est surtout pas optionnel : sans conversion, tes calculs a partir de `input` mentent gentiment. Un mensonge poli, c'est encore un mensonge - surtout sur un devis.

Quatre boites courantes. **str** : une chaine de caracteres, entre guillemets. **int** : un entier. **float** : un nombre a virgule. **bool** : `True` ou `False`, avec majuscule. Plus tard, listes et dictionnaires. Pour l'instant, maitrise ces quatre. Quand quelque chose cloche, demande-toi : "qu'est-ce que j'ai vraiment dans la boite ?" Puis verifie avec `type()`. Lea le fait encore. Max aussi. Sam l'exige avant toute aide.

:::astuce
`input("Age ? ")` donne `"12"` (texte). `int(...)` transforme en `12` (nombre). Sans ca, `"12" + "1"` devient `"121"`.
:::

## Les quatre de base

```python
phrase = "Bonjour"
ville = 'Lyon'  # simples ou doubles, au choix
vies = 3
prix = 19.99
est_connecte = True
a_fini = False
```

Attention : `True` / `False` avec majuscule. Pas `true` comme en JavaScript. Lea a perdu cinq minutes la-dessus en passant d'un langage a l'autre. Normal. Note-le. Sam met un post-it "True avec T" sur le coin de l'ecran la premiere semaine. Ca marche.

## Conversion depuis input

`input` donne du texte. Pour calculer, convertis :

```python
age_texte = input("Age ? ")
age = int(age_texte)
print("Dans 10 ans :", age + 10)
```

Versions courtes :

```python
n = int(input("Nombre ? "))
prix = float(input("Prix ? "))
```

Si la personne ecrit "douze", `int(...)` plante. Normal. Au chapitre exceptions, on apprendra a rattraper ca. Ici, tu acceptes que le programme exige un vrai nombre. Max teste toujours avec `abc` pour voir l'erreur. Bon reflexe de pilote. Tu ne cherches pas a tout proteger encore. Tu cherches a comprendre ce qui casse.

## type(), pieges, None

```python
print(type(3))      # int
print(type("3"))    # str
print(type(3.0))    # float
print(type(True))   # bool
```

Pieges classiques :

```python
print("3" + "1")   # "31" (colle du texte)
print(3 + 1)       # 4
# print("3" + 1)   # TypeError
```

Et :

```python
print(bool(""))     # False (texte vide)
print(bool("0"))    # True (texte non vide)
print(bool(0))      # False
```

**None** veut dire "pas de valeur" volontaire :

```python
valeur = None
```

Tu le croiseras avec les fonctions qui ne renvoient rien. Sam dit : "`None`, c'est le silence explicite". Utile comme image. Lea l'utilise parfois comme "pas encore calcule". Max prefere un message clair quand c'est une erreur - on verra ca avec les exceptions.

:::attention
`bool("False")` vaut `True` : la chaine n'est pas vide. Convertis d'abord, compare ensuite.
:::

## Petite histoire

Max a demande un prix, ajoute "20%" a la main dans sa tete, puis a voulu le coder. Premier essai : `prix + "20%"`. Plantage. Deuxieme essai : il convertit en `float`, calcule `prix * 1.20`, affiche. Le devis devient honnete. Lea, elle, utilise `float` pour des montants et garde les arrondis sous controle avec `round(...)` quand elle affiche. Chez DanielCraft, on prefere un calcul clair a une magie opaque.

Autre scene : Sam ecrit `"12" == 12` au tableau. Les eleves votent. Beaucoup disent vrai. Python dit `False`. Silence. Puis `type` sur chaque cote. Le clic mental arrive. C'est ca qu'on veut : voir avant de theoriser.

## Erreur classique

Additionner sans convertir. Ou croire que `bool("False")` est `False` : non, c'est `True`, parce que la chaine n'est pas vide. Autre piege : comparer un nombre et un texte (`12 == "12"` est `False`). Convertis d'abord, compare ensuite. Et encore : croire que `float("19,99")` marche avec une virgule francaise - souvent non. Remplace, ou normalise, puis convertis.

## En vrai

Ouvre la console interactive. Teste `type()` sur 4 valeurs differentes. Puis ecris un mini script TVA : demande un prix en texte, convertis en `float`, ajoute 20%, affiche le TTC. Verifie a la main avec une calculatrice. Si les deux resultats collent, tu pilotes. Si non, regarde le type avant de paniquer.

## A toi

Demande deux nombres (via `input` + `int`). Affiche leur somme, leur difference, leur produit. Bonus : affiche aussi le type de chaque resultat avec `type(...)`. Super bonus : demande un prix en `float` et affiche le TTC arrondi a deux decimales avec `round(...)`.

## Zoom : pourquoi Python est "souple"

Python ne t'oblige pas a declarer le type a l'avance. Ca va vite. Ca peut aussi cacher des erreurs. La souplesse n'est pas une permission d'etre flou. C'est une invitation a verifier. Quand tu doutes, `print(valeur, type(valeur))` est ton ami. Lea le laisse parfois en commentaire de debug cinq minutes, puis l'enleve. Sam oblige les eleves a le faire avant de demander de l'aide. Chez DanielCraft, on appelle ca "voir avant de theoriser". Tu garderas ce geste toute ta vie de code, meme avec des outils plus riches.
