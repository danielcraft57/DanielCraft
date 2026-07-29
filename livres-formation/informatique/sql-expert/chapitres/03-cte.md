# CTE : WITH pour clarifier

Une **CTE** (Common Table Expression) nomme un resultat intermediaire avec `WITH`.

```sql
WITH gros AS (
  SELECT client_id, SUM(montant) AS ca
  FROM commandes
  GROUP BY client_id
  HAVING SUM(montant) > 1000
)
SELECT c.prenom, g.ca
FROM gros g
JOIN clients c ON c.id = g.client_id;
```

## Pourquoi s'en servir

- Lire la requete comme des etapes.
- Reutiliser le meme bloc plusieurs fois.
- Preparer une recursive (chapitre suivant).

> **Piege** - Une CTE n'est pas toujours "materialisee" : le moteur peut l'inliner. Teste avec EXPLAIN.

## A retenir

- WITH = briques nommees, plus claires qu'une sous-requete geante.
