# Chapitre 14 - Ce qu'il faut retenir (bases)

Si tu ne devais garder qu'une page avant stash, undo et pull requests, ce serait celle-ci. Tu as parcouru la **boucle quotidienne**, les commandes vitales, les **zones** de Git, les habitudes qui tiennent, et les erreurs classiques que tout le monde fait au moins une fois. Chez DanielCraft, on veut une carte mentale actionnable, pas un glossaire de cinquante termes a reciter. Lis cette page comme un plan de metro : tu sais ou tu es, tu sais quelle ligne prendre. Si tu bloques plus loin, tu reviens ici dix minutes.

Lea resume en une phrase : "status, add, commit, push ; pull souvent si collab". Max resume : "photos locales, copie distante, branches pour oser". Sam resume : "lis status, ne commit aucun secret, explique tes commits". Trois phrases, un meme livre. Si tu peux dire la tienne sans notes, tu es pret pour la suite. Sinon, ce n'est pas un echec. C'est un signal de pratique. Rouvre les chapitres 4, 6 et 11. Cinq minutes chacun. Puis reessaie.

:::retenir
Status d'abord, secret jamais, branche pour oser. Cette phrase resume mieux le livre qu'une liste de vingt commandes.
:::

## Ce que ce n'est pas

Ce recap, ce n'est pas "tu as fini Git". Ce n'est pas non plus une liste a memoriser comme un poeme. Ce n'est pas un examen piege. C'est une carte. Tu t'orientes. Tu avances. Tu reviens si besoin. Ce n'est surtout pas une excuse pour sauter les ateliers : la carte ne remplace pas le terrain. Lea relit cette page avant un nouveau projet client. Max la recite le lundi matin. Sam la fait ecrire sans notes en fin de module.

## Boucle quotidienne

Le geste qui revient chaque jour ressemble a ca : tu ouvres le projet, tu fais `git status` pour voir ou tu en es, tu prepares avec `add`, tu photographies avec `commit`, tu envoies avec `push` si tu travailles avec un remote. Si tu collabores, tu `pull` souvent pour ne pas diverger trop longtemps. Ce n'est pas glamour. C'est fiable. Lea le fait avant le cafe. Max le fait avant de fermer la journee. Sam le fait en demo devant la classe. Chez DanielCraft, l'habitude bat le talent du soir ou tu "feras gaffe".

## Commandes vitales

Tu demarres avec `git init` (nouveau projet) ou `git clone` (copie d'un depot existant). Tu regardes l'etat avec `git status` - ton tableau de bord. Tu prepares avec `git add`, puis tu photographies avec `git commit`. Pour l'histoire : `git log --oneline`. Pour les pistes paralleles : `git switch` et `git branch`, puis `git merge` quand tu es pret a fusionner. Avec le distant : `git pull` pour recevoir, `git push` pour envoyer, et `git remote -v` pour verifier que tu parles au bon depot. Tu n'as pas besoin de tout savoir par coeur le jour un. Tu as besoin de savoir ou chercher quand un message te parle. L'aide `git help` existe. Les chapitres aussi.

## Zones

Git organise ton travail en zones. Tu modifies des fichiers (working directory). Tu prepares ce que tu veux photographier avec `add` (index / staging). Tu figes avec `commit` (historique local). Tu copies loin avec `push` (remote). Si tu confonds deux zones, **`status`** te le dit en clair : untracked, staged, modified. Apprends a le lire comme un tableau de bord, pas comme une insulte. Sam dit a ses eleves : "status avant, status apres". Ca evite la moitie des paniques. Lea le fait sans y penser. Max a mis une semaine a en faire un reflexe. Toi aussi, tu y arriveras.

## Habitudes

Fais `status` avant et apres chaque action importante. Ecris des messages clairs, pas "update". Mets un `.gitignore` tot, des le premier commit si possible. Prefere les petites branches pour une idee, une feature, un fix. Ne commit jamais un secret : `.env`, cles API, mots de passe. Merge souvent pour eviter les grosses divergences. Pull avant de pousser en equipe. Chez DanielCraft, ces habitudes battent les "astuces avancees" regardees sur YouTube trop tot.

:::astuce
Imprime mentalement l'aide-memoire express. Lea l'a colle sur un post-it une semaine. Ensuite, c'etait dans les doigts.
:::

## Erreurs classiques (recap)

On commit parfois sur la mauvaise branche - ca se repare si tu sais lire status. Un push peut etre refuse si le remote est en avance : pull d'abord, reparer, repush. Un **conflit** laisse des marqueurs `<<<<<<<` si tu oublies de nettoyer avant le commit de merge. Et `git add .` sans regarder, c'est le classique des secrets qui passent ou des fichiers temporaires qui polluent l'historique. Si tu les reconnais au premier regard, tu as gagne. Max les a tous faits une fois. Lea aussi. Sam les montre volontiers. Personne n'est "nul en Git". Certains n'ont pas encore assez pratique.

## Aide-memoire express

Pour l'etat : `git status`. Pour preparer : `git add`. Pour la photo : `git commit -m "..."`. Pour l'histoire : `git log --oneline`. Pour une branche : `git switch -c nom`. Pour fusionner : `git merge nom`. Pour envoyer : `git push`. Pour recevoir : `git pull`. Imprime cette page mentalement. Max la recite une fois le lundi matin. Lea n'en a plus besoin. Sam la redistribue chaque promo.

## Petite histoire

Lea a colle l'aide-memoire sur un post-it une semaine entiere. Ensuite, c'etait dans les doigts et le post-it est parti a la poubelle. Max a rate un push "rejected", a lu le chapitre pull, a corrige en dix minutes au lieu de paniquer une heure. Sam a fait ecrire sans notes la boucle add/commit/push et le role d'une branche en fin de module. Ceux qui y arrivaient passaient a stash et PR sans drame. Ceux qui bloquaient rouvraient les chapitres 4, 6 et 11 dix minutes, puis reessaient. Chez DanielCraft, c'est exactement le contrat : carte claire, pratique honnete, zero humiliation.

## Suite immediate

Deux chapitres un cran au-dessus t'attendent : stash + annuler proprement, puis les pull requests. Puis trois ateliers pour casser et reparer, un quiz, et un bravo. Tu n'es pas "fini". Tu es pret a monter d'un etage sans perdre le sol. C'est mieux que "fini". C'est solide.

## A toi

Sans notes : ecris la boucle add/commit/push et a quoi sert une branche. Si ca vient fluide, avance vers stash et PR. Sinon, rouvre les chapitres 4, 6 et 11 dix minutes chacun, puis reessaie. Ce recap ne remplace pas la pratique - il te dit ou repartir sans te disperser.
