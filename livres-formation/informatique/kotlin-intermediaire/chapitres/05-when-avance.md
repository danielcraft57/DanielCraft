# when avance

```kotlin
val label = when (x) {
  in 1..10 -> "petit"
  in 11..100 -> "moyen"
  else -> "autre"
}
```

## Usages

- Remplacer if cascades.
- Avec sealed : machine a etats lisible.

## A retenir

- when = expression, pas seulement instruction.
