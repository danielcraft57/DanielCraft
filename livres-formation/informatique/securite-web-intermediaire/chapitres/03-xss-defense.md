# XSS : comprendre et freiner

**XSS** (Cross-Site Scripting) : un attaquant injecte du JavaScript dans une page vue par d'autres utilisateurs.

## Types

- **Reflected** : payload dans l'URL, execute une fois.
- **Stored** : payload stocke en base, execute pour tous.

## Defense

1. **Echapper** les sorties HTML (`&lt;`, `&gt;`, etc.).
2. **CSP** (Content Security Policy) pour bloquer scripts non autorises.
3. Ne jamais faire `innerHTML = userInput` sans sanitization.

```javascript
// Mauvais
element.innerHTML = commentaire;

// Mieux
element.textContent = commentaire;
```

## A retenir

- XSS = code injecte dans la page.
- Echapper + CSP + textContent.
