# Chapitre 6 - Dates et periodes

Filtrer "ce mois", "cette annee", "entre deux dates". Chez DanielCraft, on stocke des dates propres et on filtre avec des bornes. Lea coupe `date_cmd >= '2026-07-01' AND date_cmd < '2026-08-01'`. Max utilise des fonctions (`DATE_TRUNC`, `strftime`...) selon le moteur - l'idee compte plus que le dialecte.

```sql
SELECT * FROM commandes
WHERE date_cmd >= '2026-07-01'
  AND date_cmd < '2026-08-01';
```

:::retenir
Periode claire = borne basse incluse, borne haute souvent exclue.
:::

## Petite histoire

Sam livre un CA "juillet". Sans bornes nettes, aout fuyait dedans. Lea impose l'intervalle demi-ouvert. Max arrete les `LIKE '2026-07%' ` sur des timestamps.

## A toi

Ecris le filtre pour le trimestre invente Q1 2026.

:::attention
Comparer date et texte mal formate = tris foireux.
:::

:::astuce
Documente le fuseau / la convention "jour calendaire" du projet.
:::
