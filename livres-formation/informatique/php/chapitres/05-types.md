# Les types de donnees

## Les types de base

| Type | Exemple | Usage |
|------|---------|-------|
| `int` | `42` | Entier |
| `float` | `3.14` | Decimal |
| `string` | `"Bonjour"` | Texte |
| `bool` | `true` / `false` | Vrai ou faux |
| `array` | `[1, 2, 3]` | Tableau |
| `null` | `null` | Absence de valeur |

## Verifier un type

```php
$age = 25;
echo gettype($age);     // integer
var_dump($age);          // int(25) - plus detaille
echo is_int($age);       // 1 (true)
```

## Conversion

```php
$texte = "42";
$nombre = (int) $texte;       // Cast explicite
$nombre = intval($texte);     // Fonction
$flottant = (float) "3.14";
```

> **Astuce DanielCraft** - PHP fait beaucoup de conversions implicites (type juggling). C'est pratique mais peut surprendre. Utilise `===` pour comparer sans conversion.

## Operations

```php
$a = 10;
$b = 3;
echo $a + $b;   // 13
echo $a / $b;   // 3.333...
echo $a % $b;   // 1
echo $a ** $b;  // 1000 (puissance)
echo intdiv($a, $b); // 3 (division entiere)
```

## Petite histoire

Nora compare `"0" == false`. PHP repond `true` (type juggling). Elle utilise `===` et obtient `false`. Lecon apprise.

## A retenir

- `var_dump()` pour debuguer les types.
- `===` pour comparer sans conversion.
- `(int)`, `(string)` pour le cast explicite.
