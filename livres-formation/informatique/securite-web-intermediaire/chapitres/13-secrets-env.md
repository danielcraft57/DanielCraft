# Secrets et variables d'environnement

## Regle d'or

**Jamais** de secrets dans le code source ou Git.

```python
# Mauvais
API_KEY = "sk-abc123..."

# Bon
import os
API_KEY = os.environ["API_KEY"]
```

## Bonnes pratiques

- Fichier `.env` local (dans `.gitignore`).
- Vault / secrets manager en production.
- Rotation reguliere des cles.
- Separer dev/staging/prod.

## A retenir

- Secrets = variables d'environnement ou vault.
- .env jamais commite.
