# Chapitre 9 - Injections : l'idee (defense)

Quand une application **colle** une entree utilisateur (champ, URL, fichier) directement dans une instruction - requete base de donnees, page HTML, commande - cette entree peut **casser** le sens de l'instruction. L'idee s'appelle souvent **injection**. Chez DanielCraft, on explique le risque pour **prevenir**. On ne montre **aucun** exploit, **aucune** payload, **aucune** recette d'attaque. Lea valide les champs. Max a appris a ne plus concatenner une requete a la main. Sam enseigne : "Separe les donnees et les instructions."

:::retenir
Entree non fiable = ne jamais la coller telle quelle dans une requete ou une page. Valider. Parametrer. Echapper a l'affichage.
:::

## Ce qui se passe (sans recette)

Imagine une question a une base : tu veux chercher un nom. Si tu construis la question en collant le texte tape par l'utilisateur au milieu, ce texte peut etre interprete comme une partie de la question plutot que comme une simple donnee. Resultat possible : comportement inattendu, fuite, corruption. Pareil cote page : un texte affiche sans precaution peut devenir du code de page. Tu n'as pas besoin de savoir "comment faire" pour comprendre "il ne faut pas coller".

## Defense : validation

Verifie le type, la longueur, le format attendu (email, nombre, liste de valeurs). Refuse ce qui sort du contrat. La validation cote navigateur aide l'UX. La validation **serveur** est le vrai frein.

## Defense : requetes preparees (idee)

Les **requetes parametrees** / preparees envoient la structure de la question d'un cote et les valeurs de l'autre. La base traite la valeur comme donnee, pas comme code SQL. C'est l'idee a retenir. Utilise les outils de ton langage / ORM qui le font correctement. N'invente pas une concatenation "securisee a la main" si tu debutes.

## Defense : affichage

Quand tu reaffiches une entree sur une page, utilise les mecanismes d'echappement du framework (ou equivalent) pour que le texte reste du texte. Encore une fois : pas de payload de demo ici.

:::attention
Ce chapitre est strictement defensif. Pas de PoC. Pas de "pour tester chez toi". Si tu veux approfondir, cherche des ressources defense / OWASP dans un cadre legitime - pas des tutoriels d'attaque.
:::

## Petite histoire

Max concatenait une recherche "pour aller vite". Lea a remplace par une requete parametree du framework. Sam a fait valider longueur et alphabet autorise. Aucun d'eux n'a "teste une injection". Ils ont ferme la porte. Chez DanielCraft, c'est le succes.

## Erreur classique

Croire que "personne ne visitera mon petit form". Autre piege : montrer des payloads "pedagogiques" a une equipe junior - ca devient une arme mal rangee.

:::astuce
Checklist code : entree -> valider -> API parametree / echappement -> stocker / afficher.
:::

## En vrai

Repere un endroit de ton projet (ou un schema) ou une entree arrive. Ecris comment tu valides et comment tu evites de coller dans une instruction.

## A toi

Explique en cinq phrases a un ami : pourquoi coller une entree dans une requete est dangereux, et quels freins tu utilises - sans donner d'exemple d'attaque.
