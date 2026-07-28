# Chapitre 6 - Agregats et GROUP BY

Parfois tu ne veux pas chaque ligne : tu veux un **resume**. Combien de clients ? Somme des totaux ? Moyenne ? Minimum / maximum ? Les fonctions d'agregat repondent. Chez DanielCraft, c'est le passage "liste" vers "chiffre utile". Lea compte les commandes par client. Max somme les totaux du mois. Sam dit : "agreger, c'est accepter de perdre le detail pour gagner la vue".

```sql
SELECT COUNT(*) AS nb
FROM clients;
```

```sql
SELECT SUM(total) AS ca, AVG(total) AS moyenne, MIN(total) AS mini, MAX(total) AS maxi
FROM commandes;
```

`COUNT(*)` compte les lignes. `COUNT(email)` compte les emails non NULL. Nuance utile apres le chapitre NULL.

:::retenir
COUNT SUM AVG MIN MAX resument. GROUP BY decoupe le resume par groupe.
:::

## GROUP BY

Pour un chiffre **par ville** ou **par client** :

```sql
SELECT ville, COUNT(*) AS nb_clients
FROM clients
GROUP BY ville
ORDER BY nb_clients DESC;
```

```sql
SELECT client_id, SUM(total) AS ca
FROM commandes
GROUP BY client_id
ORDER BY ca DESC;
```

Regle d'or debutant : dans le `SELECT`, chaque colonne non agregee doit etre dans le `GROUP BY` (selon le mode SQL strict). Ne melange pas `nom` libre et `SUM(total)` sans grouper correctement.

## HAVING (appercu)

`WHERE` filtre **avant** l'agregat. `HAVING` filtre **apres**, sur le resultat groupe :

```sql
SELECT client_id, SUM(total) AS ca
FROM commandes
GROUP BY client_id
HAVING SUM(total) >= 200;
```

Tu n'as pas besoin de tout maitriser maintenant. Retiens : WHERE sur lignes brutes, HAVING sur groupes.

## Petite histoire

Lea devait repondre "combien de clients par ville ?". Sans GROUP BY, elle comptait a la main. Avec, trois secondes. Max a mis `SELECT nom, SUM(total)` sans GROUP BY et a pris une erreur (ou un resultat incoherent selon le moteur). Sam a corrige au tableau. Message : le groupe doit etre explicite.

## Erreur classique

Oublier GROUP BY alors que tu agreges avec une colonne libre. Utiliser WHERE a la place de HAVING pour filtrer sur `SUM(...)`. Croire que COUNT(*) et COUNT(col) sont toujours egaux.

:::attention
Agreger sans definir le groupe, c'est melanger des pommes et des paniers. Ecris d'abord "par quoi je regroupe ?".
:::

## En vrai

Compte les commandes. Somme les totaux. Puis somme par `client_id`. Compare une ligne globale et plusieurs lignes groupees.

:::astuce
Pour verifier un GROUP BY, relance sans agregat avec WHERE sur un groupe (un client_id) et compare a la main.
:::

## A toi

Ecris : (1) `COUNT(*)` sur `produits`, (2) `SUM(total)` global sur `commandes`, (3) `SUM(total)` par `client_id` avec ORDER BY. Note le client en tete. Chez DanielCraft, un chiffre verifie bat un dashboard joli non compris.
