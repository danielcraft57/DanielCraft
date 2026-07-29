# OAuth 2 et OpenID Connect (vue defense)

**OAuth 2** delegue l'autorisation ; **OpenID Connect (OIDC)** ajoute l'identite (id_token).

## Flux authorization code (recommande)

1. Redirection vers le fournisseur d'identite (IdP).
2. Code echange contre tokens **cote serveur** (jamais en front seul).
3. Validation : `iss`, `aud`, expiration, signature JWKS.

## Pieges a eviter

- Implicit flow en SPA sans PKCE.
- Stocker access_token en localStorage.
- Ne pas valider le `state` anti-CSRF.

> **Piege** - Un redirect_uri mal configure ouvre la porte au vol de code.

## A retenir

- Authorization code + PKCE pour les apps modernes.
- Valider tous les claims du id_token.
