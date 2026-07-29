# Bonnes pratiques

## Conventions Kotlin

- **camelCase** : variables, fonctions, proprietes.
- **PascalCase** : classes, interfaces, objects.
- **SCREAMING_SNAKE_CASE** : constantes top-level.
- **ktlint** : formateur/linter officiel.

## Idiomes Kotlin

```kotlin
// Prefere ceci :
val noms = list.filter { it.actif }.map { it.nom }

// Plutot que :
val noms = mutableListOf<String>()
for (item in list) {
    if (item.actif) noms.add(item.nom)
}
```

## Null safety

```kotlin
// Prefere :
val nom = utilisateur?.nom ?: "Inconnu"

// Plutot que :
val nom = utilisateur!!.nom
```

## Tests

```kotlin
@Test
fun `addition de deux nombres positifs`() {
    assertEquals(5, additionner(2, 3))
}
```

Les noms de test avec backticks sont autorises en Kotlin.

> **Astuce DanielCraft** - Ecris du Kotlin idiomatique, pas du Java traduit. Utilise `when`, `data class`, lambdas.

## A retenir

- Code fonctionnel avec `filter`, `map`, `forEach`.
- Null safety systematique.
- Tests avec noms descriptifs.
