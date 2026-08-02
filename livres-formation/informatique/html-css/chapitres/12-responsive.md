# Chapitre 12 - Un site qui marche sur telephone

La plupart des gens regardent le web sur mobile. En 2026, ignorer le telephone, c'est ignorer la moitie de tes visiteurs - souvent plus. Si ta page est illisible sur un ecran etroit, c'est rate, meme si elle est parfaite sur ton grand moniteur de bureau. Le **responsive**, ce n'est pas un bonus qu'on ajoute a la fin quand on a le temps. C'est une politesse envers celui qui lit dans le metro, dans sa cuisine, ou sur son canape avec un pouce epais.

Chez DanielCraft, Lea livre toujours en testant une largeur etroite avant de dire "c'est fini". Max a perdu un client parce que son numero de telephone etait coupe hors ecran : le visiteur a abandonne sans appeler. Sam commence ses demos en mode telephone pour montrer que le web, ce n'est pas seulement un grand ecran devant une classe. Trois metiers, une meme lecon : pense doigt, pense petit ecran, pense des le debut. Tu restes le pilote. L'ecran etroit revele tes erreurs.

La base technique, c'est la balise **viewport** dans le `<head>`. Sans elle, le telephone croit souvent que ta page fait la largeur d'un grand ecran et zoom de facon horrible. Avec elle, le navigateur adapte la largeur a l'appareil. Mets-la. Toujours. Avant le reste.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

:::retenir
Viewport dans le head. Images en `max-width: 100%`. Menu qui s'empile. Teste a 360px aussi.
:::

## Ce que ce n'est pas

Ce n'est pas "faire un deuxieme site" separe pour mobile. Tu ajustes le meme HTML avec du CSS adapte. Ce n'est pas seulement une **media query** copiee-collee : les largeurs souples, les images fluides et les boutons assez grands comptent autant. Ce n'est pas ignorer le doigt : une zone cliquable minuscule, c'est une punition quotidienne pour tes visiteurs. Et ce n'est surtout pas tester uniquement sur ton PC en declarant victoire sans jamais reduire la fenetre.

Ce n'est pas non plus "responsive = media query uniquement". Sans viewport, sans images fluides, la media query ne sauve rien. Lea le verifie dans cet ordre : viewport, images, menu, boutons, scroll horizontal.

Pense a une valise. Sur grand ecran, tu deplies tout : menu en ligne, image large, texte aere. Sur telephone, tu plies sans jeter le contenu. Le menu passe peut-etre en colonne. L'image ne debord pas sur le cote. Le texte reste lisible sans zoom permanent avec deux doigts. Tu adaptes le contenant, tu gardes le message. Le responsive, c'est de la diplomatie visuelle. Max dit : "ma page doit tenir dans une poche". Sam fait sortir les eleves avec leur telephone. Lea projette le mode F12 avant/apres.

```css
img {
  max-width: 100%;
  height: auto;
}

.conteneur {
  width: min(100% - 2rem, 700px);
  margin-inline: auto;
}

.menu {
  display: flex;
  gap: 1rem;
}

@media (max-width: 600px) {
  .menu {
    flex-direction: column;
  }
}
```

Traduction : les images ne debordent jamais. La boite centrale ne depasse pas 700px. En dessous de 600px, le menu s'empile. Tu peux changer le seuil selon ton design. Le principe reste le meme. Chez DanielCraft, on valide avec les doigts, pas seulement avec les yeux.

## Tailles de doigt et vrais tests

Vise une zone cliquable confortable : environ 40 pixels de haut minimum pour un bouton ou un lien important. Reduis la fenetre du navigateur. Ouvre F12 et le mode telephone. Teste a 360px de large, pas seulement a 800px. Si tu peux, regarde sur un vrai telephone plus tard : rien ne remplace le doigt reel. Lea garde une checklist : viewport, images fluides, texte lisible, boutons assez grands, pas de scroll horizontal.

:::attention
Sans viewport, le telephone "zoome" comme si ta page etait un grand ecran. Ajoute la meta. Toujours. Avant le reste du CSS responsive.
:::

## Petite histoire

Max avait une belle page sur son ordinateur. Sur mobile, il fallait scroller lateralement pour lire une seule phrase. Honte douce quand un client lui a envoye une capture avec "je vois rien". Viewport + `max-width: 100%` + menu en colonne sous 600px : repare en une soiree. Lea montre aux clients le mode responsive avant/apres : ca convainc plus qu'un discours. Sam note "oublie viewport" comme erreur classique numero un. Les eleves qui l'oublient reviennent toujours la corriger en premier. Trois scenes, une checklist.

## Erreur classique

Oublier le viewport. Ensuite : images en largeur fixe qui debordent, boutons trop petits pour un doigt, media query avec le mauvais selecteur. Tester seulement a 1200px et declarer victoire. Le scroll horizontal, c'est presque toujours un element coupable : une image, une largeur fixe, un padding oublie. Autre piege : texte trop petit "parce que ca fait moderne". Sur telephone, ca fait "je ne lis pas".

:::astuce
Ouvre ta page en mode telephone F12. Scrolle horizontalement. Si ca bouge sur le cote, tu as un probleme a trouver avant de continuer.
:::

## En vrai

Ajoute le viewport si ce n'est pas fait. Passe ton menu en colonne sous 600px avec une media query. Redimensionne la fenetre. Cherche le scroll horizontal. S'il existe, inspecte element par element jusqu'a trouver le coupable. Souvent c'est une image ou une `width` fixe. Corrige. Reteste a 360px. Tu valides vraiment.

## A toi

Ecris ta checklist mobile perso en cinq lignes (viewport, images, texte, boutons, scroll horizontal) et applique-la a ta page en cours. Coche chaque point. Ce papier vaut plus qu'une theorie relue dix fois. Chez DanielCraft, on valide avec les doigts, pas seulement avec les yeux sur un ecran large. Tu prepares le mini-projet : une page qui tient partout.
