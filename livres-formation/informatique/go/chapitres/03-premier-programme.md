# Premier programme

## Hello World en Go

```go
package main

import "fmt"

func main() {
    fmt.Println("Bonjour le monde !")
}
```

Chaque programme Go commence par `package main` et une fonction `main()`. `fmt.Println` affiche du texte.

## Compiler et executer

```bash
go run main.go        # Compile et execute
go build -o app.exe   # Compile en binaire
./app.exe             # Execute le binaire
```

> **Astuce DanielCraft** - `go run` pour tester vite. `go build` pour produire un binaire distributable.

## Structure minimale

- `package main` : le point d'entree.
- `import` : les paquets utilises.
- `func main()` : la fonction executee au demarrage.

## Les commentaires

```go
// Commentaire sur une ligne
/* Commentaire
   sur plusieurs lignes */
```

## Petite histoire

Nora cree `main.go`, tape le hello world, lance `go run main.go`. Le message apparait. Elle modifie le texte, relance, et c'est instantane. La compilation Go est ultra-rapide.

## A retenir

- `package main` + `func main()` = point d'entree.
- `fmt.Println()` pour afficher.
- `go run` pour tester, `go build` pour compiler.
