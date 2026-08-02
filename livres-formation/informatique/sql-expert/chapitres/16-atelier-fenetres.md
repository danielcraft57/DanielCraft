# Atelier : fenetres

**Duree** : 25 minutes.

## Mission

Sur `commandes` :

1. Rang de chaque commande par `montant` **par client**.
2. Cumul des montants dans le temps par client (`SUM() OVER ... ORDER BY date`).
3. Ecart avec la commande precedente (`LAG`).

## Criteres

- Une seule requete avec plusieurs colonnes fenetre OK.
- Verifier sur 1 client a la main.

## A retenir

- PARTITION BY = groupe ; ORDER BY = ordre dans le groupe.
