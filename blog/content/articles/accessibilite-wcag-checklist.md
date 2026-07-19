---
title: "Accessibilité : pour que tout le monde puisse utiliser"
date: 2025-09-23
excerpt: "Une checklist WCAG utile : contraste, clavier, labels — et des tests qui comptent."
type: article
tags: [accessibilité, WCAG, UX, UI, front-end]
series: ux-ui-serie
series_order: 7
og_image: accessibilite-wcag-checklist-1200x630.jpg
---

# Accessibilité : pour que tout le monde puisse utiliser

L'accessibilité n'est pas un bonus à coller en fin de sprint. C'est de l'inclusion, de la qualité, souvent du SEO et de la robustesse. Et surtout : ce n'est pas si intimidant si tu vises les gains les plus rentables avant de plonger dans chaque critère WCAG.

Les principes POUR (Perceptible, Operable, Understandable, Robust) donnent une boussole. Les niveaux A, AA, AAA disent jusqu'où tu vises. Pour la plupart des produits, AA est la cible réaliste. AAA, c'est excellent sur certains critères - pas un objectif magique sur tout.

## Perceptible : ce qu'on voit et ce qu'on entend

Commence par le contraste. Texte normal : vise au moins 4.5:1. Évite le gris trop clair sur blanc - joli en maquette, illisible au soleil ou le soir. Taille lisible, longueur de ligne raisonnable. Teste sur un vrai mobile, pas seulement sur ton écran retouché.

Images : si elles portent une info, un `alt` descriptif. Si elles décorent, `alt=""` pour ne pas polluer le lecteur d'écran. Icônes seules dans un bouton : un `aria-label` clair. Les sous-titres et alternatives textuelles pour l'audio/vidéo suivent la même logique - l'info doit pouvoir passer ailleurs que par un seul canal.

<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/accessibilite-wcag.svg" alt="Schéma accessibilité WCAG : principes POUR et niveaux A, AA, AAA" class="schema-inline" width="640" />
  <figcaption>Quatre principes POUR, trois niveaux de conformité - AA comme cible, tests clavier et contraste en priorité.</figcaption>
</figure>

Tu n'as pas besoin d'être expert contraste pour commencer. Un checker, deux corrections sur les textes secondaires, et tu as déjà débloqué une part énorme des problèmes « je n'arrive pas à lire ».

## Operable : clavier, focus, pas de piège

Un utilisateur doit pouvoir tabuler, activer avec Entrée ou Espace, et surtout voir où il est. Le focus visible n'est pas un détail esthétique. C'est la boussole de navigation.

Checklist courte. Ordre de tabulation logique. Pas de piège clavier dans une modal (tu dois pouvoir sortir, notamment avec Échap). Zones cliquables assez grandes sur mobile. Liens et boutons qui ressemblent à ce qu'ils sont - un `<div>` cliquable sans rôle, sans clavier, sans focus, c'est une porte déguisée en mur.

Beaucoup de bugs « accessibilité » sont en réalité des bugs d'interaction. Si tu navigues au clavier sur ton parcours critique une fois par sprint, tu les trouves tôt - avant le support, avant l'audit.

## Understandable : formulaires et messages clairs

Un formulaire accessible, c'est d'abord un formulaire compréhensible. Chaque champ a un label visible. Les erreurs sont liées au champ et disent comment corriger. Les obligatoires sont indiqués. L'aide (format attendu) est à proximité, pas cachée dans une FAQ.

Évite le placeholder seul : il disparaît dès qu'on tape, et il ne remplace pas un label. Évite aussi l'erreur générique en haut de page (« formulaire invalide ») sans pointer quoi ni où. L'utilisateur n'a pas à jouer au détective.



<figure class="schema-figure">
  <img src="/assets/images/blog/schemas/a11y-tests.svg" alt="Schema des niveaux de test accessibilite WCAG" class="schema-inline" width="640" />
  <figcaption>Checklist + tests clavier + humains : l'auto ne suffit jamais.</figcaption>
</figure>

La lecture claire, c'est aussi le langage. Moins de jargon technique dans les messages. Des phrases courtes. Un modèle mental stable : si « Enregistrer » veut dire la même chose partout, tu réduis la charge cognitive pour tout le monde - pas seulement pour les lecteurs d'écran.

## Robust : structure et technologies d'assistance

HTML valide, hiérarchie de titres cohérente (un H1, puis H2/H3 sans sauter au hasard), landmarks (nav, main, footer). Un lien « aller au contenu » aide quand la navigation est longue. ARIA seulement quand le HTML natif ne suffit pas - et correctement, sinon tu dégrades l'expérience AT au lieu de l'améliorer.

Quand quelque chose apparaît - modal, toast, message d'erreur dynamique - gère le focus et l'annonce. Focus dans la modal à l'ouverture, retour au déclencheur à la fermeture. `aria-live` pour les toasts utiles. Sans ça, clavier et lecteur d'écran se perdent alors que la souris « voit » encore.

## Le kit 80/20 (si tu ne fais que ça)

Huit points. Contrastes corrects. Focus visible partout. Navigation clavier complète sur les parcours clés. Labels de formulaire. Erreurs actionnables et localisées. Boutons et liens sémantiques. Alt image (ou vide si décoratif). Modals accessibles (focus trap + Échap).

Avec ça, tu as déjà une accessibilité sérieuse - bien avant d'avoir lu les 50+ critères WCAG. Le reste vient ensuite, écran par écran, critère par critère, quand le socle tient.

## Comment auditer sans se noyer

Automatise ce qui s'automatise (contraste, certaines règles ARIA, structure). Puis teste à la main : clavier seul, un lecteur d'écran sur un parcours critique, zoom 200 %. Les outils attrapent des symptômes. Les humains trouvent les parcours cassés.

Ne vise pas un audit géant une fois par an. Préfère un passage court à chaque feature critique : inscription, paiement, demande de devis, espace client. Cinq minutes de Tab + un check contraste sur les textes secondaires valent mieux qu'un rapport PDF que personne n'ouvre. Note les bloquants dans le ticket, pas dans un fichier à part - sinon ils ne rentrent jamais dans le sprint.

Intègre l'accessibilité dans le [design system](/blog/articles/design-system-composants-tokens.html) : composants corrects par défaut. C'est plus efficace que de « corriger l'a11y » après chaque feature. Et forme l'équipe à deux réflexes : « je peux le faire au clavier ? » et « le message d'erreur aide-t-il à corriger ? ».

## Prioriser sans tout faire d'un coup

Tu n'auras pas AA parfait demain. Classe par impact : parcours à fort trafic ou à fort risque (argent, données personnelles, inscription). Corrige d'abord ce qui empêche d'accomplir la tâche - focus invisible, modal piège, label manquant, contraste illisible. Les polishs viennent ensuite.

Si tu dois convaincre un décideur, parle résultats : moins de tickets « je n'arrive pas à… », meilleure complétion mobile, conformité progressive. L'accessibilité n'est pas seulement éthique. C'est du produit robuste. Et souvent, les correctifs aident aussi les utilisateurs sans handicap déclaré - soleil, fatigue, une main occupée, mauvais réseau.

L'accessibilité, c'est surtout une discipline. Faire les bons choix par défaut, puis auditer les écrans critiques. Tu gagnes en qualité pour tout le monde - fatigue, soleil, bras occupé, situation temporaire - pas seulement pour une « minorité ». Commence par POUR, vise AA, applique le kit 80/20. Le reste se construit sprint après sprint.
