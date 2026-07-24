# Quiz final

Pas de piege. Relis une fois si besoin. L'idee : verifier que tu peux avancer en equipe sans paniquer.

## Questions

1. Dans un flux feature vers main, que fait-on en general juste avant de creer une branche ?
- A) Supprimer le depot distant
- B) Se placer sur `main` et faire `git pull`
- C) Faire `git push --force` sur `main`

2. Une bonne raison de garder des branches feature courtes :
- A) Pour colorier GitHub
- B) Pour limiter les divergences avec `main` et les gros conflits
- C) Parce que Git interdit les branches longues

3. Le rebase, en une idee simple, c'est surtout :
- A) Effacer GitHub
- B) Rejouer tes commits sur une autre base pour un historique plus lineaire
- C) Remplacer `git status`

4. Sur une branche `main` partagee, que faut-il presque toujours eviter ?
- A) Les pull requests
- B) Les tags annotes
- C) Un rebase suivi d'un force push

5. Un message de commit utile raconte surtout :
- A) La liste des fichiers sans intention
- B) Le pourquoi (l'intention) du changement
- C) Le mot de passe de la base

6. Dans une description de PR utile, on trouve souvent :
- A) Uniquement "fix"
- B) But, changements, et comment tester
- C) La cle API en clair

7. Proteger `main` sert surtout a :
- A) Interdire Git localement
- B) Imposer un passage par PR (et souvent review / CI) avant d'integrer
- C) Ralentir Internet

8. Une CI legere sur les PR, c'est surtout pour :
- A) Remplacer toute review humaine
- B) Lancer automatiquement des verifs (tests, lint, build) et signaler rouge/vert
- C) Generer des logos

9. Un tag `v1.2.0` sert surtout a :
- A) Remplacer les branches
- B) Nommer de facon stable un commit (souvent une version livree)
- C) Effacer l'historique

10. `git cherry-pick` sert surtout a :
- A) Copier un commit precis sur une autre branche
- B) Supprimer GitHub
- C) Remplacer `.gitignore`

11. `git bisect` sert surtout a :
- A) Punir un collegue en public
- B) Trouver par recherches successives le commit qui a introduit un bug
- C) Merger automatiquement

12. La bonne hygiene pour une cle API :
- A) La commit dans `config.js` "temporairement"
- B) La mettre hors Git (ex: `.env` ignore) et fournir un `.env.example`
- C) L'ecrire dans le titre de la PR

## Corriges

1-B, 2-B, 3-B, 4-C, 5-B, 6-B, 7-B, 8-B, 9-B, 10-A, 11-B, 12-B.

Si tu as 9/12 ou plus : tu es pret pour de vraies collabos. Sinon, relis les chapitres lies (flux, rebase, revue, protection, CI, tags, cherry-pick, bisect, secrets), sans dramatiser.
