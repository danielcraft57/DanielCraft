# Les types de donnees

## Les types scalaires

| Type | Exemples | Usage |
|------|----------|-------|
| `i32` | `42` | Entier signe 32 bits (defaut) |
| `i64` | `9_000_000_000` | Grand entier |
| `u32` | `0..4 milliards` | Entier non signe |
| `f64` | `3.14` | Flottant 64 bits (defaut) |
| `bool` | `true` / `false` | Booleen |
| `char` | `'A'`, `'é'` | Caractere Unicode |

## Les strings

```rust
let s1 = "Bonjour";           // &str (reference, immutable)
let s2 = String::from("Salut"); // String (sur le tas, mutable)
```

## Inference de type

```rust
let x = 42;        // i32 par defaut
let y = 3.14;      // f64 par defaut
let z: u8 = 255;   // Type explicite
```

## Conversion

```rust
let i = 42i32;
let f = i as f64;            // Cast
let s = i.to_string();      // Vers String
let n: i32 = "42".parse().unwrap(); // Parse
```

> **Astuce DanielCraft** - Rust ne fait aucune conversion implicite. Chaque cast est explicite et visible.

## Tuples et tableaux

```rust
let point = (10, 20);      // Tuple
let coords = [1, 2, 3, 4]; // Tableau fixe
println!("{}", point.0);    // 10
println!("{}", coords[2]);  // 3
```

## Petite histoire

Nora additionne un `i32` et un `f64`. Rust refuse. Elle ajoute `as f64` et comprend : pas de magie, tout est explicite.

## A retenir

- `i32` et `f64` par defaut.
- `&str` (reference) vs `String` (possede).
- Pas de conversion implicite.
