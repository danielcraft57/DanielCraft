# Chapitre 21 - Bravo

Tu as fini Git en equipe. Pas "tu connais toutes les options de toutes les commandes". Mieux : tu sais collaborer sans te marcher dessus. Chez DanielCraft, on mesure le progres a une chose simple : est-ce que ton prochain projet a plusieurs sera plus calme que le precedent ? Si oui, le livre a servi. Si non, relis le flux et la revue. Le reste s'accroche dessus.

Tu as une carte. **Flux**. Branches simples. Rebase et merge sans dogme. Historique lisible. Revue humaine. `main` **protegee**. CI legere. Tags et releases. Cherry-pick pour une cerise urgente. Bisect pour trouver le commit casse. Un mini-projet. Des ateliers. Fork et upstream. **Secrets** hors du depot. Des pratiques d'equipe tenables. Ce n'est pas un diplome. C'est un kit de survie pour les mardis et les vendredis.

:::retenir
Connaitre Git, c'est le moteur. Savoir collaborer, c'est la route. Tu as les deux. Tiens le contrat leger.
:::

Lea pousse sa branche. Max demande un regard. Sam dit merci au reviewer. Quelqu'un tire `main`. On recommence. Ce rythme, c'est le livre en une scene. Pas un examen. Une **habitude**. Un vendredi soir sans panique vaut mieux qu'un score parfait au quiz. Tu n'as pas besoin d'etre heroique. Tu as besoin d'etre regulier : petites PR, reviews utiles, filets techniques, secrets dehors.

Imagine le tableau blanc du chapitre 1. `main` distant, c'est le tableau officiel. Lea, Max et Sam ont chacun une copie. Sans flux, chacun dessine et s'ecrase. Avec flux : tire, dessine sur ton coin, propose, regarde, colle, nettoie. Tu connais maintenant chaque geste. Il reste a le vivre demain matin.

## Petite histoire

Lea avait peur des conflits. L'atelier les a demystifies. Max poussait sur `main` "parce que c'est plus vite". Une protection de branche l'a sauve d'un vendredi noir. Sam a commit une cle "temporairement". Le chapitre secrets l'a rattrape avant la prod. Trois peurs, trois filets. Si tu bloques, reviens au flux (ch. 2) et a la revue (ch. 6). Presque tous les frottements viennent de la.

Chez DanielCraft, on a vu des equipes talentueuses souffrir faute de contrat leger. Et des equipes moyennes livrer calmement avec cinq phrases dans un README. Le talent compte. Le rythme compte plus souvent.

:::astuce
Cette semaine, une seule pratique : protege `main`, ou ouvre une PR avec description, ou verifie `.gitignore`. Une. Tiens-la. Puis ajoute la suivante.
:::

## Ce que tu peux faire maintenant

Tenir un README de collaboration. Ouvrir des PR petites et claires. Reviewer sans blesser. Refuser le push direct sur `main`. Taguer une version. Retrouver un bug dans l'histoire. Contribuer via fork. Garder les cles dehors. Applique une pratique a la fois. Garde le contrat leger a jour. Quand ca frotte, ajustez sans ego. La suite (hooks avances, monorepo, changelog auto) s'accrochera sur ce socle. Sans socle, les outils avances empilent du bruit.

Tu peux aussi transmettre. Montre le flux a un stagiaire. Fais-lui vivre l'atelier conflit une fois. Lis avec lui la phrase sur les secrets. Enseigner ancre. L'equipe gagne deux fois. Si tu es seul, ecris un court message a un ami : "voila comment on travaille chez nous". Formuler force la clarte.

Checklist poche a coller sous l'ecran : tire `main` le matin ; branche nommee ; commits qui disent le pourquoi ; PR avec comment tester ; review utile ; merge ; tire `main` ; nettoie la branche ; tague quand tu livres ; secrets hors Git. Dix lignes. Une vie d'equipe.

## Erreur classique

Fermer le livre et revenir aux anciennes habitudes "juste pour ce hotfix". Ou empiler bots et hooks avant d'avoir un flux tenu. Autre piege : attendre d'etre expert DevOps pour proteger `main`. Tu n'as pas besoin d'etre expert. Tu as besoin d'un filet simple aujourd'hui. Autre piege : croire que le quiz 12/12 te dispense de la prochaine review bienveillante.

:::attention
Le "juste pour ce hotfix" sur `main` sans PR, c'est souvent le debut de la regression. Passe par une branche, meme a 19h.
:::

## En vrai

Cette semaine : protege `main` sur un depot (meme de test), ouvre une PR avec description, demande un regard. Une seule pratique. Tiens-la. Note ce qui change dans ton calme. Le calme est le vrai indicateur. Dans quinze jours, ajoute une deuxieme pratique (CI legere, ou `.env.example`, ou tags). Le rythme se construit par couches.

## Mission

Ecris ton contrat d'equipe en cinq lignes. Colle-le dans le README. Fais une PR qui le respecte. Puis respire. Tu n'as pas "fini Git". Tu as commence a collaborer proprement. C'est plus rare. C'est plus utile.

Cinq lignes type : "On tire main avant chaque branche. On travaille en feature/fix courtes. Toute integration passe par une PR avec comment tester. main est protegee, une review minimum. Jamais de secrets dans Git ; on tague les livraisons utiles." Adapte. Signe. Tiens.

## A toi

Coche : flux tenu / PR avec description / `main` protegee ou plan pour / secrets verifies. Si une case manque, fais-la avant le prochain livre. Pousse ta branche. Demande un regard. Merci ton reviewer. Tire `main`. Recommence. Bravo. Tu sais travailler a plusieurs avec Git.

## Petite scene finale

Lea ouvre une PR courte le mardi. Max laisse un commentaire utile. Sam merge apres vert CI. Personne ne crie. Chez DanielCraft, ce silence calme, c'est le vrai bravo. Pas un score. Un rythme.
