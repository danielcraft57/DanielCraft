# Headers de securite

Headers HTTP qui durcissent le navigateur :

| Header | Role |
|--------|------|
| `Strict-Transport-Security` | Force HTTPS |
| `X-Content-Type-Options: nosniff` | Empeche MIME sniffing |
| `X-Frame-Options: DENY` | Anti clickjacking |
| `Referrer-Policy` | Limite les fuites d'URL |
| `Permissions-Policy` | Desactive camera/micro |

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
```

> **Astuce DanielCraft** - Teste tes headers sur securityheaders.com.

## A retenir

- Quelques headers bien choisis = gros impact.
- HSTS + X-Frame + nosniff = minimum.
