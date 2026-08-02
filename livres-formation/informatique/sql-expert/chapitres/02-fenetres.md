# Fonctions fenetre en profondeur

Une **fenetre** calcule sur un groupe de lignes **sans les ecraser** (contrairement a GROUP BY).

```sql
SELECT client_id, montant,
  ROW_NUMBER() OVER (PARTITION BY client_id ORDER BY montant DESC) AS rang
FROM commandes;
```

## Familles utiles

| Fonction | Role |
|----------|------|
| ROW_NUMBER | Rang unique 1, 2, 3... |
| RANK / DENSE_RANK | Rangs avec egalites |
| SUM/AVG OVER | Totaux courants |
| LAG / LEAD | Ligne precedente / suivante |

## PARTITION BY + ORDER BY

- `PARTITION BY` = decouper les groupes.
- `ORDER BY` dans OVER = ordre **dans** la fenetre.

## A retenir

- Fenetre = detail conserve + calcul de voisinage.
- Commence par ROW_NUMBER avant les cas complexes.
