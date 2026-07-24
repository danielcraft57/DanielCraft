# Chapitre 16 - Atelier page : assembler une mini landing

Atelier pratique. Objectif : produire une landing one-page complete, propre, responsive, en collant semantique + variables + Grid + formulaire + transitions legeres + focus visible.

C'est le cousin guide du mini-projet. Si tu as deja une home du chapitre 12, tu peux la refondre ici avec un brief plus strict. Sinon, pars de zero.

## Brief

Landing pour un atelier d'une journee (sujet libre : photo, pain, couture, code chez DanielCraft...). Sections obligatoires :

1. Header (marque + nav ancres)
2. Hero (promesse + CTA)
3. Programme (3 etapes en grille)
4. Tarifs (2 cartes cote a cote sur desktop)
5. Inscription (formulaire)
6. Footer

Contraintes : pas de framework, pas d'`absolute` pour le plan general, theme 100 % variables, Tab impeccable.

## Etapes

1. Ecris tout le HTML d'un trait, textes provisoires OK.
2. Pose `:root` (palette + espace + rayon + largeur max).
3. Style le header en Flex.
4. Hero en Grid simple (texte ; optionnellement une image a cote sur desktop).
5. Section programme en `auto-fit` / `minmax`.
6. Section tarifs en `1fr 1fr` puis `1fr` sous 600px.
7. Formulaire labels + focus (chapitre 9).
8. Transitions 200ms sur CTA et cartes.
9. Media `prefers-reduced-motion`.
10. Passe le parcours Tab et corrige.
11. Teste a 320px, 768px, 1200px de large (ou redimensionne a la main).

## Amorce hero + tarifs

```css
.hero {
  display: grid;
  gap: 1.5rem;
  align-items: center;
}

@media (min-width: 800px) {
  .hero {
    grid-template-columns: 1.2fr 1fr;
  }
}

.tarifs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--gap);
}

@media (max-width: 600px) {
  .tarifs {
    grid-template-columns: 1fr;
  }
}
```

Si tu mets une image hero : `object-fit: cover`, `alt` utile, poids raisonnable.

## Contenu minimum

Hero : une phrase nette ("Apprends X en une journee"). Programme : trois titres courts. Tarifs : "Solo" et "Duo" (ou equivalent) avec prix et liste courte. Formulaire : nom, email, choix de date (`select`), bouton.

## Criteres de reussite

On comprend l'offre en cinq secondes.

La page ne casse pas en etroit.

Les ancres du menu amenent aux sections.

Le formulaire est utilisable au clavier.

Changer `--couleur-principale` change clairement la marque.

## Piege a eviter

Trop de sections "nice to have" (temoignages, logos partenaires, FAQ, Instagram...) avant d'avoir le socle. Reste sur le brief. Autre piege : deux boutons dans le hero de meme poids visuel. Un CTA principal suffit.

## Bonus

Ajoute un voile de contraste sur le hero si texte sur image. Ou une pastille "Places limitees" en CSS simple dans une carte tarif (sans absolute si tu peux ; sinon absolute dans la carte en `position: relative`, ok).

## A toi

Livre `landing.html` + `landing.css`. Chronometre 2 heures max pour la premiere version. Ensuite 20 minutes de polish (contrastes, gaps, textes). C'est valide quand tu oseais l'envoyer a un ami pour avis.
