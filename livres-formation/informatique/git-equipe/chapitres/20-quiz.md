# Chapitre 20 - Quiz final

Pas de piege. Relis une fois si besoin. Le but : verifier que tu peux avancer en equipe sans paniquer. Chez DanielCraft, le vrai test, c'est la prochaine **PR** calme, pas le 12/12. Douze questions, les themes du livre : **flux**, branches, rebase, historique, revue, protection, CI, tags, cherry-pick, bisect, **secrets**. Si tu bloques, note le numero et relis le chapitre. Pas de honte. Un miroir.

Lea note ses erreurs et rouvre deux chapitres. Max refait l'atelier flux. Sam utilise ce QCM en fin de module. Toi, tu coches sans tricher. Une premiere passe honnete vaut mieux qu'un score maquille. Le but, c'est la carte des chapitres a rouvrir. Fais le quiz, note ton score, rejoue dans une semaine. Le vrai progres se voit a la deuxieme passe.

:::retenir
Le quiz est un miroir, pas un jugement. Note le frein, relis le chapitre, agis quinze minutes.
:::

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

## Reponses

1-B, 2-B, 3-B, 4-C, 5-B, 6-B, 7-B, 8-B, 9-B, 10-A, 11-B, 12-B.

Si tu as rate la 1 ou la 2 : chapitre 2 et 3. Rate la 3 ou la 4 : chapitre 4. Rate la 5 : chapitre 5. Rate la 6 : chapitre 6 et atelier revue. Rate la 7 : chapitre 7. Rate la 8 : chapitre 8. Rate la 9 : chapitre 9. Rate la 10 : chapitre 10. Rate la 11 : chapitre 11. Rate la 12 : chapitre 18, sans detour. Une erreur pointe un chapitre, pas une faute de caractere.

## Score

- 11-12 : pret pour de vraies collabos. Tiens le contrat leger cette semaine.
- 9-10 : tres bien, relis le chapitre qui a coince, puis une micro-PR de test.
- 7-8 : relis flux, revue, protection, secrets. Refais l'atelier flux si besoin.
- 5-6 : refais ateliers flux et conflit. Pas de honte : les mains ancrent.
- moins de 5 : reprends chapitres 1 a 7 sans stress. Le quiz attendra.

## Petite histoire

Lea a eu 8/12. Elle a relu le rebase, puis tenu une PR propre. Max a rate les secrets : il a verifie son `.gitignore` le soir meme. Sam a eu 11/12 et a quand meme protege `main` sur son depot de test. Le quiz est un miroir. Chez DanielCraft, on aime ces miroirs sans humiliation.

Lea a aussi note : "j'ai coche trop vite sur cherry-pick". Elle a relance `git show` sur un depot de jouet. Cinq minutes. Le geste est revenu. Max a rate la CI : il a ecrit la phrase README avant meme d'avoir un workflow. L'intention d'abord. Sam a montre le quiz a un stagiaire : douze questions, zero piege, une carte claire.

## Erreur classique

Tricher pour "avoir 12". Ou lire les reponses avant. Ou noter le score sans action. Autre piege : croire que 12/12 remplace une PR calme la semaine suivante. Le quiz mesure le souvenir. La collabo mesure le geste.

:::attention
Un 12/12 sans depot de test et sans PR recente, c'est un score papier. Ancre par un geste de quinze minutes.
:::

## En vrai

Note ton score et le chapitre a relire. Fais une action de quinze minutes liee (ouvrir une PR de test, ajouter `.env.example`, ecrire la regle d'equipe, proteger `main`). Le geste ancre mieux qu'une relecture passive. Si tu as 12/12, choisis quand meme une pratique a renforcer : personne n'est "fini".

## A toi

Ecris : score / frein principal / prochaine pratique a tenir cette semaine. Colle sous l'ecran. Dans sept jours, rejoue seulement les questions ratees. Puis coche : une PR avec description, ou `main` protegee, ou secrets verifies. Le quiz devient un plan, pas un trophee.
