# Premier programme

## Hello World

```rust
fn main() {
    println!("Bonjour le monde !");
}
```

`fn main()` est le point d'entree. `println!` est une macro (le `!` l'indique) qui affiche du texte.

## Compiler et executer

```bash
cargo run          # Compile et execute
cargo build        # Compile seulement
cargo build --release  # Compile optimise
```

> **Astuce DanielCraft** - `cargo run` pour developper. `--release` pour la production.

## Affichage formate

```rust
let nom = "Lea";
let age = 28;
println!("Je suis {nom}, {age} ans.");
println!("{} + {} = {}", 2, 3, 2 + 3);
```

## Les commentaires

```rust
// Commentaire sur une ligne
/* Commentaire
   sur plusieurs lignes */
/// Documentation (genere du HTML avec cargo doc)
```

## Petite histoire

Nora cree un projet avec `cargo new`, modifie `src/main.rs`, lance `cargo run`. La compilation est rapide et le message apparait.

## A retenir

- `fn main()` = point d'entree.
- `println!()` pour afficher (c'est une macro).
- `cargo run` pour compiler et executer.
