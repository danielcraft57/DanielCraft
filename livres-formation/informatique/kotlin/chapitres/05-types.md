# Les types de donnees

## Types numeriques

| Type | Exemple | Usage |
|------|---------|-------|
| `Int` | `42` | Entier (defaut) |
| `Long` | `9_000_000_000L` | Grand entier |
| `Double` | `3.14` | Flottant (defaut) |
| `Float` | `3.14f` | Flottant simple precision |

## Texte et booleen

```kotlin
val texte: String = "Bonjour"
val lettre: Char = 'A'
val ok: Boolean = true
```

## Conversion

```kotlin
val i = "42".toInt()
val s = 42.toString()
val d = 3.14.toInt()   // 3
```

## Nullable types

```kotlin
var nom: String? = null   // Peut etre null
nom = "Lea"
```

Le `?` indique qu'une variable peut etre null. C'est le coeur de la null safety Kotlin.

> **Astuce DanielCraft** - Pas de conversion implicite dangereuse. Chaque conversion est explicite avec `.toInt()`, `.toString()`, etc.

## Petite histoire

Nora recoit une chaine "42" et veut la multiplier par 2. Elle appelle `.toInt()` et obtient 84. Pas de magie, tout est explicite.

## A retenir

- `Int`, `Double`, `String`, `Boolean` sont les types courants.
- `String?` = nullable, `String` = jamais null.
- Conversions explicites avec `.toXxx()`.
