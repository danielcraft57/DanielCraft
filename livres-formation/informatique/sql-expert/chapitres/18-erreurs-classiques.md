# Erreurs classiques niveau expert

| Erreur | Pourquoi | Fix |
|--------|----------|-----|
| Index partout | Ecritures lentes, plans pires | Indexer les filtres reels |
| DISTINCT pour "nettoyer" | Cache un JOIN mal fait | Corriger la jointure |
| Transaction geante | Verrous, timeouts | Decouper |
| OFFSET 100000 | De plus en plus lent | Keyset pagination |
| Recursive sans limite | Explosion / cycle | Cap profondeur |

> **Piege** - Optimiser une requete rare pendant que le N+1 de l'API detruit la prod.

## A retenir

- Expert = eviter les fausses optimisations.
