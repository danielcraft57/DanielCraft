# Installer Rust

## Ce qu'il te faut

Rust s'installe avec `rustup`, l'outil officiel qui gere les versions du compilateur et les outils associes.

## Installer rustup

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Sur Windows : telecharge `rustup-init.exe` depuis rustup.rs.

Apres l'installation :

```bash
rustc --version
cargo --version
```

## Cargo : le gestionnaire de projet

Cargo est l'outil central de Rust : il compile, teste, gere les dependances et publie.

```bash
cargo new mon-projet
cd mon-projet
cargo run
```

> **Astuce DanielCraft** - Cargo fait tout. Tu n'auras presque jamais besoin d'appeler `rustc` directement.

## Installer VS Code

Installe l'extension "rust-analyzer" pour l'auto-completion, les erreurs en temps reel et la navigation dans le code.

## Petite histoire

Max installe Rust en 2 minutes avec `rustup`. Il tape `cargo new hello`, `cargo run`, et voit "Hello, world!" immediatement.

## A retenir

- `rustup` pour installer et mettre a jour Rust.
- `cargo` pour tout : build, run, test, dependances.
- VS Code + rust-analyzer = environnement ideal.
