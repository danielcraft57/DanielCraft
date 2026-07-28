# Chapitre 1 - C'est quoi SQL ?

Tu as deja vu un tableau Excel, une liste de clients, un export de commandes. **SQL** (Structured Query Language) est le langage pour **poser des questions** a une base de donnees relationnelle : des tables rangees en lignes et colonnes. Tu ecris une **requete**. La base repond avec un resultat. Tu restes le pilote. Chez DanielCraft, on presente SQL comme un filtre clair - pas comme de la magie noire. Lea l'utilise pour verifier qui a commande quoi. Max a compris le jour ou il a filtre "Lyon" au lieu de scroller cent lignes. Sam dit a ses eleves : "SQL ne remplace pas ton jugement. Il execute ta question."

Le geste mental est simple. Une table `clients` ressemble a une grille : `id`, `nom`, `ville`. Une table `commandes` a `id`, `client_id`, `total`, `cree_le`. Tu demandes : "montre-moi les clients de Lyon". La base lit, filtre, renvoie. Ce livre suit le meme rythme que les autres formations DanielCraft : petit, clair, testable. On suppose que tu sais ouvrir un editeur et lire un resultat. Pas besoin d'etre DBA. Besoin de curiosite.

:::retenir
SQL = langage pour interroger (et parfois modifier) des tables. Tu poses une question claire. La base repond. Toi, tu verifies.
:::

## Ce que ce n'est pas

Ce n'est pas Excel avec des formules. Ce n'est pas Python. Ce n'est pas un ORM magique qui "sait" ce que tu veux. Ce n'est pas obligatoire de connaitre toutes les bases (PostgreSQL, MySQL, SQLite) avant la premiere requete : la syntaxe de base se ressemble beaucoup. Ce n'est pas non plus "tout memoriser avant SELECT". Commence par lire. Ensuite ecrire.

Ce n'est pas non plus "big data" ni "data science" des le jour un. Lea rappelle : le vrai travail, c'est formuler une question honnete. Les mots-cles aident a ne pas se tromper de grille.

## Ce que tu vas savoir faire

A la fin de ce livre, tu sauras lire avec `SELECT`, filtrer avec `WHERE`, trier et limiter, comprendre `NULL`, agreger avec `COUNT`/`SUM`/`GROUP BY`, joindre avec `INNER JOIN` et `LEFT JOIN`, inserer et mettre a jour avec prudence, supprimer sans catastrophe, comprendre cles primaires et etrangeres, et livrer un mini rapport clients/commandes. Niveau debutant solide. Pas d'administration serveur avancee. Juste du SQL clair.

## Comment lire ce livre

Lis dans l'ordre au debut. Les premiers chapitres posent le sol : idee, SELECT, WHERE, ORDER, NULL, agregats, jointures. Le milieu touche ecriture et structure. Les ateliers font faire. Le quiz verifie. A chaque fin, un "A toi". Fais-le. Cinq minutes actives battent une lecture passive.

Chez DanielCraft, on forme des gens qui livrent petit, souvent, proprement - pas des collectionneurs de screenshots de dashboards jamais reconstruits. Tu ecris. Tu lances. Tu lis le resultat. Tu corriges.

## Petite histoire

Lea livrait un mini site pour un artisan. Le client demandait "qui a commande cette semaine ?". Sans SQL, elle ouvrait trois exports CSV et croisait a la main. Avec une table `commandes` et un `WHERE`, elle a repondu en deux minutes. Quarante lignes de panique en moins. Max voulait juste "voir les cinq plus gros totaux". Sam a montre `ORDER BY total DESC LIMIT 5`. L'idee est rentree sans jargon. Personne n'a dit "c'est trop". Ils ont dit "ah, c'est une question".

## Erreur classique

Croire que SQL "devine" ce que tu veux. Ou vouloir tout le manuel avant d'ecrire un `SELECT nom FROM clients`. Autre piege : confondre la base (le stockage) et l'outil (l'interface ou tu tapes). Lea garde une regle : une question claire bat dix dashboards flous. DanielCraft insiste : petit, clair, testable.

:::attention
SQL execute exactement ce que tu ecris. Une mauvaise question donne un mauvais resultat - meme si la syntaxe est correcte.
:::

## En vrai

Imagine trois tables : `clients`, `commandes`, `produits`. Ecris sur papier une question metier en francais ("clients de Lyon", "commandes > 100", "nom du client + total"). Tu transformeras ces phrases en requetes dans les chapitres suivants.

## A toi

Ecris en trois phrases : (1) une question que tu aimerais poser a des donnees, (2) ce que tu acceptes d'apprendre d'abord (SELECT, WHERE...), (3) ce que tu ne feras pas encore (admin serveur, optimisation avancee). Garde ce papier pour le mini-projet. Chez DanielCraft, ce petit brief vaut plus qu'une heure de videos floues.

## Exemple pour sentir

```sql
SELECT nom, ville
FROM clients
WHERE ville = 'Lyon';
```

Tu n'as pas besoin de tout comprendre maintenant. L'idee : tu choisis des colonnes, une table, un filtre. Dans ce livre, on demonte ca piece par piece, avec Lea, Max et Sam - et DanielCraft comme fil : petit, clair, testable.
