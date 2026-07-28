# Chapitre 8 - Permissions et moindres privileges

Donner a tout le monde le compte **admin** "parce que c'est plus simple" est un accelerateur de catastrophe. Si ce compte fuit, tout fuit. Le principe du **moindre privilege** : chaque personne ou service a seulement les droits necessaires a sa tache. Chez DanielCraft, c'est une habitude, pas un slogan. Lea a un compte editeur pour le quotidien et un admin rare. Max a arrete de partager le meme login. Sam cree des roles.

:::retenir
Moins de droits = moins de casse si un compte ou une session fuit.
:::

## Comptes et roles

Admin / proprietaire : installations, utilisateurs, reglages critiques. Editeur / auteur : contenu. Lecteur : consultation. Pour un freelance et un client : separez les acces. Desactivez les comptes partis. Revoquez les cles API inutiles.

## Fichiers et services

Sur un hebergeur, evite les dossiers world-writable "parce que ca marche". Limite qui peut deployer. Les clefs SSH et tokens CI sont des permissions : range-les, rotate-les si fuite. On reste debutant : pas besoin d'IAM cloud avance pour commencer - juste ne pas tout ouvrir.

:::astuce
Une fois par trimestre : liste des comptes avec acces admin. Qui est encore legitime ?
:::

## Petite histoire

Un stagiaire avait l'admin "le temps du stage". Trois mois plus tard, le compte existait encore. Lea l'a revoque le jour de l'audit maison. Sam a ajoute une case "offboarding" a la checklist. Max a compris que permission = dette si on oublie.

## Erreur classique

Un seul compte pour toute l'equipe. Autre piege : laisser des comptes de test avec mots de passe faibles sur le live.

:::attention
Les comptes "demo123" / "test/test" sur la prod sont des portes ouvertes avec neon.
:::

## En vrai

Dresse la liste des gens (et bots) qui ont acces a ton site. Pour chacun : role minimum. Raye le superflu.

## A toi

Ecris qui a l'admin aujourd'hui et pourquoi. Si la reponse est "tout le monde", corrige avant la fin de semaine.
