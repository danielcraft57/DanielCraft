# Fonctions d'extension

```kotlin
fun String.initiales(): String =
  split(" ").mapNotNull { it.firstOrNull()?.uppercaseChar() }.joinToString("")

println("Loic Daniel".initiales()) // LD
```

## Pourquoi

- Enrichir un type sans heritage.
- Garder les appels lisibles.

> **Piege** - Trop d'extensions = API introuvable. Namespace clair.

## A retenir

- Extension = verb metier sur un type existant.
