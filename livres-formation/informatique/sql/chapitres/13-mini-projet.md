# Chapitre 13 - Mini-projet : clients et commandes

Objectif : un petit jeu de tables inventees et des requetes qui repondent a de vraies questions. Chez DanielCraft, le mini-projet n'est pas un ERP. C'est : lire, filtrer, agreger, joindre.

## Schema invente

`clients(id, prenom, ville)`  
`commandes(id, client_id, montant, date_cmd)`

Donnees inventees : 5 clients, 8 commandes. Tu peux les ecrire sur papier si tu n'as pas encore de base.

## Questions a repondre

1. Liste des clients de Paris.
2. Top 3 des commandes les plus cheres.
3. Total des montants par ville (JOIN + GROUP BY).
4. Clients sans commande (LEFT JOIN + filtre NULL) - bonus.

Lea fait 1 et 2. Max bloque sur 3 puis croise. Sam verifie chaque resultat a la main sur 3 lignes.

## Petite histoire

Nora (du livre finance) demanderait le chiffre. Ici Max livre : "Paris = 420 EUR ce mois (donnees inventees)". Le SQL a servi le discours, pas l'inverse.

## Erreur classique

Ecrire la requete finale sans tester SELECT * LIMIT 5 avant. Ou oublier le lien `client_id`.

## En vrai

Ecris les quatre requetes sur papier, meme imparfaites.

## A toi

Une page "Mini-projet SQL - date" avec schema + 4 reponses.

:::retenir
Mini-projet = questions metier + requetes + verification manuelle.
:::

:::attention
Sans verifier 2-3 lignes a la main, tu peux "reussir" avec un JOIN faux.
:::

:::astuce
Commence toujours par SELECT et LIMIT avant d'agreger.
:::
