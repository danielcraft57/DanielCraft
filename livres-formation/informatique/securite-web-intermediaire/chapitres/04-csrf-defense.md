# CSRF : proteger les actions

**CSRF** : un site malveillant declenche une action sur un autre site ou tu es deja connecte (ex. changer ton email).

## Defense

1. **Token CSRF** : jeton secret dans le formulaire, verifie cote serveur.
2. **SameSite cookies** : `SameSite=Strict` ou `Lax`.
3. Verifier l'**Origin** / **Referer** pour les requetes sensibles.

```html
<input type="hidden" name="csrf_token" value="abc123...">
```

> **Piege** - Les API REST sans token CSRF sont vulnerables si elles utilisent des cookies de session.

## A retenir

- CSRF = action forcee depuis un autre site.
- Token + SameSite + verification Origin.
