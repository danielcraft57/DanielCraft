# Rotation des secrets et gestion des cles

Un secret qui ne tourne jamais reste une bombe a retardement.

## Strategie

- **Rotation automatique** (90 jours max pour cles API).
- **Vault** (HashiCorp, AWS Secrets Manager) avec audit trail.
- Separation : cle dev != staging != prod.

## En cas de fuite

1. Revoquer immediatement.
2. Generer nouvelle cle.
3. Deployer sans downtime (double cle temporaire).
4. Analyser les logs d'usage de l'ancienne cle.

```bash
# Jamais en clair dans l'historique shell
export API_KEY=$(vault read -field=key secret/prod/api)
```

## A retenir

- Rotation = routine, pas urgence seule.
- Vault centralise et journalise.
