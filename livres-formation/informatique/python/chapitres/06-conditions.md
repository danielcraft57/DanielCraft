# Chapitre 6 - Les conditions (if)

Les **conditions**, c'est le moment ou ton programme cesse d'etre une suite lineaire et commence a choisir. "Si ... alors ... sinon ...". Sans conditions, tu affiches toujours la meme chose. Avec des conditions, tu adaptes : majeur ou mineur, mot de passe OK ou refuse, score suffisant ou pas. Lea s'en sert pour valider un formulaire avant d'envoyer un mail. Max pour savoir si sa marge de devis est correcte. Sam pour noter automatiquement un quiz simple. Trois metiers, meme muscle : poser une question claire, puis prendre une route.

Chez DanielCraft, on insiste sur l'**indentation** des le premier `if`. En Python, le decalage n'est pas decoratif. C'est la structure. Quatre espaces. Sans ca, Python refuse. Ce n'est pas une lubie : c'est la facon dont le langage lit les blocs. Si tu viens d'un autre langage avec des accolades, ce sera le premier choc. Ensuite, tu ne pourras plus t'en passer : le code se lit comme un plan.

```python
age = 15

if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

## Ce que ce n'est pas

Une condition, ce n'est pas "de la logique avancee reservee aux experts". Ce n'est pas non plus une excuse pour imbriquer dix `if` illisibles dans une seule fonction. Ce n'est pas la meme chose qu'une boucle : ici tu decides une fois (ou quelques fois), tu ne repetes pas automatiquement. Et ce n'est surtout pas `=` pour comparer : `=` assigne, **==** compare. Ce piege revient chez presque tout le monde, Lea et Max inclus. Sam le note en rouge au tableau des le premiere semaine.

Ce n'est pas non plus "tout tester d'un coup". Une condition claire vaut mieux qu'un monstre de `and` / `or` que tu ne comprends plus demain matin. Decoupe. Nomme. Relis a voix haute.

Tu arrives a un carrefour. Une question claire. Si oui, tu prends une route. Sinon, une autre. Parfois il y a plusieurs panneaux : **elif** = "sinon si". Tu peux en chainer plusieurs. A la fin, un `else` rattrape le reste. Plus le carrefour est clair, moins tu te perds. Si ta question est floue (`if score:` sans savoir ce que tu testes vraiment), le comportement devient etrange. Lea lit ses conditions a voix haute avant de coder. Si la phrase orale est confuse, le code le sera aussi.

Chez DanielCraft, on aime cette habitude : d'abord la phrase humaine, ensuite les symboles. "Si j'ai un ticket ou si je suis VIP, j'entre". Puis seulement `if ticket or vip:`.

:::attention
`=` range une valeur. `==` compare. Melanger les deux est le piege numero un des conditions.
:::

## elif, comparaisons, and / or / not

```python
note = 14

if note >= 16:
    print("Excellent")
elif note >= 10:
    print("Valide")
else:
    print("On revise")
```

Comparaisons utiles : `==`, `!=`, `>`, `<`, `>=`, `<=`. Tu les croiseras partout. Apprends-les comme le code de la route : pas pour briller, pour ne pas te planter au premier croisement.

```python
ticket = True
vip = False

if ticket or vip:
    print("Entre")

if ticket and vip:
    print("Acces premium")

if not vip:
    print("Pas VIP")
```

**and** exige les deux. **or** accepte l'un ou l'autre. **not** inverse. Max a mis longtemps a confondre `and` et `or` sur ses devis : "si marge OK et client OK" n'est pas "si marge OK ou client OK". Une seule lettre change le metier.

## Conditions avec texte et ternaire

```python
mdp = input("Mot de passe ? ").strip()
if mdp == "python123":
    print("OK")
else:
    print("Refuse")
```

Souvent on compare en minuscules, parce que les humains tapent comme ils veulent :

```python
if mdp.lower() == "python123":
    print("OK")
```

Operateur ternaire (apercu) :

```python
age = 20
statut = "majeur" if age >= 18 else "mineur"
print(statut)
```

Pratique pour une petite decision. Pas obligatoire. Sam dit : "si tu as besoin d'un commentaire pour comprendre ton ternaire, ecris un `if` normal". Chez DanielCraft, la lisibilite gagne toujours contre la ruse d'une ligne.

## Petite histoire

Max a code un "si temperature < 0 -> froid". Premier essai, il a mis `=` au lieu de `==`. Python a proteste ou a fait autre chose selon le cas. Deuxieme essai, correctement compare. Il a teste -2, 10, 25. Trois sorties differentes. Il a compris mieux qu'avec un cours abstrait. Lea, elle, valide des seuils de budget avant d'envoyer un mail automatique. Sam a fait ecrire a ses eleves trois branches pour une note, puis a demande : "et si la note vaut exactement 10 ?" Ceux qui avaient mis `>` au lieu de `>=` ont vu le piege. Une histoire, une lecon durable.

:::astuce
Teste toujours les frontieres : note = 10, temperature = 0. C'est la que les bugs aiment se cacher.
:::

## Exemple complet

```python
score = int(input("Score ? "))
vies = int(input("Vies ? "))

if score >= 100 and vies > 0:
    print("Niveau suivant")
elif vies == 0:
    print("Game over")
else:
    print("Continue")
```

Change les seuils. Relance avec 9, 10, 16 pour une note. Observe. C'est comme ca que ca rentre. Ne te contente pas d'un seul test "heureux". Teste aussi le bord : egalite, zero, valeur absurde.

## Erreur classique

Oublier l'indentation. Utiliser `=` au lieu de `==`. Ecrire des conditions impossibles (`if age > 18 and age < 10`). Ou trop faire confiance a une comparaison de texte sans `.strip()` / `.lower()`. Autre piege : enchainer des `if` separes quand tu voulais `elif` - plusieurs blocs peuvent alors s'executer sans que tu le veuilles. Lea a deja envoye deux messages clients le meme jour a cause de ca. Depuis, elle relit ses branches a voix haute.

## En vrai

Programme "meteo" : si temperature < 0 -> "froid", < 20 -> "doux", sinon "chaud". Teste au moins trois valeurs. Puis refais l'exemple note avec tes propres seuils. Note sur papier ce qui se passe a la frontiere (0, 20). Les frontieres, c'est la que les bugs aiment se cacher.

## A toi

Demande un mot de passe. Si c'est `"python123"`, affiche "OK". Sinon "Refuse". Bonus : accepte aussi avec majuscules mixees via `.lower()`. Puis ecris une version avec `and` : mot de passe OK et age >= 12. Garde ce petit script. On le reutilisera quand on parlera d'erreurs de conversion avec `int(input(...))`.

## Zoom : condition vs boucle

Beaucoup de debutants melangent les deux. La condition decide. La boucle repete. Tu peux mettre une condition dans une boucle ("tant que le mot de passe est faux"), et une boucle dans une branche ("si VIP, afficher chaque privilege"). Mais ce ne sont pas les memes outils. Si tu te surprends a copier dix fois le meme `if`, tu as probablement besoin d'une boucle. Si tu te surprends a tourner sans fin pour "decider une fois", tu as probablement besoin d'un `if` plus clair.
