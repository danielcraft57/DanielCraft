# Chapitre 3 - IN et EXISTS

`IN` teste si une valeur est dans une liste / resultat. `EXISTS` teste s'il existe au moins une ligne. Chez DanielCraft, on lit l'intention : appartenance vs existence. Lea prefere `EXISTS` quand elle verifie "a deja commande". Max utilise `IN` pour une petite liste d'ids.

```sql
SELECT prenom FROM clients c
WHERE EXISTS (
  SELECT 1 FROM commandes cmd
  WHERE cmd.client_id = c.id
);
```

:::retenir
IN = dans la liste. EXISTS = il existe au moins une ligne.
:::

## A toi

Reecris une question "clients sans commande" avec `NOT EXISTS`.

:::attention
`NOT IN` avec des NULL dans la sous-liste peut surprendre. Prefere `NOT EXISTS` si tu hesites.
:::

:::astuce
`SELECT 1` dans EXISTS suffit : on teste l'existence, pas les colonnes.
:::
