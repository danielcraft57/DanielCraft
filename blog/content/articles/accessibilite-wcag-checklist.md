---
title: "Accessibilité : checklist WCAG simple (et vraiment utile)"
date: 2025-09-23
excerpt: "Contrastes, navigation clavier, focus, formulaires, ARIA : une checklist concrète pour améliorer l’accessibilité sans devenir expert WCAG du jour au lendemain."
type: article
tags: [accessibilité, WCAG, UX, UI, front-end]
series: ux-ui-serie
series_order: 7
og_image: accessibilite-wcag-checklist-1200x630.jpg
---

# Accessibilité : checklist WCAG simple (et vraiment utile)

L’accessibilité n’est pas un “bonus”. C’est :

- de l’**inclusion**
- de la **qualité**
- souvent du **SEO** et de la **robustesse**

Et surtout : ce n’est pas *si compliqué* si tu commences par les points les plus rentables.

Voici une checklist pragmatique, basée sur les principes WCAG (Perceptible, Utilisable, Compréhensible, Robuste).

---

## 1) Contrastes et lisibilité (Perceptible)

- texte normal : contraste suffisant (idéalement ≥ 4.5:1)
- éviter le gris trop clair sur fond blanc
- taille mini lisible (et ligne pas trop longue)

Astuce : teste au soleil + sur écran moyen.

---

## 2) Focus visible et navigation clavier (Utilisable)

Un utilisateur doit pouvoir :

- naviguer au clavier (Tab, Shift+Tab, Enter, Space)
- voir où il est (focus visible)

Checklist :

- aucun piège clavier (tabulation bloquée dans un modal)
- l’ordre de tabulation est logique
- les éléments cliquables ont un focus distinct

---

## 3) Formulaires : labels, erreurs, aide (Compréhensible)

Formulaire accessible = formulaire clair.

- chaque champ a un **label**
- l’erreur est **liée au champ** et actionnable
- les champs obligatoires sont indiqués
- l’aide (exemple de format) est à proximité

Évite :
- placeholder seul (il disparaît)
- erreurs “génériques” en haut de page

---

## 4) Boutons, liens, zones cliquables

- un lien ressemble à un lien
- un bouton ressemble à un bouton
- une zone cliquable est assez grande (mobile)

Et surtout :
- ne pas utiliser un `<div>` cliquable sans rôle/ARIA et sans clavier

---

## 5) Images et icônes : alt, décoratif, informations

- si l’image est informative : `alt` descriptif
- si décorative : `alt=""` (pour ne pas polluer la lecture)
- icônes seules : `aria-label` sur le bouton/lien

---

## 6) Structure : titres, landmarks, navigation

Pour être “robuste”, la page doit avoir :

- une hiérarchie de titres cohérente (H1 > H2 > H3)
- des zones identifiables (nav, main, footer)
- des liens d’évitement si nécessaire (“aller au contenu”)

---

## 7) Modals, toasts, messages : annoncer les changements

Quand quelque chose apparaît :

- le focus doit aller au bon endroit (modal)
- le contenu doit être annoncé (aria-live pour toasts)

Sans ça, l’utilisateur clavier/lecteur d’écran est perdu.

---

## 8) Le kit de démarrage “80/20”

Si tu ne fais que 8 choses :

1. Contrastes corrects
2. Focus visible partout
3. Navigation clavier complète
4. Labels de formulaire
5. Erreurs actionnables et localisées
6. Boutons/liens sémantiques
7. Alt image correct (ou vide si décoratif)
8. Modals accessibles (focus trap + ESC)

Tu as déjà une accessibilité “sérieuse”.

---

## Conclusion

L’accessibilité, c’est surtout une discipline :  
**faire les bons choix par défaut** (design system + composants accessibles), puis auditer les écrans critiques.

Tu gagnes en qualité pour tout le monde, pas seulement pour une “minorité”.

