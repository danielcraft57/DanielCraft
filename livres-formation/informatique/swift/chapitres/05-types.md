# Les types de donnees

## Types numeriques

| Type | Exemple | Usage |
|------|---------|-------|
| `Int` | `42` | Entier (defaut) |
| `Double` | `3.14` | Flottant (defaut) |
| `Float` | `3.14` | Flottant simple precision |
| `Bool` | `true` | Booleen |

## Texte

```swift
let texte: String = "Bonjour"
let lettre: Character = "A"
```

## Conversion

```swift
let i = Int("42")          // Optional Int?
let s = String(42)
```

## Tuples

```swift
let point = (10, 20)
print(point.0)  // 10
print(point.1)  // 20
```

## Petite histoire

Nora additionne un `Int` et un `Double`. Swift refuse. Elle convertit avec `Double(entier)`.

## A retenir

- `Int`, `Double`, `String`, `Bool` sont les types courants.
- Conversions explicites.
- Tuples pour regrouper plusieurs valeurs.
