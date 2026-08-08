# Directives - Livres de formation

## Objectif

Creer plusieurs livres de formation (informatique, commerce, marketing, communication, IA, finance).
Chaque livre fait plusieurs dizaines de pages. Les PDF sont beaux, interessants, telechargeables.
Le langage reste simple : un enfant doit pouvoir comprendre.

## Structure du dossier

```
livres-formation/
  informatique/
  commerce/
  marketing/
  communication/
  ia/
  finance/
  prompts/
    images/
    schemas/
  pdf/
  DIRECTIVES.md
  README.md
```

## Directive de style (a appliquer partout)

Tu es une personne reelle qui s'exprime de maniere naturelle, spontanee et vivante. Evite les phrases toutes faites, les mots trop formels ou techniques, et les expressions trop parfaites. Utilise des tournures simples, comme dans une discussion entre amis. Sois clair, direct, un peu imparfait si besoin, mais toujours humain. Tu peux meme parfois raccourcir des phrases ou employer un ton plus detendu. Donne-moi une reponse qui ne semble pas ecrite par une IA.

**Public** : beaucoup de lecteurs ne sont pas informaticiens. Sur le site DanielCraft (pages marketing), zero jargon. Dans les livres formation, expliquer progressivement - ne jamais assumer que le lecteur « connait deja ».

**IA (DanielCraft)** : Loic utilise l'IA depuis 2025 (expertise prompts), livraisons souvent plus rapides - voir `docs/POSITIONNEMENT_IA.md` et `AGENTS.md`.

Consignes de ponctuation :
- Utilise des apostrophes droites (') et non des apostrophes courbees (').
- N'utilise pas de tirets cadratins (le long tiret typographique), uniquement des tirets simples (-).

Adapte ton langage pour que le style soit plus humain, moins formate, et ne ressemble pas a une reponse de chatbot.

## Regles contenu

- Phrases courtes. Mots du quotidien.
- Expliquer comme a un ami, pas comme un manuel scolaire.
- Eviter le jargon. Si un mot technique est indispensable, l'expliquer tout de suite avec un exemple simple.
- **Prose d'abord (obligatoire)** : paragraphes fluides de plusieurs phrases. Une idee se developpe. Pas de mur de puces. Pas de suite de mini-phrases sechees (une ligne = une idee isolee). Laisse une ligne vide entre deux paragraphes.
- **Mots-cles en gras** : mets en `**gras**` les notions importantes a la premiere occurrence utile (ex. **prompt**, **marge**, **branche**). Pas tout le paragraphe en gras. 3 a 8 gras par chapitre suffisent.
- **Callouts / notes pedagogiques** (1 a 3 par chapitre, pas plus).
  Chaque note = 1 a 3 phrases utiles, concretes, pas de slogan. Evite de coller la meme note sur plusieurs chapitres.
  Trois types seulement :

```md
:::retenir
La phrase cle du chapitre (une idee a emporter).
:::

:::attention
Un piege concret a eviter.
:::

:::astuce
Un geste pratique a tester tout de suite.
:::
```

- Preferer `:::retenir` + `:::attention` (et une `:::astuce` si besoin).
- **Interdit** : `:::idee`, `:::exemple`, et toute note decorative ou slogan. Les exemples concrets vont dans la prose ou dans Petite histoire.
- **Modele de chapitre** (reference : JS bases / IA generative ch.1) :
  1. Ouverture riche (2-4 paragraphes)
  2. **Schema obligatoire** (figure claire FR, injectee apres le H1 via `CHAPTER_IMAGES`)
  3. Sections utiles au fil du texte : Ce que ce n'est pas, Petite histoire, Erreur classique, En vrai, A toi
  4. Personnages concrets qui reviennent (Lea, Max, Sam...)
  5. DanielCraft mentionne naturellement
- **Interdit** : section titree "Image mentale" (et variantes). L'intuition passe par le **schema** + la prose, pas par un titre fixe.
- Listes numerotees OK pour de vraies etapes. Quiz : options A/B/C en puces.
- **Images et schemas** :
  - Couverture + felicitation.
  - **Schema obligatoire** par chapitre (cours, ateliers, quiz inclus ; SVG FR -> PNG via `CHAPTER_IMAGES`). Caption courte en francais. Preferer un schema clair a une rangee d'emojis.
  - **Exemples images generes** (optionnels) : oui, on peut en mettre **quelques-uns** (environ 2 a 5 par livre, sur les chapitres ou ca aide vraiment). Scene pedagogique concrete (ex. Lea devant la console, Max qui clique un bouton, ecran avec erreur lue). Caption FR. Ces images **completent** le schema, elles ne le remplacent pas. Pas une illustration a chaque chapitre (cout + PDF trop lourd).
  - **Placement des visuels** (obligatoire) :
    1. Schema juste sous le H1 (carte / idee du chapitre).
    2. Scene generee **au milieu** du chapitre pour aerer le texte - injecter **avant** `## Petite histoire` (sinon avant Erreur classique / En vrai / A toi). Ne pas empiler schema + scene sous le titre.
  - Fichiers scene : prefixe clair (ex. `js-scene-*.png`, `js2-scene-*.png`) pour que le build les distingue des schemas.
  - Tout texte visible dans une image = **francais uniquement**.
- **Workflow** : un livre a la fois. Rebuild PDF, commit cible, puis enchaîner le suivant (pas d'agents paralleles multi-livres).
- PDF finaux dans `pdf/`.

## Lecture et comprehension (bonnes pratiques)

- Gras = priorite visuelle pour l'essentiel (pas de soulignement).
- Callouts = notes utiles hors du fil (retenir / attention / astuce), jamais decoratives.
- Un schema = une idee visuelle par chapitre (pas trois schemas inutiles).
- Quelques scenes generees = ancrage emotionnel / exemple vivant, pas decoration. Placees au milieu pour aerer, jamais empilees sous le titre avec le schema.
- Repeter une idee avec une histoire concrete apres l'explication abstraite.
- Terminer par une micro-action ("A toi") pour ancrer.
