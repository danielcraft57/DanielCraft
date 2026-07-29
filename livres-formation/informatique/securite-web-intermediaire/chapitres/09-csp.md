# Content Security Policy (CSP)

La **CSP** dit au navigateur quelles sources de scripts, styles, images sont autorisees.

```http
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'
```

## Effet

- Bloque les scripts inline injectes (XSS).
- Empeche le chargement de JS depuis des domaines non listes.

## Demarrage progressif

1. Mode **report-only** : `Content-Security-Policy-Report-Only`.
2. Analyser les violations.
3. Passer en mode enforce.

## A retenir

- CSP = bouclier anti-XSS puissant.
- Commencer en report-only.
