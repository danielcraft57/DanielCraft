# Securite dans CI/CD

La pipeline est une porte d'entree : protege-la comme la prod.

## Pipeline durcie

- **SAST** (analyse statique) sur chaque PR.
- **DAST** periodique sur staging.
- Scan des **images Docker** (Trivy, Grype).
- Pas de secrets dans le Dockerfile ou les variables en clair.

```yaml
# Exemple etape CI
- run: npm audit --audit-level=high
- run: trivy image --exit-code 1 myapp:${{ github.sha }}
```

## Deploiement

- Environnements isoles (dev/staging/prod).
- Approbation manuelle pour prod.
- Rollback automatise teste.

## A retenir

- CI/CD compromis = prod compromise.
- Scans automatiques non negociables.
