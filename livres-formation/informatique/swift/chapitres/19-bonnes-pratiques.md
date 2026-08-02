# Bonnes pratiques

## Idiomes Swift

- Prefere `let` a `var`.
- Prefere les **structs** aux classes.
- Utilise `guard` pour sortir tot d'une fonction.
- Nomme clairement : `isValid`, `hasItems`.

## Formatage

- SwiftLint ou le formateur Xcode.
- 4 espaces d'indentation (standard Xcode).

## Tests

```swift
func testAddition() {
    XCTAssertEqual(additionner(2, 3), 5)
}
```

## A retenir

- Code idiomatique Swift, pas du Java traduit.
- Tests unitaires avec XCTest.
