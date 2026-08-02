# CTE recursive : hierarchies

Une CTE **recursive** se reference elle-meme : ideal pour arbres (categories, org chart).

```sql
WITH RECURSIVE arbre AS (
  SELECT id, parent_id, nom, 1 AS niveau
  FROM categories WHERE parent_id IS NULL
  UNION ALL
  SELECT c.id, c.parent_id, c.nom, a.niveau + 1
  FROM categories c
  JOIN arbre a ON c.parent_id = a.id
)
SELECT * FROM arbre;
```

## Garde-fous

- Toujours une ancre (partie non recursive).
- Limiter la profondeur si besoin.
- Eviter les cycles (ou les detecter).

## A retenir

- Recursive = ancre + UNION ALL + auto-jointure.
- Parfait pour hierarchie, pas pour tout.
