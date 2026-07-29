# Atelier : audit checklist API

**Duree** : 20 minutes.

## Mission

Auditer une API REST fictive `/api/v1/orders` avec ces constats :

- JWT en localStorage.
- Pas de rate limit sur POST.
- Erreurs 500 avec stack trace.
- CORS `*`.

## A faire

1. Classer chaque point : critique / majeur / mineur.
2. Proposer le correctif concret.
3. Prioriser l'ordre de correction.

## Correction type

1. JWT -> cookie HttpOnly + refresh rotation.
2. Rate limit -> 100 req/min par token.
3. Erreurs -> JSON generique + log serveur.
4. CORS -> origines explicites.

## A retenir

- Audit = prioriser par impact x facilite.
