# Gerer les erreurs

## try / catch

```kotlin
try {
    val n = "abc".toInt()
} catch (e: NumberFormatException) {
    println("Pas un nombre : ${e.message}")
}
```

## Result<T> (idiome Kotlin)

```kotlin
fun diviser(a: Int, b: Int): Result<Int> {
    return if (b == 0) Result.failure(IllegalArgumentException("Division par zero"))
    else Result.success(a / b)
}

diviser(10, 2).onSuccess { println("Resultat : $it") }
diviser(10, 0).onFailure { println("Erreur : ${it.message}") }
```

## require et check

```kotlin
fun retirer(solde: Double, montant: Double): Double {
    require(montant > 0) { "Montant doit etre positif" }
    check(montant <= solde) { "Solde insuffisant" }
    return solde - montant
}
```

## runCatching

```kotlin
val resultat = runCatching { "42".toInt() }
println(resultat.getOrDefault(0))  // 42
```

> **Astuce DanielCraft** - `Result<T>` est prefere aux exceptions pour les erreurs attendues. Reserve `throw` aux cas vraiment exceptionnels.

## Petite histoire

Max refactorise un code Java avec 5 try/catch en Kotlin avec `Result` et `runCatching`. Le code est plus lisible et plus sur.

## A retenir

- `try/catch` pour les exceptions.
- `Result<T>` pour les erreurs attendues.
- `require` et `check` pour valider les preconditions.
