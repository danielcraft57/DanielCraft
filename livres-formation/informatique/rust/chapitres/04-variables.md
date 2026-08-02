# Les variables

## Immutabilite par defaut

En Rust, les variables sont immutables par defaut. Pour les rendre mutables, on ajoute `mut`.

```rust
let nom = "Max";       // Immutable
let mut score = 0;     // Mutable
score += 10;
println!("{score}");   // 10
```

## Shadowing

On peut redeclarer une variable avec le meme nom :

```rust
let x = 5;
let x = x + 1;     // Nouveau x, pas de mut necessaire
let x = x * 2;
println!("{x}");    // 12
```

Le shadowing permet de changer le type :

```rust
let texte = "42";
let texte: i32 = texte.parse().unwrap();
```

## Constantes

```rust
const TVA: f64 = 0.20;
const MAX_JOUEURS: u32 = 100;
```

> **Astuce DanielCraft** - Immutable par defaut, c'est le choix de Rust pour prevenir les bugs. Utilise `mut` seulement quand c'est necessaire.

## Conventions

- snake_case pour les variables et fonctions : `mon_score`.
- SCREAMING_SNAKE_CASE pour les constantes : `MAX_JOUEURS`.
- PascalCase pour les types et structs : `MonType`.

## Petite histoire

Sam declare `let budget = 1800;` puis essaie `budget = 1500;`. Le compilateur refuse. Il ajoute `mut` et comprend le principe.

## A retenir

- `let` = immutable, `let mut` = mutable.
- Shadowing pour redeclarer sans `mut`.
- `const` pour les constantes (type obligatoire).
