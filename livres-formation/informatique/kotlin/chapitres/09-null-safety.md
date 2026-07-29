# Null safety

## Le probleme du null

En Java, `NullPointerException` est la cause numero 1 de crash. Kotlin elimine ce risque a la compilation.

```kotlin
var nom: String = "Lea"     // Ne peut PAS etre null
var alias: String? = null   // Peut etre null
```

## Operateur safe call

```kotlin
val longueur = alias?.length   // null si alias est null
println(longueur)              // null (pas de crash)
```

## Elvis operator

```kotlin
val longueur = alias?.length ?: 0
// Si alias est null, retourne 0
```

## Force unwrap (a eviter)

```kotlin
val longueur = alias!!.length  // Crash si null !
```

> **Piege** - `!!` force le deballage. Utilise-le seulement quand tu es certain que la valeur n'est pas null.

## Smart cast

```kotlin
fun afficherLongueur(texte: String?) {
    if (texte != null) {
        println(texte.length)  // Kotlin sait que texte n'est plus null
    }
}
```

## Petite histoire

Nora recoit un champ nullable d'une API. Au lieu de crasher, elle utilise `?.` et `?: "Inconnu"`. Plus jamais de NullPointerException.

## A retenir

- `String` = jamais null, `String?` = peut etre null.
- `?.` = safe call, `?:` = valeur par defaut.
- Evite `!!` en production.
