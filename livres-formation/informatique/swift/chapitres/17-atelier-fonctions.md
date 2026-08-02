# Atelier : fonctions

## Exercice 1 : salutation

```swift
func saluer(nom: String, heure: Int) -> String {
    switch heure {
    case ..<12: return "Bonjour \(nom) !"
    case ..<18: return "Bon apres-midi \(nom) !"
    default: return "Bonsoir \(nom) !"
    }
}
```

## Exercice 2 : moyenne

```swift
func moyenne(_ notes: [Int]) -> Double {
    guard !notes.isEmpty else { return 0 }
    return Double(notes.reduce(0, +)) / Double(notes.count)
}
```

## Exercice 3 : division securisee

```swift
func diviser(_ a: Int, par b: Int) -> Int? {
    guard b != 0 else { return nil }
    return a / b
}
```
