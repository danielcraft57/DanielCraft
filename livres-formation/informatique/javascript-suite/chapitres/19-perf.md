# Chapitre 19 - Petites habitudes de performance

Pas besoin de devenir expert perf pour eviter les betises couteuses. Quelques gestes changent deja beaucoup.

## Moins de travail inutile

Ne recree pas toute la liste HTML si un seul titre change. Ne relance pas un fetch a chaque pixel de scroll. Ne charge pas une image geante pour une icone.

## Dom : batch mental

Quand tu ajoutes 50 elements, construis-les puis ajoute-les (ou utilise un fragment). Evite d'alterner lecture et ecriture du DOM dans une boucle serree si tu n'y es pas oblige : ca peut ralentir.

## Reseau

Cache ce qui ne change pas pendant la session si c'est pertinent. Affiche un squelette ou "Chargement..." pour que l'attente soit digeste. Gere les erreurs au lieu de laisser tourner indefiniment.

## Code lisible d'abord

Optimiser un code confus, c'est peindre une voiture sans moteur. D'abord clair. Ensuite mesure. Ensuite optimise le vrai goulot. Les outils navigateur (Performance, Network) existent pour ca.

## En vrai

Pour les projets de ce livre, la perf "suffisante" c'est : reponse humaine, pas de boucle folle, pas de spam reseau. DanielCraft prefere un app simple et stable a une app "optimisee" illegible.

## A toi

Relis ton mini-projet. Cherche un seul gaspillage (fetch en double, logs en rafale, grosse image). Corrige ce seul point.
