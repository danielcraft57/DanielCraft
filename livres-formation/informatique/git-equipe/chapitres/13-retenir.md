# Chapitre 13 - A retenir

Tu n'as pas besoin de tout memoriser par coeur. Tu as besoin d'une carte mentale stable. Voici la version poche du livre, a relire avant une journee d'equipe. Chez DanielCraft, Git en equipe, ce n'est pas "connaitre plus de commandes". C'est "se synchroniser sans se blesser". Les commandes servent ce but. Si tu peux dire ca a voix haute, tu as la colonne vertebrale.

Imagine un tableau blanc au milieu de la piece. `main` distant, c'est le tableau officiel. Lea, Max et Sam ont chacun une copie. Sans **flux**, chacun dessine et s'ecrase. Avec flux : tire le tableau, dessine sur ton coin (**branche**), propose (**PR**), regarde, colle, nettoie. Petit et frequent bat grand et rare. Relis cette image avant chaque session confuse. Elle vaut mieux qu'un catalogue de sous-commandes.

:::retenir
Se synchroniser sans se blesser. Tout le reste du livre sert cette phrase.
:::

## Le flux et les branches

Tire `main` en debut de session. Cree une branche pour une intention. Commit. Pousse la branche. Ouvre une PR. Fais reviewer. Merge. Retire `main`. Recommence. `main` = reference. Feature/fix = travail. Noms clairs. Duree courte. Une intention par branche. Nettoie apres merge. GitHub Flow leger suffit a 2-5 personnes. Lea tient des features courtes. Max aussi. Sam coupe les branches zombies. Si une branche vit trop longtemps, elle devient un conflit annonce.

Le rituel du matin tient en trois commandes et une intention. `git switch main`, `git pull`, puis une branche nommee pour la tache du jour. Le soir, si la feature avance, pousse. Si elle est prete, ouvre la PR avec but et comment tester. Apres merge, tire `main` et efface la branche morte. Ce cycle, repete, bat n'importe quelle usine a process copiee d'une grosse boite.

## Rebase, merge, historique

**Merge** joint les histoires. **Rebase** rejoue tes commits sur une base plus recente. Utile sur une feature perso. Dangereux sur l'histoire partagee si tu force-push sans soin. Pas de dogme : une politique d'equipe ecrite. Messages qui disent le pourquoi. Petits commits coherents. Squash possible a l'integration. Amend seulement en local / branche perso. Pas de secrets dans Git. Chez DanielCraft, on ecrit la politique en dix lignes dans le README. Pas dans un wiki perdu.

Si tu te demandes "merge ou rebase ?", pose d'abord : "cette branche est-elle partagee ?" Si oui, merge est souvent plus doux. Si non, rebase sur `main` avant la PR peut clarifier le log. Dans les deux cas, un conflit demande un choix humain. `git rebase --abort` ou `git merge --abort` existent pour respirer.

## Revue, protection, CI

Bienveillante, utile, rapide. Description claire cote auteur. Regard priorise cote reviewer. Dire aussi ce qui est bien. Pas d'Approve fantome. Pas de tribunal. `main` protegee : pas de push direct, PR, review. CI legere : tests sur la PR, feu vert avant merge. Filet technique + filet humain. L'un sans l'autre laisse un trou. Lea aime le filet humain. Max aime le filet technique. Sam exige les deux.

Trois phrases a coller sous l'ecran : "On review pour aider.", "On ne merge pas au rouge.", "On ne pousse pas sur main." Si ton equipe ne retient que ca, elle a deja gagne une categorie de vendredis.

## Tags, cherry-pick, bisect, secrets

Nommer un commit livre : `vX.Y.Z`. Pousser le tag. Notes courtes. Aligner tag et deploiement. Cherry-pick : reprendre une cerise ailleurs, surtout en urgence. Bisect : trouver le commit qui a casse. Outils de precision, pas de panique. Fork + upstream pour contribuer a l'exterieur. Jamais de cles dans le depot. Les bonnes pratiques tiennent en quelques phrases ecrites. Relis-les avant de paniquer.

Quand la prod brule, resiste a deux reflexes : pousser direct sur `main`, et merger toute une feature longue. Prefere une branche `fix/` courte, une PR express, un cherry-pick si la cerise est isolee. Quand tu cherches un bug dans vingt commits, tente bisect avant une heure de lecture au hasard. Quand une cle fuit, invalide d'abord, nettoie ensuite.

:::astuce
Si tu te perds, reviens au chapitre 2 (flux) et au chapitre 6 (revue). Presque tous les frottements viennent de la.
:::

## Petite histoire

Lea a voulu tout retenir d'un coup. Elle a bloque. Elle a affiche cette carte au-dessus de l'ecran. Max a saute la revue "parce que c'etait petit" : prod cassee un vendredi. Sam a force-push sur une branche partagee : deux heures de reparage. Trois lecons, une carte. Si tu te perds, reviens au chapitre 2 (flux) et au chapitre 6 (revue). Presque tous les frottements viennent de la.

Chez DanielCraft, on dit souvent : la carte poche vaut mieux que la memoire heroique. Relis. Agis. Ajuste. Avant une journee confuse, dix minutes sur cette page battent une heure de recherche au hasard.

## Erreur classique

Croire que "je connais Git" = "je sais collaborer". Les bases sont le moteur. L'equipe, c'est le code de la route. Autre piege : empiler les outils (hooks, bots, templates) avant d'avoir un flux tenu a trois personnes. Autre piege : relire ce recap sans ouvrir le depot. La carte sans volant, ca ne conduit pas.

:::attention
Empiler bots et hooks avant un flux tenu, c'est decorer une maison sans fondations. Pose le flux d'abord.
:::

## En vrai

Sans regarder le livre, ecris sur papier les 8 etapes du flux (pull main ... pull main). Chronometre cinq minutes. Si tu bloques, relis le chapitre 2. Si tu y arrives, tu as la colonne vertebrale. Puis ouvre ton vrai depot et regarde si ta derniere PR suit encore cette carte. Note un ecart. Corrige-le cette semaine, pas "un jour".

## A toi

Ecris en cinq lignes le contrat d'equipe que tu veux : branches, PR, revue, `main`, secrets. Montre-le a un collegue. Ajustez. Collez-le dans le README. Une page tenue bat un discours inspire. Bonus : ajoute une ligne "comment on gere l'urgence" (hotfix via PR courte, pas push direct). Relis ce chapitre avant le quiz : c'est la carte, pas un examen.
