# Les structs

## Definir une struct

```rust
struct Animal {
    nom: String,
    age: u32,
}

fn main() {
    let chat = Animal {
        nom: String::from("Felix"),
        age: 3,
    };
    println!("{} a {} ans", chat.nom, chat.age);
}
```

## Methodes avec impl

```rust
impl Animal {
    fn se_presenter(&self) -> String {
        format!("Je suis {}, {} ans.", self.nom, self.age)
    }

    fn new(nom: &str, age: u32) -> Self {
        Self {
            nom: String::from(nom),
            age,
        }
    }
}

let chat = Animal::new("Felix", 3);
println!("{}", chat.se_presenter());
```

`&self` emprunte la struct. `Self` est un alias pour le type.

## Tuple structs

```rust
struct Point(f64, f64);
let p = Point(1.0, 2.5);
println!("{} {}", p.0, p.1);
```

## Derive

```rust
#[derive(Debug, Clone)]
struct Produit {
    nom: String,
    prix: f64,
}

let p = Produit { nom: String::from("Clavier"), prix: 49.99 };
println!("{:?}", p); // Debug
```

> **Astuce DanielCraft** - `#[derive(Debug)]` permet d'afficher une struct avec `{:?}`. Indispensable pour le debug.

## Petite histoire

Max modele un `Produit` avec `impl`. Il ajoute `#[derive(Debug)]` et peut inspecter ses objets facilement.

## A retenir

- `struct` pour les donnees, `impl` pour les methodes.
- `&self` pour emprunter, `Self` pour le type.
- `#[derive(Debug)]` pour l'affichage.
