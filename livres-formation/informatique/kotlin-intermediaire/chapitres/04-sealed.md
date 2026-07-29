# Sealed classes et interfaces

```kotlin
sealed class Resultat {
  data class Ok(val data: String) : Resultat()
  data class Err(val msg: String) : Resultat()
}

fun afficher(r: Resultat) = when (r) {
  is Resultat.Ok -> r.data
  is Resultat.Err -> r.msg
}
```

## Interet

- when **exhaustif** : le compilateur verifie tous les cas.

## A retenir

- Sealed = hierarchie fermee, parfaite pour etats.
