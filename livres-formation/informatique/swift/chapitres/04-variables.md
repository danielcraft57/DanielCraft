# Les variables

## let vs var

```swift
let nom = "Max"       // Immutable
var score = 0         // Mutable
score += 10
print(score)          // 10
```

> **Astuce DanielCraft** - Prefere `let` par defaut. Utilise `var` seulement si la valeur change.

## Types explicites

```swift
let age: Int = 25
let prix: Double = 19.99
let actif: Bool = true
```

## Constantes

```swift
let tva = 0.20
let maxJoueurs = 100
```

## Conventions

- camelCase pour variables et fonctions.
- PascalCase pour types, structs, classes, enums.

## Petite histoire

Sam declare `let budget = 1800` puis essaie de le modifier. Xcode refuse immediatement.

## A retenir

- `let` = immutable, `var` = mutable.
- Inference de type par defaut.
- camelCase / PascalCase.
