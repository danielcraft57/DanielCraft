# Chapitre 9 - .gitignore

Certains fichiers ne doivent jamais aller dans Git. Secrets, caches, gros binaires, dossiers de dependances, fichiers d'OS... Un **`.gitignore`** a la racine dit a Git : "ne propose meme pas d'ajouter ca". Ce n'est pas une liste magique universelle. C'est une **politique** claire pour ce projet. Chez DanielCraft, on le pose tot, avant le premier push public - surtout avant d'apprendre `push`. Un secret committe reste dans l'historique. Meme si tu le "supprimes" apres. Meme si tu rougis.

Lea a deja pousse un `.env` par accident. Elle a change le secret ensuite. Lecon chere. Max ignore `Thumbs.db` et ses PDF de brouillon. Sam fait creer un faux `.env` et verifier qu'il n'apparait plus dans `status`. Exercice simple, impact immense. Toi, tu vas ecrire ton premier `.gitignore` aujourd'hui, meme sur un carnet de tests. Habitude posee avant le danger reel.

Git propose des fichiers a photographier. `.gitignore` met des post-it "ne pas photographier" sur certaines etiquettes : `.env`, `node_modules/`, `__pycache__/`, `.venv/`. Tu adaptes la liste. Tu verifies avec `status`. Si un secret a deja ete photographie, tu l'enleves de l'album (**`rm --cached`**) sans forcement le supprimer de ton bureau. Puis tu tournes la page avec un commit. Si la photo est deja sur GitHub, tu changes la serrure (le secret), pas seulement l'album.

:::attention
`.gitignore` n'efface pas un fichier deja suivi. Si `.env` est deja dans l'historique, il faut `git rm --cached` + commit. Et changer le secret si c'etait un vrai.
:::

## Ce que ce n'est pas

`.gitignore`, ce n'est pas un antivirus. Ce n'est pas non plus "effacer le fichier de ton disque". Ce n'est pas retroactif si le fichier est deja suivi : il faut `git rm --cached` puis commit, et si le secret est deja en ligne, changer le secret. Et ce n'est surtout pas optionnel sur un projet qui touche des cles API, des mots de passe, des dumps. Ce n'est pas non plus "ignorer tout avec `*`" : tu ne versionnerais plus ton code. Sois precis.

Ce n'est pas non plus un fichier qu'on ecrit "plus tard, apres le push". Plus tard, le mal est fait. Ecris-le tot. Lea le cree souvent juste apres `init`. Max le cree avant le premier `add .`. Sam l'exige avant toute demo publique.

:::retenir
Avant le premier push public : relis `git status`. Cherche mots de passe, cles, dumps. Puis seulement, pousse.
:::

## Creer le fichier

A la racine du projet, cree `.gitignore` :

```text
# secrets
.env
*.key

# python
__pycache__/
.venv/

# node
node_modules/

# OS / editeur
.DS_Store
Thumbs.db
.idea/
.vscode/
```

Adapte a ton projet. Tu n'as pas besoin de tout. Tu as besoin de ce qui te concerne. Lea part d'un template GitHub, puis coupe ce qu'elle ne comprend pas. Mieux qu'une liste copiee aveugle. Max ajoute `*.pdf` sur ses carnets, sauf un manuel utile. Sam fait relire chaque ligne a voix haute en classe : "pourquoi ignore-t-on ca ?"

## Verifier et reparer

```bash
git status
```

Les fichiers ignores ne doivent plus apparaitre comme "a ajouter".

Si tu as deja `add` un fichier sensible :

```bash
git rm --cached fichier.env
```

Ca l'enleve de l'index, pas de ton disque. Puis commit. Et ajoute-le au `.gitignore`. Si le secret est deja sur GitHub : change le secret (mot de passe, cle). L'enlever de l'historique est un autre niveau. Pour ce livre, retiens : prevention d'abord, `rm --cached` ensuite, rotation du secret si fuite. Lea a appris ca a ses depens. Max a eu de la chance. Sam raconte l'histoire pour que personne n'ait a la vivre.

## Patterns utiles et templates

```text
*.log
tmp/
build/
dist/
*.pdf
!docs/manuel.pdf
```

`!` peut re-inclure une exception. Commence simple. Complexifie seulement si besoin. GitHub propose des `.gitignore` tout faits (Python, Node...). Tu peux t'en inspirer. Chez DanielCraft, on veut que tu comprennes chaque ligne que tu gardes. Une ligne incomprise est une ligne dangereuse ou inutile.

## Petite histoire

Max a ecrit un `.gitignore` pour un mini site HTML/CSS/JS avec `dist/` ignore. Il a build, vu que `status` restait propre. Sam a fait relire `status` avant tout push : "cherche mots de passe, cles, dumps". Lea garde une checklist de poche. Chez DanielCraft, le professionnalisme commence souvent par ce que tu n'enregistres pas. Lea a aussi montre a un client un depot propre : pas de secrets, pas de `node_modules`, README clair. Le client n'a pas vu Git. Il a vu de la rigueur.

## Erreur classique

Ignorer apres avoir commit le secret, sans `rm --cached`. Croire que `.gitignore` efface un fichier deja suivi. Committer `.env.example` utile... et aussi `.env` reel. Autre piege : ignorer trop large (`*` partout) et ne plus versionner ton code. Sois precis. Encore un piege : croire que "prive sur GitHub" egal "secret safe". Prive aide. Ca ne remplace pas `.gitignore` ni la rotation d'une cle fuitee.

## En vrai

Avant le premier push public : relis `git status`. Cherche mots de passe, cles, dumps, photos perso. Puis seulement, pousse. Fais-le meme sur un faux projet. Le rituel compte plus que le risque immediat. Chez DanielCraft, on prefere dix secondes de relecture a une heure de nettoyage d'historique. Si tu hesites sur une ligne du `.gitignore`, demande-toi : "est-ce du code source utile demain ?" Oui -> versionne. Non -> ignore.

## A toi

Ajoute un `.gitignore` a ton carnet de tests. Cree un faux `.env` avec `SECRET=demo`. Verifie que Git l'ignore. Bonus : `.gitignore` pour un mini site avec `dist/` a ignorer. Ecris en trois lignes ta checklist perso "avant push".
