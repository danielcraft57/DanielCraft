# Chapitre 6 - Revue de code humaine

La **pull request** n'est pas un portail magique. C'est une conversation. Quelqu'un propose un changement. Quelqu'un d'autre regarde, pose des questions, suggere, approuve. Git transporte les diffs. Les humains portent le sens. Sans revue, on merge des bombes polies. Avec une revue toxique, on merge moins, on cache, on a peur. L'objectif : une **revue** utile et bienveillante. Chez DanielCraft, la revue est un filet, pas un tribunal.

Parce que quatre yeux voient plus que deux. Parce que Max connait le back et peut voir que le front de Lea casse une API. Parce que Sam se souvient qu'un cas mobile n'est pas teste. Parce qu'ecrire pour etre lu oblige a clarifier. Tu n'as pas a etre un compilateur humain. Priorise : est-ce que la PR fait ce qu'elle dit ? Est-ce que le **perimetre** est raisonnable (pas trente sujets) ? Est-ce qu'il y a un risque securite evident (secret, injection grossiere, permission trop large) ? Est-ce que les noms aident ? Est-ce que tu saurais maintenir ce code dans trois mois ? Est-ce que l'auteur a indique comment tester ?

:::retenir
La revue aide. Elle ne juge pas. Dire aussi ce qui est clair change toute l'ambiance.
:::

## Le ton qui aide

Prefere "Ici, si l'email est vide, on n'affiche pas d'erreur - on pourrait bloquer l'envoi" a "C'est nul". Prefere "Je ne comprends pas cette condition, tu peux m'expliquer ?" a "Lol quoi". Prefere "Suggestion :" a "Obligatoire :" quand c'est vraiment une preference. Dis aussi ce qui est bien. "Claire la separation HTML / CSS" prend trois secondes et donne de l'energie. La revue n'est pas seulement une chasse aux defauts.

En tant qu'auteur, aide le reviewer. Titre clair. Description courte : but, changements principaux, comment tester. Capture d'ecran si c'est visuel. Lien vers une issue si elle existe :

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

Reponds aux commentaires sans te defendre par principe. Si tu n'es pas d'accord, explique calmement. Si tu corriges, pousse un commit et dis "c'est a jour". Une PR de cent cinquante lignes se review. Une PR de deux mille cinq cents lignes se feint. Decoupe. Si tu ne peux pas decouper, guide le reviewer : "commence par `api.js`, puis le template". En petite equipe, vise un premier regard en vingt-quatre heures quand c'est possible. Meme un "je regarde demain matin" compte.

:::astuce
"Comment tester" dans la description, c'est un cadeau au reviewer. Trois etapes suffisent souvent.
:::

Sam sur la PR de Lea : "J'ai suivi tes etapes de test sur mobile : le bloc tarifs passe bien. Une question : sur tres petit ecran, le prix passe sous le bouton - voulu ? Si non, on peut empiler en colonne des 480px. Suggestion, pas bloqueur si tu vises desktop d'abord." Lea repond : "Pas voulu. Je pousse un correctif ce soir." Elle pousse. Sam Approuve. Merge. Quatre messages, zero ego, un meilleur site. Sur GitHub, tu peux commenter sans bloquer, demander des changements, ou approuver. Utilise "request changes" pour les vrais blocants. N'approuve pas par pitie si tu n'as pas regarde.

Max, un jour, a Approuve "parce que c'etait petit" sans ouvrir les fichiers. Le formulaire a casse. Depuis, l'equipe dit : "Approve conscient ou pas Approve." Ce n'est pas de la rigidite. C'est du respect pour la prod et pour Lea qui devra debugger.

## Petite histoire

Max a approuve une PR "parce que c'etait petit" sans ouvrir les fichiers. Le formulaire a casse la prod le vendredi. Depuis, l'equipe dit : "Approve conscient ou pas Approve." Lea, elle, a appris a ecrire "comment tester" avant chaque PR. Les reviews sont devenues plus rapides parce qu'elles sont plus claires. Ce n'est pas de la triche. C'est de la politesse technique.

Chez DanielCraft, on repete : le ton compte autant que le fond. Une remarque juste dite mal, et la prochaine PR sera cachee. Une remarque moyenne dite bien, et l'auteur corrige avec le sourire.

## Erreur classique

La revue ego : "moi j'aurais fait autrement" sur chaque ligne. Ou la revue fantome : Approve sans ouvrir les fichiers. Ou l'auteur invisible qui n'ecrit aucune description. Les trois cassent le jeu. Tu peux quand meme aider sans etre expert du domaine : clarte des noms, cas limites evidents, secrets, "je ne comprends pas ce bloc". Dire "je ne connais pas bien cette API, Max peut-tu jeter un oeil ?" est professionnel.

:::attention
Approve fantome et Request changes pour une virgule : deux extremes qui cassent la confiance. Vise le fond, garde le ton.
:::

## En vrai

Prends une PR passee (la tienne ou une publique). Ecris trois commentaires bienveillants et utiles que tu aurais pu laisser. Puis ecris le commentaire toxique equivalent... et jette-le. Sens la difference. Garde la premiere version comme modele mental.

## A toi

Ajoute dans le README de l'equipe trois phrases : "On review pour aider.", "On explique le comment tester.", "On dit aussi ce qui est clair." Lis-les avant ta prochaine review.
