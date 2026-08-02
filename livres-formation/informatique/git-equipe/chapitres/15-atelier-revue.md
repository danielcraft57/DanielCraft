# Chapitre 15 - Atelier : revue de code

Ici, le code est un pretexte. L'atelier entraine le regard et le ton. Tu prepareras volontairement une **PR** "presque bien" avec deux vrais points a discuter. Chez DanielCraft, une **revue** bienveillante et utile bat une revue brillante et humiliante. Duree : 45 a 60 minutes. Ecris le **livrable**.

Lea ecrit. Max review. Sam alterne. Toi, tu joues les deux casquettes : **auteur** puis **reviewer**. La **description** aide le reviewer. Le reviewer aide l'auteur. Personne ne "gagne". Le code gagne. Si le ton casse, la prochaine PR sera cachee. Si le ton tient, l'equipe accelere. Tu vas sentir la difference entre "C'est nul" et "Ici, si l'email est vide, on pourrait bloquer l'envoi". Meme fond. Autre monde. C'est exactement le muscle de ce chapitre.

:::retenir
Le ton compte autant que le fond. Une remarque juste dite mal casse la confiance.
:::

## But et preparation

Ecrire une PR aidante, puis faire une revue bienveillante et utile. Sur un depot de test, depuis `main` a jour, cree `feature/formulaire-contact-atelier`. Ajoute un formulaire : champ email, bouton envoyer, validation imparfaite (accepte `a@b` sans domaine - voulu), commentaire HTML vague `<!-- temp -->`. Commit en deux temps. Pousse. Ouvre la PR avec vraie description (but, changements, comment tester). N'avoue pas tous les defauts : laisse le reviewer travailler. Si tu avoues tout, tu rates l'entrainement du regard.

Avant d'ouvrir la PR, relis le chapitre 6 en diagonale : priorites, ton, "comment tester". Puis ecris la description comme si Max allait la lire a 18h, fatigue. Trois sections. Pas un roman. Pas "fix". Lea dit que la description est le cadeau. Max a longtemps ecrit "voir le diff". Depuis qu'il detaille, ses reviews durent dix minutes au lieu de quarante.

## Etapes auteur

1. Titre : verbe + objet ("Ameliore le formulaire de contact").
2. Remplis but / changements / comment tester.
3. Capture si tu peux.
4. Demande review a un ami, ou change de casquette.

Prends le temps sur "comment tester". Trois lignes claires. Ouvre la page. Tape un email foireux. Clique Envoyer. Note ce que tu attends. Si tu ne peux pas ecrire ces trois lignes, la PR n'est pas prete pour un humain exterieur.

## Etapes reviewer

1. Lis la description avant le diff.
2. Suis "comment tester" pour de vrai.
3. Au moins deux commentaires utiles : validation email, commentaire `temp`.
4. Formule en suggestions, sans insultes, sans "evident".
5. Dis une chose positive.
6. Request changes si le bug email est bloquant, sinon Comment + discussion.

:::astuce
Dis une chose positive avant ou apres la suggestion. Trois secondes, beaucoup d'energie pour l'auteur.
:::

Modeles de formulation. Suggestion : "Ici, si l'email est `a@b`, l'envoi part quand meme - on pourrait exiger un domaine avec un point." Bloqueur : "La validation laisse passer `a@b` : Request changes pour ce point avant merge." Positif : "Claire la structure du formulaire, facile a tester." Copie ces trois tons. Adapte. Garde-les.

## Etapes retour auteur

1. Reponds sans te defendre pour la forme.
2. Corrige la validation. Enleve `<!-- temp -->`.
3. Pousse. "C'est a jour, tu peux revoir".
4. Approuver et merger si c'est bon.

Le "sans te defendre pour la forme" est dur la premiere fois. Sam le rappelle : tu defends le produit, pas ton ego. Lea respire avant de repondre. Max aussi, depuis une reponse trop seche un mardi. Si tu n'es pas d'accord sur un point de style, dis-le calmement. Si le bug email est reel, corrige sans debat d'ego.

## Petite histoire

Lea a Approuve sans tester : bug en prod. Max a Request changes pour une virgule : ego blesse, PR cachee. Sam a dit une chose positive puis pointe le fond : correctif en vingt minutes. Variante solo : ecris la revue dans `NOTES-REVIEW.md` comme a un collegue, puis applique tes remarques. L'exercice du ton reste valable.

Chez DanielCraft, on garde parfois deux formulations modeles dans le README : une pour une suggestion, une pour un vrai bloqueur. Lea les copie. Max aussi. Moins de stress, plus de clarte. Tu peux sortir de cet atelier avec tes deux modeles a toi.

## Criteres et pieges

PR initiale avec description utilisable. Revue sur le fond (validation), pas seulement l'esthetique. Ton respectueux. Correctif suivi. `main` via merge. Eviter : Approve sans tester ; Request changes pour preference de virgule ; auteur qui ignore ; reviewer qui reecrit toute la PR sans discussion. Si tu te surprends a reecrire, propose plutot un pair-programming apres merge.

## Erreur classique

Croire que "reviewer = trouver des fautes". Ou "auteur = defendre chaque ligne". Autre piege : discuter le style pendant une heure et rater le bug fonctionnel. Autre piege : Approve fantome pour "avancer". La confiance casse deux semaines plus tard, plus cher. Autre piege : auteur qui corrige en silence sans repondre : le reviewer ne sait pas si c'est fait.

:::attention
Discuter une virgule une heure et rater le bug email : mauvaise priorite. Le fond d'abord, le style ensuite.
:::

## En vrai

Copie deux formulations de commentaires que tu trouves reussies. Elles serviront de modeles. Lis-les a voix haute. Si ca sonne comme un jugement de personne, reformule sur le code. Colle-les dans le README sous "Exemples de revue".

## A toi

Fais l'atelier. Livrable : lien PR (ou notes) + deux commentaires modeles + une lecon sur le ton. Range-le. Bonus : montre tes deux formulations a un collegue et demande : "tu prefere recevoir laquelle ?" Dans une semaine, applique le meme ton sur une vraie PR, meme petite.
