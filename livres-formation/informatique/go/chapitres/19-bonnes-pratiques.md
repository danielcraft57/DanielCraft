# Bonnes pratiques

## Conventions Go

- **gofmt** : formate automatiquement le code. Pas de debat sur le style.
- **camelCase** : variables et fonctions privees.
- **PascalCase** : fonctions et types exportes.
- **Pas d'underscore** dans les noms (convention forte).
- **Noms courts** : `i`, `err`, `ctx`, `req`, `resp` sont idiomatiques.

## Structure d'un fichier

```go
package monpackage

import (
    "fmt"
    "os"
)

// Types
type Config struct {
    Port int
}

// Fonctions
func NouvelleConfig() Config {
    return Config{Port: 8080}
}
```

## Gestion des erreurs

- Toujours verifier `err != nil`.
- Retourner les erreurs plutot que les logger silencieusement.
- Utiliser `fmt.Errorf("contexte: %w", err)` pour enrichir.

## Documentation

```go
// NouvelleConfig retourne une configuration par defaut.
func NouvelleConfig() Config {
    return Config{Port: 8080}
}
```

Les commentaires qui commencent par le nom de la fonction deviennent la documentation (`go doc`).

> **Astuce DanielCraft** - Lance `gofmt` et `go vet` avant chaque commit. Zero effort, maximum de qualite.

## A retenir

- `gofmt` formate, `go vet` detecte les erreurs.
- Noms courts et explicites.
- Retourner les erreurs, ne pas les ignorer.
