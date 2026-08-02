# Chapitre 12 - Types de colonnes

Une colonne a un **type** : texte, nombre entier, decimal, date, booleen... Le type dit ce que tu peux comparer et calculer. Chez DanielCraft, on ne fait pas un catalogue exhaustif : on lit l'intention. `prix` en texte, c'est un piege. `prix` en nombre, tu peux sommer.

Lea stocke `ville` en texte. Max met `quantite` en entier. Sam range une date de commande en type date (ou texte ISO si l'outil est limite) et evite "hier" en clair dans la colonne.

## Ce que ce n'est pas

Ce n'est pas "tous les dialectes SQL sont identiques". MySQL, Postgres, SQLite ont des nuances. L'idee reste : choisis un type qui match l'usage.

## Petite histoire

Max compare `prix > '20'` alors que prix est texte. L'ordre lexicographique le trompe. Il passe en nombre. Lea sourit : le type a parle.

## Erreur classique

Mettre des montants en texte. Ou des dates en format francais meuble impossible a trier.

## En vrai

Liste trois colonnes de `clients` et propose un type pour chacune.

## A toi

Corrige une mauvaise idee : "telephone en nombre". Ecris pourquoi texte est souvent mieux.

:::retenir
Le type de colonne guide les comparaisons et les calculs.
:::

:::attention
Montant en texte = tris et sommes foireux.
:::

:::astuce
Pour debuter : texte, entier, decimal, date. Le reste viendra.
:::
