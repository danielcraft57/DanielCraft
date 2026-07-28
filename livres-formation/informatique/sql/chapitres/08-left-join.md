# Chapitre 8 - LEFT JOIN : garder la gauche

`INNER JOIN` ne garde que les matchs. `LEFT JOIN` garde **toutes** les lignes de la table de **gauche**, meme sans match a droite. Les colonnes de droite deviennent `NULL` si pas de commande. Chez DanielCraft, c'est la requete "tous les clients, meme ceux qui n'ont rien commande". Lea l'utilise pour relancer les inactifs. Max cherchait un bug ; c'etait juste un LEFT avec des NULL. Sam dit : "gauche = priorite de visibilite".

```sql
SELECT c.nom, co.id AS commande_id, co.total
FROM clients AS c
LEFT JOIN commandes AS co ON c.id = co.client_id
ORDER BY c.nom;
```

Un client sans commande : une ligne avec `commande_id` et `total` a NULL.

:::retenir
LEFT JOIN = tous a gauche. Droite match ou NULL.
:::

## Trouver ceux sans match

Pattern classique :

```sql
SELECT c.nom
FROM clients AS c
LEFT JOIN commandes AS co ON c.id = co.client_id
WHERE co.id IS NULL;
```

Tu gardes la gauche, tu filtres ou la droite est absente. Ideal pour "clients sans commande".

## INNER vs LEFT : choisir

- Tu veux seulement les couples existants -> INNER.
- Tu veux inventorier la gauche complete -> LEFT.
Ne choisis pas LEFT "par peur" : trop de NULL brouille le rapport. Choisis selon la question metier.

## Petite histoire

Lea a envoye un mailing a "tous les clients" en INNER JOIN par erreur : les nouveaux sans commande etaient invisibles. Passage en LEFT : la liste etait complete. Max a panique en voyant des NULL ; Sam a sourit : "c'est le signal 'pas de commande', pas une corruption". DanielCraft : NULL ici est une information.

## Erreur classique

Mettre la table "importante" a droite et s'etonner qu'elle disparaisse (ce serait un autre type de jointure). Filtrer `WHERE co.total > 0` apres LEFT sans faire attention : tu retransformes souvent le LEFT en INNER (les NULL sortent). Pour filtrer la droite en gardant les sans-match, il faut parfois mettre la condition dans le `ON`, ou accepter le comportement.

:::attention
Un WHERE sur une colonne de droite peut annuler l'interet du LEFT JOIN. Relis le resultat.
:::

## En vrai

Compare le nombre de lignes : INNER vs LEFT sur clients/commandes. Liste les clients avec `WHERE co.id IS NULL`.

:::astuce
Dis a voix haute : "je veux tous les clients". Si oui, clients a gauche en LEFT JOIN.
:::

## A toi

Ecris (1) LEFT JOIN nom + total, (2) version "sans commande" avec IS NULL, (3) une phrase : quand tu choisirais INNER a la place. Chez DanielCraft, le choix de jointure, c'est le choix de la question.
