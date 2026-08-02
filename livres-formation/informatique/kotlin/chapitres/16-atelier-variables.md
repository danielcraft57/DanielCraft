# Atelier : variables et types

## Exercice 1 : carte d'identite

```kotlin
val prenom = "Sam"
val age = 22
val ville = "Nantes"
println("Je suis $prenom, $age ans, je vis a $ville.")
```

## Exercice 2 : conversion

```kotlin
val texte = "42"
val nombre = texte.toInt()
val flottant = nombre.toDouble()
println(flottant)  // 42.0
```

## Exercice 3 : nullable

```kotlin
var pseudo: String? = null
pseudo = "DevNora"
val affichage = pseudo ?: "Anonyme"
println(affichage)
```

## Defi : temperature

```kotlin
val celsius = 37.0
val fahrenheit = celsius * 9 / 5 + 32
println("$celsius°C = $fahrenheit°F")
```

> **Astuce DanielCraft** - Utilise des noms clairs. `celsius` vaut mieux que `c`.

## A retenir

- `val` pour immutable, `var` pour mutable.
- `.toInt()`, `.toDouble()` pour les conversions.
- `?: "defaut"` pour les valeurs nullable.
