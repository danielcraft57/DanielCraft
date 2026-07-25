# Chapitre 7 - Les boucles

Une **boucle**, c'est repeter sans tout retaper. Afficher une table de 1 a 10. Demander un mot de passe jusqu'a trois essais. Parcourir une liste de fruits. Sans boucle, tu copies des lignes. Avec une boucle, tu decris la regle une fois. Lea boucle sur des fichiers a renommer. Max boucle sur des lignes de devis. Sam boucle sur des questions de quiz. Meme muscle, contextes differents. En 2026, des que tu automatises un peu, tu touches une boucle - souvent sans meme le remarquer dans un script plus gros.

Chez DanielCraft, on apprend deux familles tot : **for** quand tu sais combien de tours (ou tu parcours une collection), **while** quand tu continues tant qu'une condition reste vraie. Les deux sont utiles. Les deux peuvent devenir dangereuses si tu oublies d'avancer. Une boucle sans sortie, c'est un moteur qui tourne a vide. Ctrl+C existe. Ce n'est pas une honte. C'est un frein d'urgence.

## Ce que ce n'est pas

Une boucle, ce n'est pas "de la magie qui comprend ton intention". Ce n'est pas non plus une excuse pour boucler a l'infini "parce que ca marchera bien". Ce n'est pas la meme chose qu'une condition : la condition decide, la boucle repete. Et ce n'est surtout pas obligatoire d'utiliser `break` et `continue` partout. Ce sont des outils. Pas une preuve de niveau. Sam dit a ses eleves : "si tu mets `break` partout, je te demande pourquoi a voix haute". Souvent, une condition de boucle plus claire suffit.

Ce n'est pas non plus "for pour tout". Parfois `while` est le bon outil : attendre une reponse valide, un menu, un essai limite. Choisis selon l'intention, pas selon l'habitude.

`for i in range(1, 6)` : tu as un compteur qui va de 1 a 5 (le 6 est exclu). A chaque tour, tu fais quelque chose. `while vies > 0` : tant qu'il reste des vies, tu continues - mais tu dois diminuer `vies`, sinon tu tournes sans fin. Lea visualise une file d'attente : chaque personne passe une fois. Max visualise un compte a rebours. Sam visualise une liste de questions. Trois images, meme idee : repeter une action selon une regle claire.

Chez DanielCraft, on aime aussi l'image du "gardien a la porte" : tant que la condition est vraie, on laisse passer un tour. Des que la condition devient fausse, on ferme. Si tu oublies de changer la cle, le gardien ne ferme jamais.

:::attention
Dans un `while`, change toujours la variable de condition. Sinon : boucle infinie. Ctrl+C pour couper.
:::

## for, while, listes

```python
for i in range(1, 6):
    print("Tour", i)

for i in range(5):      # 0..4
    print(i)

for i in range(0, 10, 2):  # 0,2,4,6,8
    print(i)
```

```python
vies = 3
while vies > 0:
    print("Il reste", vies, "vies")
    vies = vies - 1
```

Boucler sur une liste :

```python
fruits = ["pomme", "banane", "kiwi"]
for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)
```

**enumerate** donne l'index et la valeur. Lea l'adore pour afficher des listes numerotees sans bricolage. Max l'utilise pour numeroter les lignes d'un devis. Une fois vu, tu le reconnaitras partout.

## break, continue, while True

```python
for n in range(1, 10):
    if n == 5:
        break      # stop complet
    if n % 2 == 0:
        continue   # saute le reste du tour
    print(n)
```

**break** = je sors. **continue** = je passe au tour suivant. Utile, mais pas magique : un message clair avant le `break` aide souvent celui qui relira ton code (toi, dans quinze jours).

Motif utile :

```python
while True:
    cmd = input("Commande (q pour quitter) : ").strip().lower()
    if cmd == "q":
        break
    print("Tu as tape :", cmd)
```

Sam utilise ce motif pour des menus d'exercices. Max l'a copie pour un mini outil "calculer / quitter". Chez DanielCraft, on aime les boucles qui ont une porte de sortie claire, visible des la premiere lecture.

## Exemple : table de multiplication

```python
n = 8
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

Refais-la en `while`. Tu verras que les deux styles existent, et que `for` est souvent plus net quand le nombre de tours est connu. Ce n'est pas une competition. C'est un choix de lisibilite.

:::retenir
`for` quand le parcours est connu. `while` quand tu attends qu'une condition change. Toujours une sortie claire.
:::

## Petite histoire

Lea devait envoyer un message personnalise a vingt prenoms. Sans boucle, elle aurait copie vingt `print`. Avec une boucle sur une liste, elle a change un prenom, relance, verifie. Dix minutes. Max a fait une boucle de decompte 10...1 puis "Decollage" pour amuser son neveu. Sam a demande trois essais de mot de passe avec `while` + compteur. L'eleve qui oubliait d'incrementer le compteur a decouvert la boucle infinie, puis Ctrl+C, puis la correction. Lecon durable : la sortie n'est pas optionnelle. Elle fait partie du design.

## Erreur classique

Oublier de modifier la variable du `while` : boucle infinie. Off-by-one avec `range` : croire que `range(1, 10)` inclut 10. Utiliser `for` quand tu as vraiment besoin d'un `while` (attente d'une reponse valide), ou l'inverse. Autre piege : `break` trop tot et croire que le reste du programme "sait" pourquoi tu es sorti - parfois un message clair avant le `break` aide. Lea a deja laisse un script "qui ne fait rien" parce qu'un `continue` sautait tout le travail utile. Relis le corps de boucle a voix haute.

## En vrai

Fais une boucle qui compte de 10 a 1, puis affiche "Decollage". Puis demande un mot de passe jusqu'a ce que ce soit le bon (max 3 essais) avec `while` + `break`. Teste les trois cas : bon du premier coup, bon au troisieme, rate les trois. Les bords comptent autant que le chemin heureux.

## A toi

Affiche la table de 8 (de 8x1 a 8x10) avec `for` et `range`. Puis une version `while`. Bonus : demande `n` a l'utilisateur et affiche sa table. Note en une phrase quand tu preferes `for` et quand tu preferes `while`. Garde cette phrase. Elle te servira au mini-projet.

## Zoom : range et le piege du dernier nombre

`range(1, 11)` donne 1 a 10. Le dernier nombre est exclu. C'est voulu. Ce n'est pas un bug. Si tu veux "de 1 a N inclus", pense `range(1, N + 1)`. Sam fait repeter cette phrase a ses eleves jusqu'a ce qu'elle sorte sans effort. Chez DanielCraft, on prefere une regle nette a dix essais au hasard.
