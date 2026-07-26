# Chapitre 17 - Fork et upstream : contribuer ailleurs

Jusqu'ici, tu etais "dans" le depot de l'equipe : tu avais le droit de pousser des branches. Sur un projet open source, ou le depot d'une autre equipe, tu n'as souvent pas ce droit. Le chemin classique : **fork**, clone, branche, PR vers le projet original. Ce n'est pas une autre religion Git. C'est le meme flux, avec une etape de copie sur ton compte. Chez DanielCraft, on contribue souvent comme ca a un outil ami : propre, petit, respectueux des regles du projet.

Tu n'as pas besoin de devenir mainteneur open source. Tu as besoin de comprendre trois boites : ton PC, ton fork, le depot original. Une fois le dessin clair, les boutons GitHub cessent d'etre magiques. Ce chapitre pose le vocabulaire et le geste, sans transformer le livre en encyclopedie.

:::retenir
Fork = ta copie. Upstream = l'original. Tu pousses sur ton fork, tu proposes une PR vers upstream.
:::

## Les mots

**Fork** : une copie du depot sur ton compte GitHub. Tu pousses sur ton fork librement. Ce n'est pas un "vol". C'est le modele prevu.

**Origin** : en general, apres clone de ton fork, `origin` pointe vers ton fork. C'est "chez toi" sur le serveur.

**Upstream** : le depot d'origine (celui de l'equipe ou du projet public). Tu le configures pour recuperer les nouveautes, pas pour y pousser directement - tu n'en as souvent pas le droit.

Pull request : tu demandes au projet original d'integrer ta branche (depuis ton fork vers upstream). Meme conversation qu'au chapitre 6. Autre cible.

## Scenario concret

Lea veut corriger une typo dans la doc d'un outil qu'elle utilise. Elle ne peut pas pousser sur le depot officiel. Elle fork. Elle clone son fork. Elle cree `fix/typo-readme`. Elle corrige. Elle pousse sur son fork. Elle ouvre une PR vers le depot officiel. Le mainteneur lit, commente, merge. Lea sync son `main` depuis upstream. Fin. Une typo, un geste propre, zero drame.

Max, lui, a voulu "reformater tout le projet" dans sa premiere PR open source. Refuse. Trop large. Sam a lu `CONTRIBUTING.md` avant. Accepte en deux jours. La difference n'etait pas le talent. C'etait le respect du cadre.

## Les commandes d'installation

Apres avoir fork sur GitHub et clone ton fork :

```bash
git remote -v
git remote add upstream https://github.com/ORG/PROJET.git
git fetch upstream
```

Remplace l'URL. Verifie :

```bash
git remote -v
```

Tu dois voir `origin` (ton fork) et `upstream` (l'original). Si tu ne vois qu'`origin`, tu n'as pas encore la fenetre sur le projet source. Ajoute upstream avant de coder longtemps : sinon tu construis sur une base qui a deja bouge.

## Rester a jour avec upstream

Avant une nouvelle contribution :

```bash
git switch main
git fetch upstream
git merge upstream/main
git push origin main
```

(adapte le nom de branche par defaut si le projet utilise autre chose)

Ainsi ton `main` local et celui de ton fork suivent le projet. Ta prochaine feature part d'une base saine. Un fork qui moisit six mois, puis une PR sur une base obsolete, egal conflits inutiles et mainteneur fatigue.

:::astuce
Avant chaque contribution : `git fetch upstream` puis merge (ou rebase) de `upstream/main` dans ton `main`. Sync d'abord, code ensuite.
:::

## Le flux de contribution

```bash
git switch main
git pull origin main
git switch -c fix/typo-readme
# ... corrections, commits ...
git push -u origin fix/typo-readme
```

Puis sur GitHub : Pull request de `ton-compte:fix/typo-readme` vers `ORG/PROJET:main`. Lis les commentaires des mainteneurs. Corrige. Sois patient. Une contribution refusee n'est pas une attaque personnelle : parfois le timing, parfois la direction du projet. Tu pousses sur ta branche de ton fork ; la PR se met a jour. Tu n'as pas besoin d'acces write sur upstream pour iterer.

Quand c'est merge, tu sync ton `main` depuis upstream (fetch + merge) pour rester aligne, et tu peux supprimer ta branche de feature sur ton fork. Meme hygiene qu'en equipe interne.

## Bonnes manieres

PR petite. Sujet unique. Message et description clairs. Respecter le style du projet. Ne pas reformater deux cents fichiers "en passant". Ne pas ouvrir dix PR de bruit le premier jour. Si le projet a un fichier `CONTRIBUTING.md`, lis-le. Ca evite quatre-vingts pour cent des malentendus. Licence, code de conduite, templates de PR : ce n'est pas de la paperasse. C'est le mode d'emploi pour etre entendu.

:::attention
Une premiere PR qui reformatte tout le depot "en passant" est souvent refusee. Un sujet, une intention, un diff lisible.
:::

## Et dans une entreprise ?

Parfois tu n'as pas de fork : tu as directement acces au depot, et le chapitre 2 suffit. Le fork sert surtout quand les droits d'ecriture sont limites, ou pour isoler des experiences. Comprendre fork/upstream reste utile des que tu touches l'open source - et parfois en interne, si l'org te met en lecture seule plus process PR.

Meme avec acces write, certains forkent pour tenter une idee folle sans polluer les branches de l'equipe. Moins courant en petite boite, courant en open source. L'idee reste : isolation plus proposition.

Dans une org GitHub, on t'ajoute parfois en write sur le depot : pas besoin de fork. On t'ajoute parfois seulement en lecture plus process fork/PR : besoin de fork. Demande quel modele est en place. Ne suppose pas. Lea a perdu une matinee a chercher un bouton "push" qui n'existait pas. Sam lui a dit : "tu es en lecture. Fork."

## Petite histoire

Lea a fork un outil, oublie `upstream`, code trois semaines, ouvert une PR. Le projet avait avance de quarante commits. Conflits partout. Elle a sync, recommence, PR minuscule. Accepte. Max a pousse vers `upstream` par erreur de remote : refuse par le serveur, ego un peu blesse, lecon nette. Chez DanielCraft, on dessine les trois boites au tableau avant la premiere contribution externe. Dix minutes. Beaucoup de clarte.

## Erreur classique

Pousser vers `upstream` alors que tu n'as pas les droits (erreur) ou, pire, croire que `git push` sans remote precise ira "au bon endroit". Verifie avec `git remote -v`. Autre piege : laisser ton fork moisir six mois. Ou ouvrir une PR geante le premier jour pour "impressionner". Tu impressionnes surtout le bouton Close.

## En vrai

Fork un petit projet (meme un depot demo), ajoute `upstream`, synchronise `main`, ouvre une PR minuscule sur ton propre fork vers un second depot de test si besoin, pour voir les boutons GitHub. L'important est de voir origin vs upstream une fois dans l'interface. Le corps retient mieux que le schema seul.

## A toi

Dessine sur papier trois boites : ton PC, ton fork, le depot original. Fleches : fetch upstream, push origin, PR vers upstream. Si le dessin est clair, le modele est clair. Garde le papier. Tu le ressortiras la prochaine fois que quelqu'un dira "fork-moi ca".
