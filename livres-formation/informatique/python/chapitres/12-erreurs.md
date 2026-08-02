# Gerer les erreurs

## Les erreurs arrivent

Meme un bon programme peut rencontrer des situations imprevues : fichier introuvable, division par zero, saisie invalide. Python permet de les attraper au lieu de planter.

## try / except

```python
try:
    nombre = int(input("Un nombre : "))
    print(10 / nombre)
except ValueError:
    print("Ce n'est pas un nombre valide.")
except ZeroDivisionError:
    print("Impossible de diviser par zero.")
```

## Les erreurs courantes

| Erreur | Cause |
|--------|-------|
| `SyntaxError` | Code mal ecrit (parenthese, indentation) |
| `NameError` | Variable inexistante |
| `TypeError` | Operation sur mauvais type |
| `ValueError` | Valeur inappropriee |
| `IndexError` | Index hors limites |
| `KeyError` | Cle absente d'un dictionnaire |
| `FileNotFoundError` | Fichier introuvable |

## finally et else

```python
try:
    f = open("data.txt")
    contenu = f.read()
except FileNotFoundError:
    print("Fichier absent")
else:
    print(f"Lu : {len(contenu)} caracteres")
finally:
    print("Fin du bloc")
```

> **Astuce DanielCraft** - N'attrape que les erreurs que tu sais gerer. Laisser remonter les autres aide au debug.

## Lever une erreur

```python
def retirer(solde, montant):
    if montant > solde:
        raise ValueError("Solde insuffisant")
    return solde - montant
```

## Petite histoire

Max demande un nombre a l'utilisateur pour calculer une moyenne. L'utilisateur tape "abc". Sans `try/except`, le programme plante. Avec, il redemande poliment.

## A retenir

- `try/except` pour attraper les erreurs.
- Precise le type d'erreur (`ValueError`, etc.).
- `raise` pour lever tes propres erreurs.
