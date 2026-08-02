# Chapitre 3 - WHERE : filtrer les lignes

Sans filtre, tu lis trop. `WHERE` garde **seulement les lignes** qui respectent une condition. Tu as choisi les colonnes avec `SELECT`. Tu cibles maintenant les lignes utiles. Chez DanielCraft, le filtre est le superpouvoir debutant. Lea filtre `ville = 'Lyon'`. Max filtre `total > 100`. Sam dit : "si ta question metier a un 'seulement', tu as besoin de WHERE".

```sql
SELECT nom, ville
FROM clients
WHERE ville = 'Lyon';
```

Comparaisons courantes : `=`, `<>` ou `!=`, `<`, `>`, `<=`, `>=`. Texte entre quotes simples `'Lyon'`. Nombres sans quotes : `total >= 50`.

:::retenir
`WHERE` filtre les lignes. Sans lui, tu ramènes souvent trop de bruit.
:::

## Combiner : AND et OR

Plusieurs conditions :

```sql
SELECT id, client_id, total
FROM commandes
WHERE total >= 50 AND total < 200;
```

`AND` : les deux doivent etre vraies. `OR` : au moins une. Utilise des parentheses quand tu melanges :

```sql
SELECT nom, ville
FROM clients
WHERE (ville = 'Lyon' OR ville = 'Paris') AND nom <> '';
```

Sans parentheses, la priorite peut te surprendre. Lea les met des qu'elle doute. Max a appris apres un resultat "trop large".

## IN et LIKE (leger)

```sql
SELECT nom, ville FROM clients WHERE ville IN ('Lyon', 'Paris', 'Nantes');
```

```sql
SELECT nom FROM clients WHERE nom LIKE 'A%';
```

`LIKE` avec `%` = "commence par / contient / finit par" selon la place du joker. Pratique. Pas magique : attention a la casse selon la base.

## Petite histoire

Max preparait "les commandes du jour utiles". Sans WHERE, il avait tout l'historique. Avec `WHERE cree_le = '2026-07-28'`, la liste tenait sur un ecran. Lea a ajoute `AND total > 0` pour ecarter les tests a zero. Sam a projete un OR mal parenthese : le resultat a explose. La classe a vu pourquoi la precision compte.

## Erreur classique

Ecrire `WHERE ville = Lyon` sans quotes (erreur ou colonne mal interpretee). Confondre `=` et `LIKE`. Filtrer sur une colonne qui n'existe pas. Autre piege : croire que WHERE trie - non, c'est `ORDER BY`.

:::attention
Une condition fausse sur toute la table renvoie zero ligne. Ce n'est pas forcement une erreur SQL : relis ta logique metier.
:::

## En vrai

Ecris en francais : "clients de Lyon ou Paris avec un nom non vide". Traduis en `WHERE` avec parentheses. Execute. Compte les lignes. Change un `OR` en `AND` et observe.

:::astuce
Quand le resultat est etrange, simplifie : une seule condition d'abord, puis rajoute AND/OR une par une.
:::

## A toi

Sur `commandes`, ecris : (1) totaux strictement > 100, (2) totaux entre 50 et 100 inclus, (3) `client_id` dans une petite liste `IN (...)`. Note combien de lignes chaque filtre garde. Chez DanielCraft, mesurer le filtre, c'est comprendre la question.
