# Transactions et niveaux d'isolement

Une **transaction** = tout ou rien (BEGIN / COMMIT / ROLLBACK).

## Niveaux (idee)

| Niveau | Idee |
|--------|------|
| READ COMMITTED | Voir seulement les commits (souvent defaut) |
| REPEATABLE READ | Snapshot plus stable |
| SERIALIZABLE | Plus strict, plus de conflits possibles |

## Verrous

- Deux ventes sur le meme stock : attention race condition.
- `SELECT ... FOR UPDATE` pour verrouiller une ligne avant update.

> **Piege** - Transaction longue = verrous longs = apps qui attendent.

## A retenir

- Isolation = compromis coherence / concurrency.
- Court et clair > long et flou.
