# Atelier : fonctions

## Exercice 1 : salutation

```rust
fn saluer(nom: &str, heure: u32) -> String {
    if heure < 12 {
        format!("Bonjour {nom} !")
    } else if heure < 18 {
        format!("Bon apres-midi {nom} !")
    } else {
        format!("Bonsoir {nom} !")
    }
}
```

## Exercice 2 : moyenne

```rust
fn moyenne(notes: &[f64]) -> f64 {
    if notes.is_empty() { return 0.0; }
    notes.iter().sum::<f64>() / notes.len() as f64
}
```

## Exercice 3 : mot de passe valide

```rust
fn mdp_valide(mdp: &str) -> bool {
    mdp.len() >= 8 && mdp.chars().any(|c| c.is_ascii_digit())
}
```

## Exercice 4 : division securisee

```rust
fn diviser(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err(String::from("Division par zero"))
    } else {
        Ok(a / b)
    }
}
```

> **Astuce DanielCraft** - `&[f64]` (slice) est plus flexible que `&Vec<f64>`.

## A retenir

- `&str` et `&[T]` pour les emprunts.
- Iterateurs (`.iter()`, `.sum()`, `.any()`) au lieu de boucles.
- `Result` pour les erreurs.
