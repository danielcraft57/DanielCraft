# Les boucles

## for et ranges

```kotlin
for (i in 0..4) {
    println(i)  // 0, 1, 2, 3, 4
}

for (i in 0 until 5) {
    println(i)  // 0, 1, 2, 3, 4 (5 exclu)
}

for (i in 5 downTo 1 step 2) {
    println(i)  // 5, 3, 1
}
```

## Parcourir une collection

```kotlin
val fruits = listOf("pomme", "banane", "cerise")
for (fruit in fruits) {
    println(fruit)
}

fruits.forEach { println(it) }
```

## while et do-while

```kotlin
var n = 0
while (n < 5) {
    println(n)
    n++
}
```

## break et continue

```kotlin
for (i in 0..10) {
    if (i == 5) break
    if (i % 2 == 0) continue
    println(i)  // 1, 3
}
```

> **Astuce DanielCraft** - `for (x in collection)` est l'idiome principal. Evite les index manuels quand possible.

## Petite histoire

Sam utilise `for (i in 1..100)` pour calculer une somme. Pas de variable d'index separee, pas d'oubli d'incrementation.

## A retenir

- `0..4` = range inclusif, `0 until 5` = exclusif.
- `for (x in liste)` pour parcourir.
- `forEach { }` pour les lambdas.
