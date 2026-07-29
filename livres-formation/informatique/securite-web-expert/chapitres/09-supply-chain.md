# Supply chain : dependances et CI

Ton code depend de milliers de paquets. Une dependance compromise = ta prod compromise.

## Actions

- **Lockfile** (`package-lock.json`, `poetry.lock`) versionne.
- **`npm audit` / `pip-audit` / Dependabot** en CI.
- **SBOM** (Software Bill of Materials) pour la tracabilite.
- Verifier signatures et checksums des releases.

## CI securise

- Secrets dans le vault CI, pas dans les logs.
- Branches protegees, revue obligatoire.
- Build reproductible, images signees.

## A retenir

- Supply chain = partie de ta surface d'attaque.
- Audit automatique a chaque merge.
