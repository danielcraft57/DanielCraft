# Chapitre 5 - Historique propre : messages, petits commits, squash

L'historique Git, c'est le journal de bord du projet. Dans six mois, Lea ouvrira `git log` pour comprendre pourquoi le formulaire valide l'email d'une certaine facon. Si elle lit "fix", "wip", "asdf", "final", elle perdra du temps. Si elle lit des messages clairs et des commits digeres, elle avancera. Un **historique** propre n'est pas de la vanite. C'est de la gentillesse envers le futur, toi y compris. Chez DanielCraft, on prefere un ton simple, factuel, sans emoji obligatoire, sans roman policier.

Un bon **message** dit surtout l'intention. "Corrige le timeout du login" bat "modif fichier". "Ajoute la section tarifs sur la page offres" bat "update". Tu n'as pas besoin d'un roman. Une ligne claire suffit souvent. Si le changement est subtil, une deuxieme ligne apres une ligne vide aide :

```text
Corrige la validation email du formulaire contact

Le champ acceptait les adresses sans point dans le domaine.
```

Un commit egal une intention coherente. Tu peux avoir plusieurs commits dans une PR, tant que chaque commit raconte une etape logique : structure HTML, puis styles, puis texte. Evite le commit unique de quatre-vingts fichiers "toute la feature" si tu peux decouper sans souffrir. Inversement, evite quarante commits "typo", "typo2", "aaa", "wip" laisses tels quels sur `main`. Avant la merge, tu peux nettoyer (**squash**, ou rebase interactif si tu maitrises).

:::retenir
Le message repond au pourquoi. Les fichiers, Git les montre deja dans le diff.
:::

## L'idee du squash

Squash egal compresser plusieurs commits en un (ou en peu). Sur GitHub, l'option "Squash and merge" prend tous les commits de la PR et les integre dans `main` comme un seul commit. Pratique pour garder `main` lisible quand la feature a vecu avec des allers-retours. Ce n'est pas obligatoire. Certaines equipes aiment garder tous les commits de la PR. D'autres squashent toujours. Choisissez. L'important est que `main` reste navigable.

Tu viens de commit et tu as oublie un fichier, ou une typo dans le message. Si tu n'as pas encore pousse (ou si tu es seul sur la branche et d'accord pour reecrire) :

```bash
git add fichier-oublie.css
git commit --amend --no-edit
```

N'amends pas un commit deja sur `main` partage. N'amends pas le travail d'un autre. **Amend** egal micro-rewrite. Puissant, local, dangereux si mal place. Un historique "propre" commence aussi par ne pas y coller des secrets. Les mots de passe, les cles API, les dumps de base (chapitre 18). Une fois pousse, un secret est difficile a vraiment effacer.

:::attention
`commit --amend` sur un commit deja publie et partage, c'est reecrire l'histoire des autres. Reserve-le a ta branche perso non partagee, ou annonce et utilise `--force-with-lease`.
:::

Avant d'ouvrir la PR, regarde :

```bash
git log main..HEAD --oneline
git diff main...HEAD
```

Est-ce que la liste des commits raconte une histoire ? Est-ce qu'il y a un fichier de debug a retirer ? Un `console.log` oublie ? Un commentaire "TODO enlever" qui devait partir ? Cinq minutes ici epargnent vingt minutes de review grevee. Tu verras parfois `feat:`, `fix:`, `docs:` (conventional commits). Utile si l'equipe s'en sert pour des changelogs automatiques. Pas obligatoire. Mieux vaut un message clair sans prefixe qu'un prefixe vide de sens.

Lea lit le log a voix haute avant d'ouvrir la PR. Si elle sourit nerveusement, elle reecrit. Max prefere des commits deja propres. Sam squash via GitHub au merge. Trois styles, une meme exigence : `main` lisible.

## Petite histoire

Lea a six commits sur sa feature tarifs : "wip", "wip2", "styles", "fix typo", "ok", "ok final". Avant d'ouvrir la PR, elle regarde le log et se dit que Sam va souffrir. Elle decide de squash via le bouton GitHub au merge, et elle reecrit le message final : "Ajoute la section tarifs sur la page offres". `main` reste lisible. Sa branche feature peut garder ses allers-retours : ce n'est qu'un brouillon. Max, lui, prefere des commits deja propres avant la PR. Les deux approches marchent si l'equipe est d'accord sur ce que doit ressembler `main`.

Chez DanielCraft, on dit souvent : le brouillon peut etre sale ; la page officielle, non.

## Erreur classique

Honte du "mauvais historique" au point de ne plus oser commit. Commit souvent en local sur ta feature. Nettoie avant d'integrer si besoin. L'inverse aussi : pousser un journal de bord illegible sur `main` parce que "on verra plus tard". Plus tard, c'est Lea un mardi a 18h. Sur ta branche perso non partagee, "wip" en local le temps d'un cafe, pourquoi pas. Avant la review, nettoie ou squash. Laisser "wip" sur `main` apres merge, c'est offrir une enigme a toute l'equipe.

:::astuce
Avant la PR : `git log main..HEAD --oneline` puis `git diff main...HEAD`. Cinq minutes de lecture epargnent vingt minutes de review.
:::

## En vrai

Prends une ancienne PR (ou un vieux `git log`). Note trois messages obscurs. Reecris-les comme tu aurais voulu les lire. Cet exercice calibre ton prochain commit. Imagine que tu ne connais pas le projet. Est-ce que le message plus le diff racontent une histoire ? Si tu dois expliquer oralement pendant cinq minutes, le message est trop maigre.

## A toi

Pour ta prochaine branche, impose-toi cette regle : chaque message repond a "pourquoi ce changement existe". Pas "quels fichiers". Le pourquoi. Puis ouvre le log et lis-le a voix haute. Si tu souris nerveusement, recommence le message.
