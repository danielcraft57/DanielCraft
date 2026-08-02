# Les types de donnees

## Les types de base

| Type | Exemple | Usage |
|------|---------|-------|
| `int` | `42` | Entier (taille depend de l'archi) |
| `int64` | `9000000000` | Grand entier |
| `float64` | `3.14` | Decimal |
| `bool` | `true` / `false` | Vrai ou faux |
| `string` | `"Bonjour"` | Texte (immutable) |
| `byte` | `'A'` | Alias pour uint8 |

## Zero values

En Go, chaque type a une valeur par defaut (zero value) :

```go
var n int      // 0
var f float64  // 0.0
var s string   // "" (vide)
var b bool     // false
```

## Conversion

```go
i := 42
f := float64(i)     // int -> float64
s := strconv.Itoa(i) // int -> string
```

> **Astuce DanielCraft** - Go ne fait pas de conversion implicite. Tu dois convertir explicitement.

## Operations

```go
a, b := 10, 3
fmt.Println(a + b)   // 13
fmt.Println(a / b)   // 3 (division entiere)
fmt.Println(a % b)   // 1 (modulo)
```

## Petite histoire

Nora additionne un `int` et un `float64`. Go refuse. Elle ajoute `float64(monInt)` et ca passe. Stricte mais clair.

## A retenir

- Go est strictement type, pas de conversion implicite.
- Zero values : chaque type a un defaut.
- `strconv` pour les conversions string <-> nombre.
