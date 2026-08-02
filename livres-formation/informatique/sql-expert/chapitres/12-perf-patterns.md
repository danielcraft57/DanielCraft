# Patterns de performance

## Checklist rapide

1. Selectionner **moins de colonnes** (`*` coute cher).
2. Filtrer **tot** (WHERE selectif).
3. Eviter N+1 applicatif (joindre ou batch).
4. Preférer `EXISTS` a `IN` avec sous-requete lourde selon cas.
5. Paginer avec cle stable (pas seulement `OFFSET` geant).

## Pagination

```sql
-- Idee : keyset
SELECT * FROM commandes
WHERE id > :dernier_id
ORDER BY id
LIMIT 50;
```

## A retenir

- Perf = moins de travail pour le moteur.
- Mesure avant d'optimiser.
