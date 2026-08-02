# Slices et maps

## Les slices

Un slice est une vue flexible sur un tableau. C'est le conteneur le plus utilise en Go.

```go
fruits := []string{"pomme", "banane", "cerise"}
fmt.Println(fruits[0])   // pomme
fmt.Println(len(fruits)) // 3
```

## Ajouter un element

```go
fruits = append(fruits, "kiwi")
```

`append` retourne un nouveau slice (Go ne modifie pas en place).

## Sous-slices

```go
nombres := []int{0, 1, 2, 3, 4, 5}
fmt.Println(nombres[1:4]) // [1 2 3]
fmt.Println(nombres[:3])  // [0 1 2]
fmt.Println(nombres[3:])  // [3 4 5]
```

## Les maps

Une map associe des cles a des valeurs (comme un dictionnaire).

```go
ages := map[string]int{
    "Lea": 28,
    "Max": 24,
}
ages["Sam"] = 22
fmt.Println(ages["Lea"]) // 28
```

## Verifier l'existence

```go
age, ok := ages["Nora"]
if !ok {
    fmt.Println("Nora pas trouvee")
}
```

> **Astuce DanielCraft** - Toujours utiliser le pattern `val, ok := map[cle]` pour eviter les zero values.

## Supprimer

```go
delete(ages, "Max")
```

## Petite histoire

Nora stocke les prix dans une map. Elle parcourt avec `range` et calcule le total en 3 lignes.

## A retenir

- Slice = liste flexible, `append` pour ajouter.
- Map = paires cle-valeur, `delete` pour supprimer.
- `val, ok := map[k]` pour verifier l'existence.
