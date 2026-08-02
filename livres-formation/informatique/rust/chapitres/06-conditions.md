# Les conditions

## if / else

```rust
let age = 17;
if age >= 18 {
    println!("Majeur");
} else {
    println!("Mineur");
}
```

Pas de parentheses, accolades obligatoires.

## if comme expression

```rust
let statut = if age >= 18 { "Majeur" } else { "Mineur" };
println!("{statut}");
```

En Rust, `if` est une expression qui retourne une valeur.

## else if

```rust
let note = 14;
let mention = if note >= 16 {
    "Tres bien"
} else if note >= 12 {
    "Bien"
} else if note >= 10 {
    "Passable"
} else {
    "Insuffisant"
};
```

## match

```rust
let jour = "lundi";
match jour {
    "lundi" | "mardi" => println!("Debut de semaine"),
    "vendredi" => println!("Presque le weekend"),
    _ => println!("Autre jour"),
}
```

`match` est exhaustif : il faut couvrir tous les cas (ou utiliser `_`).

> **Astuce DanielCraft** - `match` est plus puissant que `switch`. Il gere les patterns, les ranges, les destructurations.

## Petite histoire

Max ecrit un match sur une enum `Direction`. Le compilateur lui dit qu'il a oublie `Nord`. Il ajoute le cas et le code compile.

## A retenir

- `if` est une expression (retourne une valeur).
- Pas de parentheses, accolades obligatoires.
- `match` est exhaustif et tres puissant.
