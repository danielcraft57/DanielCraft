# Authentification robuste

## Principes

- Mots de passe hashes avec **bcrypt/Argon2** (jamais MD5/SHA1 seuls).
- **2FA** pour les comptes sensibles.
- Limiter les tentatives de connexion (rate limiting).
- Invalider les sessions au logout.

## Flux securise

1. Login -> verifier hash + 2FA si active.
2. Creer session avec ID aleatoire long.
3. Cookie `HttpOnly`, `Secure`, `SameSite`.
4. Timeout d'inactivite.

> **Astuce DanielCraft** - Ne reinvente pas l'auth. Utilise un framework ou un service eprouve (OAuth, Auth0, etc.).

## A retenir

- Hash fort + 2FA + rate limit + cookies securises.
