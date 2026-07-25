# Chapitre 1 - Salut, c'est quoi le deep learning ?

Le **deep learning**, c'est une famille de machine learning qui utilise des **reseaux de neurones artificiels** a plusieurs couches. "Deep" veut dire profond : entre l'entree (pixels, sons, tokens de texte) et la sortie (classe, nombre, prochain mot), il y a beaucoup d'etages de transformation. Ces modeles ont casse des plafonds sur l'image, la voix, puis le langage. Les **LLM** dont on parle tous les jours sont, sous le capot, des architectures de deep learning specialisees - souvent des **transformers**.

Chez DanielCraft, on ne commence pas par les equations. On commence par l'intuition : empiler des filtres qui apprennent a reconnaitre des motifs de plus en plus abstraits. Sur une photo, ca peut aller des bords aux formes, puis aux objets. Sur du texte, des fragments aux structures, puis a des intentions probables. Tu n'as pas besoin de reinventer un laboratoire. Tu as besoin d'une carte mentale solide pour dialoguer avec des outils, des prestataires, et plus tard du code.

:::retenir
Deep learning = reseaux a plusieurs couches qui apprennent aussi des representations, pas seulement une decision finale.
:::

## Ce que ce n'est pas

Ce n'est pas une conscience. Ce n'est pas "toujours mieux que le ML classique". Sur un petit tableau de dix colonnes numeriques, un modele scikit-learn simple gagne souvent. Ce n'est pas non plus un cluster de GPU obligatoire pour comprendre : tu peux saisir l'essentiel avec du papier, des exemples, et un peu de pratique. Et ce n'est surtout pas une excuse pour deployer sans validation, sans metriques, sans plan si le modele se trompe.

Ce n'est pas non plus "un seul produit". CNN pour la vision, transformers pour le langage, modeles audio, pipelines mixtes : meme famille large, usages differents. On va les demeler sans jargon opaque.

## Image mentale

Tu as une entree brute. Le reseau la transforme couche apres couche en une representation plus utile, puis en une decision. En ML classique, tu ciselais souvent les **features** a la main. En deep learning, les couches apprennent aussi des features internes. Cette automatisation a un prix : opaqueite, besoin de donnees et de calcul, risque d'**overfitting**. Le jeu n'en vaut la chandelle que si le probleme le demande - image, parole, texte long, motifs trop riches pour un tableur.

:::idee
Note un probleme "image ou texte" ou le deep learning semble pertinent, et un probleme "petit tableau" ou un modele simple suffit. Cette distinction te suivra tout le livre.
:::

## Fil rouge : Ines

Ines developpe une appli qui reconnait des pieces detachees sur photo. Elle veut aussi comprendre comment les assistants texte fonctionnent, parce que ses clients lui posent des questions et qu'elle refuse de repondre "c'est de la magie". Lea, freelance web, l'ecoute pour mieux briefer ses prestataires IA. Max, artisan, veut juste savoir pourquoi "l'IA photo" se trompe sur un chantier mal eclaire. Sam, enseignant, cherche des analogies claires pour ses eleves. Quatre regardes, une meme carte.

## Ce que tu vas savoir faire

Dans ce livre : neurone, couches, activations, idee simple de la **backprop**, **CNN**, **RNN** (overview), transformers, overfitting en deep learning, idee des **GPU**, **transfer learning**, lien avec les LLM, ateliers, choix d'architecture, limites, bonnes pratiques, quiz. Tu sortiras capable d'expliquer a un ami comment ca marche "en gros", et de ne pas te faire impressionner par un jargon vide.

Niveau debutant solide. Pas besoin de coder pour comprendre le debut. Besoin de curiosite et d'honnetete : le deep learning aide ; il ne remplace pas ta verification ni ton jugement metier.

## Petite histoire

Ines avait 180 photos de pieces, prises au telephone sous un neon jaune. Un collegue lui a dit "entraine un gros reseau from scratch, c'est du deep learning". Elle a perdu une semaine, obtenu 98 % sur le train et 41 % sur des photos nouvelles. Puis elle a bascule vers un modele preentraine, quelques couches adaptees, et une validation sur le vrai terrain. Le score a baisse sur le train. Le produit a commence a servir. Chez DanielCraft, on celebre ce genre de retournement : moins de theatre, plus de generalisation.

## Erreur classique

Croire que deep learning = toujours mieux. Ou croire qu'il faut un cluster de GPU pour comprendre. Autre piege : confondre "on a mis du deep learning" avec "le probleme est resolu". Quand tu entends cette phrase, pose les questions du livre : combien de donnees ? preentraine ou from scratch ? quelle validation ? quel budget calcul ? quel comportement hors distribution ? quel plan si le modele se trompe ?

:::attention
"Deep" n'est pas un concours de profondeur. C'est un compromis entre signal, donnees, calcul et regularisation.
:::

## En vrai

Prends un probleme de ton monde. Ecris en deux colonnes : "deep learning possible ?" et "modele simple suffit ?". Si tu hesites, c'est deja un progres : tu ne colles plus l'etiquette IA partout.

## A toi

Ecris un probleme image ou texte ou le deep learning semble pertinent, et un probleme petit tableau ou un modele simple suffit. Une phrase de justification pour chaque. Garde ce papier : les ateliers y reviendront.

## Deep learning vs ML classique

Sur un CSV metier propre, le ML classique reste souvent le bon premier reflexe. Sur une image brute (des milliers de pixels) ou du texte long, le deep learning brille parce qu'il apprend aussi des representations. En 2026, les deux coexistent dans les memes produits. Choisir, c'est matcher le probleme, pas suivre la mode.

## Ce que "50 pages" doivent changer chez toi

A la fin, tu ne seras pas chercheur. Tu seras quelqu'un qui sait ce qu'est un neurone, pourquoi on active non lineairement, comment l'erreur remonte pour ajuster les poids, pourquoi un CNN aime l'image, pourquoi un transformer aime le contexte, pourquoi l'overfitting frappe fort, pourquoi le GPU accelere, pourquoi le transfer learning est le geste 2026, et comment un chat LLM se branche sur tout ca. C'est deja beaucoup. C'est surtout actionnable demain matin.
