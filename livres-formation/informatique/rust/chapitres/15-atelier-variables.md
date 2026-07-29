# Atelier : variables et types

## Exercice 1 : carte d'identite

```rust
let prenom = "Sam";
let age = 22;
let ville = "Nantes";
println!("Je suis {prenom}, {age} ans, je vis a {ville}.");
```

## Exercice 2 : shadowing

```rust
let x = 5;
let x = x + 1;
let x = x * 2;
println!("{x}"); // 12
```

## Exercice 3 : conversion

```rust
let texte = "42";
let nombre: i32 = texte.parse().unwrap();
let flottant = nombre as f64;
println!("{flottant}"); // 42.0
```

## Defi : temperature

```rust
let celsius = 37.0_f64;
let fahrenheit = celsius * 9.0 / 5.0 + 32.0;
println!("{celsius}°C = {fahrenheit:.1}°F");
```

> **Astuce DanielCraft** - `:.1` formate avec 1 decimale. `:.2` avec 2.

## A retenir

- `let` pour immutable, `let mut` pour mutable.
- Shadowing = redeclarer sans `mut`.
- `as` pour les casts entre types numeriques.
