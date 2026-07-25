# Chapitre 9 - Les listes

Une **liste** range plusieurs valeurs, une apres l'autre. Courses, notes, prenoms, scores : des suites ordonnees. L'**index** commence a 0. `-1` pointe le dernier element. Ce n'est pas un detail de puriste. C'est la source d'une tonne d'erreurs "off-by-one" chez les debutants - et chez les autres aussi, les soirs de fatigue.

Chez DanielCraft, on traite la liste comme le premier vrai conteneur du quotidien. Lea stocke des URLs a verifier. Max range des lignes de fournitures. Sam construit une liste de questions. Quand tu sais ajouter, parcourir, tester `in`, trancher et trier, tu debloques la moitie des petits scripts utiles. Trois metiers, meme muscle : une rangee de cases, des gestes clairs.

```python
courses = ["pain", "lait", "oeufs"]
print(courses[0])  # pain
print(courses[-1]) # oeufs (dernier)
```

## Ce que ce n'est pas

Une liste, ce n'est pas un dictionnaire : ici l'ordre et la position comptent, pas une cle nommee. Ce n'est pas non plus un tuple : la liste se modifie, le tuple est fige. Ce n'est pas une excuse pour tout mettre dans une seule megasoupe sans structure. Et ce n'est surtout pas "trop basique pour etre pro" : les listes sont partout, y compris dans du code serieux. Lea dit : "si je dois dire le troisieme element, c'est une liste".

Une rangee de cases numerotees. La case 0 contient "pain". Tu peux remplacer, ajouter a la fin (`append`), inserer au debut, retirer. `len(courses)` compte. Une boucle `for item in courses` visite chaque case. Une tranche `nums[1:4]` decoupe une portion sans tout casser. Si tu imagines bien la rangee, les methodes deviennent evidentes. Chez DanielCraft, on dessine parfois ces cases au tableau. Une image nette bat dix definitions abstraites.

Max visualise ses fournitures. Sam visualise ses questions. Lea visualise une todo. Trois rangees, meme logique.

:::attention
Le premier element est a l'index 0, pas 1. Le dernier index valide vaut `len - 1`, ou utilise `-1`.
:::

## Modifier, ajouter, parcourir

```python
courses[1] = "lait d'avoine"
print(len(courses))

courses.append("beurre")
courses.insert(0, "eau")
dernier = courses.pop()
courses.remove("pain")  # enleve la premiere occurrence

for item in courses:
    print("-", item)

if "pain" in courses:
    print("On a du pain")
```

`in` se lit naturellement. Lea l'utilise pour eviter les doublons avant d'ajouter. Sam l'utilise dans des exercices "est-ce que ce mot est dans la liste ?". Max l'utilise avant d'ajouter une fourniture deja presentee.

## Tranches, tri, comprehension

```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])   # 1,2,3
print(nums[:3])    # 0,1,2
print(nums[3:])    # 3,4,5
print(nums[::-1])  # inverse
```

```python
notes = [12, 8, 15, 10]
print(sorted(notes))       # nouvelle liste
notes.sort()               # modifie sur place
notes.sort(reverse=True)
```

Attention : **sorted** renvoie une nouvelle liste, **sort** modifie sur place. Lea prefere souvent `sorted` pour ne pas ecraser l'original sans le vouloir. Chez DanielCraft, on insiste sur cette difference parce qu'elle casse des scripts "qui marchaient hier".

List comprehension (avance soft) :

```python
carres = [n * n for n in range(1, 6)]
print(carres)  # [1, 4, 9, 16, 25]

pairs = [n for n in range(10) if n % 2 == 0]
```

C'est une boucle `for` en une ligne. Lisible si c'est court. Sinon, garde une boucle classique. On refuse le style "incomprehension" deguisee en elegance.

## Tuple et set (apercus)

```python
point = (10, 20)
# point[0] = 11  # erreur : tuple non modifiable
```

Utile pour des paires fixes (coordonnees, resultat double...).

```python
tags = {"python", "debutant", "python"}
print(tags)  # les doublons sautent
```

Le **set** enleve les doublons. Max l'a utilise sans le savoir quand Sam lui a montre `set(liste)`. Apercu suffisant pour ce livre. Tu n'as pas a devenir expert des ensembles. Tu as a reconnaitre le mot.

:::astuce
Pour une moyenne : boucle + total + `len`. Verifie a la main une fois. Puis seulement, joue avec une comprehension.
:::

## Petite histoire

Sam a fait calculer une moyenne a partir d'une liste de notes. Premier reflexe eleve : additionner a la main quatre `print`. Deuxieme reflexe : boucle + total + `len`. Troisieme : comprehension pour filtrer les notes >= 10. Lea, elle, inverse une liste de taches avec `[::-1]` pour afficher la plus recente en premier. Max construit sa liste de jeux, ajoute un titre, affiche le dernier. Trois gestes, une meme famille d'outils. Chez DanielCraft, on celebre ce moment : tu ne manipules plus "une variable, puis une autre", tu manipules une collection.

## Erreur classique

Croire que l'index commence a 1. Modifier une liste pendant que tu la parcours sans savoir ce que tu fais. Confondre `sorted` et `sort`. Faire `courses[len(courses)]` et sortir des bornes (le dernier index valide est `len - 1`, ou utilise `-1`). Autre piege : `remove` d'une valeur absente, qui leve une erreur - teste avec `in` avant si besoin. Lea a deja perdu vingt minutes sur un IndexError "inexplicable" : elle comptait comme un humain, a partir de 1.

## En vrai

Fais une liste de notes. Calcule la moyenne avec une boucle. Puis, a partir de `[1,2,3,4,5,6]`, cree la liste des pairs avec une comprehension. Verifie a la main. L'habitude de verifier bat la confiance aveugle.

## A toi

Liste de 4 jeux. Ajoute-en un avec `append`. Affiche tout avec une boucle. Affiche aussi le dernier avec `[-1]`. Bonus : trie la liste et affiche les deux premiers avec une tranche. Garde ce fichier. Au chapitre dictionnaires, tu mettras des fiches a la place de simples chaines.

## Zoom : index 0, pourquoi ?

Les ordinateurs comptent souvent depuis zero. Ce n'est pas pour t'embeter. C'est une convention utile pour les calculs d'adresse. Toi, tu retiens une regle nette : premier element = index 0, dernier = index -1. Si tu hesites, affiche `len` et teste. Chez DanielCraft, on prefere un petit test a une longue peur.
