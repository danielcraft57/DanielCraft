# Atelier : structs et enums

## Exercice 1 : struct Produit

```rust
#[derive(Debug)]
struct Produit {
    nom: String,
    prix: f64,
}

impl Produit {
    fn new(nom: &str, prix: f64) -> Self {
        Self { nom: String::from(nom), prix }
    }
    fn afficher(&self) -> String {
        format!("{} - {:.2} EUR", self.nom, self.prix)
    }
}
```

## Exercice 2 : panier

```rust
struct Panier {
    produits: Vec<Produit>,
}

impl Panier {
    fn new() -> Self { Self { produits: vec![] } }
    fn ajouter(&mut self, p: Produit) { self.produits.push(p); }
    fn total(&self) -> f64 {
        self.produits.iter().map(|p| p.prix).sum()
    }
}
```

## Exercice 3 : enum Forme

```rust
use std::f64::consts::PI;

enum Forme {
    Cercle(f64),
    Rectangle(f64, f64),
}

impl Forme {
    fn aire(&self) -> f64 {
        match self {
            Forme::Cercle(r) => PI * r * r,
            Forme::Rectangle(l, h) => l * h,
        }
    }
}
```

> **Astuce DanielCraft** - `&mut self` pour modifier, `&self` pour lire.

## A retenir

- `#[derive(Debug)]` pour inspecter.
- `impl` separe donnees et comportement.
- `match` sur les enums pour le polymorphisme.
