# Les boucles

## Une seule boucle : for

Go n'a qu'un seul mot-cle de boucle : `for`. Il remplace `for`, `while` et `foreach` des autres langages.

## For classique

```go
for i := 0; i < 5; i++ {
    fmt.Println(i)
}
```

## For comme while

```go
compteur := 0
for compteur < 3 {
    fmt.Println(compteur)
    compteur++
}
```

## For infini

```go
for {
    // Tourne indefiniment
    // break pour sortir
}
```

## Parcourir avec range

```go
fruits := []string{"pomme", "banane", "cerise"}
for i, fruit := range fruits {
    fmt.Printf("%d: %s\n", i, fruit)
}
```

`range` retourne l'index et la valeur. Si tu n'as pas besoin de l'index, utilise `_`.

```go
for _, fruit := range fruits {
    fmt.Println(fruit)
}
```

> **Astuce DanielCraft** - `_` est le "blank identifier". Il permet d'ignorer une valeur retournee.

## break et continue

```go
for i := 0; i < 10; i++ {
    if i == 5 { break }
    if i%2 == 0 { continue }
    fmt.Println(i) // 1, 3
}
```

## Petite histoire

Sam remplace un `while` et un `foreach` de Python par deux `for` Go. Un seul mot-cle, moins de confusion.

## A retenir

- `for` est la seule boucle en Go.
- `range` pour parcourir slices, maps, strings.
- `_` pour ignorer une valeur.
