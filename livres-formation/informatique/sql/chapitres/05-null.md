# Chapitre 5 - NULL : la valeur absente

`NULL` veut dire **inconnu** ou **absent**. Ce n'est pas `0`. Ce n'est pas `''` (texte vide). Ce n'est pas `"NULL"` en texte. Chez DanielCraft, on traite NULL comme un trou dans la grille. Lea a perdu une heure a chercher `email = NULL`. Max a cru qu'un total NULL etait zero. Sam ecrit au tableau : "NULL ne se compare pas avec =".

Pour tester :

```sql
SELECT nom, email
FROM clients
WHERE email IS NULL;
```

```sql
SELECT nom, email
FROM clients
WHERE email IS NOT NULL;
```

`= NULL` ne fait pas ce que tu crois (le resultat n'est pas "les lignes nulles" de facon fiable). Utilise `IS NULL` / `IS NOT NULL`.

:::retenir
NULL = absent. Teste avec IS NULL / IS NOT NULL, pas avec =.
:::

## NULL dans les calculs et filtres

Une comparaison avec NULL donne souvent "inconnu", donc la ligne sort du WHERE classique. Un `total + 10` si `total` est NULL peut rester NULL. Les agregats (chapitre suivant) ont des regles : `COUNT(colonne)` ignore les NULL, `COUNT(*)` compte les lignes.

Exemple : clients sans ville renseignee :

```sql
SELECT id, nom
FROM clients
WHERE ville IS NULL;
```

## Petite histoire

Lea exportait des clients "avec email". Son `WHERE email <> ''` laissait passer des NULL selon le moteur / les donnees. Elle a passe a `WHERE email IS NOT NULL AND email <> ''`. Max avait des commandes sans `client_id` (donnees sales) : `IS NULL` les a revelees. Sam fait l'exercice "trois boites : 0, '', NULL" a chaque promo. Personne ne confond apres.

## Erreur classique

Ecrire `WHERE col = NULL`. Remplacer NULL par 0 sans reflechir (parfois OK metier, souvent mensonge). Croire que LEFT JOIN "casse" parce que des colonnes droites sont NULL - c'est normal (chapitre 8).

:::attention
Avant de remplacer NULL par une valeur par defaut, demande : "absent" et "zero" veulent-ils dire la meme chose metier ?
:::

## En vrai

Inspecte une table : cherche une colonne qui peut etre vide. Compte avec `IS NULL` et avec `= ''` si c'est du texte. Compare les comptes.

:::astuce
Quand un JOIN "perd" des lignes ou en "invente" des NULL, dessine la grille : NULL a droite = pas de match, pas forcement bug.
:::

## A toi

Ecris : (1) lignes ou une colonne est NULL, (2) lignes ou elle ne l'est pas, (3) une phrase metier expliquant ce que NULL signifie chez toi (email manquant, commande non livree...). Chez DanielCraft, nommer le trou evite de le remplir n'importe comment.
