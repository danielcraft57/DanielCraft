# Chapitre 11 - Deboguer mieux

Quand ca casse, le reflexe humain c'est "je recopie tout depuis Stack Overflow". Le reflexe utile, c'est : lire le message, trouver la ligne, formuler une hypothese, verifier une chose a la fois. Deboguer, ce n'est pas un echec. C'est une partie normale du metier. Les developpeurs experimentes passent une bonne part de leur temps a lire des erreurs. Chez DanielCraft, on le dit franchement : savoir deboguer compte autant que savoir ecrire du code neuf.

Lea debogue avec la console et les breakpoints chaque jour. Max a appris a ne plus paniquer devant le rouge. Sam apprend a ses eleves que l'erreur est un indice, pas une punition. Ce chapitre te donne les outils de base du navigateur, sans IDE complexe.

## La console, ton amie

console.log n'est pas honteux. C'est un projecteur. Affiche la valeur juste avant l'endroit douteux. Affiche reponse.status. Affiche typeof data. Affiche data.length. Souvent, le bug saute aux yeux : undefined la ou tu attendais un tableau, cle JSON mal orthographiee, selecteur qui renvoie null.

Pense aussi a console.error pour les vrais problemes (dans un catch par exemple), et a retirer les logs inutiles avant de montrer ton travail a un client. Un mur de "test 1", "test 2" dans la console n'aide personne en prod.

## Lire une stack trace

Quand le navigateur affiche une erreur rouge, il donne souvent un fichier et un numero de ligne. Clique dessus dans les DevTools. Regarde la pile : "appele depuis telle fonction, elle-meme depuis telle autre". Tu remontes le fil. Si le message dit Cannot read properties of null, tu as probablement selectionne un element qui n'existe pas encore (DOM pas pret), ou un mauvais selecteur (#liste vs .liste).

## Points d'arret (breakpoints)

Dans les outils developpeur (F12), onglet Sources, tu peux cliquer a gauche d'une ligne pour poser un breakpoint. La page s'arrete la quand le code passe. Tu inspectes les variables en direct. Tu avances pas a pas (step over, step into). C'est plus precis qu'un mur de logs quand le bug est subtil ou depend de l'ordre d'execution.

## Hypotheses courtes

Ecris mentalement : "Je pense que data n'est pas un tableau." Puis verifie avec Array.isArray(data). Une hypothese a la fois. Sinon tu changes trois choses en meme temps et tu ne sais plus ce qui a marche. Lea colle parfois un post-it : "Hypothese 1 : mauvaise URL." Elle teste. Puis hypothese 2.

## Reseau et DOM

Onglet Network : ta requete fetch est-elle partie ? Quel status HTTP ? Quel corps de reponse ? Parfois le bug n'est pas dans ton JS mais dans ce que le serveur renvoie. Onglet Elements : ton #liste existe-t-il au moment ou tu essaies de le remplir ? Si ton script est en head sans defer, le DOM n'est peut-etre pas pret.

## Petite histoire

Max a passe une heure a "reparer fetch" alors que son id etait liste-produits dans le HTML et listeProduits dans le JS. querySelector renvoyait null. Un console.log(liste) avant la boucle aurait tout debloque en deux minutes. Depuis, il loggue les variables suspectes avant de supposer que le reseau est en cause.

## Erreur classique

Changer dix lignes a la fois "pour voir". Ajouter des catch vides qui avalent l'erreur. Ignorer le message complet et ne lire que la premiere ligne. Copier une solution sans comprendre pourquoi ca marchait. Ou ne jamais ouvrir les DevTools et rester dans le flou.

## En vrai

Prends un vieux bug (ou invente-en un : mauvais id HTML, await oublie). Force l'erreur. Lis le message complet a voix haute. Relie-le a une ligne precise dans ton code. Pose un breakpoint ou un log strategique. C'est l'entrainement qui transforme la panique en routine.

## A toi

Prends un code qui marche (mini-projet ou atelier). Casse-le volontairement (mauvais selecteur, oubli de await). Debogue sans regarder la solution. Note en trois lignes ce qui t'a aide : console, Network, breakpoint ? Garde cette mini-fiche pour la prochaine fois.

## Routine de debug en cinq minutes

1) Reproduis le bug une fois, note l'action exacte. 2) Lis l'erreur complete dans la console. 3) Clique la ligne, regarde les variables. 4) Formule une hypothese unique. 5) Teste un seul changement. Lea suit cette routine meme sous pression client. Ca evite le "j'ai tout change et je ne sais plus".

## Erreurs fetch frequentes a reconnaitre

Failed to fetch : souvent reseau, CORS, ou mauvaise URL. Unexpected token < in JSON : tu parses du HTML (page d'erreur) en JSON. Cannot read properties of undefined : souvent data mal structuree ou await oublie. 404 sans crash fetch : oublie de verifier ok. Garde cette liste dans un coin de ton bureau virtuel.

## Outils complementaires

L'onglet Network montre le timing : ta lenteur vient-elle du reseau ou de ta boucle DOM ? L'onglet Application montre localStorage si tu stockes du JSON. Preserve log en console garde les messages apres rechargement : utile quand le bug arrive au submit. Sam fait une demo live de ces onglets : dix minutes qui valent des heures de guess.
