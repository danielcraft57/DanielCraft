# Les boucles

## loop : boucle infinie

```rust
let mut compteur = 0;
loop {
    compteur += 1;
    if compteur == 5 { break; }
}
```

`loop` peut retourner une valeur :

```rust
let resultat = loop {
    compteur += 1;
    if compteur == 10 { break compteur * 2; }
};
```

## while

```rust
let mut n = 0;
while n < 5 {
    println!("{n}");
    n += 1;
}
```

## for et ranges

```rust
for i in 0..5 {
    println!("{i}"); // 0, 1, 2, 3, 4
}

for i in 0..=5 {
    println!("{i}"); // 0, 1, 2, 3, 4, 5 (inclusif)
}
```

## Parcourir une collection

```rust
let fruits = vec!["pomme", "banane", "cerise"];
for fruit in &fruits {
    println!("{fruit}");
}
```

> **Astuce DanielCraft** - `&fruits` emprunte la collection. Sans `&`, la boucle consommerait le vecteur.

## break et continue

```rust
for i in 0..10 {
    if i == 5 { break; }
    if i % 2 == 0 { continue; }
    println!("{i}"); // 1, 3
}
```

## Petite histoire

Sam utilise `for i in 0..100` pour calculer une somme. Pas de variable d'index separee, pas d'oubli d'incrementation.

## A retenir

- `loop` = infini, peut retourner une valeur.
- `for i in 0..n` pour les ranges.
- `&collection` pour emprunter dans un `for`.
