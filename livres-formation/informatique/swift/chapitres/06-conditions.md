# Les conditions

## if / else

```swift
let age = 17
if age >= 18 {
    print("Majeur")
} else {
    print("Mineur")
}
```

## if comme expression (Swift 5.9+)

```swift
let statut = age >= 18 ? "Majeur" : "Mineur"
```

## switch

```swift
let jour = "lundi"
switch jour {
case "lundi", "mardi":
    print("Debut de semaine")
case "vendredi":
    print("Presque le weekend")
default:
    print("Autre jour")
}
```

`switch` doit etre exhaustif en Swift.

> **Astuce DanielCraft** - `switch` en Swift est tres puissant : ranges, tuples, patterns.

## Petite histoire

Max ecrit un `switch` sur une enum `Direction`. Le compilateur lui signale le cas manquant.

## A retenir

- `if` / `else` classique.
- `switch` exhaustif et puissant.
- Pas de fallthrough implicite.
