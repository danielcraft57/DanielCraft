# Erreurs classiques en Kotlin

## 1. Utiliser var au lieu de val

```kotlin
var nom = "Lea"  // Devrait etre val si ca ne change pas
```

## 2. Force unwrap avec !!

```kotlin
val longueur = nom!!.length  // Crash si null !
```

Utilise `?.` et `?:` a la place.

## 3. Oublier le ? pour nullable

```kotlin
var email: String = null  // Erreur de compilation !
var email: String? = null // OK
```

## 4. Confondre listOf et mutableListOf

```kotlin
val liste = listOf(1, 2, 3)
liste.add(4)  // Erreur ! listOf est immutable
```

## 5. Oublier le return dans une fonction bloc

```kotlin
fun doubler(x: Int): Int {
    x * 2  // Oublie return !
}
fun doubler(x: Int) = x * 2  // OK avec =
```

## 6. Smart cast impossible

```kotlin
var texte: String? = "hello"
if (texte != null) {
    // texte peut etre modifie par un autre thread
    println(texte.length)  // Erreur si var !
}
```

> **Astuce DanielCraft** - Le compilateur Kotlin donne des messages clairs. Lis-les attentivement.

## A retenir

- Prefere `val` et `?.`/`?:`.
- `listOf` = immutable, `mutableListOf` = mutable.
- `= expression` evite les oublis de return.
