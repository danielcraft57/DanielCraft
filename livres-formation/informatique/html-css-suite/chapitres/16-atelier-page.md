# Chapitre 16 - Atelier page : assembler une mini landing

Atelier pratique. Objectif : produire une landing one-page complete, propre, responsive, en collant semantique + variables + Grid + formulaire + transitions legeres + focus visible. C'est le cousin guide du mini-projet. Si tu as deja une home du chapitre 12, tu peux la refondre ici avec un brief plus strict. Sinon, pars de zero.

Chez DanielCraft, une landing reussie tient en une promesse claire, un parcours simple, et une inscription sans friction. Lea en livre souvent pour des ateliers clients. Max en aurait besoin pour un stage "plomberie du dimanche" s'il se lanait. Sam en fait construire une par binome en fin de module. Meme squelette, trois vies.

## Ce que ce n'est pas

Ce n'est pas un site multi-pages. Ce n'est pas non plus le moment d'ajouter temoignages, logos partenaires, FAQ, fil Instagram et chat flottant. Socle d'abord. Autre chose que ce n'est pas : deux boutons dans le hero de meme poids visuel. Un CTA principal suffit. Si tout crie, rien ne guide.

## Brief obligatoire

Landing pour un atelier d'une journee (sujet libre : photo, pain, couture, code...). Tu arrives, tu comprends l'offre en cinq secondes, tu vois le programme, tu compares deux tarifs, tu t'inscris. Sur telephone, rien ne casse. Au Tab, tu sens chaque etape. Les couleurs viennent du `:root`. Si tu changes `--couleur-principale`, la marque suit.

Sections : (1) Header (marque + nav ancres), (2) Hero (promesse + CTA), (3) Programme (3 etapes en grille), (4) Tarifs (2 cartes cote a cote sur desktop), (5) Inscription (formulaire), (6) Footer. Contraintes : pas de framework, pas d'`absolute` pour le plan general, theme 100 % variables, Tab impeccable.

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

Si tu mets une image hero : `object-fit: cover`, `alt` utile, poids raisonnable. Un voile de contraste si texte sur photo.

:::retenir
Une promesse claire, un parcours simple, une inscription sans friction. Theme 100 % variables. Tab impeccable. Socle avant les "nice to have".
:::

## Contenu minimum et criteres

Hero : une phrase nette ("Apprends X en une journee"). Programme : trois titres courts. Tarifs : "Solo" et "Duo" (ou equivalent) avec prix et liste courte. Formulaire : nom, email, choix de date (`select`), bouton.

Criteres : on comprend l'offre en cinq secondes ; la page ne casse pas en etroit ; les ancres du menu amenent aux sections ; le formulaire est utilisable au clavier ; changer `--couleur-principale` change clairement la marque.

## Petite histoire

Lea a chronometre deux heures chrono pour une premiere version "atelier photo argentique". La premiere heure a tout pose. La seconde a corrige contrastes, gaps, textes. Elle a envoye a un ami : "c'est clair, j'irais". Max a regarde la meme page et a dit "je trouve le prix, je trouve le bouton". Sam a valide le binome des que le Tab passait sans accroc - meme si une carte etait encore un peu pale. Les priorites comptent.

:::attention
Trop de sections "nice to have" avant d'avoir le socle. Hero a 3 Mo. Formulaire sans labels "parce que le placeholder suffit". Ancres cassees parce que les `id` ne matchent pas. Verifie chaque lien du menu a la main.
:::

## Erreur classique

Deux CTA de meme poids dans le hero. Peaufiner des ombres pendant trois heures sans tester le parcours. Oublier `prefers-reduced-motion`.

## En vrai

Coupe le Wi-Fi mental des reseaux sociaux. Met un timer 2 heures. Premiere version uniquement. Ensuite 20 minutes de polish. Si tu depasses trois heures a peaufiner des ombres, tu es sorti du brief. Reviens au parcours : comprendre, comparer, s'inscrire.

## Bonus

Pastille "Places limitees" dans une carte tarif (la carte en `position: relative` si besoin). Ou un second theme via classe, comme a l'atelier variables. Optionnel.

## A toi

Livre `landing.html` + `landing.css`. C'est valide quand tu oserais l'envoyer a un ami pour avis. Ecris ensuite trois retours possibles que tu redoutes (trop long, prix flou, formulaire penible) et corrige le plus probable avant d'envoyer vraiment. Chez DanielCraft, oser envoyer bat peaufiner sans fin.
