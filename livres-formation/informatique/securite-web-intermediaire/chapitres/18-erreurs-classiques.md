# Erreurs classiques

1. **JWT en localStorage** -> vole par XSS.
2. **CORS wildcard + credentials** -> fuite de session.
3. **CSP absente** -> XSS non bloque.
4. **Rate limit absent** -> brute force login.
5. **Secrets dans Git** -> fuite permanente.
6. **Debug mode en prod** -> fuite d'infos.

> **Piege** - La securite n'est pas "faite une fois". Revoie a chaque feature.
