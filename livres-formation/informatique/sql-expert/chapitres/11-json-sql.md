# JSON dans SQL (idee)

Beaucoup de moteurs stockent du **JSON** dans une colonne.

## Usages

- Attributs flexibles (metadata produit).
- Eviter une explosion de colonnes rares.

## Prudence

- Filtrer / indexer du JSON = plus complexe que des colonnes normales.
- Preferer colonnes classiques pour les champs **toujours** utilises.

```sql
-- Idee PostgreSQL
SELECT payload->>'ville' AS ville
FROM evenements;
```

## A retenir

- JSON = flexibilite, pas remplacement du modele relationnel.
