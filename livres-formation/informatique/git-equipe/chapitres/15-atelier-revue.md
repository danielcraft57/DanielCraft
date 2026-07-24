# Chapitre 15 - Atelier : revue de code

Ici, le code est un pretexte. L'atelier entraine le regard et le ton. Tu prepareras volontairement une PR "presque bien" avec deux vrais points a discuter.

## But

Ecrire une PR aidante, puis faire une revue bienveillante et utile. Duree : 45 a 60 minutes.

## Preparation

Sur un depot de test, depuis `main` a jour, cree `feature/formulaire-contact-atelier`.

Ajoute (ou modifie) un formulaire de contact avec :
- un champ email
- un bouton envoyer
- une validation imparfaite (exemple : accepte `a@b` sans domaine complet) - c'est voulu pour la revue
- un commentaire HTML un peu vague `<!-- temp -->` a enlever

Commit en deux temps. Pousse. Ouvre la PR avec une vraie description (but, changements, comment tester). N'avoue pas tous les defauts dans la description : laisse le reviewer travailler.

## Etapes auteur

1. Redige le titre : verbe + objet ("Ameliore le formulaire de contact").
2. Remplis but / changements / comment tester.
3. Ajoute une capture si tu peux (meme simple).
4. Demande une review a un ami, ou change de casquette.

## Etapes reviewer

1. Lis la description avant le diff.
2. Suis "comment tester" pour de vrai.
3. Laisse au moins deux commentaires utiles : un sur la validation email, un sur le commentaire `temp` (ou autre detail reel).
4. Formule en suggestions, sans insultes, sans "evident".
5. Dis une chose positive (structure, clarte HTML, effort de description...).
6. Choisis : Request changes si le bug email est bloquant, sinon Comment + discussion.

## Etapes retour auteur

1. Reponds sans te defendre pour la forme.
2. Corrige la validation. Enleve `<!-- temp -->`.
3. Pousse. Ecris "c'est a jour, tu peux revoir".
4. Fais Approver et merger si c'est bon.

## Criteres de reussite

La PR initiale avait une description utilisable. La revue a pointe le fond (validation), pas seulement l'esthetique. Le ton restait respectueux. Un correctif a suivi. `main` a recu le resultat via merge.

## Pieges a eviter

Approve sans tester. Request changes pour une preference de virgule. Auteur qui ignore les commentaires. Reviewer qui reecrit toute la PR a la place de l'auteur sans discussion.

## Variante solo

Ecris la revue dans un fichier `NOTES-REVIEW.md` comme si tu parlais a un collegue. Puis applique tes propres remarques. L'exercice du ton reste valable.

## Apres l'atelier

Copie deux formulations de commentaires que tu trouves reussies. Elles serviront de modeles la prochaine fois.
