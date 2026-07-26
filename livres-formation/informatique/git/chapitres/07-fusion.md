# Chapitre 7 - Fusionner (merge)

Tu as travaille sur une branche. Tu veux ramener le travail dans `main`. Le **merge**, c'est le point de jonction. Git essaie de combiner les historiques. Parfois c'est simple (**fast-forward**). Parfois ca cree un commit de fusion. Parfois ca demande ton avis (conflit, chapitre suivant). Chez DanielCraft, on apprend `merge` avant `rebase` : un outil clair d'abord, les subtilites ensuite. Tu n'as pas besoin d'etre "clever". Tu as besoin d'etre fiable.

Lea fusionne localement pour apprendre, puis passe par des pull requests sur les vrais projets. Max dessine `main` et `feature` qui se rejoignent sur un papier. Sam fait merger deux branches avec chacune un fichier different : les deux fichiers doivent etre presents sur `main`. Preuve concrete. Toi, tu vas merger pour de vrai dans ton carnet de tests. Ensuite, le mot "fusion" ne fera plus peur. Ce sera un geste.

Merge souvent. Petits pas. Une branche qui dort trois semaines accumule les surprises au moment de fusionner. Deux routes : tu ramenes le chantier dans la route principale. Si la principale n'a pas bouge, Git peut juste avancer le pointeur : fast-forward. Si les deux ont avance, Git cree souvent un **commit de jonction**. Ensuite tu regardes `log --graph`. Puis tu peux supprimer la branche locale fusionnee.

:::retenir
Merge souvent, petits pas. Une branche qui dort trois semaines accumule les surprises au moment de fusionner.
:::

## Ce que ce n'est pas

Merger, ce n'est pas "ecraser main sans regarder". Ce n'est pas non plus obligatoire de passer par GitHub pour apprendre : en local / solo, `merge` suffit. Ce n'est pas un rebase. Et ce n'est surtout pas une operation magique qui comprend ton intention metier : Git combine des historiques de fichiers. Toi, tu verifies le resultat. Tu ouvres le site. Tu lances le script. Tu lis `status`. Puis seulement tu souris.

Ce n'est pas non plus "supprimer la branche avant de verifier". Tu merges. Tu regardes. Tu testes. Puis tu peux `branch -d`. L'ordre compte. Max a supprime trop vite une fois. Il a du recreer. Lea verifie toujours le rendu avant de nettoyer.

:::astuce
Dessine `main` et `feature` sur un papier avant ton premier merge. Max a fait ca : le graphe Git n'a plus paru magique apres.
:::

## Scenario de base

```bash
git switch main
git merge idee-couleurs
```

Si tout va bien, Git cree souvent un "merge commit" (ou avance juste le pointeur). Tu vois le resultat dans les fichiers + dans `log`.

Parfois Git ouvre un editeur. Tu peux aussi :

```bash
git merge idee-couleurs -m "Fusion idee couleurs"
```

Le message de merge peut rester simple. L'important : etre sur `main` (ou sur la branche cible) avant de lancer la commande. `status` te le rappelle si tu regardes. Souvent tu es sur `main`, et tu merges la feature dedans. Pas l'inverse, sauf intention claire.

## Apres le merge

```bash
git log --oneline --graph
git branch -d idee-couleurs
```

Tu peux supprimer la branche locale une fois fusionnee. Lea le fait apres verification visuelle du site. Max regarde d'abord que les fichiers attendus sont la. Sam fait lire le graphe a voix haute : "main a avance, la feature a rejoint". Quand les eleves le disent, c'est compris.

## Quand ne pas merger directement ?

Sur GitHub, on passe souvent par une pull request (chapitre 16) : relecture, discussion, CI. En local / solo, `merge` suffit pour apprendre. Les deux cohabitent dans une vraie vie pro. Lea merge en local pour apprendre, PR pour livrer. Max a commence en local uniquement. Sam montre les deux sans dogme. Chez DanielCraft, on veut que tu saches joindre des historiques avant de formaliser la collab.

## Merge vs rebase (apercu)

`merge` : garde l'historique tel quel, ajoute souvent un commit de jonction. `rebase` : rejoue tes commits "par-dessus" une autre branche. Historique plus lineaire, mais plus piegeux. Pour ce livre : maitrise `merge` d'abord. Le rebase, tu le croiseras plus tard (avec prudence, surtout sur branches partagees). Chez DanielCraft, on refuse le rebase "parce que c'est cool" avant de savoir reparer.

## Petite histoire

Lea a fusionne `ajout-note` dans `main`, vu le graphe, sourit. Sam a fait merger deux fichiers differents : aucune collision, deux ajouts heureux. Max a voulu "tout rebaser" apres une video YouTube : Sam a dit non, pas encore. Une semaine plus tard, Max etait content d'avoir un historique comprehensible plutot qu'un exploit fragile. Chez DanielCraft, on celebre le merge propre plus que le tour de force.

## Erreur classique

Merger sans etre sur `main` (ou sur la branche cible). Supprimer la branche avant de verifier. Confondre merge et push. Autre piege : attendre trois semaines avant de fusionner - plus de divergences, plus de conflits. Merge souvent. Petits pas. Encore un piege : croire que merge "envoie sur GitHub". Non. Merge joint des historiques locaux. Push envoie ensuite, si tu as un remote.

## En vrai

Fais un dessin : `main` et `feature` qui se rejoignent. Le merge, c'est le point de jonction. Puis fais l'exercice pour de vrai dans ton carnet de tests. Regarde `log --graph --oneline`. Sens la forme. C'est cette forme que tu reverras toute ta vie de projet versionne.

## A toi

Cree une branche `ajout-note`. Commit un fichier. Merge dans `main`. Regarde `log --graph --oneline`. Bonus : deux branches avec chacune un fichier different, merge les deux dans `main`, verifie que les deux fichiers sont presents. Note en une phrase ce qui s'est passe : fast-forward ou commit de jonction.
