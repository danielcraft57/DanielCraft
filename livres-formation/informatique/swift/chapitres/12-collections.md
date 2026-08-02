# Collections

## Array

```swift
var fruits = ["pomme", "banane", "cerise"]
fruits.append("kiwi")
print(fruits.count)  // 4
```

## Dictionary

```swift
var ages = ["Lea": 28, "Sam": 22]
ages["Nora"] = 30
print(ages["Lea"] ?? 0)
```

## Set

```swift
var unique = Set([1, 2, 3, 2, 1])
print(unique)  // {1, 2, 3}
```

## Operations fonctionnelles

```swift
let nombres = [3, 1, 4, 1, 5]
let sorted = nombres.sorted()
let filtres = nombres.filter { $0 > 2 }
let somme = nombres.reduce(0, +)
```

## A retenir

- `[Type]` array, `[Cle: Valeur]` dictionary, `Set<Type>` ensemble.
- `append`, `filter`, `map`, `reduce`.
