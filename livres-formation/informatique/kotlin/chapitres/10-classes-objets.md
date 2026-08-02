# Classes et objets

## Definir une classe

```kotlin
class Animal(val nom: String, var age: Int) {
    fun sePresenter() {
        println("Je suis $nom, $age ans.")
    }
}

val chat = Animal("Felix", 3)
chat.sePresenter()
```

Les parametres du constructeur primaire deviennent automatiquement proprietes.

## Proprietes calculees

```kotlin
class Rectangle(val largeur: Int, val hauteur: Int) {
    val aire: Int
        get() = largeur * hauteur
}
```

## Visibilite

```kotlin
class Compte(private var solde: Double) {
    fun depot(montant: Double) { solde += montant }
    fun lireSolde() = solde
}
```

## Object (singleton)

```kotlin
object Config {
    const val VERSION = "1.0"
    val API_URL = "https://api.example.com"
}

println(Config.VERSION)
```

> **Astuce DanielCraft** - Le constructeur primaire avec `val`/`var` remplace le boilerplate Java.

## Petite histoire

Max cree une classe `Produit` en 3 lignes avec constructeur primaire. En Java, il aurait eu 15 lignes de getters/setters.

## A retenir

- `class Nom(val x: Type)` = constructeur + propriete.
- `get()` pour les proprietes calculees.
- `object` pour les singletons.
