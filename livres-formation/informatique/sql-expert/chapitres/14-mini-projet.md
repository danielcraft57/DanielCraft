# Mini-projet : tableau de bord SQL

**Objectif** : produire un mini dashboard clients / commandes "niveau expert".

## Livrables

1. CTE : CA par client sur 90 jours.
2. Fenetre : top 3 commandes par client (`ROW_NUMBER`).
3. EXPLAIN d'une requete lente, puis index propose.
4. Contrainte CHECK + FK documentees.

## Jeu de donnees

Tables `clients`, `commandes` (id, client_id, montant, date_cmd).

> **Astuce DanielCraft** - Verifie 3 chiffres a la main avant de presenter.

## A retenir

- Mini-projet = fenetres + CTE + mesure + integrite.
