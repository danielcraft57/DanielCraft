# Chapitre 11 - Deboguer mieux

Quand ca casse, le reflexe "je recois tout" est humain. Le reflexe utile, c'est : lire le message, trouver la ligne, verifier une hypothese.

## La console, ton amie

`console.log` n'est pas honteux. C'est un projecteur. Affiche la valeur juste avant l'endroit douteux. Affiche `reponse.status`. Affiche `typeof data`. Souvent, le bug saute aux yeux : `undefined`, tableau vide, mauvaise cle JSON.

Pense aussi a `console.error` pour les vrais problemes, et a retirer les logs inutiles avant de montrer ton travail.

## Lire une stack

Quand le navigateur affiche une erreur rouge, il donne souvent un fichier et un numero de ligne. Clique dessus. Regarde la pile : "appele depuis telle fonction, elle-meme depuis telle autre". Tu remontes le fil.

Si le message dit `Cannot read properties of null`, tu as probablement selectionne un element qui n'existe pas encore, ou un mauvais selecteur.

## Points d'arret

Dans les outils developpeur (F12), onglet Sources, tu peux cliquer a gauche d'une ligne pour poser un breakpoint. La page s'arrete la. Tu inspectes les variables. Tu avances pas a pas. C'est plus precis qu'un mur de logs.

## Hypotheses courtes

Ecris (mentalement) : "Je pense que `data` n'est pas un tableau." Puis verifie. Une hypothese a la fois. Sinon tu changes trois choses et tu ne sais plus ce qui a marche.

## En vrai

Les developpeurs experimentes passent une bonne partie du temps a lire des erreurs. Ce n'est pas un echec. C'est le metier. DanielCraft te le dit franchement : savoir deboguer compte autant que savoir ecrire.

## A toi

Prends un vieux bug (ou invente-en un : mauvais id HTML). Force l'erreur. Lis le message complet a voix haute. Relie-le a une ligne precise. C'est l'entrainement.
