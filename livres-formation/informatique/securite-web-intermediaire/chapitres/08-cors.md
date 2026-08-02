# CORS explique

**CORS** (Cross-Origin Resource Sharing) controle quels domaines peuvent appeler ton API depuis un navigateur.

## Scenario

`https://evil.com` veut appeler `https://api.tonsite.com` avec les cookies de l'utilisateur.

## Defense

```http
Access-Control-Allow-Origin: https://app.tonsite.com
Access-Control-Allow-Credentials: true
```

- **Ne jamais** mettre `Access-Control-Allow-Origin: *` avec credentials.
- Lister explicitement les origines autorisees.

> **Piege** - CORS est une protection navigateur, pas serveur. Les appels curl/postman contournent CORS.

## A retenir

- CORS = qui peut appeler ton API depuis le browser.
- Origines explicites, pas de wildcard avec cookies.
