# Chapitre 4 - Les variables

Une **variable**, ce n'est pas un concept abstrait de matheux. C'est une boite avec un nom. Tu ranges une valeur. Tu la reutilises plus tard. Tu peux changer le contenu. Le nom reste. En Python, tu n'as pas besoin d'annoncer "c'est un nombre" ou "c'est du texte" a l'avance : Python regarde la valeur et comprend. Lea range un `prix_ht`. Max range un `nombre_de_vies` pour un mini jeu. Sam range un `score_eleve`. Trois boites, meme idee.

Chez DanielCraft, on insiste sur les noms clairs des le debut. Pas parce qu'on aime le style. Parce qu'un mauvais nom te coute dix minutes plus tard, et parfois une heure en equipe.

```python
age = 12
prenom = "Leo"
score = 0
```

## Ce que ce n'est pas

Une variable, ce n'est pas une "formule magique". Ce n'est pas non plus une constante eternelle, meme si tu peux adopter une convention MAJUSCULES pour signaler "je ne veux pas changer ca". Ce n'est pas une excuse pour ecrire `x1`, `a`, `tmp2` partout. Et ce n'est surtout pas un tiroir ou tu ranges n'importe quoi sans regarder le type : tu peux ecrire `score = "dix"` apres `score = 10`, Python l'accepte, mais ton futur toi ne te remerciera pas.

Imagine des boites sur une etagere. L'etiquette dit `score`. Dedans, tu mets `0`. Plus tard, tu remplaces par `10`. Quand tu ecris `score + 1`, tu regardes dans la boite, tu calcules, souvent tu remets le resultat dans la boite avec `score = score + 1` ou le raccourci `score += 1`. Si tu confonds l'etiquette et le contenu, tu te perds. Si tu gardes des etiquettes parlantes, tu te retrouves.

:::astuce
Avant d'ecrire le code, nomme tes boites a voix haute : prenom, points, max. Si le nom sonne flou, change-le.
:::

## Changer une valeur et nommer bien

```python
score = 0
score = score + 1
score += 5  # raccourci : score = score + 5
print(score)
```

Oui :

```python
nombre_de_vies = 3
message_accueil = "Salut"
```

Non (ou alors on se perd) :

```python
x1 = 3
a = "Salut"
```

En Python, on utilise souvent le **snake_case** : mots separes par `_`. C'est la convention. Suis-la. Ton futur toi te remerciera. Lea refuse les variables d'une lettre dans ses scripts clients, sauf boucles tres courtes. Sam enleve des points si le nom ne dit rien.

## Plusieurs infos, echange, constantes

```python
a = 3
b = 5
total = a + b
print(total)
```

Tu peux aussi echanger :

```python
x = 1
y = 2
x, y = y, x
print(x, y)  # 2 1
```

Python n'a pas de vrai `const` comme certains langages. Par convention, on ecrit en **MAJUSCULES** ce qu'on ne veut pas changer :

```python
MAX_ESSAIS = 5
```

Ce n'est pas bloque techniquement. C'est un signal pour les humains. Max met `TAUX_TVA = 0.20` en haut de son calculateur. Quand le taux change, il sait ou regarder.

## Attention au piege

```python
# piege : ecraser sans faire gaffe
score = 10
score = "dix"  # autorise, mais souvent une mauvaise idee
```

Une variable peut changer de type. Ca ne veut pas dire que c'est clair. Si tu melanges nombres et textes dans la meme boite selon l'humeur, les bugs arrivent en silence puis explosent plus loin.

:::attention
Une variable contient une valeur, pas une formule vivante. Si tu changes `a` apres avoir calcule `total`, `total` ne se met pas a jour tout seul.
:::

## Petite histoire

Lea a herite d'un script ou tout s'appelait `data`, `data2`, `tmp`. Elle a passe une soiree a renommer. Le script n'etait pas "plus intelligent" apres. Il etait lisible. Le client a pu le comprendre. Chez DanielCraft, on appelle ca de la gentillesse envers le prochain lecteur - souvent toi dans trois semaines.

Max a cree un mini profil joueur : pseudo, niveau, xp. Il a change le seuil, relance, vu le "niveau up". Il a compris les variables mieux qu'avec une definition scolaire. Sam projette le meme exemple et demande aux eleves de renommer avant d'ajouter une regle.

## Exemple complet

```python
pseudo = "PixelFox"
niveau = 1
xp = 0

xp += 50
print(f"{pseudo} a {xp} xp")

if xp >= 50:
    niveau += 1
    xp -= 50
    print(f"Niveau up ! Niveau {niveau}")

print(f"Etat : niveau {niveau}, xp {xp}")
```

Meme si `if` arrive plus en detail au chapitre suivant, tu peux deja lire l'idee : la boite change, une decision suit.

## Erreur classique

Ecraser une variable importante par accident, ou reutiliser le meme nom pour deux idees differentes. Autre classique : croire que le nom de la variable "calcule tout seul". Non. `total` ne se met pas a jour si tu changes `a` apres coup, sauf si tu recalcules. La boite contient une valeur, pas une formule vivante (sauf si tu reconstruis volontairement cette logique).

## En vrai

Retape l'exemple joueur. Change le pseudo et le seuil d'xp. Relance. Puis invente un mini profil (jeu, sport, ecole) avec 3 variables minimum et une phrase complete affichee.

## A toi

Cree une variable `prenom` et une variable `points` qui commence a 0. Ajoute 10 points, puis affiche le tout avec `print` ou une f-string. Bonus : ajoute `MAX_POINTS = 100` et affiche combien il reste avant le max.
