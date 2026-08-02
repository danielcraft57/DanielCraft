# L'ownership

## Le concept central de Rust

L'ownership (possession) est ce qui rend Rust unique. Chaque valeur a un seul proprietaire. Quand le proprietaire sort du scope, la valeur est liberee.

```rust
{
    let s = String::from("Bonjour");
    // s est valide ici
} // s est libere automatiquement
```

## Le deplacement (move)

```rust
let s1 = String::from("Salut");
let s2 = s1;  // s1 est "deplace" vers s2
// println!("{s1}"); // Erreur ! s1 n'existe plus
println!("{s2}");    // OK
```

## Le clonage

```rust
let s1 = String::from("Salut");
let s2 = s1.clone();  // Copie profonde
println!("{s1} {s2}"); // OK
```

## Les references (emprunt)

```rust
fn longueur(s: &String) -> usize {
    s.len()
}

let mot = String::from("Bonjour");
let len = longueur(&mot);  // Emprunte sans prendre possession
println!("{mot} fait {len} caracteres");
```

## References mutables

```rust
fn ajouter_monde(s: &mut String) {
    s.push_str(" monde !");
}

let mut salut = String::from("Bonjour");
ajouter_monde(&mut salut);
```

> **Piege** - Une seule reference mutable OU plusieurs references immutables a la fois. Jamais les deux. C'est ce qui previent les data races.

## Petite histoire

Nora passe un `String` a une fonction. Le compilateur refuse de l'utiliser ensuite. Elle ajoute `&` et comprend l'emprunt.

## A retenir

- Chaque valeur a un proprietaire unique.
- Le deplacement transfere la possession.
- `&` emprunte, `&mut` emprunte de facon mutable.
- Une seule `&mut` OU plusieurs `&` a la fois.
