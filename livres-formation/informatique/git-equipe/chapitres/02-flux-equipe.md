# Chapitre 2 - Flux d'equipe : qui pousse ou, quand tirer

Git seul, c'est un carnet. Git en equipe, c'est un carnet partage ou tout le monde ecrit en meme temps. Sans accord, c'est le chaos poli : "j'ai pousse sur main", "j'ai ecrase ta branche", "je n'ai pas tire depuis trois jours".

Ce chapitre pose le flux. Pas la theorie des remotes. Le rythme du travail a 2 ou 3 personnes sur un meme site.

## L'image du tableau blanc

Chez DanielCraft, on imagine souvent un tableau blanc au milieu de la piece. `main` sur le serveur, c'est le tableau officiel. Ta machine a une copie. La machine de Lea aussi. Si chacun dessine sans regarder le tableau, vous vous ecrasez.

Le flux, c'est juste la regle : je mets a jour ma copie, je dessine sur mon coin (ma branche), je propose mon dessin (PR), quelqu'un regarde, puis on colle sur le tableau.

## Une journee type a trois

Le matin, Max arrive. Il veut corriger un bug sur le formulaire. Il fait ceci, dans cet esprit :

```bash
git switch main
git pull
git switch -c fix/formulaire-email
```

Il travaille. Il commit. Il pousse sa branche, pas `main` :

```bash
git push -u origin fix/formulaire-email
```

Il ouvre une pull request. Lea regarde. Sam teste le formulaire. On merge. Max revient sur `main` et tire :

```bash
git switch main
git pull
```

Lea, pendant ce temps, travaille sur `feature/page-tarifs`. Elle a tire `main` ce matin. Elle n'a pas besoin d'attendre Max pour coder. Elle aura besoin de se resynchroniser avant de merger, surtout si Max a touche des fichiers proches.

## Qui pousse ou ?

En petite equipe, la regle simple est :

Chacun pousse sur sa branche feature ou fix. Personne ne pousse directement sur `main` (sauf urgence vraiment discutable, et encore : mieux vaut une PR rapide). Le depot distant (`origin`) est la memoire commune. Ta machine n'est pas la source de verite pour les autres.

Si Max commit seulement en local et part en vacances, Lea ne voit rien. Si Max pousse sa branche, Lea peut regarder, tester, commenter.

Push tot, push souvent sur ta branche. Pas sur `main`. Sur ta branche.

## Quand tirer (pull) ?

Tire `main` au debut de ta session. Tire `main` avant d'ouvrir une PR. Tire `main` si quelqu'un vient de merger quelque chose d'important pendant que tu codes.

Tu n'as pas besoin de tirer toutes les cinq minutes. Tu as besoin de tirer avant les moments ou ca compte : demarrer, synchroniser, livrer.

```bash
git switch main
git pull
git switch feature/page-tarifs
git merge main
```

Ici, Lea ramene les nouveautes de `main` dans sa feature. Elle peut aussi rebase (chapitre 4). L'intention est la meme : ne pas decouvrir le conflit le jour du merge final.

## Communication minimale

Git ne remplace pas un message. "Je touche `contact.html` aujourd'hui" evite deux personnes sur le meme fichier. "PR prete, besoin d'un regard" evite que la PR pourrisse trois jours.

Dans une equipe de 3, un canal (Discord, Mattermost, salon Slack) suffit. Pas besoin d'un process de 12 pages. Besoin de dire ce qu'on fait.

## Le rythme "petit et frequent"

Une feature qui vit deux jours, avec 4 petits commits et une PR de 120 lignes, se review facilement. Une branche qui vit trois semaines, avec 40 commits melanges et 2000 lignes, devient un roman. Personne ne le lit vraiment. On clique Approve en esperant.

Le flux d'equipe marche mieux avec des tranches courtes. Decoupe. Livre. Recommence.

## Que faire si tu es bloque par quelqu'un ?

Sam attend la PR de Max pour avancer. Max est en reunion. Options : Sam continue sur une autre tache, ou Sam et Max se mettent d'accord pour une branche partagee (plus rare, plus de communication). Evite de "emprunter" la branche de Max pour y pousser sans prevenir. Surprise = conflits + egos.

## Le remote n'est pas magique

`git pull` ramene ce qui est deja pousse. Si Lea n'a pas pousse, tu ne vois pas son travail. Si tu n'as pas pousse, personne ne voit le tien. Le flux suppose que le travail utile finit sur le serveur, sur une branche claire.

## Matin, midi, merge

Le matin : tire `main`, choisis ta tache, cree ou reprends ta branche. Midi (ou en fin de tranche) : pousse ta branche pour ne pas garder le travail seul sur ton disque. Avant la pause longue : status propre ou stash conscient. En fin de feature : PR + message dans le canal. Apres merge : retour sur `main`, pull, suppression de branche.

Ce n'est pas du militaire. C'est un rythme qui evite les "ou est passe mon travail ?" et les "je n'avais pas la derniere version".

## Fichiers chauds

`index.html`, la config, le schema de base : si deux personnes y touchent le meme jour, parlez-vous. Git fusionnera peut-etre. Le sens metier, lui, demandera un humain. Un message "je touche contact.html cet apres-midi" coute dix secondes.

## Erreur classique

Coder deux jours sur `main` en local, puis faire un gros push. Ou ne jamais tirer et decouvrir 15 commits des autres au moment de merger. Ou pousser `--force` sur une branche partagee "parce que ca a marche chez moi".

Autre piege : croire que "on est que deux, on peut tout faire sur main". A deux, un vendredi soir, un revert malheureux, et vous avez le meme probleme qu'a dix. La discipline legere protege aussi les petites equipes.

## En vrai

Demain matin, avant de coder, fais le rituel :

```bash
git switch main
git pull
git status
```

Puis cree ou reprends ta branche. Note combien de fois cette semaine tu as tire `main`. Si la reponse est "une fois lundi", augmente le rythme.

## A toi

Ecris le flux de ton equipe en cinq lignes maximum, comme une recette. Exemple : "1) pull main 2) branche 3) commits 4) push branche 5) PR 6) review 7) merge 8) pull main". Colle-le dans le README du depot de test. Tout le monde doit pouvoir le lire en trente secondes.
