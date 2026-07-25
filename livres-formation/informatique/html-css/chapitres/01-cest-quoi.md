# Chapitre 1 - Salut, c'est quoi une page web ?

Une page web, ce n'est pas un document magique tombe du ciel. Ce n'est pas non plus "Internet" en entier. C'est un fichier (ou plusieurs) que ton **navigateur** lit, puis affiche. Tu ecris des instructions. Chrome, Firefox, Edge ou Safari les interpretent. Toi, tu vois un titre, un texte, une image, un bouton. Derriere, il y a du code. Chez DanielCraft, on aime commencer simple : avant de devenir "developpeur", tu apprends a parler deux langues de base du web - **HTML** et **CSS**.

Le HTML, c'est la structure. Les murs, les pieces, les portes. Il dit : ici un titre, ici un paragraphe, ici une image, ici un formulaire. Le CSS, c'est l'apparence. La peinture, les rideaux, l'espace entre les meubles. Il dit : ce titre est grand et vert, ce fond est doux, ce bouton a des coins ronds. Sans HTML, il n'y a rien a regarder. Sans CSS, ca marche, mais c'est souvent moche - texte noir sur fond blanc, zero atmosphere. Les deux marchent ensemble. Toujours. Tu restes le pilote. Le navigateur affiche.

En 2026, quand quelqu'un dit "j'ai fait une page web", il parle le plus souvent de ca : un fichier HTML, un peu de CSS, parfois une image. Derriere, il y a des builders, des CMS, des frameworks. Pour toi, le geste reste le meme : ecrire, sauvegarder, ouvrir, corriger. Tu comprends ce que tu touches. Tu n'es plus spectateur d'un outil opaque.

:::retenir
HTML = structure. CSS = apparence. Navigateur = guide. Toi = auteur.
:::

## Ce que ce n'est pas

Ce n'est pas un logiciel a installer pour "faire un site" en cliquant partout. Ce n'est pas non plus **JavaScript** : JS viendra plus tard pour rendre la page interactive. Ce n'est pas "mettre du bleu dans le HTML" : la couleur, c'est le job du CSS. Et ce n'est surtout pas un truc reserve aux genies. Lea, freelance web, reconstruit des pages clients tous les jours avec ces bases. Max, artisan plombier, a fait sa page vitrine avec un titre, trois photos, et un formulaire contact. Sam, enseignant, montre a ses eleves que le web, c'est d'abord de l'ordre et de la clarte.

Ce n'est pas non plus "Internet" magique. Une page locale sur ton disque, c'est deja une page web. Pour la mettre en ligne, il faudra un hebergement - plus loin. D'abord, tu apprends a ecrire. Ensuite, tu partages.

Imagine une maison. Le HTML pose les pieces. Le CSS decide si c'est cosy ou clinique. Le navigateur, c'est le guide qui te fait entrer et te montre le salon. Quand tu ouvres un site, tu lances ce guide. Il lit le code. Il te montre la page. Tu ecris du texte special. Lui, il transforme. Plus loin dans ce livre, on ajoutera balises, liens, images, formulaires, couleurs, boites, Flexbox, responsive. Pas pour te noyer. Pour que tu saches ce que tu manipules.

Lea dit : "structure d'abord, style ensuite". Max a grave ca apres avoir melange les deux trop tot. Sam dessine la maison au tableau : murs HTML, peinture CSS, visiteurs = navigateur. Les eleves comprennent en dix minutes ce que des heures de jargon n'expliquent pas.

## Ce que tu vas savoir faire

A la fin, tu sauras creer une vraie page web. Tu y mettras du texte, des images, des liens, des listes, un formulaire. Tu changeras couleurs et polices. Tu rangeras les blocs. Tu penseras telephone. Puis un mini-projet, un recap, des ateliers, l'accessibilite, un quiz, et un bravo. Niveau debutant solide. Pas besoin d'etre "tech". Besoin de curiosite et de patience : tu modifies, tu sauvegardes, tu rafraichis. Cinq minutes actives valent mieux qu'une heure passive.

## Comment lire ce livre

Lis dans l'ordre au debut. Les premiers chapitres posent le sol. Les ateliers font faire. Le quiz verifie. A chaque fin, il y a un "A toi". Fais-le. Chez DanielCraft, on forme des gens qui livrent petit, souvent, proprement - pas des collectionneurs de tutos oublies. Tu peux revenir ensuite a un chapitre precis (Flexbox, responsive, formulaires) comme a une fiche. Le livre est un atelier, pas une encyclopedie a lire d'une traite sans les mains.

## Petite histoire

Lea devait livrer une page "A propos" pour un fleuriste. Avant, elle ouvrait un builder, cliquait partout, et ne savait plus ou etait le vrai contenu. Maintenant, elle ecrit d'abord le HTML : titre, trois paragraphes, photo, lien contact. Ensuite seulement le CSS : fond creme, titre vert, image arrondie. Quarante minutes, page nette. Le client comprend. Lea assume.

Max, lui, voulait "juste une page avec mon numero". Il a commence par coller du style partout dans le HTML. Ca cassait. Un ami DanielCraft lui a dit : structure d'abord, style ensuite. Il a recommence. Trois soirs. Sa page tient sur telephone. Les clients appellent. Ce n'est pas de la magie. C'est de la methode.

## Erreur classique

Croire que HTML sert a rendre une page jolie. Beaucoup cherchent "comment mettre du bleu" dans le HTML. Autre piege : croire que "c'est trop technique pour moi" apres dix minutes. Souvent, le probleme n'est pas toi. C'est le melange trop tot : style, structure, et trop d'outils d'un coup. Commence nu. Habiller ensuite. Autre piege : vouloir un site "pro" des le soir 1. Une page claire avec un titre et deux paragraphes bat une maquette jamais finie.

:::attention
Ne cherche pas la couleur dans le HTML. Structure d'abord. Le CSS habille apres.
:::

## En vrai

Ouvre un site que tu visites souvent. Clic droit, Inspecter (ou F12). Clique une ligne HTML. Repere une regle CSS a droite. Note une chose structuree et une chose stylee. Tu viens de lire du vrai code, sans installer quoi que ce soit. Puis imagine ta propre page en trois mots : sujet, contenu, ambiance. Tu poses le terrain pour le chapitre suivant.

## A toi

Ecris en trois phrases : (1) une page que tu aimerais avoir (perso, artisan, classe, hobby), (2) ce que tu veux y mettre comme contenu, (3) ce que tu aimerais rendre joli ensuite. Garde ce papier. On y revient au mini-projet. Chez DanielCraft, ce petit brief vaut plus qu'une heure de tutorials flous.

## Exemple pour voir la difference

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Structure vs style</title>
  <style>
    body { font-family: sans-serif; background: #f0f0f0; margin: 0; padding: 20px; }
    h1 { color: #1a5f4a; }
    .carte { background: white; padding: 16px; border-radius: 8px; }
  </style>
</head>
<body>
  <div class="carte">
    <h1>Ma page</h1>
    <p>Le HTML dit : c'est un titre, c'est un paragraphe.</p>
    <p>Le CSS dit : fond gris clair, titre vert, carte blanche.</p>
  </div>
</body>
</html>
```

Copie, sauvegarde, ouvre. Tu vois deja la difference entre structure et style. Dans ce livre, on demonte ca piece par piece, avec Lea, Max et Sam comme compagnons de route - et DanielCraft comme fil : petit, clair, testable.
