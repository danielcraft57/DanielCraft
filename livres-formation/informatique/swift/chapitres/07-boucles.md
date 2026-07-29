# Les boucles

## for-in

```swift
for i in 0...4 {
    print(i)  // 0, 1, 2, 3, 4
}

for i in 0..<5 {
    print(i)  // 0, 1, 2, 3, 4
}
```

## Parcourir une collection

```swift
let fruits = ["pomme", "banane", "cerise"]
for fruit in fruits {
    print(fruit)
}
```

## while et repeat-while

```swift
var n = 0
while n < 5 {
    print(n)
    n += 1
}

repeat {
    print(n)
    n -= 1
} while n > 0
```

## break et continue

```swift
for i in 0...10 {
    if i == 5 { break }
    if i % 2 == 0 { continue }
    print(i)
}
```

## A retenir

- `0...4` inclusif, `0..<5` exclusif.
- `for-in` pour parcourir collections.
- `repeat-while` teste apres execution.
