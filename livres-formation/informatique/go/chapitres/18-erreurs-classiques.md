# Erreurs classiques en Go

## Les pieges des debutants

## 1. Variable declaree non utilisee

```go
x := 42
// Erreur de compilation si x n'est pas utilise
```

Go refuse le code mort. Utilise `_` si tu veux ignorer une valeur.

## 2. Ignorer les erreurs

```go
fichier, _ := os.Open("data.txt") // Dangereux !
```

Toujours verifier `err`.

## 3. Nil pointer dereference

```go
var p *Personne
fmt.Println(p.Nom) // panic: nil pointer dereference
```

Verifie `nil` avant d'acceder aux champs d'un pointeur.

## 4. Shadowing de variable

```go
x := 10
if true {
    x := 20 // Nouvelle variable locale, pas la meme !
    fmt.Println(x) // 20
}
fmt.Println(x) // 10
```

## 5. Slice et reference partagee

```go
a := []int{1, 2, 3}
b := a[:2]
b[0] = 99
fmt.Println(a[0]) // 99 ! Les slices partagent la memoire.
```

## 6. Boucle range et pointeur

```go
items := []Item{{Nom: "A"}, {Nom: "B"}}
var ptrs []*Item
for _, item := range items {
    ptrs = append(ptrs, &item) // Tous pointent vers la meme adresse !
}
```

> **Astuce DanielCraft** - Utilise `go vet` pour detecter les erreurs courantes automatiquement.

## A retenir

- Le compilateur Go est strict : profite-en.
- Toujours verifier `err`.
- Attention aux slices qui partagent la memoire.
