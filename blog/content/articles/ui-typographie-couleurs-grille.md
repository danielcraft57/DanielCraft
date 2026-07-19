---
title: "Textes, couleurs et alignement : rendre clair"
date: 2025-09-25
excerpt: "Hiérarchie visuelle simple : ce que l'œil comprend en deux secondes."
type: article
tags: [UI, typographie, couleurs, grille, design]
series: ux-ui-serie
series_order: 8
og_image: ui-typographie-couleurs-grille-1200x630.jpg
---

# Textes, couleurs et alignement : rendre clair

Le rendu « pro » d'une interface vient rarement d'une animation complexe. Il vient presque toujours de trois fondamentaux : la typographie, les couleurs, les espaces et la grille. Maîtriser ça, c'est gagner en lisibilité, en cohérence et en confiance. L'utilisateur ne dit pas « belle échelle typo ». Il dit « c'est clair » - ou il abandonne sans savoir pourquoi.

Ces trois leviers communiquent. La typo dit ce qui est important. La couleur dit ce qui est actionnable ou risqué. La grille dit ce qui appartient ensemble. Si l'un des trois part en vrille, l'écran paraît bricolé même avec de beaux composants.

## Typographie : une échelle, pas un buffet

Objectif : scanner l'écran sans effort. Une à deux familles max. Une échelle de tailles stable - par exemple 14 / 16 / 20 / 24 / 32 - plutôt que dix tailles inventées au feeling. Titres courts, paragraphes aérés, longueur de ligne confortable.

Le piège classique : trop de tailles « parce que ce bloc est spécial ». L'œil n'a plus de repères. Autre piège : une police expressive partout. Garde le caractère pour les titres si tu veux, le corps doit surtout se lire. Interligne et tracking comptent autant que la famille : un bon corps avec un mauvais interligne fatigue plus vite qu'une police « moyenne » bien réglée.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/ui-typo-couleur-grille.svg" alt="Schéma UI : typographie, couleurs sémantiques et grille d'espacement" class="schema-inline" width="640" />
  <figcaption>Typo pour hiérarchiser, couleur pour signifier, grille pour aligner - trois leviers, une intention claire.</figcaption>
</figure>

Pour le web produit, la lisibilité bat le spectacle. Tu peux être expressif ailleurs - landing, marketing. Dans l'outil, la typo sert le scan et la tâche.

## Hiérarchie : une intention par zone

[UI](/blog/articles/ux-ui-fondamentaux-differences.html) claire = intention claire. Un bouton primaire visible. Des secondaires plus discrets. Des liens moins importants en texte. Si tout est « important », rien ne l'est - et l'utilisateur hésite.

Sur un écran, demande-toi : quelle est l'action principale ? Tout le reste doit s'effacer un cran. Même logique pour les titres : un H1 qui porte la page, des H2 qui découpent, pas une forêt de titres au même poids. La hiérarchie typographique et la hiérarchie d'action vont ensemble. Sépare-les et tu obtiens des écrans « beaux » mais flous.

## Couleurs : sémantique avant décoration

Une bonne palette sert le sens. `primary` pour l'action principale. `neutral` pour texte, fonds, séparateurs. `success`, `warning`, `danger`, `info` pour les états. Tu peux être très minimaliste et avoir un rendu premium. Tu n'as pas besoin de sept accents.

Évite le rouge « pour mettre en valeur » - rouge = danger dans le mental model de presque tout le monde. Évite aussi de coder la signification uniquement en couleur : un succès sans icône ni texte, un daltonisme ou un écran mal calibré et le message disparaît.



<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/ui-hierarchie-visuelle.svg" alt="Schema de hierarchie visuelle typographie couleur grille" class="schema-inline" width="640" />
  <figcaption>Typo + couleur + grille = une hierarchie que l'oeil comprend en 2 secondes.</figcaption>
</figure>

Contraste : teste en conditions réelles - mobile dehors, écran moyen, soirée fatigue. Un gris clair peut être élégant en Figma et inutilisable en usage. La couleur n'est pas de la déco. C'est un signal. Traite-la comme telle.

