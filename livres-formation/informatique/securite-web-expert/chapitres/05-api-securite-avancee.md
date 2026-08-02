# API : securite avancee

Une API en production doit resister aux abus, pas seulement aux bugs.

## Checklist expert

- **Auth** : OAuth2, API keys rotables, scopes.
- **Versioning** : deprecier sans casser la securite.
- **Pagination** : limiter la charge (max 100 items).
- **Idempotency-Key** sur POST sensibles.
- **Schema strict** : rejeter champs inconnus (mass assignment).

```json
{
  "error": "invalid_scope",
  "message": "Scope orders:write requis"
}
```

## Rate limiting avance

- Par cle API + IP + endpoint.
- Slowdown progressif avant blocage.

## A retenir

- API = surface d'attaque large : durcir chaque couche.
- Erreurs explicites pour le client, pas de stack trace.
