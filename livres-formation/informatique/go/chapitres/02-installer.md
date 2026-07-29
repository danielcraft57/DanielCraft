# Installer Go

## Ce qu'il te faut

Pour coder en Go tu as besoin du compilateur Go et d'un editeur. VS Code avec l'extension Go officielle est le choix le plus populaire.

## Installer sur Windows

1. Va sur go.dev/dl, telecharge l'installeur Windows.
2. Lance l'installeur (il ajoute Go au PATH automatiquement).
3. Ouvre un terminal et tape `go version`.
4. Tu dois voir quelque chose comme `go1.22.x`.

## Installer sur Mac / Linux

```bash
# Mac avec Homebrew
brew install go

# Linux (telecharger l'archive depuis go.dev)
sudo tar -C /usr/local -xzf go1.22.x.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
```

> **Astuce DanielCraft** - Go gere ses modules lui-meme. Pas besoin d'un gestionnaire de paquets externe.

## Creer un premier projet

```bash
mkdir mon-projet
cd mon-projet
go mod init mon-projet
```

`go mod init` cree un fichier `go.mod` qui gere les dependances.

## Petite histoire

Max installe Go en 2 minutes. Il tape `go version` et tout fonctionne. Pas de configuration complexe, pas de variables d'environnement a regler.

## A retenir

- Telecharge Go sur go.dev.
- Verifie avec `go version`.
- `go mod init` pour creer un projet.
- VS Code + extension Go = environnement ideal.
