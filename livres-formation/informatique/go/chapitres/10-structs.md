# Les structs

## C'est quoi une struct ?

Go n'a pas de classes. A la place, on utilise des structs pour regrouper des donnees, et des methodes associees.

```go
type Animal struct {
    Nom string
    Age int
}

func main() {
    chat := Animal{Nom: "Felix", Age: 3}
    fmt.Println(chat.Nom) // Felix
}
```

## Methodes sur struct

```go
func (a Animal) SePresenter() string {
    return fmt.Sprintf("Je suis %s, %d ans.", a.Nom, a.Age)
}

fmt.Println(chat.SePresenter())
```

Le `(a Animal)` avant le nom est le "receiver". Il lie la methode a la struct.

## Receiver pointeur

```go
func (a *Animal) Vieillir() {
    a.Age++
}

chat.Vieillir()
fmt.Println(chat.Age) // 4
```

Avec `*Animal` (pointeur), la methode modifie la struct originale.

> **Astuce DanielCraft** - Utilise un receiver pointeur quand tu veux modifier la struct ou eviter une copie couteuse.

## Composition (pas d'heritage)

```go
type Chat struct {
    Animal   // Embedding : Chat "contient" un Animal
    Interieur bool
}

felix := Chat{
    Animal:   Animal{Nom: "Felix", Age: 3},
    Interieur: true,
}
fmt.Println(felix.Nom) // Felix (acces direct via embedding)
```

## Petite histoire

Max modele un `Produit` avec nom et prix. Il cree une methode `Afficher()`. Simple, explicite, pas de magie.

## A retenir

- `type NomStruct struct { ... }` pour definir.
- Methodes avec receiver : `func (s *Struct) Methode()`.
- Composition (embedding) au lieu d'heritage.
