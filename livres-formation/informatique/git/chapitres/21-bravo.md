# Bravo.

Tu as fini les bases de Git et GitHub.

Pas "je connais toutes les options cachees".
Mais "je sais versionner, brancher, fusionner, pousser, et me sortir d'un conflit". C'est le coeur du metier.

## Ce que tu sais faire

Tu sais installer et configurer Git. Tu utilises `add`, `commit`, `log` et `status`. Tu geres branches, merge et conflits. Tu ecris un `.gitignore`. Tu manipules remote, clone, push et pull. Tu te debrouilles avec stash et les annulations raisonnables. Et tu fais des pull requests.

## Mission finale

Sur un vrai mini projet (meme un site de 2 pages), cree un depot GitHub. Travaille sur une branche feature. Merge via une PR. Ecris un README clair. Verifie qu'aucun secret n'est dans l'historique.

## La suite (quand tu voudras)

Tu pourras regarder les hooks / pre-commit, le rebase interactif (avec prudence), les monorepos, GitHub Actions (CI), et des conventions d'equipe plus fines.

Mais la, respire.

Encore bravo.
Ton code a maintenant une memoire. Et toi aussi.

## Rituel des 2 minutes

Avant chaque session :

```bash
git status
git pull
```

Apres chaque morceau utile :

```bash
git status
git add .
git commit -m "..."
git push
```

Regarde toujours `status` avant `add .`.
Les habitudes battent la memoire.
