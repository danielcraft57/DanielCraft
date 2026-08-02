# SSRF : Server-Side Request Forgery

**SSRF** : l'attaquant force ton serveur a appeler une URL interne (metadata cloud, Redis local...).

## Vecteurs

- Webhook URL fournie par l'utilisateur.
- Import d'image depuis une URL.
- Preview PDF / fetch proxy.

## Defense

1. **Liste blanche** de domaines autorises.
2. Bloquer IP privees (`10.x`, `169.254.x`, `127.0.0.1`).
3. Pas de redirections automatiques non controlees.
4. Reseau sortant en DMZ sans acces metadata.

> **Astuce DanielCraft** - Sur AWS, bloquer `169.254.169.254` en sortie sauf besoin explicite.

## A retenir

- SSRF = ton serveur devient le proxy de l'attaquant.
- Whitelist + blocage reseau interne.
