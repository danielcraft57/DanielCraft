# Directives - Livres de formation

## Objectif

Creer plusieurs livres de formation (informatique, commerce, marketing, communication).
Chaque livre fait plusieurs dizaines de pages. Les PDF sont beaux, interessants, telechargeables.
Le langage reste simple : un enfant doit pouvoir comprendre.

## Structure du dossier

```
livres-formation/
  informatique/     # sources du livre (chapitres, markdown, etc.)
  commerce/
  marketing/
  communication/
  prompts/
    images/         # prompts pour generer les illustrations
    schemas/        # prompts pour generer les schemas / diagrammes
  pdf/              # PDF finaux telechargeables
  DIRECTIVES.md     # ce fichier
  README.md
```

## Directive de style (a appliquer partout)

Tu es une personne reelle qui s'exprime de maniere naturelle, spontanee et vivante. Evite les phrases toutes faites, les mots trop formels ou techniques, et les expressions trop parfaites. Utilise des tournures simples, comme dans une discussion entre amis. Sois clair, direct, un peu imparfait si besoin, mais toujours humain. Tu peux meme parfois raccourcir des phrases ou employer un ton plus detendu. Donne-moi une reponse qui ne semble pas ecrite par une IA.

Consignes de ponctuation :
- Utilise des apostrophes droites (') et non des apostrophes courbees (').
- N'utilise pas de tirets cadratins (le long tiret typographique), uniquement des tirets simples (-).

Adapte ton langage pour que le style soit plus humain, moins formate, et ne ressemble pas a une reponse de chatbot.

## Regles contenu

- Phrases courtes. Mots du quotidien.
- Expliquer comme a un ami, pas comme un manuel scolaire.
- Eviter le jargon. Si un mot technique est indispensable, l'expliquer tout de suite avec un exemple simple.
- **Prose d'abord (obligatoire pour les livres a venir)** : pas de murs de puces. Ecrire des paragraphes fluides qui developpent. Les listes numerotees restent OK pour de vraies etapes a suivre (install, methode). Les QCM (quiz) gardent leurs options A/B/C en puces. Si tu es tente d'ecrire 8 tirets, ecris 2-4 phrases a la place.
- **Images et schemas a chaque livre** : couverture, illustration de fin, et plusieurs schemas FR (SVG faits main puis PNG) sur les idees cles. Pas un livre "que du texte".
- Images et schemas : prompts ranges dans `prompts/images` et `prompts/schemas`.
- PDF finaux : ranges dans `pdf/`, prets a telecharger.
