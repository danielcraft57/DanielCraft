# Flow (idee)

Un **Flow** emet une sequence asynchrone de valeurs.

```kotlin
val ticks = flow {
  for (i in 1..3) {
    emit(i)
    delay(50)
  }
}
```

## Vs LiveData / callbacks

- Compose bien avec coroutines.
- Operateurs : `map`, `filter`, `collect`.

## A retenir

- Flow = stream asynchrone Kotlin.
