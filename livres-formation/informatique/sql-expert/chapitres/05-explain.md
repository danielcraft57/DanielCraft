# EXPLAIN : lire le plan

**EXPLAIN** montre comment le moteur execute ta requete (scan, index, jointure...).

```sql
EXPLAIN ANALYZE
SELECT * FROM commandes WHERE client_id = 42;
```

## Signaux a surveiller

- **Seq Scan** sur grosse table + filtre selectif → index manquant ?
- **Nested Loop** vs **Hash Join** : selon volumes.
- Cout estime vs temps reel (ANALYZE).

> **Astuce DanielCraft** - EXPLAIN avant d'ajouter un index "au feeling".

## A retenir

- Le plan > l'intuition.
- Mesure sur des volumes realistes.
