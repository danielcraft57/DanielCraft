# Fonctions d'ordre superieur

```kotlin
fun operer(a: Int, b: Int, op: (Int, Int) -> Int) = op(a, b)

operer(2, 3) { x, y -> x + y }
```

## Inline (idee)

- `inline` reduit le cout des lambdas dans les hot paths.

## A retenir

- Passer une fonction = comportement injectable.
