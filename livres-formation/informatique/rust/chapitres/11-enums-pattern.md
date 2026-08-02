# Enums et pattern matching

## Les enums

Une enum definit un type avec plusieurs variantes.

```rust
enum Direction {
    Nord,
    Sud,
    Est,
    Ouest,
}

let dir = Direction::Nord;
```

## Enums avec donnees

```rust
enum Message {
    Quitter,
    Texte(String),
    Position { x: i32, y: i32 },
}

let msg = Message::Texte(String::from("Bonjour"));
```

## match avec enums

```rust
match dir {
    Direction::Nord => println!("Vers le nord"),
    Direction::Sud => println!("Vers le sud"),
    Direction::Est => println!("Vers l'est"),
    Direction::Ouest => println!("Vers l'ouest"),
}
```

## Option<T>

Rust n'a pas de `null`. A la place, `Option<T>` :

```rust
fn trouver(liste: &[i32], cible: i32) -> Option<usize> {
    liste.iter().position(|&x| x == cible)
}

match trouver(&[1, 2, 3], 2) {
    Some(index) => println!("Trouve a l'index {index}"),
    None => println!("Non trouve"),
}
```

## if let

```rust
if let Some(i) = trouver(&[1, 2, 3], 2) {
    println!("Index : {i}");
}
```

> **Astuce DanielCraft** - `Option` et `Result` remplacent null et les exceptions. Le compilateur t'oblige a gerer les deux cas.

## Petite histoire

Nora cherche un element dans un vecteur. La fonction retourne `Option`. Le compilateur l'oblige a gerer le cas "absent". Plus de crash surprise.

## A retenir

- `enum` pour les variantes.
- `match` est exhaustif.
- `Option<T>` = Some(valeur) ou None.
- Pas de null en Rust.
