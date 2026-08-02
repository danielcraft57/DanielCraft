# Chapitre 5 - Lire l'historique

L'interet de Git, c'est de pouvoir regarder en arriere sans paniquer. Un album sans lecture, c'est une boite fermee. Avec **`log`**, **`diff`** et **`show`**, tu ouvres la boite. Tu vois qui, quand, quoi. Tu compares avant de commit. Tu comprends **`HEAD`**. Tu jettes une modif locale avec prudence. Chez DanielCraft, "lire l'historique" est une competence egale a "ecrire un commit". Sans lecture, tu photographies a l'aveugle. Avec lecture, tu pilotes.

Lea lit `diff` avant chaque commit important. Cinq secondes qui evitent une mauvaise photo. Max a decouvert `log --oneline` et a sourit : "ca ressemble a une todo". Sam fait lire un `log` a voix haute en classe : si personne ne comprend les messages, le probleme n'est pas Git, c'est la legende des photos. Toi, tu vas apprendre a ouvrir l'album avant de le modifier.

`HEAD` = ou tu es maintenant. `HEAD~1` = le commit d'avant. `log` = la liste des photos. `diff` = le detail entre deux etats. `show` = le zoom sur une photo. `restore` = "annule mes griffonnages non photographies sur ce fichier" - attention, tu perds ces griffonnages. Avant de restaurer, demande-toi si tu as vraiment besoin de jeter. Si tu hesites, copie le fichier ailleurs.

:::retenir
`git diff` = changements non stages. `git diff --staged` = ce qui attend le commit. Deux commandes, deux questions differentes.
:::

## Ce que ce n'est pas

Lire l'historique, ce n'est pas reecrire le passe (rebase interactif, etc.). Ce n'est pas non plus "revenir en arriere" a chaque commande : `log` regarde, `restore` peut jeter des modifs non commit. Ce n'est pas obligatoire de tout comprendre des options graphiques avancees. Et ce n'est surtout pas une perte de temps : cinq secondes de `diff` evitent un mauvais commit.

Ce n'est pas "Git qui modifie quelque chose" quand tu lances `log`. `log` lit. Il n'ecrit pas. Si tu as peur de "casser" en lisant, respire. Lire est toujours sur. Ecrire (reset, restore, amend) demande plus d'attention. On separe les deux familles dans la tete.

:::astuce
Avant chaque commit important, lance `git diff`. Lea le fait depuis des mois : cinq secondes qui evitent une mauvaise photo.
:::

## log et diff

```bash
git log
```

Tu vois hash, auteur, date, message. Quitte avec `q` si c'est une vue longue.

```bash
git log --oneline
```

Une ligne par commit. Ideal au debut. C'est la vue que tu vas ouvrir le plus souvent.

```bash
git log --oneline -- readme.txt
```

Voir un fichier a travers le temps. Utile quand tu te demandes "qui a casse ce CSS ?" ou "quand cette phrase a change ?".

Avant de commit :

```bash
git diff
```

Ca montre les modifications non stagees. Les `+` et les `-` deviennent vite familiers.

Entre staging et dernier commit :

```bash
git diff --staged
```

Entre deux commits :

```bash
git diff HEAD~1 HEAD
```

```bash
git show HEAD
```

Detail du dernier commit. Hash, message, diff inclus. Sam adore `show` pour expliquer "voila exactement ce que cette photo contient".

## Checkout / restore d'un fichier (apercu)

Pour jeter les modifs non commit d'un fichier :

```bash
git restore readme.txt
```

(Anciennement `git checkout -- readme.txt`.) Attention : tu perds les changements non sauves dans un commit. Lea le dit a voix haute avant d'appuyer sur Entree. Max copie parfois le fichier ailleurs s'il doute. Sam interdit `restore` en atelier tant que l'eleve n'a pas dit "je jette volontairement". Bon filtre. Chez DanielCraft, on separe clairement "lire" (`log`, `diff`, `show`) et "jeter" (`restore`) : le premier est toujours sur, le second demande une phrase orale avant Entree.

## Petite histoire

Max a fait un petit changement, lance `git diff`, vu le `+` et le `-`, compris mieux qu'avec un discours. Sam a demande trois commits avec des messages tres clairs, puis a fait lire le `log --oneline` a un camarade : "est-ce comprehensible ?". Lea a ouvert `git log --oneline --graph --all` une fois et a vu la forme de l'histoire. Chez DanielCraft, on veut que tu voies la forme, pas seulement les commandes. La forme rassure. La forme prepare le chapitre suivant.

## Erreur classique

Confondre `diff` et `diff --staged`. Croire que `log` "modifie" quelque chose. Utiliser `restore` comme une baguette sans lire. Autre piege : messages de commit flous qui rendent `log` inutile - tu as l'outil, mais pas l'info. Encore un piege : lancer `diff` apres un `add` et s'etonner que "rien n'apparait" - regarde `diff --staged`. Deux tiroirs. Deux commandes.

## En vrai

Ouvre `git log --oneline --graph --all` une fois. Meme sur un petit projet, tu vois la forme de l'histoire. Puis fais un petit changement, `git diff`, `add`, `commit`, `log --oneline`. Sens la boucle complete : ecrire, voir, preparer, photographier, relire. Si tu hesites entre `diff` et `diff --staged`, pose la question a voix haute : "ai-je deja fait `add` ?" Oui -> staged. Non -> working tree. Chez DanielCraft, cette boucle lit-ecrit vaut mieux qu'une heure de video sans ouvrir le terminal.

## A toi

Cree 3 commits avec des messages tres clairs. Demande a quelqu'un (ou a toi demain matin) de lire ton `log --oneline` : est-ce comprehensible ? Si non, reecris ta facon de titrer les prochaines photos. Note aussi la difference entre `diff` et `diff --staged` en une phrase dans `notes.md`.
