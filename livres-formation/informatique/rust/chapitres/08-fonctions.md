# Les fonctions

## Declarer une fonction

```rust
fn saluer(prenom: &str) {
    println!("Bonjour {prenom} !");
}

fn main() {
    saluer("Nora");
}
```

## Retourner une valeur

```rust
fn additionner(a: i32, b: i32) -> i32 {
    a + b  // Pas de ; = expression retournee
}
```

En Rust, la derniere expression (sans `;`) est la valeur de retour.

## Return explicite

```rust
fn diviser(a: f64, b: f64) -> f64 {
    if b == 0.0 {
        return 0.0; // Retour anticipe
    }
    a / b
}
```

## Closures

```rust
let doubler = |x: i32| x * 2;
println!("{}", doubler(5)); // 10

let mut nombres = vec![3, 1, 2];
nombres.sort_by(|a, b| a.cmp(b));
```

> **Astuce DanielCraft** - Pas de `;` a la fin = expression retournee. C'est une convention forte en Rust.

## Petite histoire

Max ecrit une fonction `calculer_ttc(prix: f64) -> f64`. Il oublie le `;` a la fin, et ca marche. Il comprend le principe des expressions.

## A retenir

- `fn nom(params) -> TypeRetour { ... }`
- Derniere expression sans `;` = retour.
- Closures avec `|params| expression`.
