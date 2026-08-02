# OWASP Top 10 (vue defense)

L'**OWASP Top 10** liste les risques web les plus frequents. Tu n'as pas besoin de tout memoriser : retiens les grandes familles.

| Rang | Risque | Contre-mesure cle |
|------|--------|-------------------|
| 1 | Controle d'acces casse | Verifier les droits a chaque action |
| 2 | Failles cryptographiques | HTTPS, algo modernes, pas de secrets en clair |
| 3 | Injection | Requetes preparees, validation |
| 4 | Design insecure | Menacer modeler, moindre privilege |
| 5 | Mauvaise config | Desactiver debug en prod, headers |

> **Astuce DanielCraft** - Utilise la Top 10 comme checklist avant mise en production.

## A retenir

- Top 10 = carte des priorites.
- Chaque chapitre suivant couvre une famille.
