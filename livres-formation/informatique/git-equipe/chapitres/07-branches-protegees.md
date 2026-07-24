# Chapitre 7 - Branches protegees : pas de push direct sur main

Tu peux ecrire la belle regle "on ne pousse pas sur main" dans le README. Un jour, quelqu'un oubliera. Un autre jour, un stagiaire ne l'aura pas lue. Un vendredi, tu pousseras toi-meme "juste un hotfix" a 19h.

Les branches protegees, c'est le filet technique. GitHub (et GitLab, et d'autres) peuvent refuser le push direct sur `main` et imposer le passage par une pull request.

## L'idee

Proteger `main`, c'est dire au serveur : "cette branche est speciale". On n'y ecrit pas comme sur un brouillon. On y arrive apres review (et souvent apres des checks automatiques).

Lea ne peut plus faire par erreur :

```bash
git push origin main
```

si la protection est bien configuree. Elle devra pousser sa branche et ouvrir une PR.

## Ou ca se regle (idee GitHub)

Sur GitHub, dans le depot : Settings, puis la zone Branch protection / Rules. Tu choisis la branche `main`. Tu actives des options du genre : exiger une pull request avant merge, exiger un certain nombre d'approbations, exiger que les status checks passent (CI), interdire le force push, interdire la suppression de la branche.

Tu n'as pas besoin de tout cocher le premier jour. Pour une equipe de 3 chez DanielCraft, un bon minimum est : pas de push direct, PR obligatoire, au moins une review, pas de force push sur `main`.

Les ecrans changent selon les versions de GitHub. L'intention reste : regles sur `main`, filet visible.

## Ce que ca change au quotidien

Max finit un fix. Il pousse `fix/login`. Il ouvre une PR vers `main`. Lea approuve. Max clique Merge. `main` avance. Le depot a refuse les raccourcis.

Si quelqu'un tente un push direct, le serveur dit non. C'est sec. C'est bon. Mieux vaut un message d'erreur clair qu'une prod cassee.

## Administrateurs et exceptions

Parfois les admins peuvent bypasser. C'est tentant. Utilisez cette exception rarement, et seulement pour des urgences vraiment discutees. Si les admins bypassent tous les jours, vous n'avez plus de protection : vous avez un theatre.

## Proteger aussi les tags ? Plus tard

On peut proteger les tags pour eviter qu'on deplace une version `v1.2.0`. Utile quand les releases comptent vraiment. Pour commencer, protege `main`. Les tags viennent au chapitre 9.

## Lien avec la CI

Si tu exiges que les checks soient verts avant merge, une CI legere (chapitre 8) devient un garde-fou automatique. Review humaine + tests automatiques = double filet. Ni l'un ni l'autre n'est parfait seul.

## Petite equipe, grand benefice

"On est que deux, pas besoin." Justement : a deux, un clic malheureux n'a pas de troisieme personne pour rattraper dans la seconde. La protection est rapide a activer et evite des soirees tristes.

## Erreur classique

Activer la protection sans prevenir l'equipe : tout le monde panique ("Git est casse"). Ou activer vingt regles d'un coup (3 reviews, 12 checks, signatures) au point de bloquer tout livraison. Commence simple. Explique. Ajuste.

Autre piege : proteger `main` mais laisser `master` ou une vieille branche de prod non protegee. Verifie quelle branche est vraiment deployee.

## En vrai

Sur un depot de test (pas le client critique), active une regle : PR obligatoire sur `main`. Demande a un collegue (ou a ton second compte) d'essayer un push direct. Voyez le refus. Puis faites le chemin PR. Le corps retient mieux qu'un paragraphe.


## Scenario avant / apres

Avant : Max pousse sur `main` un hotfix a 19h12. Le site casse. Lea tire `main` le lendemain et passe une heure a comprendre. Personne n'a review. Aucune CI.

Apres : Max pousse `fix/...`, ouvre une PR, Sam regarde deux minutes, CI verte, merge. Meme urgence relative, mais un filet. Si la CI est rouge, Max corrige avant d'infecter `main`.

## Combien de reviews ?

A trois personnes, une approval suffit souvent. A dix, parfois deux. N'impose pas trois approvals si vous etes trois et que deux sont en conges : vous vous bloquez. Adapte la regle a la taille reelle.

## Bypass et urgence

Vraie urgence prod : parfois un admin bypass, merge, deploie, puis ouvre une issue "post-mortem leger" le lendemain. Fausse urgence ("j'ai la flemme de la PR") : non. L'equipe doit sentir la difference.

## Autres branches a proteger ?

Parfois `production` ou `release/*`. Pour ce livre et une petite equipe : protege la branche que tu deploies vraiment. Souvent `main`. Une seule source de verite.


## A toi

Note dans le README : "main est protegee : pas de push direct, PR + 1 review minimum." Ajoute le lien vers les settings si utile. La regle ecrite + la regle technique = coherence.
