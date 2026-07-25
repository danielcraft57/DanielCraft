# Chapitre 13 - A retenir (carte mentale)

Si tu ne devais garder qu'une page de ce livre, ce serait celle-ci. JavaScript cote navigateur, au-dela des bases, c'est surtout : faire parler ta page avec le monde exterieur sans mentir a l'utilisateur quand ca charge ou quand ca casse. Tu valides, tu envoies ou tu recois du JSON, tu attends proprement, tu decoupes ton code, tu debogues avec methode.

Chez DanielCraft, on dit souvent : les gestes battent les listes de methodes. Relis cette carte avant un atelier, avant un ticket front, avant de paniquer sur une 404. Lea la garde ouverte. Max la recopie a sa main. Sam la projette cinq minutes en debut de seance. Trois usages, une meme colonne vertebrale.

## Les idees solides

Formulaires : preventDefault, trim, validation claire, messages humains, focus sur le champ en erreur. JSON : parse pour lire du texte recu, stringify pour envoyer. fetch GET : demander une ressource. fetch POST : envoyer un body JSON avec method, Content-Type et stringify. Promesses : then pour le succes, catch pour l'echec, return dans la chaine. async/await : meme flux, ecriture lineaire, try/catch autour des await. Erreurs : response.ok obligatoire, message simple a l'ecran, console.error pour le detail. Modules : export/import, type="module", un role par fichier. Organisation : main orchestre, api reseau, afficher DOM. Debug : une hypothese a la fois, console et Network. CORS : regle navigateur entre origines, pas un bug JS magique. Debounce : attendre un silence avant d'agir. Perf : pas de fetch spam, pas de DOM inutile.

:::retenir
"Pas d'exception ne veut pas dire succes ; undefined n'est pas une liste ; [object Object] n'est pas du JSON."
:::

## La boucle DanielCraft

1) Evenement utilisateur. 2) Validation locale. 3) Etat "chargement" visible. 4) fetch avec await. 5) Verifier ok. 6) json(). 7) Afficher ou envoyer. 8) catch avec message humain. 9) Decouper en fichiers des que ca grossit.

C'est la meme boucle pour Lea sur un formulaire contact, pour Max sur sa meteo locale, pour Sam sur une liste de citations. Les donnees changent. Le geste reste.

## Ce que tu peux oublier

Le nom exact de chaque API publique de demo. La syntaxe parfaite du premier coup. La peur du rouge dans la console. Garde les gestes. Change d'outil ou d'API si besoin. Les gestes restent.

## Petite checklist de poche

Ai-je preventDefault sur le submit ? Ai-je stringify avant POST ? Ai-je verifie ok ? Ai-je un message si ca rate ? Ai-je un "Chargement..." ? Mon fichier depasse-t-il 200 lignes sans decoupe ? Si oui partout sauf le dernier point, tu es solide pour un petit projet reel.

## Personnages, meme logique

Lea valide puis POST. Max affiche la meteo avec catch. Sam charge des listes pour ses quiz. Trois metiers, un schema : lire, verifier, agir, expliquer l'echec.

## Phrase talisman

"Pas d'exception ne veut pas dire succes ; undefined n'est pas une liste ; [object Object] n'est pas du JSON." Garde-la. Elle resume les trois bugs les plus frequents de ce livre.

## Petite histoire

Lea a voulu tout retenir d'un coup. Elle a bloque. Elle a affiche cette carte au-dessus de l'ecran et a refait le squelette async + fetch a voix haute. Max a saute response.ok "parce que ca marchait en demo" : page blanche chez le client. Sam a force une URL cassee en classe : les eleves ont enfin vu le catch. Trois lecons, une carte. Chez DanielCraft, on prefere une carte tenue a une memoire heroique.

## Erreur classique

Croire que "j'ai lu" egal "je sais assembler". Sans livrable (mini-projet, atelier), le cerveau classe ca comme "vu", pas comme "su". Autre piege : collectionner les chapitres sans jamais casser volontairement une URL. Tu ne verras jamais ton vrai catch.

:::attention
Sans tester l'echec, tu n'as qu'une moitie de competence. Casse l'URL. Verifie le message. Remets.
:::

## En vrai

Sans regarder le livre, ecris de memoire le squelette async + fetch + ok + json + catch. Chronometre cinq minutes. Compare a tes notes. Les trous montrent ce qu'il faut relire avant les ateliers. Puis coche la checklist de poche sur ton dernier script.

## A toi

Recopie cette carte sur papier en 12 lignes max, avec TES mots. Puis ecris de memoire le squelette async + fetch + ok + json + catch. Compare a tes notes. Les trous montrent ce qu'il faut relire avant les ateliers.

## Note de rythme

Prends le temps. Un atelier fait a fond vaut mieux que trois ateliers survoles. Si tu es presse, fais la moitie aujourd'hui et l'autre demain - mais ecris le livrable. Sans livrable, le cerveau classe ca comme "lu", pas comme "su". DanielCraft forme des gens qui livrent, meme petit.

## Pour aller plus loin sans te perdre

Tu n'as pas a tout maitriser d'un coup. Reviens a ce chapitre quand tu butes sur un cas reel (CORS, POST, module qui ne charge pas). Relis l'erreur classique du chapitre concerne. Refais le "A toi". Chez DanielCraft, on prefere trois relectures actives a une lecture passive de vingt pages. Si un paragraphe te semble encore flou, reformule-le a voix haute avec ton propre exemple (meteo, contact, produits). Des que ca passe a l'oral, c'est que c'est entre.
