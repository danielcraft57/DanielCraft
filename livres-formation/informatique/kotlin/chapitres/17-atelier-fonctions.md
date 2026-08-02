# Atelier : fonctions

## Exercice 1 : salutation

```kotlin
fun saluer(nom: String, heure: Int): String = when {
    heure < 12 -> "Bonjour $nom !"
    heure < 18 -> "Bon apres-midi $nom !"
    else -> "Bonsoir $nom !"
}
```

## Exercice 2 : moyenne

```kotlin
fun moyenne(notes: List<Int>): Double {
    if (notes.isEmpty()) return 0.0
    return notes.average()
}
```

## Exercice 3 : filtrage

```kotlin
fun motsLongs(mots: List<String>, min: Int) =
    mots.filter { it.length >= min }
```

## Exercice 4 : division securisee

```kotlin
fun diviser(a: Int, b: Int): Result<Int> =
    if (b == 0) Result.failure(IllegalArgumentException("Division par zero"))
    else Result.success(a / b)
```

> **Astuce DanielCraft** - `List<T>` est prefere a `MutableList<T>` en parametre (plus flexible).

## A retenir

- `when` dans les fonctions expression.
- `List<T>` en parametre, pas `MutableList`.
- `Result<T>` pour les erreurs.
