# Premier programme

## Hello World

```kotlin
fun main() {
    println("Bonjour le monde !")
}
```

`fun` declare une fonction. `main()` est le point d'entree.

## Affichage formate

```kotlin
val nom = "Sam"
val age = 28
println("Je suis $nom, $age ans.")
println("${nom.uppercase()} a $age ans.")
```

Les `$` et `${}` permettent l'interpolation de chaines.

## Les commentaires

```kotlin
// Commentaire sur une ligne
/* Commentaire
   sur plusieurs lignes */
```

## Petite histoire

Nora cree un fichier `Main.kt`, ecrit 3 lignes, clique Run. Le message s'affiche. Kotlin est concis des le depart.

## A retenir

- `fun main()` = point d'entree.
- `println()` pour afficher.
- Interpolation avec `$variable` ou `${expression}`.
