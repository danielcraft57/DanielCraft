# Chapitre 7 - HAVING

`WHERE` filtre les lignes **avant** regroupement. `HAVING` filtre les **groupes** apres `GROUP BY`. Chez DanielCraft, Lea dit : "d'abord les lignes, ensuite les paquets". Max voulait `WHERE COUNT(*) > 3` : refuse. `HAVING COUNT(*) > 3` : oui.

```sql
SELECT client_id, COUNT(*) AS nb
FROM commandes
GROUP BY client_id
HAVING COUNT(*) >= 3;
```

:::retenir
WHERE = lignes. HAVING = groupes.
:::

## A toi

Villes avec un total de montants > 500 (JOIN + GROUP BY + HAVING).

:::attention
Mettre un agregat dans WHERE est une erreur classique.
:::
