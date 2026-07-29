# Atelier : variables et types

## Objectif

Pratiquer les declarations, conversions et affichage formate.

## Exercice 1 : carte d'identite

```go
nom := "Sam"
age := 22
ville := "Nantes"
fmt.Printf("Je suis %s, %d ans, je vis a %s.\n", nom, age, ville)
```

## Exercice 2 : convertisseur EUR -> USD

```go
import "fmt"

func main() {
    var euros float64
    fmt.Print("Montant en EUR : ")
    fmt.Scanln(&euros)
    dollars := euros * 1.08
    fmt.Printf("%.2f EUR = %.2f USD\n", euros, dollars)
}
```

## Exercice 3 : swap sans variable temporaire

```go
a, b := 5, 9
a, b = b, a
fmt.Println(a, b) // 9 5
```

## Defi : aire du cercle

```go
import "math"

rayon := 5.0
fmt.Printf("Perimetre : %.2f\n", 2*math.Pi*rayon)
fmt.Printf("Aire : %.2f\n", math.Pi*rayon*rayon)
```

> **Astuce DanielCraft** - `%.2f` formate avec 2 decimales. `%d` pour les entiers, `%s` pour les strings.

## A retenir

- `:=` pour declarer vite.
- `fmt.Printf` avec les verbes de format.
- Go permet le swap : `a, b = b, a`.
