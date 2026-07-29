# Les conditions

## Prendre une decision

Un programme doit souvent choisir : si une condition est vraie, faire ceci, sinon faire cela.

```python
age = 17
if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

## if / elif / else

```python
note = 14
if note >= 16:
    print("Tres bien")
elif note >= 12:
    print("Bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")
```

Python teste les conditions de haut en bas. Des qu'une est vraie, il execute le bloc et ignore le reste.

> **Astuce DanielCraft** - L'indentation (4 espaces) definit le bloc. Pas d'accolades en Python.

## Les operateurs de comparaison

| Operateur | Signification |
|-----------|---------------|
| `==` | Egal a |
| `!=` | Different de |
| `<` | Inferieur |
| `>` | Superieur |
| `<=` | Inferieur ou egal |
| `>=` | Superieur ou egal |

## Combiner avec and / or / not

```python
age = 20
permis = True
if age >= 18 and permis:
    print("Tu peux conduire")
```

## Petite histoire

Max cree un programme qui verifie si un mot de passe fait au moins 8 caracteres. Si oui, il affiche "Mot de passe valide". Sinon, "Trop court". Trois lignes suffisent.

## Erreur classique

```python
if age = 18:  # SyntaxError ! Utilise == pour comparer
```

Un seul `=` assigne. Deux `==` comparent.

## A retenir

- `if`, `elif`, `else` pour decider.
- Indentation obligatoire (4 espaces).
- `==` pour comparer, `=` pour assigner.
