# Chapitre 2 - SELECT : lire des colonnes

Le premier geste SQL utile, c'est **lire**. Pas modifier. Pas supprimer. Lire. `SELECT` choisit **quelles colonnes** tu veux voir. `FROM` dit **dans quelle table**. Point. Chez DanielCraft, on commence toujours par regarder avant d'ecrire. Lea ouvre `clients` et demande seulement `nom` et `ville`. Max a voulu `*` des le debut ; Sam lui a dit : "vois d'abord ce que tu demandes vraiment".

La forme minimale :

```sql
SELECT nom, ville
FROM clients;
```

Tu obtiens une grille : une ligne par client, deux colonnes. Si tu ecris `SELECT * FROM clients;`, tu prends **toutes** les colonnes. Pratique pour explorer. Moins ideal pour un rapport propre : tu ramènes du bruit, et demain une colonne sensible peut apparaitre. Prefere nommer ce dont tu as besoin.

:::retenir
`SELECT colonnes FROM table` = choisir quoi lire, et ou. Commence par peu de colonnes.
:::

## Ce que ce n'est pas

Ce n'est pas encore un filtre (`WHERE` arrive au chapitre suivant). Ce n'est pas un tri. Ce n'est pas une jointure. Si tu ajoutes trop tot dix clauses, tu te perds. Lea coupe le superflu. Max a tendance a tout selectionner "au cas ou" ; Sam demande : "cette colonne sert-elle la question ?"

## Alias et lisibilite

Tu peux renommer une colonne dans le resultat avec `AS` :

```sql
SELECT nom AS client, ville AS ville_client
FROM clients;
```

Utile pour un export ou un ecran. La table ne change pas. Seul l'affichage du resultat change. Tu peux aussi selectionner une expression simple plus tard ; pour l'instant, colonnes reelles suffisent.

## Petite histoire

Lea devait preparer une liste "nom + ville" pour un mailing local. Elle a evite `SELECT *` et a pris exactement deux colonnes. Le fichier etait leger. Max a copie un `SELECT *` trouve en ligne et s'est retrouve avec dix colonnes dont un email interne. Sam a fait l'exercice a voix haute : "je choisis, je nomme, je lis". DanielCraft : le choix de colonnes est deja un acte de design.

## Erreur classique

Oublier `FROM` (la base ne sait pas ou chercher). Mal orthographier le nom de table (`client` au lieu de `clients`). Mettre une virgule en trop avant `FROM`. Autre piege : croire que `SELECT` modifie la table. Non : il lit une copie logique du resultat. La table reste intacte.

:::attention
`SELECT` ne change pas les donnees. Si tu veux modifier, ce sera `UPDATE` / `INSERT` / `DELETE` - plus tard, avec prudence.
:::

## En vrai

Dans ton outil SQL (SQLite, PostgreSQL, interface web...), execute :

```sql
SELECT id, nom, ville FROM clients;
```

Puis :

```sql
SELECT * FROM produits;
```

Compare le confort. Note ce que `*` t'apporte et ce qu'il cache.

:::astuce
Quand tu explores une table inconnue, un `SELECT * ... LIMIT 10` (chapitre 4) te montre la forme sans noyer l'ecran.
:::

## A toi

Ecris trois requetes `SELECT` sur `clients` ou `produits` : (1) une seule colonne, (2) deux colonnes nommees, (3) `*` puis une version avec colonnes explicites. Dis en une phrase laquelle tu garderais pour un rapport client. Chez DanielCraft, nommer les colonnes, c'est deja clarifier l'intention.
