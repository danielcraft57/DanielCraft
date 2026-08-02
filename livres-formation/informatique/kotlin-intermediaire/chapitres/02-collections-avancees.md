# Collections avancees

```kotlin
val noms = listOf("Lea", "Max", "Sam")
val maj = noms.map { it.uppercase() }
val longs = noms.filter { it.length > 3 }
val parLongueur = noms.groupBy { it.length }
```

## Mutable vs immutable

- `listOf` / `mutableListOf`.
- Preferer immutable en API publique.

## A retenir

- map / filter / groupBy = quotidien Kotlin.
