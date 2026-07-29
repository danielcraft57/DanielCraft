# JWT et sessions

## JWT (JSON Web Token)

Un **JWT** est un token signe contenant des claims (user id, expiration).

```
header.payload.signature
```

## Bonnes pratiques

- **Expiration courte** (15 min access + refresh token).
- Stocker en **HttpOnly cookie**, pas localStorage (XSS).
- Verifier la signature a chaque requete.
- Algorithme **RS256** ou **ES256**, pas HS256 avec secret faible.

## Sessions classiques vs JWT

| | Session serveur | JWT |
|---|----------------|-----|
| Revocation | Facile | Difficile (blacklist) |
| Scalabilite | Store partage | Stateless |
| XSS | Cookie HttpOnly | Attention localStorage |

## A retenir

- JWT = pratique mais pas magique.
- HttpOnly cookie > localStorage.
