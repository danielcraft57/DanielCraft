# Chapitre 1 - Rappel rapide et carte du livre

Tu as deja fait le premier livre HTML et CSS. Tu sais structurer une page, ecrire des balises, relier un fichier CSS, jouer avec les couleurs et les polices. Tu as vu les boites (margin, padding, border), Flexbox pour ranger les blocs, et une intro au responsive. Un peu d'accessibilite aussi.

Ici, on ne recommence pas a zero. Pas de cours "c'est quoi une marge" pendant trois pages. Si Flexbox te semble encore flou, relis le premier livre. Ce tome-ci monte d'un cran : pages plus propres, plus solides, plus jolies sans tricher.

Chez DanielCraft, on aime une image simple. Les bases, c'etait poser les murs et peindre une piece. La suite, c'est poser un vrai plan d'etage, choisir une palette qui tient partout, faire bouger un bouton sans sursaut, et penser a ceux qui naviguent autrement que toi.

## Ce que tu gardes en tete

Tu sais ecrire un HTML clair avec `h1`, `p`, `a`, `img`. Tu sais cibler avec des classes. Tu sais aligner avec Flexbox. Tu as deja ouvert la page sur telephone (ou reduit la fenetre). C'est assez pour avancer.

On ne revient pas sur "comment faire un lien" ni sur "display: flex" de A a Z. On s'en sert, oui. On ne le reexplique pas comme a un debutant total. Pareil pour margin et padding : tu les connais, on les utilise sans lecon debutant.

## La carte du livre

Imagine une page produit, un petit blog, ou une landing pour un atelier. Pour que ca tienne vraiment, il te manque encore quelques pieces. Voici la carte, dans l'ordre ou on va les poser.

D'abord le HTML semantique : dire au navigateur "ca, c'est le menu", "ca, c'est l'article", "ca, c'est le pied de page". Ensuite la cascade et la specificite : comprendre pourquoi une regle gagne sur une autre, sans paniquer. Puis les variables CSS : une couleur declaree une fois, reutilisee partout.

Grid arrive ensuite : poser la page en lignes et colonnes, pas seulement en rangee Flexbox. On fera les bases, puis une vraie mise en page (header, contenu, aside). Juste apres, Flex vs Grid : savoir choisir l'outil, pas empiler les deux au hasard.

Les images modernes : taille, `object-fit`, une idee simple de `srcset`. Les formulaires styles proprement. Des transitions legeres (hover doux, pas de cirque). L'accessibilite suite : focus visible, contrastes, labels. Un mini-projet qui assemble grid et variables. Un recap. Trois ateliers pour faire, pas seulement lire. Le mode sombre avec les variables. Un peu de perf CSS. Du debug (outils, outline, hypotheses). Un quiz. Et un bravo final.

## Un fil rouge

On va souvent parler de trois exemples. Une page produit (carte, prix, bouton). Un blog (en-tete, articles, pied). Une landing simple (hero, sections, appel a l'action). Ces exemples reviennent, pour que tu sentes le progres.

Tu verras le meme geste sous plusieurs angles : structurer, thematiser, poser la grille, soigner le detail, verifier que ca reste utilisable au clavier.

## Ce dont tu as besoin

Un editeur (VS Code, Cursor, ou autre). Un navigateur moderne. Les outils developpeur (F12). Pas de framework. Pas de Bootstrap obligatoire. Ici, on reste en HTML et CSS "nus", clairs, dans le navigateur.

## Comment lire ce livre

Lis dans l'ordre au debut. Semantique, cascade, variables, puis Grid. Flex vs Grid apres. Images, formulaires, transitions, accessibilite avant le mini-projet. Les ateliers sont la pour faire. Dark mode, perf et debug viennent solidifier. Le quiz verifie. Le dernier chapitre, c'est pour souffler.

Si tu connais deja un sujet, lis quand meme le chapitre vite : le ton et les exemples servent de rappel utile pour la suite.

## Erreur classique

Croire que "je connais les bases" = "je sais faire une vraie page pro". Les bases sont le moteur. La suite, c'est le plan, la coherence, le confort, et le respect des visiteurs. Sans semantique, ta page est un tas de `div`. Sans variables, changer de couleur devient un cauchemar. Sans Grid (ou un plan clair), le layout casse des que la fenetre change. Sans accessibilite, tu excludes du monde sans le vouloir.

Autre piege : sauter directement au mini-projet. Les ateliers et les chapitres courts sur le debug existent pour une raison. Une page "jolie" qui casse au Tab ou qui melange trois verts differents n'est pas finie.

## En vrai

Ouvre une page que tu as deja codee (page perso, carte produit...). Note ce qui manque : un vrai `header` / `main` ? une couleur copiee quinze fois ? un layout qui casse en large ? un bouton sans etat focus ? un formulaire moche ? Ce livre repond a ca.

Si tu n'as aucune page sous la main, note trois pages web que tu aimes (boutique, blog, landing) et observe : ou est le menu, ou est le contenu, comment les cartes s'alignent, si le bouton change doucement au survol.

## A toi

Ecris en trois phrases ce que tu veux construire a la fin. Pas un reseau social. Quelque chose de petit : "une page produit propre", "un blog a deux articles", "une landing pour mon atelier". Garde ce but. On y reviendra au mini-projet et aux ateliers.
