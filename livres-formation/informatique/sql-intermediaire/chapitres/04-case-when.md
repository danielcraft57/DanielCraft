# Chapitre 4 - CASE WHEN

`CASE WHEN` cree des branches dans le resultat : labels, paniers, statuts. Chez DanielCraft, c'est le "si" du SELECT. Lea marque `petit` / `gros` selon le montant. Max evite dix requetes separees.

```sql
SELECT id, montant,
  CASE
    WHEN montant >= 100 THEN 'gros'
    WHEN montant >= 50 THEN 'moyen'
    ELSE 'petit'
  END AS panier
FROM commandes;
```

:::retenir
CASE WHEN = etiquettes calculees dans le SELECT.
:::

## A toi

Etiquette les clients : 'actif' s'ils ont une commande (idee : sous-requete ou jointure + CASE).

:::astuce
Ordre des WHEN : du plus precis au plus large.
:::
