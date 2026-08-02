# Bonnes pratiques SQL expert

1. **Francais d'abord** : ecrire l'intention, puis le SQL.
2. **CTE** pour les etapes.
3. **EXPLAIN** avant / apres changement.
4. **Contraintes** en base, pas seulement en app.
5. **Tests** : petit jeu de donnees + cas limites (NULL, doublons).
6. **Revue** : une deuxieme paire d'yeux sur les requetes critiques.

## Checklist prod

- [ ] Index alignes sur EXPLAIN
- [ ] Pas de SELECT * en hot path
- [ ] Timeouts / limites de lignes
- [ ] Migrations reversible quand possible

## A retenir

- Discipline > genie ponctuel.
