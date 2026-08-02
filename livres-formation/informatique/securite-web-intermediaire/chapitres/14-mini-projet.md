# Mini-projet : durcir une petite API

## Objectif

Prendre une API CRUD simple et ajouter :

1. Requetes preparees (anti injection).
2. Rate limiting sur login.
3. Headers de securite (HSTS, X-Frame, nosniff).
4. CSP basique.
5. Validation des entrees.
6. Logging des echecs auth.

## Checklist

- [ ] Prepared statements partout
- [ ] Rate limit login (5/15min)
- [ ] Headers securite configures
- [ ] CSP en report-only
- [ ] Secrets en .env
- [ ] Logs sans mots de passe

> **Astuce DanielCraft** - Fais une passe avant/apres. Note chaque amelioration.

## A retenir

- Mini-projet = appliquer 6 contre-mesures concretes.
