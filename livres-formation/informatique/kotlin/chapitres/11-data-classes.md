# Data classes

## Le probleme

En Java, une simple classe de donnees necessite constructeur, getters, equals, hashCode, toString. En Kotlin :

```kotlin
data class Produit(val nom: String, val prix: Double)

val p1 = Produit("Clavier", 49.99)
val p2 = Produit("Clavier", 49.99)
println(p1)           // Produit(nom=Clavier, prix=49.99)
println(p1 == p2)     // true
```

## Destructuration

```kotlin
val (nom, prix) = p1
println("$nom coute $prix EUR")
```

## copy()

```kotlin
val p3 = p1.copy(prix = 39.99)
println(p3)  // Produit(nom=Clavier, prix=39.99)
```

## Quand utiliser data class

- Modeles de donnees (DTO, entites).
- Resultats de fonctions avec plusieurs valeurs.
- Toute classe dont l'egalite est basee sur le contenu.

> **Astuce DanielCraft** - `data class` genere automatiquement equals, hashCode, toString, copy et componentN. Indispensable.

## Petite histoire

Nora remplace 40 lignes de Java par `data class User(val id: Int, val name: String, val email: String)`. Le compilateur fait le reste.

## A retenir

- `data class` = equals + hashCode + toString + copy auto.
- Destructuration avec `val (a, b) = objet`.
- `.copy(champ = nouvelleValeur)` pour cloner avec modification.
