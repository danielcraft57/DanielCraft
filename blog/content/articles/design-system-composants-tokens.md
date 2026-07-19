---
title: "Design system : les briques pour rester cohérent"
date: 2025-09-18
excerpt: "Composants, tokens et adoption : une bibliothèque vivante, pas un dossier fantôme."
type: article
tags: [UI, design system, composants, tokens, front-end]
series: ux-ui-serie
series_order: 6
og_image: design-system-composants-tokens-1200x630.jpg
---

# Design system : les briques pour rester cohérent

Sans design system, chaque feature réinvente l'interface. Un bouton un peu différent. Un espacement « au feeling ». Un état d'erreur inventé à la va-vite. Au début ça passe. Puis l'équipe grossit, les écrans se multiplient, et tu te retrouves avec une dette visuelle qui ralentit tout le monde - design, front, QA. Le produit ne paraît plus fragile parce qu'il est mal codé. Il paraît fragile parce qu'il n'est plus cohérent.

Un design system n'est pas une galerie Dribbble. Ce n'est pas non plus un dump de composants « jolis ». C'est un système de production : des valeurs nommées, des briques réutilisables, des règles d'usage, et quelqu'un qui décide quand ça bouge. L'objectif n'est pas la beauté pure. C'est réduire le coût de décision à chaque écran.

## Ce que c'est vraiment (et ce que ce n'est pas)

Un design system utile tient en quatre couches. Les tokens : couleurs, tailles, rayons, espacements, typo. Les composants : bouton, champ, modal, table, toast. Les guidelines : quand utiliser quoi, patterns de formulaire, [accessibilité](/blog/articles/accessibilite-wcag-checklist.html). La gouvernance : qui décide, comment on versionne, comment on contribue.

Ce que ça n'est pas : un fichier Figma figé que personne n'ouvre, une bibliothèque de 80 composants dont 60 ne sont jamais utilisés, ou un « kit [UI](/blog/articles/ux-ui-fondamentaux-differences.html) » copié sans règles. Si le système ne change pas la façon de livrer, ce n'est qu'une vitrine.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/design-system-tokens.svg" alt="Schéma design system : tokens primitifs, sémantiques et composants" class="schema-inline" width="640" />
  <figcaption>Primitifs → sémantiques → composants : une source de vérité qui se propage partout.</figcaption>
</figure>

## Tokens : la seule vérité

Un token, c'est une valeur nommée. `color.text.primary`. `space.4`. `radius.md`. `font.size.sm`. Tu ne codes plus « #2563eb » dans cinquante endroits. Tu codes l'intention.

La puissance arrive quand tu sépares primitifs et sémantiques. Les primitifs, c'est la palette brute : `color.blue.600`, `space.4 = 16px`. Les sémantiques, c'est l'intention UI : `color.action.primary`, `color.danger`, `text.body`. Les composants consomment le sémantique : `Button.primary.bg`, `Input.border`, `Alert.error`.

Pourquoi ça change la vie ? Tu bascules light/dark sans tout casser. Tu synchronises Figma et code. Tu évites le piège des noms techniques (`blue500`) qui ne disent rien au produit. Un token sémantique dit « à quoi ça sert ». Un primitif dit « quelle valeur brute ». Les deux ont leur place - dans cet ordre.

Petit conseil : commence avec peu de tokens, bien nommés. Une échelle d'espaces, une échelle de typo, une palette sémantique courte. Tu élargiras. Un catalogue de 200 tokens dès le jour 1, c'est souvent de la procrastination déguisée en rigueur.

## Composants : prêts pour la vraie vie

Un composant utile n'est pas une maquette au repos. Il gère les états : default, hover, active, disabled. L'accessibilité : focus visible, clavier, ARIA quand c'est nécessaire. Les variants : tailles, intents (primary, secondary, danger). Les comportements : loading, erreurs, validations.

Un bouton « pro », concrètement : état loading qui empêche le double clic, largeur stable pour ne pas sauter, focus clavier lisible, message de succès ou d'échec clair. Si ton bouton n'existe que dans l'état « beau au repos », il te lâchera en prod - et les utilisateurs le sentiront avant toi.



<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/design-system-adoption.svg" alt="Schema des couches d'adoption d'un design system" class="schema-inline" width="640" />
  <figcaption>Tokens et composants ne suffisent pas : il faut une vraie adoption.</figcaption>
</figure>

Documente aussi empty, error, success. Beaucoup d'équipes livrent le happy path et découvrent les autres états en incident. Le design system, c'est le endroit où ces états deviennent le défaut, pas l'exception.

## Guidelines : éviter l'UI au hasard

Même avec de bons composants, sans guidelines les écrans divergent. Qui décide s'il y a un ou deux boutons primaires ? Où s'affichent les erreurs de formulaire ? Quelle densité pour une table ?

Capture les décisions récurrentes. Une action primaire par zone. Labels visibles, pas placeholder seul. Erreurs proches du champ et actionnables. Tables : tri, pagination, filtres avec des règles stables. Tu ne rédiges pas un roman. Tu écris les choix que l'équipe refait toutes les semaines.

Les guidelines vivent mieux près du code - Storybook, MDX, page « Patterns » - que dans un Confluence oublié. Si personne ne les trouve en cinq secondes, elles n'existent pas.

## Gouvernance : sinon ça meurt

Un design system sans owner devient un cimetière de forks. Chacun crée sa variante « juste pour ce ticket ». Trois mois plus tard, tu as quatre boutons primary différents et zéro confiance.

Il te faut un owner (même partiel), un process de contribution simple, des règles de compatibilité, des releases avec changelog. Versionner comme un produit : breaking changes annoncés, migrations documentées, pas de « on a tout changé en silence ».

La gouvernance n'est pas de la bureaucratie. C'est ce qui empêche le système de pourrir. Et c'est ce qui donne le droit de dire non à une variante inutile - poliment, avec une alternative.

## Workflow dev : sinon ça reste du design

Storybook pour la doc vivante. Tests visuels pour les régressions. Tokens exportés (JSON, CSS variables) utilisés vraiment dans le front. Lint ou conventions UI pour éviter le hors-piste. Le système accélère quand il est dans le flux de livraison, pas à côté.

Le couple gagnant : designer et développeur co-owners sur les composants critiques. Pas « design livre, front interprète ». Co-construction. Sinon tu recrées le même écart Figma/code que tu voulais supprimer.

Intègre aussi l'accessibilité dans les stories : focus, clavier, labels. Un composant « beau » mais inaccessible n'est pas un composant de design system. C'est une dette déguisée.

## Par où commencer (sans se noyer)

Ne vise pas le « grand système » d'un coup. Tokens de base + cinq composants critiques (bouton, input, select, modal, toast) + guidelines formulaires. Puis itère comme un produit : backlog, releases, feedback équipe.

Mesure ce qui compte : temps pour livrer un écran standard, nombre de variantes hors système, bugs UX liés à l'incohérence. Si ces indicateurs ne bougent pas, ton design system est encore une vitrine.

Le design system n'a de valeur que s'il rend le produit plus cohérent, accélère la livraison et réduit les bugs d'interface. Le reste - le branding du système, le site de doc ultra-soigné - peut attendre. Commence petit, versionne, gouverne. La cohérence à l'échelle, ça se construit comme une feature : intentionnellement, pas par accumulation.
