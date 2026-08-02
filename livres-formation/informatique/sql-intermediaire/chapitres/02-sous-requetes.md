# Chapitre 2 - Sous-requetes

Une **sous-requete** est une requete rangee dans une autre. Souvent dans `WHERE`, parfois dans `FROM` ou `SELECT`. Chez DanielCraft : ecrire d'abord la question interieure, tester, puis l'emboiter. Lea filtre les `client_id` actifs, puis joint. Max colle tout d'un coup et se perd.

```sql
SELECT prenom
FROM clients
WHERE id IN (
  SELECT client_id
  FROM commandes
  WHERE montant > 100
);
```

:::retenir
Sous-requete = question dans la question. Teste le dedans d'abord.
:::

## Petite histoire

Sam demande "clients avec au moins une commande > 100". Lea ecrit le SELECT interieur, voit 12 id, puis `IN`. Max veut tout en un JOIN : parfois equivalent, parfois plus clair en sous-requete.

## Erreur classique

Sous-requete qui renvoie plusieurs colonnes la ou `IN` attend une. Ou correlee lourde sans besoin.

## A toi

Ecris une sous-requete : ids des commandes d'un client donne, puis les details.

:::attention
Une sous-requete fausse empoisonne toute la requete mere.
:::

:::astuce
Alias clairs : `c` clients, `cmd` commandes.
:::
