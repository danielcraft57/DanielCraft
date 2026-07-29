# Null-safety avancee

```kotlin
val ville: String? = user?.adresse?.ville
val sure = requireNotNull(id) { "id requis" }
```

## Outils

- `?.` `?:` `!!` (eviter `!!`).
- `takeIf` / `takeUnless`.
- Platform types Java : attention aux null venant du Java.

## A retenir

- La surete null se travaille aux frontieres (API, Java).
