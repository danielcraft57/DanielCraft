# Erreurs classiques en Rust

## 1. Utiliser une valeur apres un move

```rust
let s = String::from("Bonjour");
let s2 = s;
// println!("{s}"); // Erreur : s a ete deplace
```

Solution : cloner ou emprunter avec `&`.

## 2. Reference mutable + immutable

```rust
let mut v = vec![1, 2, 3];
let r = &v[0];
v.push(4); // Erreur : v est emprunte immutablement par r
println!("{r}");
```

## 3. Oublier le point-virgule

```rust
fn double(x: i32) -> i32 {
    x * 2;  // Le ; transforme l'expression en statement (retourne ())
}
```

Enleve le `;` pour retourner la valeur.

## 4. unwrap() en production

```rust
let fichier = fs::read_to_string("absent.txt").unwrap(); // Panique !
```

Utilise `?` ou `match` a la place.

## 5. Confusion &str vs String

```rust
fn saluer(nom: String) {} // Prend possession
fn saluer(nom: &str) {}   // Emprunte seulement (prefere)
```

## 6. Oublier mut

```rust
let v = vec![1, 2, 3];
v.push(4); // Erreur : v n'est pas mutable
```

> **Astuce DanielCraft** - Le compilateur Rust donne des messages d'erreur excellents. Lis-les en entier, ils contiennent souvent la solution.

## A retenir

- Move != copie. Emprunte avec `&` quand possible.
- Pas de `;` pour retourner une valeur.
- `?` au lieu de `unwrap()` en production.
