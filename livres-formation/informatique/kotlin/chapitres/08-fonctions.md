# Les fonctions

## Declarer une fonction

```kotlin
fun saluer(prenom: String) {
    println("Bonjour $prenom !")
}

fun additionner(a: Int, b: Int): Int {
    return a + b
}
```

## Fonction expression (corps unique)

```kotlin
fun doubler(x: Int) = x * 2

fun estMajeur(age: Int) = age >= 18
```

Pas de `{}` ni de `return` : le `=` suffit.

## Parametres par defaut

```kotlin
fun saluer(prenom: String, message: String = "Bonjour") {
    println("$message $prenom !")
}

saluer("Lea")                    // Bonjour Lea !
saluer("Lea", "Salut")           // Salut Lea !
```

## Fonctions lambda

```kotlin
val nombres = listOf(3, 1, 4, 1, 5)
val doubles = nombres.map { it * 2 }
val pairs = nombres.filter { it % 2 == 0 }
```

> **Astuce DanielCraft** - `it` est le nom implicite du parametre dans une lambda a un seul argument.

## Petite histoire

Max ecrit `fun calculerTTC(prix: Double) = prix * 1.20`. Une ligne, pas de `{}`, pas de `return`. Kotlin est concis.

## A retenir

- `fun nom(params): TypeRetour { }`
- `= expression` pour les fonctions courtes.
- Parametres par defaut evitent la surcharge.
- Lambdas avec `{ it -> ... }` ou `{ ... }`.
