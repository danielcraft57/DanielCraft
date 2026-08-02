# Qualite des requetes

## Style expert

- Alias courts mais lisibles (`c`, `cmd`).
- CTE nommees metier (`actifs`, `ca_mois`).
- Commentaires **pourquoi**, pas **quoi**.

## Anti-patterns

- Sous-requetes correlees partout sans besoin.
- `DISTINCT` pour masquer un mauvais JOIN.
- Logique metier cachee dans 15 CASE imbriques.

> **Astuce DanielCraft** - Si tu ne peux pas expliquer la requete a voix haute en 30 s, simplifie.

## A retenir

- Lisible aujourd'hui = maintenable demain.
