# Atelier : EXPLAIN + index

**Duree** : 20 minutes.

## Mission

1. Ecrire `SELECT * FROM commandes WHERE client_id = ? AND date_cmd >= ?`.
2. Lancer EXPLAIN (ANALYZE si dispo).
3. Proposer **un** index composite.
4. Relancer EXPLAIN et comparer.

## Questions

- Seq scan ou index scan ?
- Le filtre date est-il utilise efficacement ?

## A retenir

- Un index, une hypothese, une mesure.
