# Les variables

## C'est quoi une variable ?

Une variable est un nom qui pointe vers une valeur. Imagine une etiquette collee sur une boite : l'etiquette est le nom, le contenu de la boite est la valeur.

```python
prenom = "Max"
age = 24
```

Ici `prenom` contient le texte "Max" et `age` contient le nombre 24.

## Regles de nommage

- Commence par une lettre ou un underscore.
- Pas d'espaces : utilise des underscores (`mon_score`).
- Pas de mots reserves (`if`, `for`, `class`...).
- Sensible a la casse : `nom` et `Nom` sont differents.

> **Astuce DanielCraft** - Choisis des noms explicites. `prix_total` est mieux que `x`.

## Modifier une variable

```python
score = 0
score = score + 10
print(score)  # 10
```

On peut reassigner une variable a tout moment.

## Afficher avec f-string

```python
ville = "Lyon"
print(f"Je vis a {ville}")
```

Les f-strings permettent d'inserer des variables dans du texte.

## Petite histoire

Sam cree un programme qui calcule son budget. Il stocke `salaire = 1800` et `loyer = 650`, puis affiche `reste = salaire - loyer`. Python lui repond 1150.

## Erreur classique

```python
print(prnom)  # NameError : faute de frappe
```

Python ne devine pas. Si le nom est mal ecrit, il dit `NameError`.

## A retenir

- Variable = nom + valeur.
- Noms explicites, sans espaces, sensibles a la casse.
- f-string pour afficher des variables dans du texte.
