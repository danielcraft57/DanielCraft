# Threat modeling (modelisation des menaces)

Avant de coder, tu identifies **qui** attaque, **quoi** proteger, **comment** entrer.

## Methode STRIDE (rappel defense)

| Lettre | Menace | Contre-mesure |
|--------|--------|---------------|
| S | Spoofing | Auth forte |
| T | Tampering | Integrite, signatures |
| R | Repudiation | Logs signes |
| I | Information disclosure | Chiffrement, ACL |
| D | Denial of service | Rate limit, CDN |
| E | Elevation of privilege | Moindre privilege |

## Diagramme de flux

1. Dessiner les acteurs (utilisateur, API, BDD, tiers).
2. Lister les donnees sensibles en transit.
3. Pour chaque fleche : quelle attaque ? quelle defense ?

> **Astuce DanielCraft** - 30 minutes de threat model avant un sprint evitent des semaines de correctifs.

## A retenir

- Threat model = carte des risques avant le code.
- STRIDE aide a ne rien oublier.
