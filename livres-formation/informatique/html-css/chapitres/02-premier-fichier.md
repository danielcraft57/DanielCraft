# Chapitre 2 - Ton premier fichier HTML

On va creer un fichier. Rien de complique. Pas de compte. Pas de carte bleue. Pas de "plateforme magique". Juste un editeur, un navigateur, et toi. Chez DanielCraft, on insiste la-dessus : le premier geste web, c'est sauvegarder un **`.html`** et l'ouvrir. Quand tu vois ton texte a l'ecran, quelque chose bascule. Tu n'es plus spectateur. Tu es auteur. Lea le vit encore a chaque nouveau stagiaire. Max l'a vecu sur sa page plomberie. Sam le recree en classe chaque annee.

Tu as besoin de deux choses. Un editeur de texte : le Bloc-notes marche, VS Code (gratuit) est plus confortable. Un navigateur : celui que tu utilises deja. C'est tout. Lea travaille dans VS Code parce que la coloration aide a voir les balises. Max a commence avec le Bloc-notes et ca a suffi pour sa premiere page artisan. Sam montre les deux a ses eleves : l'outil change, le fichier reste le meme. L'important, c'est le geste : ecrire, sauvegarder, ouvrir, corriger, rafraichir.

En 2026, quand quelqu'un dit "j'ai cree ma premiere page", il parle souvent de ce cycle. Derriere, il y a des generateurs et des CMS. Pour toi, le geste fondateur reste nu : un fichier, un navigateur, un F5. Tu restes le pilote. Le fichier obeit.

:::retenir
Sauvegarde en `.html`, ouvre dans le navigateur, modifie, F5. C'est le cycle de base.
:::

## Ce que ce n'est pas

Ce n'est pas encore un site en ligne. Ton fichier vit sur ton ordinateur. Pour le mettre sur Internet, il faudra un hebergement - plus tard. Ce n'est pas un framework. Ce n'est pas "du HTML avance". C'est un squelette : **doctype**, html, head, body, un titre, un paragraphe. Si tu cherches deja les animations et les menus deroulants, tu te disperses. D'abord le fichier. Ensuite le reste.

Ce n'est pas non plus un fichier Word renomme. HTML, c'est du texte brut avec des balises. Pas de bouton "gras" cache. Chaque instruction est visible. C'est une force : tu vois ce que tu fais. Lea dit : "si tu ne vois pas la balise, tu ne controles pas la page".

Pense a une lettre. Le `<head>`, c'est l'enveloppe et les infos pour le facteur (titre de l'onglet, encodage des accents). Le `<body>`, c'est le message que le destinataire lit. Le navigateur ouvre la lettre et l'affiche. Toi, tu ecris. Lui, il montre. Lea dit : "head pour la machine, body pour l'humain". Max retient : "ce que je vois dans l'onglet, c'est le head ; ce que je vois sur la page, c'est le body". Sam dessine l'enveloppe au tableau. Les eleves ne melangent plus les deux.

## Cree le fichier

Ouvre ton editeur. Copie le code ci-dessous. Enregistre en `index.html` (attention a l'extension `.html`, pas `.txt`). Double-clique dessus. Ca s'ouvre dans le navigateur.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Ma premiere page</title>
</head>
<body>
  <h1>Salut !</h1>
  <p>Ca y est. J'ai fait une page web.</p>
</body>
</html>
```

Si tu vois "Salut !" en gros, bravo. C'est bon. Si tu vois le code brut au lieu de la page, regarde l'extension du fichier : souvent Windows a ajoute `.txt` en douce. Renomme proprement. Sauvegarde. Rouvre. Le contraste enseigne mieux qu'un paragraphe.

:::attention
Sur Windows, verifie que le fichier s'appelle bien `index.html` et pas `index.html.txt`. Sinon le navigateur affiche le code brut.
:::

## On explique ligne par ligne (sans stress)

`<!DOCTYPE html>` dit au navigateur : c'est du HTML moderne. Toujours en haut. `<html lang="fr">` ouvre la page et precise le francais. `<head> ... </head>` contient les infos pour le navigateur, pas le gros du contenu visible. Exemple : le titre de l'onglet avec `<title>`. `<meta charset="UTF-8">` fait marcher les accents. Crucial en francais. Sans ca, tu peux voir des caracteres bizarres. `<body> ... </body>` est le corps : tout ce que tu vois va ici. `<h1>` est un gros titre. `<p>` est un paragraphe.

Tu n'as pas a reciter ca par coeur. Tu as a reconnaitre le squelette. Lea le tape une fois par projet. Max le copie depuis son premier fichier. Sam le fait reconstruire de memoire en fin de seance.

## Les balises ouvrantes et fermantes

Regarde : `<p>` ouvre. `</p>` ferme. Le slash `/` veut dire "c'est fini pour ce truc". Comme des parentheses. Tu ouvres, tu fermes. Si tu oublies une fermeture, la page peut avoir l'air cassee. Respire. Corrige. Rafraichis (**F5**). Chez DanielCraft, le cycle "sauvegarder puis F5" est sacre. Sans lui, tu debogues un fantome.

:::astuce
Apres chaque modif : sauvegarde, puis F5. Si tu oublies de rafraichir, tu crois que "ca n'a rien change".
:::

## Petite histoire

Lea a perdu vingt minutes la premiere fois parce que son fichier s'appelait `index.html.txt`. Le navigateur affichait le code comme du texte. Elle a demande a un collegue. Il a rit doucement, a montre l'extension, et elle n'a plus jamais fait l'erreur. Max, lui, avait mis le titre dans le body et se demandait pourquoi l'onglet disait encore "sans titre". Il a deplace le `<title>` dans le head. Clique. Compris.

Sam fait parfois l'exercice en classe : deux fichiers identiques, un `.html` et un `.txt`. Les eleves comprennent que le navigateur ne devine pas : il lit ce que tu lui donnes, avec le bon nom. Trois scenes, une lecon : le nom du fichier compte autant que son contenu.

## Erreur classique

Enregistrer en `.txt` sans le voir. Oublier le charset et croire que "le francais casse HTML". Mettre tout dans le head. Ou oublier de rafraichir apres une modif et croire que "ca n'a rien change". Toujours : sauvegarder, puis F5. Autre piege : modifier le mauvais fichier (copie sur le bureau vs copie dans le dossier projet). Verifie le chemin avant de paniquer. Lea garde une regle : une seule source de verite, un seul dossier projet.

## En vrai

Cree le fichier. Change le texte du `h1` avec ton prenom. Sauvegarde. Rafraichis. Tu viens de modifier un site. Serieux. Puis change le titre de l'onglet. Observe la difference entre ce qui est dans le head et ce qui est dans le body. Ajoute une deuxieme phrase dans un nouveau `<p>`. Tu construis deja une vraie page, meme minuscule. Si le code brut s'affiche, regarde l'extension. Corrige. Relance.

## A toi

Ecris une page "Ma premiere page" avec ton prenom dans le h1, une phrase sur toi dans un paragraphe, et un titre d'onglet clair. Note en une ligne ce qui t'a bloque, s'il y a eu un blocage. On debugge plus tard - la, on valide le geste. Garde ce fichier : tu t'en serviras dans tout le livre. Style DanielCraft : petit, clair, testable, un fichier qui existe vraiment.
