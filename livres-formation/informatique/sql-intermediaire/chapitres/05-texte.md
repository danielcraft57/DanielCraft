# Chapitre 5 - Fonctions texte

`UPPER`, `LOWER`, `LENGTH`, `TRIM`, `CONCAT` (ou `||` selon moteur), `LIKE` avec `%`. Chez DanielCraft : nettoyer et comparer sans magie. Lea uniformise les villes en majuscules pour croiser. Max cherche `LIKE '%Paris%'`.

Les noms exacts dependent du moteur (SQLite, Postgres, MySQL). L'idee reste : transformer le texte pour filtrer ou afficher.

:::retenir
Fonctions texte = nettoyer, mesurer, concatener, chercher.
:::

## A toi

Ecris un filtre : prenoms qui commencent par 'A' (LIKE).

:::attention
LIKE sensible a la casse selon le moteur / collation.
:::