## Espaces : la moitié de la perception qualité

Les marges et paddings font une part énorme de la sensation « soigné » vs « bricolé ». Choisis une échelle - 4 / 8 / 12 / 16 / 24 / 32 - et tiens-toi-y. Un spacing incohérent fatigue l'œil même si les couleurs sont justes.

Regroupe ce qui va ensemble, sépare ce qui doit se distinguer. Trop d'air partout, l'écran se dilue. Pas assez, tout se colle. L'échelle te donne des crans : tu n'improvises plus « 13px parce que ça rentrait ».

Dans un [design system](/blog/articles/design-system-composants-tokens.html), ces espaces deviennent des tokens. Même bénéfice que pour les couleurs : cohérence, thèmes, moins de débats pixel.

## Grille : alignement = confiance

Sur le web, une grille (12 colonnes ou plus simple) aide à aligner, à rester cohérent en responsive, à éviter les décalages qui fatiguent. Même sans grille formelle, pense lignes invisibles : titres alignés, champs alignés, boutons alignés.

Le responsive n'est pas « tout empiler ». C'est décider comment la grille se contracte : quelles colonnes fusionnent, quels blocs passent l'un sous l'autre, quels espacements restent stables. Une UI qui « saute » entre breakpoints donne une impression d'instabilité - même si le contenu est bon.

L'alignement rassure. Le désalignement, même subtil, donne une sensation amateur. Les utilisateurs ne te le formuleront pas. Ils le sentiront.

## Vingt minutes pour améliorer un écran

Identifie l'action principale. Réduis le bruit - enlève un ou deux éléments inutiles. Unifie autour de deux tailles de police (titre / corps) plus éventuellement un label. Applique l'échelle d'espaces. Vérifie le contraste du texte. Recale sur la grille.

Tu verras un gain immédiat, souvent plus fort qu'une nouvelle illustration ou une micro-animation. Parce que tu as traité la communication visuelle, pas le vernis.

Si tu travailles en équipe, formalise ces règles en tokens et en guidelines courtes. La prochaine personne n'aura pas à « sentir » la bonne densité. Elle aura une échelle. C'est comme ça que la qualité UI survit au turnover et aux sprints chargés.

## Densité : ni vide, ni étouffement

La densité dépend du contexte. Un outil métier dense peut être légitime si les utilisateurs y passent des heures et connaissent le domaine. Une landing ou un parcours grand public a besoin d'air. Le piège, c'est d'appliquer la même densité partout « pour la cohérence ». Cohérence de tokens, oui. Cohérence de densité aveugle, non.

Quand tu doutes, augmente d'abord l'espace autour de l'action principale et du message d'erreur. Réduis le bruit secondaire. Tu clarifies sans tout « aérer » artificiellement. Et si un écran paraît vide, ce n'est pas toujours un manque de contenu - parfois c'est une hiérarchie trop plate, où rien ne capte l'œil.

## Travailler avec le contenu réel

Les faux textes « Lorem » mentent. Un titre produit de douze mots casse la ligne que tu avais prévue. Un label long pousse le bouton. Un message d'erreur verbeux déborde. Dès que tu peux, conçois avec du contenu réel ou réaliste - y compris les cas limites. La typo et la grille se jugent là, pas sur une maquette idéale.

Pareil pour les langues : si tu internationalises, prévois de la place. L'allemand ou le français long ne rentrent pas dans la même boîte que l'anglais court. Une grille trop serrée sur le happy path anglais te le rappellera en prod.

## Trois leviers, un métier

Typo, couleurs et grille ne sont pas de la décoration. Ce sont des outils de communication : ils guident l'attention, clarifient les actions, rendent le produit fiable. Commence par une échelle typo, une palette sémantique courte, une échelle d'espaces et un alignement honnête. Le reste - effets, motion, détails - vient après, quand la hiérarchie tient déjà debout.
