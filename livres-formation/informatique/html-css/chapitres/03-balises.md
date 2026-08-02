# Chapitre 3 - Les balises, c'est des etiquettes

Une **balise**, c'est une etiquette. Elle dit au navigateur : ce bout de texte, c'est un titre ; celui-la, c'est un lien ; celui-ci, c'est une image. Sans etiquettes, le navigateur voit une soupe de mots. Avec des etiquettes, il construit une page. Chez DanielCraft, on repete souvent : HTML, ce n'est pas "ecrire joli". C'est nommer correctement ce que tu montres. Lea etiquette avant de styler. Max etiquette avant de chercher la couleur. Sam demande le sens avant la taille.

La forme generale est simple. Tu ouvres, tu mets un contenu, tu fermes : `<nom>contenu</nom>`. Exemple : `<strong>Important</strong>` met le mot en gras parce que tu as dit "important", pas seulement parce que c'est plus gros. En 2026, quand quelqu'un dit "j'ai mis des balises", il parle souvent de cette hygiene. Derriere, il y a des centaines de balises HTML. Pour toi, une poignee suffit. Tu restes le pilote. L'etiquette oriente.

:::retenir
Balise = sens. Attribut = detail. Ouvre, contenu, ferme - sauf les balises seules.
:::

## Ce que ce n'est pas

Ce n'est pas du CSS. Une balise ne "fait pas joli" par mission premiere : elle donne du **sens**. Ce n'est pas non plus une liste infinie a apprendre par coeur ce soir. Une poignee de balises te mene deja loin. Et ce n'est pas "plus de balises = meilleure page". Trop d'etiquettes inutiles, c'est du bruit. Un `div` partout "parce que ca marche" cache souvent un manque de reflexion.

Ce n'est pas non plus du JavaScript. Les balises decrivent. Elles ne calculent pas, ne verifient pas un mot de passe, ne chargent pas des donnees toutes seules. Structure d'abord. Comportement, plus tard. Lea le rappelle aux clients impatients de "faire bouger" avant d'avoir un plan clair.

Tu ranges une cuisine. Tu colles des etiquettes : farine, sucre, sel. Le navigateur est le cuisinier. S'il lit "farine" sur le sucre, le gateau rate. Pareil sur une page : si tu mets un titre dans un `div` vague juste pour la taille, tu mens un peu a la machine - et aux lecteurs d'ecran, et a Google. Dis la verite structurelle. Habiller, ce sera le CSS. Max a compris le jour ou un lecteur d'ecran a lu sa page "n'importe comment" parce que tout etait en `div`. Sam fait coller des post-its sur des bouts de papier avant d'ecrire une ligne de code.

## Quelques balises utiles tout de suite

Tu vas croiser `h1` a `h6` pour les titres (`h1` le plus important), `p` pour un paragraphe, `a` pour un lien, `img` pour une image, `ul` / `ol` / `li` pour les listes, `div` pour une boite generique, `span` pour un petit bout dans une phrase, `br` pour un retour a la ligne. Tu n'as pas a tout maitriser d'un coup. Tu as a reconnaitre le motif : ouvrir, contenu, fermer - sauf pour quelques balises seules.

```html
<h1>Mon titre</h1>
<p>Un paragraphe avec un mot <strong>important</strong>.</p>
<a href="contact.html">Contact</a>
```

## Balises seules (pas de fermeture)

Certaines n'ont pas de contenu a enfermer. `<br>` va a la ligne. `<img src="photo.jpg" alt="Une photo">` affiche une image. Tu ne fermes pas comme un paragraphe. Tu donnes des **attributs**, et c'est tout. `<meta charset="UTF-8">` dans le head est pareil : une instruction, pas un bloc de texte. Lea dit : "pas de contenu a enfermer, pas de balise fermante". Sam fait lever la main : "qui fermerait un `img` ?" Personne, apres deux semaines.

## Attributs : des infos en plus

Dans une balise, tu ajoutes des details. `<a href="https://exemple.com">Clique ici</a>` : `href` est l'adresse. Sur une image, `src` est le chemin, `alt` est la description si l'image ne charge pas - utile aussi pour l'accessibilite. Les attributs ne sont pas de la deco. Ce sont des instructions precises. Max a gagne des appels avec un simple `href="tel:..."`. Lea refuse les `alt=""` vides sur des images importantes.

Exemple concret : `<a href="contact.html">Contact</a>` - la balise dit "lien", `href` dit ou ca mene, le texte dit ce que le visiteur lit. Trois infos, une seule etiquette.

## HTML, c'est de l'ordre

Le navigateur lit de haut en bas. Ce que tu mets en premier apparait en premier (sauf si le CSS change l'ordre plus tard). Range ton code. **Indente**. Lea dit que l'indentation lui a fait gagner des heures de debug. Max a appris apres avoir cherche une balise non fermee pendant une soiree entiere. Sam refuse les fichiers "en ligne" sans retours : l'oeil ne voit plus rien. Chez DanielCraft, un fichier indente n'est pas du luxe. C'est de la survie.

:::astuce
Indente d'un cran a chaque ouverture de balise. Tes yeux trouvent les erreurs plus vite.
:::

## Petite histoire

Sam a donne un exo : "page avec un titre, deux paragraphes, un mot important". Un eleve a tout mis dans des `div` et a force la taille en CSS colle n'importe ou. Ca marchait "un peu". Puis le lecteur d'ecran a lu n'importe comment. Sam a fait recommencer avec `h1`, `p`, `strong`. Meme contenu. Meilleure page. Lea, sur un audit client, retrouve souvent ce piege : joli a l'oeil, flou pour la machine.

Max avait mis son numero dans un `p` sans lien. Les visiteurs copiaient-coliaient mal. Un `<a href="tel:0612345678">` plus tard, les appels ont monte. Bonne balise, bon attribut, bon resultat. Trois scenes, une lecon : l'etiquette juste change la vie de la page.

## Erreur classique

Oublier de fermer une balise. Ecrire `</p>` sans avoir ouvert `<p>`. Mettre un `h1` parce que "c'est plus gros" alors que tu voulais juste un sous-titre. Si la page a l'air cassee, regarde d'abord les ouvertures et fermetures. Respire. Corrige. Rafraichis. Autre piege : inventer des noms de balises (`<titre>`, `<texte>`). Le navigateur ne reconnait que le vocabulaire HTML. Lea dit : "tu ne inventes pas le francais ; tu ne inventes pas le HTML".

:::attention
Ne choisis pas une balise pour sa taille par defaut. Choisis-la pour son sens. La taille, c'est le CSS.
:::

## En vrai

Ecris une page avec un `h1`, deux `p`, et un mot en `<strong>`. Ouvre-la. Puis ajoute un `span` autour d'un mot sans style : tu verras que sans CSS, `span` ne change presque rien - c'est normal. C'est une poignee pour plus tard. Ajoute un commentaire `<!-- section contact -->` : il ne s'affiche pas, il t'aide. Relis ton fichier a voix haute en nommant chaque balise. Le reflexe s'ancre.

## A toi

Fais la meme page "Ma journee en etiquettes" : un titre, trois phrases, un mot important, et une note en commentaire HTML `<!-- ... -->` pour toi. Le commentaire ne s'affiche pas. Il te parle. Comme un post-it invisible. Relis ton code a voix haute en nommant chaque balise : "titre, paragraphe, important". Ca ancre le reflexe DanielCraft. Garde ce fichier pour le chapitre texte.
