# Les variables

## val vs var

```kotlin
val nom = "Max"       // Immutable (comme final en Java)
var score = 0         // Mutable
score += 10
println(score)        // 10
```

> **Astuce DanielCraft** - Prefere `val` par defaut. Utilise `var` seulement quand la valeur doit changer.

## Types explicites

```kotlin
val age: Int = 25
val prix: Double = 19.99
val actif: Boolean = true
```

Kotlin infere le type quand c'est evident :

```kotlin
val ville = "Paris"   // String infere
val compteur = 42     // Int infere
```

## Constantes

```kotlin
const val TVA = 0.20
const val MAX_JOUEURS = 100
```

`const val` doit etre un type primitif ou String, declare au niveau top-level ou dans un objet.

## Conventions

- camelCase pour variables et fonctions : `monScore`.
- PascalCase pour classes : `MonType`.
- SCREAMING_SNAKE_CASE pour constantes : `MAX_JOUEURS`.

## Petite histoire

Sam declare `val budget = 1800` puis essaie `budget = 1500`. Le compilateur refuse. Il comprend : `val` = immutable.

## A retenir

- `val` = immutable, `var` = mutable.
- Inference de type par defaut.
- `const val` pour les constantes compile-time.
