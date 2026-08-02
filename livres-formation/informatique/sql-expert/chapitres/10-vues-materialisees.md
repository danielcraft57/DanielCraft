# Vues materialisees

Une **vue** calcule a la volee. Une **vue materialisee** stocke le resultat (a rafraichir).

## Quand

- Rapports lourds lus souvent.
- Agregats stables (refresh nocturne OK).

```sql
-- Idee (syntaxe selon moteur)
REFRESH MATERIALIZED VIEW rapport_mensuel;
```

## Contrepartie

- Donnees potentiellement **stale**.
- Espace disque + cout de refresh.

## A retenir

- Materialise = cache SQL versionne.
- Documente la fraicheur attendue.
