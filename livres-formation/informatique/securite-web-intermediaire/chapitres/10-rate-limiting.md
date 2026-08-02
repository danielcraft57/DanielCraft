# Rate limiting et brute force

Le **rate limiting** limite le nombre de requetes par IP/utilisateur sur une fenetre de temps.

## Cas d'usage

- Login : 5 tentatives / 15 min.
- API publique : 100 req / min.
- Reset password : 3 / heure.

## Implementation

- Compteur en memoire (Redis ideal).
- Reponse `429 Too Many Requests`.
- Captcha apres N echecs.

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 900
```

## A retenir

- Rate limit = frein automatique.
- Protege login, API, actions sensibles.
