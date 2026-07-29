# Les types de donnees

## Les types de base

| Type | Exemple | Usage |
|------|---------|-------|
| `int` | `42` | Entier |
| `long` | `9000000000L` | Grand entier |
| `double` | `3.14` | Decimal (defaut) |
| `decimal` | `19.99m` | Precision financiere |
| `bool` | `true` / `false` | Vrai ou faux |
| `char` | `'A'` | Un caractere |
| `string` | `"Bonjour"` | Texte |

## Types valeur vs reference

Les types simples (`int`, `double`, `bool`) sont des types valeur : la variable contient directement la donnee. Les `string` et objets sont des types reference : la variable pointe vers la donnee.

## Conversion

```csharp
string texte = "42";
int nombre = int.Parse(texte);       // Peut lever une exception
bool ok = int.TryParse(texte, out int n); // Plus sur
```

> **Astuce DanielCraft** - Prefere `TryParse` a `Parse` pour eviter les plantages sur des saisies invalides.

## Operations

```csharp
int a = 10, b = 3;
Console.WriteLine(a + b);  // 13
Console.WriteLine(a / b);  // 3 (division entiere)
Console.WriteLine(a % b);  // 1 (reste)
Console.WriteLine((double)a / b); // 3.333...
```

## Petite histoire

Nora calcule un prix TTC avec `decimal` pour eviter les erreurs d'arrondi. `19.99m * 1.20m` donne exactement `23.988m`.

## A retenir

- C# est fortement type : le compilateur verifie tout.
- `int`, `double`, `string`, `bool` pour 90% des cas.
- `decimal` pour l'argent.
- `TryParse` pour convertir sans risque.
