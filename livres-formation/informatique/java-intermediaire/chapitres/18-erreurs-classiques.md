# Erreurs classiques

| Erreur | Fix |
|--------|-----|
| `get()` sur Optional vide | `orElse` / `ifPresent` |
| Modifier une List pendant for-each | Iterator / `removeIf` |
| Catch vide | Logger ou remonter |
| Heritage a 6 niveaux | Composition |
| `==` sur Integer caches | `equals` |

## A retenir

- Les pieges courants ont des antidotes simples.
