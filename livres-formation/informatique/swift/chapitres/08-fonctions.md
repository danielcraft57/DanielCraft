# Les fonctions

## Declarer une fonction

```swift
func saluer(prenom: String) {
    print("Bonjour \(prenom) !")
}

func additionner(a: Int, b: Int) -> Int {
    return a + b
}
```

## Parametres avec labels

```swift
func retirer(de compte: Double, montant: Double) -> Double {
    return compte - montant
}

retirer(de: 1000, montant: 50)
```

## Parametres par defaut

```swift
func saluer(prenom: String, message: String = "Bonjour") {
    print("\(message) \(prenom) !")
}
```

## Closures

```swift
let nombres = [3, 1, 4, 1, 5]
let doubles = nombres.map { $0 * 2 }
let pairs = nombres.filter { $0 % 2 == 0 }
```

> **Astuce DanielCraft** - `$0`, `$1` sont les raccourcis pour les parametres de closure.

## A retenir

- `func nom(_ param: Type) -> Retour`.
- Labels externes et internes.
- Closures avec `{ $0 }`.
