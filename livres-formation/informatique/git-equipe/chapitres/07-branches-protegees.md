# Chapitre 7 - Branches protegees : pas de push direct sur main

Tu peux ecrire la belle regle "on ne pousse pas sur main" dans le README. Un jour, quelqu'un oubliera. Un autre jour, un stagiaire ne l'aura pas lue. Un vendredi, tu pousseras toi-meme "juste un hotfix" a 19h. Les **branches protegees**, c'est le filet technique. GitHub (et GitLab, et d'autres) peuvent refuser le push direct sur `main` et imposer le passage par une **pull request**. Chez DanielCraft, on prefere un message d'erreur clair qu'une prod cassee.

Proteger `main`, c'est dire au serveur : "cette branche est speciale". On n'y ecrit pas comme sur un brouillon. On y arrive apres **review** (et souvent apres des checks automatiques). Lea ne peut plus faire par erreur :

```bash
git push origin main
```

si la protection est bien configuree. Elle devra pousser sa branche et ouvrir une PR. Sur GitHub, dans le depot : Settings, puis la zone Branch protection / Rules. Tu choisis la branche `main`. Tu actives des options du genre : exiger une pull request avant merge, exiger un certain nombre d'approbations, exiger que les status checks passent (CI), interdire le force push, interdire la suppression de la branche.

:::retenir
La regle ecrite dans le README est fragile. La regle technique sur `main` tient meme un vendredi a 19h.
:::

## Ce que ca change au quotidien

Max finit un fix. Il pousse `fix/login`. Il ouvre une PR vers `main`. Lea approuve. Max clique Merge. `main` avance. Le depot a refuse les raccourcis. Si quelqu'un tente un push direct, le serveur dit non. C'est sec. C'est bon. Pour une equipe de trois, un bon minimum est : pas de push direct, PR obligatoire, au moins une review, pas de force push sur `main`. Les ecrans changent selon les versions de GitHub. L'intention reste : regles sur `main`, filet visible.

Si tu exiges que les checks soient verts avant merge, une **CI** legere (chapitre 8) devient un garde-fou automatique. Review humaine plus tests automatiques egal double filet. Ni l'un ni l'autre n'est parfait seul. Parfois les admins peuvent bypasser. C'est tentant. Utilisez cette exception rarement, et seulement pour des urgences vraiment discutees. Si les admins bypassent tous les jours, vous n'avez plus de protection : vous avez un theatre.

:::attention
Si les admins bypassent la protection tous les jours, vous n'avez plus de filet : vous avez un theatre. Reserve le bypass aux vraies urgences discutees.
:::

Avant : Max pousse sur `main` un hotfix a 19h12. Le site casse. Lea tire `main` le lendemain et passe une heure a comprendre. Personne n'a review. Aucune CI. Apres : Max pousse `fix/...`, ouvre une PR, Sam regarde deux minutes, CI verte, merge. Meme urgence relative, mais un filet. Si la CI est rouge, Max corrige avant d'infecter `main`. A trois personnes, une approval suffit souvent. A dix, parfois deux. N'impose pas trois approvals si vous etes trois et que deux sont en conges : vous vous bloquez.

Sam aime dire : "le serveur dit non, ce n'est pas moi qui suis mechant". Ca desarme les egos. Lea sourit. Max pousse sa branche. Le flux tient.

## Petite histoire

L'equipe a active la protection sans prevenir personne. Tout le monde a panique : "Git est casse." Sam a explique en cinq minutes. Deux semaines plus tard, personne ne voudrait revenir en arriere. "On est que deux, pas besoin." Justement : a deux, un clic malheureux n'a pas de troisieme personne pour rattraper dans la seconde. La protection est rapide a activer et evite des soirees tristes.

Chez DanielCraft, on active souvent la protection le jour 1 du depot de test, avant meme le premier vrai feature. Habitude avant vitesse.

## Erreur classique

Activer vingt regles d'un coup (3 reviews, 12 checks, signatures) au point de bloquer toute livraison. Commence simple. Explique. Ajuste. Autre piege : proteger `main` mais laisser `master` ou une vieille branche de prod non protegee. Verifie quelle branche est vraiment deployee. On peut proteger les tags plus tard (chapitre 9). Pour commencer, protege `main`.

:::astuce
Minimum utile a trois : PR obligatoire, une review, pas de force push sur `main`. Tu pourras durcir ensuite.
:::

## En vrai

Sur un depot de test (pas le client critique), active une regle : PR obligatoire sur `main`. Demande a un collegue (ou a ton second compte) d'essayer un push direct. Voyez le refus. Puis faites le chemin PR. Le corps retient mieux qu'un paragraphe. Si tu es solo, cree une seconde branche et tente le push : le message d'erreur suffit a ancrer.

## A toi

Note dans le README : "main est protegee : pas de push direct, PR plus 1 review minimum." Ajoute le lien vers les settings si utile. La regle ecrite plus la regle technique egal coherence. Bonus : ajoute une phrase sur le bypass admin ("urgence discutee seulement").

## Zoom : filet visible, egos calmes

Sam aime le moment ou le serveur dit non. Ce n'est plus "Max est mechant". C'est "la branche est protegee". Lea sourit. Max pousse sa feature. Chez DanielCraft, on active souvent la protection le jour 1 du depot de test, avant meme le premier vrai feature. Habitude avant vitesse. Tu peux durcir ensuite. Tu peux rarement assouplir sans drame si la prod a deja brule.
