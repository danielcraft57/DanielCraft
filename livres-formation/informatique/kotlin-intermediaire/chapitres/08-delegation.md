# Delegation

```kotlin
interface Repo { fun find(id: Int): String? }

class CacheRepo(private val inner: Repo) : Repo by inner {
  // surcharge possible
}
```

## by lazy

```kotlin
val config by lazy { loadConfig() }
```

## A retenir

- Delegation = reutiliser sans heritage lourd.
