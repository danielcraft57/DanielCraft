# Chapitre 6 - Revue de code humaine

La pull request n'est pas un portail magique. C'est une conversation. Quelqu'un propose un changement. Quelqu'un d'autre regarde, pose des questions, suggere, approuve. Git transporte les diffs. Les humains portent le sens.

Sans revue, on merge des bombes polies. Avec une revue toxique, on merge moins, on cache, on a peur. L'objectif : une revue utile et bienveillante.

## Pourquoi reviewer ?

Parce que quatre yeux voient plus que deux. Parce que Max connait le back et peut voir que le front de Lea casse une API. Parce que Sam se souvient qu'un cas mobile n'est pas teste. Parce que ecrire pour etre lu oblige a clarifier.

Chez DanielCraft, la revue est un filet, pas un tribunal.

## Quoi regarder (sans tout relire ligne a ligne)

Tu n'as pas a etre un compilateur humain. Priorise.

Est-ce que la PR fait ce qu'elle dit ? Est-ce que le perimetre est raisonnable (pas 30 sujets) ? Est-ce qu'il y a un risque securite evident (secret, injection grossiere, permission trop large) ? Est-ce que les noms aident ? Est-ce que tu saurais maintenir ce code dans trois mois ? Est-ce que l'auteur a indique comment tester ?

Regarde aussi ce qui manque : gestion d'erreur, cas vide, accessibilite d'un bouton, message utilisateur incomprehensible.

Tu peux laisser passer un detail de style mineur si l'equipe n'a pas de regle stricte. Tu ne laisses pas passer un formulaire qui envoie des donnees en clair par erreur.

## Le ton qui aide

Prefere "Ici, si l'email est vide, on n'affiche pas d'erreur - on pourrait bloquer l'envoi" a "C'est nul". Prefere "Je ne comprends pas cette condition, tu peux m'expliquer ?" a "Lol quoi". Prefere "Suggestion :" a "Obligatoire :" quand c'est vraiment une preference.

Dis aussi ce qui est bien. "Claire la separation HTML / CSS" prend trois secondes et donne de l'energie. La revue n'est pas seulement une chasse aux defauts.

## En tant qu'auteur de la PR

Aide le reviewer. Titre clair. Description courte : but, changements principaux, comment tester. Capture d'ecran si c'est visuel. Lien vers une issue si elle existe.

```text
## But
Afficher les tarifs sur /offres

## Changements
- section tarifs dans offres.html
- styles associes
- liens depuis l'accueil

## Comment tester
1. Ouvrir /offres
2. Verifier mobile
3. Cliquer "Contact" depuis un tarif
```

Reponds aux commentaires sans te defendre par principe. Si tu n'es pas d'accord, explique calmement. Si tu corriges, pousse un commit et dis "c'est a jour".

## Taille de PR

Une PR de 150 lignes se review. Une PR de 2500 lignes se feint. Decoupe. Si tu ne peux pas decouper (trop lie), guide le reviewer : "commence par `api.js`, puis le template".

## Temps de reponse

Une PR qui attend une semaine pourrit. L'auteur rebase, le contexte se perd, la motivation tombe. En petite equipe, vise un premier regard en 24h quand c'est possible. Meme un "je regarde demain matin" compte.

## Approve, request changes, commentaire

Sur GitHub, tu peux commenter sans bloquer, demander des changements, ou approuver. Utilise "request changes" pour les vrais blocants. N'approuve pas par pitie si tu n'as pas regarde. N'utilise pas "request changes" pour une virgule.

## Erreur classique

La revue ego : "moi j'aurais fait autrement" sur chaque ligne. Ou la revue fantome : Approve sans ouvrir les fichiers. Ou l'auteur invisible qui n'ecrit aucune description. Les trois cassent le jeu.

## En vrai

Prends une PR passee (la tienne ou une publique). Ecris trois commentaires bienveillants et utiles que tu aurais pu laisser. Puis ecris le commentaire toxique equivalent... et jette-le. Sens la difference. Garde la premiere version comme modele mental.


## Exemple de fil de review (ton juste)

Sam sur la PR de Lea :

"J'ai suivi tes etapes de test sur mobile : le bloc tarifs passe bien. Une question : sur tres petit ecran, le prix passe sous le bouton - voulu ? Si non, on peut empiler en colonne des 480px. Suggestion, pas bloqueur si tu vises desktop d'abord."

Lea repond : "Pas voulu. Je pousse un correctif ce soir." Elle pousse. Sam Approuve. Merge. Quatre messages, zero ego, un meilleur site.

## Ce qu'on ne review pas (ou peu)

Le gout personnel sans regle d'equipe ("moi j'aime les simples quotes"). La refonte totale hors sujet. Le "j'aurais tout ecrit autrement" sans proposition actionnable. La revue n'est pas un concours de style.

## Check-list mentale du reviewer (sans en faire une religion)

Je comprends le but. J'ai regarde les fichiers touches. J'ai teste ou j'ai dit pourquoi je ne pouvais pas. J'ai signale les risques. J'ai laisse au moins une remarque utile ou un approve conscient. C'est deja une bonne review.

## Quand tu n'es pas expert du domaine

Tu peux quand meme aider : clarte des noms, cas limites evidents, secrets, "je ne comprends pas ce bloc". Dire "je ne connais pas bien cette API, Max peut-tu jeter un oeil ?" est professionnel. Ce n'est pas un echec.


## A toi

Ajoute dans le README de l'equipe trois phrases : "On review pour aider.", "On explique le comment tester.", "On dit aussi ce qui est clair." Lis-les avant ta prochaine review.
