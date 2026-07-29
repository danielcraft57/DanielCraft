# Bonnes pratiques intermediaire

- **Threat modeling** leger : quoi proteger, qui attaque, comment.
- **Defense in depth** : plusieurs couches (validation + prepared + CSP + headers).
- **Principe du moindre privilege** : DB, fichiers, API keys.
- **Revue de code** orientee securite.
- **Dependances** : `npm audit`, Dependabot, mises a jour.

## A retenir

- Plusieurs couches > une seule mesure.
- Automatiser les verifications (audit, headers check).
