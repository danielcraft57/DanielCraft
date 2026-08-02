# Partitionnement (idee)

**Partitionner** = decouper une grosse table en morceaux (par date, region...).

## Interet

- Scanner seulement la partition utile (prune).
- Archiver / detacher d'anciennes partitions.

## Exemple mental

`commandes` partitionnee par mois : `WHERE date >= '2026-01-01' AND date < '2026-02-01'` ne lit que janvier.

> **Astuce DanielCraft** - Partitionne quand la table est **vraiment** grosse, pas par snobisme.

## A retenir

- Partition = organisation physique, pas magie SQL.
- La cle de partition doit matcher tes filtres.
