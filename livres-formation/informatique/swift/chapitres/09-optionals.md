# Les optionals

## Le probleme du nil

Swift utilise `Optional` pour representer l'absence de valeur :

```swift
var nom: String? = nil
nom = "Lea"
```

## Deballage securise

```swift
if let valeur = nom {
    print(valeur.count)
}
```

## Guard let

```swift
func afficherLongueur(_ texte: String?) {
    guard let texte = texte else { return }
    print(texte.count)
}
```

## Nil coalescing

```swift
let affichage = nom ?? "Inconnu"
```

## Force unwrap (a eviter)

```swift
let longueur = nom!.count  // Crash si nil !
```

> **Piege** - `!` force le deballage. Reserve-le aux cas ou tu es certain.

## Petite histoire

Nora recoit un champ optional d'une API. Elle utilise `if let` et evite tout crash.

## A retenir

- `Type?` = optional (peut etre nil).
- `if let`, `guard let`, `??` pour gerer nil.
- Evite `!` en production.
