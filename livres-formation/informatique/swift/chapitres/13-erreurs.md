# Gerer les erreurs

## throw et Error

```swift
enum MonErreur: Error {
    case soldeInsuffisant
    case montantInvalide
}

func retirer(solde: inout Double, montant: Double) throws {
    guard montant > 0 else { throw MonErreur.montantInvalide }
    guard montant <= solde else { throw MonErreur.soldeInsuffisant }
    solde -= montant
}
```

## try / catch

```swift
var solde = 100.0
do {
    try retirer(solde: &solde, montant: 150)
} catch MonErreur.soldeInsuffisant {
    print("Solde insuffisant")
} catch {
    print("Erreur : \(error)")
}
```

## try? et try!

```swift
let n = try? Int("abc")   // nil si echec
let m = try! Int("42")    // crash si echec
```

> **Astuce DanielCraft** - `throws` pour les erreurs attendues. `try?` pour simplifier quand nil suffit.

## A retenir

- `throws` / `try` / `catch`.
- `enum` conforme a `Error`.
- `try?` retourne optional.
