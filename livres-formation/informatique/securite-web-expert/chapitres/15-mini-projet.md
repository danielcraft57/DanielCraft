# Mini-projet : architecture securisee

**Objectif** : concevoir (sur papier ou schema) une API SaaS multi-tenant avec checklist expert.

## Exigences

- Auth OIDC + scopes par tenant.
- Rate limit par tenant et endpoint.
- Upload avatars (images only, S3 prive).
- Logs sans PII, alertes echecs auth.
- CI : audit deps + scan image.

## Livrables

1. Diagramme threat model (STRIDE sur 3 flux).
2. Liste headers HTTP + CSP proposee.
3. Runbook incident (1 page).

> **Astuce DanielCraft** - Presente le schema a un collegue : s'il comprend les flux, c'est bon.

## A retenir

- Mini-projet = synthese architecture + processus.
- Documenter avant d'implementer.
