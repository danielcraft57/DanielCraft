# Index : strategie avancee

Un index accelere certaines lectures, ralentit un peu les ecritures.

## Types d'idees

- Index sur colonnes de **WHERE** / **JOIN** frequents.
- Index **composite** : ordre des colonnes compte (`(a, b)` aide `WHERE a = ?` puis `a = ? AND b = ?`).
- Index **couvrant** : toutes les colonnes lues sont dans l'index (moins de retours table).

## Anti-patterns

- Indexer toutes les colonnes.
- Index inutilises (maintenance inutile).
- Fonctions sur colonnes indexees (`WHERE LOWER(email) = ...`) qui empechent l'usage.

## A retenir

- Index = outil cible, pas decoration.
- Verifie avec EXPLAIN apres creation.
