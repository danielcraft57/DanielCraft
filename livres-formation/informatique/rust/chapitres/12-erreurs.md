# Gerer les erreurs

## Result<T, E>

Rust utilise `Result` pour les operations qui peuvent echouer :

```rust
use std::fs;

fn lire_fichier(chemin: &str) -> Result<String, std::io::Error> {
    fs::read_to_string(chemin)
}

match lire_fichier("data.txt") {
    Ok(contenu) => println!("{contenu}"),
    Err(e) => println!("Erreur : {e}"),
}
```

## L'operateur ?

```rust
fn lire_et_compter(chemin: &str) -> Result<usize, std::io::Error> {
    let contenu = fs::read_to_string(chemin)?; // Propage l'erreur
    Ok(contenu.len())
}
```

`?` retourne l'erreur automatiquement si le Result est Err.

## unwrap et expect

```rust
let n: i32 = "42".parse().unwrap();        // Panique si erreur
let n: i32 = "42".parse().expect("Pas un nombre"); // Message custom
```

> **Piege** - `unwrap()` panique (crash). Utilise-le seulement dans les tests ou quand tu es certain du resultat.

## Creer ses propres erreurs

```rust
fn retirer(solde: f64, montant: f64) -> Result<f64, String> {
    if montant > solde {
        return Err(String::from("Solde insuffisant"));
    }
    Ok(solde - montant)
}
```

## Petite histoire

Max utilise `unwrap()` partout. Son programme panique sur un fichier manquant. Il remplace par `?` et gere proprement l'erreur.

## A retenir

- `Result<T, E>` = Ok(valeur) ou Err(erreur).
- `?` propage l'erreur elegamment.
- `unwrap()` = panique. A eviter en production.
