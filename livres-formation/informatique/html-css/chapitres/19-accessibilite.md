# Chapitre 19 - Accessibilite et bonnes manieres

**Accessibilite**, ca veut dire : le plus de gens possible peuvent utiliser ta page, quel que soit leur corps, leur materiel ou leur fatigue. Y compris avec un clavier seul, un lecteur d'ecran, un contraste faible, un doigt epais, une connexion lente, ou une fin de journee ou tu plisses les yeux. Pas besoin d'etre expert certifie. Juste quelques reflexes honnetes des le debut.

Chez DanielCraft, ce n'est pas un chapitre "moralisateur" qu'on survole. C'est du professionnalisme concret. Lea le vend comme de la qualite : "votre site sera lisible par plus de monde". Max l'a compris quand un client age a dit "enfin je peux lire sans loupe". Sam le note dans ses grilles avec autant de serieux que le HTML. Tu as deja des bases : **`alt`**, labels, titres ranges, viewport. Ici, on solidifie. En 2026, quand quelqu'un dit "c'est accessible", il parle souvent de ces reflexes. Tu restes le pilote. Le soin se voit.

:::retenir
`alt` utile. Contraste ok. Liens explicites. Titres ranges. Zones cliquables confortables. Labels presents.
:::

## Ce que ce n'est pas

Ce n'est pas "faire moche au nom de l'accessibilite". Souvent, accessible = plus clair, donc plus beau utile. Ce n'est pas une certification WCAG complete en un chapitre. Ce n'est pas non plus mettre `alt=""` partout sans reflechir : decoratif vs informatif, tu choisis consciemment. Une image purement decorative peut avoir un alt vide. Une photo de produit, non. Lea refuse les `alt="image"`. Sam raye les "clique ici".

Tu invites du monde chez toi. Certains voient bien, d'autres moins. Certains utilisent la souris, d'autres la touche Tab. Certains lisent dehors au soleil. Tu n'eteins pas la lumiere "parce que c'est design sombre et premium". Tu gardes des chemins praticables. Ta page est une maison hospitaliere, pas un club prive. Max dit : "si mon oncle ne peut pas lire, j'ai rate". Sam fait Tab les yeux detournes. Lea projette un mauvais contraste : personne ne lit du fond de la salle.

```html
<img src="chat.jpg" alt="Chat orange assis sur un canape gris">
```

Pas `alt="image"`. Pas `alt="photo1"`. Lea ecrit des **`alt`** comme des legendes courtes. Max decrit "camion de depannage devant la maison a Lyon". Sam demande de lire les alt a voix haute : si ca ne decrit rien, c'est a refaire.

## Contraste, liens, boutons, titres

Texte gris tres clair sur fond blanc = fatigue et exclusion. Texte sombre sur fond clair = mieux. Si tu plisses les yeux, change. Liens : evite "clique ici", prefere "Voir les tarifs" ou "Appeler Max". Boutons : assez grands sur telephone (environ 40px de haut). Titres : **`h1`** puis **`h2`** puis **`h3`**, sans sauter des niveaux juste pour la taille. Chez DanielCraft, ces regles sont du soin, pas du luxe.

:::astuce
Teste Tab sur ta page avant de dire "c'est fini". Si tu te perds au clavier, un lecteur d'ecran se perdra aussi.
:::

## Clavier et checklist rapide

Essaie Tab : tu dois atteindre tous les liens et boutons importants dans un ordre logique. Si tu te perds, simplifie. Mini checklist : `alt` utiles, contraste ok, liens explicites, titres ranges, zones cliquables confortables, viewport, labels. Corriger trois points sur ta page perso, c'est deja un vrai plus professionnel.

## Petite histoire

Lea a livre un site "premium" en gris tres pale. Audit : contraste insuffisant. Correction : texte plus sombre, boutons plus nets, liens soulignes. Le client a dit "moins luxe". Puis ses utilisateurs ages ont repondu plus vite. Il a garde la version accessible. Max a remplace "clique ici" par "Appeler Max au 06..." : plus d'appels. Sam projette un mauvais contraste : personne ne lit. Trois scenes, une lecon.

## Erreur classique

Aller trop loin dans le "design pale". Oublier le clavier. Mettre du texte important uniquement dans une image. Croire que l'accessibilite, "c'est pour plus tard". Plus tard, c'est plus cher, et tu as deja perdu des visiteurs. Autre piege : `alt=""` sur une image informative pour "faire plaisir au validateur". Choisis consciemment.

## En vrai

Reprends ta page perso. Corrige trois points : un `alt` plus precis, un meilleur contraste, un lien plus explicite. Teste Tab du debut a la fin. Lis tes `alt` a voix haute. Si ca decrit vraiment, tu as gagne. Sinon, reecris. Cinq minutes de soin valent une heure de deco inutile.

## A toi

Ecris ta checklist accessibilite en six lignes et colle-la pres de ton ecran (ou en commentaire HTML en tete de page). Prochaine page que tu construis, tu l'utilises avant de dire "c'est fini". Reflexe DanielCraft : accessible n'est pas optionnel, c'est du soin apporte au travail. Tu en es capable des maintenant.
