# Chapitre 17 - Choisir une architecture (carte de decision)

Tu n'as pas a inventer une architecture nouvelle. Tu as a choisir une **famille** adaptee. Chez DanielCraft, le prestige d'un papier ne paie pas les faux positifs clients. On part du probleme, on descend vers le moteur - jamais l'inverse.

Ce chapitre consolide ce que tu as traverse : CNN, RNN, transformers, transfer, LLM, ML classique. C'est une carte de decision, pas un catalogue de marques.

:::retenir
Pars du probleme et des contraintes (donnees, calcul, risque, latence). L'architecture suit.
:::

## Ce que ce n'est pas

Ce n'est pas "toujours un LLM". Ce n'est pas "toujours un CNN". Ce n'est pas non plus une verite eternelle : en 2026 les familles evoluent, les principes de matching restent. Et ce n'est pas un permis d'ignorer une baseline simple.

Petit tableau numerique : ML classique d'abord. Images : CNN ou vision transformer preentraine + transfer. Texte generation / chat : LLM existant + prompt / RAG. Series temporelles : modeles specialises ou approches mixtes ; ne force pas un LLM partout. Audio : modeles parole / audio preentraines. Multi-taches complexes : parfois pipelines (vision puis regles puis LLM). Ines range ses sujets dans ces cases avant d'ouvrir un repo.

## Questions de decision

Combien de donnees labellisees ? Quel budget calcul ? Quelle latence acceptable ? Quel besoin d'interpretabilite ? Quel risque d'erreur ? Existe-t-il un modele fondation proche ? Peut-on resoudre sans deep learning ? Lea pose ces questions en reunion ; les reponses changent le devis plus surement qu'un buzzword.

:::astuce
Si tu ne peux pas repondre a "que se passe-t-il si le modele se trompe ?", tu n'es pas pret a choisir l'architecture.
:::

## Anti-patterns

LLM pour classer 3 categories sur un CSV de 20 colonnes. CNN from scratch avec 40 images. Agent autonome le jour 1. Transformer "parce que c'est moderne" sur une serie temporelle ou un modele simple suffit. Pipeline opaque a trois etages sans test de chaque brique. Note tes anti-patterns personnels : ils reviennent.

## Petite histoire

Un client a demande a Lea "un transformer sur nos exports comptables". Elle a montre qu'un modele tabulaire + regles battait un prototype LLM en cout, latence, et auditabilite. Le client a garde le LLM pour rediger des commentaires, pas pour scorer. Deux outils, deux jobs. Max a vecu l'inverse : pour reconnaitre une piece sur photo, le tableur ne suffisait pas ; le CNN transfer oui.

## Erreur classique

Partir d'une architecture parce qu'elle est a la mode. Autre piege : copier l'architecture d'un concurrent sans avoir ses donnees ni son risque. Troisieme : melanger trois familles dans un pipeline sans pouvoir expliquer le role de chacune.

:::attention
Une architecture impressionnante mal evaluee reste une dette. Choisis le minimum qui prouve la valeur.
:::

## En vrai

Prends deux problemes de ton monde. Pour chacun, remplis : famille choisie, raison, alternative, critere d'echec. Dix minutes chrono.

## A toi

Remplis la carte pour 2 problemes. Architecture choisie + raison + alternative + risque principal. Garde-la a cote du plan CNN et de la fiche transformer.

## Pipelines mixtes

Parfois le bon systeme n'est pas "un" reseau. Vision pour classer, regles pour seuils, LLM pour expliquer a un humain. Teste chaque brique, puis l'ensemble. Sam insiste : un pipeline non teste multiplie les hallucinations operationnelles. Chez DanielCraft, on prefere trois briques claires a une boite noire unique adulee.

## Lien avec limites et bonnes pratiques

Choisir une architecture, c'est aussi accepter ses limites (prochain chapitre) et adopter des pratiques sobres (chapitre suivant). La carte de decision n'est complete que branchee sur le risque et la discipline d'execution.

## Scene de reunion

"On veut du deep learning." "Quel probleme ?" "Classer 4 types de tickets texte." "Combien de labels ?" "300." "Baseline TF-IDF ou modele texte preentraine leger d'abord. LLM complet ensuite seulement si besoin d'explication riche." La reunion dure douze minutes. Le prestige du papier n'a pas parle. Chez DanielCraft, c'est une belle reunion.

## Matrice express (a recopier)

Lignes : tableau, image, texte court classif, texte generation, serie temporelle, audio. Colonnes : famille candidate, preentraine ?, besoin GPU, risque erreur, alternative simple. Remplir en 15 minutes change une reunion. Ines l'a fait ; le partenaire a arrete de demander "du GPT sur les colonnes Excel".

## Quand mixer

Vision pour detecter, regle pour seuil, LLM pour expliquer. Chaque fleche du pipeline a un test. Si tu ne peux pas tester une fleche, tu ne la deploies pas seule. Chez DanielCraft, le mixte assume bat le monolithe mystique.
