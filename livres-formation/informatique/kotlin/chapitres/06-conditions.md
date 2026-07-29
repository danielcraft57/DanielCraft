# Les conditions

## if / else

```kotlin
val age = 17
if (age >= 18) {
    println("Majeur")
} else {
    println("Mineur")
}
```

## if comme expression

```kotlin
val statut = if (age >= 18) "Majeur" else "Mineur"
println(statut)
```

En Kotlin, `if` retourne une valeur. Pas besoin de ternaire `? :`.

## when (equivalent switch ameliore)

```kotlin
val jour = "lundi"
when (jour) {
    "lundi", "mardi" -> println("Debut de semaine")
    "vendredi" -> println("Presque le weekend")
    else -> println("Autre jour")
}
```

`when` peut aussi matcher des types, des ranges, des conditions :

```kotlin
when {
    age < 12 -> println("Enfant")
    age < 18 -> println("Adolescent")
    else -> println("Adulte")
}
```

> **Astuce DanielCraft** - `when` remplace `switch` et fait bien plus. C'est l'idiome Kotlin pour les conditions multiples.

## Petite histoire

Max ecrit un `when` sur une enum `Direction`. Le compilateur verifie l'exhaustivite. Il ajoute le cas manquant et le code compile.

## A retenir

- `if` est une expression (retourne une valeur).
- `when` remplace switch, plus puissant.
- Pas de ternaire : utilise `if` expression.
