# Les enums

## Enum simple

```swift
enum Direction {
    case nord, sud, est, ouest
}

let dir = Direction.nord
```

## Enum avec valeurs associees

```swift
enum Message {
    case quitter
    case texte(String)
    case position(x: Int, y: Int)
}

let msg = Message.texte("Bonjour")
```

## switch sur enum

```swift
switch dir {
case .nord: print("Vers le nord")
case .sud: print("Vers le sud")
case .est: print("Vers l'est")
case .ouest: print("Vers l'ouest")
}
```

## Raw values

```swift
enum Jour: String {
    case lundi = "Lundi"
    case mardi = "Mardi"
}
```

## A retenir

- `enum` pour les variantes.
- Valeurs associees pour porter des donnees.
- `switch` exhaustif sur les enums.
