# Chapitre 16 - Atelier : conflit en equipe

Les **conflits** font peur parce qu'ils arrivent souvent le vendredi, quand tout le monde veut partir. Ici, tu vas en creer un expres, le resoudre calmement, et voir que ce n'est qu'un fichier qui demande un choix humain. Git ne "casse" pas. Il s'arrete et te demande : "deux versions, laquelle ?" Chez DanielCraft, le meilleur conflit est celui evite tot. Le deuxieme meilleur est celui resolu sans drama. Duree : 45 a 75 minutes. Ecris le **livrable**. Sans note, le cerveau classe ca comme "lu", pas comme "su".

Lea a panique la premiere fois qu'elle a vu les marqueurs. Max aussi. Sam a appris `merge --abort` avant d'apprendre a resoudre. Abandonner proprement est une competence. Tu vas en avoir besoin. Cet atelier ne te rend pas expert en fusion. Il te rend capable de respirer quand le terminal crie.

:::retenir
Un conflit, c'est un choix de contenu, pas une panne Git. Respire, choisis, enleve les marqueurs, commit.
:::

Deux branches touchent le meme titre. Alex ecrit "Atelier Git equipe". Blake ecrit "Site vitrine DanielCraft". `main` recoit Alex d'abord. Blake synchronise : conflit. Marqueurs `<<<<<<<`. Tu choisis, ou tu combines. Tu enleves les marqueurs. Tu commits. Tu respires. La page affiche une seule version claire. Personne n'a "gagne". Le site a gagne.

Le meme scenario arrive en vrai quand Lea et Max touchent `index.html` le meme jour sans se le dire. Git fusionnera peut-etre les zones eloignees. Sur la meme ligne, il demandera un humain. Le canal ("je touche le titre aujourd'hui") reste le meilleur antidote. L'atelier, lui, entraine le muscle quand l'antidote a rate.

## But et scenario

Provoquer un conflit sur le meme fichier, le resoudre, finir sur une `main` propre. Deux branches touchent le titre de `index.html` (ou le bandeau). Alex et Blake partent du meme `main`. Tu peux jouer les deux roles sur un seul compte. Idealement, un ami joue Blake pour sentir le "vrai" frottement.

## Etapes

1. Sur `main` a jour, note le titre actuel.

```bash
git switch main
git pull
```

2. Branche Alex : `feature/titre-atelier`, modifie le titre, commit, pousse, **PR**, merge dans `main`.

3. Puis branche Blake depuis `main` tire :

```bash
git switch main
git pull
git switch -c feature/titre-vitrine
```

Autre texte au meme endroit. Commit.

4. Ramene `main` :

```bash
git fetch origin
git merge origin/main
```

Conflit. Marqueurs :

```text
<<<<<<< HEAD
titre de Blake
=======
titre d'Alex (venu de main)
>>>>>>> ...
```

5. Choisis ou combine ("Site vitrine DanielCraft - atelier Git"). Enleve les marqueurs. Sauve. Relis le fichier : aucun `<<<<<<<` ne doit rester.

6. Resolu :

```bash
git add index.html
git commit
```

7. Pousse. PR. Description : "Resolution de conflit sur le titre, version combinee telle." Review. Merge.

8. Tire `main`. Verifie le titre dans le navigateur. Sens le soulagement : c'etait ca, le monstre.

:::astuce
Si tu paniques au milieu : `git merge --abort` (ou `git rebase --abort`). Tu reviens a l'avant. Puis tu recommences a froid.
:::

## Variante rebase

Au lieu de merge : `git rebase origin/main`, resols, `git rebase --continue`, puis `git push --force-with-lease` sur la branche perso. Compare le ressenti. Le **rebase** rejoue tes commits sur une base plus recente. Le merge colle les histoires avec un noeud. Les deux demandent le meme choix de contenu. Seule la forme de l'historique change. Note ce que tu preferes. On en reparlera dans le contrat d'equipe.

## Petite histoire

Lea a laisse les marqueurs dans le fichier : page cassee en prod, texte illisible avec des `=======`. Max a choisi au hasard sans parler : ego blesse, mauvaise version. Sam a combine et explique dans la PR : calme, trace, confiance. Regle d'equipe a ecrire : "si on touche aux memes zones, on se parle avant" + "on synchronise `main` souvent".

Chez DanielCraft, on chronometre parfois cet atelier. Quarante-cinq minutes suffisent si le depot est pret. Soixante-quinze si c'est la premiere fois que tu vois les marqueurs. Le but n'est pas la vitesse. C'est le calme.

## Criteres et panique

Aucun `<<<<<<<` restant. Site affiche. Historique montre la resolution. Tu expliques a voix haute ce que tu as choisi et pourquoi. Si panique : abort, pause cafe, recommence. Un conflit mal resolu pousse sur `main` est pire qu'un conflit non resolu encore local.

:::attention
Ne force-push jamais sur `main` pour "effacer le conflit". Tu effaces aussi le travail des autres. Resols, commit, PR.
:::

## Erreur classique

Resoudre en gardant "les deux textes empiles" sans enlever les marqueurs. Ou blamer la personne au lieu de choisir le contenu. Ou synchroniser `main` une fois par semaine seulement : tu transformes un petit conflit en roman. Autre piege : ouvrir la PR sans dire "j'ai resolu un conflit, voici le choix". Le reviewer doit savoir.

## En vrai

Ecris la regle d'equipe anti-conflit en deux phrases. Colle-la dans le README. Relis-la le prochain lundi avant de toucher `index.html`.

## A toi

Fais l'atelier. Livrable : notes du choix final + regle d'equipe + ressenti merge vs rebase si teste. Range-le. La prochaine fois que le terminal criera, tu auras deja vecu la scene.
