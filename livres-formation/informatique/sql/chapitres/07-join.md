# Chapitre 7 - INNER JOIN : croiser deux tables

Une table seule ne raconte pas tout. `clients` a les noms. `commandes` a les totaux et un `client_id`. Pour afficher **nom + total**, tu **joins** sur la cle commune. `INNER JOIN` garde seulement les lignes ou le match existe des deux cotes. Chez DanielCraft, c'est le geste "relier sans magie". Lea joint pour facturer. Max voyait des ids ; Sam lui a montre le nom via JOIN. L'oeil a change.

```sql
SELECT clients.nom, commandes.total, commandes.cree_le
FROM clients
INNER JOIN commandes ON clients.id = commandes.client_id;
```

`ON` dit comment ca matche. Ici : l'id client egal a la cle etrangere de la commande.

:::retenir
INNER JOIN = intersection utile. Seulement les lignes qui matchent des deux cotes.
:::

## Alias de tables

Pour alleger :

```sql
SELECT c.nom, co.total
FROM clients AS c
INNER JOIN commandes AS co ON c.id = co.client_id
WHERE co.total >= 50
ORDER BY co.total DESC;
```

Tu prefixes les colonnes (`c.nom`) pour eviter l'ambiguite si les deux tables ont `id`.

## Pourquoi INNER "perd" des lignes

Un client sans commande n'apparait pas en INNER JOIN. Une commande orpheline (client_id inconnu) non plus. Ce n'est pas forcement un bug : c'est la definition. Si tu veux garder les clients sans commande, tu passeras au LEFT JOIN (chapitre suivant).

## Petite histoire

Sam a dessine deux cercles au tableau : clients et commandes. L'intersection = INNER. Lea a livre un export "qui a commande" sans les curieux inactifs. Max a oublié le `ON` et a cree un produit cartesien monstrueux (chaque client avec chaque commande). La base a ralenti. Lecon : jamais de JOIN sans condition claire.

:::attention
Un JOIN sans bon `ON` (ou avec une mauvaise cle) multiplie les lignes. Verifie avec COUNT avant/apres.
:::

## Erreur classique

Joindre sur les mauvais champs (`clients.nom = commandes.total`). Oublier le prefixe et avoir `id` ambigu. Filtrer apres coup sans comprendre pourquoi des clients manquent (INNER).

## En vrai

Compte `SELECT COUNT(*) FROM commandes`. Puis compte le INNER JOIN clients/commandes. Si les nombres divergent fort, inspecte les `client_id` orphelins.

:::astuce
Ecris d'abord la phrase : "chaque commande appartient a un client via client_id". Puis traduis en ON.
:::

## A toi

Ecris un INNER JOIN `clients` + `commandes` affichant nom, total, date. Ajoute WHERE total >= 50. Limite a 10. Chez DanielCraft, une jointure lue a voix haute ("sur client_id") evite le flou.
