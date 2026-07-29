# Ce qu'il faut retenir

| Risque | Defense |
|--------|---------|
| XSS | Echapper + CSP |
| CSRF | Token + SameSite |
| Injection SQL | Prepared statements |
| Auth faible | Hash + 2FA + rate limit |
| JWT mal utilise | HttpOnly + expiration courte |
| CORS ouvert | Origines explicites |
| Brute force | Rate limiting |
| Config | Headers securite |
| Fuites secrets | .env + vault |

> **Astuce DanielCraft** - OWASP Top 10 + checklist headers = base solide avant prod.
