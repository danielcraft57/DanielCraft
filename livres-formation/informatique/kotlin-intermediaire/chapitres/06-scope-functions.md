# Scope functions : let, run, apply, also, with

```kotlin
val user = User().apply {
  name = "Lea"
  age = 30
}

val len = name?.let { it.length } ?: 0
```

## Aide-memoire

| Fonction | Objet | Retour |
|----------|-------|--------|
| let | it | lambda |
| run | this | lambda |
| apply | this | objet |
| also | it | objet |

## A retenir

- Choisir selon ce que tu veux retourner.
