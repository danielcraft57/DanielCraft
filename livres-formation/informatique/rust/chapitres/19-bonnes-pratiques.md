# Bonnes pratiques

## Conventions Rust

- **snake_case** : variables, fonctions, modules.
- **PascalCase** : types, structs, enums, traits.
- **SCREAMING_SNAKE_CASE** : constantes.
- **Clippy** : linter officiel, `cargo clippy`.

## Structure de projet

```
mon-projet/
  Cargo.toml       # Dependances et metadata
  src/
    main.rs         # Point d'entree
    lib.rs          # Bibliotheque (optionnel)
```

## Gestion des erreurs

```rust
// Prefere ceci :
let contenu = fs::read_to_string("data.txt")?;

// Plutot que :
let contenu = fs::read_to_string("data.txt").unwrap();
```

## Documentation

```rust
/// Calcule le prix TTC a partir du HT.
///
/// # Exemples
/// ```
/// let ttc = calculer_ttc(100.0);
/// assert_eq!(ttc, 120.0);
/// ```
fn calculer_ttc(ht: f64) -> f64 {
    ht * 1.20
}
```

Les doc-tests (`///`) sont executes par `cargo test`.

## Outils

- `cargo fmt` : formatage automatique.
- `cargo clippy` : suggestions d'amelioration.
- `cargo test` : tests unitaires et doc-tests.

> **Astuce DanielCraft** - Lance `cargo clippy` avant chaque commit. Il detecte les patterns non idiomatiques.

## A retenir

- `cargo fmt` + `cargo clippy` + `cargo test` = qualite.
- `?` pour propager les erreurs.
- Doc-tests dans les commentaires `///`.
