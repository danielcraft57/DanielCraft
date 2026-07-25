# Chapitre 19 - Petites habitudes de performance

Pas besoin de devenir expert performance web pour eviter les betises couteuses. Quelques gestes changent deja beaucoup sur les mini-apps de ce livre : moins de travail inutile, moins de requetes spam, une attente qui parait moins longue parce qu'elle est expliquee. Chez DanielCraft, on prefere une appli simple et stable a une appli "optimisee" illegible avec des micro-hacks partout.

Lea optimise apres mesure, pas avant. Max evite surtout les erreurs grossieres. Sam rappelle : lisibilite d'abord. Ce chapitre est une boussole, pas un manuel d'ingenieur perf.

## Moins de travail inutile

Ne recree pas toute la liste HTML si un seul titre change : mets a jour l'element concerne. Ne relance pas un fetch a chaque pixel de scroll sans debounce ou sans vraie raison. Ne charge pas une image geante pour une icone de 32 pixels. Si tu as deja les donnees en memoire, filtre localement au lieu de redemander au serveur a chaque lettre (debounce plus cache, chapitre 18). La perf, ce n'est pas "aller plus vite a tout prix". C'est "ne pas gaspiller". Un fetch inutile, c'est du gaspillage. Un DOM detruit et recree entier pour un changement minuscule, idem. Un spinner infini sans message, c'est du gaspillage de confiance utilisateur.

## DOM : batch mental

Quand tu ajoutes 50 elements, construis-les en memoire puis ajoute-les (DocumentFragment ou append en une fois). Evite d'alterner lecture et ecriture du DOM dans une boucle serree si tu n'y es pas oblige : chaque toucher au DOM peut declencher du recalcul layout. Pour 10 li dans un exercice, ce n'est pas critique. Pour 500, ca se voit.

## Reseau

Affiche un squelette ou "Chargement..." pour que l'attente soit digeste psychologiquement. Gere les erreurs au lieu de laisser tourner indefiniment. Evite les fetch en double : si un chargement est en cours, desactive le bouton ou ignore le second clic. Debounce les recherches live. Cache en variable session ce qui ne change pas pendant la visite (liste deja chargee).

## Code lisible d'abord

Optimiser un code confus, c'est peindre une voiture sans moteur. D'abord clair (modules, noms, gestion erreurs). Ensuite mesure si tu sens la lenteur. Ensuite optimise le vrai goulot. Les outils navigateur (onglet Performance, Network avec waterfall) existent pour ca. Ne devine pas au hasard.

## Petite histoire

Max avait un bouton "Actualiser" qui relancait fetch a chaque clic nerveux du client. Trois requetes identiques en deux secondes. Lea a ajoute un flag enChargement et desactive le bouton pendant le fetch. Meme donnees, moins de charge, meilleure impression pro.

## Erreur classique

Optimiser prematurement : micro-refactor obscur pour gagner 2 ms. Ignorer le reseau : 50 fetch par seconde sur une recherche. Oublier l'UX de l'attente : pas de feedback = "ca marche pas ?". Confondre perf et complexite : plus de code != plus rapide.

## En vrai

Relis ton mini-projet ou atelier fetch. Cherche un seul gaspillage concret (fetch en double, pas de debounce sur filtre, liste recreee entierement a chaque filtre mineur). Corrige ce seul point. Mesure au feeling avant/apres. Un fix vaut mieux que dix conseils theoriques. Ouvre Network une fois : compte les requetes. Le chiffre ancre mieux qu'un sentiment.

## A toi

Note un gaspillage trouve et comment tu l'as corrige (ou compte le corriger). Si tu n'en trouves aucun, fais relire ton code a quelqu'un ou relis-le demain matin avec des yeux neufs. Il y en a presque toujours un. Bonus : ecris le gaspillage en une phrase dans le README du projet - pour ton futur toi.

## Mesurer sans obsession

Onglet Network : combien de requetes au chargement ? Quelle taille du JSON ? Performance : une interaction lente est-elle due au JS ou au layout ? Tu n'as pas besoin de maitriser ces outils a fond. Tu as besoin de regarder une fois pour calibrer ton intuition. Lea ouvre Network quand un client dit "c'est lent" : souvent, c'est six images non compressees, pas le fetch.

## Accessibilite et perf

Un bouton desactive pendant chargement evite double clic ET annonce visuellement l'attente. Un message texte vaut mieux qu'un spinner seul pour les lecteurs d'ecran basiques. Ce n'est pas le coeur du chapitre, mais DanielCraft aime les apps qui ne stressent pas l'utilisateur. Perf percue, c'est aussi clarte.

## Priorites pour ce niveau

1) Pas de fetch spam (debounce). 2) Pas de DOM reconstruit sans raison. 3) Feedback chargement/erreur. 4) Code decoupe lisible. 5) Optimisations micro seulement si mesure prouve le goulot. Max suit cette liste. Sam la met au tableau. Si tu fais deja 1 a 4, tu es large pour les projets de ce livre. Chez DanielCraft, on repete : ne pas gaspiller bat "optimiser pour le plaisir".
