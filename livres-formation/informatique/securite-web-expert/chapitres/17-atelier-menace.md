# Atelier : threat model express

**Duree** : 25 minutes.

## Scenario

Application de prise de rendez-vous medicaux : patient, medecin, admin, API, BDD PostgreSQL, envoi SMS tiers.

## Etapes

1. Dessiner les 4 acteurs et 5 flux de donnees.
2. Appliquer STRIDE sur le flux « patient reserve un creneau ».
3. Lister 3 contre-mesures prioritaires.

## Correction type

- Spoofing patient -> auth MFA optionnelle.
- Tampering creneau -> validation serveur + verrou optimistic.
- Info disclosure -> chiffrement BDD + ACL par role.

## A retenir

- 25 min suffisent pour un premier threat model utile.
