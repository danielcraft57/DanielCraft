# Collections

## list, set, map

```kotlin
val fruits = listOf("pomme", "banane", "cerise")     // Immutable
val notes = mutableListOf(12, 15, 18)                 // Mutable
val unique = setOf(1, 2, 3, 2, 1)                    // {1, 2, 3}
val ages = mapOf("Lea" to 28, "Sam" to 22)           // Immutable
```

## Operations courantes

```kotlin
val nombres = listOf(3, 1, 4, 1, 5, 9)

nombres.size              // 6
nombres.sorted()          // [1, 1, 3, 4, 5, 9]
nombres.filter { it > 3 } // [4, 5, 9]
nombres.map { it * 2 }    // [6, 2, 8, 2, 10, 18]
nombres.sum()             // 23
nombres.maxOrNull()       // 9
```

## Parcourir une map

```kotlin
for ((nom, age) in ages) {
    println("$nom a $age ans")
}
```

## Sealed classes (bonus)

```kotlin
sealed class Resultat {
    data class Succes(val data: String) : Resultat()
    data class Erreur(val message: String) : Resultat()
}
```

> **Astuce DanielCraft** - Prefere `listOf` (immutable) par defaut. Utilise `mutableListOf` seulement si tu dois modifier.

## Petite histoire

Sam filtre une liste de 1000 produits avec `.filter { it.prix < 50 }`. Une ligne, pas de boucle manuelle.

## A retenir

- `listOf`, `setOf`, `mapOf` = immutables.
- `filter`, `map`, `sorted`, `sum` = operations fonctionnelles.
- `for ((k, v) in map)` pour parcourir une map.
