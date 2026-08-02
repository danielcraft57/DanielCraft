# Coroutines (idee)

Les **coroutines** gerent l'asynchrone sans callback hell.

```kotlin
suspend fun charger(): String {
  delay(100)
  return "ok"
}
```

## Concepts

- `suspend` : peut se mettre en pause.
- `launch` / `async` : demarrer du travail.
- Scope : qui annule quoi.

> **Astuce DanielCraft** - Apprends `viewModelScope` / `coroutineScope` avant les details Dispatchers.

## A retenir

- Coroutine = concurrence structuree (idee).
