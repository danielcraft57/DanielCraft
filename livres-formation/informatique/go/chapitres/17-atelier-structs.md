# Atelier : structs et interfaces

## Objectif

Modeliser des donnees avec des structs et utiliser des interfaces.

## Exercice 1 : struct Produit

```go
type Produit struct {
    Nom  string
    Prix float64
}

func (p Produit) Afficher() string {
    return fmt.Sprintf("%s - %.2f EUR", p.Nom, p.Prix)
}
```

## Exercice 2 : panier

```go
type Panier struct {
    produits []Produit
}

func (p *Panier) Ajouter(prod Produit) {
    p.produits = append(p.produits, prod)
}

func (p Panier) Total() float64 {
    t := 0.0
    for _, prod := range p.produits {
        t += prod.Prix
    }
    return t
}
```

## Exercice 3 : interface Forme

```go
type Forme interface {
    Aire() float64
}

type Cercle struct { Rayon float64 }
type Rectangle struct { L, H float64 }

func (c Cercle) Aire() float64    { return math.Pi * c.Rayon * c.Rayon }
func (r Rectangle) Aire() float64 { return r.L * r.H }

func afficherAire(f Forme) {
    fmt.Printf("Aire : %.2f\n", f.Aire())
}
```

> **Astuce DanielCraft** - Pense "composition" plutot que "heritage". Go privilegie les petites interfaces.

## A retenir

- Structs pour les donnees, methodes pour le comportement.
- Interfaces implicites : pas besoin de declarer `implements`.
- Receiver pointeur pour modifier la struct.
