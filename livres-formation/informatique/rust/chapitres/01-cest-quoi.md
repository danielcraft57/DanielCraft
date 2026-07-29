# C'est quoi Rust ?

## Le langage en une phrase

Rust est un langage systeme cree par Mozilla en 2010. Il garantit la securite memoire sans ramasse-miettes (garbage collector). Il est aussi rapide que C et C++ mais elimine des categories entieres de bugs.

## Pourquoi apprendre Rust ?

Rust est elu "langage le plus aime" sur Stack Overflow depuis 8 ans consecutifs. Il est utilise par Microsoft, Google, Amazon, Meta et Cloudflare. Linux l'integre dans son noyau.

> **Astuce DanielCraft** - Rust est exigeant mais recompense : un code qui compile fonctionne presque toujours correctement.

Nora decouvre Rust en cherchant un langage rapide et sur. Elle ecrit un petit outil CLI qui traite des fichiers en parallele, sans crash.

## A quoi ca ressemble ?

```rust
fn main() {
    let nom = "Lea";
    println!("Salut {nom}, bienvenue en Rust !");
}
```

## Petite histoire

Graydon Hoare cree Rust chez Mozilla pour construire un navigateur web plus sur. Le langage grandit, se stabilise en 2015 (version 1.0), et conquiert les systemes, le cloud et le WebAssembly.

## En vrai

Sam utilise Rust pour creer un outil de parsing ultra-rapide. Max ecrit un serveur HTTP avec Actix. Nora compile en WebAssembly pour le navigateur.

> **Piege** - Le compilateur Rust est strict. Il refuse du code que d'autres langages accepteraient. C'est voulu : il previent les bugs avant l'execution.

## A retenir

- Rust = securite memoire + performance.
- Pas de garbage collector.
- Le compilateur est ton meilleur allie.
