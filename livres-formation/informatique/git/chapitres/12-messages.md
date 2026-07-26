# Chapitre 12 - De bons messages de commit

Un bon **message** sauve ton futur toi. Et ton equipe. Et le client qui te demande "pourquoi ce total a change en mars". L'**historique** n'est pas un tas de "update" empiles. C'est un journal de bord : chaque commit raconte une intention. Si tu ne comprends plus un message d'hier, le probleme n'est pas Git. C'est la legende de la photo. Chez DanielCraft, on traite le message comme une competence pro, pas comme une corvee qu'on reportera au prochain sprint.

Lea ecrit a l'imperatif court : "Ajouter", "Corriger", "Clarifier". Elle ajoute le pourquoi quand ce n'est pas evident : "Corriger le total TTC (oubli de la TVA)". Max a du desapprendre "final final 2" et "aaa" apres avoir ri de son propre `log`. Sam projette un `git log --oneline` propre et un sale devant la classe : la difference se voit en dix secondes. Toi, tu vas viser le propre. Pas le parfait academique. Le lisible. Le jour ou tu debug a 23h un vendredi, tu remercieras ton toi du matin.

Imagine que tu lis ton historique a voix haute dans six mois, sans ouvrir les fichiers. La premiere ligne doit tenir en une respiration (50 a 72 caracteres ideaux). Prefere un verbe a l'**imperatif** : "Ajouter", pas "J'ai ajoute". Explique le pourquoi si ce n'est pas evident. Un commit = une intention coherente. Pas "j'ai change 40 fichiers sans rapport parce que c'etait vendredi". Pas non plus 40 micro-commits illegibles ("fix", "fix2"). Le juste milieu vient avec l'experience. En attendant, vise "une idee claire par photo".

:::retenir
Un commit = une intention. La premiere ligne resume. Le pourquoi reste si ce n'est pas evident.
:::

## Ce que ce n'est pas

Un bon message, ce n'est pas un roman de vingt lignes a chaque fois. Ce n'est pas non plus un emoji seul ou un numero de ticket copie-colle sans contexte. Ce n'est pas obligatoire d'adopter Conventional Commits des le jour un - utile en equipe, apercu ici - mais ce n'est pas une religion. Et ce n'est surtout pas "je corrigerai plus tard" : tu ne reecris pas toute l'historique tous les matins. Ecris bien maintenant.

Ce n'est pas non plus "un label `feat:` devant asdf". Un prefixe ne sauve pas un message vide. L'intention d'abord. Le format ensuite. Lea l'utilise sur les projets clients a plusieurs. Max s'en passe en solo, mais garde des messages clairs sans prefixe. Les deux vont.

## Oui et Non (exemples concrets)

Les bons messages ressemblent a ca : "Corriger le total TTC (oubli de la TVA)", "Ajouter la page contact", "Retirer le fichier .env du suivi". Tu comprends l'action et souvent la raison. Les mauvais ressemblent a ca : "update", "fix", "wip", "asdf", "final final 2". Ils ne disent rien. Ils polluent l'album. Quand Sam voit "fix stuff" dans un depot eleve, il demande : "fix quoi, pour qui, pourquoi ?". Si tu ne peux pas repondre, le message est mauvais. Reecris-le avant de pousser, ou amend si tu n'as pas encore pousse et que tu es seul sur la branche.

Lea compare deux projets : l'un avec des messages nets, l'autre avec des "update". Sur le premier, elle retrouve un bug en deux minutes. Sur le second, elle lit des diffs pendant une heure. Max a compris le jour ou il a du expliquer un changement a un client : le message clair lui a evite de rougir au telephone.

## Corps optionnel et Conventional Commits

Parfois le titre ne suffit pas. Git accepte un corps de message :

```bash
git commit -m "Corriger le calcul du panier" -m "Le total ignorait les codes promo. Desormais appliques avant TVA."
```

Tu verras parfois en equipe des prefixes comme `feat:`, `fix:`, `docs:` :

```text
feat: ajouter export PDF
fix: corriger lien casse du sommaire
docs: preciser l'install Windows
```

Utile quand toute l'equipe parle la meme langue. Pas obligatoire pour apprendre. L'important : l'intention lisible, pas le label a la mode. Chez DanielCraft, on juge un historique a voix haute : si Sam comprend sans contexte, c'est bon.

## Exemple de fil propre

Voici un historique qu'on peut lire en dix secondes :

```text
Initialiser le projet
Ajouter la page d'accueil
Corriger le lien du menu mobile
Ignorer le fichier .env
Documenter l'installation dans le README
```

Tu vois l'histoire du projet sans ouvrir un seul fichier. C'est ca, le but. Si tu rougis en lisant ton propre log, change ta facon d'ecrire demain, pas dans six mois. La honte productive marche. Max l'a vecue. Lea aussi, plus tot dans sa carriere. Sam la provoque volontairement en classe avec bienveillance.

:::astuce
Projette ton `git log --oneline` a voix haute. Si Sam comprend sans contexte, c'est bon. Si tu rougis, change ta facon d'ecrire demain.
:::

## Petite histoire

Lea a du retrouver pourquoi un total etait faux sur un site e-commerce. Le message "Corriger le total TTC (oubli de la TVA)" l'a menee en trente secondes au bon commit. Sur un autre projet legacy, "update" l'a forcee a lire des diffs pendant une heure. Max a reecrit sa facon d'ecrire apres avoir projete son log devant un ami developpeur. Sam fait ecrire trois messages "pro" avant le premier vrai commit en classe. Rituel simple, resultat durable. Chez DanielCraft, le message clair est une forme de respect pour l'equipe future - et pour toi-meme.

## Erreur classique

Messages vides de sens : "update", "fix", "changes". Tout mettre dans un seul commit "grosse feature" sans decoupage. Mentir dans le message ("fix typo" alors que tu as refactore toute l'archi). Copier le style Conventional sans en respecter l'esprit : un label `feat:` devant "asdf" reste un mauvais message. Autre piege : ecrire pour une IA, pas pour un humain qui debug a 23h un vendredi. L'humain d'abord. Toujours.

## En vrai

Lis ton `git log --oneline` sur ton carnet de tests. Si tu ne comprends plus un message d'hier, c'est le signal. Renomme ta facon d'ecrire des maintenant. Fais 3 commits sur ton carnet avec des messages "pro". Compare avant/apres. Tu sentiras la difference tout de suite.

## A toi

Reecris ces messages pourris en bons messages : `update`, `fix stuff`, et `aaa`. Puis applique le meme standard sur ton prochain vrai commit. Garde l'exemple de fil propre sous les yeux une semaine. Note ce qui t'a le plus aide : l'imperatif, le pourquoi entre parentheses, ou la taille d'un commit.
