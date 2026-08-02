# Mini-projet : outil CLI de notes

## L'objectif

On cree un outil en ligne de commande qui permet d'ajouter, lister et chercher des notes. Sauvegarde en fichier texte simple.

## Structure (src/main.rs)

```rust
use std::fs;
use std::io::{self, Write};

const FICHIER: &str = "notes.txt";

fn charger() -> Vec<String> {
    fs::read_to_string(FICHIER)
        .unwrap_or_default()
        .lines()
        .filter(|l| !l.is_empty())
        .map(String::from)
        .collect()
}

fn sauvegarder(notes: &[String]) {
    let contenu = notes.join("\n");
    fs::write(FICHIER, contenu).expect("Impossible d'ecrire");
}

fn lire_ligne(prompt: &str) -> String {
    print!("{prompt}");
    io::stdout().flush().unwrap();
    let mut buf = String::new();
    io::stdin().read_line(&mut buf).unwrap();
    buf.trim().to_string()
}

fn main() {
    let mut notes = charger();
    loop {
        println!("\n1. Ajouter  2. Lister  3. Chercher  4. Quitter");
        match lire_ligne("> ").as_str() {
            "1" => {
                let note = lire_ligne("Note : ");
                if !note.is_empty() {
                    notes.push(note);
                    sauvegarder(&notes);
                    println!("Ajoutee.");
                }
            }
            "2" => {
                if notes.is_empty() {
                    println!("Aucune note.");
                } else {
                    for (i, n) in notes.iter().enumerate() {
                        println!("  {}. {n}", i + 1);
                    }
                }
            }
            "3" => {
                let terme = lire_ligne("Recherche : ").to_lowercase();
                for n in &notes {
                    if n.to_lowercase().contains(&terme) {
                        println!("  {n}");
                    }
                }
            }
            "4" => { println!("A bientot !"); break; }
            _ => {}
        }
    }
}
```

## Ce que tu apprends

- `std::fs` pour lire/ecrire des fichiers.
- `Vec<String>` et les iterateurs.
- `match` sur des chaines.
- Ownership : `&notes` pour emprunter.

> **Astuce DanielCraft** - Commence par le menu, puis ajoute une commande a la fois.

## A retenir

- Ownership et emprunt en action.
- Iterateurs pour transformer les donnees.
- `match` pour le menu.
