# Logging et detection

## Quoi logger

- Tentatives de login echouees.
- Acces admin.
- Erreurs 500.
- Modifications de donnees sensibles.

## Quoi NE PAS logger

- Mots de passe.
- Tokens complets.
- Donnees perso inutiles (RGPD).

## Alertes

- Pic de 401/403.
- Multiples echecs login meme IP.
- Requetes vers des paths suspects (`/admin`, `/.env`).

## A retenir

- Logger les evenements de securite, pas les secrets.
- Alerter sur les patterns anormaux.
